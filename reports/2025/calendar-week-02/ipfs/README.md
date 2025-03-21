# Nebula Measurement Results Calendar Week 2 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 2 - 2025](#nebula-measurement-results-calendar-week-2---2025)
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

The following results show measurement data that were collected in calendar week 2 in 2025 from `2025-01-13` to `2025-01-20`.

- Number of crawls `84`
- Number of visits `10,127,725`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `53,828`
- Number of unique peer IDs discovered in the DHT `53,190`
- Number of unique IP addresses found `56,633`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/harmony-one/harmony@9dba11df4` (2025-01-13 12:01:09)
- `MessageMesh` (2025-01-13 14:01:50)
- `bootnode-20250113090940` (2025-01-13 16:01:13)
- `bootnode-20250113161200` (2025-01-13 18:01:33)
- `kubo/0.33.0-rc1/1b5aa0bfa-dirty` (2025-01-13 18:03:17)
- `kubo/0.34.0-dev/3b098b9/1234567890123456789012345678901234567890` (2025-01-13 20:02:07)
- `bootnode-20250113161539` (2025-01-14 00:01:08)
- `feishup2pclient@147ac74b5-dirty` (2025-01-14 04:01:07)
- `bootnode-20250114034033` (2025-01-14 04:01:33)
- `kubo/0.34.0-dev/3b098b969-dirty` (2025-01-14 10:02:09)
- `dvpncmd@5b4f7a6ac-dirty` (2025-01-14 12:01:17)
- `feishup2pclient@9d06c1071-dirty` (2025-01-14 18:01:46)
- `ppp@` (2025-01-15 12:01:11)
- `kubo/0.34.0-dev/1768204/docker` (2025-01-15 14:01:25)
- `jackalnft@` (2025-01-16 04:01:57)
- `github.com/element-hq/dendrite@19f0cfb12` (2025-01-16 06:01:47)
- `js-libp2p/2.5.0 UserAgent=v20.18.1` (2025-01-16 08:01:38)
- `kubo/0.34.0-dev/f41b190e1-dirty` (2025-01-16 08:02:20)
- `dvpncmd@5b4f7a6ac-hayek` (2025-01-16 16:01:12)
- `js-libp2p/2.5.0 UserAgent=v22.1.0` (2025-01-16 16:01:20)
- `github.com/element-hq/dendrite@19f0cfb12-dirty` (2025-01-16 16:01:27)
- `feishup2pclient@c6ca155f0-dirty` (2025-01-16 18:01:55)
- `kubo/0.32.1/9c611b3c7-dirty` (2025-01-16 18:03:19)
- `kubo/0.34.0-dev/f41b190/docker` (2025-01-17 00:01:27)
- `dvpncmd@12e527325-hayek` (2025-01-17 10:01:17)
- `github.com/containers/gvisor-tap-vsock@aed59c011-dirty` (2025-01-17 14:01:34)
- `feishup2pclient@614747781-dirty` (2025-01-17 14:01:51)
- `github.com/containers/gvisor-tap-vsock@e3ddf6b53-dirty` (2025-01-18 00:01:09)
- `bootnode-20250118015206` (2025-01-18 02:01:14)
- `github.com/containers/gvisor-tap-vsock@8555b6d56-dirty` (2025-01-18 14:01:17)
- `go-ipfs/0.13.0-dev/25cc85fa9-dirty` (2025-01-18 14:02:13)
- `kubo/0.33.0-dev/124216309` (2025-01-18 18:01:56)
- `bootnode-20250118193254` (2025-01-18 20:01:52)
- `github.com/containers/gvisor-tap-vsock@3b1ef657d-dirty` (2025-01-19 06:01:11)
- `github.com/containers/gvisor-tap-vsock@42c6a2c45-dirty` (2025-01-19 08:01:23)
- `huh/0.0.0` (2025-01-19 20:02:09)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/tari_meta_data_info/5` (2025-01-13 14:01:35)
- `/getBesuEnrollResult` (2025-01-16 06:01:03)
- `/postTxHash` (2025-01-16 06:01:03)
- `/getEthAddress` (2025-01-16 06:01:03)
- `/orbitdb/heads/orbitdb/zdpuAueMFz2WSAUn9ApfScHtmyAgZnT1rB4xp1Pp2bAJzVxVn` (2025-01-16 08:01:38)
- `/orbitdb/heads/orbitdb/zdpuAz1das19QvUWSrRetzzp2GABwFsqi5PdRV9jJY9vjhtPK` (2025-01-18 10:01:16)
- `/gvisor/libp2p-tap/1.0.0` (2025-01-18 14:01:17)
- `/gvisor/libp2p-tap-udp/1.0.0` (2025-01-19 08:01:23)
- `/gvisor/libp2p-tap-tcp/1.0.0` (2025-01-19 08:01:23)
- `/orbitdb/heads/orbitdb/zdpuAmtWE7ACueDWBAA7gmHT6Jg372i5yfHdWnkYsY3S9YMHC` (2025-01-19 16:01:26)
- `/orbitdb/heads/orbitdb/zdpuAxByd1M9wZWCJRp7uwBLyL1uCeSzGkQX2pGkrsKqVGdSt` (2025-01-19 16:01:38)
- `/orbitdb/heads/orbitdb/zdpuB2nh985yx3SepF2Ny6DJ7TSkAZDmbj9JggToy2FQYz5Cu` (2025-01-19 20:01:29)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `5.39.80.110` | FR | 84 | ['edgevpn']| True  |
| `2001:41d0:8:926e::1` | FR | 84 | ['edgevpn']| True  |
| `152.81.47.227` | FR | 71 | ['kubo/0.32.0/', 'kubo/0.34.0-dev/']| False  |
| `26.26.26.1` | US | 50 | ['gobind@', 'go-ipfs/0.8.0/48f94e2', 'kubo/0.28.0/']| False  |
| `172.233.243.82` | FR | 47 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 47 | ['edgevpn']| True  |
| `91.230.153.86` | RU | 35 | ['edgevpn']| False  |
| `143.110.168.61` | GB | 32 | ['kubo/0.29.0/3f0947b', 'kubo/0.30.0/']| True  |
| `142.93.215.219` | IN | 30 | ['kubo/0.29.0/3f0947b']| True  |
| `111.226.19.108` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |

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

In the specified time interval from `2025-01-13` to `2025-01-20` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-01-13` to `2025-01-20` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-01-13` to `2025-01-20` in the DHT and their datacenter association.

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