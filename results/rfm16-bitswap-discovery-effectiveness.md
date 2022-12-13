# RFM-16: Effectiveness of Bitswap Discovery Process

Author: [Guillaume Michel](https://github.com/guillaumemichel)

Date: 2022-12-13

## Table of contents

1. [Motivation](#motivation)
2. [Measurement Methodology](#measurement-methodology)
    - [CIDs selection](#cids-selection)
    - [Kubo](#kubo)
    - [go-bitswap](#go-bitswap)
    - [Logs](#logs)
    - [Running measurements](#running-measurements)
    - [Technical Limitations](#technical-limitations)
3. [Results and Analysis](#results-and-analysis)
4. [Improvement suggestions](#improvement-suggestions)
5. [Conclusion](#conclusion)

## Motivation

Bitswap is the data exchange protocol for IPFS. Whenever a new CID is requested to [`kubo`](https://github.com/ipfs/kubo), a new Bitswap session will start, and the node will broadcast requests for the CID to its directly connected peers. If the file isn’t discovered in `ProviderSearchDelay` seconds, Bitswap starts a DHT walk to discover the providers of the file identified by the CID. If the DHT walk returns some providers, Bitswap will connect to them and ask them to transfer the file identified by the CID.

At the time of writing, Bitswap has a `ProviderSearchDelay` variable set to 1 second by default. This means that, unless the node is already directly connected to the content provider, the request to discover and fetch the content will be delayed by a second, which is far from ideal as IPFS targets sub-second data delivery. We would like to provide a better value for the `ProviderSearchDelay` whose value has been arbitrarily selected until now.

This study aims at measuring the effectiveness of the Bitswap discovery process, or in other words how efficient is Bitswap as a content discovery protocol. The performance of Bitswap discovery is the ratio of requests succeeding before the DHT walk starts. We also measure the time distribution of the successful Bitswap requests, and the number of packets sent by Bitswap for each requested CID. 

Assuming that the content is uniformly distributed on the ~20’000 peers participating in the DHT, given that each node broadcasts requests to its ~1’000 directly connected peers, we would expect a success rate of approximately $\frac{1'000}{20'000} = 5\%$.

## Measurement Methodology

The Bitswap measurements mainly consist in requesting various CIDs to `kubo` and to monitor whether the Bitswap requests succeed without a DHT walk, recording the time distribution of successful Bitswap requests, and log incoming and outgoing Bitswap packets. In order to get this information, we had to modify both `kubo` and `go-bitswap` implementations.

### CIDs selection

We want the requests to be realistic requests of content that is actually being requested on the network. Hence, we selected CIDs from two different sources, to be able to compare if there were any differences in the success rate. It is important that all requested CIDs are independent from each other. For instance, if the root CID of a large file is requested, we don’t want to measure the resolution of all pieces of the file. Instead, we are only interested in the initially requested CID. This is because it is very likely for the rest of the CIDs of the DAG to be available through the same peer as the root CID was, i.e., the peer is very likely to have all of the file if it has its root CID.

The first source of CIDs is passive Bitswap sniffing. [Leo Balduf](https://github.com/mrd0ll4r) from the Weizenbaum Institute has been running a `kubo` node, recording all Bitswap requests. Out of the list of all requests, we only kept the CIDs, removed duplicates and randomized the list, in order to avoid any correlation between successive CIDs in the list. The Bitswap sniffing logs were captured on 2022-08-16.

The second source of CIDs is the logs from the IPFS Gateways gathered using [Thunderdome](https://github.com/ipfs-shipyard/thunderdome/tree/main/cmd/logtool). The logs contain all CIDs that were requested to the IPFS Gateways over HTTP(S). The list of CIDs is also randomized in order to avoid any correlation between successive requests, and invalid CIDs were filtered out from the logs. The Gateways logs were captured on 2022-12-05.

### Kubo

Normally, the `ipfs get <CID>` command will first resolve the provided CID, and in the case where this CID has children, the children CIDs will be resolved too before returning. We want to avoid this behavior, as it will give a bias to the measurements. For instance, in the case where the root CID of a large file is requested, if all blocks of the file are requested through Bitswap we would certainly measure a very good performance, as all blocks are stored on the same content provider. Hence, finding the first block can be considered to be content discovery, but fetching all the blocks from the content providers don’t provide a good metric on content discovery.

As there is no easy way to identify which CIDs from our sample are root CIDs and which are not, we slightly modified `kubo` to prevent it to follow up after a root CID request. The implementation can be found TODO:

### go-bitswap

#### Blocking `FindProvidersAsync`Hi @asuryt I just had another read and still think it's a great report! I left a few comments. I think there's only another read left from @yiannisbot and/or @guissou ?

`FindProvidersAsync` is the function that is called by Bitswap client `sessions` after the `ProviderSearchDelay` in order to discover content providers for a CID from the DHT. We want to give Bitswap more time than `ProviderSearchDelay = 1 second` to discover the content, so that we can have a better analysis of the successful content discovery time distribution, even if that’s not a realistic delay to wait for. In other words, we want to have an overall picture of the Bitswap discovery latency for all successful requests (not only those that respond within 1s). Hence, all calls to `FindProvidersAsync` have been blocked from the Bitswap client code. If the Bitswap client is able to find the content associated with the CID, the request will be considered as `SUCCESS`.

#### Timeout

After a timeout value, set to `15` seconds, we interrupt the Bitswap request, simply because we have to stop the request after some time. We selected 15 seconds, as this delay seems more than enough for Bitswap to find content without the help of the DHT, and more than 15 seconds would slow down the measurements too much.

#### DHT lookup

Once the timeout is reached and the Bitswap request is cancelled, we need to try to fetch the file. If the file wasn’t found by Bitswap and isn’t discoverable by the DHT, then it is probably not available anymore in the network. This case shouldn’t be considered as a failure from Bitswap. A Bitswap request is considered to be a failure only if Bitswap didn’t manage to discover the content in 15 seconds, and if the DHT walk returned at least one provider from which the content could actually be fetched.

Therefore, a DHT walk will start after the timeout. All providers returned by the DHT lookup will be queried by the [Selfish Bitswap Client](https://github.com/guillaumemichel/go-selfish-bitswap-client). The Selfish Bitswap Client is a simple Bitswap client that will request a CID to a specific PeerID using the Bitswap protocol. It doesn't implement Bitswap sessions nor peer manager, like the standard Bitswap client. It doesn't contain a Bitswap server, and thus won't serve blocks.

If the Bitswap client isn’t able to discover the content associated with the CID within 15 seconds, and the content was later fetched by the selfish Bitswap client after the DHT walk, the request is considered as a `FAILURE`. If the DHT walk doesn’t yield any providers for the content, the request is considered as `NO_PROVS`, and if a provider record is found but the file couldn’t be fetched by the selfish Bitswap client, the request is categorized as `FETCH_FAILED`.

### Logs

Our measurement tool generates two distinct log files. The first log files logs the following information for each IPFS request:
- The timestamp corresponding to the time the request was made.
- The requested CID.
- The number of directly connected peers at the time the request returns.
- `NO_PROV` OR `FETCH_FAILED` to notify that the file wasn't fetched OR duration of the successful request in milliseconds and the block provider OR only the block provider if the block was discovered using the DHT.

The second log file contains one entry for each outgoing and incoming messages:
- The timestamp of the message
- Message type, among the following: `WANT_HAVE`, `HAVE`, `DONT_HAVE`, `WANT_BLOCK`, `BLOCK`, `CANCEL_WANT_BLOCK`.
- The CID associated with the message.
- The PeerID receiving or sending the message.

All the results that are presented below are derived from these log files.

### Running measurements

A shell script is [available](../implementations/rfm16-bitswap-discovery-effectiveness/) to start the measurements. It basically starts a modified `kubo` daemon, and calls a python script. The [python script](../implementations/rfm16-bitswap-discovery-effectiveness/requests.py) reads a list of CIDs and concurrently requests CIDs (10 threads by default) by calling `ipfs get <CID>`. All results are logged to files as the experiment goes.

The experiments were run on a `e2-custom-6-16384` Debian 11 Virtual Machine from Google Cloud, located in `europe-west-b`.

### Technical limitations

The duration we measure for successful Bitswap content discoveries is the Time To First Block, and not the Time To First Byte (TTFB). Ideally, it would be better to measure the TTFB, as the size of the block doesn’t matter when measuring content discovery. However, as only one block is fetched, we can assume that all fetched blocks almost have the same size. We also measure the Time To First HAVE, hence we have the knowledge of when the content was discovered.

## Results and Analysis

The experiment we present the results was started on Monday 2022-11-28 at 11:37:44 GMT and has been running for 50 hours. The list of CIDs provides from Bitswap sniffing as described in [CIDs selections](#cids-selection).


### Request categorization

As described in [DHT lookup](#dht-lookup), each Bitswap request is given a category depending on the availability of the block in the network.

| Statistics | |
| --- | --- |
| Overall success rate | 98.37% (within 15 seconds) |
| Available content rate | 70.91% |

| Request Categorization | Count |
|---|---|
| TOTAL | 71769 |
| SUCESS | 50062 |
| FAILURE | 831 |
| NO_PROV | 20779 |
| FETCH_FAILED | 97 |

The overall success rate is defined as the number of queried CIDs found by Bitswap within 15 seconds divided by the number of queried CIDs available in the network. This value was measured at 98.37% for 50893 requests for available CIDs, which is larger than we expected. We will explain this number later in the report using additional data and plots. 

It is also notable that the available content rate, defined as the number of available requested CIDs in the network divided by the total number of requests, is relatively low. This means that roughly 30% of the CIDs we requested weren't found by Bitswap nor the DHT. This number can be explained because the Bitswap traffic used to generate the list of requested CIDs was sniffed back in August 2022, and the measurements were run in November 2022. This shows content churn over time.

### Top 10 block providers

We counted the number of blocks served by each PeerID, and list the 10 PeerIDs providing the most blocks.

| | PeerID | Number of blocks served | Operator |
|---|---|---|---|
| 1. | 12D3KooWGtRcWvihm4hX2gT6bQu3uyjb78rgyQR3hPhkxMwivscY | 5398 |
| 2. | 12D3KooWLsSWaRsoCejZ6RMsGqdftpKbohczNqs3jvNfPgRwrMp2 | 4113 | nft.storage |
| 3. | 12D3KooWGRJo1vLDBtfS8a4cVss2QVqvbCaPgtmwwgpUtW675QRa | 3543 | nft.storage |
| 4. | 12D3KooWAuBxG5uMBkeyFwHD9JyHaJGTqn7NhJbmmukNDPHSLKts | 3167 | nft.storage |
| 5. | 12D3KooWJc7GbwkjVg9voPNxdRnmEDS3i8NXNwRXD6kLattaMnE4 | 3085 | nft.storage |
| 6. | 12D3KooWEGeZ19Q79NdzS6CJBoCwFZwujqi5hoK8BtRcLa48fJdu | 2357 |
| 7. | 12D3KooWJ59N9z5CyLTtcUTnuTKnRTEVxiztijiEAYbP16aZjQ3D | 2287 | nft.storage |
| 8. | 12D3KooWENiDwDCPnbEQKHHsDnSsE5Y3oLyXnxuyhjcCEBK9TvkU | 2051 |
| 9. | 12D3KooWC9L4RjPGgqpzBUBkcVpKjJYofCkC5i5QdQftg1LdsFb2 | 1826 |
| 10. | 12D3KooWKd92H37a8gCDZPDAAGTYvEGAq7CNk1TcaCkcZedkTwFG | 1750 | nft.storage |

Out of the 10 top blocks providers, 6 of them are listed in the nft.storage [peer list](https://github.com/nftstorage/nft.storage/blob/main/PEERS). As this list may not be up-to-date, it is very likely that all peers in this list are actually operated by nft.storage. The PeerIDs have been tested against the [list of content providers](https://docs.ipfs.tech/how-to/peering-with-content-providers/#content-provider-list), but no PeerID was matched.


### Content Provider distribution for successful bitswap requests

We measured the share of the content being served by the top blocks providers.

| Top N providers | Percentage of blocks served |
|---|---|
| Top 1 | 10.61% |
| Top 3 | 25.65% |
| Top 5 | 37.93% |
| Top 10 | 58.12% |
| Top 20 | 75.41% |
| Top 50 | 84.39% |
| Top 361 | 98.49% |
| Top 723 | 100.0% |

Given that the public DHT contains approximatively 15'000 host at the time of writing, it is surprising to observe that only 10 peers serve almost 60% of all 50893 IPFS requests. It means that if all peers would send Bitswap requests to the top 20 blocks providers only, they would still get a success rate of $98.37\% \times 75.41\% = 74.18\%$. Also note that there were only 723 distinct providers for the 50893 requested CIDs. Hence, it would be possible to be connected to all of them at once, to get a success rate of 100%, as an IPFS node usually has around 1000 open direct connections.

### Success rate over time

![success-rate-over-time-experiment_20221205.png](../implementations/rfm16-bitswap-discovery-effectiveness/plots/success-rate-over-time-experiment_20221205.png)

The observed success rate over time appears to be roughly constant. We could have expected to see an increase in the success rate over time, as the IPFS node would have failed some requests, made DHT lookups, learned about new providers and kept them in its directly connected peers.

### Number of open connections over time

![connected-peers.png](../implementations/rfm16-bitswap-discovery-effectiveness/plots/connected-peers.png)

The number of open connections over time seems roughly constant too, which is expected as libp2p is configured to keep around 1000 open connections. Note that the number of open connections has been exported using the libp2p `host.Network().Peers()` method. 

### Success rate vs number of open connection

![success-rate-vs-npeers.png](../implementations/rfm16-bitswap-discovery-effectiveness/plots/success-rate-vs-npeers.png)

We can see no evident correlation between the success rate and the number of directly connected peers. The success rate on this plot will be more accurate between 900 and 1000 open connections that in the extreme low and high values, because there are much more samples of requests with 900-1000 open connections than request with less than 700 or more than 1200 connections.

### Bitswap latency

The following plot displays the time distribution of successful bitswap requests. 

![success-rate-15s.png](../implementations/rfm16-bitswap-discovery-effectiveness/plots/success-rate-15s.png)

We see that an overwhelming majority of requests succeed within the first second. The following plot zooms in the first second of the bitswap requests time distribution.

![success-rate-1s.png](../implementations/rfm16-bitswap-discovery-effectiveness/plots/success-rate-1s.png)

We see that a majority of Bitswap requests (75.98%) succeed within the first 200 ms, which demonstrates that Bitswap is very fast to discover content. It is important to note that the experiments were run from a data center located in central europe. Hence, other nodes may observe a significant shift of this graph depending on their distance to the content they are trying to access.

The following plots show the cummulative density function of the bitswap requests durations.

![cdf-latencies.png](../implementations/rfm16-bitswap-discovery-effectiveness/plots/cdf-latencies.png)

The following plot is the zoomed version of the cummulative density function between 0 and 1 second.

![cdf-latencies.png](../implementations/rfm16-bitswap-discovery-effectiveness/plots/cdf-latencies-1s-experiment_20221205.png)

Again, we observe that the curve is very steep before 215 milliseconds.

| Time | Percentage of requests |
|---|---|
| < 100 ms | 38.94% |
| < 150 ms | 61.88% |
| < 200 ms | 75.98% |
| < 500 ms | 88.69% |
| < 1 s | 95.20% |
| < 5 s | 98.54% |
| < 15s | 100.0% |

### Messages count

The following statistics are the average numbers over all successful Bitswap requests.

| | Count of messages per Bitswap request |
|---|---|
| Total | 1719.98 |
| Sent | 1714.11 |
| Received | 5.87 |

| | Number of solicited peers per Bitswap request |
|---|---|
| Count | 853.32 |

| | Number of exchange messages per message type per Bitswap request |
|---|---|
| WANT_HAVE | 856.07 |
| WANT_BLOCK | 8.30 |
| CANCEL | 849.74 |
| HAVE | 3.95 |
| DONT_HAVE | 0.18 |
| BLOCK | 1.74 |

We can clearly see that Bitswap has a large content discovery success rate because it simply broadcast its requests to its directly connected peers. Each Bitswap request first broadcast a `WANT_HAVE` message to more than 800 directly connected peers. Once the block is fetched, the node must send `CANCEL_WANT_BLOCK` messages to all peers it sent the `WANT_HAVE` request, which makes a total of more than 1700 messages per Bitswap request.

In comparison, the DHT roughly find content in 3-5 hops and has a concurrency parameter set to 3, meaning that it is expected to send at most ~15 messages. However, the average latency of finding content through the DHT is much higher than using a Bitswap broadcast.

### Gateway CIDs comparison

In order to compare double check whether the CIDs obtained by sniffing Bitswap traffic are representative to the traffic in the IPFS network, we have done the same measurements with a list of CIDs originating from the IPFS Gateways logs. The experiment started on 2022-12-05 at 15:23:43 GMT and ran for 1 hour and 45 minutes. We will only include relevant results.

| Statistics | |
| --- | --- |
| Overall success rate | 99.83% (within 15 seconds) |
| Available content rate | 95.64% |

| Request Categorization | Count |
|---|---|
| TOTAL | 32404 |
| SUCESS | 30936 |
| FAILURE | 54 |
| NO_PROV | 1134 |
| FETCH_FAILED | 280 |

We observed a larger overall success rate (99.83% vs 98.37% for the first experiment). We also observe that the ratio of `FETCH_FAILED` is more important in the second experiment, which could explain why the success rate is higher. Maybe the content was available, but the Selfish Bitswap Client failed to retrieve it, which boosted the success rate. The available content rate is also much higher (95.64% vs 70.91% for the first experiment). This can be explained because the CIDs for the Gateway experiment were collected a few days before the experiments. The CIDs collected by sniffing Bitswap were collected multiple months before running the experiment.

![success-rate-1s-gatewaycids_10_20221206.png](../implementations/rfm16-bitswap-discovery-effectiveness/plots/success-rate-1s-gatewaycids_10_20221206.png)

We observe a similar distribution for the Bitswap discovery time. Confirming that most of the successful Bitswap requests succeed in less than 200 milliseconds.

| Time | Percentage of requests |
|---|---|
| < 100 ms | 43.59% |
| < 150 ms | 56.82% |
| < 200 ms | 64.02% |
| < 500 ms | 81.94% |
| < 1 s | 90.44% |
| < 5 s | 98.69% |
| < 15s | 100.0% |


## Improvement suggestions

## Conclusion
