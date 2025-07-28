# Nebula Measurement Results Calendar Week 29 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 29 - 2025](#nebula-measurement-results-calendar-week-29---2025)
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

The following results show measurement data that were collected in calendar week 29 in 2025 from `2025-07-21` to `2025-07-28`.

- Number of crawls `84`
- Number of visits `10,058,519`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `62,523`
- Number of unique peer IDs discovered in the DHT `62,312`
- Number of unique IP addresses found `42,303`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250716145657-42efe41d37e6+dirty` (2025-07-21 06:01:18)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250721020349-4b0ccbf4bb01` (2025-07-21 08:01:38)
- `bootnode-20250721102326` (2025-07-21 10:02:07)
- `kubo/0.37.0-dev/bb58ca473-dirty` (2025-07-21 10:03:09)
- `bootnode-20250721031728` (2025-07-21 12:03:13)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250721020300-7a6967fcf4d8+dirty` (2025-07-21 14:01:04)
- `pinshare@v0.1.2-0.20250718154645-5304d07f6d5b+dirty` (2025-07-21 14:03:51)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250721165133-983bfd483827+dirty` (2025-07-21 18:02:59)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250722025537-a3cf157efc45+dirty` (2025-07-22 04:02:34)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250722015438-281299812250+dirty` (2025-07-22 10:02:30)
- `bootnode-20250722120844` (2025-07-22 12:01:45)
- `bootnode-20250722120719` (2025-07-22 12:01:51)
- `bootnode-20250722050604` (2025-07-22 12:03:22)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250722081152-e0aae9ef26ca+dirty` (2025-07-22 12:04:09)
- `github.com/harmony-one/harmony@v1.10.3-0.20250721182046-97552e3ced7c` (2025-07-22 12:04:20)
- `kubo/0.36.0/0276b3faf-dirty/docker` (2025-07-22 14:02:29)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250722082804-b46b6c36feea+dirty` (2025-07-22 16:02:19)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250723015622-d1a92960bce9+dirty` (2025-07-23 04:03:08)
- `helia/4.0.1 libp2p/1.2.1 UserAgent=v22.13.1` (2025-07-23 12:02:02)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250723152008-73ce557a500f+dirty` (2025-07-23 16:01:13)
- `peersky-browser/1.0.0-beta.6 js-libp2p/2.8.12 electron/29.4.6` (2025-07-23 18:04:29)
- `js-libp2p/2.8.12 node/24.4.0` (2025-07-23 20:04:17)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250724013707-f585d9f52528+dirty` (2025-07-24 02:01:43)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250724013544-7d4064659bb1` (2025-07-24 02:02:19)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250724013544-7d4064659bb1+dirty` (2025-07-24 02:02:28)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250724075846-355362a6a79e+dirty` (2025-07-24 10:01:07)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250724051631-80ad35d55434+dirty` (2025-07-24 10:01:12)
- `ca-vsc@v0.0.0-20250718121252-8b79866e830c+dirty` (2025-07-24 12:04:34)
- `kubo/0.36.0/5f5ace40c` (2025-07-24 16:03:39)
- `kubo/0.36.0/Homebrew/desktop` (2025-07-24 16:04:50)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250724075757-9d807630a439+dirty` (2025-07-25 06:01:34)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250725011157-068a0220a373+dirty` (2025-07-25 06:03:34)
- `kubo/0.36.0/82d97034d-dirty` (2025-07-25 08:02:55)
- `oprueba.com/orphe-agent@v1.0.0-beta.1.0.20250725021123-d56fc388c62f` (2025-07-25 10:01:28)
- `github.com/harmony-one/harmony@v1.10.3-0.20250724210822-7b9412cac10a` (2025-07-25 10:02:37)
- `gossipTea@v0.2.1-0.20250724095208-c8fadc1315ec+dirty` (2025-07-26 22:02:57)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/botnet/command/1.0.0` (2025-07-24 06:01:51)
- `/ipfs/ping/11.0.0` (2025-07-26 12:01:15)
- `/ipfs/ping/5.0.0` (2025-07-26 14:01:33)
- `/gossip/network/chat/1.0.0/private/` (2025-07-26 22:02:57)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `37.27.190.73` | FI | 118 | ['kubo/0.32.1/']| True  |
| `2a01:4f9:c012:92ce::1` | DE | 118 | ['kubo/0.32.1/']| True  |
| `86.141.173.74` | GB | 72 | ['kubo/0.32.1/']| False  |
| `2a00:15c9::4182` | IR | 56 | ['edgevpn']| False  |
| `109.122.253.245` | IR | 56 | ['edgevpn']| False  |
| `104.250.129.19` | US | 50 | ['p2pd/0.1']| True  |
| `104.250.129.22` | US | 50 | ['p2pd/0.1']| True  |
| `104.250.129.20` | US | 48 | ['p2pd/0.1']| True  |
| `104.250.129.21` | US | 48 | ['p2pd/0.1']| True  |
| `152.81.47.226` | FR | 46 | ['kubo/0.33.0/']| False  |

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

In the specified time interval from `2025-07-21` to `2025-07-28` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-07-21` to `2025-07-28` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-07-21` to `2025-07-28` in the DHT and their datacenter association.

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