# Nebula Measurement Results Calendar Week 7 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 7 - 2025](#nebula-measurement-results-calendar-week-7---2025)
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

The following results show measurement data that were collected in calendar week 7 in 2025 from `2025-02-17` to `2025-02-24`.

- Number of crawls `84`
- Number of visits `9,933,897`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `52,838`
- Number of unique peer IDs discovered in the DHT `52,408`
- Number of unique IP addresses found `60,231`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.33.0-dev/124216309-dirty` (2025-02-17 16:01:14)
- `jackalnft@8f571def8-dirty` (2025-02-17 16:01:35)
- `kubo/0.33.2/ad1868a42-dirty` (2025-02-17 16:02:08)
- `jackalnft@2b11aca26-dirty` (2025-02-17 18:01:10)
- `bootnode-20250217183038` (2025-02-17 20:01:51)
- `kubo/0.34.0-dev/40a7a388a` (2025-02-18 02:01:25)
- `kubo/0.34.0-dev/e41dc12/docker` (2025-02-18 04:01:34)
- `github.com/wetware/go@v0.0.0-20250217231832-a4ddfce0f994+dirty` (2025-02-18 08:01:07)
- `bootnode-20250218094656` (2025-02-18 10:01:24)
- `kubo/0.34.0-dev/eb53bbf/docker` (2025-02-18 18:01:18)
- `kubo/0.34.0-dev/f00e115/docker` (2025-02-19 00:01:27)
- `jackalnft@c8258b842-dirty` (2025-02-19 04:01:54)
- `bootnode-20250219095929` (2025-02-19 10:01:09)
- `feishup2pclient@802e4aef7-dirty` (2025-02-19 12:01:26)
- `github.com/harmony-one/harmony@5357da280-dirty` (2025-02-19 14:01:24)
- `bootnode-20250219143358` (2025-02-19 16:01:07)
- `jackalnft@790232f6a-dirty` (2025-02-20 02:01:28)
- `ca-vsc@v0.0.0-20250220044051-91bd7aa39858` (2025-02-20 06:01:56)
- `kubo/0.33.2/ad1868a/collab.ipfscluster.io` (2025-02-20 12:01:14)
- `helia/5.2.1 js-libp2p/2.7.0 node/22.14.0` (2025-02-20 18:01:09)
- `feishup2pclient@2a61293fe-dirty` (2025-02-20 18:01:32)
- `bootnode-20250220180942` (2025-02-20 20:02:04)
- `bootnode-20250220150536` (2025-02-20 22:01:27)
- `js-libp2p/js-libp2p node/22.14.0` (2025-02-20 22:01:56)
- `p2p_win@ef1f12423-dirty` (2025-02-21 06:01:28)
- `bootnode-20250221093729` (2025-02-21 10:02:03)
- `p2p_win@c6f004c4c-dirty` (2025-02-21 14:01:31)
- `kubo/0.34.0-dev/9a4fffa/docker` (2025-02-21 22:01:16)
- `kubo/0.34.0-dev/9a4fffa35-dirty` (2025-02-22 00:01:56)
- `kubo/0.34.0-dev/56a0532/docker` (2025-02-22 02:01:24)
- `kubo/0.34.0-dev/96215c5/docker` (2025-02-22 04:01:35)
- `kubo/0.33.0-dev/b62a5aa7c-dirty` (2025-02-22 10:01:51)
- `@libp2p/amino-dht-bootstrapper/1.8.6 js-libp2p/2.7.2 node/22.14.0` (2025-02-22 10:01:52)
- `bootnode-20250222140139` (2025-02-22 14:01:54)
- `bootnode-20250223080102` (2025-02-23 08:01:13)
- `bootnode-20250223060551` (2025-02-23 08:01:42)
- `bootnode-20250223062925` (2025-02-23 08:01:44)
- `@libp2p/amino-dht-bootstrapper/1.8.7 js-libp2p/2.7.2 node/22.14.0` (2025-02-23 10:01:16)
- `bootnode-20250223100108` (2025-02-23 10:01:24)
- `@libp2p/amino-dht-bootstrapper/1.8.8 js-libp2p/0.0.0 node/22.14.0` (2025-02-23 16:01:48)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/sendParty12` (2025-02-17 10:01:11)
- `/getParty11` (2025-02-17 10:01:11)
- `/sendParty01` (2025-02-17 10:01:11)
- `/sendParty11` (2025-02-17 10:01:11)
- `ww/0.1.0` (2025-02-18 08:01:07)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `2001:41d0:8:926e::1` | FR | 84 | ['edgevpn']| True  |
| `5.39.80.110` | FR | 84 | ['edgevpn']| True  |
| `88.99.172.194` | DE | 71 | ['kubo/0.18.1/675f8bd/docker', 'kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| True  |
| `1.159.159.63` | AU | 53 | ['kubo/0.32.1/']| False  |
| `172.233.243.82` | FR | 52 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 52 | ['edgevpn']| True  |
| `142.93.215.219` | IN | 50 | ['kubo/0.17.0/', 'kubo/0.29.0/3f0947b']| True  |
| `2.85.41.176` | GR | 38 | ['kubo/0.32.1/']| False  |
| `91.230.153.86` | RU | 36 | ['edgevpn']| False  |
| `26.26.26.1` | US | 29 | ['feishup2pclient@8cdae9cb9-dirty', 'kubo/0.28.0/']| False  |

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

In the specified time interval from `2025-02-17` to `2025-02-24` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-02-17` to `2025-02-24` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-02-17` to `2025-02-24` in the DHT and their datacenter association.

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