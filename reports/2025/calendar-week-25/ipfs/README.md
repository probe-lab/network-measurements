# Nebula Measurement Results Calendar Week 25 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 25 - 2025](#nebula-measurement-results-calendar-week-25---2025)
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

The following results show measurement data that were collected in calendar week 25 in 2025 from `2025-06-23` to `2025-06-30`.

- Number of crawls `84`
- Number of visits `8,424,431`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `50,545`
- Number of unique peer IDs discovered in the DHT `50,157`
- Number of unique IP addresses found `32,409`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.37.0-dev/92aa9936c` (2025-06-23 02:01:03)
- `github.com/dcnetio/go-dcnode@6aa448285-dirty` (2025-06-23 18:01:37)
- `helia/5.4.2 js-libp2p/2.8.9 node/22.16.0` (2025-06-23 22:01:37)
- `oprueba.com/ooa@v1.0.0-beta.1+dirty` (2025-06-23 22:01:54)
- `kubo/0.36.0-rc1/127da7c/bootstrap.libp2p.io` (2025-06-24 00:01:06)
- `kubo/0.37.0-dev/ace0b0b/docker` (2025-06-24 08:01:40)
- `kubo/0.36.0-rc1/127da7c/collab.ipfscluster.io` (2025-06-24 14:01:08)
- `kubo/0.37.0-dev/ace0b0b98-dirty` (2025-06-24 14:01:29)
- `oprueba.com/p2pTun@v0.0.0-20250624151824-9fe6161ba326+dirty` (2025-06-24 16:01:37)
- `bootnode-20250625011313` (2025-06-25 02:01:04)
- `oprueba.com/p2pTun@v0.0.0-20250625022244-062cc1299ce3` (2025-06-25 06:01:06)
- `oprueba.com/p2pTun@v1.0.0-beta.1.0.20250625062814-b9745bb78cf6` (2025-06-25 08:01:42)
- `pinshare@v0.1.3-0.20250622174302-9fcd4471218b+dirty` (2025-06-25 12:01:14)
- `kubo/0.37.0-dev/be24176/docker` (2025-06-25 12:01:31)
- `oprueba.com/ooa@v1.0.0-beta.1` (2025-06-25 18:01:22)
- `@libp2p/amino-dht-bootstrapper/1.9.30 js-libp2p/2.8.12 node/22.16.0` (2025-06-25 22:01:15)
- `ca-vsc@v0.0.0-20250625123131-d9a02a920929` (2025-06-26 10:01:49)
- `kubo/0.36.0-dev/c4c70cb53-dirty` (2025-06-26 10:01:54)
- `oprueba.com/p2pTun@v1.0.0-beta.1+dirty` (2025-06-26 10:02:19)
- `kubo/0.37.0-dev/be2417697-dirty` (2025-06-26 16:01:30)
- `pinshare@v0.1.3-0.20250625181725-53a0297b790b+dirty` (2025-06-26 20:02:09)
- `kubo/0.37.0-dev/839023c/docker` (2025-06-26 22:01:45)
- `ca-vsc@v0.0.0-20250627090853-1f64e5282b4f` (2025-06-27 10:01:29)
- `github.com/harmony-one/harmony@v1.10.3-0.20250626120340-0cf7f45c3bb9` (2025-06-27 10:01:40)
- `kubo/0.37.0-dev/a0632aa/docker` (2025-06-27 12:01:39)
- `bootnode-20250627133323` (2025-06-27 14:01:22)
- `oprueba.com/ooa@v1.0.0-beta.1.0.20250626024014-417bb2c26b17` (2025-06-28 12:01:47)
- `oprueba.com/ooa@v1.0.0-beta.1.0.20250628134424-3b2741a5f826+dirty` (2025-06-28 14:01:38)
- `bootnode-20250628145112` (2025-06-28 16:01:41)
- `oprueba.com/ooa@v1.0.0-beta.1.0.20250628170726-bd92e8f9c5c8+dirty` (2025-06-29 06:01:37)
- `@libp2p/amino-dht-bootstrapper/1.9.31 js-libp2p/2.8.12 node/22.17.0` (2025-06-29 10:02:29)
- `kubo/0.37.0-dev/` (2025-06-29 16:02:06)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/controlplane/v1` (2025-06-25 08:01:42)
- `/dataplane/v1` (2025-06-25 18:01:22)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `2a01:4f9:c012:92ce::1` | DE | 92 | ['kubo/0.32.1/']| True  |
| `37.27.190.73` | FI | 92 | ['kubo/0.32.1/']| True  |
| `64.227.156.187` | IN | 79 | ['kubo/0.29.0/3f0947b']| True  |
| `139.59.6.4` | IN | 57 | ['kubo/0.29.0/3f0947b']| True  |
| `64.227.134.114` | IN | 43 | ['kubo/0.29.0/3f0947b']| True  |
| `142.93.215.219` | IN | 40 | ['kubo/0.28.0/', 'kubo/0.29.0/3f0947b']| True  |
| `64.227.166.181` | IN | 37 | ['kubo/0.29.0/3f0947b']| True  |
| `162.55.44.107` | DE | 32 | ['kubo/0.29.0/3f0947b', 'kubo/0.35.0/desktop']| True  |
| `188.245.202.3` | DE | 29 | ['kubo/0.29.0/3f0947b']| True  |
| `91.230.153.86` | RU | 26 | ['edgevpn']| False  |

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

In the specified time interval from `2025-06-23` to `2025-06-30` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-06-23` to `2025-06-30` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-06-23` to `2025-06-30` in the DHT and their datacenter association.

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