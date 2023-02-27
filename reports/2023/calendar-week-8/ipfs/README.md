# Nebula Measurement Results Calendar Week 8 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 8 - 2023](#nebula-measurement-results-calendar-week-8---2023)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
    - [Agent Versions](#agent-versions)
    - [Protocols](#protocols)
    - [Top 10 Rotating Nodes](#top-10-rotating-nodes)
    - [Crawls](#crawls)
      - [Overall](#overall)
      - [Classification](#classification)
      - [Agents](#agents)
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
    - [DOMContentLoaded](#domcontentloaded)
    - [Peer Classification](#peer-classification)
    - [Storm Specific Protocols](#storm-specific-protocols)

## General Information

The following results show measurement data that were collected in calendar week 8 in 2023 from `2023-02-20` to `2023-02-27`.

- Number of crawls `336`
- Number of visits `44,380,027`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `65,236`
- Number of unique peer IDs discovered in the DHT `65,119`
- Number of unique IP addresses found `54,095`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `go-ipfs/0.11.0-dev/3f4e37f9a-dirty` (2023-02-20 16:21:49)
- `delta@4662a96b0-dirty` (2023-02-20 19:22:07)
- `SybilNode@9ebc0a872-dirty` (2023-02-20 22:51:24)
- `delta@2ee3144dc-dirty` (2023-02-21 02:22:55)
- `delta@1955f5bd1-dirty` (2023-02-21 02:52:08)
- `kubo/0.16.0/38117db/sti` (2023-02-21 03:23:49)
- `delta@eba315a69-dirty` (2023-02-21 04:22:08)
- `delta@eba315a69` (2023-02-21 04:52:18)
- `SybilNode@898075078-dirty` (2023-02-21 05:23:51)
- `SybilNode@fa0d91c23-dirty` (2023-02-21 06:23:33)
- `main@fa0d91c23-dirty` (2023-02-21 06:23:50)
- `dht2@` (2023-02-21 20:23:56)
- `validation-bot@c3d994223` (2023-02-21 21:53:07)
- `validation-bot@e06eb5da7` (2023-02-21 22:23:23)
- `validation-bot@758498d23` (2023-02-21 23:53:35)
- `kubo/0.19.0-dev/714a968/docker` (2023-02-22 00:52:51)
- `validation-bot@f75801865` (2023-02-22 02:53:29)
- `kubo/0.19.0-dev/a17e168a6-dirty` (2023-02-22 03:23:10)
- `delta@32339c71c-dirty` (2023-02-22 04:53:29)
- `delta@b6cfa6e7e-dirty` (2023-02-22 05:21:45)
- `kubo/0.19.0-dev/4db6ae177-dirty` (2023-02-22 05:52:32)
- `kubo/0.19.0-dev/4db6ae177` (2023-02-22 12:52:25)
- `kubo/0.19.0-dev/4db6ae1/docker` (2023-02-22 15:21:13)
- `kubo/0.19.0-dev/92a5ab5` (2023-02-22 17:22:16)
- `github.com/gloflow/gloflow@d08470672-dirty` (2023-02-22 19:53:09)
- `validation-bot@641df2eaf` (2023-02-22 20:22:47)
- `validation-bot@c5a5ee0f7` (2023-02-22 21:22:50)
- `kubo/0.19.0-dev/92a5ab527-dirty` (2023-02-22 22:21:11)
- `github.com/application-research/estuary@cdeee2914-dirty` (2023-02-23 01:23:36)
- `kubo/0.19.0-dev/86da181f7-dirty` (2023-02-23 08:53:29)
- `go-ipfs/0.14.0-dev/9db6641e-dirty` (2023-02-23 13:21:36)
- `validation-bot@b9799b4b4` (2023-02-23 16:53:37)
- `kubo/0.19.0-dev/dbfa1004a-dirty` (2023-02-23 17:21:56)
- `kubo/0.17.0/4485d6b-dirty/docker` (2023-02-23 18:52:01)
- `kubo/0.19.0-dev/f73cd19/docker` (2023-02-23 21:51:28)
- `delta@cda34b9ae-dirty` (2023-02-24 01:21:30)
- `delta@189d8618f-dirty` (2023-02-24 01:22:54)
- `main@f1ecfa16c-dirty` (2023-02-24 01:23:27)
- `delta@a99654e91-dirty` (2023-02-24 01:51:30)
- `kubo/0.19.0-dev/a3366c522` (2023-02-24 10:22:34)
- `kubo/0.18.1/505f072d2` (2023-02-24 10:52:01)
- `kubo/0.19.0-dev/4283b9d98` (2023-02-24 11:23:18)
- `kubo/0.19.0-dev/82ede56/docker` (2023-02-24 14:51:53)
- `kubo/0.19.0-dev/4283b9d/docker` (2023-02-24 16:51:33)
- `kubo/0.19.0-dev/4283b9d98-dirty` (2023-02-24 21:23:30)
- `delta@447ccf957-dirty` (2023-02-25 00:51:37)
- `delta@be6a38e44-dirty` (2023-02-26 07:22:26)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/p2pforwarder/dial/1.0.0` (2023-02-22 01:52:52)
- `/p2pforwarder/portssub/1.0.0` (2023-02-22 01:52:52)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `54.187.21.48` | US | 3260 | ['kubo/0.17.0/4485d6b71', 'main@f1ecfa16c-dirty', 'main@fa0d91c23-dirty', 'SybilNode@07f8aea17-dirty', 'SybilNode@347fc79bf-dirty', 'SybilNode@898075078-dirty', 'SybilNode@9ebc0a872-dirty', 'SybilNode@fa0d91c23-dirty']| True  |
| `193.60.241.98` | GB | 2697 | ['kubo/0.15.0/3ae52a41e', 'main@950539f12-dirty', 'SybilNode@d54ece3ca-dirty', 'SybilNode@ee19f0e95-dirty']| False  |
| `159.203.76.161` | US | 237 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `117.174.25.136` | CN | 49 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.135` | CN | 48 | ['go-ipfs/0.8.0/cc95853']| False  |
| `111.9.31.185` | CN | 48 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.181` | CN | 48 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.187` | CN | 48 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.137` | CN | 48 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.208` | CN | 48 | ['go-ipfs/0.8.0/cc95853']| False  |

### Crawls

#### Overall

![Crawl Overview](./plots/crawl-overview.png)

#### Classification

![Crawl Classifications](./plots/crawl-classifications.png)

#### Agents

![Crawl Properties By Agent](./plots/crawl-properties.png)

Only the top 10 kubo versions appear in the right graph (due to lack of colors) based on the average count in the time interval. The `0.8.x` versions **do not** contain disguised storm peers.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

#### Total Peer IDs Discovered Classification

![Peer count by classification](./plots/peer-classifications.png)

In the specified time interval from `2023-02-20` to `2023-02-27` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-02-20` to `2023-02-27` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-02-20` to `2023-02-27` in the DHT and their datacenter association.

### Classification

![Datacenter Distribution By Classification](./plots/cloud-classification.png)

The classifications are documented [here](#peer-classification). Note that the x-axes are different.

### Agents

![Datacenter Distribution By Agent](./plots/cloud-agents.png)

The number in parentheses in the graph titles show the number of unique peer IDs that went into the specific subgraph.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Website Monitoring

We are using [`phantomas`](https://github.com/macbre/phantomas) for the following measurements. The graphs below show the p50, p90, and p99 timings of different metrics and aggregate the performance across the last week.

**Do you want another metric visualized?** Check out [this long list](https://github.com/macbre/phantomas/blob/devel/docs/metrics.md) of options.

### Time To First Byte

The time it took to receive the first byte of the first response (that was not a redirect). The large number in each tile is the time in seconds and the small number in each lower right corner is the percentage change compared to the previous week. The number at the very bottom of the graph shows the sample size that went into each subplot/website. Note: the color scales are different in each graph.

![Time To First Byte](./plots/tiros-ttfb.png)

### DOMContentLoaded

The DOMContentLoaded event fires when the HTML document has been completely parsed, and all deferred scripts (`<script defer src="…">` and `<script type="module">`) have downloaded and executed. The large number in each tile is the time in seconds and the small number in each lower right corner is the percentage change compared to the previous week. The number at the very bottom of the graph shows the sample size that went into each subplot/website. Note: the color scales are different in each graph.

![DOMContentLoaded](./plots/tiros-domcontentloaded.png)

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