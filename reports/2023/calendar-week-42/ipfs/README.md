# Nebula Measurement Results Calendar Week 42 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 42 - 2023](#nebula-measurement-results-calendar-week-42---2023)
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

The following results show measurement data that were collected in calendar week 42 in 2023 from `2023-10-16` to `2023-10-23`.

- Number of crawls `336`
- Number of visits `42,738,286`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `43,353`
- Number of unique peer IDs discovered in the DHT `42,353`
- Number of unique IP addresses found `57,523`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.20.0-dev/353dd49/docker` (2023-10-16 08:22:06)
- `kubo/0.23.0-s3/3a1a0413a-dirty` (2023-10-16 19:51:58)
- `helia/2.0.3 js-libp2p/0.46.14 UserAgent=v18.17.0` (2023-10-17 13:51:55)
- `kubo/0.23.0/53db4584f-dirty` (2023-10-17 23:22:24)
- `github.com/application-research/edge-ur@526a92e9a-dirty` (2023-10-18 06:51:27)
- `kubo/0.22.0/4d329a9a0` (2023-10-18 16:22:33)
- `kubo/0.22.0/3f884d3/gala.games` (2023-10-18 18:21:14)
- `kubo/0.23.0/4695fd9fe` (2023-10-19 03:22:25)
- `kubo/0.23.0/4695fd9/docker` (2023-10-19 15:51:58)
- `Polkadot Bulletin Chain Node/v0.1.0-dev-bf9bca25365 (alice)` (2023-10-19 15:52:30)
- `kubo/0.22.0/8362f1c0b` (2023-10-19 19:52:34)
- `kubo/0.23.0/da3cf310d-dirty` (2023-10-19 21:21:54)
- `kubo/0.22.0/70bd7c88e` (2023-10-21 05:52:08)
- `kubo/0.23.0-dev/ced348366` (2023-10-21 13:52:24)
- `github.com/alvin-reyes/edge-urid@8efdf8b9c-dirty` (2023-10-22 00:51:55)
- `kubo/0.23.0/89a4769/docker` (2023-10-22 03:22:04)
- `kubo/0.23.0/89a476948` (2023-10-22 16:21:50)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/quai/0.1.0` (2023-10-16 18:22:19)
- `/dot-bulletin/sync/warp` (2023-10-19 15:52:30)
- `/1bdffdced47df42750cc88cd4064909cbb2f02fa276da2b69992fb63e0962bbe/light/2` (2023-10-19 15:52:30)
- `/dot-bulletin/light/2` (2023-10-19 15:52:30)
- `/1bdffdced47df42750cc88cd4064909cbb2f02fa276da2b69992fb63e0962bbe/sync/warp` (2023-10-19 15:52:30)
- `/1bdffdced47df42750cc88cd4064909cbb2f02fa276da2b69992fb63e0962bbe/state/2` (2023-10-19 15:52:30)
- `/1bdffdced47df42750cc88cd4064909cbb2f02fa276da2b69992fb63e0962bbe/sync/2` (2023-10-19 15:52:30)
- `/dot-bulletin/block-announces/1` (2023-10-19 15:52:30)
- `/paritytech/grandpa/1` (2023-10-19 15:52:30)
- `/1bdffdced47df42750cc88cd4064909cbb2f02fa276da2b69992fb63e0962bbe/transactions/1` (2023-10-19 15:52:30)
- `/dot-bulletin/transactions/1` (2023-10-19 15:52:30)
- `/1bdffdced47df42750cc88cd4064909cbb2f02fa276da2b69992fb63e0962bbe/kad` (2023-10-19 15:52:30)
- `/dot-bulletin/state/2` (2023-10-19 15:52:30)
- `/dot-bulletin/sync/2` (2023-10-19 15:52:30)
- `/1bdffdced47df42750cc88cd4064909cbb2f02fa276da2b69992fb63e0962bbe/block-announces/1` (2023-10-19 15:52:30)
- `/1bdffdced47df42750cc88cd4064909cbb2f02fa276da2b69992fb63e0962bbe/grandpa/1` (2023-10-19 15:52:30)
- `/dot-bulletin/kad` (2023-10-19 15:52:30)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 214 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `51.15.128.68` | FR | 182 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `172.33.1.5` | US | 96 | ['kubo/0.15.0/3ae52a4', 'kubo/0.17.0/4485d6b', 'kubo/0.22.0/3f884d3/docker']| False  |
| `51.158.240.182` | FR | 64 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `163.172.146.218` | FR | 56 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `203.161.53.164` | MY | 46 | ['kubo/0.20.0/b8c4725/docker']| False  |
| `51.158.117.131` | FR | 44 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `212.47.244.180` | FR | 34 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `151.115.54.82` | PL | 27 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.154.220` | FR | 27 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2023-10-16` to `2023-10-23` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-10-16` to `2023-10-23` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-10-16` to `2023-10-23` in the DHT and their datacenter association.

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