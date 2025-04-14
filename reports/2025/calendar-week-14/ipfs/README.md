# Nebula Measurement Results Calendar Week 14 - 2025

## Table of Contents

- [Nebula Measurement Results Calendar Week 14 - 2025](#nebula-measurement-results-calendar-week-14---2025)
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

The following results show measurement data that were collected in calendar week 14 in 2025 from `2025-04-07` to `2025-04-14`.

- Number of crawls `84`
- Number of visits `9,580,127`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `53,288`
- Number of unique peer IDs discovered in the DHT `52,789`
- Number of unique IP addresses found `46,933`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `gitlab.feishuwg.com/feishu/saascli@6786161f2-dirty` (2025-04-07 00:01:49)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.2` (2025-04-07 06:01:25)
- `github.com/INFURA/ipfs-p2p-server@277e15b2a` (2025-04-07 08:01:15)
- `kubo/0.35.0-dev/d67bdc07d` (2025-04-07 14:01:41)
- `github.com/harmony-one/harmony@v1.10.3-0.20250403180333-f905f11cb095+dirty` (2025-04-07 16:01:16)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.3` (2025-04-07 16:01:38)
- `github.com/JackalLabs/sequoia@31a310af0` (2025-04-07 16:01:59)
- `local/example/v2@v0.0.0-20250407135535-0b702970c0b6+dirty` (2025-04-07 20:01:11)
- `github.com/harmony-one/harmony@v1.10.3-0.20250407170725-a3ebecdd1eb3+dirty` (2025-04-07 22:01:44)
- `bootnode-20250408034307` (2025-04-08 04:01:11)
- `dvpncmd@a8315f86d-hayek` (2025-04-08 06:01:24)
- `local/k8s-swarm-example/v2@` (2025-04-08 06:01:29)
- `bootnode-20250408045218` (2025-04-08 06:01:34)
- `js-libp2p/2.8.0 node/20.19.0` (2025-04-08 10:01:29)
- `bootnode-20250408103842` (2025-04-08 12:01:29)
- `bootnode-20250408075336` (2025-04-08 14:01:11)
- `bootnode-20250408144808` (2025-04-08 14:01:12)
- `dvpncmd@` (2025-04-08 14:01:21)
- `bootnode-20250408144552` (2025-04-08 14:02:01)
- `kubo/0.35.0-dev/d67bdc07d-dirty` (2025-04-08 22:01:47)
- `kubo/0.35.0-dev/19b591d/docker` (2025-04-08 22:02:06)
- `github.com/JackalLabs/sequoia@31a310af0-dirty` (2025-04-09 16:01:28)
- `kubo/0.35.0-dev/35d952a08` (2025-04-09 18:01:31)
- `kubo/0.35.0-dev/996bcf3/1234567890123456789012345678901234567890` (2025-04-09 18:01:34)
- `kubo/0.35.0-dev/996bcf3` (2025-04-09 18:01:39)
- `kubo/0.35.0-dev/fe3106f/docker` (2025-04-09 20:01:18)
- `kubo/0.35.0-dev/996bcf3/docker` (2025-04-09 20:01:22)
- `helia/5.3.0 js-libp2p/2.8.3 node/23.2.0` (2025-04-10 08:01:35)
- `@libp2p/amino-dht-bootstrapper/1.9.2 js-libp2p/2.8.3 node/22.14.0` (2025-04-10 08:01:41)
- `bootnode-20250410155554` (2025-04-10 16:01:14)
- `bootnode-20250410180037` (2025-04-10 16:01:24)
- `bootnode-20250410180551` (2025-04-10 18:01:35)
- `bootnode-20250410230313` (2025-04-11 00:01:23)
- `bootnode-20250411134450` (2025-04-11 12:01:35)
- `dvpncmd@c00526527-hayek` (2025-04-11 14:01:31)
- `bootnode-20250411155602` (2025-04-11 14:01:37)
- `bootnode-20250411145806` (2025-04-11 14:01:44)
- `bootnode-20250411093050` (2025-04-11 16:01:33)
- `kubo/0.35.0-dev/fe3106f9a-dirty` (2025-04-11 16:01:34)
- `bootnode-20250411161331` (2025-04-11 16:01:42)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.3.0.20250411152531-1602eaf6f1cc` (2025-04-11 16:02:01)
- `github.com/SelimCelen/kadserver@v0.0.0-20250401233257-41ba52b050e0+dirty` (2025-04-12 04:01:55)
- `js-libp2p/2.8.1 node/20.17.0` (2025-04-12 06:01:18)
- `js-libp2p/2.8.3 node/20.18.0` (2025-04-12 10:01:24)
- `js-libp2p/2.8.2 node/20.18.3` (2025-04-13 08:01:15)
- `bootnode-20250413105952` (2025-04-13 12:01:14)
- `dvpncmd@88ef8ddfe-hayek` (2025-04-13 12:01:15)
- `github.com/JackalLabs/sequoia@v1.3.0-rc.4.0.20250413195356-5ef64e5bdf8a` (2025-04-13 20:01:58)
- `github.com/JackalLabs/sequoia@5ef64e5bd` (2025-04-13 20:01:58)
- `bootnode-20250413211258` (2025-04-13 22:01:09)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/orbitdb/heads/orbitdb/zdpuAv8UvguX9GwaAVt2MzPG3DREjs3XWfPu6jDYoz5ZHVxnU` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAvaxpxwMXbmBhKBDimJ6krPTEuLjDzUnscSf8XqyMYBkS` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuB1b2Q8uhJmv7S5apjYxFx54mha8FCTRpb2HZP48XHRQZz` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAoNx2xMrta4dACECsdJC1iKnZ4CowMFV2YYS4KocxU7Vw` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAsmcwNFjiNdRND1LzMDze98SzCew3GUM8cRRHd5FK9XvV` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAxfXXCX2JnTs59FoxKNBuBwM63dj9i3PgtEP5hKNKCdcr` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAukk6mHeNorP4QYW9fstzKT8B4go6CtZ5LRNoEReNTuo9` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAwNJ3BemQu34AVEMiYepDnmoZgvbK6Z4LnNQ1pvUnaETr` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAnbfM5YU1QouwudJSvdBD3o57geagfYMpnWiQy7ytpGE6` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAs1dht3ihhmPJtaRY2WSKCJDNK2VyuM3SmY1uZhn7FNJA` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAs2D4Q6CJQ7QPvQebCf8HEoAeaFFBE9pniMkYj1yVxRXk` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAzDpDwgWD8fCtKhi4PAMFCg6uQnCKZZLbJb8jgfHfncMt` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAqFsgPkB1BKsESCxjKcCEvoGKYWezwSGH7gwNSvpW7hn3` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAtpr2syK8dp9PtNnuiUpi667N1YJ1rEaRdrRReHVQtZak` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAxEDZ1xcEyvJCV5QzYGShZL3yaMPPuvmxwwFq8cruhowG` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAuXBCj6SWt6V2B6F8Qe6Saavaukh7YD7dJ2LziRkRfxwg` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAvsyMdVB4H6Y2CQUPaihPv5yb6Ye6bPPPxj5PmGEhPRvq` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAmbaF3k2Sg2qTyPT86spbFmRzWdFkYtTzqhZC1B5dNkcA` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAmEzzmJhxXiFwdeXNzyr3jJSFhKhbndpjPGagUWNSRDom` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuApkcifznAmZnaXeWyLucfwZ3GgBDpihUc6EZkH6fdwz94` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAuo4UewWkhCGPCnLtvgajGUYVxdYU7z4ws3M5tV63Nrvs` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAwHERKDrG4x1FZP2NXEHyQzD2KyUozhMTnAftGiZDgZeq` (2025-04-10 16:01:27)
- `/orbitdb/heads/orbitdb/zdpuAoJuPryvT8zJoq86rHkAsSU6Yx4g5Wn1G5jyQ6EBt6Te6` (2025-04-10 18:01:34)
- `/orbitdb/heads/orbitdb/zdpuAwQVQBZdahXw94L7KNuxnBLjqoUkctq5igpfWvvW3P8Zf` (2025-04-10 18:01:34)
- `/orbitdb/heads/orbitdb/zdpuAvmTVwWoMu6y3Xquksfye75vtQfSLPqdStgsXYHN4SLbb` (2025-04-11 04:02:02)
- `/orbitdb/heads/orbitdb/zdpuB2CnqhSmc4p7bL811KRdHkJL476xMhxJUUQpP8adA7jLw` (2025-04-11 04:02:02)
- `/file-transfer/1.0` (2025-04-12 04:01:55)
- `/chat/2.0.0` (2025-04-12 04:01:55)
- `/file-transfer/2.0` (2025-04-12 04:01:55)
- `/krelay/ping/1.0.0` (2025-04-12 04:01:55)
- `/krelay/peer-exchange/1.0.0` (2025-04-12 04:01:55)
- `/orbitdb/heads/orbitdb/zdpuB2VJ6qjRNDpNYpyVzUbxnMZCmsQbuFU68hbFQuCywfvTn` (2025-04-13 08:01:15)
- `/orbitdb/heads/orbitdb/zdpuAko6pqTfaRcrpb2vrco2yf3m62KZZyFAoLFiaj3Zz14RS` (2025-04-13 08:01:15)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `172.233.243.82` | FR | 45 | ['edgevpn']| True  |
| `2600:3c07::f03c:95ff:febb:e7a` | FR | 45 | ['edgevpn']| True  |
| `89.89.190.64` | FR | 34 | ['kubo/0.32.1/']| False  |
| `138.199.197.24` | DE | 32 | ['kubo/0.34.0-dev/']| False  |
| `2a01:4f8:1c1b:7477::1` | DE | 32 | ['kubo/0.34.0-dev/']| True  |
| `26.26.26.1` | US | 32 | ['go-ipfs/0.8.0/48f94e2', 'kubo/0.22.0/desktop', 'kubo/0.28.0/']| False  |
| `88.99.172.194` | DE | 25 | ['kubo/0.18.1/675f8bd/docker', 'kubo/0.29.0/3f0947b']| True  |
| `91.230.153.86` | RU | 23 | ['edgevpn']| False  |
| `49.12.5.41` | DE | 22 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| True  |
| `121.6.199.196` | SG | 22 | ['kubo/0.32.1/']| False  |

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

In the specified time interval from `2025-04-07` to `2025-04-14` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2025-04-07` to `2025-04-14` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2025-04-07` to `2025-04-14` in the DHT and their datacenter association.

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