# Nebula Measurement Results Calendar Week 6 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 6 - 2025](#nebula-measurement-results-calendar-week-6---2025)
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

The following results show measurement data that were collected in calendar week 6 in 2025 from `2025-02-10` to `2025-02-17`.

- Number of crawls `84`
- Number of visits `10,081,461`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `51,235`
- Number of unique peer IDs discovered in the DHT `50,720`
- Number of unique IP addresses found `57,994`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `helia/5.2.0 js-libp2p/2.5.2 UserAgent=v20.18.2` (2025-02-10 06:01:13)
- `bootnode-20250210063724` (2025-02-10 08:01:38)
- `bootnode-20250210113646` (2025-02-10 12:01:26)
- `bootnode-20250210125656` (2025-02-10 12:01:29)
- `kubo/0.34.0-dev/e77a484/docker` (2025-02-10 16:01:38)
- `kubo/0.34.0-dev/e77a484aa` (2025-02-10 18:01:10)
- `bootnode-20250205153649` (2025-02-10 22:01:37)
- `helia/5.2.0 js-libp2p/2.6.1 UserAgent=v22.13.1` (2025-02-11 06:01:56)
- `kubo/0.33.0/Homebrew` (2025-02-11 08:01:42)
- `github.com/harmony-one/harmony@72e90f75a-dirty` (2025-02-11 10:01:59)
- `rust-libp2p/0.46.0` (2025-02-11 10:02:01)
- `kubo/0.33.1/9bfbc4e52-dirty` (2025-02-11 12:01:25)
- `js-libp2p/2.4.2 UserAgent=v23.6.0` (2025-02-11 14:02:00)
- `kubo/0.33.1/f486266/bootstrap.libp2p.io` (2025-02-12 00:01:01)
- `kubo/0.34.0-dev/d137d7a/docker` (2025-02-12 00:02:10)
- `jackalnft@d89ea89c3-dirty` (2025-02-12 04:01:41)
- `bootnode-20250212044111` (2025-02-12 06:01:50)
- `jackalnft@ce2377178-dirty` (2025-02-12 08:01:05)
- `github.com/harmony-one/harmony@0da69c182-dirty` (2025-02-12 10:01:07)
- `ca-vsc@894109d6d` (2025-02-12 10:02:17)
- `ca-vsc@46fad1d9a` (2025-02-12 12:02:03)
- `bootnode-20250212150614` (2025-02-12 16:01:28)
- `js-libp2p/2.4.2 UserAgent=v23.1.0` (2025-02-12 16:02:12)
- `bootnode-20250210133530` (2025-02-12 18:01:09)
- `jackalnft@27e12dada-dirty` (2025-02-12 20:01:47)
- `jackalnft@deb3ebb83-dirty` (2025-02-12 22:01:57)
- `github.com/harmony-one/harmony@100fcba15-dirty` (2025-02-13 06:01:18)
- `ca-vsc@46fad1d9a-dirty` (2025-02-13 10:01:30)
- `p2proxy@78e9d7dba` (2025-02-13 16:01:17)
- `jackalnft@e31d4b84d-dirty` (2025-02-13 18:01:07)
- `helia/5.1.1 js-libp2p/2.4.2 UserAgent=v22.13.1` (2025-02-13 20:01:10)
- `jackalnft@9a3875c67-dirty` (2025-02-13 20:01:47)
- `kubo/0.33.2/8942a17/bootstrap.libp2p.io` (2025-02-13 22:01:04)
- `kubo/0.33.2/8942a17` (2025-02-13 22:01:05)
- `jackalnft@f517700ef-dirty` (2025-02-13 22:01:36)
- `kubo/0.33.2/ad1868a` (2025-02-14 00:01:02)
- `kubo/0.33.2/ad1868a/docker` (2025-02-14 00:01:06)
- `kubo/0.33.2/ad1868a/1234567890123456789012345678901234567890` (2025-02-14 00:01:20)
- `jackalnft@15bb87a02-dirty` (2025-02-14 00:02:01)
- `kubo/0.33.2/desktop` (2025-02-14 04:01:25)
- `kubo/0.34.0-dev/04982f3/docker` (2025-02-14 04:01:38)
- `bootnode-20250214034053` (2025-02-14 04:01:40)
- `github.com/harmony-one/harmony@c59f3d95f-dirty` (2025-02-14 04:02:04)
- `github.com/harmony-one/harmony@460c1a6e6` (2025-02-14 06:01:36)
- `kubo/0.33.2/` (2025-02-14 08:01:06)
- `p2proxy@5ca9fdd97` (2025-02-14 08:01:55)
- `github.com/harmony-one/harmony@876dca62e-dirty` (2025-02-14 08:01:58)
- `kubo/0.34.0-dev/04982f37f` (2025-02-14 08:02:17)
- `ca-vsc@52861ba0d` (2025-02-14 10:01:28)
- `kubo/0.34.0-dev/04982f37f-dirty` (2025-02-14 10:01:38)
- `kubo/0.33.2/Homebrew` (2025-02-14 12:01:23)
- `ca-vsc@1bbca4e76-dirty` (2025-02-14 12:01:40)
- `universal-connectivity/go-peer` (2025-02-14 12:02:03)
- `kubo/0.33.2/ad1868a/bootstrap.libp2p.io` (2025-02-14 16:01:03)
- `kubo/0.33.2/8942a17/bootstrap.libp2p.io/staging` (2025-02-14 16:01:03)
- `jackalnft@a8371ff4f-dirty` (2025-02-14 18:01:10)
- `kubo/0.33.2/ad1868a42/desktop` (2025-02-14 20:01:43)
- `kubo/0.34.0-dev/40a7a38/docker` (2025-02-14 22:01:23)
- `kubo/0.33.2/72876be-dirty` (2025-02-15 02:01:43)
- `bootnode-20250215124312` (2025-02-15 14:01:48)
- `libp2p/1.9.4 UserAgent=v20.18.3` (2025-02-15 18:01:41)
- `kubo/0.33.2/docker` (2025-02-15 22:01:38)
- `bootnode-20250216012704` (2025-02-16 02:01:11)
- `dvpncmd@2b2d5dcf4-hayek` (2025-02-16 16:01:17)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/orbitdb/heads/orbitdb/zdpuAzQi2wjs135VhWjj62XSSwPySfV41by5FUxme9fByZQDi` (2025-02-13 20:01:10)
- `/orbitdb/heads/orbitdb/zdpuAsJkrPQ9yVYVVGzAz4aeaCxLvxYL7xdrEED6HwU8inNEV` (2025-02-13 20:01:10)
- `/setupSync` (2025-02-14 02:01:12)
- `/postReleaseTxHash` (2025-02-14 02:01:12)
- `/postRefundTxHash` (2025-02-14 02:01:12)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `180.175.224.135` | CN | 103 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `5.39.80.110` | FR | 83 | ['edgevpn']| True  |
| `2001:41d0:8:926e::1` | FR | 83 | ['edgevpn']| True  |
| `80.106.161.133` | GR | 65 | ['kubo/0.32.1/']| False  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 51 | ['edgevpn']| True  |
| `172.233.243.82` | FR | 51 | ['edgevpn']| True  |
| `1.159.159.63` | AU | 49 | ['kubo/0.32.1/']| False  |
| `88.99.172.194` | DE | 40 | ['kubo/0.18.1/675f8bd/docker', 'kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| True  |
| `26.26.26.1` | US | 39 | ['gobind@', 'go-ipfs/0.8.0/48f94e2', 'kubo/0.28.0/']| False  |
| `91.230.153.86` | RU | 38 | ['edgevpn']| False  |

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

In the specified time interval from `2025-02-10` to `2025-02-17` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-02-10` to `2025-02-17` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-02-10` to `2025-02-17` in the DHT and their datacenter association.

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