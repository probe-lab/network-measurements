# Nebula Measurement Results Calendar Week 6 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 6 - 2024](#nebula-measurement-results-calendar-week-6---2024)
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

The following results show measurement data that were collected in calendar week 6 in 2024 from `2024-02-05` to `2024-02-12`.

- Number of crawls `336`
- Number of visits `40,032,580`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `63,811`
- Number of unique peer IDs discovered in the DHT `61,836`
- Number of unique IP addresses found `84,433`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.22.0/3f884d315/desktop` (2024-02-05 11:50:52)
- `github.com/libp2p/go-libp2p/examples@cea5b4ce1-dirty` (2024-02-05 13:21:16)
- `helia/4.0.1 libp2p/1.2.1 UserAgent=v19.9.0` (2024-02-05 14:52:13)
- `kubo/0.26.0/brave` (2024-02-05 16:51:18)
- `neuron/sdk@2bed2e4dd-dirty` (2024-02-05 17:21:23)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v18.15.0` (2024-02-05 21:21:18)
- `kubo/0.26.0/69e9c8fdf-dirty` (2024-02-05 22:51:20)
- `kubo/0.21.0/4d5f2b89e` (2024-02-06 08:20:58)
- `helia/3.0.1 libp2p/1.2.1 UserAgent=v20.10.0` (2024-02-06 09:52:22)
- `/chat/1.1.0` (2024-02-06 12:21:23)
- `kubo/0.27.0-dev/dccbfcf/docker` (2024-02-06 16:22:27)
- `kubo/0.27.0-dev/dccbfcf6b-dirty/docker` (2024-02-06 20:21:02)
- `kubo/0.26.0/docker` (2024-02-07 04:52:31)
- `js-libp2p/0.45.9 UserAgent=v21.5.0` (2024-02-07 11:21:08)
- `js-libp2p/0.45.9` (2024-02-07 15:51:02)
- `neuron/sdk@311dbeead-dirty` (2024-02-07 19:21:15)
- `neuron/sdk@4b8ecb69e` (2024-02-07 22:21:01)
- `github.com/bahner/go-ma-actor@106384873-dirty` (2024-02-08 01:21:07)
- `kubo/0.26.0/kube` (2024-02-08 01:51:51)
- `invictus@` (2024-02-08 14:21:07)
- `kubo/0.27.0-dev/f4ff4f7/docker` (2024-02-08 14:51:30)
- `simple-bootstrap-node-master@dd4e397b8-dirty` (2024-02-08 16:51:06)
- `github.com/bahner/go-ma-actor@d9ace67b2-dirty` (2024-02-08 20:21:15)
- `kubo/0.27.0-dev/eb7f663/docker` (2024-02-09 03:21:41)
- `libp2p/1.2.3 UserAgent=v18.19.0` (2024-02-09 08:21:01)
- `go-ipfs/0.14.0-dev/506b24326` (2024-02-09 08:21:06)
- `feishup2pclient` (2024-02-09 08:21:07)
- `helia/4.0.1 libp2p/1.2.3 UserAgent=v18.19.0` (2024-02-09 08:22:06)
- `neuron/sdk@4b8ecb69e-dirty` (2024-02-09 09:50:51)
- `kubo/0.27.0-dev/1514785/docker` (2024-02-09 17:21:15)
- `neuron/sdk@81ff193ac-dirty` (2024-02-09 17:21:19)
- `kubo/0.27.0-dev/1628289` (2024-02-09 18:21:36)
- `kubo/0.24.0/e70db6531-dirty/docker` (2024-02-09 21:21:11)
- `neuron/sdk@6b8010ed0-dirty` (2024-02-09 21:50:50)
- `xc` (2024-02-10 13:52:23)
- `libp2p/1.2.1 UserAgent=v20.11.0` (2024-02-10 17:51:23)
- `Avail Node/v1.10.0-b514ad4ea43 ()` (2024-02-10 21:20:51)
- `github.com/bahner/go-ma-actor@106384873` (2024-02-11 00:22:08)
- `github.com/bahner/go-ma-actor@169ae9944-dirty` (2024-02-11 00:51:14)
- `github.com/bahner/go-ma-actor@316c05259-dirty` (2024-02-11 14:21:29)
- `helia/4.0.1 libp2p/1.2.1 UserAgent=v20.8.0` (2024-02-11 23:51:09)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/customized-chat/1.1.0` (2024-02-05 13:21:16)
- `/fs/0.0.1` (2024-02-09 08:21:07)
- `/orbitdb/heads/orbitdb/zdpuAvvLtZu1DbBDX8bmPd2Sqxkg3zZxenDW2pxakf8BLQ3b2` (2024-02-10 17:51:23)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 216 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `172.33.1.5` | US | 134 | ['kubo/0.15.0/3ae52a4', 'kubo/0.19.1/', 'kubo/0.22.0/3f884d3/docker']| False  |
| `51.15.128.68` | FR | 95 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.128.68` | IN | 95 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `212.47.234.38` | FR | 92 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.238.83` | FR | 77 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.142.254` | FR | 74 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 62 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.125.129` | FR | 58 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 58 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-02-05` to `2024-02-12` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-02-05` to `2024-02-12` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-02-05` to `2024-02-12` in the DHT and their datacenter association.

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