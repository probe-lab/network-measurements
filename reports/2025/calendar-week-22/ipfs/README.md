# Nebula Measurement Results Calendar Week 22 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 22 - 2025](#nebula-measurement-results-calendar-week-22---2025)
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

The following results show measurement data that were collected in calendar week 22 in 2025 from `2025-06-02` to `2025-06-09`.

- Number of crawls `84`
- Number of visits `8,778,197`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `63,944`
- Number of unique peer IDs discovered in the DHT `63,502`
- Number of unique IP addresses found `28,793`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20250602014417` (2025-06-02 02:01:18)
- `helia/5.4.2 js-libp2p/2.8.8 electron/29.4.6` (2025-06-02 04:02:01)
- `@libp2p/amino-dht-bootstrapper/1.9.26 js-libp2p/2.8.8-6a3ae02f5 node/22.16.0` (2025-06-02 08:01:25)
- `kubo/0.36.0-dev/e491ee9/docker` (2025-06-02 22:01:19)
- `kubo/0.36.0-dev/Homebrew` (2025-06-03 02:01:22)
- `kubo/0.36.0-dev/78ef5e9/docker` (2025-06-03 04:01:12)
- `kubo/0.35.0/docker` (2025-06-03 06:01:02)
- `bootnode-20250603054946` (2025-06-03 06:01:51)
- `kubo/0.35.0/direct` (2025-06-03 12:01:12)
- `kubo/0.23.0/29783c478` (2025-06-03 12:01:26)
- `kubo/0.36.0-dev/78ef5e9ee` (2025-06-03 18:01:18)
- `github.com/dcnetio/go-dcnode@623507228-dirty` (2025-06-03 20:01:32)
- `@libp2p/amino-dht-bootstrapper/1.9.27 js-libp2p/2.8.9 node/22.16.0` (2025-06-04 10:01:17)
- `bootnode-20250604145426` (2025-06-04 16:01:10)
- `kubo/0.36.0-dev/d39cb7f/docker` (2025-06-05 00:01:22)
- `dvpncmd@fd59cafd0-hayek` (2025-06-05 06:01:21)
- `kubo/0.33.0-dev/ec4c55232` (2025-06-05 12:01:48)
- `ca-vsc@v0.0.0-20250605124809-83aea760928c` (2025-06-05 14:01:47)
- `ca-vsc@v0.0.0-20250605133333-894fd9200c33` (2025-06-05 16:01:28)
- `oprueba.com/oos-agent@v0.0.0-20250605162506-60688550b84f+dirty` (2025-06-05 22:02:00)
- `@libp2p/amino-dht-bootstrapper/1.9.28 js-libp2p/0.0.0 node/22.16.0` (2025-06-06 06:01:45)
- `kubo/0.33.0-dev/3e29d1520-dirty` (2025-06-06 14:01:25)
- `bootnode-20250606125817` (2025-06-06 16:01:08)
- `oprueba.com/oos-agent@v0.0.0-20250606150116-79b9240a7cc7+dirty` (2025-06-06 16:01:08)
- `kubo/0.36.0-dev/7e1132b31` (2025-06-06 18:01:08)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250606173653-a7c271ea6d5c` (2025-06-06 18:01:45)
- `helia/5.4.2 js-libp2p/2.8.9 electron/29.4.6` (2025-06-06 20:01:18)
- `github.com/JackalLabs/sequoia@1d97b4a5e` (2025-06-06 20:01:24)
- `kubo/0.36.0-dev/605851976` (2025-06-06 22:01:02)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.5` (2025-06-06 22:01:19)
- `bootnode-20250608064032` (2025-06-08 08:01:41)
- `github.com/dcnetio/go-dcnode@7036cd810-dirty` (2025-06-08 18:01:05)
- `oprueba.com/oos-agent@v0.0.0-20250608124901-e91029da4971` (2025-06-08 22:01:18)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `matrix-libp2p-monitor` (2025-06-08 22:01:26)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `82.180.162.171` | US | 367 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.30.0/846c5cc', 'kubo/0.33.2/']| False  |
| `91.230.153.86` | RU | 33 | ['edgevpn']| False  |
| `162.55.134.135` | DE | 22 | ['kubo/0.35.0/']| True  |
| `54.83.92.159` | US | 20 | ['kubo/0.36.0-dev/']| True  |
| `38.101.215.12` | US | 20 | ['p2pd/0.1']| False  |
| `60.244.138.148` | TW | 20 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `123.181.11.224` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `123.181.8.94` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `172.33.0.7` | US | 19 | ['kubo/0.28.0/e7f0f34/docker', 'kubo/0.35.0/a78d155/docker']| False  |
| `49.12.81.229` | DE | 18 | ['kubo/0.35.0/']| True  |

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

In the specified time interval from `2025-06-02` to `2025-06-09` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-06-02` to `2025-06-09` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-06-02` to `2025-06-09` in the DHT and their datacenter association.

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