# Nebula Measurement Results Calendar Week 3 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 3 - 2024](#nebula-measurement-results-calendar-week-3---2024)
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

The following results show measurement data that were collected in calendar week 3 in 2024 from `2024-01-15` to `2024-01-22`.

- Number of crawls `336`
- Number of visits `44,344,808`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `68,336`
- Number of unique peer IDs discovered in the DHT `66,337`
- Number of unique IP addresses found `87,809`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.27.0-dev/982d8a9` (2024-01-15 06:21:33)
- `go-ipfs/0.11.0-dev/6a10c1d` (2024-01-15 06:22:41)
- `neuron/sdk@8f0168a46-dirty` (2024-01-15 09:21:39)
- `kubo/0.18.0-rc2/docker` (2024-01-15 10:52:38)
- `helia/3.0.1 libp2p/1.1.2 UserAgent=v20.11.0` (2024-01-15 12:21:38)
- `github.com/INFURA/ipfs-p2p-server@` (2024-01-15 15:51:00)
- `js-libp2p/0.45.9 UserAgent=v18.18.2` (2024-01-15 18:21:34)
- `neuron/sdk@9f8e872e5-dirty` (2024-01-15 22:21:12)
- `kubo/0.24.0-dev/a4efea5c7` (2024-01-15 22:52:29)
- `kubo/0.26.0-rc1/b3c251a/thunderdome` (2024-01-16 10:20:56)
- `kubo/0.25.0/413a52d/thunderdome` (2024-01-16 10:21:44)
- `github.com/hsanjuan/ipfs-lite@` (2024-01-16 11:51:11)
- `helia/3.0.1 libp2p/1.2.0 UserAgent=v20.11.0` (2024-01-16 12:22:27)
- `kubo/0.25.0/e70db6531` (2024-01-16 13:21:20)
- `kubo/0.27.0-dev/e11d7b0/docker` (2024-01-16 17:21:02)
- `helia/3.0.1 libp2p/1.2.0 UserAgent=v21.5.0` (2024-01-16 17:21:20)
- `neuron/sdk@14bb37d9d` (2024-01-16 22:22:46)
- `kubo/0.25.0/docker` (2024-01-17 04:21:04)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.2.0` (2024-01-17 04:51:08)
- `kubo/0.27.0-dev/e11d7b0c1-dirty` (2024-01-17 08:51:22)
- `helia/3.0.1 libp2p/1.2.0 UserAgent=v20.10.0` (2024-01-17 15:21:05)
- `kubo/0.27.0-dev/c0d7da2/docker` (2024-01-17 15:22:25)
- `kubo/0.26.0-rc1/b3c251a/1234567890123456789012345678901234567890` (2024-01-17 15:51:49)
- `kubo/0.27.0-dev/c0d7da22a` (2024-01-18 02:52:13)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v18.18.2` (2024-01-18 03:52:33)
- `bootstrap-node` (2024-01-18 09:21:32)
- `kubo/0.27.0-dev/e11d7b0c1-dirty/docker` (2024-01-18 09:51:40)
- `kubo/0.23.0/3a1a0413a-dirty/docker` (2024-01-18 13:51:57)
- `libp2p/1.2.0 UserAgent=v21.6.0` (2024-01-19 07:21:15)
- `kubo/0.27.0-dev/4790618a2` (2024-01-19 12:21:18)
- `helia/3.0.1 libp2p/1.2.0 UserAgent=v21.2.0` (2024-01-19 17:21:09)
- `kubo/0.27.0-dev/4790618/docker` (2024-01-19 18:51:01)
- `kubo/0.18.1/fb7f7b15b-dirty` (2024-01-19 22:51:12)
- `kubo/0.22.0-dev/4c3528955` (2024-01-19 23:21:55)
- `helia/3.0.1 libp2p/1.2.0 UserAgent=v18.17.1` (2024-01-20 17:51:56)
- `SecuraChain` (2024-01-21 15:52:26)
- `github.com/multiverse-vcs/go-multiverse` (2024-01-21 16:50:51)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `vtx-src-frame_grad_averager::GradientAverager.rpc_aggregate_part` (2024-01-15 20:21:08)
- `vtx-src-frame_grad_averager::GradientAverager.rpc_join_group` (2024-01-15 20:21:08)
- `vtx-src-frame_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-01-15 20:21:08)
- `vtx-src-frame_grad_averager::GradientAverager.rpc_download_state` (2024-01-15 20:21:08)
- `vtx-src-frame_state_averager::TrainingStateAverager.rpc_download_state` (2024-01-15 20:21:08)
- `vtx-src-frame_state_averager::TrainingStateAverager.rpc_join_group` (2024-01-15 20:21:08)
- `/nrn-adsb/1.0.0` (2024-01-15 22:21:12)
- `vtx-src-src_grad_averager::GradientAverager.rpc_aggregate_part` (2024-01-15 23:51:15)
- `vtx-src-src_state_averager::TrainingStateAverager.rpc_download_state` (2024-01-15 23:51:15)
- `vtx-src-src_grad_averager::GradientAverager.rpc_join_group` (2024-01-15 23:51:15)
- `vtx-src-src_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-01-15 23:51:15)
- `vtx-src-src_state_averager::TrainingStateAverager.rpc_join_group` (2024-01-15 23:51:15)
- `vtx-src-src_grad_averager::GradientAverager.rpc_download_state` (2024-01-15 23:51:15)
- `vtx-frame_grad_averager::GradientAverager.rpc_aggregate_part` (2024-01-16 02:51:08)
- `vtx-frame_grad_averager::GradientAverager.rpc_join_group` (2024-01-16 02:51:08)
- `vtx-frame_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-01-16 02:51:08)
- `vtx-frame_state_averager::TrainingStateAverager.rpc_join_group` (2024-01-16 02:51:08)
- `vtx-frame_grad_averager::GradientAverager.rpc_download_state` (2024-01-16 02:51:08)
- `vtx-frame_state_averager::TrainingStateAverager.rpc_download_state` (2024-01-16 02:51:08)
- `/bitcoin-stn/alert-system/0.0.1` (2024-01-16 04:22:00)
- `/ipfs-onion/nf-PSnet/1.0.0/chat` (2024-01-17 03:22:31)
- `/ipfs-onion/nf-PSnet/1.0.0/file-trans` (2024-01-17 03:22:31)
- `/ipfs-onion/nf-PSnet/1.0.0/packet` (2024-01-17 03:22:31)
- `/ipfs-onion/nf-PSnet/1.0.0/discovery` (2024-01-17 03:22:31)
- `/ipfs-onion/nf-PSnet/1.0.0/protoOnionConn` (2024-01-17 03:22:31)
- `/tss/keySign/session/d5747d38-b5c6-11ee-9f0d-0242c0a60a78` (2024-01-18 06:21:18)
- `/tss/keySign/session/c3b25f09-b5c9-11ee-8b32-0242c0a60a78` (2024-01-18 06:21:18)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `172.33.1.5` | US | 456 | ['go-ipfs/0.12.1/', 'kubo/0.15.0/3ae52a4', 'kubo/0.19.1/', 'kubo/0.22.0/3f884d3/docker', 'kubo/0.25.0/413a52d/docker']| False  |
| `159.203.76.161` | US | 188 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `51.15.128.68` | FR | 97 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.128.68` | IN | 97 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `212.47.234.38` | FR | 96 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.129.249` | FR | 84 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 61 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 56 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 56 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 56 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-01-15` to `2024-01-22` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-01-15` to `2024-01-22` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-01-15` to `2024-01-22` in the DHT and their datacenter association.

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