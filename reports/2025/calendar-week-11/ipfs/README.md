# Nebula Measurement Results Calendar Week 11 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 11 - 2025](#nebula-measurement-results-calendar-week-11---2025)
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

The following results show measurement data that were collected in calendar week 11 in 2025 from `2025-03-17` to `2025-03-24`.

- Number of crawls `84`
- Number of visits `9,718,525`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `46,931`
- Number of unique peer IDs discovered in the DHT `46,508`
- Number of unique IP addresses found `48,466`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/harmony-one/harmony@c71b715b9` (2025-03-17 10:01:14)
- `github.com/harmony-one/harmony@f210b3a8f-dirty` (2025-03-17 14:01:08)
- `bootnode-20250317155856` (2025-03-17 16:01:11)
- `bootnode-20250317152139` (2025-03-17 16:01:15)
- `bootnode-20250317092137` (2025-03-17 18:02:07)
- `github.com/JackalLabs/sequoia@14fa485b7` (2025-03-17 22:01:31)
- `kubo/0.35.0-dev/` (2025-03-18 02:01:54)
- `kubo/0.33.0-dev/ed0edb100-dirty` (2025-03-18 08:01:42)
- `github.com/dcnetio/go-dcnode@9b808c131-dirty` (2025-03-18 12:01:11)
- `kubo/0.33.2/Homebrew/desktop` (2025-03-18 14:01:38)
- `jackalnft@6ec942875-dirty` (2025-03-18 14:01:49)
- `bootnode-20250318172050` (2025-03-18 18:01:07)
- `bootnode-20250319000203` (2025-03-19 02:01:45)
- `kubo/0.34.0-rc2/3d87596/collab.ipfscluster.io` (2025-03-19 08:01:02)
- `p2proxy@d898a7fff` (2025-03-19 10:01:19)
- `rust-libp2p/0.39.0` (2025-03-19 16:01:24)
- `feishup2pclient@4e31f87e1-dirty` (2025-03-19 16:01:37)
- `p2p_win@9e9f50d3e-dirty` (2025-03-19 16:01:53)
- `kubo/0.35.0-dev/b2efaa992-dirty` (2025-03-19 16:01:55)
- `kubo/0.35.0-dev/00438b1/docker` (2025-03-20 10:01:11)
- `github.com/mynextid/kad-dht@dad37fbf3-dirty` (2025-03-20 10:01:20)
- `kubo/0.35.0-dev/ba171b5/docker` (2025-03-20 12:01:53)
- `github.com/harmony-one/harmony@1adbd2b24` (2025-03-20 14:01:26)
- `kubo/0.35.0-dev/c389c88` (2025-03-20 14:01:27)
- `bootnode-20250320124457` (2025-03-20 14:01:46)
- `kubo/0.35.0-dev/f7e3c15` (2025-03-20 16:01:29)
- `libp2p/1.9.4 UserAgent=v20.19.0` (2025-03-20 18:01:09)
- `@libp2p/amino-dht-bootstrapper/1.9.0 js-libp2p/2.8.2-071267286 node/22.14.0` (2025-03-20 18:01:22)
- `github.com/JackalLabs/sequoia@812a50d90` (2025-03-20 18:01:43)
- `kubo/0.34.0/5cca561` (2025-03-20 22:01:02)
- `kubo/0.34.0/5cca561/docker` (2025-03-20 22:01:03)
- `github.com/JackalLabs/sequoia@812a50d90-dirty` (2025-03-20 22:01:21)
- `kubo/0.34.0/5cca561/1234567890123456789012345678901234567890` (2025-03-20 22:01:40)
- `kubo/0.34.0/` (2025-03-20 22:01:43)
- `kubo/0.34.0/5cca561/bootstrap.libp2p.io` (2025-03-21 00:01:03)
- `bootnode-20250320220556` (2025-03-21 00:01:51)
- `kubo/0.35.0-dev/b339490/docker` (2025-03-21 04:01:53)
- `kubo/0.33.0-dev/87d232bb0-dirty` (2025-03-21 06:01:45)
- `ca-vsc@v0.0.0-20250313054155-5af5ae0a1c11` (2025-03-21 10:01:19)
- `github.com/harmony-one/harmony@74fedff42` (2025-03-21 12:01:30)
- `kubo/0.34.0/Homebrew` (2025-03-21 14:01:06)
- `github.com/JackalLabs/sequoia@v1.2.1-rc.2.0.20250321134342-e3dc20fa6a4f` (2025-03-21 14:01:37)
- `github.com/JackalLabs/sequoia@7efbdc4c8` (2025-03-21 16:01:43)
- `github.com/JackalLabs/sequoia@v1.2.1-rc.2.0.20250321154547-7efbdc4c80ea` (2025-03-21 16:02:02)
- `jackalnft@9e5886ad9-dirty` (2025-03-21 18:01:32)
- `bootnode-20250322144852` (2025-03-22 16:01:12)
- `bootnode-20250323001316` (2025-03-23 02:01:04)
- `changeme@` (2025-03-23 10:01:17)
- `js-libp2p/2.8.2 node/20.17.0` (2025-03-23 20:01:32)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `harmony/epochsync/partner/0/1.0.0` (2025-03-17 10:01:14)
- `harmony/sync/partner/0/1.0.0` (2025-03-17 10:01:14)
- `harmony/sync/partner/1/1.0.0` (2025-03-17 10:01:14)
- `/ipfs/kad/1.0.0/wan` (2025-03-18 02:01:54)
- `/ipfs/kad/1.0.0/lan` (2025-03-18 02:01:54)
- `/tricker/proxy/1.0.0` (2025-03-19 16:01:24)
- `/gnostr/proxy/1.0.0` (2025-03-20 00:01:15)
- `/otter/ident4/0.0.0` (2025-03-22 10:01:44)
- `/orbitdb/heads/orbitdb/zdpuAvXbAsKAYT3RELtcpVvFg4RmN71TP2KMVAmmaLChzcfUg` (2025-03-23 20:01:32)
- `/orbitdb/voyager/rpc/v1.0.0` (2025-03-23 20:01:32)
- `/orbitdb/heads/orbitdb/zdpuAsohR368NuDs1B1LVCnWzRnZNYfcmsrZknQubitx6PSnd` (2025-03-23 20:01:32)
- `/orbitdb/voyager/v1.0.0` (2025-03-23 20:01:32)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `5.39.80.110` | FR | 84 | ['edgevpn']| True  |
| `2001:41d0:8:926e::1` | FR | 84 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 42 | ['edgevpn']| True  |
| `172.233.243.82` | FR | 42 | ['edgevpn']| True  |
| `89.89.190.64` | FR | 38 | ['kubo/0.32.1/']| False  |
| `26.26.26.1` | US | 34 | ['go-ipfs/0.8.0/48f94e2', 'kubo/0.28.0/']| False  |
| `217.155.3.245` | GB | 25 | ['edgevpn', 'kubo/0.33.2/ad1868a/docker']| False  |
| `72.82.59.11` | US | 23 | ['edgevpn']| False  |
| `102.35.52.29` | RE | 21 | ['kubo/0.32.1/']| False  |
| `91.230.153.86` | RU | 20 | ['edgevpn']| False  |

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

In the specified time interval from `2025-03-17` to `2025-03-24` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-03-17` to `2025-03-24` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-03-17` to `2025-03-24` in the DHT and their datacenter association.

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