# Nebula Measurement Results Calendar Week 32 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 32 - 2023](#nebula-measurement-results-calendar-week-32---2023)
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

The following results show measurement data that were collected in calendar week 32 in 2023 from `2023-08-07` to `2023-08-14`.

- Number of crawls `336`
- Number of visits `55,166,770`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `43,954`
- Number of unique peer IDs discovered in the DHT `43,855`
- Number of unique IP addresses found `61,043`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `js-libp2p/0.45.6 UserAgent=v18.12.1` (2023-08-07 03:23:16)
- `github.com/4everland/ipns-server@697170315-dirty` (2023-08-07 09:52:15)
- `kubo/0.17.0-dev/5d5fb41a4-dirty` (2023-08-07 12:22:05)
- `kubo/0.22.0-dev/895963b95` (2023-08-07 13:22:47)
- `app-ecos@e36dc5fe9-dirty` (2023-08-07 16:52:50)
- `kubo/0.23.0-dev/c5cc835/docker` (2023-08-08 03:21:40)
- `kubo/0.21.0/DangleBat` (2023-08-08 05:22:31)
- `github.com/4everland/ipns-server@727578893-dirty` (2023-08-08 09:21:28)
- `kubo/0.21.1/bc0d1a4/docker` (2023-08-08 12:51:40)
- `kubo/0.22.0/3f884d3/docker` (2023-08-08 15:22:49)
- `kubo/0.23.0-dev/2a20180/docker` (2023-08-08 20:52:35)
- `kubo/0.22.0/` (2023-08-09 05:22:12)
- `github.com/4everland/ipfs-servers@b6a23d2a4-dirty` (2023-08-09 07:52:02)
- `kubo/0.22.0/desktop` (2023-08-09 17:51:31)
- `kubo/0.22.0/3f884d3/s̳̪̦̩̝͎͙͝u͍̫̺̝̱̰͝p̠͔̫͓̬̦` (2023-08-09 19:21:39)
- `kubo/0.23.0-dev/54ac812/docker` (2023-08-09 22:51:21)
- `github.com/bahner/myspace-pubsub-daemon@b362a6c48` (2023-08-09 23:52:50)
- `kubo/0.22.0/3f884d315` (2023-08-10 12:52:16)
- `kubo/0.23.0-dev/7c2aee010` (2023-08-10 17:51:44)
- `kubo/ceramic-0.19.1-validator/71fd60f-dirty/docker` (2023-08-10 18:22:54)
- `github.com/application-research/edge-ur@9f41c7e29-dirty` (2023-08-10 19:21:46)
- `github.com/bahner/go-myspace-client@02fd79ba1-dirty` (2023-08-11 00:51:53)
- `github.com/bahner/go-myspace-client@f4dfeb03c-dirty` (2023-08-11 02:21:16)
- `github.com/bahner/myspace-pubsub-daemon@741a311d0` (2023-08-11 04:52:30)
- `github.com/bahner/go-myspace-client@5dd42d380` (2023-08-11 05:22:13)
- `kubo/0.23.0-dev/54ac812` (2023-08-11 09:22:08)
- `rust-libp2p-server/0.12.1` (2023-08-11 11:21:01)
- `go-ipfs/0.9.0-dev/2ed925442` (2023-08-11 16:22:51)
- `kubo/0.22.0/3f884d3` (2023-08-11 16:51:20)
- `github.com/chenjia404/p2ptunnel@045e521d9-dirty` (2023-08-11 18:52:22)
- `kubo/0.22.0/3f884d315/docker` (2023-08-11 20:51:20)
- `github.com/ikeikeikeike/peerdrive@` (2023-08-12 16:52:53)
- `github.com/threecorp/peerdrive@` (2023-08-13 15:21:34)
- `github.com/bahner/go-dht-server@` (2023-08-13 19:52:50)
- `github.com/bahner/go-dht-bootstrap-peer@` (2023-08-13 21:52:53)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `2ee2e74e9cc622ebe9ad24f123d6a8fac2826ef4fad1f9ef6098be0d8d5740c7d963c914a015ef18e94c5f62fadc07db61f8601ff21688b3bfcddfdbfa1e7fcd` (2023-08-07 03:51:54)
- `/peerdrive/1.0.0` (2023-08-12 16:52:53)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 200 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `35.199.42.20` | US | 81 | ['Taubyte Node v1.0']| True  |
| `44.206.49.127` | US | 48 | ['kubo/0.14.0-rc1/']| True  |
| `172.33.1.5` | US | 26 | ['kubo/0.15.0/3ae52a4', 'kubo/0.17.0/4485d6b', 'kubo/0.22.0/3f884d3/docker']| False  |
| `173.212.218.215` | DE | 23 | ['go-ipfs/0.11.0/d6518322f4']| True  |
| `91.53.107.231` | DE | 21 | ['go-ipfs/0.6.0/']| False  |
| `93.95.167.72` | RU | 18 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `46.50.211.77` | RU | 17 | ['go-ipfs/0.8.0/48f94e2']| False  |
| `91.39.218.195` | DE | 16 | ['go-ipfs/0.6.0/']| False  |
| `61.65.53.92` | TW | 15 | ['go-ipfs/0.8.0/48f94e2']| False  |

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

In the specified time interval from `2023-08-07` to `2023-08-14` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-08-07` to `2023-08-14` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-08-07` to `2023-08-14` in the DHT and their datacenter association.

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