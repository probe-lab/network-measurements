# Nebula Measurement Results Calendar Week 41 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 41 - 2024](#nebula-measurement-results-calendar-week-41---2024)
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

The following results show measurement data that were collected in calendar week 41 in 2024 from `2024-10-07` to `2024-10-14`.

- Number of crawls `336`
- Number of visits `23,442,613`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `49,049`
- Number of unique peer IDs discovered in the DHT `47,796`
- Number of unique IP addresses found `45,567`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.31.0-rc1/desktop` (2024-10-07 01:50:43)
- `bootnode-20241007004256` (2024-10-07 01:50:53)
- `bootnode-20241007023902` (2024-10-07 03:51:07)
- `bootnode-20241007045021` (2024-10-07 04:50:55)
- `bootnode-20241007073331` (2024-10-07 05:50:56)
- `bootnode-20241007055451` (2024-10-07 06:20:53)
- `bootnode-20241007070422` (2024-10-07 07:21:07)
- `bootnode-20241007060922` (2024-10-07 07:50:50)
- `bootnode-20241007081304` (2024-10-07 08:21:11)
- `bootnode-20241007093557` (2024-10-07 12:20:56)
- `kubo/0.32.0-dev/00e1f812a-dirty` (2024-10-07 15:21:06)
- `bootnode-20241007102053` (2024-10-07 15:21:12)
- `ca-vsc@` (2024-10-07 15:50:57)
- `bootnode-20241007160719` (2024-10-07 16:21:02)
- `kubo/0.32.0-dev/00e1f812a` (2024-10-07 16:21:21)
- `rust-libp2p/0.45.0` (2024-10-07 16:21:22)
- `bootnode-20241007105238` (2024-10-07 16:51:20)
- `bootnode-20241007170145` (2024-10-07 17:21:04)
- `bootnode-20241007160908` (2024-10-07 17:21:20)
- `kubo/0.32.0-dev/ec9bf5088` (2024-10-07 18:21:03)
- `bootnode-20241007192539` (2024-10-07 18:51:09)
- `bootnode-20241007142041` (2024-10-07 19:21:10)
- `bootnode-20241007195115` (2024-10-07 19:51:21)
- `bootnode-20241007152037` (2024-10-07 20:21:02)
- `bootnode-20241007231513` (2024-10-07 23:21:12)
- `bootnode-20241008002047` (2024-10-08 00:20:58)
- `bootnode-20241007202103` (2024-10-08 01:21:07)
- `bootnode-20241008031656` (2024-10-08 03:21:17)
- `bootnode-20241008071113` (2024-10-08 07:21:19)
- `bootnode-20241008091029` (2024-10-08 07:51:02)
- `bootnode-20241008082928` (2024-10-08 08:51:01)
- `libp2p/1.3.3 UserAgent=v20.18.0` (2024-10-08 09:21:12)
- `bootnode-20241008094445` (2024-10-08 12:21:59)
- `github.com/harmony-one/harmony@2e824e126-dirty` (2024-10-08 14:50:50)
- `kubo/0.32.0-dev/091bc08/docker` (2024-10-08 15:51:11)
- `bootnode-20241008122033` (2024-10-08 17:20:57)
- `bootnode-20241008181225` (2024-10-08 18:21:12)
- `bootnode-20241008224902` (2024-10-08 23:21:10)
- `kubo/0.31.0-rc2/bd9e154/1234567890123456789012345678901234567890` (2024-10-08 23:51:00)
- `kubo/0.31.0-rc2/` (2024-10-09 00:20:53)
- `bootnode-20241008192015` (2024-10-09 00:21:04)
- `bootnode-20241009053428` (2024-10-09 03:50:56)
- `bootnode-20241009043002` (2024-10-09 04:51:12)
- `bootnode-20241009052904` (2024-10-09 05:50:55)
- `bootnode-20241009075004` (2024-10-09 07:51:00)
- `bootnode-20241009073028` (2024-10-09 07:51:16)
- `bootnode-20241009092048` (2024-10-09 09:21:14)
- `bootnode-20241009113304` (2024-10-09 11:51:04)
- `bootnode-20241009112832` (2024-10-09 11:51:05)
- `bootnode-20241009130408` (2024-10-09 14:21:00)
- `github.com/INFURA/ipfs-p2p-server@f6341f422` (2024-10-09 14:21:06)
- `bootnode-20241009105037` (2024-10-09 15:51:02)
- `bootnode-20241009153444` (2024-10-09 16:51:14)
- `bootnode-20241009180531` (2024-10-09 18:20:58)
- `bootnode-20241009125205` (2024-10-09 18:21:18)
- `helia/5.0.0 libp2p/2.1.8 UserAgent=v20.14.0` (2024-10-09 21:20:49)
- `kubo/0.30.0/debox/0.2.0` (2024-10-09 21:50:55)
- `bootnode-20241009190957` (2024-10-09 22:21:04)
- `bootnode-20241009220621` (2024-10-09 22:51:20)
- `bootnode-20241010012022` (2024-10-10 01:21:22)
- `bootnode-20241010005700` (2024-10-10 01:51:05)
- `bootnode-20241010020328` (2024-10-10 02:21:12)
- `bootnode-20241010035659` (2024-10-10 02:21:28)
- `bootnode-20241010022931` (2024-10-10 02:51:10)
- `bootnode-20241009221610` (2024-10-10 03:51:01)
- `bootnode-20241010045032` (2024-10-10 04:50:47)
- `bootnode-20241010051101` (2024-10-10 05:21:21)
- `bootnode-20241010003952` (2024-10-10 05:50:57)
- `kubo/0.32.0-dev/091bc083c-dirty` (2024-10-10 05:50:58)
- `bootnode-20241010064125` (2024-10-10 07:21:03)
- `bootnode-20241010092727` (2024-10-10 08:21:07)
- `bootnode-20241010040302` (2024-10-10 09:50:58)
- `bootnode-20241010100741` (2024-10-10 10:20:51)
- `helia/5.0.0 libp2p/2.1.8 UserAgent=v20.16.0` (2024-10-10 10:51:14)
- `bootnode-20241010061742` (2024-10-10 11:21:02)
- `bootnode-20241010063815` (2024-10-10 11:50:50)
- `github.com/INFURA/ipfs-p2p-server@0371255db` (2024-10-10 11:51:09)
- `bootnode-20241010065847` (2024-10-10 12:21:05)
- `bootnode-20241010125043` (2024-10-10 12:50:49)
- `bootnode-20241010085045` (2024-10-10 13:50:58)
- `bootnode-20241010133816` (2024-10-10 14:51:09)
- `bootnode-20241010200917` (2024-10-10 19:21:06)
- `bootnode-20241010142039` (2024-10-10 19:21:17)
- `bootnode-20241010145045` (2024-10-10 19:50:53)
- `bootnode-20241010221941` (2024-10-10 21:21:09)
- `bootnode-20241010183230` (2024-10-10 23:50:58)
- `bootnode-20241010192047` (2024-10-11 00:21:01)
- `bootnode-20241010200304` (2024-10-11 01:20:56)
- `bootnode-20241011042312` (2024-10-11 05:21:00)
- `bootnode-20241011055834` (2024-10-11 06:21:07)
- `bootnode-20241011062650` (2024-10-11 06:50:52)
- `kubo/0.32.0-dev/091bc08` (2024-10-11 07:50:48)
- `bootnode-20241011081516` (2024-10-11 08:51:10)
- `bootnode-20241011090632` (2024-10-11 09:21:15)
- `bootnode-20241011082714` (2024-10-11 10:20:49)
- `bootnode-20241011053805` (2024-10-11 10:51:00)
- `bootnode-20241011113736` (2024-10-11 11:50:52)
- `bootnode-20241011121059` (2024-10-11 12:21:15)
- `bootnode-20241011123127` (2024-10-11 13:51:33)
- `github.com/INFURA/ipfs-p2p-server@2ef702b45` (2024-10-11 15:21:00)
- `bootnode-20241011163802` (2024-10-11 16:51:08)
- `bootnode-20241011164006` (2024-10-11 16:51:10)
- `bootnode-20241011135037` (2024-10-11 18:50:56)
- `bootnode-20241012001820` (2024-10-11 22:50:59)
- `helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0` (2024-10-12 00:50:48)
- `bootnode-20241011191917` (2024-10-12 01:20:57)
- `bootnode-20241011203951` (2024-10-12 02:20:52)
- `bootnode-20241012003700` (2024-10-12 02:21:12)
- `bootnode-20241012034622` (2024-10-12 03:51:17)
- `bootnode-20241012042932` (2024-10-12 04:51:11)
- `bootnode-20241012045930` (2024-10-12 05:21:13)
- `bootnode-20241012082014` (2024-10-12 08:20:52)
- `bootnode-20241012103953` (2024-10-12 09:21:05)
- `bootnode-20241012081859` (2024-10-12 10:20:51)
- `bootnode-20241012055007` (2024-10-12 10:51:19)
- `bootnode-20241012135034` (2024-10-12 11:51:08)
- `bootnode-20241012074619` (2024-10-12 12:50:51)
- `bootnode-20241012123958` (2024-10-12 13:20:55)
- `bootnode-20241012095006` (2024-10-12 14:50:52)
- `helia/5.0.0 libp2p/2.1.9 UserAgent=v18.18.2` (2024-10-12 15:21:19)
- `bootnode-20241012103200` (2024-10-12 15:51:00)
- `bootnode-20241012143033` (2024-10-12 17:21:05)
- `bootnode-20241012183053` (2024-10-12 17:51:05)
- `bootnode-20241012125349` (2024-10-12 18:21:04)
- `bootnode-20241012154734` (2024-10-12 21:20:58)
- `bootnode-20241012222507` (2024-10-12 22:50:53)
- `kubo/0.31.0-rc2/desktop` (2024-10-13 02:51:25)
- `bootnode-20241013010749` (2024-10-13 03:20:54)
- `bootnode-20241012222028` (2024-10-13 03:21:13)
- `bootnode-20241012224146` (2024-10-13 04:20:54)
- `kubo/0.31.0-rc2/bd9e154/docker` (2024-10-13 05:25:58)
- `kubo/0.31.0-rc2/bd9e154` (2024-10-13 05:50:47)
- `bootnode-20241013081551` (2024-10-13 07:20:50)
- `bootnode-20241013035047` (2024-10-13 08:50:51)
- `bootnode-20241013083806` (2024-10-13 08:51:17)
- `bootnode-20241013093855` (2024-10-13 09:50:52)
- `bootnode-20241013045123` (2024-10-13 10:51:28)
- `bootnode-20241013111940` (2024-10-13 12:21:02)
- `bootnode-20241013125218` (2024-10-13 13:50:58)
- `bootnode-20241013153351` (2024-10-13 15:50:47)
- `bootnode-20241013103805` (2024-10-13 15:50:49)
- `bootnode-20241013111849` (2024-10-13 16:21:07)
- `bootnode-20241013175028` (2024-10-13 17:50:55)
- `bootnode-20241013130050` (2024-10-13 18:20:55)
- `p2px@` (2024-10-13 19:50:53)
- `bootnode-20241013194959` (2024-10-13 20:22:53)
- `bootnode-20241013145257` (2024-10-13 20:52:40)
- `bootnode-20241013232941` (2024-10-13 21:51:08)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/arcana/dsg/1.0.0` (2024-10-07 15:50:57)
- `/orbitdb/heads/orbitdb/zdpuAptViQq3mC1YLGyc1z7YuQeAvr4kmQdkzcBXh78q9apZT` (2024-10-11 18:21:09)
- `/orbitdb/heads/orbitdb/zdpuAx3QWkWr4ueh5KTmHe1iHyYu8AXtWsuqy7WgQayj7Ctwk` (2024-10-11 18:21:09)
- `/orbitdb/heads/orbitdb/zdpuB2u7uwtX2mSTsNdoJ7JauGbwdAReovUPdxUBv4ZWZsYZU` (2024-10-11 18:21:09)
- `/orbitdb/heads/orbitdb/zdpuAmk2K9ZkxNuWMMQV3ndjyaaVTHMFrkqYGSaD1dSgWnjr8` (2024-10-11 18:21:09)
- `/orbitdb/heads/orbitdb/zdpuAmqqkouGYYPcWqgeppwjpHRtKKgex6uqzLTvrsTNT3J7d` (2024-10-11 18:21:09)
- `/orbitdb/heads/orbitdb/zdpuAopNeHFZ2TqWAQgCUFnMSc2RMYCgSqBG8bkYSCwRLPQF2` (2024-10-11 18:21:09)
- `/orbitdb/heads/orbitdb/zdpuAud4ea8Qb8KK6sxt9Fmw4EHd82MXTwMzQND4Fma3KACx6` (2024-10-11 18:21:09)
- `/orbitdb/heads/orbitdb/zdpuAxDhYQQkrL8CQD5ZWNbdoa1gDVkJUS7tuPM697XcDVSzU` (2024-10-11 18:21:09)
- `/orbitdb/heads/orbitdb/zdpuAmbas2yTZh7jtvQBHjEB9j84b7Nf9kwFZCRZHCUZmbYeu` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAnQV9A5uohqVgj1e9XuT9J5FdjUHCDcvUzMtxXv4MXWFr` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAkadzfcv85pcGSw8DbgFSeSPfVVi3SF6MYkv1dKz3FuW9` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuB2BrvmPQYJ7BUrXKDT9zmPxxArTeVFPqbSruqPtLbndPP` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAoK2sQgNnvc7FNnzGjGtp7cbGvXaAc5qYJHaMCkCyfLKT` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuArRxWRviCVGW4sXmyyjkdSbZRfbiZb5PLM1yT3eJdD1VJ` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAskV7vrFKpR1faxe5oJiy5Xk5nyv3PJr9mXogx2EhN9JH` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAugQrJHfh8w5Kja8ofcRatbp8zuUWSyG6JKJdGJngb53d` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAuph6zbxEqE7TczzveV4PPwLCWR9sXpjkLVE3puoPH6P1` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAvrjRCTkhGTynVcHTQnL6nZWnyG4FVJoj2AEFKu4uTUPG` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuB2gEKoAZQH3LK4NMxG3kt367rSU1CGMJHMmNaq6yQudEK` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAzxv1SANift11BUvY9sf38gQHAomwMq29LizkCeM63N7S` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAtwnejF7Yc5pE5XiQK56WHQqLEvj5w8Ca3ZdV6DUuSehz` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAkqh4hSnqcKZMdtjjPpfiSRbaEaqLFe4B5gEbgQFRvKnD` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAndTd2pSLrfWEhEatpE3bjb1HHJ1Ltx7EcCNAPLm4PXcF` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAxgJ9SmpXXEGD1ZtuWNoXT55Yj46U2EJAgJA5pGXVQ4K8` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAxtiMXXtqRtkMrBiFKVAxLEkRCZvMkB7Q6ZpR7YL2otgz` (2024-10-11 18:21:10)
- `/orbitdb/heads/orbitdb/zdpuAzCDqvjCTfejVJZTZFD9JkBuHS8SfvQeABS95gjFrT2Vi` (2024-10-11 18:21:10)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `51.159.174.206` | FR | 89 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.150.159` | FR | 89 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.247.127` | FR | 88 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 78 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 78 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `68.183.11.180` | NL | 57 | ['edgevpn']| True  |
| `151.115.47.2` | PL | 43 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-10-07` to `2024-10-14` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-10-07` to `2024-10-14` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-10-07` to `2024-10-14` in the DHT and their datacenter association.

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