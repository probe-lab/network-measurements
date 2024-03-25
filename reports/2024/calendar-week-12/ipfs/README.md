# Nebula Measurement Results Calendar Week 12 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 12 - 2024](#nebula-measurement-results-calendar-week-12---2024)
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

The following results show measurement data that were collected in calendar week 12 in 2024 from `2024-03-18` to `2024-03-25`.

- Number of crawls `336`
- Number of visits `37,711,513`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `63,274`
- Number of unique peer IDs discovered in the DHT `61,840`
- Number of unique IP addresses found `88,751`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.28.0-dev/54d7edc-dirty` (2024-03-18 01:21:21)
- `kubo/0.28.0-dev/53d1221` (2024-03-18 05:51:29)
- `kubo/0.25.0/a0b65cb-dirty` (2024-03-18 05:52:06)
- `github.com/0xsequence/bundler@bcaab5948-dirty` (2024-03-18 13:51:34)
- `vulpine_serv@` (2024-03-18 16:20:52)
- `neuron/sdk@996259355-dirty` (2024-03-18 21:22:05)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v18.19.1` (2024-03-18 22:51:47)
- `kubo/0.23.0/322604b9f-dirty` (2024-03-19 03:51:09)
- `github.com/bahner/go-ma-actor@c39a51775` (2024-03-19 05:50:53)
- `github.com/bahner/go-ma-actor@22eb7c4ad-dirty` (2024-03-19 10:20:44)
- `kubo/0.28.0-dev/9a5f5e7/docker` (2024-03-19 12:21:09)
- `kubo/0.28.0-dev/21728eb/docker` (2024-03-19 18:51:18)
- `ceramic-one/0.13.0` (2024-03-19 19:50:57)
- `kubo/0.27.0-rc1/e6c7032ab` (2024-03-20 01:22:04)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v20.11.1` (2024-03-20 19:20:52)
- `github.com/bahner/go-ma-actor@ebee0f92e` (2024-03-20 21:51:29)
- `go-ipfs/0.13.0-dev/d5ad847e0` (2024-03-21 02:50:44)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v18.19.0` (2024-03-21 10:51:37)
- `neuron/sdk@605999186-dirty` (2024-03-21 12:21:42)
- `kubo/0.27.0/e10e42acd-dirty` (2024-03-21 12:51:07)
- `kubo/0.27.0/0402ec314-dirty` (2024-03-21 17:51:10)
- `kubo/0.28.0-dev/7daa23c0d-dirty` (2024-03-21 20:21:37)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v21.4.0` (2024-03-21 22:21:18)
- `github.com/bitcoin-sv/alert-system@0f10bb85c` (2024-03-21 23:20:46)
- `github.com/0xsequence/bundler@56fa088f5-dirty` (2024-03-22 00:21:03)
- `kubo/0.28.0-dev/21728eb00-dirty/docker` (2024-03-22 03:21:00)
- `helia/4.1.0 libp2p/1.3.0 UserAgent=v18.14.2` (2024-03-22 07:51:10)
- `github.com/zzz136454872/upgradeable-consensus@9a0fc5c22-dirty` (2024-03-22 13:51:08)
- `github.com/0xsequence/bundler@622f494e6` (2024-03-22 14:51:47)
- `kubo/0.28.0-dev/9047fed8d-dirty` (2024-03-22 17:21:17)
- `github.com/bitcoin-sv/alert-system@0f10bb85c-dirty` (2024-03-22 17:50:49)
- `kubo/0.28.0-dev/21728eb` (2024-03-23 12:51:55)
- `Chainflip Node/v1.2.1-ccfcb7e07a8 (bite-sized-border-2072)` (2024-03-23 15:20:43)
- `github.com/bahner/go-ma-actor@caf13f494-dirty` (2024-03-23 17:50:53)
- `SybilNode@ca43010bf-dirty` (2024-03-23 18:50:50)
- `pubsub@` (2024-03-24 09:51:30)
- `github.com/bahner/go-ma-actor@93889396a-dirty` (2024-03-24 15:21:21)
- `kubo/0.28.0-dev/9047fed/docker` (2024-03-24 23:51:50)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/sdn/pingpong/1.0.0` (2024-03-21 17:51:10)
- `/ceramic/kad` (2024-03-21 18:21:00)
- `/ceramic/kad/1.0.0` (2024-03-21 19:21:16)
- `/consensus/1.0.0` (2024-03-22 13:51:08)
- `/orbitdb/heads/orbitdb/zdpuB2uee6PgXhXExsyPjFUWBFfCcpjp5EuoH5tzeiZFbjY7e` (2024-03-22 20:51:21)
- `/orbitdb/heads/orbitdb/zdpuAn1iF6cdfN6TjDqtdca8JRhZ8KoYuW4c5njenfz3JukSm` (2024-03-22 23:21:38)
- `/flip-pers-2-65e960c4/transactions/1` (2024-03-23 15:20:43)
- `/7a5d4db858ada1d20ed6ded4933c33313fc9673e5fffab560d0ca714782f2080/light/2` (2024-03-23 15:20:43)
- `/flip-pers-2-65e960c4/light/2` (2024-03-23 15:20:43)
- `/7a5d4db858ada1d20ed6ded4933c33313fc9673e5fffab560d0ca714782f2080/sync/warp` (2024-03-23 15:20:43)
- `/7a5d4db858ada1d20ed6ded4933c33313fc9673e5fffab560d0ca714782f2080/sync/2` (2024-03-23 15:20:43)
- `/flip-pers-2-65e960c4/state/2` (2024-03-23 15:20:43)
- `/7a5d4db858ada1d20ed6ded4933c33313fc9673e5fffab560d0ca714782f2080/transactions/1` (2024-03-23 15:20:43)
- `/flip-pers-2-65e960c4/kad` (2024-03-23 15:20:43)
- `/flip-pers-2-65e960c4/sync/warp` (2024-03-23 15:20:43)
- `/flip-pers-2-65e960c4/sync/2` (2024-03-23 15:20:43)
- `/7a5d4db858ada1d20ed6ded4933c33313fc9673e5fffab560d0ca714782f2080/block-announces/1` (2024-03-23 15:20:43)
- `/7a5d4db858ada1d20ed6ded4933c33313fc9673e5fffab560d0ca714782f2080/grandpa/1` (2024-03-23 15:20:43)
- `/7a5d4db858ada1d20ed6ded4933c33313fc9673e5fffab560d0ca714782f2080/kad` (2024-03-23 15:20:43)
- `/7a5d4db858ada1d20ed6ded4933c33313fc9673e5fffab560d0ca714782f2080/state/2` (2024-03-23 15:20:43)
- `/flip-pers-2-65e960c4/block-announces/1` (2024-03-23 15:20:43)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 224 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `141.95.151.126` | FR | 121 | ['kubo/0.27.0/', 'kubo/0.28.0-dev/', 'SybilNode@']| False  |
| `51.159.134.20` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 69 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 69 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `172.33.1.5` | US | 69 | ['kubo/0.19.1/', 'kubo/0.22.0/3f884d3/docker']| False  |
| `51.15.201.219` | FR | 63 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `90.116.141.211` | FR | 56 | ['kubo/0.26.0/brave', 'kubo/0.27.0/', 'SybilNode@']| False  |
| `51.159.151.120` | FR | 54 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.245.0` | FR | 53 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-03-18` to `2024-03-25` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-03-18` to `2024-03-25` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-03-18` to `2024-03-25` in the DHT and their datacenter association.

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