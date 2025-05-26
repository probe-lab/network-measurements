# Nebula Measurement Results Calendar Week 20 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 20 - 2025](#nebula-measurement-results-calendar-week-20---2025)
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

The following results show measurement data that were collected in calendar week 20 in 2025 from `2025-05-19` to `2025-05-26`.

- Number of crawls `84`
- Number of visits `8,246,031`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `58,794`
- Number of unique peer IDs discovered in the DHT `58,570`
- Number of unique IP addresses found `28,394`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `exuberant-scent` (2025-05-19 16:01:25)
- `kubo/0.36.0-dev/20d9660/docker` (2025-05-19 22:01:11)
- `helia/2.0.3 js-libp2p/0.46.11 UserAgent=v18.20.7` (2025-05-20 00:01:50)
- `helia/5.4.1 js-libp2p/2.8.5 node/23.8.0` (2025-05-20 02:01:50)
- `@libp2p/amino-dht-bootstrapper/1.9.6 js-libp2p/2.8.6 node/22.15.1` (2025-05-20 08:01:23)
- `megaphone` (2025-05-20 12:01:29)
- `kubo/0.36.0-dev/1c11ad6` (2025-05-20 14:01:06)
- `cowardly-vest` (2025-05-20 14:01:23)
- `kubo/0.36.0-dev/1c11ad699-dirty` (2025-05-20 14:01:32)
- `kubo/0.36.0-dev/1c11ad6/docker` (2025-05-20 18:01:16)
- `kubo/0.35.0-rc2/1f1574f/1234567890123456789012345678901234567890` (2025-05-20 20:01:07)
- `github.com/filecoin-project/boost@cf2578759` (2025-05-21 00:01:29)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250520235455-d4f2d410f115+dirty` (2025-05-21 00:01:37)
- `ca-vsc@v0.0.0-20250521091505-faf41d9e2aa5` (2025-05-21 10:01:50)
- `kubo/0.36.0-dev/3290afc/docker` (2025-05-21 14:01:09)
- `kubo/0.35.0-rc2/cd3e498/1234567890123456789012345678901234567890` (2025-05-21 14:01:19)
- `oprueba.com/oos-agent@v0.0.0-20250521135446-c68186985153+dirty` (2025-05-21 16:01:28)
- `kubo/0.35.0-rc2/cd3e498` (2025-05-21 16:01:43)
- `kubo/0.35.0/a78d155` (2025-05-21 18:01:05)
- `kubo/0.35.0/a78d155/docker` (2025-05-21 18:01:19)
- `kubo/0.35.0/a78d155/1234567890123456789012345678901234567890` (2025-05-21 18:01:42)
- `kubo/0.35.0/` (2025-05-21 20:01:13)
- `kubo/0.28.0-dev/d16be4daf` (2025-05-21 22:01:13)
- `kubo/0.35.0/a78d155/kubernetes` (2025-05-21 22:01:44)
- `kubo/0.36.0-dev/6058519/docker` (2025-05-22 02:01:17)
- `ca-vsc@v0.0.0-20250522092930-cc88d713fba0` (2025-05-22 12:01:44)
- `ca-vsc@v0.0.0-20250522114445-bf74ffc68597+dirty` (2025-05-22 14:01:17)
- `helia/5.4.2 js-libp2p/2.8.7 node/22.11.0` (2025-05-22 16:01:22)
- `oprueba.com/oos-agent@v0.0.0-20250522064229-886f408f86de+dirty` (2025-05-22 18:01:26)
- `kubo/0.35.0/Homebrew` (2025-05-22 20:01:28)
- `kubo/0.35.0/a78d155/bootstrap.libp2p.io` (2025-05-22 22:01:04)
- `bootnode-20250522231543` (2025-05-23 00:01:33)
- `kubo/0.35.0/desktop` (2025-05-23 02:01:44)
- `oprueba.com/oos-agent@v0.0.0-20250523024859-1c23e8999bca+dirty` (2025-05-23 06:01:41)
- `kubo/0.35.0/d0d24ea-dirty` (2025-05-23 10:01:19)
- `ca-vsc@v0.0.0-20250523081857-343be635c1f1` (2025-05-23 10:01:41)
- `helia/2.0.3 js-libp2p/0.46.11 UserAgent=v18.20.5` (2025-05-23 12:01:05)
- `kubo/0.33.2/1422fcc/docker` (2025-05-23 12:01:32)
- `ca-vsc@v0.0.0-20250523084356-a9466cfec153+dirty` (2025-05-23 12:01:37)
- `oprueba.com/oos-agent@v0.0.0-20250523094708-ec2406b7414e+dirty` (2025-05-23 14:01:26)
- `js-libp2p/2.8.5 node/20.19.2` (2025-05-23 14:01:57)
- `kubo/0.35.0/a78d155/collab.ipfscluster.io` (2025-05-23 16:01:17)
- `someguy/v0.9.1 2025-05-16-6cb37a4` (2025-05-23 16:01:18)
- `oprueba.com/oos-agent@v0.0.0-20250523143056-b98971062cae+dirty` (2025-05-23 16:01:27)
- `oprueba.com/oos-agent@v0.0.0-20250523172040-fafade506e5b+dirty` (2025-05-23 18:01:30)
- `kubo/0.35.0-rc1/6e89271/docker` (2025-05-23 20:01:13)
- `bootnode-20250523231854` (2025-05-24 00:01:29)
- `bootnode-20250524024227` (2025-05-24 04:01:52)
- `bootnode-20250524050359` (2025-05-24 06:01:17)
- `kubo/0.33.0-dev/a525846ab` (2025-05-24 14:01:08)
- `kubo/0.35.0/a78d155de` (2025-05-24 14:01:09)
- `fsp2pcloud@825e25b0a-dirty` (2025-05-24 16:01:13)
- `kubo/0.36.0-dev/605851976-dirty` (2025-05-25 02:01:23)
- `bootnode-20250525092316` (2025-05-25 10:01:17)
- `@libp2p/amino-dht-bootstrapper/1.9.7 js-libp2p/2.8.8 node/22.16.0` (2025-05-25 12:01:35)
- `fsp2pcloud@3c4757ee9-dirty` (2025-05-25 16:01:23)
- `oprueba.com/oos-agent@v0.0.0-20250525080037-6f440b893491+dirty` (2025-05-25 18:01:45)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/ax/broadcast/1.0.0` (2025-05-19 16:01:25)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `82.180.162.171` | US | 355 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.30.0/846c5cc', 'kubo/0.33.2/']| False  |
| `91.230.153.86` | RU | 39 | ['edgevpn']| False  |
| `101.78.97.56` | SG | 32 | ['kubo/0.32.1/']| False  |
| `123.181.15.116` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `46.151.104.25` | RU | 19 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `38.101.215.12` | US | 18 | ['p2pd/0.1']| False  |
| `89.89.190.64` | FR | 15 | ['kubo/0.32.1/']| False  |
| `111.226.17.116` | CN | 15 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `2001:861:3a08:f3a0:30dd:a538:6658:4790` | FR | 15 | ['kubo/0.32.1/']| False  |
| `73.166.122.55` | US | 14 | ['kubo/0.32.1/']| False  |

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

In the specified time interval from `2025-05-19` to `2025-05-26` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-05-19` to `2025-05-26` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-05-19` to `2025-05-26` in the DHT and their datacenter association.

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