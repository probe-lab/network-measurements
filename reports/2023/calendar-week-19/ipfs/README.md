# Nebula Measurement Results Calendar Week 19 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 19 - 2023](#nebula-measurement-results-calendar-week-19---2023)
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

The following results show measurement data that were collected in calendar week 19 in 2023 from `2023-05-08` to `2023-05-15`.

- Number of crawls `336`
- Number of visits `42,110,078`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `38,129`
- Number of unique peer IDs discovered in the DHT `38,029`
- Number of unique IP addresses found `54,980`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `go.vocdoni.io/dvote@071ace240-dirty` (2023-05-08 01:22:50)
- `0.11.4` (2023-05-08 07:51:47)
- `github.com/hpzzz/p2p_app@364f1c0ec-dirty` (2023-05-08 13:23:23)
- `go.vocdoni.io/dvote@cd9e93fac-dirty` (2023-05-08 15:21:58)
- `go-ipfs/0.13.0-dev/4ad316803` (2023-05-08 15:53:16)
- `github.com/hpzzz/p2p_app@992dacaa4-dirty` (2023-05-08 15:53:45)
- `kubo/0.21.0-dev/c178c51/docker` (2023-05-08 18:51:25)
- `go.vocdoni.io/dvote@82df13aab-dirty` (2023-05-08 22:22:33)
- `go.vocdoni.io/dvote@9a40b1b51-dirty` (2023-05-08 23:21:17)
- `gitlab.com/nunet/device-management-service@134abc73b-dirty` (2023-05-09 06:21:17)
- `kubo/0.21.0-dev/c178c5183` (2023-05-09 06:53:17)
- `go.vocdoni.io/dvote@d461ff689-dirty` (2023-05-09 09:52:40)
- `kubo/0.20.0/b8c4725/docker` (2023-05-09 10:21:03)
- `github.com/hpzzz/p2p_app@56c4418cf-dirty` (2023-05-09 12:53:34)
- `kubo/0.20.0/b8c472500` (2023-05-09 13:21:16)
- `go.vocdoni.io/dvote@b30a5cf0a-dirty` (2023-05-09 13:21:43)
- `kubo/0.20.0/b8c4725/s̳̪̦̩̝͎͙͝u͍̫̺̝̱̰͝p̠͔̫͓̬̦` (2023-05-09 13:22:16)
- `kubo/0.20.0/` (2023-05-09 13:22:25)
- `github.com/application-research/estuary@f44f6bc2a-dirty` (2023-05-09 13:51:59)
- `go.vocdoni.io/dvote@8168c864a-dirty` (2023-05-09 13:52:07)
- `kubo/0.20.0/desktop` (2023-05-09 14:52:38)
- `a@` (2023-05-09 15:23:35)
- `kubo/0.20.0/b8c4725` (2023-05-09 15:51:40)
- `kubo/0.21.0-dev/b27da1cc8-dirty` (2023-05-09 19:25:00)
- `kubo/0.21.0-dev/f7cab554f` (2023-05-10 04:52:34)
- `go.vocdoni.io/dvote@8903e32bd-dirty` (2023-05-10 07:51:20)
- `kubo/0.21.0-dev/eab0baa/docker` (2023-05-10 07:52:49)
- `kubo/0.21.0-dev/0e7331c95` (2023-05-10 10:51:53)
- `kubo/0.21.0-dev/0e7331c/docker` (2023-05-10 11:22:58)
- `kubo/0.21.0-dev/61f8c7301-dirty` (2023-05-10 14:22:33)
- `kubo/0.21.0-dev/61f8c73/docker` (2023-05-10 15:23:48)
- `github.com/application-research/estuary@42a3d0ed9-dirty` (2023-05-10 19:22:11)
- `kubo/0.19.0-dev/766671321-dirty` (2023-05-11 07:22:59)
- `github.com/amba-p2p@a483329af-dirty` (2023-05-11 12:52:30)
- `github.com/application-research/estuary@08b9bad61-dirty` (2023-05-11 13:53:28)
- `go-ipfs/0.13.0-dev/91c526571` (2023-05-11 17:22:46)
- `github.com/application-research/estuary@1a87d30e3-dirty` (2023-05-11 17:51:31)
- `kubo/0.21.0-dev/61f8c7301` (2023-05-11 18:51:18)
- `go.vocdoni.io/dvote@af85c0571-dirty` (2023-05-12 10:22:14)
- `go.vocdoni.io/dvote@911ae8550-dirty` (2023-05-12 21:51:58)
- `totti/portforward@` (2023-05-13 06:52:14)
- `github.com/ethtweet/ethtweet@2e11c6ad7-dirty` (2023-05-13 18:22:54)
- `github.com/ethtweet/ethtweet@f60d25db4-dirty` (2023-05-14 09:22:59)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/echo/echoreq/0.0.1` (2023-05-10 18:23:31)
- `/nunet/dms/ping/0.0.1` (2023-05-10 22:52:27)
- `/nunet/dms/depreq/0.0.2` (2023-05-10 22:52:27)
- `/idena/gossip/1.1.0` (2023-05-12 14:21:23)
- `/nunet/dms/dht/0.0.2` (2023-05-12 16:52:28)
- `/port-forward/0.0.1` (2023-05-13 06:52:14)
- `c4d2b0a90265860e2c404e5e4f32ad05124076f8a8c5838881cb4ee7e0e5e529` (2023-05-14 20:22:28)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 262 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `117.174.25.136` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.135` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `111.9.31.185` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `118.113.192.67` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.137` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.187` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.181` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.208` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `182.149.116.105` | CN | 61 | ['go-ipfs/0.8.0/cc95853']| False  |

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

In the specified time interval from `2023-05-08` to `2023-05-15` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-05-08` to `2023-05-15` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-05-08` to `2023-05-15` in the DHT and their datacenter association.

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

Code can be found here: [dennis-tra/parsec](https://github.com/dennis-tra/parsec) (we plan to move this to our [ProbeLab organization](https://github.com/plprobelab))

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