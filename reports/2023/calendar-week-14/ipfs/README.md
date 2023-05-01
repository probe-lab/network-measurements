# Nebula Measurement Results Calendar Week 14 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 14 - 2023](#nebula-measurement-results-calendar-week-14---2023)
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

The following results show measurement data that were collected in calendar week 14 in 2023 from `2023-04-03` to `2023-04-10`.

- Number of crawls `336`
- Number of visits `43,835,102`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `46,151`
- Number of unique peer IDs discovered in the DHT `46,049`
- Number of unique IP addresses found `51,806`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/mearaj/protonet@8660b3ae5-dirty` (2023-04-03 05:53:38)
- `kubo/0.20.0-dev/d1713ca/docker` (2023-04-03 10:52:08)
- `go.vocdoni.io/dvote@301f524b4-dirty` (2023-04-03 11:22:15)
- `github.com/dennis-tra/parsec@c9a441937-dirty` (2023-04-03 12:51:13)
- `github.com/mearaj/protonet@fed5655c5-dirty` (2023-04-03 12:51:25)
- `go-ipfs/0.10.0-rc2/` (2023-04-03 13:22:35)
- `gitlab.com/nunet/bootstrap-node-v2@` (2023-04-03 15:21:50)
- `delta@bb7da0297` (2023-04-03 19:51:09)
- `github.com/mearaj/protonet@d0a4625fa-dirty` (2023-04-03 20:23:10)
- `kubo/0.18.1/b72194ecc` (2023-04-03 21:53:35)
- `delta@f2beb58bc` (2023-04-03 22:21:07)
- `delta@9790ef67e-dirty` (2023-04-04 03:51:11)
- `github.com/mearaj/protonet@3c754c65e` (2023-04-04 03:52:33)
- `github.com/mearaj/protonet@3c754c65e-dirty` (2023-04-04 04:23:14)
- `delta@a1ce43cfd-dirty` (2023-04-04 04:51:16)
- `github.com/mearaj/protonet@03d097ba8-dirty` (2023-04-04 04:52:53)
- `kubo/0.20.0-dev/68ee5e61a` (2023-04-04 07:51:17)
- `kubo/0.20.0-dev/68ee5e6/docker` (2023-04-04 09:52:00)
- `node` (2023-04-04 09:53:27)
- `kubo/0.20.0-dev/715707b/docker` (2023-04-04 13:22:44)
- `spook@30869d5c0-dirty` (2023-04-04 15:22:57)
- `kubo/0.20.0-dev/68ee5e61a-dirty` (2023-04-04 17:23:37)
- `delta@edb652e2a` (2023-04-04 19:51:14)
- `kubo/0.20.0-dev/027c5b1/docker` (2023-04-04 19:53:18)
- `kubo/0.20.0-dev/027c5b1a0-dirty` (2023-04-04 20:51:22)
- `0.9.1` (2023-04-05 09:23:05)
- `kubo/0.20.0-dev/ccbd476e5-dirty` (2023-04-05 09:23:13)
- `gitlab.com/nunet/bootstrap-node` (2023-04-05 10:51:36)
- `kubo/0.20.0-dev/fd830b3/docker` (2023-04-05 12:21:28)
- `kubo/0.20.0-dev/0ec22f4/docker` (2023-04-05 13:51:47)
- `github.com/mearaj/protonet@24d9a7527` (2023-04-05 14:21:09)
- `kubo/0.19.1/958e586/docker` (2023-04-05 17:22:02)
- `github.com/mearaj/protonet@4162faf31-dirty` (2023-04-05 20:51:13)
- `kubo/0.19.1/` (2023-04-05 21:22:20)
- `github.com/mearaj/protonet@6c235cb9a-dirty` (2023-04-05 22:22:42)
- `github.com/mearaj/protonet@2db20ddbe-dirty` (2023-04-05 23:21:18)
- `kubo/0.19.1/desktop` (2023-04-05 23:51:47)
- `kubo/0.19.1/958e586` (2023-04-06 01:24:08)
- `github.com/mearaj/protonet@2c45a518d-dirty` (2023-04-06 02:51:11)
- `github.com/mearaj/protonet@f84e575e0-dirty` (2023-04-06 03:22:33)
- `github.com/mearaj/protonet@6e78eb398-dirty` (2023-04-06 04:22:07)
- `github.com/dennis-tra/parsec@b4bce31d8-dirty` (2023-04-06 08:23:21)
- `kubo/0.19.1/958e586ca` (2023-04-06 08:54:10)
- `github.com/dennis-tra/parsec@c1b28a41b-dirty` (2023-04-06 09:21:19)
- `kubo/0.20.0-dev/1958510/docker` (2023-04-06 12:52:15)
- `kubo/0.19.1/958e586/filebase` (2023-04-06 14:51:22)
- `kubo/0.20.0-dev/c6a59c9/docker` (2023-04-06 16:22:25)
- `github.com/mearaj/protonet@27d7ee9ad-dirty` (2023-04-06 18:23:44)
- `github.com/mearaj/protonet@8b6904f42-dirty` (2023-04-07 06:22:31)
- `kubo/0.20.0-dev/e89cce63f-dirty` (2023-04-07 08:52:39)
- `kubo/0.21.0-dev/c58aadb/docker` (2023-04-07 09:21:37)
- `delta@ef6ea94c5-dirty` (2023-04-07 11:51:12)
- `github.com/mearaj/protonet@7b3db6e0e-dirty` (2023-04-07 12:51:18)
- `github.com/mearaj/protonet@1456c5a7b-dirty` (2023-04-07 13:22:24)
- `github.com/mearaj/protonet@10493736b` (2023-04-07 14:23:01)
- `kubo/0.20.0-rc1/ff409cc/s̳̪̦̩̝͎͙͝u͍̫̺̝̱̰͝p̠͔̫͓̬̦` (2023-04-07 16:22:36)
- `kubo/0.19.1/VALGRIND` (2023-04-07 17:22:07)
- `delta@ef6ea94c5` (2023-04-07 18:51:08)
- `main@5078dd95d-dirty` (2023-04-08 01:23:22)
- `github.com/mearaj/protonet@5713e18a9` (2023-04-08 05:52:15)
- `github.com/mearaj/protonet@5713e18a9-dirty` (2023-04-08 10:21:50)
- `github.com/mearaj/protonet@04d6bba23-dirty` (2023-04-08 16:52:23)
- `github.com/mearaj/protonet@501a5e016-dirty` (2023-04-08 17:52:33)
- `kubo/0.20.0-rc1/` (2023-04-08 19:21:25)
- `github.com/mearaj/protonet@ea3135f5d-dirty` (2023-04-08 21:52:51)
- `github.com/mearaj/protonet@c90ad245d-dirty` (2023-04-08 22:22:33)
- `github.com/mearaj/protonet@8d78e4be9-dirty` (2023-04-08 22:52:31)
- `github.com/mearaj/protonet@ca8b5037e-dirty` (2023-04-09 12:52:44)
- `github.com/mearaj/protonet@cfc356e26-dirty` (2023-04-09 13:22:31)
- `SybilNode@f69d6f031-dirty` (2023-04-09 15:21:20)
- `github.com/mearaj/protonet@bb2be1097` (2023-04-09 20:52:33)
- `github.com/mearaj/protonet@bb2be1097-dirty` (2023-04-09 21:22:29)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/custom-node/0.1.0` (2023-04-04 09:53:27)
- `/protonet.wallet/msg-chat/0.0.1` (2023-04-05 14:21:09)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `193.60.241.97` | GB | 800 | ['kubo/0.16.0-dev/b6b97d90a', 'SybilNode@adb4f469a-dirty', 'SybilNode@f69d6f031-dirty']| False  |
| `54.187.21.48` | US | 763 | ['kubo/0.17.0/4485d6b71', 'main@5078dd95d-dirty', 'SybilNode@ef7cf7ce7-dirty']| True  |
| `159.203.76.161` | US | 272 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `193.60.241.98` | GB | 194 | ['hydra-booster/0.7.4', 'kubo/0.15.0/3ae52a41e', 'SybilNode@d54ece3ca-dirty']| False  |
| `117.174.25.136` | CN | 63 | ['go-ipfs/0.8.0/cc95853']| False  |
| `111.9.31.185` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.208` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.137` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `117.174.25.135` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |
| `183.222.63.181` | CN | 62 | ['go-ipfs/0.8.0/cc95853']| False  |

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

![DHT Server vs. Clients](./plots/dht-servers-vs-clients.png)

- DHT Server peers: unique peers that we found with our network crawls
- DHT Client peers: unique peers that we saw from our bootstrapper/preload nodes minus DHT Server peers


#### Errors

![Crawl Errors](./plots/crawl-errors.png)

#### Total Peer IDs Discovered Classification

![Peer count by classification](./plots/peer-classifications.png)

In the specified time interval from `2023-04-03` to `2023-04-10` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-04-03` to `2023-04-10` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-04-03` to `2023-04-10` in the DHT and their datacenter association.

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

**TODO**: As soon as we have more than two full weeks of data we'll report weekly graphs.

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
