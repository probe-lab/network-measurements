# Nebula Measurement Results Calendar Week 19 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 19 - 2025](#nebula-measurement-results-calendar-week-19---2025)
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

The following results show measurement data that were collected in calendar week 19 in 2025 from `2025-05-12` to `2025-05-19`.

- Number of crawls `84`
- Number of visits `8,339,294`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `64,165`
- Number of unique peer IDs discovered in the DHT `63,913`
- Number of unique IP addresses found `27,874`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `fsp2pcloud@` (2025-05-12 08:02:18)
- `dvpncmd@2d0280f2f-hayek` (2025-05-12 14:01:56)
- `kubo/0.36.0-dev/6f37df778-dirty` (2025-05-12 16:01:10)
- `bootnode-20250512101211` (2025-05-12 16:02:05)
- `bootnode-20250512225051` (2025-05-13 00:01:39)
- `github.com/harmony-one/harmony@v1.10.3-0.20250513122740-9341e6007307` (2025-05-13 18:01:42)
- `kubo/0.36.0-dev/a63e399` (2025-05-13 22:01:03)
- `kubo/0.36.0-dev/a63e399/1234567890123456789012345678901234567890` (2025-05-13 22:02:15)
- `kubo/0.36.0-dev/6f37df778-dirty/docker` (2025-05-14 00:02:13)
- `github.com/JackalLabs/sequoia@be4830aca` (2025-05-14 02:02:26)
- `yoledigi_device_1.0.0` (2025-05-14 10:02:20)
- `ca-vsc@v0.0.0-20250514124339-e65fc97bf17a` (2025-05-14 14:01:40)
- `github.com/harmony-one/harmony@v1.10.3-0.20250514085420-899cbe80405f` (2025-05-14 14:02:04)
- `bootnode-20250514164858` (2025-05-14 18:01:23)
- `kubo/0.36.0-dev/6f37df7` (2025-05-14 20:02:12)
- `kubo/0.36.0-dev/a63e399/docker` (2025-05-15 08:01:03)
- `helia/5.4.1 js-libp2p/2.8.5 node/22.11.0` (2025-05-15 12:01:40)
- `ca-vsc@v0.0.0-20250515080333-dd82b6465e08` (2025-05-15 14:01:48)
- `kubo/0.36.0-dev/2ab3f58/docker` (2025-05-15 18:01:36)
- `kubo/0.36.0-dev/2ab3f58/1234567890123456789012345678901234567890` (2025-05-15 20:01:31)
- `kubo/0.35.0-rc2/623902e/1234567890123456789012345678901234567890` (2025-05-16 00:02:23)
- `kubo/0.35.0-rc2/` (2025-05-16 04:01:46)
- `kubo/0.36.0-dev/f84fb28/docker` (2025-05-16 12:01:52)
- `kubo/0.36.0-dev/` (2025-05-16 16:01:48)
- `kubo/0.35.0-rc2/623902e` (2025-05-16 20:01:03)
- `ca-vsc@v0.0.0-20250516102810-7d256183272a` (2025-05-16 20:01:42)
- `github.com/cloud-equities/KNIRVCHAIN_GO_ROOT_MCP@` (2025-05-17 02:01:08)
- `bootnode-20250517070806` (2025-05-17 08:01:38)
- `kubo/0.35.0-rc2/623902e/docker` (2025-05-17 10:01:17)
- `kubo/0.36.0-dev/f84fb2849` (2025-05-17 12:02:00)
- `github.com/dcnetio/go-dcnode@f36f85b49-dirty` (2025-05-17 16:01:45)
- `github.com/dcnetio/go-dcnode@43dc082bf-dirty` (2025-05-17 18:01:05)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/relay/speedtest/1.0.0` (2025-05-12 08:02:18)
- `/knirv/chain-sync/1.0.0` (2025-05-17 02:01:08)
- `/dc/transfer/1.0.0` (2025-05-17 16:01:45)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `91.230.153.86` | RU | 42 | ['edgevpn']| False  |
| `116.203.135.82` | DE | 28 | ['kubo/0.21.0/docker']| True  |
| `38.101.215.12` | US | 22 | ['p2pd/0.1']| False  |
| `111.226.17.116` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `73.166.122.55` | US | 17 | ['kubo/0.32.1/']| False  |
| `101.78.97.56` | SG | 17 | ['kubo/0.32.1/']| False  |
| `46.151.104.25` | RU | 17 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `60.244.138.148` | TW | 15 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `92.49.120.230` | MQ | 13 | ['kubo/0.32.1/']| False  |
| `24.251.118.111` | US | 12 | ['kubo/0.32.1/']| False  |

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

In the specified time interval from `2025-05-12` to `2025-05-19` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-05-12` to `2025-05-19` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-05-12` to `2025-05-19` in the DHT and their datacenter association.

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