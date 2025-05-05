# Nebula Measurement Results Calendar Week 17 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 17 - 2025](#nebula-measurement-results-calendar-week-17---2025)
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

The following results show measurement data that were collected in calendar week 17 in 2025 from `2025-04-28` to `2025-05-05`.

- Number of crawls `84`
- Number of visits `9,872,077`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `70,800`
- Number of unique peer IDs discovered in the DHT `70,512`
- Number of unique IP addresses found `43,832`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `ca-vsc@v0.0.0-20250428051250-13a121d90eb9` (2025-04-28 08:01:55)
- `kubo/0.33.0-dev/05105ae7a-dirty` (2025-04-28 10:01:39)
- `bootnode-20250428113918` (2025-04-28 12:02:09)
- `github.com/harmony-one/harmony@v1.10.3-0.20250428135428-d60ca5a2af57` (2025-04-28 14:01:14)
- `github.com/harmony-one/harmony@v1.10.3-0.20250428051833-6b932cc879b1` (2025-04-28 14:02:14)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250428181028-bcd0219a47e4` (2025-04-28 20:02:41)
- `github.com/JackalLabs/sequoia@bcd0219a4` (2025-04-28 20:02:49)
- `kubo/0.33.0-dev/2aca7fc64-dirty` (2025-04-29 08:01:59)
- `js-libp2p/0.45.9 UserAgent=v22.15.0` (2025-04-29 08:02:24)
- `github.com/harmony-one/harmony@v1.10.3-0.20250428105256-f9c787096a97+dirty` (2025-04-29 14:01:18)
- `kubo/0.35.0-dev/ee5665d37-dirty` (2025-04-29 14:01:50)
- `js-libp2p/2.8.5 node/22.15.0` (2025-04-29 16:01:30)
- `dvpncmd@d5811d420-hayek` (2025-04-29 16:01:44)
- `kubo/0.35.0-dev/ef39965/docker` (2025-04-29 16:01:53)
- `kubo/0.35.0-dev/ef399655d` (2025-04-29 18:02:12)
- `kubo/0.35.0-dev/ef399655d-dirty` (2025-04-29 20:01:35)
- `p2proxy@f911a30cb-dirty` (2025-04-30 06:01:30)
- `fsp2pcloud@9bb450fa8-dirty` (2025-04-30 14:01:10)
- `dvpncmd@b159ecdba-hayek` (2025-04-30 14:02:07)
- `kubo/0.35.0-dev/e5e7cf180-dirty` (2025-04-30 16:02:33)
- `kubo/0.35.0-dev/b3973fa` (2025-04-30 22:01:31)
- `kubo/0.35.0-dev/7059620/docker` (2025-05-01 06:02:00)
- `github.com/harmony-one/harmony@v1.10.3-0.20250429130000-8e8fe33e9f04+dirty` (2025-05-01 12:01:36)
- `js-libp2p/2.5.0 UserAgent=v23.10.0` (2025-05-01 14:01:43)
- `kubo/0.35.0-dev/a5997375d-dirty/docker` (2025-05-01 16:01:13)
- `@libp2p/amino-dht-bootstrapper/1.9.4 js-libp2p/2.8.4 node/22.15.0` (2025-05-01 16:01:33)
- `kubo/0.33.0-dev/5e44b6005-dirty` (2025-05-02 08:02:01)
- `dvpncmd@d4b04c1c2-hayek` (2025-05-02 14:01:37)
- `bootnode-20250503061804` (2025-05-03 08:01:52)
- `notesapp@5223eb8c4-dirty` (2025-05-03 16:02:32)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/orbitdb/heads/orbitdb/zdpuAqHZogHB4sb75NTyYmuYGt8t7bDRXXubwAApgEo8NRy3Y` (2025-05-01 10:02:38)
- `/orbitdb/heads/orbitdb/zdpuAryxtr9h8VzdCWbQ1hJ8CjEsNK4Pi5qdAid7GcFtgqNEQ` (2025-05-01 10:02:38)
- `/orbitdb/heads/orbitdb/zdpuAtaSFpDjnoM49Ycs64fVbP51Qp7hopP1AudqjTAjpcAe5` (2025-05-01 10:02:38)
- `/orbitdb/heads/orbitdb/zdpuAphwZNVqF3casi3oFp8A1HwStmGhv351piXatHYwD1Sek` (2025-05-01 10:02:38)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 77 | ['edgevpn']| True  |
| `172.233.243.82` | FR | 77 | ['edgevpn']| True  |
| `88.99.172.194` | DE | 37 | ['kubo/0.29.0/3f0947b']| True  |
| `91.230.153.86` | RU | 35 | ['edgevpn']| False  |
| `26.26.26.1` | US | 31 | ['go-ipfs/0.8.0/48f94e2', 'kubo/0.28.0/']| False  |
| `123.181.11.122` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `47.219.42.123` | US | 19 | ['kubo/0.32.1/']| False  |
| `85.243.15.41` | PT | 19 | ['kubo/0.35.0-dev/', 'kubo/0.35.0-dev/2ff9f3406-dirty']| False  |
| `111.226.18.192` | CN | 18 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `60.244.138.148` | TW | 18 | ['go-ipfs/0.8.0/48f94e2']| False  |

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

In the specified time interval from `2025-04-28` to `2025-05-05` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-04-28` to `2025-05-05` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-04-28` to `2025-05-05` in the DHT and their datacenter association.

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