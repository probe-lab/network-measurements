# Nebula Measurement Results Calendar Week 8 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 8 - 2025](#nebula-measurement-results-calendar-week-8---2025)
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

The following results show measurement data that were collected in calendar week 8 in 2025 from `2025-02-24` to `2025-03-03`.

- Number of crawls `84`
- Number of visits `9,665,664`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `51,743`
- Number of unique peer IDs discovered in the DHT `51,371`
- Number of unique IP addresses found `59,446`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/element-hq/dendrite@4f9183d83-dirty` (2025-02-24 10:01:09)
- `bootnode-20250224084947` (2025-02-24 10:01:26)
- `kubo/0.34.0-dev/f00e115e1` (2025-02-24 16:01:57)
- `kubo/0.34.0-dev/26bb4ca/docker` (2025-02-25 02:01:38)
- `jackalnft@b057020d3-dirty` (2025-02-25 02:02:01)
- `kubo/0.34.0-dev/26bb4ca27` (2025-02-25 04:01:02)
- `bootnode-20250225063951` (2025-02-25 08:01:15)
- `bootnode-20250225093708` (2025-02-25 10:01:05)
- `@libp2p/amino-dht-bootstrapper/1.8.12 js-libp2p/2.7.3 node/22.14.0` (2025-02-25 12:01:16)
- `kubo/0.34.0-dev/65a9b59/docker` (2025-02-25 12:01:19)
- `kubo/0.34.0-dev/baa94fc` (2025-02-26 00:01:04)
- `kubo/0.34.0-dev/baa94fc/1234567890123456789012345678901234567890` (2025-02-26 00:01:49)
- `kubo/0.34.0-dev/baa94fc/docker` (2025-02-26 02:01:25)
- `feishup2pclient@6f6b04610-dirty` (2025-02-26 10:01:04)
- `bootnode-20250226103312` (2025-02-26 12:01:09)
- `bootnode-20250226115818` (2025-02-26 12:01:25)
- `bootnode-20250226113806` (2025-02-26 12:02:00)
- `bootnode-20250226141218` (2025-02-26 14:01:20)
- `kubo/0.34.0-dev/baa94fcb2` (2025-02-26 14:01:29)
- `@libp2p/amino-dht-bootstrapper/1.8.15 js-libp2p/2.7.4 node/22.14.0` (2025-02-26 14:01:49)
- `bootnode-20250226141510` (2025-02-26 14:02:10)
- `bootnode-20250226070941` (2025-02-26 14:02:11)
- `bootnode-20250226080426` (2025-02-26 16:01:39)
- `kubo/0.33.0-dev/a71067981-dirty` (2025-02-26 18:02:04)
- `bootnode-20250226112806` (2025-02-26 20:01:28)
- `kubo/0.34.0-dev/f00e115e1-dirty` (2025-02-27 06:01:11)
- `bootnode-20250226150133` (2025-02-27 08:01:11)
- `github.com/harmony-one/harmony@185e52cf3` (2025-02-27 10:01:06)
- `kubo/0.34.0-dev/baa94fcb2-dirty` (2025-02-27 16:01:50)
- `github.com/element-hq/dendrite@c902bc025-dirty` (2025-02-27 16:02:03)
- `@libp2p/amino-dht-bootstrapper/1.8.17 js-libp2p/2.7.4 node/22.14.0` (2025-02-27 18:01:38)
- `bootnode-20250227210150` (2025-02-27 22:01:18)
- `ca-vsc@v0.0.0-20250228050624-f0bc5953dd21` (2025-02-28 06:01:08)
- `github.com/zzz136454872/upgradeable-consensus@e9e69ddf7-dirty` (2025-02-28 06:01:19)
- `p2proxy@889caa6e5` (2025-02-28 08:01:15)
- `github.com/harmony-one/harmony@806f2eb8a` (2025-02-28 10:01:19)
- `bootnode-20250228055747` (2025-02-28 12:01:11)
- `bootnode-20250228130017` (2025-02-28 12:02:05)
- `github.com/element-hq/dendrite@74c19f455-dirty` (2025-02-28 12:02:05)
- `bootnode-20250228130259` (2025-02-28 14:01:13)
- `bootnode-20250228155859` (2025-02-28 16:01:09)
- `kubo/0.33.0-dev/424130fb2-dirty` (2025-02-28 16:01:32)
- `@libp2p/amino-dht-bootstrapper/1.8.19 js-libp2p/2.7.4 node/22.14.0` (2025-02-28 22:01:50)
- `jackalnft@856b8a775-dirty` (2025-03-01 06:01:19)
- `@libp2p/amino-dht-bootstrapper/1.8.20 js-libp2p/2.7.4 node/22.14.0` (2025-03-01 08:01:51)
- `kubo/0.33.2/ad1868a42` (2025-03-01 10:01:41)
- `@libp2p/amino-dht-bootstrapper/1.8.21 js-libp2p/2.7.4 node/22.14.0` (2025-03-01 10:01:53)
- `@libp2p/amino-dht-bootstrapper/1.8.22 js-libp2p/2.7.4 node/22.14.0` (2025-03-01 20:01:38)
- `@libp2p/amino-dht-bootstrapper/1.8.23 js-libp2p/2.7.4 node/22.14.0` (2025-03-01 22:01:52)
- `kubo/0.33.2/ad1868a/kubernetes` (2025-03-01 22:01:56)
- `feishup2pclient@df019738b-dirty` (2025-03-02 02:01:31)
- `helia/5.2.1 js-libp2p/2.7.4 node/23.5.0` (2025-03-02 08:01:13)
- `bootnode-20250302080610` (2025-03-02 10:01:29)
- `github.com/harmony-one/harmony@5da780844` (2025-03-02 16:01:18)
- `@libp2p/amino-dht-bootstrapper/1.8.24 js-libp2p/2.7.4 node/22.14.0` (2025-03-02 20:01:26)
- `bootnode-20250302190504` (2025-03-02 20:01:57)
- `kubo/0.33.2/ad1868a/raylab.pro` (2025-03-02 22:01:08)
- `@libp2p/amino-dht-bootstrapper/1.8.25 js-libp2p/0.0.0 node/22.14.0` (2025-03-02 22:01:39)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/relay/sync/1.0` (2025-02-28 18:01:18)
- `/file-push/0.0.1` (2025-03-01 20:01:47)
- `/phpwebchain/1.0.0` (2025-03-02 18:01:30)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `2001:41d0:8:926e::1` | FR | 83 | ['edgevpn']| True  |
| `5.39.80.110` | FR | 83 | ['edgevpn']| True  |
| `172.233.243.82` | FR | 48 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 48 | ['edgevpn']| True  |
| `142.93.215.219` | IN | 44 | ['kubo/0.29.0/3f0947b', 'kubo/0.30.0/']| True  |
| `26.26.26.1` | US | 38 | ['kubo/0.28.0/']| False  |
| `91.230.153.86` | RU | 33 | ['edgevpn']| False  |
| `1.159.159.63` | AU | 28 | ['kubo/0.32.1/']| False  |
| `88.99.172.194` | DE | 26 | ['kubo/0.18.1/675f8bd/docker', 'kubo/0.29.0/3f0947b']| True  |
| `5.132.100.198` | NL | 22 | ['edgevpn']| False  |

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

In the specified time interval from `2025-02-24` to `2025-03-03` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-02-24` to `2025-03-03` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-02-24` to `2025-03-03` in the DHT and their datacenter association.

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