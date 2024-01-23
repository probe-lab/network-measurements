# Nebula Measurement Results Calendar Week 10 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 10 - 2023](#nebula-measurement-results-calendar-week-10---2023)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
    - [Agent Versions](#agent-versions)
    - [Protocols](#protocols)
    - [Top 10 Rotating Nodes](#top-10-rotating-nodes)
    - [Crawls](#crawls)
      - [Overall](#overall)
      - [Classification](#classification)
      - [Agents](#agents)
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
  - [DHT Performance](#dht-performance)
    - [Weekly](#weekly)
    - [Daily](#daily)
  - [Terminology](#terminology)
    - [Peer Classification](#peer-classification)
    - [Storm Specific Protocols](#storm-specific-protocols)

## General Information

The following results show measurement data that were collected in calendar week 10 in 2023 from `2023-03-06` to `2023-03-13`.

- Number of crawls `336`
- Number of visits `44,753,313` (Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur)
- Number of unique peer IDs visited `41,498`
- Number of unique peer IDs discovered in the DHT `41,388`
- Number of unique IP addresses found `54,012` (IPv4 + IPv6)

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/Jackieyewang/TSC-2023/action/peer/basic-chat-with-rendezvous@cc1a5e256-dirty` (2023-03-06 08:22:47)
- `go.vocdoni.io/dvote@f0e377e0b-dirty` (2023-03-06 10:51:14)
- `go.vocdoni.io/dvote@035d354e2-dirty` (2023-03-06 11:51:24)
- `go.vocdoni.io/dvote@3562a366a-dirty` (2023-03-06 12:23:25)
- `go.vocdoni.io/dvote@b890aab9b-dirty` (2023-03-06 12:51:21)
- `go.vocdoni.io/dvote@00817b99f-dirty` (2023-03-06 14:23:19)
- `kubo/0.19.0-rc1/0f1181d/docker` (2023-03-06 15:51:35)
- `kubo/0.19.0-rc1/desktop` (2023-03-06 16:21:30)
- `kubo/0.18.1/brave` (2023-03-06 16:52:09)
- `kubo/0.19.0-rc1/0f1181d` (2023-03-06 23:21:08)
- `delta@fd9a84622-dirty` (2023-03-07 01:22:28)
- `kubo/0.20.0-dev/6d7ad61/docker` (2023-03-07 01:22:41)
- `github.com/mearaj/protonet@5c82f4702-dirty` (2023-03-07 03:53:59)
- `github.com/photon-storage/go-photon@2ce12fc1c` (2023-03-07 05:51:35)
- `github.com/photon-storage/go-photon@2ce12fc1c-dirty` (2023-03-07 06:23:27)
- `go.vocdoni.io/dvote@61101a8e4-dirty` (2023-03-07 12:22:01)
- `go.vocdoni.io/dvote@410e1daec-dirty` (2023-03-07 12:23:53)
- `go.vocdoni.io/dvote@a90660636-dirty` (2023-03-07 14:51:34)
- `go.vocdoni.io/dvote@30204eeff-dirty` (2023-03-07 14:52:12)
- `delta@f99216266-dirty` (2023-03-07 15:52:20)
- `kubo/0.20.0-dev/c6f1f4d/docker` (2023-03-07 15:53:31)
- `decrux@31e8c1b4f` (2023-03-07 19:53:53)
- `kubo/0.19.0-rc1/` (2023-03-07 20:53:53)
- `github.com/mearaj/protonet@c18303c02-dirty` (2023-03-07 22:21:37)
- `github.com/mearaj/protonet@a90b82fd3-dirty` (2023-03-07 22:52:23)
- `github.com/mearaj/protonet@11ba4f051` (2023-03-08 00:52:21)
- `delta@34c8d685f-dirty` (2023-03-08 02:52:10)
- `kubo/0.20.0-dev/ec13650/docker` (2023-03-08 08:51:49)
- `github.com/mearaj/protonet@a5657bcd1-dirty` (2023-03-08 15:52:30)
- `github.com/application-research/estuary@6558d0685` (2023-03-08 19:20:55)
- `github.com/application-research/estuary@6558d0685-dirty` (2023-03-08 19:21:30)
- `github.com/mearaj/protonet@0de63d28b-dirty` (2023-03-08 23:23:55)
- `kubo/0.19.0-rc1/0f1181d/s̳̪̦̩̝͎͙͝u͍̫̺̝̱̰͝p̠͔̫͓̬̦` (2023-03-09 00:53:39)
- `github.com/mearaj/protonet@63807214e-dirty` (2023-03-09 03:23:49)
- `kubo/0.20.0-dev/` (2023-03-09 03:52:00)
- `kubo/0.19.0-rc1/0f1181d23` (2023-03-09 10:51:20)
- `github.com/mearaj/protonet@20ec4958d-dirty` (2023-03-09 16:51:51)
- `github.com/mearaj/protonet@78206ac75-dirty` (2023-03-09 18:22:40)
- `github.com/mearaj/protonet@032741c09-dirty` (2023-03-09 20:53:09)
- `github.com/mearaj/protonet@01bfac900-dirty` (2023-03-09 21:22:03)
- `validation-bot@84378f68e` (2023-03-09 22:23:20)
- `github.com/mearaj/protonet@d4edcbbc9` (2023-03-09 23:51:17)
- `go-ipfs/0.8.0-dev/0401f6097-dirty` (2023-03-10 03:21:31)
- `github.com/photon-storage/go-photon@f640d23b3-dirty` (2023-03-10 03:51:46)
- `github.com/mearaj/protonet@26bd06370-dirty` (2023-03-10 03:53:19)
- `github.com/mearaj/protonet@378b4b8cd-dirty` (2023-03-10 05:24:18)
- `github.com/bpc2016/p2p@c2ec28936-dirty` (2023-03-10 06:51:39)
- `main@` (2023-03-10 09:53:27)
- `go.vocdoni.io/dvote@f6bb28920-dirty` (2023-03-10 10:21:20)
- `github.com/photon-storage/go-photon@34318c22b` (2023-03-10 11:52:47)
- `kubo/0.20.0-dev/5ad5158e8` (2023-03-10 14:52:03)
- `delta@a37a7eba0-dirty` (2023-03-11 00:51:45)
- `github.com/mearaj/protonet@710670f92` (2023-03-11 00:52:17)
- `github.com/mearaj/protonet@710670f92-dirty` (2023-03-11 01:23:10)
- `github.com/mearaj/protonet@767b86801-dirty` (2023-03-11 04:52:45)
- `github.com/mearaj/protonet@7d73e64ca-dirty` (2023-03-11 06:52:34)
- `kubo/0.20.0-dev/a4052c645` (2023-03-11 06:53:39)
- `kubo/0.20.0-dev/a4052c645-dirty` (2023-03-11 07:22:04)
- `kubo/0.20.0-dev/a4052c6/docker` (2023-03-11 09:53:10)
- `github.com/mearaj/protonet@58377133f` (2023-03-11 14:51:35)
- `github.com/mearaj/protonet@58377133f-dirty` (2023-03-11 14:53:25)
- `delta@cf4f25056-dirty` (2023-03-11 15:21:27)
- `github.com/mearaj/protonet@075541dcf-dirty` (2023-03-12 00:21:16)
- `github.com/mearaj/protonet@bfe2fcccb-dirty` (2023-03-12 00:51:59)
- `github.com/mearaj/protonet@1f4985d62-dirty` (2023-03-12 01:51:23)
- `github.com/photon-storage/go-photon@34318c22b-dirty` (2023-03-12 01:53:19)
- `delta@c6ac0e3f8-dirty` (2023-03-12 13:51:27)
- `github.com/mearaj/protonet@e34fd6b34` (2023-03-12 20:21:18)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:



### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `193.60.241.98` | GB | 299 | ['hydra-booster/0.7.4', 'kubo/0.15.0/3ae52a41e', 'SybilNode@d54ece3ca-dirty', 'SybilNode@ee19f0e95-dirty']| False  |
| `159.203.76.161` | US | 292 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `54.146.127.35` | US | 70 | ['iroh/0.2.0']| True  |
| `117.174.25.136` | CN | 64 | ['go-ipfs/0.8.0/cc95853']| False  |
| `54.187.21.48` | US | 64 | ['kubo/0.17.0/4485d6b71', 'main@f1ecfa16c-dirty', 'SybilNode@9ebc0a872-dirty']| True  |
| `117.174.25.135` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `111.9.31.185` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.181` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.137` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.187` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |

### Crawls

#### Overall

![Crawl Overview](./plots/crawl-overview.png)

#### Classification

![Crawl Classifications](./plots/crawl-classifications.png)

#### Agents

![Crawl Properties By Agent](./plots/crawl-properties.png)

Only the top 10 kubo versions appear in the right graph (due to lack of colors) based on the average count in the time interval. The `0.8.x` versions **do not** contain disguised storm peers.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

#### Errors

![Crawl Errors](./plots/crawl-errors.png)

#### Total Peer IDs Discovered Classification

![Peer count by classification](./plots/peer-classifications.png)

In the specified time interval from `2023-03-06` to `2023-03-13` we visited `41,498` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-03-06` to `2023-03-13` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-03-06` to `2023-03-13` in the DHT and their datacenter association.

### Classification

![Datacenter Distribution By Classification](./plots/cloud-classification.png)

The classifications are documented [here](#peer-classification). Note that the x-axes are different.

### Agents

![Datacenter Distribution By Agent](./plots/cloud-agents.png)

The number in parentheses in the graph titles show the number of unique peer IDs that went into the specific subgraph.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

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


## Terminology

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