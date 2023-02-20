# Nebula Measurement Results Calendar Week 7 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 7 - 2023](#nebula-measurement-results-calendar-week-7---2023)
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
  - [Top Updating Peers](#top-updating-peers)
  - [Website Monitoring](#website-monitoring)
    - [Performance Timing Page Load](#performance-timing-page-load)
    - [Time To First Byte](#time-to-first-byte)
  - [Terminology](#terminology)
    - [Peer Classification](#peer-classification)
    - [Storm Specific Protocols](#storm-specific-protocols)

## General Information

The following results show measurement data that were collected in calendar week 7 in 2023 from `2023-02-13` to `2023-02-20`.

- Number of crawls `310`
- Number of visits `40,114,037`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `87,661`
- Number of unique peer IDs discovered in the DHT `87,229`
- Number of unique IP addresses found `52,800`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.19.0-dev/89826a3/docker` (2023-02-13 09:22:14)
- `delta@4d3746f30-dirty` (2023-02-13 13:54:04)
- `main@950539f12-dirty` (2023-02-13 23:21:58)
- `gitee.com/rocket049/p2pshare` (2023-02-14 06:53:10)
- `go.vocdoni.io/dvote@11aa8b97f-dirty` (2023-02-14 12:21:50)
- `go.vocdoni.io/dvote@d41bdca4b-dirty` (2023-02-14 13:51:12)
- `kubo/0.19.0-dev/e59c605f2-dirty` (2023-02-14 17:23:10)
- `go.vocdoni.io/dvote@7fc4492d8-dirty` (2023-02-14 19:51:13)
- `kubo/0.19.0-dev/0ff406170-dirty` (2023-02-14 22:51:14)
- `delta@bed9fc32d-dirty` (2023-02-15 02:52:31)
- `kubo/0.19.0-dev/ed4d6b7d4-dirty` (2023-02-15 05:53:12)
- `go-ipfs/0.13.0/c9d51bbe0-dirty` (2023-02-15 07:53:11)
- `kubo/0.19.0-dev/ed4d6b7/docker` (2023-02-15 16:51:35)
- `github.com/application-research/estuary@24bc4a7eb-dirty` (2023-02-15 18:21:40)
- `delta@f44c64372-dirty` (2023-02-15 23:22:01)
- `delta@b104bbd7b-dirty` (2023-02-15 23:52:10)
- `github.com/application-research/estuary@8de7e1566-dirty` (2023-02-16 14:21:39)
- `go.vocdoni.io/dvote@992df48a7-dirty` (2023-02-16 20:21:42)
- `delta@aca1a1e1b-dirty` (2023-02-16 21:21:37)
- `github.com/CaduceusMetaverseProtocol/MetaNet@095012690-dirty` (2023-02-17 08:23:10)
- `github.com/mearaj/protonet@` (2023-02-17 17:24:02)
- `kubo/0.19.0-dev/19feb1583` (2023-02-18 03:52:28)
- `kubo/0.15.0-dev/846d36258-dirty` (2023-02-18 05:53:58)
- `kubo/0.19.0-dev/19feb15/docker` (2023-02-18 16:51:34)
- `github.com/libp2p/go-libp2p@` (2023-02-18 16:54:12)
- `peer-to-peer-app-v0.01@f60414d74-dirty` (2023-02-18 16:54:14)
- `kubo/0.19.0-dev/d7dea9caf-dirty` (2023-02-18 22:21:07)
- `delta@45b784bca-dirty` (2023-02-19 05:22:06)
- `delta@8f92d60cf-dirty` (2023-02-19 05:51:40)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `wesign` (2023-02-14 06:53:10)
- `/p2p/rpc/rm` (2023-02-14 07:54:09)
- `customprotocol` (2023-02-14 09:52:05)
- `/sharefile/1.0.0` (2023-02-15 14:23:26)
- `/peerai/compute/1.0.0` (2023-02-16 09:23:04)
- `/nunet/dms/dht/0.0.1` (2023-02-16 11:23:48)
- `/nunet/dms/depreq/0.0.1` (2023-02-16 11:23:48)
- `/nunet/dms/chat/0.0.1` (2023-02-16 11:23:48)
- `/protonet.x/msg-chat/0.0.1` (2023-02-17 17:24:02)
- `/protonet.x/sync/0.0.1` (2023-02-17 17:24:02)
- `/rex/fileshare` (2023-02-18 16:54:14)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `2001:41d0:304:200::41f5` | FR | 3133 | ['kubo/0.17.0/4485d6b71']| True  |
| `141.94.68.144` | FR | 3133 | ['kubo/0.17.0/4485d6b71']| False  |
| `51.210.150.216` | FR | 2712 | ['kubo/0.17.0/4485d6b71']| True  |
| `2001:41d0:304:200::41cd` | FR | 2712 | ['kubo/0.17.0/4485d6b71']| True  |
| `2001:41d0:304:200::41da` | FR | 2655 | ['kubo/0.17.0/4485d6b71']| True  |
| `51.210.151.221` | FR | 2655 | ['kubo/0.17.0/4485d6b71']| True  |
| `193.60.241.98` | GB | 1637 | ['hydra-booster/0.7.4', 'kubo/0.15.0/3ae52a41e', 'main@950539f12-dirty', 'SybilNode@d54ece3ca-dirty', 'SybilNode@ee19f0e95-dirty']| False  |
| `159.203.76.161` | US | 215 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `178.132.7.102` | NL | 46 | ['go-ipfs/0.8.0/48f94e2', 'go-ipfs/0.8.0/ce693d7', 'kubo/0.16.0/38117db/docker', 'kubo/0.17.0/4485d6b/docker', 'rust-libp2p/0.7.0', 'storm']| True  |
| `59.26.142.157` | KR | 34 | ['go-ipfs/0.8.0/48f94e2']| False  |

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

In the specified time interval from `2023-02-13` to `2023-02-20` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-02-13` to `2023-02-20` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-02-13` to `2023-02-20` in the DHT and their datacenter association.

### Classification

![Datacenter Distribution By Classification](./plots/cloud-classification.png)

The classifications are documented [here](#peer-classification). Note that the x-axes are different.

### Agents

![Datacenter Distribution By Agent](./plots/cloud-agents.png)

The number in parentheses in the graph titles show the number of unique peer IDs that went into the specific subgraph.

`storm*` are `go-ipfs/0.8.0/48f94e2` peers that support at least one [storm specific protocol](#storm-specific-protocols).

## Top Updating Peers

An "updating peer" is a peer that we observed with multiple agent versions.  

| Peer ID           | Final Agent Version     | Number of Transitions | Distinct Agent Versions | Number of Distinct AVs |
|:----------------- |:------------ | ------------- |:------------ | -------------- |
| `12D3KooWRfMPo6du...` | `kubo/0.14.0/e0fabd6/docker` | 187  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWNM6h5XD7...` | `kubo/0.14.0/e0fabd6` | 182  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWEoPrMZRs...` | `kubo/0.14.0/e0fabd6/docker` | 176  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWHhpZoae9...` | `kubo/0.14.0/e0fabd6/docker` | 175  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWRT1kXi8B...` | `kubo/0.14.0/e0fabd6` | 174  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWKs4Gz9JC...` | `kubo/0.14.0/e0fabd6` | 173  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWNxYW9zBZ...` | `kubo/0.14.0/e0fabd6` | 169  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWGBGducVn...` | `kubo/0.14.0/e0fabd6` | 168  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWDNeeug7H...` | `kubo/0.14.0/e0fabd6` | 168  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |
| `12D3KooWQn1N1pWz...` | `kubo/0.14.0/e0fabd6` | 167  | kubo/0.14.0/e0fabd6<br/>kubo/0.14.0/e0fabd6/docker | 2 |

## Website Monitoring

We are using [`phantomas`](https://github.com/macbre/phantomas) for the following measurements. The graphs below show the p50, p90, and p99 timings of different metrics and aggregate the performance across the last week.

**Do you want another metric visualized?** Check out [this long list](https://github.com/macbre/phantomas/blob/devel/docs/metrics.md) of options.

### Performance Timing Page Load

![Performance Timing Page Load](./plots/tiros-performance-timing-page-load.png)

The time it took to fully load the page. The large number in each tile is the time in second and the small number in each lower right corner is the number of data points that went into each measurement.

### Time To First Byte

![Time To First Byte](./plots/tiros-ttfb.png)


The time it took to receive the first byte of the first response (that was not a redirect). The large number in each tile is the time in second and the small number in each lower right corner is the number of data points that went into each measurement.

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