# Nebula Measurement Results Calendar Week 44 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 44 - 2024](#nebula-measurement-results-calendar-week-44---2024)
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

The following results show measurement data that were collected in calendar week 44 in 2024 from `2024-10-28` to `2024-11-04`.

- Number of crawls `336`
- Number of visits `29,147,053`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `56,102`
- Number of unique peer IDs discovered in the DHT `54,791`
- Number of unique IP addresses found `45,090`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20241028003004` (2024-10-28 00:21:01)
- `bootnode-20241028001150` (2024-10-28 00:50:55)
- `bootnode-20241027203030` (2024-10-28 01:51:08)
- `bootnode-20241028013716` (2024-10-28 02:21:06)
- `bootnode-20241028033235` (2024-10-28 02:51:23)
- `bootnode-20241027222030` (2024-10-28 03:21:08)
- `bootnode-20241028032900` (2024-10-28 03:51:38)
- `bootnode-20241028043257` (2024-10-28 04:21:34)
- `bootnode-20241028030030` (2024-10-28 04:50:53)
- `bootnode-20241027233311` (2024-10-28 05:21:01)
- `bootnode-20241028000049` (2024-10-28 05:21:06)
- `bootnode-20241028064337` (2024-10-28 07:21:28)
- `bootnode-20241028072055` (2024-10-28 07:21:28)
- `bootnode-20241028070917` (2024-10-28 07:51:33)
- `bootnode-20241028084247` (2024-10-28 08:51:09)
- `bootnode-20241028092055` (2024-10-28 10:21:08)
- `bootnode-20241028013105` (2024-10-28 10:51:06)
- `libp2p/2.1.10 UserAgent=v20.18.0` (2024-10-28 10:51:37)
- `bootnode-20241028104953` (2024-10-28 11:51:40)
- `bootnode-20241028113116` (2024-10-28 12:21:04)
- `kubo/0.32.0-dev/21b5c88/collab.ipfscluster.io` (2024-10-28 12:21:07)
- `bootnode-20241028062518` (2024-10-28 12:51:24)
- `bootnode-20241028144115` (2024-10-28 14:21:34)
- `github.com/harmony-one/harmony@7711bee87` (2024-10-28 14:50:52)
- `bootnode-20241028085843` (2024-10-28 14:51:19)
- `bootnode-20241028150522` (2024-10-28 15:20:56)
- `bootnode-20241028101902` (2024-10-28 15:21:05)
- `bootnode-20241028160402` (2024-10-28 15:22:10)
- `bootnode-20241028160140` (2024-10-28 15:51:14)
- `bootnode-20241028180505` (2024-10-28 17:21:09)
- `bootnode-20241028112918` (2024-10-28 17:21:44)
- `kubo/0.31.0-dev/836d516` (2024-10-28 17:51:15)
- `bootnode-20241028192157` (2024-10-28 18:50:59)
- `bootnode-20241028191147` (2024-10-28 20:21:35)
- `bootnode-20241028152109` (2024-10-28 21:21:11)
- `bootnode-20241028205433` (2024-10-28 22:21:02)
- `bootnode-20241028232457` (2024-10-28 23:21:20)
- `bootnode-20241028223623` (2024-10-28 23:21:29)
- `kubo/0.32.0-dev/e51d90785` (2024-10-28 23:50:54)
- `bootnode-20241028185444` (2024-10-29 00:21:03)
- `bootnode-20241029021303` (2024-10-29 01:51:01)
- `bootnode-20241028191400` (2024-10-29 02:21:03)
- `bootnode-20241029023629` (2024-10-29 02:51:12)
- `bootnode-20241029042017` (2024-10-29 03:20:50)
- `bootnode-20241029024622` (2024-10-29 03:21:23)
- `bootnode-20241029025742` (2024-10-29 03:21:24)
- `bootnode-20241028215645` (2024-10-29 03:21:28)
- `bootnode-20241029055343` (2024-10-29 05:20:54)
- `bootnode-20241029051909` (2024-10-29 05:21:08)
- `bootnode-20241029010436` (2024-10-29 06:21:48)
- `bootnode-20241029044713` (2024-10-29 06:21:50)
- `github.com/harmony-one/harmony@c3951262b` (2024-10-29 06:50:57)
- `bootnode-20241029051052` (2024-10-29 07:21:32)
- `bootnode-20241029073845` (2024-10-29 08:50:57)
- `kubo/0.32.0-dev/e51d907/collab.ipfscluster.io` (2024-10-29 08:51:24)
- `bootnode-20241029024531` (2024-10-29 09:21:07)
- `bootnode-20241029093120` (2024-10-29 09:21:19)
- `someguy/v0.5.2 2024-10-23-94cc5f7` (2024-10-29 09:51:02)
- `bootnode-20241029045829` (2024-10-29 10:21:27)
- `bootnode-20241029084815` (2024-10-29 12:21:16)
- `bootnode-20241029065937` (2024-10-29 12:21:24)
- `bootnode-20241029053555` (2024-10-29 12:21:43)
- `bootnode-20241029075531` (2024-10-29 12:51:04)
- `bootnode-20241029121926` (2024-10-29 12:51:19)
- `bootnode-20241029123230` (2024-10-29 13:51:12)
- `bootnode-20241029123357` (2024-10-29 16:20:56)
- `libp2p/1.3.3 UserAgent=v22.10.0` (2024-10-29 16:21:02)
- `bootnode-20241029161031` (2024-10-29 16:21:10)
- `bootnode-20241029102609` (2024-10-29 16:21:35)
- `kubo/0.32.0-dev/e68493ab3` (2024-10-29 17:20:52)
- `bootnode-20241029174626` (2024-10-29 17:21:22)
- `bootnode-20241029165710` (2024-10-29 18:21:16)
- `bootnode-20241029215430` (2024-10-29 21:51:17)
- `bootnode-20241029163903` (2024-10-29 22:21:12)
- `bootnode-20241029212718` (2024-10-29 22:21:17)
- `kubo/0.32.0-dev/3134fd2/docker` (2024-10-29 22:51:25)
- `bootnode-20241029204729` (2024-10-29 23:21:04)
- `bootnode-20241030002455` (2024-10-30 02:21:09)
- `bootnode-20241030032758` (2024-10-30 02:51:00)
- `bootnode-20241029212631` (2024-10-30 03:20:55)
- `github.com/JackalLabs/sequoia@d7fb2a0bd` (2024-10-30 03:20:56)
- `bootnode-20241029193722` (2024-10-30 05:21:09)
- `bootnode-20241029225721` (2024-10-30 05:51:09)
- `ca-vsc@d16b2c250` (2024-10-30 07:50:43)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v20.11.0` (2024-10-30 08:20:55)
- `go-ipfs/0.11.0-rc1/` (2024-10-30 08:21:03)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v16.20.2` (2024-10-30 08:21:30)
- `helia/4.2.0 libp2p/1.5.1 UserAgent=v22.10.0` (2024-10-30 10:50:57)
- `bootnode-20241030100342` (2024-10-30 10:50:59)
- `libp2p/2.2.1 UserAgent=v20.18.0` (2024-10-30 11:21:07)
- `bootnode-20241030113221` (2024-10-30 11:51:30)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v20.10.0` (2024-10-30 11:51:38)
- `kubo/0.32.0-dev/3134fd246` (2024-10-30 11:51:43)
- `bootnode-20241030141844` (2024-10-30 13:20:59)
- `bootnode-20241030054748` (2024-10-30 13:21:00)
- `bootnode-20241030133107` (2024-10-30 13:51:07)
- `kubo/0.32.0-dev/3134fd2/1234567890123456789012345678901234567890` (2024-10-30 13:51:28)
- `libp2p/1.3.3 UserAgent=v22.11.0` (2024-10-30 14:21:08)
- `bootnode-20241030143455` (2024-10-30 14:51:18)
- `kubo/0.32.0-dev/8c41c4d/docker` (2024-10-30 16:50:55)
- `bootnode-20241030182047` (2024-10-30 17:20:59)
- `kubo/0.32.0-rc1/60fa6cd/1234567890123456789012345678901234567890` (2024-10-30 17:21:17)
- `kubo/0.32.0-dev/caa8844/docker` (2024-10-30 17:50:53)
- `bootnode-20241030173545` (2024-10-30 17:50:58)
- `kubo/0.33.0-dev/` (2024-10-30 18:20:50)
- `bootnode-20241030171319` (2024-10-30 18:21:05)
- `kubo/0.33.0-dev/c5586d5/docker` (2024-10-30 18:50:55)
- `kubo/0.32.0-rc1/` (2024-10-30 19:21:34)
- `bootnode-20241030195908` (2024-10-30 20:51:14)
- `kubo/0.33.0-dev/1ca0ae0/docker` (2024-10-30 22:51:04)
- `bootnode-20241030231937` (2024-10-30 23:21:32)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v22.10.0` (2024-10-30 23:51:33)
- `bootnode-20241030210610` (2024-10-31 00:51:04)
- `bootnode-20241030173327` (2024-10-31 00:51:04)
- `bootnode-20241031025009` (2024-10-31 01:51:22)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v20.17.0` (2024-10-31 01:51:22)
- `bootnode-20241030212616` (2024-10-31 02:50:52)
- `bootnode-20241031022726` (2024-10-31 03:21:08)
- `bootnode-20241031045036` (2024-10-31 03:51:05)
- `bootnode-20241031002634` (2024-10-31 05:51:17)
- `kubo/0.32.0-rc1/60fa6cd/docker` (2024-10-31 07:50:51)
- `bootnode-20241031032013` (2024-10-31 08:20:50)
- `bootnode-20241031092943` (2024-10-31 08:51:02)
- `bootnode-20241031083904` (2024-10-31 09:21:43)
- `bootnode-20241031100739` (2024-10-31 09:50:54)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v21.7.3` (2024-10-31 11:21:42)
- `bootnode-20241031111359` (2024-10-31 12:21:12)
- `bootnode-20241031123048` (2024-10-31 12:21:23)
- `bootnode-20241031133757` (2024-10-31 12:50:58)
- `bootnode-20241031055844` (2024-10-31 13:50:51)
- `bootnode-20241031120442` (2024-10-31 14:50:54)
- `bootnode-20241031104108` (2024-10-31 15:51:00)
- `bootnode-20241031095053` (2024-10-31 18:21:04)
- `bootnode-20241031181548` (2024-10-31 18:50:54)
- `bootnode-20241031173142` (2024-10-31 19:51:38)
- `bootnode-20241031150249` (2024-10-31 20:21:07)
- `ca-vsc@cefab5caa` (2024-10-31 20:50:48)
- `bootnode-20241031182908` (2024-10-31 20:50:53)
- `bootnode-20241031222028` (2024-10-31 21:20:52)
- `bootnode-20241031153137` (2024-10-31 21:20:57)
- `bootnode-20241031212053` (2024-10-31 21:20:59)
- `bootnode-20241031205625` (2024-10-31 21:50:54)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.18.0` (2024-10-31 21:51:22)
- `bootnode-20241031222051` (2024-10-31 22:21:42)
- `bootnode-20241101000201` (2024-10-31 23:21:16)
- `bootnode-20241031190408` (2024-11-01 00:20:52)
- `kubo/0.32.0-dev/e68493a/collab.ipfscluster.io` (2024-11-01 01:20:58)
- `bootnode-20241101011226` (2024-11-01 01:21:06)
- `bootnode-20241031213734` (2024-11-01 02:50:54)
- `bootnode-20241101034858` (2024-11-01 03:51:33)
- `bootnode-20241101050313` (2024-11-01 04:21:00)
- `bootnode-20241101041813` (2024-11-01 04:21:11)
- `bootnode-20241101010040` (2024-11-01 06:21:08)
- `bootnode-20241101042152` (2024-11-01 06:21:09)
- `bootnode-20241101015014` (2024-11-01 06:50:54)
- `kubo/0.31.0/f40ad1302` (2024-11-01 06:51:32)
- `p2pnet@-dirty` (2024-11-01 07:20:48)
- `bootnode-20241101012504` (2024-11-01 07:20:52)
- `bootnode-20241101055351` (2024-11-01 07:51:00)
- `bootnode-20241101082208` (2024-11-01 07:51:06)
- `kubo/0.31.0/f40ad13` (2024-11-01 08:20:57)
- `github.com/libp2p/universal-connectivity/go-peer@370dbbacd` (2024-11-01 08:50:51)
- `bootnode-20241101063410` (2024-11-01 08:51:06)
- `kubo/0.31.0/09bbc1c6a-dirty` (2024-11-01 08:51:19)
- `bootnode-20241101052028` (2024-11-01 10:20:58)
- `bootnode-20241101103431` (2024-11-01 10:50:54)
- `bootnode-20241101112227` (2024-11-01 10:50:59)
- `bootnode-20241101072042` (2024-11-01 12:21:14)
- `bootnode-20241101065916` (2024-11-01 12:50:59)
- `bootnode-20241101133757` (2024-11-01 13:51:12)
- `bootnode-20241101145447` (2024-11-01 14:21:39)
- `bootnode-20241101133527` (2024-11-01 15:20:56)
- `bootnode-20241101122018` (2024-11-01 15:21:41)
- `bootnode-20241101170420` (2024-11-01 16:20:53)
- `bootnode-20241101153203` (2024-11-01 16:51:09)
- `bootnode-20241101112643` (2024-11-01 16:51:24)
- `bootnode-20241101172524` (2024-11-01 19:21:14)
- `bootnode-20241101144830` (2024-11-01 20:20:56)
- `bootnode-20241101173602` (2024-11-01 21:51:27)
- `bootnode-20241101214454` (2024-11-01 22:21:02)
- `bootnode-20241101195833` (2024-11-01 22:21:42)
- `bootnode-20241101224846` (2024-11-01 22:50:58)
- `bootnode-20241101235342` (2024-11-01 23:50:58)
- `bootnode-20241102002917` (2024-11-02 00:51:23)
- `bootnode-20241102034040` (2024-11-02 03:50:48)
- `bootnode-20241102040411` (2024-11-02 03:51:13)
- `bootnode-20241102035107` (2024-11-02 03:51:15)
- `kubo/0.31.0/qkpay` (2024-11-02 04:21:02)
- `bootnode-20241102031541` (2024-11-02 06:21:48)
- `bootnode-20241102025046` (2024-11-02 07:50:57)
- `bootnode-20241102095838` (2024-11-02 09:20:59)
- `bootnode-20241102083526` (2024-11-02 09:21:09)
- `p2proxy@cb68693d7` (2024-11-02 09:52:05)
- `bootnode-20241102090600` (2024-11-02 11:51:31)
- `bootnode-20241102073226` (2024-11-02 12:51:32)
- `bootnode-20241101110252` (2024-11-02 17:21:07)
- `bootnode-20241102181621` (2024-11-02 18:51:14)
- `bootnode-20241102192109` (2024-11-02 18:51:28)
- `github.com/ethtweet/ethtweet@3f690b1e3-dirty` (2024-11-02 20:21:07)
- `bootnode-20241102182533` (2024-11-02 20:50:56)
- `bootnode-20241102210744` (2024-11-02 23:51:01)
- `bootnode-20241102185537` (2024-11-03 00:21:04)
- `kubo/0.33.0-dev/1ca0ae0af-dirty/docker` (2024-11-03 00:51:00)
- `bootnode-20241102220745` (2024-11-03 02:21:08)
- `bootnode-20241103031759` (2024-11-03 03:21:39)
- `bootnode-20241103040719` (2024-11-03 04:21:35)
- `bootnode-20241103052924` (2024-11-03 04:51:06)
- `bootnode-20241103054853` (2024-11-03 05:50:54)
- `bootnode-20241103013508` (2024-11-03 08:20:48)
- `bootnode-20241103085943` (2024-11-03 08:20:49)
- `bootnode-20241103041857` (2024-11-03 10:20:48)
- `kubo/0.27.0-dev/9343a95/docker` (2024-11-03 12:21:20)
- `bootnode-20241103111228` (2024-11-03 13:21:04)
- `bootnode-20241103055011` (2024-11-03 13:21:10)
- `bootnode-20241103110241` (2024-11-03 14:21:32)
- `bootnode-20241103092736` (2024-11-03 16:21:04)
- `bootnode-20241103163940` (2024-11-03 16:50:57)
- `bootnode-20241103170050` (2024-11-03 17:21:22)
- `bootnode-20241103192021` (2024-11-03 18:21:00)
- `bootnode-20241103174415` (2024-11-03 18:50:53)
- `bootnode-20241103190256` (2024-11-03 19:51:10)
- `bootnode-20241103195006` (2024-11-03 19:51:12)
- `bootnode-20241103202021` (2024-11-03 20:20:49)
- `bootnode-20241103205326` (2024-11-03 21:51:09)
- `bootnode-20241103163007` (2024-11-03 22:50:52)
- `bootnode-20241103153925` (2024-11-03 23:51:32)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/postPoint` (2024-10-30 01:20:56)
- `/postPsig` (2024-10-30 01:20:56)
- `/getSK` (2024-10-30 01:20:56)
- `/example/message/1.0.1` (2024-10-30 03:20:46)
- `/orbitdb/heads/orbitdb/zdpuB2MBW2ctobk5qGgh3Lt1X7pL3x1dCQ5WrubHecMPRFEfL` (2024-11-01 16:21:35)
- `/orbitdb/heads/orbitdb/zdpuB3CRTZeKigwNxeMjdfhsBnbNHFAnBtqz9WwePiqS3ZEeA` (2024-11-01 16:21:35)
- `/orbitdb/heads/orbitdb/zdpuAnPfSXKbFi3aPiABdHbaGyeseqnwDKF7SpLCbaH1T7odm` (2024-11-01 16:21:35)
- `TransformerConnectionHandler.rpc_backward` (2024-11-02 02:21:04)
- `TransformerConnectionHandler.rpc_inference` (2024-11-02 02:21:04)
- `TransformerConnectionHandler.rpc_info` (2024-11-02 02:21:04)
- `TransformerConnectionHandler.rpc_backward_stream` (2024-11-02 02:21:04)
- `TransformerConnectionHandler.rpc_forward` (2024-11-02 02:21:04)
- `TransformerConnectionHandler.rpc_forward_stream` (2024-11-02 02:21:04)
- `TransformerConnectionHandler.rpc_push` (2024-11-02 02:21:04)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `157.173.99.87` | GB | 1653 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| False  |
| `82.180.162.171` | US | 505 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.22.0/3f884d3/gala.games', 'kubo/0.30.0/846c5cc']| False  |
| `2001:41d0:8:e55c::1` | FR | 128 | ['helia/3.0.0 libp2p/1.1.1 UserAgent=v18.15.0', 'kubo/0.16.0/', 'kubo/0.29.0/brave', 'rust-libp2p/0.45.0']| True  |
| `5.135.162.92` | FR | 128 | ['helia/3.0.0 libp2p/1.1.1 UserAgent=v18.15.0', 'kubo/0.16.0/', 'kubo/0.29.0/brave', 'rust-libp2p/0.45.0']| True  |
| `172.98.12.34` | US | 112 | ['go-ipfs/0.11.0/d6518322f4', 'kubo/0.22.0/3f884d3/gala.games', 'rust-libp2p/0.45.0']| False  |
| `162.55.191.65` | DE | 83 | ['go-ipfs/0.11.0/67220ed', 'go-ipfs/0.11.0/67220ed/docker', 'rust-libp2p/0.44.2', 'rust-libp2p/0.45.0']| True  |
| `51.159.150.159` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 72 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 71 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 70 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-10-28` to `2024-11-04` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-10-28` to `2024-11-04` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-10-28` to `2024-11-04` in the DHT and their datacenter association.

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