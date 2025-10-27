# Nebula Measurement Results Calendar Week 42 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 42 - 2025](#nebula-measurement-results-calendar-week-42---2025)
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

The following results show measurement data that were collected in calendar week 42 in 2025 from `2025-10-20` to `2025-10-27`.

- Number of crawls `80`
- Number of visits `8,068,553`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `59,552`
- Number of unique peer IDs discovered in the DHT `59,402`
- Number of unique IP addresses found `35,780`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/bsv-blockchain/teranode@v0.9.99-0.20251020093033-e42fdba7eb8e+dirty` (2025-10-20 12:02:28)
- `kubo/0.38.1/gateway` (2025-10-20 12:05:01)
- `github.com/harmony-one/harmony@v1.10.3-0.20251020150931-8c696208c60f` (2025-10-20 18:04:17)
- `github.com/bsv-blockchain/teranode@v0.11.17-0.20251020090344-17d3c1e35321` (2025-10-20 18:05:02)
- `github.com/bsv-blockchain/teranode@v0.9.99-0.20251020124211-3d0216ea37f2+dirty` (2025-10-20 20:03:25)
- `helia/6.0.2 js-libp2p/3.0.6 node/20.19.5` (2025-10-20 22:03:02)
- `kubo/0.38.1/svc` (2025-10-21 00:06:13)
- `kubo/0.36.0/svc` (2025-10-21 02:02:15)
- `github.com/bsv-blockchain/teranode@v0.11.17-0.20251021004217-f6396b578d61` (2025-10-21 02:04:13)
- `bootnode-20251021044049` (2025-10-21 06:01:14)
- `js-libp2p/0.45.9 UserAgent=v22.18.0` (2025-10-22 08:01:15)
- `github.com/bsv-blockchain/teranode@v0.9.99-0.20251021143409-17094d53181f+dirty` (2025-10-22 08:06:12)
- `github.com/bsv-blockchain/teranode@v0.9.99-0.20251022100605-6d9ee0495acb+dirty` (2025-10-22 12:01:22)
- `github.com/bsv-blockchain/teranode@v0.11.18-0.20251022145105-e246183b8160+dirty` (2025-10-22 16:04:25)
- `ca-vsc@v0.0.0-20251022153655-f86f21c1c033` (2025-10-22 16:05:09)
- `github.com/JackalLabs/sequoia@v1.3.3-0.20251022175044-8b3a8cab32c8+dirty` (2025-10-22 18:01:10)
- `go-libp2p/example/autotls` (2025-10-23 16:03:03)
- `github.com/bsv-blockchain/teranode@v0.11.19-0.20251023130813-33fed0e5170a` (2025-10-23 18:03:20)
- `kubo/0.39.0-dev/0cc232b-dirty` (2025-10-23 20:02:13)
- `kubo/0.39.0-dev/16479ec/docker` (2025-10-23 20:04:55)
- `bootnode-20251024093451` (2025-10-24 08:01:11)
- `bootnode-20251024023312` (2025-10-24 08:01:23)
- `bootnode-20251024093314` (2025-10-24 08:02:10)
- `github.com/harmony-one/harmony@v1.10.3-0.20251023154445-c2d0f2fb9587` (2025-10-24 08:02:39)
- `kubo/0.39.0-dev/886ac22/docker` (2025-10-24 10:02:45)
- `kubo/0.39.0-dev/ae78c78/docker` (2025-10-25 04:03:02)
- `kubo/0.39.0-dev/8a15763a6/riscv64-test` (2025-10-25 16:01:04)
- `kubo/0.39.0-dev/ae78c7821` (2025-10-25 22:04:19)
- `kubo/0.39.0-dev/8a15763/👁️�🗨️ÄñЖ中あ📝 ⟨ع|א|ქ|አ|থ|සි⟩ ΩΣΔΦ±∞ ñoñ-ÅSCÏÏ→UTF8️⃣ 語文字=🎨 ÖÜẞÞ♠♥♦♣ ∀x∈🌍:x→💫` (2025-10-26 02:03:34)
- `bootnode-20251026135804` (2025-10-26 14:02:19)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/warp/exchange` (2025-10-22 14:03:31)
- `/warp/discovery` (2025-10-22 14:03:31)
- `/warp/identity` (2025-10-22 14:03:31)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `49.49.241.108` | TH | 105 | ['p2pd/0.1']| False  |
| `152.81.47.226` | FR | 70 | ['kubo/0.33.0/', 'kubo/0.37.0/']| False  |
| `109.122.253.245` | IR | 67 | ['edgevpn']| False  |
| `2a00:15c9::4182` | IR | 67 | ['edgevpn']| False  |
| `3.127.244.115` | DE | 52 | ['kubo/0.39.0-dev/0cc232b-dirty', 'kubo/0.39.0-dev/cf8194a8d-dirty']| True  |
| `49.49.239.15` | TH | 44 | ['p2pd/0.1']| False  |
| `91.227.33.28` | US | 41 | ['kubo/0.37.0/']| False  |
| `172.33.0.2` | US | 41 | ['kubo/0.35.0/a78d155/docker', 'kubo/0.37.0/6898472/docker']| False  |
| `34.63.61.122` | US | 40 | ['p2pd/0.1']| True  |
| `34.9.182.32` | US | 40 | ['p2pd/0.1']| True  |

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

In the specified time interval from `2025-10-20` to `2025-10-27` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-10-20` to `2025-10-27` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-10-20` to `2025-10-27` in the DHT and their datacenter association.

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