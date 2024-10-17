# Nebula Measurement Results Calendar Week 39 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 39 - 2024](#nebula-measurement-results-calendar-week-39---2024)
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

The following results show measurement data that were collected in calendar week 39 in 2024 from `2024-09-23` to `2024-09-30`.

- Number of crawls `335`
- Number of visits `24,016,361`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `55,042`
- Number of unique peer IDs discovered in the DHT `54,748`
- Number of unique IP addresses found `63,858`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20240923021359` (2024-09-23 02:21:10)
- `bootnode-20240922221657` (2024-09-23 04:50:57)
- `bootnode-20240923041608` (2024-09-23 04:51:12)
- `bootnode-20240923050333` (2024-09-23 06:21:16)
- `bootnode-20240923014733` (2024-09-23 06:51:10)
- `bootnode-20240923065702` (2024-09-23 08:21:00)
- `bootnode-20240923085833` (2024-09-23 09:51:31)
- `bootnode-20240923104424` (2024-09-23 10:51:10)
- `helia/2.0.3 js-libp2p/0.46.16 UserAgent=v18.20.4` (2024-09-23 11:21:06)
- `bootnode-20240923154835` (2024-09-23 15:51:26)
- `bootnode-20240923112707` (2024-09-23 17:21:20)
- `bootnode-20240923141002` (2024-09-23 19:21:38)
- `bootnode-20240923201949` (2024-09-23 20:51:05)
- `bootnode-20240924002633` (2024-09-23 23:21:07)
- `bootnode-20240923184854` (2024-09-23 23:51:34)
- `bootnode-20240924014323` (2024-09-24 01:51:35)
- `bootnode-20240924033755` (2024-09-24 02:21:04)
- `bootnode-20240924042818` (2024-09-24 02:50:48)
- `bootnode-20240924053852` (2024-09-24 04:20:56)
- `bootnode-20240924080912` (2024-09-24 06:20:55)
- `bootnode-20240924020816` (2024-09-24 07:21:24)
- `bootnode-20240924031049` (2024-09-24 08:51:09)
- `bootnode-20240924044327` (2024-09-24 09:50:52)
- `bootnode-20240924113624` (2024-09-24 11:51:02)
- `bootnode-20240924122954` (2024-09-24 13:21:32)
- `bootnode-20240924145926` (2024-09-24 15:20:55)
- `kubo/0.31.0-dev/58434ec/docker` (2024-09-24 17:21:02)
- `bootnode-20240924171735` (2024-09-24 17:50:54)
- `bootnode-20240924162943` (2024-09-24 18:21:06)
- `bootnode-20240924180859` (2024-09-24 18:21:24)
- `bootnode-20240924191026` (2024-09-24 18:51:06)
- `bootnode-20240924182912` (2024-09-24 18:51:24)
- `p2proxy@90fb20e35` (2024-09-24 19:21:08)
- `bootnode-20240924204958` (2024-09-24 20:50:50)
- `bootnode-20240924205019` (2024-09-24 20:50:53)
- `bootnode-20240924163044` (2024-09-24 21:51:08)
- `kubo/0.31.0-dev/ce23fc7/docker` (2024-09-24 21:51:35)
- `bootnode-20240924221445` (2024-09-24 22:20:46)
- `bootnode-20240925002047` (2024-09-25 00:21:44)
- `bootnode-20240925005052` (2024-09-25 00:51:23)
- `bootnode-20240925012735` (2024-09-25 02:21:08)
- `bootnode-20240925014116` (2024-09-25 02:21:24)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v22.6.0` (2024-09-25 04:21:03)
- `bootnode-20240925052903` (2024-09-25 06:21:22)
- `kubo/0.31.0-dev/ce23fc7cc` (2024-09-25 06:50:48)
- `bootnode-20240925072041` (2024-09-25 07:21:14)
- `bootnode-20240925032022` (2024-09-25 08:21:14)
- `bootnode-20240925094426` (2024-09-25 10:50:58)
- `bootnode-20240925154655` (2024-09-25 16:51:06)
- `someguy/v0.4.2 2024-08-21-02b8190` (2024-09-25 18:22:24)
- `kubo/0.30.0/846c5cc-dirty` (2024-09-25 20:21:24)
- `bootnode-20240926004528` (2024-09-25 22:50:47)
- `bootnode-20240926020551` (2024-09-26 00:51:00)
- `bootnode-20240926032637` (2024-09-26 02:21:11)
- `bootnode-20240926025054` (2024-09-26 02:51:03)
- `bootnode-20240926023423` (2024-09-26 03:21:21)
- `bootnode-20240926031645` (2024-09-26 03:51:23)
- `bootnode-20240926045702` (2024-09-26 05:21:01)
- `bootnode-20240926080726` (2024-09-26 06:20:57)
- `bootnode-20240926080144` (2024-09-26 08:20:54)
- `bootnode-20240926034755` (2024-09-26 08:50:54)
- `bootnode-20240926075515` (2024-09-26 09:21:44)
- `bootnode-20240926074234` (2024-09-26 09:51:14)
- `js-libp2p/0.45.9 UserAgent=v22.9.0` (2024-09-26 10:50:49)
- `bootnode-20240926070053` (2024-09-26 12:20:53)
- `rumo/dev-none` (2024-09-26 15:20:55)
- `bootnode-20240926102131` (2024-09-26 16:51:02)
- `bootnode-20240926174343` (2024-09-26 17:51:07)
- `kubo/0.31.0-dev/836d516/docker` (2024-09-26 17:51:11)
- `bootnode-20240926193827` (2024-09-26 21:21:29)
- `bootnode-20240926155610` (2024-09-26 21:50:59)
- `bootnode-20240926194956` (2024-09-27 00:51:13)
- `bootnode-20240927024917` (2024-09-27 01:21:00)
- `bootnode-20240927012549` (2024-09-27 01:51:29)
- `bootnode-20240927035944` (2024-09-27 02:21:08)
- `bootnode-20240927062513` (2024-09-27 07:21:08)
- `bootnode-20240927064850` (2024-09-27 07:21:08)
- `bootnode-20240927092012` (2024-09-27 07:21:11)
- `github.com/harmony-one/harmony@feb518058` (2024-09-27 09:20:57)
- `bootnode-20240927063804` (2024-09-27 09:51:26)
- `kubo/0.26.0/dfec50d-dirty/docker` (2024-09-27 13:21:20)
- `github.com/ourzora/zora-ipfs@9f8aecc90-dirty` (2024-09-27 13:51:00)
- `bootnode-20240927084943` (2024-09-27 13:51:07)
- `bootnode-20240927135041` (2024-09-27 13:51:23)
- `bootnode-20240927090713` (2024-09-27 14:20:51)
- `bootnode-20240927154053` (2024-09-27 14:21:13)
- `kubo/0.31.0-dev/ca4f486/docker` (2024-09-27 14:21:23)
- `bootnode-20240927142914` (2024-09-27 14:51:17)
- `bootnode-20240927095831` (2024-09-27 15:21:25)
- `bootnode-20240927112016` (2024-09-27 16:20:49)
- `bootnode-20240927115107` (2024-09-27 16:51:23)
- `bootnode-20240927120506` (2024-09-27 17:21:00)
- `bootnode-20240927155023` (2024-09-27 17:51:20)
- `bootnode-20240927162107` (2024-09-27 21:21:16)
- `bootnode-20240927220114` (2024-09-27 22:51:17)
- `bootnode-20240927154724` (2024-09-27 22:51:26)
- `bootnode-20240928031239` (2024-09-28 01:21:04)
- `bootnode-20240928013543` (2024-09-28 04:21:19)
- `bootnode-20240928083446` (2024-09-28 06:51:10)
- `bootnode-20240928060311` (2024-09-28 07:50:56)
- `kubo/0.31.0-dev/836d51650-dirty` (2024-09-28 07:51:17)
- `bootnode-20240928080351` (2024-09-28 08:21:02)
- `bootnode-20240928040128` (2024-09-28 09:21:06)
- `bootnode-20240928122429` (2024-09-28 13:20:51)
- `kubo/0.17.0-dev/052d797` (2024-09-28 16:51:23)
- `bootnode-20240928155928` (2024-09-28 17:51:23)
- `bootnode-20240928222939` (2024-09-28 20:50:51)
- `bootnode-20240928203111` (2024-09-28 22:20:55)
- `bootnode-20240928235019` (2024-09-28 23:51:00)
- `bootnode-20240929015038` (2024-09-29 01:50:59)
- `bootnode-20240929015257` (2024-09-29 03:21:21)
- `bootnode-20240928222808` (2024-09-29 04:20:59)
- `kubo/0.31.0-dev/a178307/docker` (2024-09-29 04:21:25)
- `bootnode-20240928235853` (2024-09-29 06:20:55)
- `bootnode-20240929015012` (2024-09-29 06:50:50)
- `bootnode-20240929065105` (2024-09-29 07:21:10)
- `bootnode-20240929030318` (2024-09-29 08:21:07)
- `bootnode-20240929080241` (2024-09-29 08:50:57)
- `bootnode-20240929083234` (2024-09-29 08:51:02)
- `p2proxy@680eb132a-dirty` (2024-09-29 11:51:10)
- `bootnode-20240929123141` (2024-09-29 12:20:54)
- `bootnode-20240929135053` (2024-09-29 13:50:57)
- `bootnode-20240929085055` (2024-09-29 13:51:01)
- `bootnode-20240929135145` (2024-09-29 14:21:02)
- `p2proxy@63f364f0d-dirty` (2024-09-29 14:21:22)
- `bootnode-20240929135431` (2024-09-29 14:51:12)
- `bootnode-20240929155247` (2024-09-29 15:51:02)
- `bootnode-20240929155443` (2024-09-29 16:21:03)
- `bootnode-20240929215311` (2024-09-29 20:21:18)
- `bootnode-20240929215043` (2024-09-29 21:50:52)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/ssh` (2024-09-24 19:21:08)
- `/web/stream` (2024-09-24 19:21:08)
- `/web/graphql` (2024-09-24 19:21:08)
- `/web/static` (2024-09-24 19:21:08)
- `/web/http` (2024-09-24 19:21:08)
- `/rumo/auth/0.1.0` (2024-09-26 15:20:55)
- `/hypermedia/0.4.1` (2024-09-28 09:51:27)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `51.159.150.159` | FR | 86 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.247.127` | FR | 84 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 76 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 74 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 74 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 73 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 73 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `68.183.11.180` | NL | 50 | ['edgevpn']| True  |
| `51.15.216.149` | FR | 44 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-09-23` to `2024-09-30` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-09-23` to `2024-09-30` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-09-23` to `2024-09-30` in the DHT and their datacenter association.

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