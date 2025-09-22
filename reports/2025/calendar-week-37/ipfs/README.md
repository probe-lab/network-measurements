# Nebula Measurement Results Calendar Week 37 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 37 - 2025](#nebula-measurement-results-calendar-week-37---2025)
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

The following results show measurement data that were collected in calendar week 37 in 2025 from `2025-09-15` to `2025-09-22`.

- Number of crawls `84`
- Number of visits `9,862,763`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `66,351`
- Number of unique peer IDs discovered in the DHT `66,177`
- Number of unique IP addresses found `40,667`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `helia/5.5.1 js-libp2p/2.9.0 node/24.6.0` (2025-09-15 00:03:00)
- `kubo/0.38.0-dev/38be790/docker` (2025-09-16 00:04:04)
- `github.com/licketyspliket/ipfs@v0.0.0-20250915223223-97e33ca7ebb3+dirty` (2025-09-16 02:01:09)
- `oprueba.com/p2pTun@v1.0.0+dirty` (2025-09-16 12:05:21)
- `ca-vsc@v0.0.0-20250916154527-fc63c5beb1ca` (2025-09-16 18:01:04)
- `delta@8746d819f-dirty` (2025-09-16 18:03:04)
- `github.com/bpfs/v4@1406901e4-dirty` (2025-09-17 00:05:37)
- `github.com/bpfs/v4@5293bcd61-dirty` (2025-09-17 04:02:18)
- `kubo/0.38.0-dev/38be7908b` (2025-09-17 10:02:20)
- `kubo/0.38.0-dev/38be790` (2025-09-17 22:01:07)
- `js-libp2p/2.10.0 node/20.19.3` (2025-09-18 16:05:18)
- `kubo/0.38.0-dev/006f9dc/docker` (2025-09-18 16:05:48)
- `kubo/0.38.0-dev/e597e15c0-dirty` (2025-09-18 18:05:33)
- `js-libp2p/2.10.0 node/22.5.1` (2025-09-18 20:06:13)
- `kubo/0.38.0-dev/d37b92b/docker` (2025-09-19 02:06:16)
- `kubo/0.38.0-dev/6e38f6f/docker` (2025-09-19 08:03:43)
- `kubo/0.39.0-dev/22f0377/docker` (2025-09-19 22:01:18)
- `kubo/0.38.0-rc1/d4b446b/1234567890123456789012345678901234567890` (2025-09-19 22:05:53)
- `kubo/0.38.0-rc1/riscv64-test` (2025-09-20 00:01:11)
- `kubo/0.38.0-rc1/d4b446b` (2025-09-20 02:01:03)
- `kubo/0.38.0-rc1/` (2025-09-20 02:05:07)
- `github.com/JackalLabs/sequoia@v1.3.2` (2025-09-20 02:05:28)
- `kubo/0.38.0-rc1/d4b446b/docker` (2025-09-20 12:04:01)
- `kubo/0.38.0-rc1/d4b446b/collab.ipfscluster.io` (2025-09-21 06:01:06)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/bpfs/blockchain/tx_direct/1.0.0` (2025-09-17 00:05:37)
- `/bpfs/consensus/heartbeat/1.0.0` (2025-09-17 00:05:37)
- `/bpfs/sync/kbucket/1.0.0` (2025-09-17 00:05:37)
- `/bpfs/sync/range_paginated/1.0.0` (2025-09-17 00:05:37)
- `/weisyn/consensus/heartbeat/1.0.0` (2025-09-18 04:02:20)
- `/weisyn/consensus/block_submission/1.0.0` (2025-09-18 04:02:20)
- `/weisyn/sync/kbucket/1.0.0` (2025-09-18 04:02:20)
- `/weisyn/blockchain/tx_direct/1.0.0` (2025-09-18 04:02:20)
- `/weisyn/sync/range_paginated/1.0.0` (2025-09-18 04:02:20)
- `/owl-whisper/chat/1.0.0` (2025-09-18 14:07:08)
- `/owl-whisper/file/1.0.0` (2025-09-18 14:07:08)
- `/kmsg/mailbox/1.0` (2025-09-18 16:05:18)
- `/kmsg/receipts/1.0` (2025-09-18 16:05:18)
- `/kmsg/wallet-discovery/1.0` (2025-09-18 16:05:18)
- `/kmsg/relay/1.0` (2025-09-18 16:05:18)
- `/kmsg/session-establishment/1.0` (2025-09-18 16:05:18)
- `/kmsg/prekey-bundle/1.0` (2025-09-18 16:05:18)
- `/kmsg/test-message/1.0` (2025-09-18 16:05:18)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `107.170.62.220` | US | 220 | ['p2pd/0.1']| True  |
| `162.243.196.28` | US | 209 | ['p2pd/0.1']| True  |
| `192.241.186.58` | US | 187 | ['p2pd/0.1']| True  |
| `109.122.253.245` | IR | 66 | ['edgevpn']| False  |
| `2a00:15c9::4182` | IR | 66 | ['edgevpn']| False  |
| `172.33.0.2` | US | 41 | ['kubo/0.35.0/a78d155/docker']| False  |
| `162.55.183.24` | DE | 40 | ['edgevpn']| True  |
| `2a01:4f8:1c1e:79b9::1` | DE | 40 | ['edgevpn']| True  |
| `49.12.81.229` | DE | 39 | ['kubo/0.37.0/']| True  |
| `91.230.153.86` | RU | 32 | ['edgevpn']| False  |

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

In the specified time interval from `2025-09-15` to `2025-09-22` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-09-15` to `2025-09-22` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-09-15` to `2025-09-22` in the DHT and their datacenter association.

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