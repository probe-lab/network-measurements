# Nebula Measurement Results Calendar Week 13 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 13 - 2025](#nebula-measurement-results-calendar-week-13---2025)
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

The following results show measurement data that were collected in calendar week 13 in 2025 from `2025-03-31` to `2025-04-07`.

- Number of crawls `84`
- Number of visits `9,699,850`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `48,224`
- Number of unique peer IDs discovered in the DHT `47,642`
- Number of unique IP addresses found `47,744`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/JackalLabs/sequoia@27ff270bd` (2025-03-31 02:01:37)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.1.0.20250330231014-27ff270bd592` (2025-03-31 04:01:29)
- `ca-vsc@v0.0.0-20250326084816-2f0c39a0fe7b` (2025-03-31 06:01:08)
- `github.com/harmony-one/harmony@c0a9ff05b-dirty` (2025-03-31 12:01:32)
- `ca-vsc@v0.0.0-20250331145907-ece4b4f57271+dirty` (2025-03-31 18:01:46)
- `github.com/harmony-one/harmony@80c42394e-dirty` (2025-04-01 00:01:37)
- `github.com/JackalLabs/sequoia@27ff270bd-dirty` (2025-04-01 04:01:44)
- `github.com/harmony-one/harmony@661948a08-dirty` (2025-04-01 08:01:37)
- `bootnode-20250401162842` (2025-04-01 18:01:50)
- `bootnode-20250401194613` (2025-04-01 20:01:23)
- `kubo/0.35.0-dev/fd50eb0/docker` (2025-04-02 02:01:28)
- `github.com/harmony-one/harmony@0acd42a4b` (2025-04-02 12:01:04)
- `helia/5.2.1 js-libp2p/2.7.2 node/22.14.0` (2025-04-02 12:01:56)
- `github.com/harmony-one/harmony@0acd42a4b-dirty` (2025-04-02 14:02:01)
- `kubo/0.35.0-dev/e3a8301/1234567890123456789012345678901234567890` (2025-04-02 16:01:39)
- `kubo/0.35.0-dev/e3a8301d9` (2025-04-02 16:01:43)
- `kubo/0.35.0-dev/e3a8301d9-dirty` (2025-04-02 18:01:27)
- `kubo/0.35.0-dev/fd50eb0fc-dirty` (2025-04-03 12:01:58)
- `bootnode-20250403143218` (2025-04-03 16:01:34)
- `bootnode-20250403173237` (2025-04-03 18:01:19)
- `github.com/harmony-one/harmony@v1.10.3-0.20250403180333-f905f11cb095` (2025-04-03 20:01:11)
- `kubo/0.35.0-dev/d7f0266/docker` (2025-04-04 00:01:50)
- `p2ptunnel@0edb529d3` (2025-04-04 08:01:08)
- `bootnode-20250404085732` (2025-04-04 14:01:49)
- `bootnode-20250404234352` (2025-04-05 00:01:27)
- `js-libp2p/2.8.2 node/20.19.0` (2025-04-05 04:02:12)
- `kubo/0.35.0-dev/249ee3f84` (2025-04-05 14:01:13)
- `bootnode-20250405143914` (2025-04-05 16:01:43)
- `kubo/0.34.1/4649554b7` (2025-04-05 22:01:50)
- `jackalnft@6f155ee80-dirty` (2025-04-06 04:01:52)
- `bootnode-20250406054908` (2025-04-06 06:01:26)
- `kubo/0.34.1/4649554/kubernetes` (2025-04-06 08:01:10)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.19.0` (2025-04-06 10:01:29)
- `jackalnft@b70ef8dab-dirty` (2025-04-06 16:02:02)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.2.0.20250406203602-fc55dd50ad0d` (2025-04-06 22:01:55)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/universal-connectivity-file/1` (2025-03-31 06:01:29)
- `/orbitdb/heads/orbitdb/zdpuAz8vihBggKBn1eNt1AndHHqyT6eH6nV5S7ASPYwvWJ15Y` (2025-04-05 04:02:12)
- `/orbitdb/heads/orbitdb/zdpuAnU6Nv5QcwE5JGQqZwV6jxPYxVgsin5Th4DPfLoTiY8MB` (2025-04-05 04:02:12)
- `/orbitdb/heads/orbitdb/zdpuB2HhTe1PBJRLExL4neoxKZNLQeGkTGC4Wn3eF1apdL2vg` (2025-04-05 06:01:20)
- `/orbitdb/heads/orbitdb/zdpuAu7UuLzWsRXpEKqUzu19sTW5Q1sLPuvTzwzASKkD58FxK` (2025-04-05 06:01:20)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `172.233.243.82` | FR | 41 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 41 | ['edgevpn']| True  |
| `89.89.190.64` | FR | 38 | ['kubo/0.32.1/']| False  |
| `69.53.12.84` | US | 35 | ['kubo/0.32.1/']| False  |
| `102.35.52.29` | RE | 34 | ['kubo/0.32.1/']| False  |
| `5.39.80.110` | FR | 33 | ['edgevpn']| True  |
| `26.26.26.1` | US | 33 | ['go-ipfs/0.8.0/48f94e2', 'kubo/0.22.0/desktop', 'kubo/0.28.0/', 'kubo/0.30.0/desktop']| False  |
| `2001:41d0:8:926e::1` | FR | 33 | ['edgevpn']| True  |
| `80.77.36.40` | UA | 27 | ['kubo/0.32.1/']| False  |
| `91.230.153.86` | RU | 26 | ['edgevpn']| False  |

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

In the specified time interval from `2025-03-31` to `2025-04-07` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-03-31` to `2025-04-07` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-03-31` to `2025-04-07` in the DHT and their datacenter association.

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