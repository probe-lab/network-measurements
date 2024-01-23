# Nebula Measurement Results Calendar Week 40 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 40 - 2023](#nebula-measurement-results-calendar-week-40---2023)
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

The following results show measurement data that were collected in calendar week 40 in 2023 from `2023-10-02` to `2023-10-09`.

- Number of crawls `336`
- Number of visits `56,236,945`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `47,090`
- Number of unique peer IDs discovered in the DHT `46,291`
- Number of unique IP addresses found `47,346`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/dennis-tra/parsec@a15c73a21-dirty` (2023-10-02 16:22:42)
- `github.com/dennis-tra/parsec@2db39b892-dirty` (2023-10-02 16:51:16)
- `kubo/0.24.0-dev/97527472f` (2023-10-02 22:21:26)
- `kubo/0.22.0/cf4c3eb25` (2023-10-03 01:21:26)
- `github.com/dennis-tra/parsec@b47cf1534-dirty` (2023-10-03 04:51:31)
- `kubo/0.23.0-rc1/9dbe4f4` (2023-10-03 05:52:05)
- `kubo/0.24.0-dev/9752747/docker` (2023-10-03 09:22:11)
- `github.com/dennis-tra/parsec@1dce65c5b-dirty` (2023-10-03 09:51:10)
- `kubo/0.23.0-dev/ac3dd1a/docker` (2023-10-03 15:51:35)
- `kubo/0.22.0/3f884d3/thunderdome` (2023-10-03 16:21:50)
- `kubo/0.22.0/ff1a93c6d` (2023-10-03 22:21:55)
- `kubo/0.18.0/6750377-dirty/docker` (2023-10-04 03:23:03)
- `kubo/0.23.0-dev/0398d0c/thunderdome` (2023-10-04 09:51:57)
- `xmd-drop@5c26f37f0-dirty` (2023-10-04 11:52:52)
- `xmd-drop@` (2023-10-04 18:51:32)
- `kubo/0.22.0/36de33346` (2023-10-04 19:51:55)
- `kubo/0.24.0-dev/c80a5a867` (2023-10-05 06:21:46)
- `kubo/0.23.0-rc1/9dbe4f4/docker` (2023-10-05 09:51:49)
- `kubo/0.23.0-rc1/9dbe4f4/thunderdome` (2023-10-05 10:21:25)
- `xmd-drop@0d3ff4339-dirty` (2023-10-05 12:52:22)
- `kubo/0.23.0-dev/65e9598/thunderdome` (2023-10-05 14:22:15)
- `kubo/0.23.0/3a1a041/docker` (2023-10-05 16:21:26)
- `kubo/0.24.0-dev/c80a5a867-dirty` (2023-10-05 16:52:13)
- `github.com/bahner/go-dht-bootstrap-peer@5fce1454b-dirty` (2023-10-05 16:52:51)
- `kubo/0.23.0/` (2023-10-05 18:51:03)
- `kubo/0.24.0-dev/6dbae76/docker` (2023-10-05 20:52:17)
- `kubo/0.23.0/3a1a041/1234567890123456789012345678901234567890` (2023-10-05 23:23:08)
- `kubo/0.23.0/ecda7ae/docker` (2023-10-06 01:52:21)
- `go-ipfs/0.11.0/e6a3b2fc2e` (2023-10-06 12:21:43)
- `kubo/0.23.0/3a1a0413a/desktop` (2023-10-07 08:52:58)
- `git.energy/corepass/go-communicator@6427d38d5-dirty` (2023-10-07 11:51:56)
- `github.com/bahner/go-dht-bootstrap-peer@3f4d60ae0` (2023-10-07 13:21:43)
- `kubo/0.23.0/3a1a0413a` (2023-10-07 14:51:12)
- `github.com/bahner/go-dht-bootstrap-peer@438ccf631-dirty` (2023-10-07 20:21:30)
- `github.com/bahner/go-dht-bootstrap-peer@f8083f53a` (2023-10-08 00:51:13)
- `kubo/0.23.0/3a1a041` (2023-10-08 02:52:33)
- `github.com/bahner/go-dht-bootstrap-peer@1860287d6-dirty` (2023-10-08 03:22:15)
- `kubo/0.23.0/a7c6518/docker` (2023-10-08 12:51:56)
- `kubo/0.23.0/desktop` (2023-10-08 15:22:02)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/xmd-test/1.1.0` (2023-10-05 12:52:22)
- `/dhtapp/1.0.0` (2023-10-06 02:22:29)
- `corepass/signaling/1.0.0` (2023-10-07 11:51:56)
- `/araneidae/vpn/0.1` (2023-10-08 08:52:51)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 210 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `51.15.238.83` | FR | 117 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `172.33.1.5` | US | 48 | ['kubo/0.15.0/3ae52a4', 'kubo/0.17.0/4485d6b', 'kubo/0.22.0/3f884d3/docker']| False  |
| `151.115.54.82` | PL | 44 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 42 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `163.172.142.51` | FR | 35 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.156.36` | FR | 34 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `212.47.244.180` | FR | 32 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.154.220` | FR | 21 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `206.189.255.126` | US | 21 | ['kubo/0.18.1/675f8bd-dirty/docker']| True  |

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

In the specified time interval from `2023-10-02` to `2023-10-09` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-10-02` to `2023-10-09` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-10-02` to `2023-10-09` in the DHT and their datacenter association.

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