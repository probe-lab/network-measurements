# Nebula Measurement Results Calendar Week 13 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 13 - 2023](#nebula-measurement-results-calendar-week-13---2023)
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

The following results show measurement data that were collected in calendar week 13 in 2023 from `2023-03-27` to `2023-04-03`.

- Number of crawls `336`
- Number of visits `44,387,575`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `48,939`
- Number of unique peer IDs discovered in the DHT `48,835`
- Number of unique IP addresses found `54,202`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `delta@26bd916be-dirty` (2023-03-27 03:21:46)
- `delta@4f0b68049-dirty` (2023-03-27 03:51:33)
- `kubo/0.20.0-dev/bf7d0fc/docker` (2023-03-27 11:53:06)
- `kubo/0.20.0-dev/88d431c/docker` (2023-03-27 17:23:30)
- `github.com/mearaj/protonet@77a9393d6-dirty` (2023-03-27 19:21:53)
- `github.com/mearaj/protonet@68faffab6-dirty` (2023-03-27 23:52:23)
- `github.com/mearaj/protonet@c052d010d-dirty` (2023-03-28 03:52:36)
- `github.com/mearaj/protonet@8f4629969-dirty` (2023-03-28 04:22:50)
- `github.com/mearaj/protonet@2997ed6c0-dirty` (2023-03-28 05:21:50)
- `github.com/mearaj/protonet@aa48b79a7` (2023-03-28 06:51:56)
- `kubo/0.20.0-dev/405b1d2/docker` (2023-03-28 06:52:48)
- `github.com/mearaj/protonet@aa48b79a7-dirty` (2023-03-28 07:53:19)
- `kubo/0.19.0-rc1/288a1168a` (2023-03-28 08:22:49)
- `kubo/0.18.1/505f072d2-dirty` (2023-03-28 09:22:00)
- `gitlab.com/nunet/device-management-service@73bba797f-dirty` (2023-03-28 10:23:02)
- `github.com/mearaj/protonet@19bcd2115` (2023-03-28 13:51:31)
- `kubo/0.20.0-dev/405b1d2dc` (2023-03-28 16:22:43)
- `validation-bot@7cee7c025` (2023-03-28 17:25:05)
- `go.vocdoni.io/dvote@9dd4e110b-dirty` (2023-03-28 21:51:12)
- `github.com/mearaj/protonet@529cb6fe8` (2023-03-28 22:22:39)
- `github.com/mearaj/protonet@529cb6fe8-dirty` (2023-03-28 23:22:12)
- `kubo/0.20.0-dev/ed671e848-dirty` (2023-03-29 06:51:53)
- `kubo/0.20.0-dev/3ab1086/docker` (2023-03-29 10:23:11)
- `github.com/dennis-tra/parsec@1c9a303fe-dirty` (2023-03-29 10:52:23)
- `kubo/0.19.0-rc1/288a1168a-dirty` (2023-03-29 10:53:01)
- `kubo/0.19.0/196321958-dirty/docker` (2023-03-29 13:21:16)
- `github.com/dennis-tra/parsec@9a0fc9a52-dirty` (2023-03-29 13:51:09)
- `kubo/0.15.0-rc1/` (2023-03-29 15:53:35)
- `github.com/dennis-tra/parsec@9f77bae53-dirty` (2023-03-29 16:22:02)
- `delta@0b8db5e0a-dirty` (2023-03-29 16:51:14)
- `github.com/dennis-tra/parsec@ba40eb8dd-dirty` (2023-03-29 17:21:44)
- `go-ipfs/0.9.0-dev/65d9507c3` (2023-03-29 18:22:01)
- `delta@07397eab6-dirty` (2023-03-30 00:21:21)
- `main@af9444801-dirty` (2023-03-30 05:51:52)
- `github.com/mearaj/protonet@10dcf4eb3-dirty` (2023-03-30 06:53:22)
- `github.com/dennis-tra/parsec@00bf3ec46-dirty` (2023-03-30 07:52:03)
- `kubo/0.20.0-dev/e89cce6/docker` (2023-03-30 09:52:58)
- `github.com/4everland/ipfs-servers@12926ed10-dirty` (2023-03-30 14:53:36)
- `github.com/mearaj/protonet@f77bea64e` (2023-03-30 16:21:37)
- `github.com/mearaj/protonet@171956fc7` (2023-03-30 17:21:46)
- `validation-bot@2c4751016` (2023-03-30 17:52:46)
- `kubo/0.20.0-dev/353dd49be` (2023-03-30 18:52:36)
- `delta@07397eab6` (2023-03-30 20:54:00)
- `kubo/0.20.0-dev/61e787d53-dirty` (2023-03-31 02:23:20)
- `kubo/0.20.0-dev/e89cce6` (2023-03-31 03:53:36)
- `kubo/0.20.0-dev/daa597c3e-dirty` (2023-03-31 04:53:15)
- `relayd/1.0` (2023-03-31 07:22:59)
- `kubo/0.17.0-dev/b5b18e23e` (2023-03-31 10:53:36)
- `kubo/0.20.0-dev/c81d2da/docker` (2023-03-31 12:22:02)
- `kubo/0.20.0-dev/3ab1086f7` (2023-03-31 12:52:42)
- `go-ipfs/0.13.0-rc1/` (2023-03-31 16:23:00)
- `github.com/dennis-tra/parsec@2fe673e0c-dirty` (2023-03-31 17:21:09)
- `go.vocdoni.io/dvote@7ca99b817-dirty` (2023-03-31 17:52:28)
- `kubo/0.20.0-dev/353dd49be-dirty` (2023-03-31 19:22:43)
- `kubo/0.20.0-dev/ac3e6b02b-dirty` (2023-03-31 22:53:50)
- `delta@c0e3dbe31-dirty` (2023-04-01 00:21:13)
- `github.com/mearaj/protonet@b3229800b-dirty` (2023-04-01 10:52:23)
- `github.com/dennis-tra/parsec@6df28db0c-dirty` (2023-04-01 12:53:34)
- `kubo/0.20.0-dev/6dffb587d-dirty` (2023-04-01 13:52:25)
- `kubo/0.20.0-dev/55587d8/filebase` (2023-04-01 14:21:03)
- `main@94dd84eb7-dirty` (2023-04-01 15:51:34)
- `github.com/mearaj/protonet@a8cc84c9c-dirty` (2023-04-02 01:22:31)
- `delta@b4d65dcdb-dirty` (2023-04-02 12:22:56)
- `delta@25735eb27-dirty` (2023-04-02 13:21:13)
- `delta@d5e89047d-dirty` (2023-04-02 19:52:02)
- `delta@9c76b3ec1-dirty` (2023-04-02 20:21:14)
- `kubo/0.20.0-dev/55587d8/docker` (2023-04-02 21:51:53)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/aichat/1.0.0` (2023-03-30 15:53:38)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `193.60.241.97` | GB | 1625 | ['kubo/0.16.0-dev/b6b97d90a', 'kubo/0.17.0-dev/b5b18e23e', 'SybilNode@adb4f469a-dirty']| False  |
| `159.203.76.161` | US | 261 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `54.187.21.48` | US | 255 | ['kubo/0.17.0/4485d6b71', 'main@94dd84eb7-dirty', 'main@af9444801-dirty', 'main@afb5e3386-dirty', 'SybilNode@ef7cf7ce7-dirty']| True  |
| `193.60.241.98` | GB | 190 | ['hydra-booster/0.7.4', 'kubo/0.15.0/3ae52a41e', 'SybilNode@d54ece3ca-dirty']| False  |
| `117.174.25.136` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.135` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `111.9.31.185` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.181` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.137` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.187` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |

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

In the specified time interval from `2023-03-27` to `2023-04-03` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-03-27` to `2023-04-03` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-03-27` to `2023-04-03` in the DHT and their datacenter association.

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
