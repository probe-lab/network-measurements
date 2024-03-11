# Nebula Measurement Results Calendar Week 10 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 10 - 2024](#nebula-measurement-results-calendar-week-10---2024)
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

The following results show measurement data that were collected in calendar week 10 in 2024 from `2024-03-04` to `2024-03-11`.

- Number of crawls `336`
- Number of visits `36,701,263`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `64,927`
- Number of unique peer IDs discovered in the DHT `63,309`
- Number of unique IP addresses found `88,687`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.28.0-dev/a01cc58c8-dirty/docker` (2024-03-04 10:20:54)
- `kubo/0.27.0/59bcea8/docker` (2024-03-04 10:51:00)
- `kubo/0.27.0/` (2024-03-04 12:20:41)
- `kubo/0.28.0-dev/d7fb526/docker` (2024-03-04 12:51:05)
- `kubo/0.28.0-dev/fcbdf39/docker` (2024-03-04 15:51:06)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v21.6.2` (2024-03-04 15:51:20)
- `neuron/sdk@ef87251e8-dirty` (2024-03-04 15:51:36)
- `neuron/sdk@e79f71d1c-dirty` (2024-03-04 17:21:23)
- `kubo/0.28.0-dev/fcbdf390b-dirty/docker` (2024-03-04 17:21:58)
- `neuron/sdk@433362d97-dirty` (2024-03-04 19:21:48)
- `github.com/JackalLabs/sequoia@8786c4c7c-dirty` (2024-03-04 20:51:30)
- `github.com/bahner/go-ma-actor@6cf113024-dirty` (2024-03-04 22:50:46)
- `helia/4.0.1 libp2p/1.2.3 UserAgent=v21.6.2` (2024-03-05 00:51:02)
- `kubo/0.27.0/59bcea8` (2024-03-05 01:21:00)
- `kubo/0.28.0-dev/fcbdf390b` (2024-03-05 01:50:52)
- `helia/4.0.2 libp2p/1.2.4 UserAgent=v20.9.0` (2024-03-05 04:21:26)
- `kubo/0.27.0/59bcea878` (2024-03-05 04:51:25)
- `kubo/0.28.0-dev/e22f47a/docker` (2024-03-05 09:21:10)
- `ceramic-one/0.12.0` (2024-03-05 13:51:57)
- `github.com/bahner/go-ma-actor@ac9a6e1e8-dirty` (2024-03-06 00:22:13)
- `github.com/bahner/go-ma-actor@135a975ac-dirty` (2024-03-06 01:21:21)
- `kubo/0.28.0-dev/e22f47ae4` (2024-03-06 01:21:22)
- `prox_powd@d96e9f880-dirty` (2024-03-06 07:21:18)
- `rust-libp2p-server/0.12.5` (2024-03-06 09:21:04)
- `kubo/0.28.0-dev/e22f47ae4-dirty/docker` (2024-03-06 11:21:22)
- `kubo/0.26.0/VALGRIND` (2024-03-06 13:21:47)
- `kubo/0.27.0/3fd4507-dirty` (2024-03-06 19:20:59)
- `helia/4.0.0 libp2p/1.2.1 UserAgent=v20.10.0` (2024-03-06 19:50:54)
- `github.com/bahner/go-ma-actor@b1b811df4-dirty` (2024-03-06 21:21:05)
- `kubo/0.26.0/kubernetes` (2024-03-06 22:22:06)
- `github.com/bahner/go-ma-actor@dd090f268-dirty` (2024-03-07 01:20:47)
- `prox_powd@67210460f-dirty` (2024-03-07 10:22:11)
- `prox_powd@2a0687455-dirty` (2024-03-07 11:51:54)
- `libp2p/1.2.4 UserAgent=v20.11.0` (2024-03-07 16:50:55)
- `kubo/0.27.0/59bcea8/1234567890123456789012345678901234567890` (2024-03-07 16:50:58)
- `libp2p/1.2.4 UserAgent=v19.9.0` (2024-03-07 16:51:30)
- `github.com/diadata-org/diaprotocol-node@` (2024-03-07 17:51:15)
- `kubo/0.28.0-dev/` (2024-03-07 21:21:02)
- `kubo/0.27.0/VALGRIND` (2024-03-08 08:51:11)
- `helia/4.0.0 libp2p/1.2.1 UserAgent=v18.17.0` (2024-03-08 08:51:19)
- `kubo/0.23.0/a7c651849` (2024-03-08 13:21:47)
- `github.com/bahner/go-ma-actor@2204818b0-dirty` (2024-03-08 17:22:18)
- `go-btfs/2.3.4/a5500e3` (2024-03-08 20:21:34)
- `github.com/bahner/go-ma-actor@ec87d7881-dirty` (2024-03-08 21:50:51)
- `github.com/bahner/go-ma-actor@0e3c84009` (2024-03-08 23:51:16)
- `kubo/0.28.0-dev/e22f47ae4-dirty` (2024-03-09 03:52:06)
- `github.com/bahner/go-ma-actor@434d2647a-dirty` (2024-03-09 04:21:30)
- `github.com/bahner/go-ma-actor@0cfe4c40d-dirty` (2024-03-09 05:50:59)
- `github.com/bahner/go-ma-actor@3da5050d3-dirty` (2024-03-09 05:51:24)
- `github.com/bahner/go-ma-actor@3da5050d3` (2024-03-09 08:51:09)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/ceramic/recon/0.1.0/interest` (2024-03-05 13:51:57)
- `/ceramic/recon/0.1.0/model` (2024-03-05 13:51:58)
- `/space-data-network/id-exchange/1.0.0` (2024-03-05 22:22:12)
- `/jerry9999mars/kad/1.0.0` (2024-03-06 10:21:04)
- `/orbitdb/heads/orbitdb/zdpuAnpE1vd6s4eixzijkTWhdmNEFrL1puyXNViu5DBbKqAo5` (2024-03-06 19:50:54)
- `hivetrain-z_grad_averager::GradientAverager.rpc_download_state` (2024-03-09 06:21:29)
- `hivetrain-z_state_averager::TrainingStateAverager.rpc_download_state` (2024-03-09 06:21:29)
- `hivetrain-z_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-03-09 06:21:29)
- `hivetrain-z_grad_averager::GradientAverager.rpc_aggregate_part` (2024-03-09 06:21:29)
- `hivetrain-z_state_averager::TrainingStateAverager.rpc_join_group` (2024-03-09 06:21:29)
- `hivetrain-z_grad_averager::GradientAverager.rpc_join_group` (2024-03-09 06:21:30)
- `hiveminer_grad_averager::GradientAverager.rpc_download_state` (2024-03-09 22:20:53)
- `hiveminer_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-03-09 22:20:53)
- `hiveminer_grad_averager::GradientAverager.rpc_aggregate_part` (2024-03-09 22:20:53)
- `hiveminer_state_averager::TrainingStateAverager.rpc_join_group` (2024-03-09 22:20:53)
- `hiveminer_state_averager::TrainingStateAverager.rpc_download_state` (2024-03-09 22:20:53)
- `hiveminer_grad_averager::GradientAverager.rpc_join_group` (2024-03-09 22:20:53)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 219 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `51.15.230.142` | FR | 116 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `212.47.234.38` | FR | 111 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.134.20` | FR | 84 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | NL | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.201.219` | FR | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `172.33.1.5` | US | 73 | ['kubo/0.19.1/', 'kubo/0.22.0/3f884d3/docker']| False  |
| `51.159.151.120` | FR | 72 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-03-04` to `2024-03-11` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-03-04` to `2024-03-11` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-03-04` to `2024-03-11` in the DHT and their datacenter association.

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