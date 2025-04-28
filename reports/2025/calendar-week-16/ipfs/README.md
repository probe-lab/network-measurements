# Nebula Measurement Results Calendar Week 16 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 16 - 2025](#nebula-measurement-results-calendar-week-16---2025)
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

The following results show measurement data that were collected in calendar week 16 in 2025 from `2025-04-21` to `2025-04-28`.

- Number of crawls `84`
- Number of visits `9,758,032`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `65,355`
- Number of unique peer IDs discovered in the DHT `65,036`
- Number of unique IP addresses found `43,489`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `js-libp2p/0.45.9 UserAgent=v22.11.0` (2025-04-21 02:02:10)
- `bootnode-20250421035411` (2025-04-21 04:01:32)
- `js-libp2p/2.8.5 node/20.17.0` (2025-04-21 06:01:36)
- `js-libp2p/2.8.5 node/20.19.0` (2025-04-21 08:01:58)
- `dvpncmd@1c77eff5f-hayek` (2025-04-21 12:01:57)
- `github.com/harmony-one/harmony@v1.10.3-0.20250421120919-e5a8d68fc92a+dirty` (2025-04-21 18:02:22)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250421214837-20bdef74d560` (2025-04-21 22:01:44)
- `github.com/JackalLabs/sequoia@20bdef74d` (2025-04-21 22:02:18)
- `dvpncmd@86235aeec-hayek` (2025-04-22 06:01:19)
- `dvpncmd@86235aeec-dirty` (2025-04-22 10:02:22)
- `ca-vsc@v0.0.0-20250422091628-069434d5df7e` (2025-04-22 16:02:29)
- `dvpncmd@ac6485404-hayek` (2025-04-22 20:01:36)
- `kubo/0.35.0-dev/docker` (2025-04-22 20:02:00)
- `bootnode-20250422165807` (2025-04-22 22:02:40)
- `github.com/harmony-one/harmony@v1.10.3-0.20250422224904-a8242525b96b` (2025-04-24 02:01:05)
- `bootnode-20250424080659` (2025-04-24 10:02:18)
- `ca-vsc@v0.0.0-20250424114236-ad77b6d7ca7f` (2025-04-24 14:01:33)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.19.1` (2025-04-24 14:02:02)
- `dvpncmd@ad0596379-hayek` (2025-04-24 18:01:53)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250424193806-5cdbabc3df43` (2025-04-24 20:02:03)
- `github.com/JackalLabs/sequoia@19ab034b7` (2025-04-24 20:02:05)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250424213018-f93d19ad3fad` (2025-04-24 22:01:49)
- `dvpncmd@5ebd72cdb-hayek` (2025-04-25 06:02:03)
- `ca-vsc@v0.0.0-20250425070331-2ce1c5fa5fe7` (2025-04-25 08:01:25)
- `kubo/0.35.0-dev/ee5665d/docker` (2025-04-25 10:02:14)
- `github.com/harmony-one/harmony@v1.10.3-0.20250425154509-a1640073b512` (2025-04-25 16:01:10)
- `kubo/0.35.0-dev/f2bc13e92-dirty` (2025-04-25 20:01:19)
- `js-libp2p/2.8.5 node/20.18.3` (2025-04-26 08:01:43)
- `js-libp2p/2.8.5 node/20.19.1` (2025-04-26 16:01:21)
- `bootnode-20250426081141` (2025-04-26 16:01:52)
- `kubo/0.35.0-dev/ee5665d37` (2025-04-27 00:01:41)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250427000306-a602732ac2e0` (2025-04-27 02:01:57)
- `github.com/JackalLabs/sequoia@a602732ac` (2025-04-27 02:02:04)
- `dvpncmd@22b81ebce-hayek` (2025-04-27 04:02:20)
- `kubo/0.35.0-dev/2ff9f3406-dirty` (2025-04-27 10:01:04)
- `js-libp2p/js-libp2p node/23.11.0` (2025-04-27 12:03:00)
- `js-libp2p/2.8.5 node/23.11.0` (2025-04-27 14:02:27)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/orbitdb/heads/orbitdb/zdpuAow6WwFzQZ6F2MAq8V4ace8XdEktvRpRV4mzMUtQzKWK8` (2025-04-24 04:02:11)
- `/orbitdb/heads/orbitdb/zdpuAyHkbfdbUKBW5WUaBo2jhpPZBXH1J7UsCDJY4ypoHqi2D` (2025-04-24 14:02:02)
- `/telemetry/upload/0.6.0` (2025-04-25 20:01:19)
- `/telemetry/telemetry/0.6.0` (2025-04-25 20:01:19)
- `/telemetry/download/0.6.0` (2025-04-25 20:01:19)
- `/perf/1.0.0` (2025-04-27 12:03:00)
- `/ipfs/astrawiki` (2025-04-27 14:02:27)
- `/orbitdb/heads/orbitdb/zdpuB15HaJTQrnu2f64FQVPpFmyoByf4yW6ULNbeF5hdLeEqt` (2025-04-27 14:02:27)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `172.233.243.82` | FR | 71 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 71 | ['edgevpn']| True  |
| `85.243.15.41` | PT | 39 | ['kubo/0.35.0-dev/2ff9f3406-dirty', 'kubo/0.35.0-dev/f2bc13e92-dirty']| False  |
| `91.230.153.86` | RU | 37 | ['edgevpn']| False  |
| `26.26.26.1` | US | 33 | ['go-ipfs/0.8.0/48f94e2', 'kubo/0.28.0/', 'kubo/0.30.0/desktop']| False  |
| `123.181.11.122` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `38.101.215.12` | US | 18 | ['p2pd/0.1']| False  |
| `123.181.13.205` | CN | 18 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `101.78.97.56` | SG | 16 | ['kubo/0.32.1/']| False  |
| `37.27.83.206` | FI | 15 | ['kubo/0.35.0-dev/2ff9f3406-dirty']| True  |

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

In the specified time interval from `2025-04-21` to `2025-04-28` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-04-21` to `2025-04-28` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-04-21` to `2025-04-28` in the DHT and their datacenter association.

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