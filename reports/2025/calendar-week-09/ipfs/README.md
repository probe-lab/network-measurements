# Nebula Measurement Results Calendar Week 9 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 9 - 2025](#nebula-measurement-results-calendar-week-9---2025)
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

The following results show measurement data that were collected in calendar week 9 in 2025 from `2025-03-03` to `2025-03-10`.

- Number of crawls `84`
- Number of visits `9,661,012`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `49,279`
- Number of unique peer IDs discovered in the DHT `48,924`
- Number of unique IP addresses found `53,573`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `ca-vsc@v0.0.0-20250303122935-dbbc24ca915b` (2025-03-04 06:01:08)
- `bootnode-20250304070940` (2025-03-04 08:01:45)
- `@libp2p/amino-dht-bootstrapper/1.8.26 js-libp2p/2.8.0 node/22.14.0` (2025-03-04 10:01:15)
- `p2p_win@e7aeeb8fe-dirty` (2025-03-04 10:01:37)
- `kubo/0.34.0-dev/bb9e95d9a-dirty` (2025-03-04 12:01:07)
- `github.com/harmony-one/harmony@85424e63c` (2025-03-04 12:02:00)
- `kubo/0.33.0-dev/820bb0755` (2025-03-04 14:01:36)
- `kubo/0.34.0-dev/4c29169/docker` (2025-03-04 14:01:48)
- `github.com/harmony-one/harmony@85424e63c-dirty` (2025-03-04 14:02:03)
- `ca-vsc@v0.0.0-20250304171112-fb0dea2d3a04` (2025-03-04 18:01:51)
- `github.com/JackalLabs/sequoia@f2447f375` (2025-03-04 20:01:13)
- `github.com/JackalLabs/sequoia@8aefdf1bd` (2025-03-04 22:01:22)
- `kubo/0.34.0-dev/5a3ec3a/docker` (2025-03-04 22:01:46)
- `github.com/JackalLabs/sequoia@v1.1.8-0.20250304202315-e81350a4c3eb` (2025-03-04 22:01:56)
- `github.com/harmony-one/harmony@bb93067dd` (2025-03-05 00:01:18)
- `bootnode-20250304220811` (2025-03-05 00:01:26)
- `helia/5.2.1 js-libp2p/2.8.0 node/20.15.1` (2025-03-05 00:01:57)
- `feishup2pclient@9f24fea66-dirty` (2025-03-05 06:01:46)
- `kubo/0.34.0-dev/86aee74/docker` (2025-03-05 08:01:19)
- `kubo/0.33.0-dev/820bb0755-dirty` (2025-03-05 14:01:36)
- `kubo/0.34.0-rc1/3a8320d/1234567890123456789012345678901234567890` (2025-03-06 00:01:23)
- `kubo/0.34.0-dev/e221e94/docker` (2025-03-06 00:02:02)
- `libp2p/1.9.1 UserAgent=v20.17.0` (2025-03-06 00:02:04)
- `kubo/0.34.0-rc1/3a8320d` (2025-03-06 02:01:16)
- `kubo/0.35.0-dev/3e1fb7e/docker` (2025-03-06 02:01:18)
- `kubo/0.34.0-rc1/` (2025-03-06 02:01:20)
- `github.com/JackalLabs/sequoia@e81350a4c` (2025-03-06 02:01:22)
- `bootnode-20250306054127` (2025-03-06 06:02:04)
- `github.com/harmony-one/harmony@a90922918` (2025-03-06 10:01:03)
- `kubo/0.34.0-rc1/3a8320d/docker` (2025-03-06 10:01:07)
- `@libp2p/amino-dht-bootstrapper/1.8.27 js-libp2p/2.8.0 node/22.14.0` (2025-03-06 10:01:08)
- `bootnode-20250306025927` (2025-03-06 10:01:19)
- `bootnode-20250306100235` (2025-03-06 10:01:19)
- `bootnode-20250306095929` (2025-03-06 10:01:51)
- `@libp2p/amino-dht-bootstrapper/1.8.28 js-libp2p/2.8.0 node/22.14.0` (2025-03-06 12:01:20)
- `p2p_win@68a671a3d-dirty` (2025-03-06 14:01:40)
- `ca-vsc@v0.0.0-20250306140301-0be4b0740f75` (2025-03-06 18:01:04)
- `bootnode-20250306235744` (2025-03-07 00:01:32)
- `kubo/0.35.0-dev/3e1fb7e51-dirty` (2025-03-07 04:01:05)
- `js-libp2p/2.5.0 UserAgent=v23.3.0` (2025-03-07 08:01:16)
- `github.com/harmony-one/harmony@f9aed67ad-dirty` (2025-03-07 08:01:39)
- `p2p_win@4b7a11daa-dirty` (2025-03-07 12:01:37)
- `ca-vsc@v0.0.0-20250306072038-8b29de3bea5f` (2025-03-07 16:01:05)
- `kubo/0.35.0-dev/3e1fb7e51` (2025-03-07 18:01:16)
- `bootnode-20250307234536` (2025-03-08 00:01:25)
- `kubo/0.33.2/debox/0.3.0` (2025-03-08 00:01:50)
- `kubo/0.34.0-rc1/desktop` (2025-03-08 04:01:40)
- `kubo/0.33.0-dev/759d5a56f-dirty` (2025-03-08 10:01:56)
- `bootnode-20250309020152` (2025-03-09 04:01:39)
- `p2p_win@6a7f10940-dirty` (2025-03-09 16:01:06)
- `bootnode-20250309164853` (2025-03-09 18:01:28)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/orbitdb/heads/orbitdb/zdpuAu9t5Avi2BVBEu3wjDTBcMYTyUKnuqPx3saFUKEw6GXhc` (2025-03-07 08:01:16)
- `/orbitdb/heads/orbitdb/zdpuAyvkTHk4w8wMTVCjvDRrFQpeGyYdrgoK48ufj8B5WgZst` (2025-03-07 08:01:16)
- `/orbitdb/heads/orbitdb/zdpuAyM5AWffHSqTtxf2KubRARvwYFTycfuQX4ZG4MhhdyUML` (2025-03-07 08:01:16)
- `/orbitdb/heads/orbitdb/zdpuB29HS4Pd9vjr4qs9NdfEH5TCmVPqoHm9frf9c77Crq7Z5` (2025-03-07 08:01:16)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `2001:41d0:8:926e::1` | FR | 84 | ['edgevpn']| True  |
| `5.39.80.110` | FR | 84 | ['edgevpn']| True  |
| `88.99.172.194` | DE | 51 | ['kubo/0.18.1/675f8bd/docker', 'kubo/0.29.0/3f0947b']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 46 | ['edgevpn']| True  |
| `172.233.243.82` | FR | 46 | ['edgevpn']| True  |
| `89.89.190.64` | FR | 41 | ['kubo/0.32.1/']| False  |
| `80.77.36.40` | UA | 33 | ['kubo/0.32.1/']| False  |
| `91.230.153.86` | RU | 32 | ['edgevpn']| False  |
| `142.93.215.219` | IN | 32 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| True  |
| `86.98.210.180` | AE | 25 | ['kubo/0.32.1/']| False  |

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

In the specified time interval from `2025-03-03` to `2025-03-10` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-03-03` to `2025-03-10` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-03-03` to `2025-03-10` in the DHT and their datacenter association.

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