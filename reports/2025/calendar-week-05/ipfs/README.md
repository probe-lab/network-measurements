# Nebula Measurement Results Calendar Week 5 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 5 - 2025](#nebula-measurement-results-calendar-week-5---2025)
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

The following results show measurement data that were collected in calendar week 5 in 2025 from `2025-02-03` to `2025-02-10`.

- Number of crawls `84`
- Number of visits `10,227,187`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `52,498`
- Number of unique peer IDs discovered in the DHT `51,982`
- Number of unique IP addresses found `57,817`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `ca-vsc@9d407eb16` (2025-02-03 14:01:31)
- `bootnode-20250203093454` (2025-02-03 16:01:13)
- `bootnode-20250203160110` (2025-02-03 16:02:03)
- `bootnode-20250203163215` (2025-02-03 16:02:17)
- `bootnode-20250203163005` (2025-02-03 18:01:15)
- `bootnode-20250203160321` (2025-02-03 18:01:25)
- `bootnode-20250203161900` (2025-02-03 18:01:55)
- `github.com/JackalLabs/sequoia@0b06ba6b2` (2025-02-04 02:01:38)
- `kubo/0.34.0-dev/4bd79bd/docker` (2025-02-04 10:02:06)
- `kubo/0.34.0-dev/16a77e56a` (2025-02-04 18:01:04)
- `kubo/0.33.0/docker` (2025-02-04 18:01:04)
- `kubo/0.33.1/9bfbc4e` (2025-02-04 20:01:03)
- `kubo/0.33.1/9bfbc4e/1234567890123456789012345678901234567890` (2025-02-04 20:01:29)
- `kubo/0.33.1/9bfbc4e/docker` (2025-02-04 20:01:45)
- `kubo/0.33.1/90f0bbb` (2025-02-04 20:02:16)
- `kubo/0.33.1/9bfbc4e/bootstrap.libp2p.io` (2025-02-05 00:01:03)
- `kubo/0.34.0-dev/580ce69/docker` (2025-02-05 00:01:28)
- `kubo/0.33.1/` (2025-02-05 02:01:27)
- `github.com/harmony-one/harmony@72e90f75a` (2025-02-05 08:01:41)
- `ca-vsc@c7bf1e378` (2025-02-05 12:01:16)
- `ca-vsc@63ef502aa` (2025-02-05 12:02:18)
- `github.com/harmony-one/harmony@76607e5f7` (2025-02-05 14:01:19)
- `kubo/0.33.1/6d2c005-dirty` (2025-02-05 16:01:30)
- `bootnode-20250205083357` (2025-02-05 16:01:39)
- `kubo/0.33.1/Homebrew` (2025-02-05 16:02:12)
- `kubo/0.33.1/desktop` (2025-02-05 18:01:47)
- `bootnode-20250205153357` (2025-02-05 18:02:14)
- `bootnode-20250205181550` (2025-02-05 20:01:58)
- `github.com/tempmobynet/mobyrelayservices-go@` (2025-02-05 20:02:50)
- `kubo/0.34.0-dev/ad81ead/docker` (2025-02-06 00:02:09)
- `kubo/0.34.0-dev/68c0879a4` (2025-02-06 02:01:20)
- `kubo/0.34.0-dev/68c0879/docker` (2025-02-06 08:02:07)
- `bootnode-20250206083640` (2025-02-06 10:01:24)
- `kubo/0.34.0-dev/580ce695e-dirty` (2025-02-06 22:02:09)
- `kubo/0.34.0-dev/68c0879a4-dirty` (2025-02-06 22:02:17)
- `kubo/0.34.0-dev/b387530/docker` (2025-02-06 22:02:24)
- `kubo/0.33.1/9bfbc4e/collab.ipfscluster.io` (2025-02-07 00:01:16)
- `bootnode-20250207000105` (2025-02-07 00:01:25)
- `kubo/0.33.1/9bfbc4e52/desktop` (2025-02-07 08:01:22)
- `bootnode-20250207175903` (2025-02-07 18:02:07)
- `kubo/0.34.0-dev/b387530d0` (2025-02-07 22:01:11)
- `bootnode-20250208000054` (2025-02-08 00:01:04)
- `bootnode-20250208060056` (2025-02-08 06:01:54)
- `kubo/0.33.1/9bfbc4e52` (2025-02-08 20:01:03)
- `bootnode-20250209120136` (2025-02-09 14:01:30)
- `bootnode-20250209180147` (2025-02-09 20:02:07)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/address-exchange/1.0.1` (2025-02-05 14:01:47)
- `/moby/register-agent/1.0.0` (2025-02-05 20:02:50)
- `/relay/1.0.0` (2025-02-05 20:02:50)
- `/moby/discover/1.0.0` (2025-02-06 22:02:15)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `2001:41d0:8:926e::1` | FR | 84 | ['edgevpn']| True  |
| `5.39.80.110` | FR | 84 | ['edgevpn']| True  |
| `152.81.47.227` | FR | 71 | ['kubo/0.32.0/']| False  |
| `180.175.224.135` | CN | 63 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `172.233.243.82` | FR | 53 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 53 | ['edgevpn']| True  |
| `1.159.159.63` | AU | 50 | ['kubo/0.32.1/']| False  |
| `26.26.26.1` | US | 39 | ['go-ipfs/0.8.0/48f94e2', 'kubo/0.28.0/']| False  |
| `91.230.153.86` | RU | 36 | ['edgevpn']| False  |
| `80.106.161.133` | GR | 31 | ['kubo/0.32.1/']| False  |

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

In the specified time interval from `2025-02-03` to `2025-02-10` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-02-03` to `2025-02-10` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-02-03` to `2025-02-10` in the DHT and their datacenter association.

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