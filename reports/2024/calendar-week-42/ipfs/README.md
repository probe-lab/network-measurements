# Nebula Measurement Results Calendar Week 42 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 42 - 2024](#nebula-measurement-results-calendar-week-42---2024)
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

The following results show measurement data that were collected in calendar week 42 in 2024 from `2024-10-14` to `2024-10-21`.

- Number of crawls `336`
- Number of visits `24,376,498`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `52,268`
- Number of unique peer IDs discovered in the DHT `51,521`
- Number of unique IP addresses found `44,334`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20241013191552` (2024-10-14 00:20:57)
- `bootnode-20241013195007` (2024-10-14 00:50:57)
- `bootnode-20241013202043` (2024-10-14 01:20:55)
- `bootnode-20241014025430` (2024-10-14 03:20:53)
- `bootnode-20241014023801` (2024-10-14 03:20:56)
- `bootnode-20241014044029` (2024-10-14 04:20:48)
- `bootnode-20241013230851` (2024-10-14 04:21:03)
- `bootnode-20241014062025` (2024-10-14 06:21:11)
- `bootnode-20241014060902` (2024-10-14 06:51:04)
- `bootnode-20241014081102` (2024-10-14 08:21:13)
- `kubo/0.31.0-dev/e909852ba-dirty` (2024-10-14 08:51:01)
- `bootnode-20241014102039` (2024-10-14 10:20:51)
- `bootnode-20241014055040` (2024-10-14 10:50:48)
- `bootnode-20241014120254` (2024-10-14 10:51:25)
- `bootnode-20241014102054` (2024-10-14 11:21:01)
- `bootnode-20241014100845` (2024-10-14 11:52:36)
- `bootnode-20241014090908` (2024-10-14 14:20:56)
- `bootnode-20241014165120` (2024-10-14 14:51:35)
- `bootnode-20241014131017` (2024-10-14 15:21:10)
- `bootnode-20241014150318` (2024-10-14 15:50:51)
- `bootnode-20241014145737` (2024-10-14 17:21:19)
- `kubo/0.32.0-dev/7ae58bc99` (2024-10-14 18:50:57)
- `bootnode-20241014200153` (2024-10-14 18:51:25)
- `bootnode-20241014140422` (2024-10-14 20:21:16)
- `bootnode-20241014155100` (2024-10-14 20:51:15)
- `bootnode-20241014165055` (2024-10-14 21:51:11)
- `bootnode-20241015001309` (2024-10-14 22:51:04)
- `bootnode-20241014190154` (2024-10-15 00:20:57)
- `bootnode-20241015001025` (2024-10-15 00:21:13)
- `bootnode-20241015012048` (2024-10-15 01:20:54)
- `bootnode-20241014213802` (2024-10-15 02:51:15)
- `bootnode-20241014225026` (2024-10-15 03:50:53)
- `bootnode-20241015050338` (2024-10-15 03:50:57)
- `bootnode-20241015042031` (2024-10-15 04:20:55)
- `bootnode-20241015033724` (2024-10-15 04:51:01)
- `bootnode-20241015014357` (2024-10-15 06:50:54)
- `bootnode-20241015021400` (2024-10-15 07:21:07)
- `bootnode-20241015060901` (2024-10-15 07:51:07)
- `bootnode-20241015033145` (2024-10-15 08:51:14)
- `bootnode-20241015083446` (2024-10-15 09:21:06)
- `bootnode-20241015095019` (2024-10-15 09:50:58)
- `bootnode-20241015045015` (2024-10-15 09:50:58)
- `bootnode-20241015125554` (2024-10-15 11:50:49)
- `bootnode-20241015065059` (2024-10-15 11:51:22)
- `bootnode-20241015075031` (2024-10-15 12:50:53)
- `bootnode-20241015131831` (2024-10-15 13:20:52)
- `bootnode-20241015130028` (2024-10-15 13:21:21)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v21.5.0` (2024-10-15 13:51:45)
- `bootnode-20241015140123` (2024-10-15 14:20:52)
- `bootnode-20241015133853` (2024-10-15 14:20:54)
- `bootnode-20241015141740` (2024-10-15 14:51:07)
- `bootnode-20241015095058` (2024-10-15 14:51:09)
- `bootnode-20241015140624` (2024-10-15 15:21:00)
- `bootnode-20241015171754` (2024-10-15 15:50:50)
- `github.com/JackalLabs/sequoia@a382b1449` (2024-10-15 16:21:36)
- `bootnode-20241015183501` (2024-10-15 16:50:50)
- `bootnode-20241015115116` (2024-10-15 16:51:22)
- `bootnode-20241015182645` (2024-10-15 17:20:59)
- `bootnode-20241015125048` (2024-10-15 17:51:21)
- `bootnode-20241015201859` (2024-10-15 18:21:17)
- `bootnode-20241015130322` (2024-10-15 18:21:32)
- `bootnode-20241015183916` (2024-10-15 19:21:03)
- `bootnode-20241015194959` (2024-10-15 19:51:03)
- `bootnode-20241015210044` (2024-10-15 21:21:03)
- `bootnode-20241015170411` (2024-10-15 22:21:07)
- `bootnode-20241015184623` (2024-10-15 23:50:50)
- `bootnode-20241015225707` (2024-10-15 23:51:03)
- `bootnode-20241015184644` (2024-10-15 23:51:17)
- `libp2p/1.9.4 UserAgent=v20.18.0` (2024-10-16 00:51:44)
- `bootnode-20241015224721` (2024-10-16 03:50:56)
- `bootnode-20241016062926` (2024-10-16 06:20:56)
- `bootnode-20241016060934` (2024-10-16 06:21:06)
- `bootnode-20241016094732` (2024-10-16 08:51:03)
- `DerekBum/p2pChat@` (2024-10-16 09:21:08)
- `bootnode-20241016102131` (2024-10-16 10:51:13)
- `bootnode-20241016132005` (2024-10-16 11:21:18)
- `bootnode-20241016120344` (2024-10-16 12:21:16)
- `xp2p@` (2024-10-16 14:51:01)
- `github.com/bornholm/neighbour-watch@` (2024-10-16 15:51:10)
- `kubo/0.32.0-dev/091bc083c` (2024-10-16 15:51:12)
- `bootnode-20241016111905` (2024-10-16 16:21:20)
- `bootnode-20241016161238` (2024-10-16 16:21:28)
- `kubo/0.32.0-dev/36f385c/docker` (2024-10-16 16:51:24)
- `kubo/0.31.0/5a32936` (2024-10-16 17:20:46)
- `kubo/0.31.0/5a32936/docker` (2024-10-16 17:20:53)
- `kubo/0.31.0/5a32936/1234567890123456789012345678901234567890` (2024-10-16 17:20:54)
- `bootnode-20241016153309` (2024-10-16 17:20:59)
- `bootnode-20241016122044` (2024-10-16 17:21:11)
- `github.com/taurusgroup/multi-party-sig@4d84aafb5-dirty` (2024-10-16 17:51:19)
- `bootnode-20241016130013` (2024-10-16 18:21:01)
- `kubo/0.32.0-dev/c488864/docker` (2024-10-16 18:51:23)
- `bootnode-20241016184352` (2024-10-16 18:51:26)
- `kubo/0.32.0-dev/b336602/docker` (2024-10-16 19:51:03)
- `kubo/0.32.0-dev/` (2024-10-16 19:51:24)
- `bootnode-20241016213307` (2024-10-16 20:20:55)
- `bootnode-20241016141251` (2024-10-16 20:51:09)
- `kubo/0.32.0-dev/61bae03/docker` (2024-10-16 20:51:32)
- `kubo/0.31.0/` (2024-10-16 20:51:41)
- `bootnode-20241016234141` (2024-10-16 23:50:59)
- `bootnode-20241017030905` (2024-10-17 01:21:12)
- `kubo/0.31.0/5a32936f7` (2024-10-17 02:51:00)
- `bootnode-20241017023750` (2024-10-17 02:51:11)
- `bootnode-20241017031823` (2024-10-17 03:21:25)
- `github.com/harmony-one/harmony@8ba758a41` (2024-10-17 04:51:26)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v20.14.0` (2024-10-17 04:51:30)
- `bootnode-20241017063117` (2024-10-17 04:51:46)
- `bootnode-20241017052028` (2024-10-17 05:20:51)
- `bootnode-20241017004951` (2024-10-17 05:51:05)
- `bootnode-20241017052848` (2024-10-17 06:21:02)
- `github.com/harmony-one/harmony@91e8ffc5b` (2024-10-17 06:51:13)
- `kubo/0.32.0-dev/16c90f0/docker` (2024-10-17 08:51:10)
- `bootnode-20241017073007` (2024-10-17 09:21:09)
- `bootnode-20241017120638` (2024-10-17 10:21:11)
- `bootnode-20241017123731` (2024-10-17 11:21:24)
- `libp2p/2.1.9 UserAgent=v20.18.0` (2024-10-17 11:21:26)
- `bootnode-20241017140843` (2024-10-17 12:21:08)
- `bootnode-20241017141100` (2024-10-17 14:21:27)
- `bootnode-20241017095010` (2024-10-17 14:51:13)
- `kubo/0.31.0/5a32936/bootstrap.libp2p.io` (2024-10-17 16:20:42)
- `bootnode-20241017160555` (2024-10-17 16:20:58)
- `bootnode-20241017171838` (2024-10-17 17:21:07)
- `bootnode-20241017174611` (2024-10-17 17:51:25)
- `bootnode-20241017125045` (2024-10-17 18:20:57)
- `bootnode-20241017180050` (2024-10-17 18:21:26)
- `bootnode-20241017195736` (2024-10-17 19:21:15)
- `bootnode-20241017192103` (2024-10-17 19:21:16)
- `kubo/0.31.0/desktop` (2024-10-17 19:50:50)
- `bootnode-20241017214921` (2024-10-17 22:21:06)
- `bootnode-20241017174431` (2024-10-17 23:20:56)
- `bootnode-20241017212049` (2024-10-18 02:21:02)
- `bootnode-20241018040814` (2024-10-18 03:51:10)
- `bootnode-20241018022848` (2024-10-18 03:51:11)
- `bootnode-20241018053433` (2024-10-18 05:50:56)
- `bootnode-20241018050608` (2024-10-18 05:50:56)
- `bootnode-20241018061631` (2024-10-18 06:21:11)
- `bootnode-20241018084041` (2024-10-18 06:50:56)
- `bootnode-20241018025116` (2024-10-18 07:51:20)
- `bootnode-20241018031910` (2024-10-18 08:21:01)
- `bootnode-20241018080728` (2024-10-18 09:21:05)
- `bootnode-20241018135033` (2024-10-18 13:51:04)
- `bootnode-20241018151226` (2024-10-18 14:20:51)
- `bootnode-20241018095049` (2024-10-18 14:50:59)
- `github.com/JackalLabs/sequoia@4b3702920-dirty` (2024-10-18 15:21:04)
- `github.com/JackalLabs/sequoia@4b3702920` (2024-10-18 15:21:08)
- `bootnode-20241018174529` (2024-10-18 16:20:48)
- `kubo/0.31.0/da34275-dirty` (2024-10-18 16:51:15)
- `bootnode-20241018200708` (2024-10-18 18:51:06)
- `kubo/0.32.0-dev/a03863741` (2024-10-18 19:21:10)
- `bootnode-20241018190041` (2024-10-18 19:21:25)
- `kubo/0.32.0-dev/538c9bb05` (2024-10-18 22:20:53)
- `bootnode-20241019005932` (2024-10-18 23:21:46)
- `bootnode-20241018194753` (2024-10-19 00:50:52)
- `bootnode-20241018235819` (2024-10-19 00:50:58)
- `bootnode-20241019005714` (2024-10-19 01:21:25)
- `bootnode-20241018204840` (2024-10-19 01:51:02)
- `bootnode-20241019023922` (2024-10-19 02:50:59)
- `bootnode-20241019035043` (2024-10-19 03:50:52)
- `bootnode-20241019033049` (2024-10-19 03:51:03)
- `github.com/taurusgroup/multi-party-sig@0bb37aca3-dirty` (2024-10-19 04:51:03)
- `kubo/0.32.0-dev/16c90f063` (2024-10-19 05:20:53)
- `bootnode-20241019002656` (2024-10-19 05:50:50)
- `bootnode-20241019045217` (2024-10-19 05:50:54)
- `bootnode-20241019013711` (2024-10-19 06:51:01)
- `bootnode-20241019044808` (2024-10-19 09:50:57)
- `bootnode-20241019051842` (2024-10-19 10:20:55)
- `bootnode-20241019092543` (2024-10-19 10:51:18)
- `bootnode-20241019131406` (2024-10-19 13:21:05)
- `bootnode-20241019132856` (2024-10-19 13:51:03)
- `bootnode-20241019085857` (2024-10-19 14:21:18)
- `bootnode-20241019144959` (2024-10-19 14:51:02)
- `bootnode-20241019103956` (2024-10-19 15:51:40)
- `kubo/0.32.0-dev/16c90f063-dirty` (2024-10-19 16:51:34)
- `bootnode-20241019170925` (2024-10-19 17:20:48)
- `bootnode-20241019180612` (2024-10-19 18:21:08)
- `bootnode-20241019190855` (2024-10-19 19:21:17)
- `bootnode-20241019143756` (2024-10-19 20:20:50)
- `bootnode-20241019195000` (2024-10-19 20:21:05)
- `bootnode-20241019153822` (2024-10-19 20:50:52)
- `bootnode-20241019161207` (2024-10-19 21:20:50)
- `bootnode-20241019233025` (2024-10-19 21:51:31)
- `bootnode-20241020000322` (2024-10-20 01:51:37)
- `bootnode-20241019204153` (2024-10-20 02:20:52)
- `bootnode-20241020040149` (2024-10-20 02:20:57)
- `libp2p/2.1.9 UserAgent=v19.9.0` (2024-10-20 03:20:46)
- `libp2p/1.9.4 UserAgent=v19.9.0` (2024-10-20 03:20:47)
- `kubo/0.31.0/collab.ipfscluster.io` (2024-10-20 03:20:52)
- `bootnode-20241019214717` (2024-10-20 03:21:06)
- `kubo/0.32.0-dev/078c23d/docker` (2024-10-20 03:51:07)
- `bootnode-20241020022504` (2024-10-20 03:51:14)
- `bootnode-20241019231835` (2024-10-20 04:21:00)
- `bootnode-20241019215629` (2024-10-20 04:21:04)
- `bootnode-20241020063210` (2024-10-20 04:50:57)
- `bootnode-20241020011957` (2024-10-20 06:21:21)
- `bootnode-20241020065929` (2024-10-20 07:21:23)
- `bootnode-20241020090834` (2024-10-20 07:51:12)
- `bootnode-20241020071945` (2024-10-20 08:21:08)
- `bootnode-20241020085038` (2024-10-20 08:50:58)
- `fsp2p@5c02ad085-dirty` (2024-10-20 09:51:38)
- `bootnode-20241020122008` (2024-10-20 10:20:52)
- `bootnode-20241020060942` (2024-10-20 11:20:55)
- `bootnode-20241020062155` (2024-10-20 11:50:55)
- `bootnode-20241020114731` (2024-10-20 12:21:20)
- `bootnode-20241020145524` (2024-10-20 13:21:00)
- `bootnode-20241020150442` (2024-10-20 13:21:29)
- `bootnode-20241020074820` (2024-10-20 13:50:51)
- `bootnode-20241020144811` (2024-10-20 15:21:09)
- `bootnode-20241020172554` (2024-10-20 15:51:19)
- `bootnode-20241020173619` (2024-10-20 16:20:55)
- `bootnode-20241020112115` (2024-10-20 16:21:38)
- `bootnode-20241020084112` (2024-10-20 16:21:48)
- `xcod@` (2024-10-20 16:50:55)
- `bootnode-20241020122033` (2024-10-20 17:21:08)
- `bootnode-20241020193846` (2024-10-20 18:20:55)
- `bootnode-20241020201732` (2024-10-20 18:21:05)
- `helia/5.0.1 libp2p/2.1.9 UserAgent=v22.8.0` (2024-10-20 18:22:01)
- `bootnode-20241020212024` (2024-10-20 19:20:59)
- `bootnode-20241020193847` (2024-10-20 19:51:10)
- `bootnode-20241020230047` (2024-10-20 22:21:13)
- `bootnode-20241020225038` (2024-10-20 22:50:56)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/private-chat/1.0.0` (2024-10-14 07:21:03)
- `/multipartysig/1.0.0` (2024-10-16 18:21:05)
- `defs@stream/forward/network/1.0.0` (2024-10-18 02:20:51)
- `/bpfs/stream/1.0.0` (2024-10-18 02:20:51)
- `/share_chain_sync/2` (2024-10-19 02:21:33)
- `/tari_direct_peer_info/2` (2024-10-19 02:21:33)
- `/tari_direct_peer_info/1` (2024-10-19 02:50:46)
- `/share_chain_sync/1` (2024-10-19 02:50:46)
- `/share_chain_sync/3` (2024-10-20 18:52:17)
- `/tari_direct_peer_info/3` (2024-10-20 18:52:17)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `147.102.107.99` | GR | 99 | ['rust-libp2p/0.45.0']| False  |
| `94.141.103.221` | AM | 88 | ['rust-libp2p/0.45.0']| False  |
| `51.159.150.159` | FR | 88 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 86 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `91.108.247.167` | AU | 85 | ['rust-libp2p/0.45.0']| False  |
| `51.15.247.127` | FR | 84 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 77 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 77 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-10-14` to `2024-10-21` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-10-14` to `2024-10-21` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-10-14` to `2024-10-21` in the DHT and their datacenter association.

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