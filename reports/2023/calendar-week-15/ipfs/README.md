# Nebula Measurement Results Calendar Week 15 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 15 - 2023](#nebula-measurement-results-calendar-week-14---2023)
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

The following results show measurement data that were collected in calendar week 15 in 2023 from `2023-04-10` to `2023-04-17`.

- Number of crawls `336`
- Number of visits `42,879,608`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `60,376`
- Number of unique peer IDs discovered in the DHT `60,279`
- Number of unique IP addresses found `53,846`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/amba-p2p@53d0172c8-dirty` (2023-04-10 11:22:58)
- `kubo/0.21.0-dev/a97bf42/docker` (2023-04-10 11:52:04)
- `kubo/0.19.1/958e586ca/desktop` (2023-04-10 12:22:04)
- `kubo/0.19.0-dev/b583569/docker` (2023-04-10 13:52:02)
- `libp2p-chat` (2023-04-10 15:51:37)
- `kubo/0.21.0-dev/` (2023-04-10 23:22:46)
- `github.com/nickjfree/goose@51b96a454-dirty` (2023-04-11 02:23:23)
- `kubo/0.21.0-dev/03a98280e-dirty` (2023-04-11 07:23:30)
- `kubo/0.21.0-dev/56a3b35/docker` (2023-04-11 07:52:49)
- `kubo/0.21.0-dev/03a9828/docker` (2023-04-11 08:23:06)
- `github.com/libp2p/go-libp2p/examples/pubsub/chat@952f7cbc5` (2023-04-11 09:53:29)
- `github.com/mearaj/protonet@82db6c065-dirty` (2023-04-11 12:22:48)
- `kubo/0.21.0-dev/41d415929` (2023-04-11 13:21:48)
- `github.com/mearaj/protonet@77e2a9edc-dirty` (2023-04-11 13:53:03)
- `github.com/gioapp/cms` (2023-04-11 13:53:32)
- `github.com/mearaj/protonet@8553038be-dirty` (2023-04-11 16:54:02)
- `kubo/0.19.1/958e586ca-dirty/docker` (2023-04-11 19:21:23)
- `kubo/0.21.0-dev/3a15a0fc5` (2023-04-12 07:21:08)
- `kubo/0.21.0-dev/3a15a0f/docker` (2023-04-12 08:23:09)
- `github.com/mearaj/protonet@1d544cf99-dirty` (2023-04-12 10:22:19)
- `github.com/mearaj/protonet@4c6f244a0-dirty` (2023-04-12 10:51:47)
- `0.11.0` (2023-04-12 14:52:18)
- `github.com/mearaj/protonet@f335465ee-dirty` (2023-04-12 14:52:35)
- `github.com/mearaj/protonet@b3df2b570-dirty` (2023-04-12 16:53:14)
- `example/gotest@` (2023-04-12 17:51:39)
- `delta@915821b91` (2023-04-12 18:51:12)
- `github.com/mearaj/protonet@8b183fa3d-dirty` (2023-04-12 20:52:51)
- `github.com/mearaj/protonet@65a582105-dirty` (2023-04-13 01:52:26)
- `main@5bbc51363-dirty` (2023-04-13 05:21:22)
- `github.com/4everland/ipfs-servers@eb17031bd-dirty` (2023-04-13 10:21:29)
- `github.com/mearaj/protonet@5e1afa343-dirty` (2023-04-13 13:22:08)
- `github.com/mearaj/protonet@1c6664be6-dirty` (2023-04-13 14:52:30)
- `github.com/mearaj/protonet@e5f75c98e-dirty` (2023-04-13 15:52:47)
- `main@ab1485c58-dirty` (2023-04-13 17:52:29)
- `github.com/ethtweet/ethtweet@8614ea7d3-dirty` (2023-04-14 06:51:57)
- `github.com/mearaj/protonet@5b7d175da` (2023-04-14 07:51:22)
- `kubo/0.21.0-dev/78895a1/docker` (2023-04-14 13:23:18)
- `go.vocdoni.io/dvote@c9425c1fd-dirty` (2023-04-14 13:51:21)
- `go.vocdoni.io/dvote@93405fef1-dirty` (2023-04-14 14:22:50)
- `kubo/0.21.0-dev/78895a118` (2023-04-15 10:51:57)
- `github.com/mearaj/protonet@cac1100ff` (2023-04-15 14:22:37)
- `kubo/0.21.0-dev/3a15a0fc5-dirty` (2023-04-15 14:51:14)
- `delta@35b0241a6-dirty` (2023-04-16 06:21:56)
- `kubo/0.20.0-dev/80826d0/docker` (2023-04-16 18:53:02)
- `main@3125fbc11-dirty` (2023-04-16 19:52:22)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/prox/0.0.1` (2023-04-11 03:51:50)
- `fx/file/1` (2023-04-13 06:23:02)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `54.187.21.48` | US | 2498 | ['kubo/0.17.0/4485d6b71', 'main@3125fbc11-dirty', 'main@5078dd95d-dirty', 'main@5bbc51363-dirty', 'main@ab1485c58-dirty', 'SybilNode@ef7cf7ce7-dirty']| True  |
| `193.60.241.97` | GB | 1928 | ['kubo/0.16.0-dev/b6b97d90a', 'SybilNode@f69d6f031-dirty']| False  |
| `159.203.76.161` | US | 299 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `193.60.241.98` | GB | 266 | ['hydra-booster/0.7.4', 'kubo/0.15.0/3ae52a41e', 'main@', 'SybilNode@', 'SybilNode@d54ece3ca-dirty']| False  |
| `117.174.25.136` | CN | 64 | ['go-ipfs/0.8.0/cc95853']| False  |
| `111.9.31.185` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.208` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.135` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.137` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.181` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |

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

In the specified time interval from `2023-04-10` to `2023-04-17` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-04-10` to `2023-04-17` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-04-10` to `2023-04-17` in the DHT and their datacenter association.

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
