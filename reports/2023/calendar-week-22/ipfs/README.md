# Nebula Measurement Results Calendar Week 22 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 22 - 2023](#nebula-measurement-results-calendar-week-22---2023)
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

The following results show measurement data that were collected in calendar week 22 in 2023 from `2023-05-29` to `2023-06-05`.

- Number of crawls `334`
- Number of visits `53,409,198`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `43,831`
- Number of unique peer IDs discovered in the DHT `43,731`
- Number of unique IP addresses found `62,062`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.21.0-dev/e3126eb/docker` (2023-05-29 12:21:46)
- `kubo/0.21.0-dev/38556b8/docker` (2023-05-29 15:52:31)
- `github.com/dennis-tra/parsec@ff893ed49-dirty` (2023-05-30 08:53:42)
- `kubo/0.21.0-dev/c10b804/docker` (2023-05-30 09:23:30)
- `github.com/dennis-tra/parsec@028ca3e3e-dirty` (2023-05-30 11:51:53)
- `github.com/dennis-tra/parsec@3c433e429-dirty` (2023-05-30 13:51:18)
- `gitlab.com/nunet/bootstrap-node@d1a9ccab5-dirty` (2023-05-30 15:23:38)
- `kubo/0.21.0-dev/1869a17a8` (2023-05-30 17:52:49)
- `gitlab.com/nunet/device-management-service@c026371c7-dirty` (2023-05-30 19:23:57)
- `github.com/dennis-tra/parsec@687f02f68-dirty` (2023-05-31 07:21:43)
- `kubo/0.20.0-rc2/8418b083d-dirty` (2023-05-31 09:51:43)
- `gitlab.com/nunet/device-management-service@e1a45a8dd-dirty` (2023-05-31 15:23:38)
- `gitlab.com/nunet/device-management-service@36e543bd2-dirty` (2023-06-01 09:52:33)
- `kubo/0.21.0-dev/dfd244816-dirty` (2023-06-01 09:53:56)
- `github.com/application-research/edge-ur@9cd69a9d4-dirty` (2023-06-01 12:51:17)
- `go-ipfs/0.13.0/:SHA` (2023-06-01 12:52:16)
- `github.com/application-research/edge-ur@b7d6a0e88-dirty` (2023-06-01 14:51:28)
- `kubo/0.21.0-dev/6eef0b4/docker` (2023-06-01 14:53:31)
- `delta@2ca99701d-dirty` (2023-06-01 15:23:59)
- `kubo/0.21.0-dev/5eb0723bf` (2023-06-01 16:23:30)
- `github.com/application-research/edge-ur@b56055897-dirty` (2023-06-01 20:22:47)
- `kubo/0.21.0-dev/8fbf39d32` (2023-06-01 21:52:52)
- `github.com/application-research/edge-ur@2c4b148db-dirty` (2023-06-01 22:22:53)
- `kubo/0.21.0-dev/7efb5836f-dirty` (2023-06-01 23:52:02)
- `kubo/0.21.0-dev/eb265f7/docker` (2023-06-02 11:53:19)
- `kubo/0.20.0/brave` (2023-06-02 20:23:28)
- `github.com/application-research/edge-ur@bfbcf7645-dirty` (2023-06-03 11:54:53)
- `delta@4ba3866e7-dirty` (2023-06-03 12:52:39)
- `kubo/0.21.0-dev/8f0359a97` (2023-06-03 17:51:32)
- `github.com/application-research/edge-ur@37f9fc367-dirty` (2023-06-03 23:52:43)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/mintter/0.0.4` (2023-06-03 00:53:54)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 256 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `145.40.68.85` | NL | 57 | ['Taubyte Node v1.0']| False  |
| `35.199.42.20` | US | 57 | ['Taubyte Node v1.0']| True  |
| `86.109.9.179` | US | 56 | ['Taubyte Node v1.0']| True  |
| `54.187.21.48` | US | 50 | ['kubo/0.17.0/4485d6b71', 'SybilNode@ef7cf7ce7-dirty']| True  |
| `111.9.31.185` | CN | 44 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.136` | CN | 44 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.187` | CN | 44 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.137` | CN | 43 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.135` | CN | 43 | ['go-ipfs/0.8.0/cc95853']| False  |

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

![DHT Server vs. Clients](./plots/dht-servers-vs-clients.png)

- DHT Server peers: unique peers that we found with our network crawls
- DHT Client peers: unique peers that we saw from our bootstrapper/preload nodes minus DHT Server peers

#### Errors

![Crawl Errors](./plots/crawl-errors.png)

#### Total Peer IDs Discovered Classification

![Peer count by classification](./plots/peer-classifications.png)

In the specified time interval from `2023-05-29` to `2023-06-05` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-05-29` to `2023-06-05` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-05-29` to `2023-06-05` in the DHT and their datacenter association.

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

**TODO**: As soon as we have more than two full weeks of data we'll report weekly graphs.

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