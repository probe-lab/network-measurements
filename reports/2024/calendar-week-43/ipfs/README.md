# Nebula Measurement Results Calendar Week 43 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 43 - 2024](#nebula-measurement-results-calendar-week-43---2024)
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

The following results show measurement data that were collected in calendar week 43 in 2024 from `2024-10-21` to `2024-10-28`.

- Number of crawls `336`
- Number of visits `26,672,486`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `54,918`
- Number of unique peer IDs discovered in the DHT `54,049`
- Number of unique IP addresses found `42,965`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20241021015203` (2024-10-21 00:20:50)
- `bootnode-20241020193617` (2024-10-21 00:51:16)
- `bootnode-20241020215907` (2024-10-21 03:21:08)
- `bootnode-20241021032705` (2024-10-21 03:51:18)
- `bootnode-20241020224446` (2024-10-21 05:21:00)
- `bootnode-20241021050829` (2024-10-21 05:21:00)
- `bootnode-20241021054424` (2024-10-21 05:21:53)
- `bootnode-20241021035323` (2024-10-21 05:50:49)
- `bootnode-20241021102046` (2024-10-21 08:21:04)
- `bootnode-20241021100352` (2024-10-21 08:21:14)
- `bootnode-20241021111431` (2024-10-21 09:20:56)
- `bootnode-20241021040033` (2024-10-21 09:20:59)
- `bootnode-20241021091335` (2024-10-21 09:51:13)
- `bootnode-20241021130444` (2024-10-21 11:21:31)
- `bootnode-20241021062723` (2024-10-21 11:50:55)
- `bootnode-20241021111519` (2024-10-21 11:51:07)
- `bootnode-20241021133454` (2024-10-21 12:51:04)
- `bootnode-20241021113413` (2024-10-21 12:51:30)
- `bootnode-20241021150439` (2024-10-21 13:20:55)
- `kubo/0.32.0-dev/550f464/docker` (2024-10-21 14:51:16)
- `bootnode-20241021084744` (2024-10-21 15:21:23)
- `github.com/harmony-one/harmony@bcc0b51b0` (2024-10-21 16:21:10)
- `bootnode-20241021152423` (2024-10-21 16:50:52)
- `helia/5.0.1 libp2p/2.1.9 UserAgent=v19.7.0` (2024-10-21 16:51:09)
- `bootnode-20241021165537` (2024-10-21 16:51:19)
- `ca-vsc@bc7a65ff1` (2024-10-21 16:51:21)
- `kubo/0.32.0-dev/1cb1537/docker` (2024-10-21 17:50:47)
- `helia/5.0.1 libp2p/2.1.9 UserAgent=v18.20.4` (2024-10-21 17:50:50)
- `bootnode-20241021125045` (2024-10-21 17:50:58)
- `kubo/0.32.0-dev/68b478d/docker` (2024-10-21 18:50:49)
- `bootnode-20241021184539` (2024-10-21 19:20:51)
- `helia/5.0.1 libp2p/2.1.9 UserAgent=v20.18.0` (2024-10-21 19:21:03)
- `bootnode-20241021210523` (2024-10-21 19:21:26)
- `bootnode-20241021214555` (2024-10-21 19:51:01)
- `bootnode-20241021141408` (2024-10-21 19:51:01)
- `bootnode-20241021194619` (2024-10-21 20:21:14)
- `bootnode-20241021145157` (2024-10-21 20:51:05)
- `github.com/zeta-chain/zetacore@c05a91c38-dirty` (2024-10-21 21:21:04)
- `bootnode-20241022001657` (2024-10-21 22:21:20)
- `bootnode-20241021233628` (2024-10-21 23:21:33)
- `bootnode-20241022011732` (2024-10-21 23:50:57)
- `kubo/0.31.0-dev/a17830754` (2024-10-21 23:51:16)
- `bootnode-20241021170447` (2024-10-22 00:21:06)
- `bootnode-20241022002817` (2024-10-22 00:50:59)
- `bootnode-20241021192533` (2024-10-22 00:51:13)
- `bootnode-20241021224534` (2024-10-22 01:21:00)
- `bootnode-20241021201622` (2024-10-22 01:51:02)
- `github.com/zeta-chain/zetacore@b6c5b7a9a-dirty` (2024-10-22 02:20:53)
- `bootnode-20241022020858` (2024-10-22 02:21:00)
- `bootnode-20241022004139` (2024-10-22 02:51:02)
- `bootnode-20241022024918` (2024-10-22 03:21:25)
- `bootnode-20241022021547` (2024-10-22 03:51:04)
- `bootnode-20241022041555` (2024-10-22 04:20:57)
- `bootnode-20241021232016` (2024-10-22 04:20:59)
- `bootnode-20241022033712` (2024-10-22 04:51:09)
- `bootnode-20241022060929` (2024-10-22 05:20:53)
- `bootnode-20241022060122` (2024-10-22 06:51:10)
- `bootnode-20241022072029` (2024-10-22 07:21:04)
- `bootnode-20241022074948` (2024-10-22 07:21:16)
- `bootnode-20241022011103` (2024-10-22 07:21:21)
- `bootnode-20241022105019` (2024-10-22 08:51:06)
- `bootnode-20241022114749` (2024-10-22 09:50:52)
- `bootnode-20241022100432` (2024-10-22 10:21:27)
- `bootnode-20241022112046` (2024-10-22 11:21:28)
- `ca-vsc@bc7a65ff1-dirty` (2024-10-22 13:20:51)
- `bootnode-20241022154834` (2024-10-22 14:20:54)
- `ca-vsc@2728605b9` (2024-10-22 14:21:12)
- `bootnode-20241022155702` (2024-10-22 14:51:23)
- `bootnode-20241022101836` (2024-10-22 15:20:59)
- `github.com/zeta-chain/zetacore@509578fad` (2024-10-22 15:21:16)
- `bootnode-20241022110005` (2024-10-22 16:20:49)
- `bootnode-20241022115328` (2024-10-22 17:21:08)
- `kubo/0.32.0-dev/1fd5ab4/docker` (2024-10-22 18:51:28)
- `github.com/zeta-chain/zetacore@b6c5b7a9a` (2024-10-22 19:20:54)
- `bootnode-20241022203222` (2024-10-22 20:20:56)
- `bootnode-20241022211743` (2024-10-22 22:50:58)
- `kubo/0.32.0-dev/8913a1c/docker` (2024-10-22 22:51:04)
- `bootnode-20241022215846` (2024-10-22 23:20:56)
- `kubo/0.32.0-dev/56c68a1/docker` (2024-10-22 23:51:31)
- `kubo/0.32.0-dev/56c68a1/1234567890123456789012345678901234567890` (2024-10-23 00:21:11)
- `bootnode-20241023010314` (2024-10-23 00:50:58)
- `bootnode-20241023003933` (2024-10-23 00:51:21)
- `github.com/jc-lab/p2p-portforwarder@e20cecfe3-dirty` (2024-10-23 00:51:30)
- `github.com/zeta-chain/zetacore@571b8ae87-dirty` (2024-10-23 01:50:53)
- `xcodv2@` (2024-10-23 03:50:46)
- `bootnode-20241023054826` (2024-10-23 03:50:48)
- `ca-vsc@2a20d5232-dirty` (2024-10-23 05:51:18)
- `bootnode-20241023050350` (2024-10-23 06:51:05)
- `bootnode-20241023034340` (2024-10-23 07:21:34)
- `bootnode-20241023071829` (2024-10-23 07:51:19)
- `github.com/zeta-chain/zetacore@571b8ae87` (2024-10-23 08:20:43)
- `bootnode-20241023024402` (2024-10-23 08:20:53)
- `bootnode-20241023085823` (2024-10-23 09:21:06)
- `bootnode-20241023040452` (2024-10-23 09:21:23)
- `go-test/dev@` (2024-10-23 10:21:09)
- `bootnode-20241023104955` (2024-10-23 10:51:29)
- `bootnode-20241023112019` (2024-10-23 11:20:54)
- `bootnode-20241023124046` (2024-10-23 12:20:50)
- `bootnode-20241023104236` (2024-10-23 12:51:44)
- `bootnode-20241023142750` (2024-10-23 13:21:14)
- `github.com/probe-lab/parsec@040d98067-dirty` (2024-10-23 13:50:47)
- `bootnode-20241023152822` (2024-10-23 13:50:58)
- `bootnode-20241023082335` (2024-10-23 14:51:00)
- `bootnode-20241023081245` (2024-10-23 14:52:30)
- `bootnode-20241023143251` (2024-10-23 15:51:27)
- `bootnode-20241023165450` (2024-10-23 17:51:20)
- `bootnode-20241023130705` (2024-10-23 18:21:40)
- `bootnode-20241023193439` (2024-10-23 19:51:25)
- `bootnode-20241023145854` (2024-10-23 20:21:29)
- `ca-vsc@2a20d5232` (2024-10-23 20:51:42)
- `bootnode-20241023225119` (2024-10-23 21:21:20)
- `bootnode-20241024002002` (2024-10-23 22:20:59)
- `github.com/ethtweet/ethtweet@cd7820130-dirty` (2024-10-23 22:50:43)
- `bootnode-20241024005942` (2024-10-23 23:20:54)
- `bootnode-20241023230712` (2024-10-23 23:51:07)
- `bootnode-20241023223659` (2024-10-23 23:51:29)
- `bootnode-20241024003327` (2024-10-24 00:51:06)
- `bootnode-20241023215334` (2024-10-24 04:51:03)
- `bootnode-20241024072206` (2024-10-24 06:20:58)
- `bootnode-20241024005407` (2024-10-24 06:21:06)
- `bootnode-20241024072044` (2024-10-24 07:21:17)
- `bootnode-20241024083017` (2024-10-24 07:21:32)
- `bootnode-20241024032731` (2024-10-24 08:50:56)
- `bootnode-20241024084529` (2024-10-24 08:51:02)
- `bootnode-20241024094053` (2024-10-24 08:51:37)
- `helia/5.0.0 libp2p/2.1.9 UserAgent=v20.18.0` (2024-10-24 09:51:00)
- `bootnode-20241024114400` (2024-10-24 10:21:35)
- `bootnode-20241024045859` (2024-10-24 10:51:20)
- `bootnode-20241024110119` (2024-10-24 11:21:24)
- `bootnode-20241024075002` (2024-10-24 12:51:02)
- `bootnode-20241024132423` (2024-10-24 14:20:51)
- `bootnode-20241024135705` (2024-10-24 14:21:03)
- `bootnode-20241024144952` (2024-10-24 14:50:46)
- `bootnode-20241024154136` (2024-10-24 15:21:08)
- `github.com/JackalLabs/sequoia@aab3a317b` (2024-10-24 15:21:21)
- `bootnode-20241024154254` (2024-10-24 15:51:34)
- `fsp2p@b9807d1f1-dirty` (2024-10-24 16:21:03)
- `bootnode-20241024094112` (2024-10-24 16:21:03)
- `bootnode-20241024182020` (2024-10-24 18:20:49)
- `bootnode-20241024191516` (2024-10-24 18:21:39)
- `bootnode-20241024171901` (2024-10-24 19:21:31)
- `bootnode-20241024154457` (2024-10-24 20:51:10)
- `bootnode-20241024223635` (2024-10-24 22:52:22)
- `bootnode-20241024235424` (2024-10-24 23:23:00)
- `bootnode-20241024182911` (2024-10-25 01:21:03)
- `bootnode-20241025024756` (2024-10-25 01:51:09)
- `bootnode-20241025024324` (2024-10-25 02:21:39)
- `bootnode-20241025054627` (2024-10-25 03:51:34)
- `bootnode-20241025050342` (2024-10-25 05:20:57)
- `bootnode-20241025070855` (2024-10-25 05:21:01)
- `bootnode-20241025070439` (2024-10-25 07:22:08)
- `bootnode-20241025055216` (2024-10-25 07:22:10)
- `helia/5.1.0 libp2p/2.1.10 UserAgent=v20.12.2` (2024-10-25 08:21:09)
- `bootnode-20241025084244` (2024-10-25 08:50:56)
- `bootnode-20241025095528` (2024-10-25 10:21:21)
- `bootnode-20241025105352` (2024-10-25 11:20:53)
- `kubo/0.31.0/5a32936f7-dirty` (2024-10-25 14:20:45)
- `bootnode-20241025115504` (2024-10-25 17:21:00)
- `bootnode-20241025183047` (2024-10-25 17:21:05)
- `bootnode-20241025183019` (2024-10-25 17:51:28)
- `bootnode-20241025121735` (2024-10-25 17:51:42)
- `bootnode-20241025173824` (2024-10-25 18:51:25)
- `bootnode-20241025191550` (2024-10-25 19:21:15)
- `bootnode-20241025140928` (2024-10-25 19:21:19)
- `kubo/0.32.0-dev/ecb81c9/docker` (2024-10-25 19:51:04)
- `bootnode-20241025192705` (2024-10-25 19:51:21)
- `bootnode-20241025204739` (2024-10-25 20:51:17)
- `bootnode-20241025212034` (2024-10-25 21:20:49)
- `kubo/0.30.0/846c5ccf6-dirty/docker` (2024-10-25 21:21:58)
- `bootnode-20241025210752` (2024-10-25 21:51:11)
- `bootnode-20241025161015` (2024-10-25 21:51:28)
- `github.com/JackalLabs/sequoia@aab3a317b-dirty` (2024-10-25 22:20:56)
- `bootnode-20241026004114` (2024-10-25 23:21:01)
- `bootnode-20241025172115` (2024-10-25 23:21:13)
- `bootnode-20241025230817` (2024-10-25 23:21:14)
- `bootnode-20241025180818` (2024-10-25 23:50:54)
- `bootnode-20241025194330` (2024-10-26 00:51:06)
- `bootnode-20241026000142` (2024-10-26 01:21:07)
- `bootnode-20241026020909` (2024-10-26 02:20:57)
- `bootnode-20241025204015` (2024-10-26 03:20:52)
- `bootnode-20241026024217` (2024-10-26 03:50:53)
- `bootnode-20241026041036` (2024-10-26 04:21:26)
- `bootnode-20241026040238` (2024-10-26 04:21:39)
- `bootnode-20241026052051` (2024-10-26 05:21:10)
- `bootnode-20241025232155` (2024-10-26 05:51:11)
- `bootnode-20241026054207` (2024-10-26 06:51:17)
- `bootnode-20241026083318` (2024-10-26 07:21:37)
- `bootnode-20241026090713` (2024-10-26 07:21:43)
- `helia/5.1.0 libp2p/2.1.10 UserAgent=v22.9.0` (2024-10-26 08:51:09)
- `kubo/0.23.0/84d238954` (2024-10-26 08:51:31)
- `bootnode-20241026105721` (2024-10-26 09:21:41)
- `bootnode-20241026120348` (2024-10-26 10:51:30)
- `bootnode-20241026131459` (2024-10-26 11:21:06)
- `bootnode-20241026061421` (2024-10-26 11:51:07)
- `bootnode-20241026072949` (2024-10-26 12:51:12)
- `bootnode-20241026083057` (2024-10-26 13:51:01)
- `bootnode-20241026085510` (2024-10-26 14:21:03)
- `bootnode-20241026151746` (2024-10-26 14:51:14)
- `bootnode-20241026152511` (2024-10-26 17:21:40)
- `bootnode-20241026130520` (2024-10-26 18:21:51)
- `bootnode-20241026211736` (2024-10-26 19:51:59)
- `xv4@` (2024-10-26 20:21:09)
- `bootnode-20241026153805` (2024-10-26 20:51:04)
- `bootnode-20241026204308` (2024-10-26 21:21:02)
- `bootnode-20241026144557` (2024-10-26 21:21:08)
- `bootnode-20241026233807` (2024-10-26 21:51:10)
- `bootnode-20241026174844` (2024-10-26 22:51:21)
- `bootnode-20241027005915` (2024-10-27 01:21:16)
- `bootnode-20241026203719` (2024-10-27 01:51:10)
- `bootnode-20241027022832` (2024-10-27 02:20:52)
- `bootnode-20241026203920` (2024-10-27 02:20:57)
- `bootnode-20241027022846` (2024-10-27 04:21:21)
- `bootnode-20241027072611` (2024-10-27 06:51:03)
- `bootnode-20241027022250` (2024-10-27 07:51:37)
- `bootnode-20241027035345` (2024-10-27 09:51:14)
- `bootnode-20241027102039` (2024-10-27 10:20:59)
- `bootnode-20241027103105` (2024-10-27 10:51:11)
- `helia/5.1.0 libp2p/2.1.10 UserAgent=v18.19.1` (2024-10-27 11:51:12)
- `bootnode-20241027125132` (2024-10-27 12:21:44)
- `bootnode-20241027080434` (2024-10-27 13:20:52)
- `bootnode-20241027134800` (2024-10-27 13:51:29)
- `bootnode-20241027145834` (2024-10-27 15:20:57)
- `bootnode-20241027114641` (2024-10-27 16:51:17)
- `bootnode-20241027120740` (2024-10-27 17:21:22)
- `bootnode-20241027183003` (2024-10-27 18:51:20)
- `bootnode-20241027194940` (2024-10-27 19:20:52)
- `bootnode-20241027161935` (2024-10-27 21:20:52)
- `bootnode-20241027163922` (2024-10-27 22:21:27)
- `bootnode-20241027223536` (2024-10-27 23:21:19)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/matrixp2p` (2024-10-21 07:51:04)
- `/p2p/join-party-leader` (2024-10-21 21:21:04)
- `/p2p/tss` (2024-10-21 21:21:04)
- `/p2p/join-party` (2024-10-21 21:21:04)
- `/p2p/signatureNotifier` (2024-10-21 21:21:04)
- `/tari_direct_peer_info/4` (2024-10-22 19:20:57)
- `/share_chain_sync/4` (2024-10-22 19:20:57)
- `/example/message/1.0.0` (2024-10-24 05:50:53)
- `/catch_up_sync/4` (2024-10-26 11:51:33)
- `/myapp/messagesync/1.0.0` (2024-10-26 20:21:09)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `157.173.99.87` | GB | 1596 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| False  |
| `51.159.150.159` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `94.141.101.36` | AM | 79 | ['rust-libp2p/0.45.0']| False  |
| `51.159.174.206` | FR | 76 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 75 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.247.127` | FR | 74 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 73 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 73 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `152.81.47.227` | FR | 72 | ['kubo/0.28.0/', 'kubo/0.31.0/']| False  |
| `5.135.162.92` | FR | 70 | ['kubo/0.16.0/', 'rust-libp2p/0.45.0']| True  |

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

In the specified time interval from `2024-10-21` to `2024-10-28` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-10-21` to `2024-10-28` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-10-21` to `2024-10-28` in the DHT and their datacenter association.

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