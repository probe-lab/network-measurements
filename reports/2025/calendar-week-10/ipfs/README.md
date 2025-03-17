# Nebula Measurement Results Calendar Week 10 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 10 - 2025](#nebula-measurement-results-calendar-week-10---2025)
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

The following results show measurement data that were collected in calendar week 10 in 2025 from `2025-03-10` to `2025-03-17`.

- Number of crawls `84`
- Number of visits `9,758,613`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `47,168`
- Number of unique peer IDs discovered in the DHT `46,750`
- Number of unique IP addresses found `50,310`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `ca-vsc@v0.0.0-20250306072038-8b29de3bea5f+dirty` (2025-03-10 12:01:19)
- `kubo/0.35.0-dev/426060767` (2025-03-10 18:01:12)
- `kubo/0.35.0-dev/4260607/docker` (2025-03-10 18:01:51)
- `bootnode-20250310210515` (2025-03-10 22:01:30)
- `bootnode-20250311074815` (2025-03-11 08:01:39)
- `p2p_win@fc81dda4e-dirty` (2025-03-11 14:01:32)
- `js-libp2p/0.0.0 browser/Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36` (2025-03-11 18:01:42)
- `kubo/0.35.0-dev/095cc0d/docker` (2025-03-12 02:01:12)
- `js-libp2p/2.8.0 node/20.18.3` (2025-03-12 04:01:29)
- `p2proxy@0c4a78293` (2025-03-12 10:01:29)
- `kubo/0.33.0-dev/5d4b53a86-dirty` (2025-03-12 16:01:21)
- `kubo/0.30.0-dev/a50497b72` (2025-03-12 20:01:12)
- `bootnode-20250312182347` (2025-03-12 20:01:18)
- `kubo/0.30.0-dev/5f6682ad9-dirty` (2025-03-12 20:01:22)
- `kubo/0.34.0-dev/3793792` (2025-03-12 22:01:28)
- `bootnode-20250312214229` (2025-03-12 22:01:42)
- `kubo/0.35.0-dev/095cc0d73` (2025-03-13 04:01:04)
- `ca-vsc@v0.0.0-20250313044039-97c71b6e1ca8+dirty` (2025-03-13 06:01:06)
- `p2p_win@bcef83e86-dirty` (2025-03-13 06:01:39)
- `github.com/harmony-one/harmony@420cd947b` (2025-03-13 12:01:08)
- `kubo/0.34.0-dev/Homebrew` (2025-03-13 16:01:09)
- `kubo/0.35.0-dev/183dc7d/docker` (2025-03-14 02:01:10)
- `github.com/dcnetio/go-dcnode@c5217cea3-dirty` (2025-03-14 06:01:21)
- `kubo/0.33.0-dev/c831724bd-dirty` (2025-03-14 08:01:25)
- `bootnode-20250314134830` (2025-03-14 14:01:22)
- `bnsnet@v0.0.0-20250313192108-6ca2a112ad9b+dirty` (2025-03-14 14:01:53)
- `kubo/0.34.0-rc1/ca4b612/1234567890123456789012345678901234567890` (2025-03-14 18:01:09)
- `bootnode-20250314174855` (2025-03-14 18:01:16)
- `helia/5.2.0 js-libp2p/2.5.0 UserAgent=v20.9.0` (2025-03-14 18:01:20)
- `helia/2.0.3 js-libp2p/0.46.16 UserAgent=v18.20.6` (2025-03-14 18:01:36)
- `kubo/0.35.0-dev/b2efaa9/docker` (2025-03-14 18:01:47)
- `kubo/0.34.0-rc2/3d87596/1234567890123456789012345678901234567890` (2025-03-14 20:01:50)
- `kubo/0.34.0-rc2/3d87596` (2025-03-15 00:01:03)
- `kubo/0.34.0-rc2/` (2025-03-15 02:01:51)
- `github.com/dcnetio/go-dcnode@eb3dac5cb-dirty` (2025-03-15 06:01:06)
- `kubo/0.34.0-rc2/3d875968b` (2025-03-15 22:02:00)
- `bootnode-20250316025528` (2025-03-16 04:01:32)
- `kubo/0.33.0-dev/ca3735fa0-dirty` (2025-03-16 16:01:17)
- `bootnode-20250316185547` (2025-03-16 20:01:38)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/p2pmessage/1.0.0` (2025-03-11 16:01:11)
- `/mw/evm/0.0.1` (2025-03-11 18:01:42)
- `/secured/ping/1.0.0` (2025-03-11 18:01:42)
- `/orbitdb/heads/orbitdb/zdpuArkSmb5rDZbe5JYFeoyRWZN1hFBgsHFCt9opDi2Kj2AED` (2025-03-12 04:01:29)
- `/marz/1.0.0` (2025-03-13 02:01:22)
- `/dc/thread/0.0.1` (2025-03-14 06:01:21)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `2001:41d0:8:926e::1` | FR | 83 | ['edgevpn']| True  |
| `5.39.80.110` | FR | 83 | ['edgevpn']| True  |
| `172.233.243.82` | FR | 43 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 43 | ['edgevpn']| True  |
| `89.89.190.64` | FR | 39 | ['kubo/0.32.1/']| False  |
| `26.26.26.1` | US | 32 | ['go-ipfs/0.8.0/48f94e2', 'kubo/0.28.0/']| False  |
| `91.230.153.86` | RU | 31 | ['edgevpn']| False  |
| `86.98.210.180` | AE | 28 | ['kubo/0.32.1/']| False  |
| `2001:861:3a08:f3a0:d851:2b3f:ee65:5642` | FR | 27 | ['kubo/0.32.1/']| False  |
| `2001:8f8:153b:4075:4b62:9dc1:2919:c4a9` | AE | 21 | ['kubo/0.32.1/']| False  |

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

In the specified time interval from `2025-03-10` to `2025-03-17` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-03-10` to `2025-03-17` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-03-10` to `2025-03-17` in the DHT and their datacenter association.

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