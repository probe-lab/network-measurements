# Nebula Measurement Results Calendar Week 49 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 49 - 2024](#nebula-measurement-results-calendar-week-49---2024)
  - [General Information](#general-information)
    - [Agent Versions](#agent-versions)
    - [Protocols](#protocols)
    - [Top 10 Rotating Nodes](#top-10-rotating-nodes)
    - [Crawls](#crawls)
      - [Overall](#overall)
      - [Classification](#classification)
      - [Agents](#agents)
      - [DHT Server vs. Clients](#dht-server-vs-clients)
      - [Errors](#errors)
      - [Total Peer IDs Discovered Classification](#total-peer-ids-discovered-classification)
      - [Protocols](#protocols-1)
  - [Churn](#churn)
  - [Inter Arrival Time](#inter-arrival-time)
  - [Agent Version Analysis](#agent-version-analysis)
    - [Overall](#overall-1)
    - [Kubo](#kubo)
    - [Classification](#classification-1)
  - [Geolocation](#geolocation)
    - [Unique IP Addresses](#unique-ip-addresses)
    - [Classification](#classification-2)
    - [Agents](#agents-1)
  - [Datacenters](#datacenters)
    - [Overall](#overall-2)
    - [Classification](#classification-3)
    - [Agents](#agents-2)
  - [Website Monitoring](#website-monitoring)
    - [Time To First Byte](#time-to-first-byte)
    - [First Contentful Paint](#first-contentful-paint)
    - [Largest Contentful Paint](#largest-contentful-paint)
    - [HTTP vs. Kubo](#http-vs-kubo)
    - [Error Rate](#error-rate)
  - [DHT Performance](#dht-performance)
    - [Weekly](#weekly)
    - [Daily](#daily)
    - [Error Rate](#error-rate-1)
  - [Terminology](#terminology)
    - [Peer Classification](#peer-classification)
    - [Storm Specific Protocols](#storm-specific-protocols)


## General Information

The following results show measurement data that were collected in calendar week 49 in 2024 from `2024-12-02` to `2024-12-09`.

- Number of crawls `84`
- Number of visits `10,284,855`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `44,274`
- Number of unique peer IDs discovered in the DHT `42,488`
- Number of unique IP addresses found `34,542`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20241201080501` (2024-12-02 00:01:15)
- `bootnode-20241201124016` (2024-12-02 00:01:26)
- `helia/4.2.3 libp2p/1.6.0 UserAgent=v20.9.0` (2024-12-02 00:01:29)
- `ca-vsc@aacae1136` (2024-12-02 10:02:19)
- `kubo/0.33.0-dev/e487ac75c-dirty` (2024-12-02 14:01:07)
- `bootnode-20241202080122` (2024-12-02 14:01:28)
- `kubo/0.32.1/ddde79f4f-dirty` (2024-12-02 16:02:22)
- `github.com/functionland/go-fula@6f5a65baa` (2024-12-02 18:01:15)
- `bootnode-20241202200115` (2024-12-02 20:01:30)
- `bootnode-20241202210233` (2024-12-02 22:01:38)
- `bootnode-20241202212631` (2024-12-02 22:01:59)
- `kubo/0.32.1/ae80605db-dirty` (2024-12-03 02:01:23)
- `bootnode-20241203075034` (2024-12-03 08:02:16)
- `fsp2p@af855cf9d-dirty` (2024-12-03 14:01:17)
- `github.com/libp2p/go-libp2p/examples@288868c0d-dirty` (2024-12-03 16:02:09)
- `bootnode-20241203124423` (2024-12-03 22:01:28)
- `kubo/0.33.0-dev/433444b60-dirty` (2024-12-04 02:01:18)
- `kubo/0.33.0-dev/433444b60` (2024-12-04 02:02:00)
- `ca-vsc@49d2dfe79` (2024-12-04 06:01:10)
- `ca-vsc@74ba62ad8` (2024-12-04 08:01:36)
- `kubo/0.33.0-dev/9b887ea/1234567890123456789012345678901234567890` (2024-12-04 14:01:46)
- `kubo/0.33.0-dev/53e793a/docker` (2024-12-04 14:02:13)
- `kubo/0.33.0-dev/433444b/1234567890123456789012345678901234567890` (2024-12-04 16:01:33)
- `bootnode-20241204171755` (2024-12-04 18:01:51)
- `bootnode-20241204192906` (2024-12-04 20:01:23)
- `bootnode-20241204205402` (2024-12-05 00:01:23)
- `bootnode-20241205042311` (2024-12-05 08:01:37)
- `js-libp2p/0.0.0 UserAgent=vTEST` (2024-12-05 10:02:20)
- `kubo/0.24.0/e70db65/energiasonorasoftware-protonmail-com` (2024-12-05 14:04:49)
- `ca-vsc@4ceb6e34f` (2024-12-06 08:01:44)
- `libp2p/2.3.1 UserAgent=v22.11.0` (2024-12-07 08:01:21)
- `helia/2.0.0 libp2p/2.3.1 UserAgent=v20.18.1` (2024-12-07 08:02:11)
- `kubo/0.32.1/Pleione 0.5` (2024-12-07 14:02:14)
- `libp2p/1.9.4 UserAgent=v20.11.1` (2024-12-07 18:01:12)
- `bootnode-20241207212122` (2024-12-07 22:01:29)
- `bootnode-20241208151626` (2024-12-08 16:01:20)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/p2pnet/wallet/login/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/block/latest/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/membership/details/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/membership/payment/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/membership/list/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/mining/info/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/node/register/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/file/upload/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/recharge/points/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/transfer/transaction/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/token/upload/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/miner/submit/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/payment/qrcode/1.0.0` (2024-12-03 10:01:26)
- `/p2pnet/traffic/upload/1.0.0` (2024-12-03 10:01:26)
- `/orbitdb/heads/orbitdb/zdpuApD3ctehCrPXtdDJSaPbmKo71zEhFV6VKQPtcz9UsoVYx` (2024-12-04 06:02:05)
- `/orbitdb/heads/orbitdb/zdpuAuPk6Rg5ewBYQx4Yp2ycMAR8Nj17RfmoFNmw7VdFvRv12` (2024-12-04 08:02:00)
- `/otter/activitypub/0.0.1` (2024-12-05 08:01:31)
- `/orbitdb/heads/orbitdb/zdpuAt7DjR56FLUGVmb22ceHDnidoc33WGPN77YATtgBB4BP7` (2024-12-05 10:01:29)
- `/orbitdb/heads/orbitdb/zdpuAmoqavhbYYcV4cwkN9koFFbeYp4sZca7WErYEVWofiGJA` (2024-12-05 16:01:19)
- `/orbitdb/heads/orbitdb/zdpuApogpdf1N8JV91yqCxMpx2ups7KsqtAsH3GE5aRj96rZw` (2024-12-06 08:02:11)
- `/orbitdb/heads/orbitdb/zdpuAonjtUV45hyTjJKQGzggzeSFf8RwpsALiN1jtRgeL46B1` (2024-12-06 14:01:41)
- `http-proxy` (2024-12-07 08:01:21)
- `/http-proxy/1.0.0` (2024-12-08 00:02:04)
- `/orbitdb/heads/orbitdb/zdpuAorx1hydeev1AYfyGspK6wfUrH6MTQ1WEckXtwzyN2TbX` (2024-12-08 10:01:12)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `139.59.6.4` | IN | 95 | ['kubo/0.29.0/3f0947b']| True  |
| `82.180.162.171` | US | 91 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.30.0/', 'kubo/0.30.0/846c5cc']| False  |
| `51.15.247.127` | FR | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.150.159` | FR | 77 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 77 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `152.81.47.227` | FR | 71 | ['kubo/0.32.0/', 'kubo/0.33.0-dev/']| False  |
| `51.15.64.186` | NL | 51 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 51 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 49 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `143.110.168.61` | GB | 47 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| True  |

### Crawls

#### Overall

![Crawl Overview](./plots/crawl-overview.png)

#### Classification

![Crawl Classifications](./plots/crawl-classifications.png)

#### Agents

![Crawl Properties By Agent](./plots/crawl-properties.png)

Only the top 10 kubo versions appear in the right graph (due to lack of colors) based on the average count in the time interval. The `0.8.x` versions **do not** contain disguised storm peers.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

#### DHT Server vs. Clients

You can find the most up-to-date graph on [`probelab.io/ipfskpi`](https://probelab.io/ipfskpi/#ipfs-servers-vs-clients-plot).

#### Errors

![Crawl Errors](./plots/crawl-errors.png)

#### Total Peer IDs Discovered Classification

![Peer count by classification](./plots/peer-classifications.png)

In the specified time interval from `2024-12-02` to `2024-12-09` we visited `` unique peer IDs.
All peer IDs fall into one of the following classifications:

| Classification | Description |
| --- | --- |
| `offline` | A peer that was never seen online during the measurement period (always offline) but found in the DHT |
| `dangling` | A peer that was seen going offline and online multiple times during the measurement period |
| `oneoff` | A peer that was seen coming online and then going offline **only once** during the measurement period |
| `online` | A peer that was not seen offline at all during the measurement period (always online) |
| `left` | A peer that was online at the beginning of the measurement period, did go offline and didn't come back online |
| `entered` | A peer that was offline at the beginning of the measurement period but appeared within and didn't go offline since then |

#### Protocols

![Crawl Properties By Protocols](./plots/crawl-protocols.png)

## Churn

![Peer Churn](./plots/peer-churn.png)

Only the top 10 kubo versions appear in the right graph (due to lack of colors) based on the average count in the time interval. The `0.8.x` versions **do not** contain disguised storm peers. This graph also excludes peers that were online the whole time. You can read this graph as: if I see a peer joining the network, what's the likelihood for it to stay `X` hours in the network.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Inter Arrival Time

![Inter Arrival Time](./plots/peer-inter-arrival-time.png)

Only the top 10 kubo versions appear in the right graph (due to lack of colors) based on the average count in the time interval. The `0.8.x` versions **do not** contain disguised storm peers.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Agent Version Analysis

### Overall

![Overall Agent Distribution](./plots/agents-overall.png)

Includes all peers that the crawler was able to connect to at least once: `dangling`, `online`, `oneoff`, `entered`. Hence, the total number of peers is lower as the graph excludes `offline` and `left` peers (see [classification](#peer-classification)).

### Kubo

![Kubo Agent Distribution](./plots/agents-kubo.png)

`storm` shows the `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

### Classification

![Agents by Classification](./plots/agents-classification.png)

The classifications are documented [here](#peer-classification).
`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Geolocation

### Unique IP Addresses

![Unique IP addresses](./plots/geo-unique-ip.png)

This graph shows all IP addresses that we found from `2024-12-02` to `2024-12-09` in the DHT and their geolocation distribution by country.

### Classification

![Peer Geolocation By Classification](./plots/geo-peer-classification.png)

The classifications are documented [here](#peer-classification). 
The number in parentheses in the graph titles show the number of unique peer IDs that went into the specific subgraph.

### Agents

![Peer Geolocation By Agent](./plots/geo-peer-agents.png)

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Datacenters

### Overall

![Overall Datacenter Distribution](./plots/cloud-overall.png)

This graph shows all IP addresses that we found from `2024-12-02` to `2024-12-09` in the DHT and their datacenter association.

### Classification

![Datacenter Distribution By Classification](./plots/cloud-classification.png)

The classifications are documented [here](#peer-classification). Note that the x-axes are different.

### Agents

![Datacenter Distribution By Agent](./plots/cloud-agents.png)

The number in parentheses in the graph titles show the number of unique peer IDs that went into the specific subgraph.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Website Monitoring

For a description of our measurement methodology check out [this repository](https://github.com/dennis-tra/tiros).

### Time To First Byte

The time it took to receive the first byte of the first response (that was not a redirect). The large number in each tile is the time in seconds. The number at the very bottom of the graph shows the sample size that went into each subplot/website. Note: the color scales are different in each graph.

![Time To First Byte](./plots/tiros-ttfb.png)

### First Contentful Paint

![First contentful Paint](./plots/tiros-fcp.png)

### Largest Contentful Paint

![Largest contentful Paint](./plots/tiros-lcp.png)

### HTTP vs. Kubo

The number above each bar shows the sample size that went into the calculation.

![HTTP vs. Kubo](./plots/tiros-kubo-vs-http.png)

### Error Rate

The following graph shows the daily error rate in accessing these website.

![Error Rate](./plots/tiros-errors.png)

## DHT Performance

We are running lean libp2p peers that just support the Kademlia DHT protocol in six different AWS regions. Each peer takes turns to publish the provider record for a CID of random data. All other peers are then instructed to lookup that CID. "Looking up" here means finding the provider record. So the numbers below don't show the actual content retrieval times (which would depend on file sizes) but instead the DHT performance. The peers run `go-libp2p-kad-dht` version `v0.21.1` + default configurations.

Code can be found here: [dennis-tra/parsec](https://github.com/dennis-tra/parsec) (we plan to move this to our [ProbeLab organization](https://github.com/probe-lab))

### Weekly

![Weekly Region CDF Publications + Retrievals](./plots/parsec-regions-cdf.png)

The number in parenthesis is the number of publications/retrievals for that particular region that went into the calculation.

![Weekly Region Boxplot Publications + Retrievals](./plots/parsec-regions-boxplot.png)

The number in the box is the number of publications/retrievals for that particular region that went into the calculation.

The box extends from the first quartile (Q1) to the third quartile (Q3) of the data, with a line at the median. The whiskers extend from the box by 1.5x the inter-quartile range (IQR). Flier points are those past the end of the whiskers. See https://en.wikipedia.org/wiki/Box_plot for reference.

### Daily

![Daily Publications Boxplot](./plots/parsec-publications-boxplot-daily.png)

The number in the box is the number of publications that went into the calculation of the box.

The box extends from the first quartile (Q1) to the third quartile (Q3) of the data, with a line at the median. The whiskers extend from the box by 1.5x the inter-quartile range (IQR). Flier points are those past the end of the whiskers. See https://en.wikipedia.org/wiki/Box_plot for reference.

![Daily Retrieval Boxplot](./plots/parsec-retrievals-boxplot-daily.png)
The number in the box is the number of publications/retrievals that went into the calculation of the box.

The box extends from the first quartile (Q1) to the third quartile (Q3) of the data, with a line at the median. The whiskers extend from the box by 1.5x the inter-quartile range (IQR). Flier points are those past the end of the whiskers. See https://en.wikipedia.org/wiki/Box_plot for reference.

### Error Rate

![Publication/Retrieval Error Rate](./plots/parsec-error-rate.png)



### Peer Classification

| Classification | Description |
| --- | --- |
| `offline` | A peer that was never seen online during the measurement period (always offline) but found in the DHT |
| `dangling` | A peer that was seen going offline and online multiple times during the measurement period |
| `oneoff` | A peer that was seen coming online and then going offline **only once** during the measurement period |
| `online` | A peer that was not seen offline at all during the measurement period (always online) |
| `left` | A peer that was online at the beginning of the measurement period, did go offline and didn't come back online |
| `entered` | A peer that was offline at the beginning of the measurement period but appeared within and didn't go offline since then |

### Storm Specific Protocols

The following protocol strings are unique for `storm` nodes according to [this Bitdefender paper](https://www.bitdefender.com/files/News/CaseStudies/study/376/Bitdefender-Whitepaper-IPStorm.pdf):

- `/sreque/*`
- `/shsk/*`
- `/sfst/*`
- `/sbst/*`
- `/sbpcp/*`
- `/sbptp/*`
- `/strelayp/*`