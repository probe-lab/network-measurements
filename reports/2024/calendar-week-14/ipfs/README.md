# Nebula Measurement Results Calendar Week 14 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 14 - 2024](#nebula-measurement-results-calendar-week-14---2024)
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

The following results show measurement data that were collected in calendar week 14 in 2024 from `2024-04-01` to `2024-04-08`.

- Number of crawls `336`
- Number of visits `34,665,482`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `60,026`
- Number of unique peer IDs discovered in the DHT `58,256`
- Number of unique IP addresses found `80,596`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `helia/3.0.1 libp2p/1.3.1 UserAgent=v20.12.0` (2024-04-01 15:21:05)
- `main@6238759c0-dirty` (2024-04-01 21:21:47)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v21.7.1` (2024-04-02 10:21:05)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v18.19.1` (2024-04-02 18:51:10)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v21.6.2` (2024-04-03 01:50:53)
- `kubo/0.28.0-dev/b7b6137/docker` (2024-04-03 05:51:08)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v21.1.0` (2024-04-03 11:21:02)
- `kubo/0.28.0-dev/efceaec/docker` (2024-04-03 11:51:04)
- `kubo/0.27.0/brave` (2024-04-03 13:51:29)
- `kubo/0.28.0-dev/78a96e3/docker` (2024-04-03 14:51:25)
- `kubo/0.28.0-dev/78a96e3fa-dirty` (2024-04-03 17:51:25)
- `kubo/0.28.0-dev/78a96e3fa` (2024-04-03 18:51:34)
- `kubo/0.24.0/2d4a20e9c` (2024-04-03 20:51:26)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v18.16.1` (2024-04-04 06:51:21)
- `kubo/0.28.0-dev/6d53507/docker` (2024-04-04 06:51:28)
- `kubo/0.28.0-dev/8143db029` (2024-04-04 11:51:25)
- `kubo/0.28.0-dev/cd78f2e/docker` (2024-04-04 12:51:12)
- `kubo/0.28.0-dev/324424f53` (2024-04-04 12:51:28)
- `libp2p/1.3.1 UserAgent=v18.16.0` (2024-04-04 13:51:11)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v18.16.0` (2024-04-04 13:51:30)
- `kubo/0.28.0-dev/11183bb/docker` (2024-04-04 15:51:14)
- `kubo/0.28.0-dev/9db17fbe3` (2024-04-04 19:51:22)
- `kubo/0.27.0/59bcea878-dirty` (2024-04-05 00:20:50)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.12.0` (2024-04-05 08:51:00)
- `helia/4.1.0 libp2p/1.3.1 UserAgent=v21.6.2` (2024-04-05 09:20:58)
- `kubo/0.28.0-dev/6d535072d` (2024-04-05 10:21:12)
- `kubo/0.28.0-dev/413de0f/docker` (2024-04-05 23:21:29)
- `helia/4.1.0 libp2p/1.3.2 UserAgent=v21.6.2` (2024-04-06 05:50:58)
- `kubo/0.28.0-dev/413de0f83` (2024-04-06 09:20:54)
- `goserial/libp2p-adapter@` (2024-04-06 11:51:24)
- `github.com/bahner/go-ma-actor@c8a4dcd19` (2024-04-06 17:21:06)
- `github.com/bahner/go-ma-actor@c8a4dcd19-dirty` (2024-04-06 18:22:04)
- `github.com/bahner/go-ma-actor@3ee63766b` (2024-04-06 23:21:18)
- `github.com/bahner/go-ma-actor@8ad1059e3-dirty` (2024-04-07 00:50:54)
- `github.com/bahner/go-ma-actor@1c44e9166-dirty` (2024-04-07 02:51:33)
- `foxnet/implant@` (2024-04-07 11:51:39)
- `libp2p/1.3.1 UserAgent=v20.9.0` (2024-04-07 12:51:52)
- `github.com/bahner/go-ma-actor@952a16ec6-dirty` (2024-04-07 20:29:21)
- `github.com/bahner/go-ma-actor@0ad6459f6` (2024-04-07 21:27:54)
- `github.com/bahner/go-ma-actor@d756e8bdc-dirty` (2024-04-07 22:25:09)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/orbitdb/heads/orbitdb/zdpuApZ6ZWBH3MgXbG5cn4netY9VnRBH9RKQBgAinxTHoQkb8` (2024-04-01 15:21:05)
- `/orbitdb/heads/orbitdb/zdpuAwBj7kVEaFtSSLqk2FwccarRvud46hB1D2dinNDNYMuzt` (2024-04-07 12:51:52)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 228 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `51.15.245.0` | FR | 117 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.134.20` | FR | 85 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.151.120` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | NL | 74 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `151.115.53.194` | PL | 56 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `188.165.71.178` | FR | 55 | ['kubo/0.27.0/', 'main@6238759c0-dirty']| True  |
| `51.15.245.0` | FR | 52 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-04-01` to `2024-04-08` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-04-01` to `2024-04-08` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-04-01` to `2024-04-08` in the DHT and their datacenter association.

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