# Nebula Measurement Results Calendar Week 17 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 17 - 2024](#nebula-measurement-results-calendar-week-17---2024)
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

The following results show measurement data that were collected in calendar week 17 in 2024 from `2024-04-22` to `2024-04-29`.

- Number of crawls `336`
- Number of visits `28,985,221`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `49,629`
- Number of unique peer IDs discovered in the DHT `48,775`
- Number of unique IP addresses found `71,203`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `helia/4.1.0 libp2p/1.4.2 UserAgent=v20.11.1` (2024-04-22 09:37:27)
- `kubo/0.29.0-dev/eb97cf9e-dirty` (2024-04-22 13:51:30)
- `helia/4.1.1 libp2p/1.4.2 UserAgent=v20.9.0` (2024-04-22 21:50:59)
- `github.com/IceFireDB/icefiredb-crdt-kv@46163f77a` (2024-04-23 10:21:00)
- `helia/4.1.2 libp2p/1.4.2 UserAgent=v20.11.1` (2024-04-23 15:21:01)
- `helia/4.1.2 libp2p/1.4.2 UserAgent=v18.18.2` (2024-04-24 11:20:47)
- `helia/4.1.2 libp2p/1.4.2 UserAgent=v18.19.1` (2024-04-24 16:21:07)
- `helia/4.1.2 libp2p/1.4.3 UserAgent=v20.11.0` (2024-04-25 03:51:24)
- `kubo/0.29.0-dev/docker` (2024-04-25 03:51:27)
- `github.com/libp2p/universal-connectivity/go-peer@5a7f5421c` (2024-04-25 12:21:08)
- `js-libp2p/0.45.9 UserAgent=v20.12.2` (2024-04-25 14:51:17)
- `helia/4.1.2 libp2p/1.4.3 UserAgent=v20.11.1` (2024-04-25 15:21:00)
- `github.com/libp2p/universal-connectivity/go-peer@7c9082074` (2024-04-26 09:51:03)
- `github.com/harmony-one/harmony@8717ccf61` (2024-04-28 17:50:45)
- `github.com/harmony-one/harmony@ae578ba99` (2024-04-28 17:50:47)
- `github.com/harmony-one/harmony@3e7ff3839` (2024-04-28 17:50:47)
- `github.com/harmony-one/harmony@` (2024-04-28 17:50:47)
- `github.com/harmony-one/harmony@49bba1785` (2024-04-28 17:50:50)
- `github.com/harmony-one/harmony@99b3ea85c` (2024-04-28 17:50:50)
- `github.com/harmony-one/harmony@40a2374d4` (2024-04-28 17:50:51)
- `github.com/harmony-one/harmony@d5956cee9` (2024-04-28 17:50:53)
- `github.com/harmony-one/harmony@f4de23f96` (2024-04-28 17:50:56)
- `github.com/harmony-one/harmony` (2024-04-28 17:50:59)
- `github.com/harmony-one/harmony@b3aebb62d` (2024-04-28 17:51:08)
- `github.com/harmony-one/harmony@a4ce4b134` (2024-04-28 17:51:16)
- `github.com/redline-finance/go-harmony-p2p-client@9d32bd476-dirty` (2024-04-28 17:51:29)
- `github.com/harmony-one/harmony@1b9614ba2` (2024-04-28 17:51:32)
- `github.com/harmony-one/harmony@782eb4f75` (2024-04-28 18:20:59)
- `github.com/harmony-one/harmony@948730eed` (2024-04-28 18:21:15)
- `github.com/harmony-one/harmony@3e66b85b3` (2024-04-28 18:21:24)
- `github.com/harmony-one/harmony@47949a1ef` (2024-04-28 19:20:52)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `llama_state_averager::TrainingStateAverager.rpc_join_group` (2024-04-23 09:51:18)
- `llama_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-04-23 09:51:18)
- `llama_state_averager::TrainingStateAverager.rpc_download_state` (2024-04-23 09:51:18)
- `v0_0_1_r3_grad_averager::DTGradientAverager.rpc_join_group` (2024-04-24 12:20:50)
- `v0_0_1_r3_grad_averager::DTGradientAverager.rpc_download_state` (2024-04-24 12:20:50)
- `v0_0_1_r3_state_averager::DTStateAverager.rpc_aggregate_part` (2024-04-24 12:20:50)
- `v0_0_1_r3_grad_averager::DTGradientAverager.rpc_aggregate_part` (2024-04-24 12:20:50)
- `v0_0_1_r3_state_averager::DTStateAverager.rpc_download_state` (2024-04-24 12:20:50)
- `v0_0_1_r3_state_averager::DTStateAverager.rpc_join_group` (2024-04-24 12:20:50)
- `v0_0_1_r3::DTGradientAverager.rpc_download_state` (2024-04-24 13:21:13)
- `v0_0_1_r3::DTStateAverager.rpc_join_group` (2024-04-24 13:21:13)
- `v0_0_1_r3::DTStateAverager.rpc_download_state` (2024-04-24 13:21:13)
- `v0_0_1_r3::DTGradientAverager.rpc_aggregate_part` (2024-04-24 13:21:13)
- `v0_0_1_r3::DTGradientAverager.rpc_join_group` (2024-04-24 13:21:13)
- `v0_0_1_r3::DTStateAverager.rpc_aggregate_part` (2024-04-24 13:21:13)
- `bpfs@stream/file/shared/1.1.0` (2024-04-26 10:51:25)
- `/NetHive/vpn` (2024-04-28 03:21:03)
- `harmony/sync/mainnet/0/1.0.0/1` (2024-04-28 17:51:08)
- `harmony/sync/partner/0/1.0.0/1` (2024-04-28 18:20:59)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 189 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `188.165.71.178` | FR | 165 | ['hydra-booster/0.7.4', 'kubo/0.27.0/']| True  |
| `51.15.230.142` | FR | 123 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.230.142` | FR | 120 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `188.165.71.178` | FR | 105 | ['kubo/0.27.0/']| True  |
| `51.15.245.0` | FR | 100 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.245.0` | FR | 99 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.201.219` | FR | 82 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | NL | 82 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-04-22` to `2024-04-29` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-04-22` to `2024-04-29` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-04-22` to `2024-04-29` in the DHT and their datacenter association.

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