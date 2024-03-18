# Nebula Measurement Results Calendar Week 11 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 11 - 2024](#nebula-measurement-results-calendar-week-11---2024)
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

The following results show measurement data that were collected in calendar week 11 in 2024 from `2024-03-11` to `2024-03-18`.

- Number of crawls `336`
- Number of visits `27,342,388`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `62,481`
- Number of unique peer IDs discovered in the DHT `61,419`
- Number of unique IP addresses found `87,794`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `helia/4.0.2 libp2p/1.2.4 UserAgent=v18.17.1` (2024-03-11 01:22:11)
- `prox_powd@074fedb90-dirty` (2024-03-11 03:21:46)
- `github.com/bahner/go-ma-actor@f513c1e7d-dirty` (2024-03-11 20:51:35)
- `Chainflip Node/v1.2.1-ca84e37e244 (glorious-journey-9858)` (2024-03-12 00:20:45)
- `libp2p/1.2.3 UserAgent=v18.18.2` (2024-03-12 04:20:53)
- `helia/4.0.2 libp2p/1.2.4 UserAgent=v20.10.0` (2024-03-12 05:50:55)
- `kubo/0.27.0/qkpay` (2024-03-12 06:51:53)
- `netdisc@6e6c471e7-dirty` (2024-03-12 13:20:48)
- `helia/4.0.2 libp2p/1.3.0 UserAgent=v20.4.0` (2024-03-12 15:51:01)
- `kubo/0.26.0/dfec50d5f7ff` (2024-03-12 16:20:56)
- `kubo/0.27.0/docker` (2024-03-12 16:21:51)
- `kubo/0.28.0-dev/e22f47a` (2024-03-12 19:51:55)
- `github.com/bahner/go-ma-actor@52dd2deaf` (2024-03-12 20:51:03)
- `github.com/bahner/go-ma-actor@e4431de36-dirty` (2024-03-12 20:51:10)
- `rust-libp2p-server/0.12.7` (2024-03-13 03:51:26)
- `helia/4.0.2 libp2p/1.3.0 UserAgent=v18.19.1` (2024-03-13 06:50:57)
- `kubo/0.27.0/desktop` (2024-03-13 07:51:27)
- `github.com/bahner/go-ma-actor@6a26a0afa-dirty` (2024-03-13 18:20:50)
- `helia/4.0.2 libp2p/1.2.4 UserAgent=v21.1.0` (2024-03-13 19:51:04)
- `helia/4.0.2 libp2p/1.2.4 UserAgent=v21.6.2` (2024-03-14 01:50:55)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v18.16.0` (2024-03-14 08:21:00)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.11.1` (2024-03-14 08:21:14)
- `git.pangu.datalab/POFK/go-libp2p-proxy@513733960-dirty` (2024-03-15 03:21:11)
- `netdisc@c025d1d7e-dirty` (2024-03-15 05:51:15)
- `libp2p/1.2.4 UserAgent=v21.5.0` (2024-03-15 07:21:42)
- `libp2p/1.3.0 UserAgent=v21.5.0` (2024-03-15 13:51:21)
- `github.com/bahner/go-ma-actor@bf7c22f75-dirty` (2024-03-15 19:50:57)
- `github.com/bahner/go-ma-actor@b1825b6ab-dirty` (2024-03-16 00:50:53)
- `github.com/bahner/go-ma-actor@ea1b94ba5-dirty` (2024-03-16 02:51:00)
- `github.com/bahner/go-ma-actor@0221fd047` (2024-03-16 04:51:08)
- `github.com/bahner/go-ma-actor@0221fd047-dirty` (2024-03-16 06:21:17)
- `kubo/0.22.0-dev/5156f2116` (2024-03-16 07:51:00)
- `github.com/bahner/go-ma-actor@77a490e3e` (2024-03-17 00:20:50)
- `github.com/bahner/go-ma-actor@d12a91d98` (2024-03-17 02:51:42)
- `ipfsbot_serv@` (2024-03-17 11:21:30)
- `github.com/bahner/go-ma-actor@41c895bdc-dirty` (2024-03-17 19:21:12)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v21.6.2` (2024-03-17 20:20:57)
- `github.com/bahner/go-ma-actor@9e8e244ce-dirty` (2024-03-17 22:50:51)
- `github.com/bahner/go-ma-actor@94639981a-dirty` (2024-03-17 23:52:18)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `bpfs@stream/block/hash/1.0.0` (2024-03-11 09:50:55)
- `bpfs@stream/blockChain/browser/1.0.0` (2024-03-11 09:50:55)
- `bpfs@stream/blockchain/init/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/transaction/preprocessing/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/Storage/Award/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/balance/full/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/balance/available/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/blockChain/height/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/screen/balance/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/transaction/updateRecord/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/block/newSubmission/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/blockchain/height/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/transaction/pending/1.0.0` (2024-03-11 09:50:56)
- `bpfs@stream/transaction/signed/1.0.0` (2024-03-11 09:50:56)
- `/foggie/p2p/kad/1.0.0` (2024-03-11 12:20:50)
- `bpfs@stream/balance/full/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/block/hash/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/transaction/preprocessing/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/blockchain/init/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/balance/available/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/block/newSubmission/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/screen/balance/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/transaction/pending/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/Storage/Award/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/transaction/signed/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/blockChain/browser/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/blockChain/height/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/transaction/updateRecord/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/blockchain/height/1.1.0` (2024-03-12 09:22:10)
- `bpfs@stream/leader/full/1.1.0` (2024-03-14 10:20:49)
- `/pioufukuan/0.1.0` (2024-03-15 03:21:11)
- `/orbitdb/heads/orbitdb/zdpuAz1FDAAsSd3okfeFgixjNj8grTYZwNyy3ccjuhPBxHfY8` (2024-03-15 07:21:42)
- `/orbitdb/heads/orbitdb/zdpuAv2W8ZWsoHt7jUZ5Jg1V1k9bfrp74NrJHt1VRoQ6RG3eS` (2024-03-16 07:21:00)
- `skypier` (2024-03-17 17:51:01)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 218 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `51.159.134.20` | FR | 86 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.201.219` | FR | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.151.120` | FR | 82 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `90.116.141.211` | FR | 76 | ['kubo/0.18.0/', 'kubo/0.26.0/brave', 'kubo/0.27.0/', 'main@', 'SybilNode@']| False  |
| `172.33.1.5` | US | 73 | ['kubo/0.15.0/3ae52a4', 'kubo/0.19.1/', 'kubo/0.22.0/3f884d3/docker']| False  |
| `51.15.64.186` | FR | 70 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 70 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | NL | 69 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | FR | 69 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-03-11` to `2024-03-18` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-03-11` to `2024-03-18` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-03-11` to `2024-03-18` in the DHT and their datacenter association.

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