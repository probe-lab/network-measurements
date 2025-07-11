# Nebula Measurement Results Calendar Week 18 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 18 - 2025](#nebula-measurement-results-calendar-week-18---2025)
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

The following results show measurement data that were collected in calendar week 18 in 2025 from `2025-05-05` to `2025-05-12`.

- Number of crawls `84`
- Number of visits `9,106,948`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `70,504`
- Number of unique peer IDs discovered in the DHT `70,235`
- Number of unique IP addresses found `30,596`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20250504201523` (2025-05-05 00:01:36)
- `kubo/0.35.0-dev/705962018` (2025-05-05 00:01:49)
- `bootnode-20250505055522` (2025-05-05 06:01:05)
- `libp2p/1.9.4 UserAgent=v20.19.1` (2025-05-05 12:02:28)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250505135705-7fa902618b55` (2025-05-05 16:01:34)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250505172536-04a31f4e0101` (2025-05-05 22:01:46)
- `github.com/harmony-one/harmony@v1.10.3-0.20250505155223-61816f79a8d1+dirty` (2025-05-06 04:02:26)
- `github.com/JackalLabs/sequoia@v1.3.0-alpha.2` (2025-05-06 16:02:17)
- `bootnode-20250506183425` (2025-05-06 18:01:39)
- `bootnode-20250506183157` (2025-05-06 18:04:01)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250506182241-1a93f9178732` (2025-05-06 20:01:24)
- `kubo/0.35.0-dev/fffdec3/docker` (2025-05-06 20:02:01)
- `github.com/harmony-one/harmony@v1.10.3-0.20250506153713-e10d464a9c0f` (2025-05-06 20:02:13)
- `kubo/0.35.0-dev/b5d7369/docker` (2025-05-06 20:02:15)
- `bootnode-20250506113003` (2025-05-06 22:01:12)
- `kubo/0.35.0-dev/7c844ba/1234567890123456789012345678901234567890` (2025-05-06 22:01:50)
- `bootnode-20250507055729` (2025-05-07 06:01:13)
- `dvpncmd@1297f54d1-hayek` (2025-05-07 12:02:19)
- `bootnode-20250507155009` (2025-05-07 14:02:09)
- `kubo/0.35.0-rc1/6e89271/1234567890123456789012345678901234567890` (2025-05-07 16:02:23)
- `kubo/0.36.0-dev/925a4d1/docker` (2025-05-07 16:02:26)
- `bootnode-20250507141133` (2025-05-07 20:01:06)
- `kubo/0.35.0-rc1/` (2025-05-07 20:01:23)
- `kubo/0.36.0-dev/925a4d1b4-dirty` (2025-05-07 22:01:19)
- `kubo/0.35.0-rc1/6e89271` (2025-05-08 02:02:23)
- `kubo/0.36.0-dev/8c2c500/docker` (2025-05-08 04:02:33)
- `kubo/0.35.0-dev/ddeb3a41c-dirty` (2025-05-08 12:01:03)
- `ca-vsc@v0.0.0-20250508104634-501c223131a8` (2025-05-08 12:02:33)
- `bootnode-20250508155600` (2025-05-08 14:01:21)
- `kubo/0.36.0-dev/8c2c5009d-dirty` (2025-05-08 14:01:41)
- `bootnode-20250508155713` (2025-05-08 14:01:56)
- `bootnode-20250508085455` (2025-05-08 14:02:16)
- `github.com/harmony-one/harmony@v1.10.3-0.20250506153713-e10d464a9c0f+dirty` (2025-05-08 16:01:23)
- `ca-vsc@v0.0.0-20250508122021-9d142c6e72e2` (2025-05-09 08:01:33)
- `js-libp2p/2.8.5 node/22.14.0` (2025-05-09 12:01:53)
- `kubo/0.35.0-rc1/6e89271d4` (2025-05-09 20:01:30)
- `kubo/0.36.0-dev/6f37df7/docker` (2025-05-10 02:02:08)
- `js-libp2p/2.8.5 node/22.12.0` (2025-05-11 08:01:20)
- `kubo/0.35.0-rc1/desktop` (2025-05-11 10:02:15)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `harmony/sync/testnet/0/1.0.0/0` (2025-05-07 14:02:19)
- `harmony/sync/testnet/1/1.0.0/0` (2025-05-07 14:02:19)
- `/f2f-share/fetch/0.0.1` (2025-05-09 12:01:53)
- `/rats/2.0.0` (2025-05-10 14:01:46)
- `/rats/2.0.0/file` (2025-05-10 14:01:46)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `172.233.243.82` | FR | 83 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 83 | ['edgevpn']| True  |
| `116.203.135.82` | DE | 40 | ['kubo/0.21.0/docker']| True  |
| `91.230.153.86` | RU | 39 | ['edgevpn']| False  |
| `101.78.97.56` | SG | 29 | ['kubo/0.32.1/']| False  |
| `128.79.63.31` | FR | 28 | ['kubo/0.32.1/']| False  |
| `2001:861:3190:8fa0:d15d:f145:24d3:d256` | FR | 28 | ['kubo/0.32.1/']| False  |
| `80.77.36.40` | UA | 25 | ['kubo/0.32.1/']| False  |
| `38.101.215.12` | US | 25 | ['p2pd/0.1']| False  |
| `95.217.209.25` | FI | 20 | ['kubo/0.35.0-dev/ddeb3a41c-dirty']| True  |

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

In the specified time interval from `2025-05-05` to `2025-05-12` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-05-05` to `2025-05-12` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-05-05` to `2025-05-12` in the DHT and their datacenter association.

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