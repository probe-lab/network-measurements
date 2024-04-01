# Nebula Measurement Results Calendar Week 13 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 13 - 2024](#nebula-measurement-results-calendar-week-13---2024)
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

The following results show measurement data that were collected in calendar week 13 in 2024 from `2024-03-25` to `2024-04-01`.

- Number of crawls `336`
- Number of visits `36,090,132`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `64,590`
- Number of unique peer IDs discovered in the DHT `62,796`
- Number of unique IP addresses found `89,835`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.27.0/f2a0454-dirty` (2024-03-25 05:21:12)
- `github.com/zzz136454872/upgradeable-consensus@8fdb39fe9-dirty` (2024-03-25 09:20:55)
- `kubo/0.28.0-dev/62eb143/docker` (2024-03-25 09:50:59)
- `github.com/zzz136454872/upgradeable-consensus@5a9214cea` (2024-03-25 13:50:59)
- `github.com/INFURA/ipfs-p2p-server@3171337b2` (2024-03-25 17:22:21)
- `kubo/0.25.0/3a6a641-dirty` (2024-03-25 18:50:57)
- `github.com/INFURA/ipfs-p2p-server@550a49e6c` (2024-03-25 19:22:19)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v18.19.0` (2024-03-26 17:22:18)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v20.11.0` (2024-03-27 07:21:39)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v20.10.0` (2024-03-27 09:50:58)
- `github.com/bitcoin-sv/alert-system@a100a1210` (2024-03-27 13:51:10)
- `libp2p/1.3.0 UserAgent=v18.18.2` (2024-03-27 16:21:01)
- `SybilNode@6238759c0-dirty` (2024-03-27 17:21:01)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v21.7.1` (2024-03-27 18:21:46)
- `github.com/INFURA/ipfs-p2p-server@7cc249061` (2024-03-27 20:52:05)
- `kubo/0.24.0/docker` (2024-03-28 04:21:54)
- `github.com/zzz136454872/upgradeable-consensus@90ab4f614-dirty` (2024-03-28 07:20:56)
- `github.com/zzz136454872/upgradeable-consensus@23c541730` (2024-03-28 08:21:08)
- `github.com/zzz136454872/upgradeable-consensus@c51dc760f` (2024-03-28 12:21:27)
- `github.com/zzz136454872/upgradeable-consensus@6b4f08a19` (2024-03-28 13:20:52)
- `github.com/zzz136454872/upgradeable-consensus@fb8bb310c` (2024-03-28 13:50:58)
- `github.com/zzz136454872/upgradeable-consensus@c5fb3b232` (2024-03-28 14:21:08)
- `github.com/zzz136454872/upgradeable-consensus@cd52a5481` (2024-03-28 14:50:49)
- `github.com/zzz136454872/upgradeable-consensus@36ad80d72` (2024-03-28 15:20:54)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v18.15.0` (2024-03-28 16:51:44)
- `kubo/0.28.0-dev/62eb14391` (2024-03-29 06:50:45)
- `github.com/zzz136454872/upgradeable-consensus@96adcbc57` (2024-03-29 07:50:59)
- `github.com/zzz136454872/upgradeable-consensus@e511d4bc4` (2024-03-29 08:20:50)
- `github.com/zzz136454872/upgradeable-consensus@bce51cdd5` (2024-03-29 08:50:58)
- `github.com/zzz136454872/upgradeable-consensus@fb1ffaf42` (2024-03-29 09:20:51)
- `github.com/zzz136454872/upgradeable-consensus@bf75ed50c` (2024-03-29 09:51:18)
- `github.com/zzz136454872/upgradeable-consensus@e0aebc289` (2024-03-29 10:21:08)
- `github.com/zzz136454872/upgradeable-consensus@65ae5572c` (2024-03-29 12:20:52)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v18.17.1` (2024-03-29 12:20:57)
- `github.com/zzz136454872/upgradeable-consensus@1b1b940f1` (2024-03-29 12:50:48)
- `github.com/zzz136454872/upgradeable-consensus@918298932` (2024-03-29 13:51:24)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v20.5.0` (2024-03-29 21:50:56)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v20.12.0` (2024-03-29 23:51:08)
- `go-btfs/2.3.5/9fdd194` (2024-03-30 10:21:11)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v20.9.0` (2024-03-31 21:20:52)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `bpfs@stream/transaction/id/1.1.0` (2024-03-28 06:52:01)
- `bpfs@stream/blockChain/bestheight/1.1.0` (2024-03-29 09:51:03)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `54.233.234.50` | BR | 268 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.26.0/', 'kubo/0.26.0/brave']| True  |
| `159.203.76.161` | US | 226 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `188.165.71.178` | FR | 218 | ['kubo/0.20.0/', 'kubo/0.27.0/', 'SybilNode@6238759c0-dirty', 'SybilNode@ca43010bf-dirty']| True  |
| `51.159.134.20` | FR | 85 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | NL | 74 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | FR | 74 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 73 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 73 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.245.0` | FR | 70 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `3.1.209.56` | SG | 58 | ['kubo/0.26.0/']| True  |

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

In the specified time interval from `2024-03-25` to `2024-04-01` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-03-25` to `2024-04-01` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-03-25` to `2024-04-01` in the DHT and their datacenter association.

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