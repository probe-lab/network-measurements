# Nebula Measurement Results Calendar Week 5 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 5 - 2024](#nebula-measurement-results-calendar-week-5---2024)
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

The following results show measurement data that were collected in calendar week 5 in 2024 from `2024-01-29` to `2024-02-05`.

- Number of crawls `336`
- Number of visits `41,326,754`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `63,850`
- Number of unique peer IDs discovered in the DHT `61,842`
- Number of unique IP addresses found `84,221`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.27.0-dev/4d3cc96c1` (2024-01-29 04:51:22)
- `js-libp2p/0.46.7 UserAgent=v18.18.2` (2024-01-29 05:21:16)
- `github.com/jknezevic/p2p-test@` (2024-01-29 10:51:08)
- `kubo/0.26.0/04e04ef-dirty` (2024-01-29 12:21:00)
- `github.com/INFURA/ipfs-p2p-server@c50976dbb` (2024-01-29 13:51:16)
- `kubo/0.25.0/15a12da-dirty` (2024-01-29 17:51:00)
- `github.com/INFURA/ipfs-p2p-server@d8dbb7ae1` (2024-01-29 17:51:47)
- `github.com/bahner/go-ma-relay@1a545aa7d-dirty` (2024-01-29 18:21:55)
- `go-ma-pong@b70078338-dirty` (2024-01-29 21:21:44)
- `github.com/bahner/go-ma-relay@b70078338-dirty` (2024-01-29 21:22:34)
- `kubo/0.21.0/qikfox` (2024-01-29 23:51:39)
- `kubo/0.24.0/qikfox` (2024-01-30 01:21:40)
- `go-ma-pong@9da60dff8-dirty` (2024-01-30 02:51:09)
- `github.com/INFURA/ipfs-p2p-server@172db4fe7` (2024-01-30 10:52:23)
- `Polkadot Bulletin Chain Node/v0.1.0-dev-c92b5220453 (alice)` (2024-01-30 13:22:35)
- `github.com/INFURA/ipfs-p2p-server@9c260935d` (2024-01-30 17:51:31)
- `github.com/INFURA/ipfs-p2p-server@bfc78871a` (2024-01-31 13:21:15)
- `js-libp2p/0.45.9 UserAgent=v20.9.0` (2024-01-31 22:51:44)
- `github.com/dozyio/ppdb@` (2024-02-01 01:51:03)
- `kubo/0.26.0-s3/096f510ab-dirty` (2024-02-01 08:22:31)
- `helia/4.0.1 libp2p/1.2.1 UserAgent=v21.2.0` (2024-02-01 08:52:02)
- `github.com/diadata-org/diaprotocol@566574094-dirty` (2024-02-01 11:22:25)
- `github.com/jknezevic/p2p-test@64a9de36f-dirty` (2024-02-01 12:20:54)
- `kubo/0.27.0-dev/1a3b8d707` (2024-02-01 13:51:04)
- `helia/4.0.1 libp2p/1.2.1 UserAgent=v20.11.0` (2024-02-01 15:50:59)
- `github.com/INFURA/ipfs-p2p-server@04d21089e` (2024-02-01 15:51:27)
- `kubo/0.27.0-dev/4d3cc96c1-dirty` (2024-02-01 17:21:20)
- `newrelay@7f1edbc48` (2024-02-01 17:51:45)
- `newrelay@2dd717425` (2024-02-01 19:51:11)
- `kubo/0.27.0-dev/1a3b8d7/docker` (2024-02-01 22:20:59)
- `carrier4@d61dab1e9-dirty` (2024-02-02 07:20:58)
- `kubo/0.27.0-dev/efdef7f/docker` (2024-02-02 12:22:23)
- `kubo/0.27.0-dev/efdef7fdc-dirty/docker` (2024-02-02 18:51:39)
- `js-libp2p/0.45.9 UserAgent=v16.18.1` (2024-02-02 21:21:04)
- `github.com/INFURA/ipfs-p2p-server@ff11a0a37` (2024-02-02 21:52:18)
- `helia/2.0.3 js-libp2p/0.46.16 UserAgent=v18.19.0` (2024-02-03 11:21:12)
- `go-ma-pong@93bd6103e-dirty` (2024-02-03 12:20:58)
- `go-ma-pong@e70a526bc-dirty` (2024-02-03 12:51:34)
- `go-ma-pong@be2cdc33d` (2024-02-03 13:21:15)
- `github.com/bahner/go-ma-actor@ffdb25fd2` (2024-02-03 13:50:50)
- `github.com/bahner/go-ma-actor@be2cdc33d-dirty` (2024-02-03 14:22:24)
- `github.com/bahner/go-ma-actor@b93fc0f20` (2024-02-03 19:52:22)
- `github.com/bahner/go-ma-actor@b93fc0f20-dirty` (2024-02-03 20:51:46)
- `github.com/bahner/go-ma-actor@b87608058-dirty` (2024-02-03 22:51:01)
- `github.com/bahner/go-ma-actor@0fd6523e0-dirty` (2024-02-04 02:52:02)
- `kubo/0.27.0-dev/efdef7fdc` (2024-02-04 03:20:47)
- `github.com/bahner/go-ma-actor@9774cc29b-dirty` (2024-02-04 03:21:10)
- `github.com/bahner/go-ma-actor@8c4841df6-dirty` (2024-02-04 11:21:38)
- `github.com/bahner/go-ma-actor@221de0464-dirty` (2024-02-04 14:52:17)
- `github.com/bahner/go-ma-actor@aadf74f39-dirty` (2024-02-04 15:51:45)
- `github.com/bahner/go-ma-actor@b107065ed` (2024-02-04 16:21:24)
- `github.com/bahner/go-ma-actor@b107065ed-dirty` (2024-02-04 17:21:43)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v18.18.2` (2024-02-04 21:21:17)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/orbitdb/heads/orbitdb/zdpuAnG1rU7RcEPpi2pAXzMeT675tYsHLntc8WdfRZD6iw2Ce` (2024-01-29 02:21:29)
- `/tss/keySign/session/0830e93b-bf16-11ee-9bea-0242c0a60a78` (2024-01-30 02:22:02)
- `/cf08b3b19e74116a4b388a6ebacb017e19dec2491799f35a967e83a363258417/sync/warp` (2024-01-30 13:22:35)
- `/cf08b3b19e74116a4b388a6ebacb017e19dec2491799f35a967e83a363258417/sync/2` (2024-01-30 13:22:35)
- `/cf08b3b19e74116a4b388a6ebacb017e19dec2491799f35a967e83a363258417/block-announces/1` (2024-01-30 13:22:35)
- `/cf08b3b19e74116a4b388a6ebacb017e19dec2491799f35a967e83a363258417/light/2` (2024-01-30 13:22:35)
- `/cf08b3b19e74116a4b388a6ebacb017e19dec2491799f35a967e83a363258417/state/2` (2024-01-30 13:22:35)
- `/cf08b3b19e74116a4b388a6ebacb017e19dec2491799f35a967e83a363258417/grandpa/1` (2024-01-30 13:22:35)
- `/cf08b3b19e74116a4b388a6ebacb017e19dec2491799f35a967e83a363258417/transactions/1` (2024-01-30 13:22:35)
- `/cf08b3b19e74116a4b388a6ebacb017e19dec2491799f35a967e83a363258417/kad` (2024-01-30 13:22:35)
- `/tss/keySign/session/3b2f9b37-c084-11ee-9da3-0242c0a60a78` (2024-01-31 22:22:23)
- `/tss/keySign/session/ad30b1b9-c0a5-11ee-945d-0242c0a60a78` (2024-02-01 02:21:10)
- `/tss/keySign/session/ab65ca90-c0a5-11ee-945d-0242c0a60a78` (2024-02-01 02:21:10)
- `/tss/keySign/session/abff5ba9-c0a5-11ee-945d-0242c0a60a78` (2024-02-01 02:21:10)
- `/tss/keySign/session/af93370a-c0a5-11ee-945d-0242c0a60a78` (2024-02-01 02:21:10)
- `/p2p/_testing` (2024-02-01 17:51:45)
- `/tss/keySign/session/22019a5b-c165-11ee-bc52-0242c0a60a78` (2024-02-02 00:51:14)
- `/tss/keySign/session/2810cacb-c165-11ee-9517-0242c0a60a78` (2024-02-02 00:51:46)
- `/tss/keySign/session/ce6571aa-c1b4-11ee-995d-0242c0a60a78` (2024-02-02 10:21:30)
- `/tss/keySign/session/73372259-c2ad-11ee-a6b2-0242c0a60a78` (2024-02-03 16:52:10)
- `/tss/keySign/session/70d49be9-c2ad-11ee-a6b2-0242c0a60a78` (2024-02-03 16:52:10)
- `/tss/keySign/session/6fa34067-c2ad-11ee-a6b2-0242c0a60a78` (2024-02-03 16:52:10)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 208 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `172.33.1.5` | US | 151 | ['kubo/0.15.0/3ae52a4', 'kubo/0.19.1/', 'kubo/0.22.0/3f884d3/docker']| False  |
| `212.47.234.38` | FR | 94 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.128.68` | IN | 88 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.128.68` | FR | 88 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.142.254` | FR | 75 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 63 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `151.115.53.194` | PL | 58 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 53 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 53 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-01-29` to `2024-02-05` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-01-29` to `2024-02-05` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-01-29` to `2024-02-05` in the DHT and their datacenter association.

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

Code can be found here: [dennis-tra/parsec](https://github.com/dennis-tra/parsec) (we plan to move this to our [ProbeLab organization](https://github.com/plprobelab))

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