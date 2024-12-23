# Nebula Measurement Results Calendar Week 51 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 51 - 2024](#nebula-measurement-results-calendar-week-51---2024)
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

The following results show measurement data that were collected in calendar week 51 in 2024 from `2024-12-16` to `2024-12-23`.

- Number of crawls `84`
- Number of visits `9,960,009`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `47,249`
- Number of unique peer IDs discovered in the DHT `46,157`
- Number of unique IP addresses found `39,609`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/functionland/go-fula@286e8f535` (2024-12-16 00:01:16)
- `bootnode-20241215200815` (2024-12-16 00:01:18)
- `github.com/jimmale/jcs@e976d6502-dirty` (2024-12-16 00:01:20)
- `kubo/0.32.1/9017453/aya-myos-local` (2024-12-16 02:01:44)
- `js-libp2p/0.0.0 UserAgent=v22.11.0` (2024-12-16 12:02:08)
- `kubo/0.33.0-dev/07b874217` (2024-12-16 14:01:15)
- `bootnode-20241217033633` (2024-12-17 04:01:20)
- `kubo/0.29.0/docker` (2024-12-17 06:01:29)
- `bootnode-20241217103322` (2024-12-17 14:01:21)
- `bootnode-20241217161351` (2024-12-17 18:01:15)
- `ipfsUploader@429ebd1f5-dirty` (2024-12-17 20:01:23)
- `js-libp2p/2.4.2 UserAgent=v22.11.0` (2024-12-17 20:01:27)
- `kubo/0.33.0-dev/898f024f3` (2024-12-18 04:01:34)
- `p2proxy@db30fe917-dirty` (2024-12-18 14:01:39)
- `bootnode-20241218022430` (2024-12-18 16:01:28)
- `bootnode-20241218163459` (2024-12-18 20:01:24)
- `kubo/0.33.0-dev/d178b8745` (2024-12-19 02:01:38)
- `kubo/0.33.0-dev/898f024/docker` (2024-12-19 06:01:50)
- `github.com/probe-lab/ants-watch@` (2024-12-19 14:01:04)
- `kubo/0.33.0-dev/898f024` (2024-12-19 22:01:21)
- `helia/5.1.1 js-libp2p/2.4.2 UserAgent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36` (2024-12-20 00:01:10)
- `kubo/0.33.0-dev/295fd96/docker` (2024-12-20 00:01:41)
- `kubo/0.33.0-dev/ecb2558/docker` (2024-12-20 00:01:47)
- `kubo/0.33.0-dev/f2c1905/docker` (2024-12-20 02:01:15)
- `github.com/JackalLabs/sequoia@84abf8e45` (2024-12-20 04:01:12)
- `MessageMesh@2e393962b-dirty` (2024-12-20 10:02:17)
- `bootnode-20241220103525` (2024-12-20 12:01:15)
- `kubo/0.33.0-dev/2919d6d/1234567890123456789012345678901234567890` (2024-12-20 16:01:26)
- `kubo/0.33.0-dev/f2c190535` (2024-12-20 18:02:00)
- `bootnode-20241220161236` (2024-12-20 20:02:04)
- `kubo/0.33.0-rc1/1b5aa0b` (2024-12-21 00:02:05)
- `kubo/0.33.0-rc1/` (2024-12-21 06:01:28)
- `bootnode-20241221012545` (2024-12-21 08:01:41)
- `github.com/p2pdao/libp2p-proxy@0fde7823f-dirty` (2024-12-21 14:01:14)
- `github.com/manishmeganathan/peerchat@be689bf10-dirty` (2024-12-21 18:01:09)
- `github.com/manishmeganathan/peerchat@3af239c47-dirty` (2024-12-21 20:01:39)
- `github.com/manishmeganathan/peerchat@2add1b686-dirty` (2024-12-21 22:01:24)
- `github.com/manishmeganathan/peerchat@7bc536fe7-dirty` (2024-12-22 02:01:12)
- `github.com/manishmeganathan/peerchat@d1560c693-dirty` (2024-12-22 02:01:40)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `jcs` (2024-12-16 00:01:20)
- `/defs/handshake/1.0.0` (2024-12-21 10:01:20)
- `/orbitdb/heads/orbitdb/zdpuAtyhrLZwfxgH4SPTRbm19iaNPFguYi4YTTc5dPcmSxScf` (2024-12-21 10:01:57)
- `/orbitdb/heads/orbitdb/zdpuAukcnhxNYjizGgx4cZvrh5u7nng24osQKNi1GvHEHjdyd` (2024-12-21 10:01:57)
- `/orbitdb/heads/orbitdb/zdpuAztie7e2YbD6R2vG5MAMa6XB6qZDqUJxPVbj7JRuMYVyQ` (2024-12-21 14:01:56)
- `/orbitdb/heads/orbitdb/zdpuArEZhyfyDBCwmCky8ecdCKt7nzKHpgXoTAcDbTQ3nLGaz` (2024-12-21 16:01:32)
- `/orbitdb/heads/orbitdb/zdpuAnXRXP8fjGg6V1CWhcH6H6UefVGoTE13zZHchUvPZQyZ8` (2024-12-21 16:01:32)
- `/orbitdb/heads/orbitdb/zdpuAypvn3s2iYdKCoEJxLAw9Va1EHH9jeW4ipd6PiScKQJbn` (2024-12-21 16:01:39)
- `/orbitdb/heads/orbitdb/zdpuAsMDHwjupqm9o2Q7xoAs9o9c9wFpWNduZsQa5nZ3MfcNA` (2024-12-21 16:01:39)
- `/p2pdao/libp2p-proxy/1.0.0` (2024-12-21 22:01:24)
- `/p2pdao/libp2p-ssh/1.0.0` (2024-12-21 22:01:24)
- `/p2pdao/libp2p-podman/1.0.0` (2024-12-21 22:01:24)
- `/address-exchange/1.0.0` (2024-12-22 04:01:43)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `152.81.47.227` | FR | 72 | ['kubo/0.32.0/']| False  |
| `2001:41d0:8:926e::1` | FR | 52 | ['edgevpn']| True  |
| `5.39.80.110` | FR | 52 | ['edgevpn']| True  |
| `143.110.168.61` | GB | 51 | ['kubo/0.29.0/3f0947b', 'kubo/0.30.0/']| True  |
| `91.230.153.86` | RU | 35 | ['edgevpn']| False  |
| `139.59.6.4` | IN | 25 | ['kubo/0.29.0/3f0947b']| True  |
| `123.181.15.58` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `123.181.15.198` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `2.50.224.180` | AE | 18 | ['edgevpn']| False  |
| `31.170.191.49` | RU | 18 | ['go-ipfs/0.8.0/48f94e2']| False  |

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

In the specified time interval from `2024-12-16` to `2024-12-23` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-12-16` to `2024-12-23` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-12-16` to `2024-12-23` in the DHT and their datacenter association.

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