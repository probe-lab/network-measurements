# Nebula Measurement Results Calendar Week 21 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 21 - 2025](#nebula-measurement-results-calendar-week-21---2025)
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

The following results show measurement data that were collected in calendar week 21 in 2025 from `2025-05-26` to `2025-06-02`.

- Number of crawls `84`
- Number of visits `8,468,394`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `61,703`
- Number of unique peer IDs discovered in the DHT `61,190`
- Number of unique IP addresses found `28,160`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `helia/5.4.2 js-libp2p/2.8.8 node/22.11.0` (2025-05-26 10:01:41)
- `oprueba.com/oos-agent@v0.0.0-20250526092956-419956987df7+dirty` (2025-05-26 12:01:29)
- `@libp2p/amino-dht-bootstrapper/1.9.8 js-libp2p/0.0.0 node/22.16.0` (2025-05-26 14:01:05)
- `ca-vsc@v0.0.0-20250526131644-b5e49211a2b2` (2025-05-26 14:01:37)
- `bootnode-20250526182709` (2025-05-26 22:01:48)
- `myjoypin/0.1.0` (2025-05-27 00:01:10)
- `ca-vsc@v0.0.0-20250526131644-b5e49211a2b2+dirty` (2025-05-27 00:01:32)
- `@libp2p/amino-dht-bootstrapper/1.9.9 js-libp2p/0.0.0 node/22.16.0` (2025-05-27 00:01:41)
- `oprueba.com/oos-agent@v0.0.0-20250527063348-3840a6ce3cca+dirty` (2025-05-27 08:01:32)
- `oprueba.com/oos-agent@v0.0.0-20250527090854-bdd23cf57ae3+dirty` (2025-05-27 10:01:26)
- `kubo/0.33.0-dev/52582a5b9-dirty` (2025-05-27 10:01:36)
- `github.com/harmony-one/harmony@v1.10.3-0.20250527084357-ca41a9970ed9` (2025-05-27 10:01:45)
- `bootnode-20250527122603` (2025-05-27 12:01:20)
- `bootnode-20250527062209` (2025-05-27 12:01:30)
- `bootnode-20250527131343` (2025-05-27 12:01:42)
- `bootnode-20250527052445` (2025-05-27 12:01:48)
- `bootnode-20250527131958` (2025-05-27 20:01:05)
- `kubo/0.36.0-dev/423720d1b-dirty` (2025-05-28 00:01:29)
- `kubo/0.36.0-dev/4144fa1` (2025-05-28 04:01:22)
- `kubo/0.36.0-dev/4144fa1b9-dirty` (2025-05-28 06:01:18)
- `bootnode-20250528095315` (2025-05-28 10:01:17)
- `ca-vsc@v0.0.0-20250528101809-a27a5f48e13f+dirty` (2025-05-28 12:01:12)
- `ca-vsc@v0.0.0-20250528101809-a27a5f48e13f` (2025-05-28 12:01:52)
- `ca-vsc@v0.0.0-20250528114437-c3d6b9c74c53` (2025-05-28 14:01:14)
- `kubo/0.36.0-dev/4144fa1/docker` (2025-05-28 14:01:42)
- `bootnode-20250528175944` (2025-05-28 18:01:11)
- `github.com/JackalLabs/sequoia@v1.3.0-alpha.3` (2025-05-28 20:01:18)
- `github.com/JackalLabs/sequoia@74c4428f6` (2025-05-28 20:01:22)
- `bootnode-20250528205322` (2025-05-28 20:01:24)
- `kubo/0.36.0-dev/4144fa1b9` (2025-05-28 20:01:32)
- `bootnode-20250528205158` (2025-05-28 20:01:36)
- `bootnode-20250528135038` (2025-05-28 20:01:50)
- `js-libp2p/0.45.9 UserAgent=v20.11.1` (2025-05-29 06:01:28)
- `@libp2p/amino-dht-bootstrapper/1.9.10 js-libp2p/2.8.8-d91ae66c6 node/22.16.0` (2025-05-29 10:01:41)
- `p2pd/go-libp2p@0.36.1` (2025-05-29 10:01:45)
- `github.com/harmony-one/harmony@v1.10.3-0.20250528144245-d8fa6fa2717a` (2025-05-29 12:01:18)
- `@libp2p/amino-dht-bootstrapper/1.9.11 js-libp2p/2.8.8-d91ae66c6 node/22.16.0` (2025-05-29 12:01:32)
- `ca-vsc@v0.0.0-20250528114437-c3d6b9c74c53+dirty` (2025-05-29 12:01:42)
- `kubo/0.36.0-dev/cf096c2a8` (2025-05-29 14:01:16)
- `kubo/0.36.0-dev/cf096c2` (2025-05-29 14:01:19)
- `libp2p/1.8.0` (2025-05-29 14:01:26)
- `kubo/0.36.0-dev/20d9660a6` (2025-05-29 16:01:23)
- `@libp2p/amino-dht-bootstrapper/1.9.13 js-libp2p/0.0.0 node/22.16.0` (2025-05-29 16:01:28)
- `bootnode-20250529143827` (2025-05-29 16:01:53)
- `@libp2p/amino-dht-bootstrapper/1.9.15 js-libp2p/0.0.0 node/22.16.0` (2025-05-29 20:01:20)
- `bootnode-20250529231449` (2025-05-30 00:01:48)
- `kubo/0.36.0-dev/cf096c2a8-dirty` (2025-05-30 04:01:42)
- `@libp2p/amino-dht-bootstrapper/1.9.19 js-libp2p/0.0.0 node/22.16.0` (2025-05-30 08:01:25)
- `@libp2p/amino-dht-bootstrapper/1.9.21 js-libp2p/0.0.0 node/22.16.0` (2025-05-30 12:01:50)
- `kubo/0.36.0-dev/cf096c2/docker` (2025-05-30 12:01:54)
- `@libp2p/amino-dht-bootstrapper/1.9.23 js-libp2p/2.8.8-6a3ae02f5 node/22.16.0` (2025-05-30 20:01:14)
- `kubo/0.36.0-dev/8f87a69/docker` (2025-05-31 00:02:04)
- `bootnode-20250531020236` (2025-05-31 04:01:11)
- `@libp2p/amino-dht-bootstrapper/1.9.24 js-libp2p/2.8.8-6a3ae02f5 node/22.16.0` (2025-05-31 12:01:06)
- `kubo/0.35.0/49e269000` (2025-06-01 02:01:30)
- `bootnode-20250601072221` (2025-06-01 08:01:50)
- `oprueba.com/oos-agent@v0.0.0-20250528151952-1585c9cfd765+dirty` (2025-06-01 10:01:31)
- `@libp2p/amino-dht-bootstrapper/1.9.25 js-libp2p/2.8.8-6a3ae02f5 node/22.16.0` (2025-06-01 14:01:20)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:



### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `82.180.162.171` | US | 370 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.30.0/846c5cc', 'kubo/0.33.2/', 'kubo/0.34.1/']| False  |
| `51.210.217.70` | FR | 101 | ['rust-ipfs']| True  |
| `91.230.153.86` | RU | 31 | ['edgevpn']| False  |
| `54.83.92.159` | US | 22 | ['kubo/0.36.0-dev/']| True  |
| `38.101.215.12` | US | 21 | ['p2pd/0.1']| False  |
| `123.181.15.116` | CN | 19 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `123.181.8.94` | CN | 19 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `89.89.190.64` | FR | 18 | ['kubo/0.32.1/']| False  |
| `116.203.135.82` | DE | 18 | ['kubo/0.21.0/docker']| True  |
| `162.55.243.101` | DE | 17 | ['kubo/0.33.2/', 'kubo/0.35.0/']| True  |

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

In the specified time interval from `2025-05-26` to `2025-06-02` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-05-26` to `2025-06-02` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-05-26` to `2025-06-02` in the DHT and their datacenter association.

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