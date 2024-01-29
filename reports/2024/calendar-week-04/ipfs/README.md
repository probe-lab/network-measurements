# Nebula Measurement Results Calendar Week 4 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 4 - 2024](#nebula-measurement-results-calendar-week-4---2024)
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

The following results show measurement data that were collected in calendar week 4 in 2024 from `2024-01-22` to `2024-01-29`.

- Number of crawls `336`
- Number of visits `37,093,215`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `63,933`
- Number of unique peer IDs discovered in the DHT `62,073`
- Number of unique IP addresses found `82,398`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.26.0/096f510/docker` (2024-01-22 14:51:04)
- `kubo/0.27.0-dev/d1db95c/docker` (2024-01-22 15:52:25)
- `kubo/0.26.0/096f510ab` (2024-01-22 16:52:24)
- `kubo/0.26.0/` (2024-01-22 17:52:33)
- `kubo/0.26.0/desktop` (2024-01-22 18:21:57)
- `kubo/0.27.0-dev/5f18f4d/docker` (2024-01-22 18:51:02)
- `helia/3.0.1 libp2p/1.2.0 UserAgent=v20.9.0` (2024-01-22 19:20:54)
- `github.com/INFURA/ipfs-p2p-server@fb2b0e992` (2024-01-22 21:21:58)
- `github.com/INFURA/ipfs-p2p-server@3ccbe5ac4` (2024-01-22 21:52:26)
- `github.com/INFURA/ipfs-p2p-server@a47e624c2` (2024-01-22 22:22:27)
- `kubo/0.26.0/096f510/1234567890123456789012345678901234567890` (2024-01-22 22:51:05)
- `kubo/0.27.0-dev/5f18f4d43` (2024-01-23 00:21:03)
- `kubo/0.26.0/096f510` (2024-01-23 08:51:04)
- `kubo/0.27.0-dev/3a8495d/docker` (2024-01-23 10:50:48)
- `github.com/INFURA/ipfs-p2p-server@4aadac027` (2024-01-23 11:52:04)
- `kubo/0.21.0-dev/eb06857/docker` (2024-01-23 13:21:15)
- `kubo/0.27.0-dev/3a8495d84` (2024-01-23 14:22:28)
- `kubo/0.27.0-dev/79235497a` (2024-01-23 18:21:03)
- `kubo/0.27.0-dev/be9d87a/docker` (2024-01-23 20:22:01)
- `github.com/INFURA/ipfs-p2p-server@643bad0ff` (2024-01-23 21:51:27)
- `github.com/INFURA/ipfs-p2p-server@9e16b2688` (2024-01-23 22:22:06)
- `kubo/0.27.0-dev/e166af9/docker` (2024-01-24 12:20:48)
- `github.com/sukun/go-libp2p-file-transfer@4fffb7762-dirty` (2024-01-24 12:20:53)
- `github.com/INFURA/ipfs-p2p-server@b61c287f9` (2024-01-24 15:51:31)
- `kubo/0.27.0-dev/f9edd2b/docker` (2024-01-24 18:21:25)
- `metafog@` (2024-01-24 19:51:05)
- `helia/3.0.1 libp2p/1.1.2 UserAgent=v21.2.0` (2024-01-24 19:51:15)
- `kubo/0.26.0/dfec50d5f` (2024-01-25 10:21:29)
- `kubo/0.27.0-dev/3a8495d84-dirty` (2024-01-25 10:52:21)
- `Avail Node/v1.9.0-unknown (Boi)` (2024-01-25 16:50:51)
- `libp2p/1.2.0 UserAgent=v20.10.0` (2024-01-25 18:51:04)
- `kubo/0.27.0-dev/262151f/docker` (2024-01-26 03:21:34)
- `helia/4.0.0 libp2p/1.2.1 UserAgent=v18.17.1` (2024-01-26 08:51:14)
- `kubo/0.25.0/413a52d0e/docker` (2024-01-26 15:52:10)
- `github.com/INFURA/ipfs-p2p-server@b0c3f820f` (2024-01-26 18:21:40)
- `kubo/0.27.0-dev/4d3cc96/docker` (2024-01-26 20:22:04)
- `helia/4.0.0 libp2p/1.2.1 UserAgent=v21.6.1` (2024-01-26 20:51:44)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.11.0` (2024-01-26 21:51:06)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v18.19.0` (2024-01-26 21:51:09)
- `js-libp2p/0.45.9 UserAgent=v16.20.1` (2024-01-26 23:52:28)
- `libp2p/1.2.0 UserAgent=v21.5.0` (2024-01-27 03:51:44)
- `kubo/0.20.0-rc2/8418b08/docker` (2024-01-28 03:21:19)
- `libp2p/1.2.1 UserAgent=v18.17.1` (2024-01-28 04:50:59)
- `github.com/bahner/go-ma-relay@3cbd35a8a-dirty` (2024-01-28 13:22:06)
- `github.com/bahner/go-ma-relay@ed0f6bc04-dirty` (2024-01-28 14:50:56)
- `go-ma-home@f43599db0-dirty` (2024-01-28 15:20:48)
- `github.com/bahner/go-ma-relay@f43599db0-dirty` (2024-01-28 15:52:07)
- `helia/3.0.1 libp2p/1.2.0 UserAgent=v20.3.1` (2024-01-28 18:20:52)
- `go-ma-pong@10c8dfe4b-dirty` (2024-01-28 20:50:48)
- `github.com/bahner/go-ma-relay@10c8dfe4b-dirty` (2024-01-28 21:21:19)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/sukun/file/fetch` (2024-01-24 12:20:53)
- `/sukun/file/list` (2024-01-24 12:20:53)
- `/metafog-container-copyfrom/1.0.0` (2024-01-24 19:51:05)
- `/metafog-container-create/1.0.0` (2024-01-24 19:51:05)
- `/metafog-container-exec/1.0.0` (2024-01-24 19:51:05)
- `/metafog-tcp-proxy/1.0.0` (2024-01-24 19:51:05)
- `/metafog-container-delete/1.0.0` (2024-01-24 19:51:05)
- `/metafog-container-logs/1.0.0` (2024-01-24 19:51:05)
- `/metafog-container-ping/1.0.0` (2024-01-24 19:51:05)
- `/metafog-http-rev-proxy/1.0.0` (2024-01-24 19:51:05)
- `/metafog-pod-get-info/1.0.0` (2024-01-24 19:51:05)
- `/metafog-container-copyto/1.0.0` (2024-01-24 19:51:05)
- `/hypermedia/0.3.0` (2024-01-24 22:20:48)
- `/tss/keySign/session/a8f605a4-bc34-11ee-9328-0242c0a60a78` (2024-01-26 10:21:36)
- `/hypermedia/0.3.0-dev` (2024-01-26 10:51:14)
- `/bitcoin-testnet/alert-system/0.0.1` (2024-01-26 19:21:30)
- `/orbitdb/heads/orbitdb/zdpuAtkqXPRZSSEMqJP8w6taoxTuB7bfDTycJVVjKs2nn3S3e` (2024-01-27 03:51:44)
- `/orbitdb/heads/orbitdb/zdpuAvTRAzGEog3LhTAayMa1MbV4i6WaVuPNK5vxUhm8uqJuC` (2024-01-27 04:51:08)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `172.33.1.5` | US | 211 | ['kubo/0.15.0/3ae52a4', 'kubo/0.17.0/4485d6b', 'kubo/0.19.1/', 'kubo/0.22.0/3f884d3/docker']| False  |
| `159.203.76.161` | US | 192 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `212.47.234.38` | FR | 93 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.128.68` | FR | 91 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.128.68` | IN | 91 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 60 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `151.115.53.194` | PL | 58 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 56 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 56 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 50 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-01-22` to `2024-01-29` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-01-22` to `2024-01-29` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-01-22` to `2024-01-29` in the DHT and their datacenter association.

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