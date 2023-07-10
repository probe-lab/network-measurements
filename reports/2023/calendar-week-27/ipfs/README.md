# Nebula Measurement Results Calendar Week 27 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 27 - 2023](#nebula-measurement-results-calendar-week-27---2023)
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

The following results show measurement data that were collected in calendar week 27 in 2023 from `2023-07-03` to `2023-07-10`.

- Number of crawls `336`
- Number of visits `54,722,369`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `51,628`
- Number of unique peer IDs discovered in the DHT `51,522`
- Number of unique IP addresses found `61,761`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `main@9672f6598-dirty` (2023-07-03 07:22:25)
- `kubo/0.21.0/294db3e/docker` (2023-07-03 07:52:04)
- `kubo/0.22.0-dev/f797e9e6d` (2023-07-03 08:52:46)
- `kubo/0.22.0-dev/f797e9e6d-dirty` (2023-07-03 09:52:23)
- `kubo/0.21.0/` (2023-07-03 13:22:21)
- `0.13.1` (2023-07-03 13:52:03)
- `github.com/ethtweet/ethtweet@85153641a-dirty` (2023-07-03 14:51:58)
- `kubo/0.21.0/294db3e/s̳̪̦̩̝͎͙͝u͍̫̺̝̱̰͝p̠͔̫͓̬̦` (2023-07-03 17:52:04)
- `kubo/0.21.0/294db3e30` (2023-07-03 18:51:33)
- `go-ipfs/0.9.1/1a33f9c17b` (2023-07-04 01:51:55)
- `kubo/0.21.0/294db3e` (2023-07-04 02:21:56)
- `SybilNode@ecd479240-dirty` (2023-07-04 06:22:50)
- `github.com/ethtweet/ethtweet@524560d64-dirty` (2023-07-04 06:52:07)
- `kubo/0.18.0/fc2e11e` (2023-07-04 14:52:32)
- `kubo/0.21.0/desktop` (2023-07-04 19:21:23)
- `kubo/0.18.0/629337d` (2023-07-05 01:52:16)
- `main@629337dd8-dirty` (2023-07-05 02:22:22)
- `kubo/0.18.0/093a0b7` (2023-07-05 09:22:08)
- `main@093a0b758` (2023-07-05 10:22:06)
- `main@fcebb2ef8-dirty` (2023-07-05 16:52:00)
- `kubo/0.18.0/598d07d` (2023-07-05 18:21:50)
- `main@598d07de4` (2023-07-05 18:22:17)
- `SybilNode@fcebb2ef8-dirty` (2023-07-05 19:21:40)
- `main@37ae15b78-dirty` (2023-07-06 00:22:20)
- `kubo/0.18.0/37ae15b` (2023-07-06 00:22:35)
- `main@64e9584d9-dirty` (2023-07-06 07:21:07)
- `main@b01e5e1b4-dirty` (2023-07-06 10:22:48)
- `github.com/ethtweet/ethtweet@117bdfa24-dirty` (2023-07-06 10:52:21)
- `app-ecos@8b5e86f12-dirty` (2023-07-06 15:22:57)
- `kubo/0.22.0-dev/895963b95-dirty/docker` (2023-07-06 17:51:31)
- `main@a0023a31c-dirty` (2023-07-07 00:21:07)
- `kubo/0.21.0/294db3e30-dirty` (2023-07-07 12:22:22)
- `kubo/0.21.0/docker` (2023-07-08 12:21:48)
- `rust-libp2p-server/0.10.0` (2023-07-08 13:52:53)
- `github.com/akakream/sailorsailor@a54b1ebc2-dirty` (2023-07-08 15:52:46)
- `github.com/akakream/sailorsailor@d3c9e73b6-dirty` (2023-07-08 16:52:58)
- `github.com/akakream/sailorsailor@ed86d685e` (2023-07-08 17:52:49)
- `kubo/0.22.0-dev/4a5e99d7e` (2023-07-08 19:21:29)
- `github.com/ethtweet/ethtweet@ded10d7c0-dirty` (2023-07-08 23:22:36)
- `github.com/ethtweet/ethtweet@dacc64713-dirty` (2023-07-09 08:52:02)
- `kubo/0.22.0-dev/4a5e99d7e-dirty` (2023-07-09 11:21:43)
- `github.com/ethtweet/ethtweet@07f3d1f89-dirty` (2023-07-09 11:52:22)
- `app-ecos@a00fcdd5a-dirty` (2023-07-09 15:53:00)
- `github.com/ethtweet/ethtweet@9409931da-dirty` (2023-07-09 17:23:01)
- `github.com/ethtweet/ethtweet@8d65a0d99-dirty` (2023-07-09 20:52:17)
- `kubo/0.22.0-dev/4a5e99d/docker` (2023-07-09 23:52:27)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/bpfs/versionRequestProtocol/1.0.0` (2023-07-04 01:21:59)
- `/bpfs/versionResponseProtocol/1.0.0` (2023-07-04 03:22:43)
- `/bpfs/offlineProtocol/1.0.0` (2023-07-04 06:22:31)
- `/bpfs/checkVersionProtocol/1.0.0` (2023-07-04 06:22:31)
- `/the-man/1.0.0` (2023-07-04 23:21:46)
- `ecos/v1/radar/user` (2023-07-06 15:22:57)
- `ecos/v1/radar/myapps` (2023-07-06 16:22:34)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `52.88.221.48` | US | 422 | ['kubo/0.18.0/37ae15b', 'main@37ae15b78-dirty', 'main@a0023a31c-dirty', 'main@b01e5e1b4-dirty', 'SybilNode@']| True  |
| `193.60.241.98` | GB | 356 | ['kubo/0.18.0/fc2e11e', 'main@', 'main@fcebb2ef8-dirty', 'SybilNode@', 'SybilNode@fcebb2ef8-dirty']| False  |
| `54.149.215.250` | US | 327 | ['kubo/0.18.0/598d07d', 'kubo/0.18.0/629337d', 'main@598d07de4', 'main@629337dd8-dirty', 'main@64e9584d9-dirty', 'SybilNode@']| True  |
| `35.86.242.254` | US | 270 | ['kubo/0.18.0/093a0b7', 'main@093a0b758', 'SybilNode@']| True  |
| `159.203.76.161` | US | 194 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `35.199.42.20` | US | 88 | ['Taubyte Node v1.0']| True  |
| `54.187.21.48` | US | 47 | ['kubo/0.17.0/4485d6b71', 'main@9672f6598-dirty', 'SybilNode@ef7cf7ce7-dirty']| True  |
| `91.53.106.77` | DE | 38 | ['go-ipfs/0.6.0/']| False  |
| `172.33.1.5` | US | 32 | ['kubo/0.15.0/3ae52a4', 'kubo/0.17.0/4485d6b', 'kubo/0.19.2/afb27ca/docker']| False  |
| `91.53.96.245` | DE | 30 | ['go-ipfs/0.6.0/']| False  |

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

In the specified time interval from `2023-07-03` to `2023-07-10` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-07-03` to `2023-07-10` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-07-03` to `2023-07-10` in the DHT and their datacenter association.

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