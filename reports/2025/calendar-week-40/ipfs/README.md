# Nebula Measurement Results Calendar Week 40 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 40 - 2025](#nebula-measurement-results-calendar-week-40---2025)
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

The following results show measurement data that were collected in calendar week 40 in 2025 from `2025-10-06` to `2025-10-13`.

- Number of crawls `84`
- Number of visits `9,418,931`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `63,020`
- Number of unique peer IDs discovered in the DHT `62,859`
- Number of unique IP addresses found `33,658`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20251006053813` (2025-10-06 12:01:17)
- `bootnode-20251006123714` (2025-10-06 12:04:08)
- `jackalnft@9dbd158be-dirty` (2025-10-06 16:04:34)
- `kubo/0.39.0-dev/2b5adee` (2025-10-06 16:06:12)
- `github.com/harmony-one/harmony@v1.10.3-0.20251006165247-2e96f8a9c422` (2025-10-06 20:04:06)
- `github.com/bitcoin-sv/teranode@v0.9.99-0.20251006170523-ce2aa64a21dd+dirty` (2025-10-06 22:02:07)
- `github.com/weisyn/v1@` (2025-10-07 04:05:26)
- `github.com/harmony-one/harmony@v1.10.3-0.20251006165247-2e96f8a9c422+dirty` (2025-10-07 16:04:18)
- `github.com/bitcoin-sv/teranode@v0.9.99-0.20251007152504-afde6454fad4+dirty` (2025-10-07 18:02:17)
- `github.com/JackalLabs/sequoia@v1.3.3-0.20251008133204-2b7a579fbb22` (2025-10-08 14:04:28)
- `kubo/0.37.0-dev/c631f6c0c-dirty` (2025-10-08 14:05:24)
- `github.com/bitcoin-sv/teranode@v0.9.99-0.20251008155857-aa9d0aa9d751+dirty` (2025-10-08 16:01:47)
- `kubo/0.39.0-dev/` (2025-10-08 18:01:35)
- `kubo/0.39.0-dev/f4834e7/docker` (2025-10-08 18:04:47)
- `kubo/0.38.1/fb14754/👁️�🗨️ÄñЖ中あ📝 ⟨ع|א|ქ|አ|থ|සි⟩ ΩΣΔΦ±∞ ñoñ-ÅSCÏÏ→UTF8️⃣ 語文字=🎨 ÖÜẞÞ♠♥♦♣ ∀x∈🌍:x→💫` (2025-10-08 20:01:19)
- `kubo/0.38.1/6bf52ae` (2025-10-08 20:04:24)
- `kubo/0.38.1/6bf52ae/docker` (2025-10-08 20:05:20)
- `kubo/0.38.1/6bf52ae/👁️�🗨️ÄñЖ中あ📝 ⟨ع|א|ქ|አ|থ|සි⟩ ΩΣΔΦ±∞ ñoñ-ÅSCÏÏ→UTF8️⃣ 語文字=🎨 ÖÜẞÞ♠♥♦♣ ∀x∈🌍:x→💫` (2025-10-09 00:04:34)
- `kubo/0.38.1/` (2025-10-09 00:06:31)
- `kubo/0.38.1/Homebrew` (2025-10-09 06:05:00)
- `ca-vsc@v0.0.0-20251007194841-4c5b6f20e2b9+dirty` (2025-10-09 10:06:06)
- `github.com/bitcoin-sv/teranode@v0.9.99-0.20251009122301-d092e422f034+dirty` (2025-10-09 14:02:55)
- `kubo/0.39.0-dev/c04781c/docker` (2025-10-09 14:02:55)
- `kubo/0.38.1/desktop` (2025-10-09 14:05:32)
- `kubo/0.38.1/riscv64-test` (2025-10-09 16:03:24)
- `kubo/0.38.1/6bf52ae/bootstrap.libp2p.io` (2025-10-09 18:01:03)
- `github.com/JackalLabs/sequoia@v1.3.3-0.20251009185819-8d894a78a98a` (2025-10-09 20:03:18)
- `github.com/JackalLabs/sequoia@v1.3.3-0.20251008170350-1b7854a1e975` (2025-10-09 20:06:10)
- `github.com/JackalLabs/sequoia@v1.3.3-0.20251009185819-8d894a78a98a+dirty` (2025-10-09 22:01:20)
- `kubo/0.38.1/6bf52ae/collab.ipfscluster.io` (2025-10-09 22:04:27)
- `kubo/0.39.0-dev/c04781c` (2025-10-10 16:04:02)
- `github.com/bsv-blockchain/teranode@` (2025-10-10 16:06:20)
- `github.com/bsv-blockchain/teranode@v0.9.99-0.20251010174809-4d0daa497cac+dirty` (2025-10-10 18:01:15)
- `github.com/bsv-blockchain/teranode@v0.11.6-wip-1.0.20251010175830-52b72ac36a8a+dirty` (2025-10-10 18:03:01)
- `github.com/bsv-blockchain/teranode@v0.9.99-0.20251011012947-5a8f80000ab3+dirty` (2025-10-12 06:03:15)
- `kubo/0.38.1/qkpay` (2025-10-12 12:05:05)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:



### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `49.49.243.57` | TH | 151 | ['p2pd/0.1']| False  |
| `49.49.235.131` | TH | 117 | ['p2pd/0.1']| False  |
| `2a00:15c9::4182` | IR | 79 | ['edgevpn']| False  |
| `109.122.253.245` | IR | 79 | ['edgevpn']| False  |
| `172.33.0.2` | US | 51 | ['kubo/0.35.0/a78d155/docker', 'kubo/0.37.0/6898472/docker']| False  |
| `2a01:4f8:1c1e:79b9::1` | DE | 50 | ['edgevpn']| True  |
| `162.55.183.24` | DE | 50 | ['edgevpn']| True  |
| `172.33.0.4` | US | 38 | ['kubo/0.35.0/a78d155/docker', 'kubo/0.37.0/6898472/docker']| False  |
| `65.108.15.100` | FI | 37 | ['kubo/0.37.0/']| True  |
| `34.132.203.230` | US | 35 | ['p2pd/0.1']| True  |

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

In the specified time interval from `2025-10-06` to `2025-10-13` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-10-06` to `2025-10-13` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-10-06` to `2025-10-13` in the DHT and their datacenter association.

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