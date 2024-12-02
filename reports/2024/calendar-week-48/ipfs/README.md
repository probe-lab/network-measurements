# Nebula Measurement Results Calendar Week 48 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 48 - 2024](#nebula-measurement-results-calendar-week-48---2024)
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

The following results show measurement data that were collected in calendar week 48 in 2024 from `2024-11-25` to `2024-12-02`.

- Number of crawls `144`
- Number of visits `13,680,787`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `47,933`
- Number of unique peer IDs discovered in the DHT `45,930`
- Number of unique IP addresses found `36,414`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20241125005135` (2024-11-25 00:21:39)
- `bootnode-20241125040226` (2024-11-25 04:52:05)
- `bootnode-20241125044039` (2024-11-25 05:20:56)
- `bootnode-20241125062107` (2024-11-25 06:22:28)
- `bootnode-20241125063622` (2024-11-25 06:51:14)
- `bootnode-20241125062604` (2024-11-25 06:51:16)
- `bootnode-20241125065106` (2024-11-25 06:51:33)
- `bootnode-20241125085113` (2024-11-25 08:51:30)
- `bootnode-20241125102110` (2024-11-25 09:21:23)
- `bootnode-20241125030927` (2024-11-25 09:51:25)
- `bootnode-20241125111920` (2024-11-25 10:21:46)
- `bootnode-20241125043005` (2024-11-25 10:51:10)
- `bootnode-20241125122046` (2024-11-25 11:21:06)
- `bootnode-20241125063121` (2024-11-25 12:50:53)
- `bootnode-20241125142458` (2024-11-25 14:51:23)
- `bootnode-20241125081158` (2024-11-25 14:51:58)
- `bootnode-20241125155154` (2024-11-25 15:21:23)
- `bootnode-20241125155620` (2024-11-25 16:21:09)
- `kubo/0.33.0-dev/d1f6541/docker` (2024-11-25 17:51:07)
- `bootnode-20241125114626` (2024-11-25 18:51:08)
- `kubo/0.33.0-dev/0bd0edc78-dirty` (2024-11-25 20:20:53)
- `bootnode-20241125152039` (2024-11-25 21:21:07)
- `bootnode-20241125210122` (2024-11-25 21:21:58)
- `bootnode-20241125223730` (2024-11-25 22:21:17)
- `kubo/0.33.0-dev/ef58568/docker` (2024-11-25 23:51:21)
- `bootnode-20241125172435` (2024-11-25 23:51:30)
- `bootnode-20241126001337` (2024-11-26 00:21:02)
- `bootnode-20241126005408` (2024-11-26 01:22:01)
- `bootnode-20241126013932` (2024-11-26 01:51:06)
- `bootnode-20241126023839` (2024-11-26 01:51:40)
- `bootnode-20241126025039` (2024-11-26 02:50:49)
- `bootnode-20241126033913` (2024-11-26 02:51:26)
- `bootnode-20241126023443` (2024-11-26 03:22:00)
- `bootnode-20241126042054` (2024-11-26 04:21:01)
- `bootnode-20241126045122` (2024-11-26 04:51:42)
- `bootnode-20241126055449` (2024-11-26 05:20:55)
- `bootnode-20241126073612` (2024-11-26 07:51:06)
- `bootnode-20241126022034` (2024-11-26 08:21:10)
- `bootnode-20241126082139` (2024-11-26 08:21:57)
- `bootnode-20241126105040` (2024-11-26 10:50:50)
- `kubo/0.33.0-dev/37c5060/docker` (2024-11-26 11:50:51)
- `bootnode-20241126125044` (2024-11-26 12:51:27)
- `bootnode-20241126141015` (2024-11-26 13:21:54)
- `bootnode-20241126075427` (2024-11-26 14:21:40)
- `bootnode-20241126142110` (2024-11-26 14:21:45)
- `bootnode-20241126143936` (2024-11-26 14:51:05)
- `bootnode-20241126152054` (2024-11-26 15:21:10)
- `bootnode-20241126092104` (2024-11-26 15:21:20)
- `bootnode-20241126092608` (2024-11-26 16:01:25)
- `kubo/0.22.0-dev/b685355/docker` (2024-11-26 18:02:08)
- `kubo/0.32.1/c1154d0-dirty` (2024-11-26 22:01:15)
- `bootnode-20241126230120` (2024-11-26 22:01:42)
- `kubo/0.33.0-dev/23ef1d7/1234567890123456789012345678901234567890` (2024-11-27 00:01:08)
- `bootnode-20241126232635` (2024-11-27 00:01:21)
- `bootnode-20241126234410` (2024-11-27 00:01:29)
- `bootnode-20241127031800` (2024-11-27 10:01:22)
- `bootnode-20241127125631` (2024-11-27 12:01:16)
- `bootnode-20241127150059` (2024-11-27 14:01:59)
- `ca-vsc@164144ade` (2024-11-27 14:02:04)
- `bootnode-20241127154313` (2024-11-27 16:01:20)
- `bootnode-20241127155016` (2024-11-27 16:01:36)
- `bootnode-20241127114955` (2024-11-27 18:01:58)
- `kubo/0.33.0-dev/778a418/docker` (2024-11-28 02:01:26)
- `kubo/0.33.0-dev/778a418/1234567890123456789012345678901234567890` (2024-11-28 02:02:07)
- `bootnode-20241128004920` (2024-11-28 02:02:08)
- `bootnode-20241128060029` (2024-11-28 06:01:05)
- `bootnode-20241128075229` (2024-11-28 08:01:35)
- `bootnode-20241128061510` (2024-11-28 08:02:21)
- `bootnode-20241128023121` (2024-11-28 10:01:21)
- `libp2p/2.3.1 UserAgent=v20.18.1` (2024-11-28 10:01:42)
- `github.com/JackalLabs/sequoia@2add5ce72` (2024-11-28 20:01:26)
- `bootnode-20241129000100` (2024-11-29 00:01:15)
- `dhttestnet@` (2024-11-29 00:02:05)
- `bootnode-20241128194733` (2024-11-29 02:01:47)
- `bootnode-20241128235002` (2024-11-29 06:01:28)
- `kubo/0.24.0/2d4a20e-dirty` (2024-11-29 08:01:17)
- `bootnode-20241129134141` (2024-11-29 14:01:28)
- `p2proxy@646a7f278` (2024-11-29 14:01:28)
- `bootnode-20241129133656` (2024-11-29 14:01:39)
- `kubo/0.32.1/ae80605db` (2024-11-29 22:01:18)
- `kubo/0.33.0-dev/8654538/docker` (2024-11-29 22:01:30)
- `bootnode-20241130030843` (2024-11-30 04:01:12)
- `bootnode-20241130084957` (2024-11-30 08:01:33)
- `otter/0.0.0` (2024-11-30 12:01:11)
- `kubo/0.33.0-dev/8654538cc` (2024-12-01 00:01:59)
- `bootnode-20241201012410` (2024-12-01 02:01:34)
- `helia/5.1.1 libp2p/2.3.1 UserAgent=v22.11.0` (2024-12-01 10:01:32)
- `helia/5.1.1 libp2p/2.3.1 UserAgent=v21.6.2` (2024-12-01 18:01:12)
- `bootnode-20241201171018` (2024-12-01 20:01:27)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/dddns/1.0.0` (2024-11-28 04:01:14)
- `/party01TLP` (2024-11-28 08:01:19)
- `/party11TLP` (2024-11-28 08:01:19)
- `/orbitdb/heads/orbitdb/zdpuAmUzrUZ6nozX7fQpznAmkbEQgwwY7tRoFesZGiMEDVec5` (2024-11-28 10:01:42)
- `/getPK` (2024-11-29 04:01:10)
- `/getEnrollResult` (2024-11-29 04:01:10)
- `/otter/filedrop/0.0.1` (2024-11-30 12:01:11)
- `/viserion/kad/1.0.0` (2024-12-01 12:01:19)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `82.180.162.171` | US | 629 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.22.0/', 'kubo/0.22.0/3f884d3/gala.games', 'kubo/0.28.0-dev/121cfae/docker', 'kubo/0.30.0/846c5cc']| False  |
| `139.59.6.4` | IN | 150 | ['kubo/0.29.0/3f0947b']| True  |
| `51.159.174.206` | FR | 85 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.150.159` | FR | 84 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.247.127` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 77 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 77 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 76 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 76 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-11-25` to `2024-12-02` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-11-25` to `2024-12-02` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-11-25` to `2024-12-02` in the DHT and their datacenter association.

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