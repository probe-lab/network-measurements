# Nebula Measurement Results Calendar Week 31 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 31 - 2023](#nebula-measurement-results-calendar-week-31---2023)
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

The following results show measurement data that were collected in calendar week 31 in 2023 from `2023-07-31` to `2023-08-07`.

- Number of crawls `334`
- Number of visits `54,426,845`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `44,840`
- Number of unique peer IDs discovered in the DHT `44,735`
- Number of unique IP addresses found `61,438`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `0.0.3-unstable-2023-07-28` (2023-07-31 08:22:02)
- `kubo/0.23.0-dev/89b043238` (2023-07-31 17:21:03)
- `gobind` (2023-07-31 19:22:42)
- `kubo/0.23.0-dev/89b0432/docker` (2023-07-31 20:22:59)
- `kubo/0.19.0-dev/fd1d36ee6-dirty` (2023-08-01 05:22:04)
- `github.com/ikeikeikeike/vpn-mesh@5be1d08a0-dirty` (2023-08-01 08:52:40)
- `kubo/ceramic-0.19.1-validator/` (2023-08-01 19:22:14)
- `github.com/ikeikeikeike/vpn-mesh@91174ada4-dirty` (2023-08-01 19:51:53)
- `github.com/ikeikeikeike/vpn-mesh@91174ada4` (2023-08-01 19:52:28)
- `kubo/ceramic-0.19.1-validator/1c3115f-dirty/docker` (2023-08-01 22:52:46)
- `kubo/ceramic-0.19.1-validator/3760a0f-dirty/docker` (2023-08-02 03:22:51)
- `kubo/0.22.0-rc1/9db33d3/docker` (2023-08-02 06:21:34)
- `kubo/0.22.0-dev/de3982d` (2023-08-02 07:21:54)
- `0.0.5-unstable-2023-08-02` (2023-08-02 11:22:25)
- `github.com/IceFireDB/IceFireDB-Proxy` (2023-08-03 00:22:25)
- `kubo/ceramic-0.19.1-validator/0331144-dirty/docker` (2023-08-03 03:52:49)
- `0.0.5-unstable-2023-08-04` (2023-08-03 17:22:26)
- `kubo/0.23.0-dev/` (2023-08-03 17:52:25)
- `kubo/0.23.0-dev/7977f26/docker` (2023-08-03 21:22:36)
- `kubo/0.23.0-dev/7977f26e8` (2023-08-03 21:51:43)
- `0.0.4-unstable-2023-08-02` (2023-08-03 22:22:55)
- `app-ecos@85ef34f7f-dirty` (2023-08-04 14:52:53)
- `kubo/0.23.0-dev/4cd49cf/docker` (2023-08-04 20:52:19)
- `kubo/0.19.2/a002e89-dirty` (2023-08-05 14:52:12)
- `kubo/0.19.2/2a38430-dirty` (2023-08-06 03:52:25)
- `kubo/0.19.2/8780dde-dirty` (2023-08-06 07:52:28)
- `kubo/0.21.0/294db3e30/docker` (2023-08-06 12:52:06)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `gobind`
- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `ConnectionHandler.rpc_backward_stream` (2023-07-31 13:52:15)
- `ConnectionHandler.rpc_forward_stream` (2023-07-31 13:52:15)
- `ConnectionHandler.rpc_info` (2023-07-31 15:22:45)
- `ConnectionHandler.rpc_backward` (2023-07-31 15:22:45)
- `ConnectionHandler.rpc_forward` (2023-07-31 15:22:45)
- `/mesh/discovery/0.0.1` (2023-08-01 18:52:08)
- `/MarzTunnl/TestBench/0.0.1` (2023-08-01 19:52:54)
- `/iin/0.0.1` (2023-08-02 18:52:40)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 200 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `35.199.42.20` | US | 104 | ['Taubyte Node v1.0']| True  |
| `44.206.49.127` | US | 62 | ['kubo/0.14.0-rc1/']| True  |
| `123.240.86.23` | TW | 27 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `91.39.197.21` | DE | 26 | ['go-ipfs/0.6.0/']| False  |
| `37.211.184.148` | QA | 26 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `61.65.53.92` | TW | 26 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `172.33.1.5` | US | 25 | ['kubo/0.15.0/3ae52a4', 'kubo/0.17.0/4485d6b']| False  |
| `91.53.110.182` | DE | 22 | ['go-ipfs/0.6.0/']| False  |
| `91.53.121.132` | DE | 22 | ['go-ipfs/0.6.0/']| False  |

### Crawls

#### Overall

![Crawl Overview](./plots/crawl-overview.png)

#### Classification

![Crawl Classifications](./plots/crawl-classifications.png)

#### Agents

![Crawl Properties By Agent](./plots/crawl-properties.png)

Only the top 10 kubo versions appear in the right graph (due to lack of colors) based on the average count in the time interval. The `0.8.x` versions **do not** contain disguised storm peers.

`storm*` are `gobind, go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

#### DHT Server vs. Clients

You can find the most up-to-date graph on [`probelab.io/ipfskpi`](https://probelab.io/ipfskpi/#ipfs-servers-vs-clients-plot).

#### Errors

![Crawl Errors](./plots/crawl-errors.png)

#### Total Peer IDs Discovered Classification

![Peer count by classification](./plots/peer-classifications.png)

In the specified time interval from `2023-07-31` to `2023-08-07` we visited `` unique peer IDs.
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

`storm*` are `gobind, go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Inter Arrival Time

![Inter Arrival Time](./plots/peer-inter-arrival-time.png)

Only the top 10 kubo versions appear in the right graph (due to lack of colors) based on the average count in the time interval. The `0.8.x` versions **do not** contain disguised storm peers.

`storm*` are `gobind, go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

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
`storm*` are `gobind, go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Geolocation

### Unique IP Addresses

![Unique IP addresses](./plots/geo-unique-ip.png)

This graph shows all IP addresses that we found from `2023-07-31` to `2023-08-07` in the DHT and their geolocation distribution by country.

### Classification

![Peer Geolocation By Classification](./plots/geo-peer-classification.png)

The classifications are documented [here](#peer-classification). 
The number in parentheses in the graph titles show the number of unique peer IDs that went into the specific subgraph.

### Agents

![Peer Geolocation By Agent](./plots/geo-peer-agents.png)

`storm*` are `gobind, go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Datacenters

### Overall

![Overall Datacenter Distribution](./plots/cloud-overall.png)

This graph shows all IP addresses that we found from `2023-07-31` to `2023-08-07` in the DHT and their datacenter association.

### Classification

![Datacenter Distribution By Classification](./plots/cloud-classification.png)

The classifications are documented [here](#peer-classification). Note that the x-axes are different.

### Agents

![Datacenter Distribution By Agent](./plots/cloud-agents.png)

The number in parentheses in the graph titles show the number of unique peer IDs that went into the specific subgraph.

`storm*` are `gobind, go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

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

Code can be found here: [dennis-tra/parsec](https://github.com/dennis-tra/parsec) (we plan to move this to our [ProbeLab organization](https://github.com/plprobelab))

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