# Nebula Measurement Results Calendar Week 50 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 50 - 2023](#nebula-measurement-results-calendar-week-50---2023)
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

The following results show measurement data that were collected in calendar week 50 in 2023 from `2023-12-11` to `2023-12-18`.

- Number of crawls `336`
- Number of visits `53,405,102`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `183,349`
- Number of unique peer IDs discovered in the DHT `182,771`
- Number of unique IP addresses found `115,764`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `Avail Node/v1.8.2-d517e727f6a (SolsticeSculpt)` (2023-12-11 06:54:55)
- `kubo/0.25.0-rc1/0c6f08c/thunderdome` (2023-12-11 07:52:21)
- `Avail Node/v1.8.0-9c5f37b9230 (zkmehdi)` (2023-12-11 07:53:55)
- `kubo/0.26.0-dev/1a89365` (2023-12-11 08:52:38)
- `Avail Node/v1.8.2-d517e727f6a (WhisperingBreeze)` (2023-12-11 09:25:23)
- `Chainflip Node/v1.1.0-8c10b3a13a4 (gentle-able-7157)` (2023-12-11 11:24:16)
- `Gear Node/v0.3.1-5d8fb07221d (analizator31)` (2023-12-11 11:25:00)
- `Subspace CLI/v0.7.1-f1702c7d63256dfb55910dfe3d164a7cb1472b69 (oibek)` (2023-12-11 11:25:14)
- `Avail Node/v1.8.2-d517e727f6a (RadiantCalm)` (2023-12-11 12:25:02)
- `Avail Node/v1.8.2-d517e727f6a (MidnightMeadows)` (2023-12-11 12:25:16)
- `Avail Node/v1.8.2-d517e727f6a (1vasiliUs)` (2023-12-11 12:55:22)
- `Chainflip Node/v1.1.0-8c10b3a13a4 (miscreant-wren-7350)` (2023-12-11 23:24:59)
- `Avail Node/v1.8.2-d517e727f6a (Zeniths_)` (2023-12-11 23:55:04)
- `Avail Node/v1.8.2-d517e727f6a (EclipseThunderL)` (2023-12-11 23:55:09)
- `Avail Node/v1.8.2-d517e727f6a (Bunaitoswits)` (2023-12-12 01:25:07)
- `Avail Node/v1.8.2-d517e727f6a (BlockValidator)` (2023-12-12 01:54:50)
- `Avail Node/v1.8.3-a0820931850 (Tuneezi)` (2023-12-12 01:55:09)
- `Avail Node/v1.8.3-a0820931850 (dexsensei)` (2023-12-12 01:55:09)
- `Avail Node/v1.8.2-d517e727f6a (li0ity)` (2023-12-12 01:55:09)
- `Avail Node/v1.8.2-d517e727f6a (NUminantorS)` (2023-12-12 01:55:09)
- `Avail Node/v1.8.2-d517e727f6a (SecretZephyr)` (2023-12-12 02:24:49)
- `Avail Node/v1.8.2-d517e727f6a (EmberEcho)` (2023-12-12 02:25:14)
- `Avail Node/v1.8.3-a0820931850 (whiskeyboo)` (2023-12-12 05:24:52)
- `Avail Node/v1.8.2-d517e727f6a (Runnernuinarower)` (2023-12-12 06:55:14)
- `Avail Node/v1.8.2-d517e727f6a (Numikande)` (2023-12-12 09:25:14)
- `Avail Node/v1.8.2-d517e727f6a (Varietuswiere)` (2023-12-12 09:25:20)
- `Avail Node/v1.8.2-d517e727f6a (abc)` (2023-12-12 10:24:11)
- `Avail Node/v1.8.2-d517e727f6a (hafsda)` (2023-12-12 11:24:58)
- `Avail Node/v1.8.2-d517e727f6a (BrightFossa)` (2023-12-12 11:25:15)
- `Avail Node/v1.8.2-d517e727f6a (CactusCavalierE)` (2023-12-12 13:55:20)
- `Avail Node/v1.8.2-d517e727f6a (subspollule)` (2023-12-12 15:25:14)
- `Avail Node/v1.8.2-d517e727f6a (PixelFlux Technologies)` (2023-12-12 15:25:15)
- `Avail Node/v1.8.2-d517e727f6a (Maverne)` (2023-12-12 16:25:20)
- `Avail Node/v1.8.2-d517e727f6a (Enigma_)` (2023-12-12 20:54:59)
- `pw-p2p@ff0dceb37-dirty` (2023-12-12 21:52:34)
- `Avail Node/v1.8.0-9c5f37b9230 (piter)` (2023-12-12 23:55:02)
- `Avail Node/v1.8.2-d517e727f6a (BrightHawkmoth)` (2023-12-13 00:25:12)
- `Avail Node/v1.8.2-d517e727f6a (momic)` (2023-12-13 00:55:11)
- `Avail Node/v1.8.2-d517e727f6a (In2pect0RpaPa)` (2023-12-13 04:24:59)
- `Avail Node/v1.8.2-d517e727f6a (rolni)` (2023-12-13 04:55:05)
- `Avail Node/v1.8.2-d517e727f6a (CosmicCrusade)` (2023-12-13 04:55:08)
- `Avail Node/v1.8.2-d517e727f6a (SapphireTwilight)` (2023-12-13 07:25:11)
- `Avail Node/v1.8.2-d517e727f6a (RiftRider)` (2023-12-13 07:25:15)
- `Avail Node/v1.8.2-d517e727f6a (anave)` (2023-12-13 08:55:16)
- `Avail Node/v1.8.2-d517e727f6a (Nyraxia)` (2023-12-13 10:25:09)
- `kubo/0.25.0-rc1/0c6f08c/docker` (2023-12-13 10:53:13)
- `Avail Node/v1.8.2-d517e727f6a (PixelPatriarch)` (2023-12-13 11:25:13)
- `Avail Node/v1.8.2-d517e727f6a (magipoca)` (2023-12-13 13:24:33)
- `Avail Node/v1.8.2-d517e727f6a (Tuouferckiat)` (2023-12-13 13:25:16)
- `Avail Node/v1.8.2-d517e727f6a (Shierimitsu)` (2023-12-13 15:25:10)
- `Avail Node/v1.8.2-d517e727f6a (Zephyr_)` (2023-12-13 15:55:12)
- `Avail Node/v1.8.2-d517e727f6a (Credentialify)` (2023-12-13 16:25:07)
- `Avail Node/v1.8.2-d517e727f6a (squared)` (2023-12-13 17:25:09)
- `Avail Node/v1.8.2-d517e727f6a (FrostEngine)` (2023-12-13 17:25:11)
- `Avail Node/v1.8.2-d517e727f6a (Jerksy)` (2023-12-13 17:55:25)
- `Avail Node/v1.8.2-d517e727f6a (noodist3)` (2023-12-13 17:55:25)
- `Avail Node/v1.8.2-d517e727f6a (diagras)` (2023-12-13 19:25:05)
- `Avail Node/v1.8.2-d517e727f6a (NODETERMINATOR)` (2023-12-13 21:25:06)
- `Avail Node/v1.8.2-d517e727f6a (Venomy777)` (2023-12-13 21:54:56)
- `Avail Node/v1.8.2-d517e727f6a (Lekirawen)` (2023-12-13 21:54:57)
- `Avail Node/v1.8.2-d517e727f6a (GARMNODE)` (2023-12-13 22:54:07)
- `Gear Node/v0.3.1-5d8fb07221d (Soloval)` (2023-12-13 23:55:10)
- `Avail Node/v1.8.2-d517e727f6a (trk)` (2023-12-14 00:24:48)
- `Avail Node/v1.8.2-d517e727f6a (4t2)` (2023-12-14 01:54:52)
- `Avail Node/v1.8.2-d517e727f6a (EchoEnigma)` (2023-12-14 02:55:01)
- `Avail Node/v1.8.2-d517e727f6a (EZENODE)` (2023-12-14 05:54:53)
- `Avail Node/v1.8.2-d517e727f6a (Liwiishishe)` (2023-12-14 06:24:47)
- `Gear Node/v0.3.1-5d8fb07221d (buonix)` (2023-12-14 07:24:47)
- `Avail Node/v1.8.2-d517e727f6a (MysticWings)` (2023-12-14 07:24:47)
- `Avail Node/v1.8.2-d517e727f6a (hfgh67235)` (2023-12-14 07:54:52)
- `Avail Node/v1.8.2-d517e727f6a (Antija)` (2023-12-14 10:55:06)
- `kubo/0.25.0/413a52d/docker` (2023-12-14 14:51:40)
- `Avail Node/v1.8.2-d517e727f6a (gsnode)` (2023-12-14 14:55:02)
- `Avail Node/v1.8.2-d517e727f6a (vmi1548796)` (2023-12-14 16:25:15)
- `kubo/0.25.0/` (2023-12-14 17:21:42)
- `kubo/0.25.0/413a52d0e` (2023-12-14 21:51:53)
- `kubo/0.26.0-dev/0fdd979/docker` (2023-12-15 00:22:14)
- `kubo/0.25.0/413a52d` (2023-12-15 08:52:25)
- `kubo/0.25.0/9234731-dirty` (2023-12-15 12:52:32)
- `kubo/0.26.0-dev/d407c882c` (2023-12-15 12:52:33)
- `kubo/0.25.0/413a52d/1234567890123456789012345678901234567890` (2023-12-16 02:22:37)
- `pct` (2023-12-16 14:23:02)
- `github.com/metis-seq/tss-server@f7dc5e532` (2023-12-17 13:23:28)
- `xpc` (2023-12-17 22:22:27)
- `oracle@` (2023-12-17 23:22:24)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/subspace-gemini-3g/sync/2` (2023-12-11 11:25:14)
- `/418040fc282f5e5ddd432c46d05297636f6f75ce68d66499ff4cbda69ccd180b/sync/2` (2023-12-11 11:25:14)
- `/avail_kad/id/1.0.0` (2023-12-14 16:51:24)
- `/bitcoin/alert-system/0.0.1` (2023-12-15 05:22:52)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 220 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `34.245.162.177` | IE | 130 | ['avail-light-client/rust-client']| True  |
| `3.249.160.11` | IE | 130 | ['avail-light-client/rust-client']| True  |
| `54.75.0.2` | IE | 130 | ['avail-light-client/rust-client']| True  |
| `52.50.235.89` | IE | 129 | ['avail-light-client/rust-client']| True  |
| `54.247.27.252` | IE | 125 | ['avail-light-client/rust-client']| True  |
| `212.47.234.38` | FR | 114 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.238.83` | FR | 111 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `34.244.55.184` | IE | 100 | ['avail-light-client/rust-client']| True  |
| `54.246.7.156` | IE | 100 | ['avail-light-client/rust-client']| True  |

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

In the specified time interval from `2023-12-11` to `2023-12-18` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-12-11` to `2023-12-18` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-12-11` to `2023-12-18` in the DHT and their datacenter association.

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