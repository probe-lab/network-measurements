# Nebula Measurement Results Calendar Week 37 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 37 - 2024](#nebula-measurement-results-calendar-week-37---2024)
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

The following results show measurement data that were collected in calendar week 37 in 2024 from `2024-09-09` to `2024-09-16`.

- Number of crawls `336`
- Number of visits `23,813,233`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `63,919`
- Number of unique peer IDs discovered in the DHT `63,683`
- Number of unique IP addresses found `112,689`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20240908195038` (2024-09-09 00:51:05)
- `bootnode-20240909020255` (2024-09-09 02:21:33)
- `bootnode-20240909023254` (2024-09-09 02:51:36)
- `bootnode-20240909042047` (2024-09-09 04:20:57)
- `bootnode-20240909074239` (2024-09-09 08:21:01)
- `bootnode-20240909045054` (2024-09-09 09:51:18)
- `bootnode-20240909104547` (2024-09-09 10:50:54)
- `bootnode-20240909075048` (2024-09-09 12:51:09)
- `bootnode-20240909080200` (2024-09-09 13:21:05)
- `bootnode-20240909133924` (2024-09-09 13:50:50)
- `bootnode-20240909095104` (2024-09-09 14:51:40)
- `bootnode-20240909170610` (2024-09-09 16:20:56)
- `js-libp2p/0.45.5 UserAgent=v22.4.0` (2024-09-09 16:21:25)
- `bootnode-20240909132939` (2024-09-09 18:50:59)
- `github.com/flamingotv/manager@f4726c42b-dirty` (2024-09-09 19:51:38)
- `bootnode-20240909155035` (2024-09-09 20:50:59)
- `bootnode-20240909171112` (2024-09-09 22:21:30)
- `github.com/JackalLabs/sequoia@09bb848e2` (2024-09-09 23:21:17)
- `bootnode-20240910002615` (2024-09-10 00:50:57)
- `bootnode-20240909195940` (2024-09-10 01:20:56)
- `bootnode-20240909205023` (2024-09-10 01:50:49)
- `github.com/JackalLabs/sequoia@756e990e9-dirty` (2024-09-10 01:51:43)
- `kubo/0.30.0-rc3/collab.ipfscluster.io` (2024-09-10 02:52:07)
- `bootnode-20240909225636` (2024-09-10 04:20:57)
- `bootnode-20240910034737` (2024-09-10 04:50:53)
- `bootnode-20240910051822` (2024-09-10 05:20:50)
- `bootnode-20240910065755` (2024-09-10 05:21:42)
- `bootnode-20240910061943` (2024-09-10 06:21:11)
- `bootnode-20240910075102` (2024-09-10 07:51:31)
- `bootnode-20240910065840` (2024-09-10 09:21:22)
- `bootnode-20240910121842` (2024-09-10 10:20:47)
- `bootnode-20240910125035` (2024-09-10 12:50:52)
- `pouw/0.9.27` (2024-09-10 13:21:45)
- `bootnode-20240910090005` (2024-09-10 14:20:50)
- `bootnode-20240910095043` (2024-09-10 14:51:23)
- `bootnode-20240910153925` (2024-09-10 15:51:11)
- `bootnode-20240910142309` (2024-09-10 16:21:06)
- `bootnode-20240910132026` (2024-09-10 18:20:52)
- `bootnode-20240910135030` (2024-09-10 18:50:46)
- `github.com/flamingotv/manager@d1e8c14d9-dirty` (2024-09-10 20:21:06)
- `helia/4.2.5 libp2p/1.9.4 UserAgent=v20.11.1` (2024-09-10 21:50:53)
- `bootnode-20240910205052` (2024-09-11 01:51:00)
- `flamingotv` (2024-09-11 01:51:03)
- `github.com/JackalLabs/sequoia@a47b6fa2e` (2024-09-11 03:20:45)
- `bootnode-20240911031920` (2024-09-11 03:50:55)
- `bootnode-20240911055057` (2024-09-11 05:51:24)
- `bootnode-20240911074200` (2024-09-11 06:50:59)
- `github.com/JackalLabs/sequoia@45d36f09c` (2024-09-11 06:50:59)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v18.20.2` (2024-09-11 08:52:18)
- `github.com/INFURA/ipfs-p2p-server@a255afb35` (2024-09-11 10:21:42)
- `bootnode-20240911055026` (2024-09-11 10:51:03)
- `bootnode-20240911114653` (2024-09-11 12:20:52)
- `bootnode-20240911145306` (2024-09-11 13:20:56)
- `bootnode-20240911082002` (2024-09-11 13:21:22)
- `bootnode-20240911090112` (2024-09-11 14:20:53)
- `bootnode-20240911142101` (2024-09-11 14:21:06)
- `kubo/0.30.0/846c5cc/docker` (2024-09-11 14:50:47)
- `kubo/0.30.0/846c5cc` (2024-09-11 14:50:54)
- `kubo/0.30.0/846c5cc/1234567890123456789012345678901234567890` (2024-09-11 14:51:34)
- `bootnode-20240911145118` (2024-09-11 14:51:37)
- `kubo/0.30.0/` (2024-09-11 16:20:50)
- `github.com/JackalLabs/sequoia@45d36f09c-dirty` (2024-09-11 16:20:57)
- `kubo/0.31.0-dev/3799c32/docker` (2024-09-11 17:21:25)
- `bootnode-20240911135103` (2024-09-11 18:51:13)
- `kubo/0.31.0-dev/4842d6e/docker` (2024-09-11 21:50:54)
- `bootnode-20240911161222` (2024-09-11 22:21:06)
- `kubo/0.31.0-dev/4842d6e54` (2024-09-11 22:21:39)
- `kubo/0.31.0-dev/87542882e` (2024-09-11 22:50:55)
- `bootnode-20240911225048` (2024-09-11 22:51:02)
- `bootnode-20240911185042` (2024-09-11 23:50:50)
- `bootnode-20240911223703` (2024-09-12 00:20:51)
- `bootnode-20240911200849` (2024-09-12 01:51:07)
- `kubo/0.30.0/846c5ccf6` (2024-09-12 04:51:09)
- `bootnode-20240912060840` (2024-09-12 06:21:03)
- `bootnode-20240912064907` (2024-09-12 06:50:51)
- `bootnode-20240912090529` (2024-09-12 07:50:59)
- `bootnode-20240912075046` (2024-09-12 07:51:20)
- `bootnode-20240912083058` (2024-09-12 09:51:46)
- `bootnode-20240912085524` (2024-09-12 11:21:08)
- `kubo/0.31.0-dev/4842d6e54-dirty` (2024-09-12 11:50:53)
- `kubo/0.30.0/desktop` (2024-09-12 12:20:58)
- `helia/4.2.5 libp2p/1.9.4 UserAgent=v20.17.0` (2024-09-12 12:21:06)
- `bootnode-20240912081438` (2024-09-12 13:21:25)
- `bootnode-20240912155001` (2024-09-12 15:51:07)
- `bootnode-20240912151002` (2024-09-12 15:51:09)
- `bootnode-20240912112843` (2024-09-12 16:50:49)
- `bootnode-20240912163129` (2024-09-12 16:51:23)
- `kubo/0.30.0/846c5cc/bootstrap.libp2p.io` (2024-09-12 18:20:58)
- `bootnode-20240912163354` (2024-09-12 18:21:47)
- `helia/4.2.5 libp2p/1.9.4 UserAgent=v22.0.0` (2024-09-12 19:51:04)
- `bootnode-20240912155114` (2024-09-12 20:51:25)
- `helia/4.2.5 libp2p/1.9.4 UserAgent=v22.6.0` (2024-09-12 21:50:54)
- `bootnode-20240912191554` (2024-09-13 00:20:57)
- `bootnode-20240913020001` (2024-09-13 02:21:03)
- `bootnode-20240913031542` (2024-09-13 03:20:56)
- `bootnode-20240913054025` (2024-09-13 05:50:57)
- `bootnode-20240913075058` (2024-09-13 05:51:08)
- `ecos-boostrap@617f60978-dirty` (2024-09-13 08:21:01)
- `bootnode-20240913074846` (2024-09-13 08:51:32)
- `bootnode-20240913111123` (2024-09-13 09:21:02)
- `bootnode-20240913063745` (2024-09-13 12:21:27)
- `github.com/flamingotv/manager@8abdfc09e-dirty` (2024-09-13 12:50:52)
- `bootnode-20240913122216` (2024-09-13 13:51:04)
- `bootnode-20240913132124` (2024-09-13 14:50:55)
- `bootnode-20240913150733` (2024-09-13 15:20:56)
- `bootnode-20240913102012` (2024-09-13 15:21:09)
- `bootnode-20240913185054` (2024-09-13 18:51:09)
- `bootnode-20240913170046` (2024-09-13 22:20:54)
- `bootnode-20240914025844` (2024-09-14 03:21:07)
- `bootnode-20240914053443` (2024-09-14 05:21:36)
- `bootnode-20240914070536` (2024-09-14 07:20:50)
- `bootnode-20240914023508` (2024-09-14 07:50:53)
- `helia/2.0.3 js-libp2p/0.46.11 UserAgent=v20.16.0` (2024-09-14 08:51:41)
- `bootnode-20240914042638` (2024-09-14 10:21:42)
- `bootnode-20240914060706` (2024-09-14 11:20:59)
- `bootnode-20240914105544` (2024-09-14 11:21:12)
- `bootnode-20240914070757` (2024-09-14 13:20:59)
- `bootnode-20240914091838` (2024-09-14 14:21:44)
- `kubo/0.31.0-dev/f6fb36cf4` (2024-09-14 14:51:54)
- `bootnode-20240914173836` (2024-09-14 18:20:54)
- `bootnode-20240914143233` (2024-09-14 19:51:01)
- `bootnode-20240914185210` (2024-09-14 19:51:29)
- `bootnode-20240914202016` (2024-09-14 20:20:58)
- `bootnode-20240914205037` (2024-09-14 20:50:57)
- `bootnode-20240914145258` (2024-09-14 20:51:04)
- `bootnode-20240914211830` (2024-09-14 21:20:57)
- `bootnode-20240914180401` (2024-09-14 23:20:56)
- `bootnode-20240914225855` (2024-09-14 23:51:02)
- `bootnode-20240914191430` (2024-09-15 00:50:58)
- `bootnode-20240915024707` (2024-09-15 00:51:16)
- `bootnode-20240915042817` (2024-09-15 02:50:54)
- `bootnode-20240914222034` (2024-09-15 03:20:53)
- `bootnode-20240915044820` (2024-09-15 04:50:54)
- `bootnode-20240915051228` (2024-09-15 05:51:20)
- `bootnode-20240915061253` (2024-09-15 06:20:55)
- `bootnode-20240915083900` (2024-09-15 07:50:56)
- `bootnode-20240915025036` (2024-09-15 07:50:58)
- `kubo/0.30.0/VALGRIND` (2024-09-15 07:51:07)
- `bootnode-20240915035039` (2024-09-15 08:50:54)
- `bootnode-20240915040707` (2024-09-15 09:20:48)
- `bootnode-20240915092045` (2024-09-15 09:20:53)
- `bootnode-20240915124924` (2024-09-15 10:51:20)
- `bootnode-20240915063203` (2024-09-15 11:50:52)
- `bootnode-20240915142330` (2024-09-15 14:51:24)
- `bootnode-20240915194003` (2024-09-15 18:21:07)
- `bootnode-20240915205025` (2024-09-15 18:50:51)
- `bootnode-20240915204724` (2024-09-15 21:51:04)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `crimep/navigaton/1.0.0` (2024-09-09 16:21:38)
- `/storage/req` (2024-09-09 19:51:38)
- `/storage/res` (2024-09-09 19:51:38)
- `/hypermedia/0.4.0-dev` (2024-09-10 12:21:26)
- `/chat/1.0` (2024-09-10 13:21:45)
- `/hypermedia/0.4.0--data-dir=/data` (2024-09-10 16:51:33)
- `crimep/communcation/1.0.0` (2024-09-11 03:51:01)
- `/flamingo/kad/1.0.0` (2024-09-13 13:21:19)
- `/flamingo/ipfs/bitswap/1.2.0` (2024-09-13 13:21:19)
- `/flamingo/ipfs/bitswap/1.0.0` (2024-09-13 13:50:46)
- `/flamingo/ipfs/bitswap` (2024-09-13 13:50:46)
- `/flamingo/ipfs/bitswap/1.1.0` (2024-09-13 13:50:46)
- `flamingo/ipfs/bitswap/1.0.0` (2024-09-15 09:20:52)
- `flamingo/ipfs/bitswap` (2024-09-15 09:20:52)
- `flamingo/ipfs/bitswap/1.1.0` (2024-09-15 09:20:52)
- `flamingo/ipfs/bitswap/1.2.0` (2024-09-15 09:20:52)
- `/flamingo/storage/res` (2024-09-15 09:50:59)
- `/flamingo/storage/req` (2024-09-15 09:50:59)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `51.15.64.186` | NL | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.247.127` | FR | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.150.159` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 76 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 66 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `68.183.11.180` | NL | 51 | ['edgevpn']| True  |
| `178.128.39.79` | GB | 43 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b', 'kubo/0.29.0/brave']| True  |

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

In the specified time interval from `2024-09-09` to `2024-09-16` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-09-09` to `2024-09-16` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-09-09` to `2024-09-16` in the DHT and their datacenter association.

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