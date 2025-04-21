# Nebula Measurement Results Calendar Week 15 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 15 - 2025](#nebula-measurement-results-calendar-week-15---2025)
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

The following results show measurement data that were collected in calendar week 15 in 2025 from `2025-04-14` to `2025-04-21`.

- Number of crawls `84`
- Number of visits `9,483,036`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `61,262`
- Number of unique peer IDs discovered in the DHT `60,893`
- Number of unique IP addresses found `44,565`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `my-test-app-123ABC/0.0.1` (2025-04-14 00:01:10)
- `bootnode-20250413220711` (2025-04-14 00:01:36)
- `js-libp2p/2.8.3 node/22.2.0` (2025-04-14 04:01:14)
- `kubo/0.35.0-dev/d7f026606` (2025-04-14 08:02:07)
- `js-libp2p/2.8.3 node/23.3.0` (2025-04-14 10:01:57)
- `js-libp2p/2.8.3 node/22.14.0` (2025-04-14 12:01:42)
- `github.com/JackalLabs/sequoia@8a5ef5117` (2025-04-14 14:01:21)
- `bootnode-20250414082857` (2025-04-14 14:01:28)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250414130137-8a5ef5117508` (2025-04-14 14:01:47)
- `bootnode-20250414154230` (2025-04-14 14:02:00)
- `github.com/harmony-one/harmony@v1.10.3-0.20250414123840-8a7e6eabad12` (2025-04-14 16:01:14)
- `bootnode-20250414162418` (2025-04-14 16:01:19)
- `js-libp2p/2.8.2 node/22.14.0` (2025-04-14 16:01:32)
- `bootnode-20250414162321` (2025-04-14 16:01:39)
- `bootnode-20250415100733` (2025-04-15 10:01:17)
- `kubo/0.34.0-dev/d137d7a4a-dirty` (2025-04-15 10:01:41)
- `bootnode-20250415113505` (2025-04-15 12:01:18)
- `helia/5.3.0 js-libp2p/2.7.2 node/20.18.3` (2025-04-15 18:01:20)
- `github.com/bradanzie/dqmp@v0.0.0-20250415115220-10f4c7ef6ecb+dirty` (2025-04-15 18:01:46)
- `kubo/0.35.0-dev/6b55e64/docker` (2025-04-16 00:01:46)
- `bootnode-20250416071639` (2025-04-16 08:01:19)
- `bootnode-20250416115108` (2025-04-16 10:01:13)
- `bootnode-20250416133535` (2025-04-16 12:01:54)
- `bootnode-20250416141136` (2025-04-16 14:01:25)
- `bootnode-20250416071006` (2025-04-16 14:01:43)
- `bootnode-20250416155726` (2025-04-16 14:02:05)
- `kubo/0.35.0-dev/05d0bb3` (2025-04-16 16:01:45)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250415133050-b25c22fa8217` (2025-04-16 22:01:48)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250417020000-81012856420f` (2025-04-17 02:01:25)
- `@libp2p/amino-dht-bootstrapper/1.9.3 js-libp2p/2.8.4 node/22.14.0` (2025-04-17 10:01:13)
- `bootnode-20250417115921` (2025-04-17 10:01:14)
- `bootnode-20250417045528` (2025-04-17 10:01:18)
- `bootnode-20250417120003` (2025-04-17 10:01:34)
- `github.com/JackalLabs/sequoia@810128564` (2025-04-17 14:01:47)
- `helia/5.3.0 js-libp2p/2.8.4 node/20.18.1` (2025-04-18 04:01:25)
- `github.com/JackalLabs/sequoia@7e22926c5` (2025-04-18 06:01:44)
- `github.com/iracding/ogma/dhtServer@` (2025-04-18 08:01:21)
- `ca-vsc@v0.0.0-20250416142454-2b2ebd211520` (2025-04-18 14:01:54)
- `kubo/0.34.1/docker` (2025-04-19 02:01:12)
- `bootnode-20250419030359` (2025-04-19 04:01:22)
- `kubo/0.35.0-dev/6b55e6491-dirty` (2025-04-19 18:01:45)
- `github.com/JackalLabs/sequoia@7e22926c5-dirty` (2025-04-20 08:01:41)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `ModuleServicer.rpc_backward_module` (2025-04-14 14:01:37)
- `ModuleServicer.rpc_backward_module_stream` (2025-04-14 14:01:37)
- `ModuleServicer.rpc_forward_module` (2025-04-14 14:01:37)
- `ModuleServicer.rpc_forward_module_stream` (2025-04-14 14:01:37)
- `/orbitdb/heads/orbitdb/zdpuArQNYHkBeR5oEQ34vRkiCtXeyL1FffCAmu7yQoQr6vdYV` (2025-04-14 16:01:32)
- `/orbitdb/heads/orbitdb/zdpuAw2tuFtjfVWVM5BkD7yiRnayf2NneH9sDKxuXhfKcqop9` (2025-04-14 16:01:32)
- `/orbitdb/heads/orbitdb/zdpuB1XwnZKqga3XNBeJXquJhTJ6AE7XNigBLMQm4D88PJjWE` (2025-04-14 16:01:32)
- `/orbitdb/heads/orbitdb/zdpuAoUx1yR237dhJ3ZDZkiSQafkqQbktNqoLktnEvjniozZX` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAsx6ytECtNDVRh3JtirjbiF8uiFenxj9k4aMQ2JKBWTkb` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAtCvdpzknhQfqY2k13FD9hJ4DJ2Pz2Vaf1wNpDkv3txg1` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAucLVFnEHoW65r4vWt7P9FCz32jHsE2owqGP8vjvcgUbJ` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAqthgbvugCZFZJ9CCWyfmsuihdNktrqfWsWtNBt7JbqXH` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAra3ZRCSZ5Sddzt6Je94H3mAnydexHcrr3e8zqEGkY449` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAriTMozLiFPubxwFiQhyNbWY3MwvMf9bykoga15eXEvYd` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAkkjrYrXXWuDMX4uaKK7vsAfvxRGrSuu6CHGvdfQ34WY5` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAr3pcSnVePtAJ8bAJ1EA3uVtZFYcFHmb3qG2vFfegPZcL` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuB2DF9XqWXbPibj5QLCeWCDqHcQj732yd3wgh3jc8J5Njy` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuArETNPEQdR2djJRFkeT4hjfsBaMgCPRvoJ9aBytbrFx36` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAzM6XiZajVTULJ1RuFzMV8EB1UyopoeeG66QUCme3nq4e` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAo2mgp5KGHharC1uwpoPmKQhv4jaVXpbfUf8ZktJ9UQoE` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAuaifJpPLJUade5S3G6fJwNB4PADZ4ukZU5nTcvWccjYm` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAw2FQT8AwKsgpK6gYqrWr3hhGEtRWeYDQ6sxvHmgqrQVi` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAyrMX442E9vya4EW8uwNBH3HZGg4aBz4wW89hCkJ8V9pt` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAtFPhK1UC5UXnVtNkadBoKpHD2aggyRMu1ypDXqPrnvtU` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAz6t7qz2dUQirNxaTHi47Jes7XmucMjFcBWkTtJbcrKUJ` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAyKhDXVopK3kzagfeDAGroe5dAh87xrb21HHPcwPQWY11` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuB2XT5QNNDmEz7EoaXptoVqKU7TiAeVQheH9xXtr6aWWQ4` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAuQR8yQfjksiyEp2g77K3T5vyrowoY7BYLmS9LGiTs4QL` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAwAv4TTBnzJACUyz5kQ27vCszBmbZv3cUfsGmzxCfdTVL` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAwuzXiz3pgJx3TXik9Wv1bkZak8jPtgGxt7haAL3rzmwC` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAqxzRzkFRuHbiCc9ctAnZHr7gB3PdgWDeDFMbTAFrh8DV` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuArTKiE4FdhhJzmfCxLUNyYkMay8DMLqsUKzRhgmajWezD` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuArBbEsLmsLriH9aH8yZmWR5nufYKbhSRsECzkZqKyWPK4` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAsHYj5aMBEBPLSGMbupuqQkKByxnekrzvpTMBWdos92nc` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAucNHmpYVtnZcFNciH3okKeh9ZVyTzzam6hHHWwaz3YJY` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAvtmc7Zs5sXCkK8Ph2Db2xpTpH7LDtBXWoUN4Ud9qDZPU` (2025-04-14 16:01:33)
- `/orbitdb/heads/orbitdb/zdpuAw4ecGTwKmxGgsePxxAitkyPvxKPN4uHiKC6yhSYyiwhp` (2025-04-14 16:01:33)
- `/dqmp/addr-exchange/1.0.0` (2025-04-15 18:01:46)
- `/_test_publishing_/1.0.0` (2025-04-18 02:01:20)
- `/pft/1.0.0` (2025-04-18 08:01:20)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `88.99.172.194` | DE | 111 | ['kubo/0.18.1/675f8bd/docker', 'kubo/0.29.0/3f0947b']| True  |
| `172.233.243.82` | FR | 55 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 55 | ['edgevpn']| True  |
| `26.26.26.1` | US | 27 | ['kubo/0.28.0/', 'kubo/0.30.0/desktop']| False  |
| `91.230.153.86` | RU | 26 | ['edgevpn']| False  |
| `123.181.13.205` | CN | 20 | ['kubo/0.28.0-dev/121cfae/docker']| False  |
| `136.244.23.253` | US | 15 | ['kubo/0.32.1/']| False  |
| `89.89.190.64` | FR | 14 | ['kubo/0.32.1/']| False  |
| `64.227.166.181` | IN | 13 | ['kubo/0.28.0/', 'kubo/0.29.0/3f0947b', 'kubo/0.32.1/']| True  |
| `80.77.36.40` | UA | 13 | ['kubo/0.32.1/']| False  |

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

In the specified time interval from `2025-04-14` to `2025-04-21` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-04-14` to `2025-04-21` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-04-14` to `2025-04-21` in the DHT and their datacenter association.

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