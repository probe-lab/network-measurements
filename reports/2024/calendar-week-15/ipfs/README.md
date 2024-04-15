# Nebula Measurement Results Calendar Week 15 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 15 - 2024](#nebula-measurement-results-calendar-week-15---2024)
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

The following results show measurement data that were collected in calendar week 15 in 2024 from `2024-04-08` to `2024-04-15`.

- Number of crawls `336`
- Number of visits `28,655,504`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `51,503`
- Number of unique peer IDs discovered in the DHT `49,024`
- Number of unique IP addresses found `71,125`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.12.1` (2024-04-08 13:57:04)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v18.19.0` (2024-04-08 18:30:51)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v18.18.2` (2024-04-09 01:02:24)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v20.8.1` (2024-04-09 09:45:08)
- `kubo/0.29.0-dev/` (2024-04-10 04:51:08)
- `kubo/0.17.0-dev/8c72ea9` (2024-04-10 09:21:30)
- `kubo/0.29.0-dev/4ae097e/docker` (2024-04-10 16:21:04)
- `kubo/0.28.0-rc1/` (2024-04-11 04:21:09)
- `kubo/0.28.0-rc1/a91640f/docker` (2024-04-11 06:51:09)
- `helia/3.0.1 libp2p/1.3.3 UserAgent=v18.14.2` (2024-04-11 08:21:02)
- `helia/4.1.0 libp2p/1.3.3 UserAgent=v16.18.0` (2024-04-11 21:50:53)
- `helia/4.1.0 libp2p/1.3.3 UserAgent=v21.7.3` (2024-04-11 22:51:11)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v21.7.2` (2024-04-12 02:21:03)
- `kubo/0.29.0-dev/4ae097efe-dirty` (2024-04-12 05:20:47)
- `chat2@` (2024-04-12 06:50:56)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v20.12.2` (2024-04-12 09:51:41)
- `kubo/0.28.0-rc1/a91640f/1234567890123456789012345678901234567890` (2024-04-12 17:51:27)
- `libp2p/1.3.3 UserAgent=v20.11.1` (2024-04-13 18:51:37)
- `kubo/0.29.0-dev/4ae097efe` (2024-04-14 01:21:51)
- `helia/4.1.0 libp2p/1.4.0 UserAgent=v18.19.1` (2024-04-14 12:20:47)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/edgevpn/file/0.1` (2024-04-11 16:50:59)
- `/super-fun/1.0.0` (2024-04-11 21:50:53)
- `bpfs@stream/file/folders/list/1.1.0` (2024-04-12 12:50:57)
- `bpfs@stream/file/record/1.1.0` (2024-04-12 12:50:57)
- `bpfs@stream/file/upload/1.1.0` (2024-04-12 12:50:57)
- `bpfs@stream/file/folders/1.1.0` (2024-04-12 12:50:57)
- `bpfs@stream/file/folders/update/1.1.0` (2024-04-12 12:50:57)
- `bpfs@stream/file/upload/check/1.1.0` (2024-04-12 12:50:57)
- `defs@stream/download/local/1.0.0` (2024-04-12 12:50:57)
- `defs@stream/sending/network/1.0.0` (2024-04-12 12:50:57)
- `defs@stream/peer/distance/1.0.0` (2024-04-12 12:50:57)
- `bpfs@stream/file/update/1.1.0` (2024-04-12 12:50:57)
- `defs@stream/download/checklist/response/1.0.0` (2024-04-12 12:50:57)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 227 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `188.165.71.178` | FR | 166 | ['kubo/0.18.0/', 'kubo/0.27.0/', 'main@6238759c0-dirty']| True  |
| `188.165.71.178` | FR | 165 | ['kubo/0.18.0/', 'kubo/0.27.0/']| True  |
| `51.15.245.0` | FR | 115 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.245.0` | FR | 115 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.134.20` | FR | 89 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.134.20` | FR | 89 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 82 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 82 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.151.120` | FR | 82 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-04-08` to `2024-04-15` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-04-08` to `2024-04-15` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-04-08` to `2024-04-15` in the DHT and their datacenter association.

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