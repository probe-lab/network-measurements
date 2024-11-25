# Nebula Measurement Results Calendar Week 47 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 47 - 2024](#nebula-measurement-results-calendar-week-47---2024)
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

The following results show measurement data that were collected in calendar week 47 in 2024 from `2024-11-18` to `2024-11-25`.

- Number of crawls `332`
- Number of visits `22,034,071`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `51,857`
- Number of unique peer IDs discovered in the DHT `50,519`
- Number of unique IP addresses found `40,669`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20241118015104` (2024-11-18 00:51:23)
- `bootnode-20241118020834` (2024-11-18 01:21:10)
- `bootnode-20241118010058` (2024-11-18 01:21:23)
- `bootnode-20241117190115` (2024-11-18 01:21:31)
- `bootnode-20241118013706` (2024-11-18 01:51:15)
- `bootnode-20241118021442` (2024-11-18 02:51:18)
- `bootnode-20241118035014` (2024-11-18 03:51:00)
- `bootnode-20241118042058` (2024-11-18 04:21:21)
- `bootnode-20241118031931` (2024-11-18 04:22:38)
- `bootnode-20241117224604` (2024-11-18 05:21:16)
- `bootnode-20241118055120` (2024-11-18 05:51:37)
- `bootnode-20241118062115` (2024-11-18 06:22:08)
- `bootnode-20241118065044` (2024-11-18 06:51:12)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36` (2024-11-18 08:21:11)
- `bootnode-20241118082110` (2024-11-18 08:21:18)
- `bootnode-20241118020010` (2024-11-18 09:21:21)
- `bootnode-20241118104034` (2024-11-18 09:51:02)
- `bootnode-20241118095104` (2024-11-18 09:51:15)
- `bootnode-20241118033030` (2024-11-18 09:51:17)
- `bootnode-20241118093059` (2024-11-18 09:52:06)
- `bootnode-20241118100824` (2024-11-18 10:21:05)
- `bootnode-20241118090247` (2024-11-18 10:21:08)
- `MessageMesh@fbdd75964-dirty` (2024-11-18 10:21:29)
- `bootnode-20241118112022` (2024-11-18 10:22:01)
- `kubo/0.32.1/4f411d1fa-dirty` (2024-11-18 10:50:55)
- `bootnode-20241118115112` (2024-11-18 11:51:20)
- `bootnode-20241118062042` (2024-11-18 12:21:04)
- `bootnode-20241118122105` (2024-11-18 12:21:26)
- `bootnode-20241118142137` (2024-11-18 13:22:09)
- `bootnode-20241118142041` (2024-11-18 14:20:56)
- `bootnode-20241118145920` (2024-11-18 14:21:07)
- `bootnode-20241118155029` (2024-11-18 14:51:15)
- `bootnode-20241118152135` (2024-11-18 15:21:59)
- `bootnode-20241118165030` (2024-11-18 15:51:14)
- `bootnode-20241118100132` (2024-11-18 16:51:27)
- `bootnode-20241118180809` (2024-11-18 17:21:06)
- `bootnode-20241118165953` (2024-11-18 17:51:00)
- `bootnode-20241118182057` (2024-11-18 18:21:14)
- `bootnode-20241118185357` (2024-11-18 18:21:30)
- `bootnode-20241118184703` (2024-11-18 19:21:02)
- `bootnode-20241118192144` (2024-11-18 19:22:05)
- `helia/5.1.0 libp2p/2.3.1 UserAgent=v20.16.0` (2024-11-18 20:21:43)
- `bootnode-20241118203954` (2024-11-18 20:51:20)
- `bootnode-20241118200736` (2024-11-18 20:51:59)
- `kubo/0.33.0-dev/9e4395a8c` (2024-11-18 20:52:02)
- `kubo/0.33.0-dev/9e4395a8c-dirty` (2024-11-18 21:21:01)
- `bootnode-20241118212120` (2024-11-18 21:21:37)
- `bootnode-20241118151515` (2024-11-18 21:50:54)
- `bootnode-20241118225021` (2024-11-18 21:51:20)
- `bootnode-20241118214207` (2024-11-18 21:51:48)
- `bootnode-20241118222047` (2024-11-18 22:21:50)
- `bootnode-20241118232115` (2024-11-18 23:21:26)
- `bootnode-20241118223102` (2024-11-18 23:22:02)
- `bootnode-20241118184114` (2024-11-19 00:50:58)
- `bootnode-20241119001801` (2024-11-19 00:51:14)
- `bootnode-20241119020947` (2024-11-19 01:21:16)
- `kubo/0.32.1/9017453/collab.ipfscluster.io` (2024-11-19 02:51:26)
- `bootnode-20241119040309` (2024-11-19 03:21:24)
- `bootnode-20241119042719` (2024-11-19 03:50:58)
- `bootnode-20241118211145` (2024-11-19 03:51:06)
- `bootnode-20241119045814` (2024-11-19 04:20:56)
- `bootnode-20241119035527` (2024-11-19 04:51:18)
- `bootnode-20241118230548` (2024-11-19 06:21:07)
- `bootnode-20241119001043` (2024-11-19 07:20:54)
- `bootnode-20241119072555` (2024-11-19 08:20:51)
- `bootnode-20241119085911` (2024-11-19 08:21:06)
- `bootnode-20241119081653` (2024-11-19 08:21:15)
- `bootnode-20241119084109` (2024-11-19 08:51:40)
- `kubo/0.32.1/qkpay` (2024-11-19 09:21:08)
- `bootnode-20241119095106` (2024-11-19 09:51:10)
- `bootnode-20241119051956` (2024-11-19 11:21:18)
- `bootnode-20241119123553` (2024-11-19 11:50:55)
- `bootnode-20241119061005` (2024-11-19 12:21:09)
- `bootnode-20241119125112` (2024-11-19 12:51:20)
- `bootnode-20241119145223` (2024-11-19 14:50:58)
- `bootnode-20241119150823` (2024-11-19 15:21:05)
- `bootnode-20241119162130` (2024-11-19 16:22:07)
- `bootnode-20241119163856` (2024-11-19 16:51:14)
- `bootnode-20241119173718` (2024-11-19 17:50:57)
- `kubo/0.33.0-dev/3a1b8ee/docker` (2024-11-19 17:51:09)
- `bootnode-20241119174047` (2024-11-19 18:21:56)
- `ca-vsc@1a5962c94` (2024-11-19 18:22:50)
- `bootnode-20241119183310` (2024-11-19 18:50:57)
- `kubo/0.33.0-dev/d506003/docker` (2024-11-19 18:51:57)
- `bootnode-20241119205011` (2024-11-19 19:50:54)
- `bootnode-20241119203137` (2024-11-19 19:51:01)
- `kubo/0.32.1/9017453/bootstrap.libp2p.io` (2024-11-19 20:50:40)
- `bootnode-20241119152102` (2024-11-19 21:21:30)
- `bootnode-20241119190803` (2024-11-19 21:22:03)
- `bootnode-20241119230439` (2024-11-19 22:21:31)
- `bootnode-20241119225052` (2024-11-19 22:50:58)
- `bootnode-20241119232601` (2024-11-19 22:51:05)
- `bootnode-20241119163114` (2024-11-19 22:51:49)
- `bootnode-20241119165011` (2024-11-19 23:21:09)
- `bootnode-20241120000809` (2024-11-19 23:22:02)
- `bootnode-20241119232625` (2024-11-19 23:51:06)
- `bootnode-20241120004930` (2024-11-19 23:51:58)
- `bootnode-20241119170129` (2024-11-19 23:52:10)
- `bootnode-20241119174026` (2024-11-20 00:21:18)
- `bootnode-20241120013400` (2024-11-20 00:51:09)
- `bootnode-20241119180224` (2024-11-20 00:51:21)
- `bootnode-20241120014111` (2024-11-20 01:51:24)
- `bootnode-20241120025430` (2024-11-20 02:21:55)
- `bootnode-20241120032421` (2024-11-20 02:50:53)
- `bootnode-20241119203642` (2024-11-20 03:20:57)
- `bootnode-20241120042035` (2024-11-20 04:21:04)
- `bootnode-20241120052437` (2024-11-20 04:50:59)
- `bootnode-20241120054040` (2024-11-20 04:51:31)
- `github.com/libp2p/go-libp2p/examples@08f9d22f9` (2024-11-20 06:21:22)
- `bootnode-20241120062116` (2024-11-20 06:21:29)
- `bootnode-20241120060657` (2024-11-20 06:22:05)
- `ca-vsc@bb95140e8` (2024-11-20 06:22:16)
- `bootnode-20241120062659` (2024-11-20 06:51:00)
- `bootnode-20241120071356` (2024-11-20 06:51:25)
- `github.com/harmony-one/harmony@e103771b1` (2024-11-20 07:21:42)
- `bootnode-20241120020429` (2024-11-20 08:21:06)
- `bootnode-20241120022031` (2024-11-20 08:21:22)
- `bootnode-20241120065302` (2024-11-20 08:22:13)
- `p2proxy@e8eb46744-dirty` (2024-11-20 09:20:51)
- `bootnode-20241120092058` (2024-11-20 09:21:08)
- `bootnode-20241120092254` (2024-11-20 09:21:08)
- `bootnode-20241120095004` (2024-11-20 09:50:53)
- `bootnode-20241120092511` (2024-11-20 09:51:06)
- `bootnode-20241120105040` (2024-11-20 10:51:00)
- `bootnode-20241120103425` (2024-11-20 10:51:55)
- `bootnode-20241120125019` (2024-11-20 12:51:17)
- `bootnode-20241120112810` (2024-11-20 12:51:20)
- `bootnode-20241120132518` (2024-11-20 13:22:41)
- `bootnode-20241120144945` (2024-11-20 14:50:57)
- `bootnode-20241120152109` (2024-11-20 15:21:35)
- `bootnode-20241120100950` (2024-11-20 16:21:12)
- `bootnode-20241120155019` (2024-11-20 16:21:28)
- `bootnode-20241120150520` (2024-11-20 16:51:57)
- `bootnode-20241120164049` (2024-11-20 16:52:00)
- `bootnode-20241120110955` (2024-11-20 17:21:15)
- `bootnode-20241120172103` (2024-11-20 17:51:41)
- `bootnode-20241120122109` (2024-11-20 18:21:17)
- `bootnode-20241120190921` (2024-11-20 19:22:01)
- `bootnode-20241120225108` (2024-11-20 22:51:28)
- `bootnode-20241120164448` (2024-11-20 23:21:24)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v20.15.0` (2024-11-21 00:21:14)
- `bootnode-20241121010042` (2024-11-21 00:21:53)
- `bootnode-20241121012111` (2024-11-21 01:21:33)
- `bootnode-20241121042044` (2024-11-21 03:21:02)
- `bootnode-20241121023354` (2024-11-21 03:21:22)
- `bootnode-20241120215035` (2024-11-21 03:50:48)
- `bootnode-20241121054951` (2024-11-21 04:50:48)
- `bootnode-20241121055237` (2024-11-21 05:21:06)
- `bootnode-20241121065308` (2024-11-21 06:21:08)
- `bootnode-20241121000748` (2024-11-21 06:51:12)
- `bootnode-20241121063811` (2024-11-21 07:20:59)
- `bootnode-20241121084721` (2024-11-21 07:50:57)
- `bootnode-20241121082022` (2024-11-21 08:21:03)
- `bootnode-20241121103907` (2024-11-21 09:51:01)
- `bootnode-20241121131114` (2024-11-21 12:21:25)
- `bootnode-20241121125032` (2024-11-21 12:51:17)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v18.19.1` (2024-11-21 14:21:13)
- `bootnode-20241121144920` (2024-11-21 14:51:59)
- `bootnode-20241121150158` (2024-11-21 15:21:04)
- `kubo/0.33.0-dev/d50600391-dirty` (2024-11-21 16:51:44)
- `bootnode-20241121175822` (2024-11-21 18:20:58)
- `bootnode-20241121190904` (2024-11-21 18:21:55)
- `bootnode-20241121184047` (2024-11-21 18:52:00)
- `bootnode-20241121185117` (2024-11-21 18:52:11)
- `bootnode-20241121202012` (2024-11-21 19:21:13)
- `ca-vsc@48d6eef49` (2024-11-21 19:22:07)
- `kubo/0.32.1/mars.i.ipfs.io` (2024-11-21 23:21:20)
- `bootnode-20241121235948` (2024-11-22 00:20:59)
- `bootnode-20241121175824` (2024-11-22 00:21:05)
- `bootnode-20241122011828` (2024-11-22 01:21:30)
- `bootnode-20241122022117` (2024-11-22 01:51:14)
- `bootnode-20241121193125` (2024-11-22 01:51:41)
- `bootnode-20241122032043` (2024-11-22 03:20:59)
- `bootnode-20241122023558` (2024-11-22 03:21:19)
- `bootnode-20241122020910` (2024-11-22 03:51:48)
- `bootnode-20241122030410` (2024-11-22 04:21:23)
- `bootnode-20241122050904` (2024-11-22 04:21:41)
- `bootnode-20241121212152` (2024-11-22 04:22:20)
- `bootnode-20241122045034` (2024-11-22 04:50:54)
- `bootnode-20241122052011` (2024-11-22 05:21:26)
- `bootnode-20241122062050` (2024-11-22 05:21:56)
- `p2proxy@4a2ef6ea0-dirty` (2024-11-22 07:21:03)
- `p2proxy@673de366b-dirty` (2024-11-22 07:51:14)
- `bootnode-20241122020147` (2024-11-22 08:21:13)
- `bootnode-20241122022151` (2024-11-22 08:51:03)
- `bootnode-20241122121740` (2024-11-22 11:21:17)
- `bootnode-20241122115053` (2024-11-22 11:51:18)
- `kubo/0.32.0-dev/docker` (2024-11-22 13:21:01)
- `libp2p/1.3.3 UserAgent=v20.18.1` (2024-11-22 13:51:09)
- `bootnode-20241122142854` (2024-11-22 14:50:55)
- `bootnode-20241122102012` (2024-11-22 16:21:14)
- `bootnode-20241122181352` (2024-11-22 17:51:23)
- `bootnode-20241122114139` (2024-11-22 18:21:21)
- `bootnode-20241122195009` (2024-11-22 19:51:23)
- `bootnode-20241122211435` (2024-11-22 20:23:25)
- `bootnode-20241122212106` (2024-11-22 21:21:29)
- `bootnode-20241122205854` (2024-11-22 21:51:02)
- `bootnode-20241122231803` (2024-11-22 22:21:14)
- `bootnode-20241122225139` (2024-11-22 22:52:11)
- `bootnode-20241122234045` (2024-11-23 00:51:33)
- `github.com/functionland/go-fula@0abc84fdc` (2024-11-23 01:21:17)
- `bootnode-20241123015105` (2024-11-23 01:51:15)
- `bootnode-20241123033057` (2024-11-23 02:51:01)
- `bootnode-20241123022543` (2024-11-23 03:51:56)
- `bootnode-20241122203705` (2024-11-23 04:21:15)
- `bootnode-20241123045043` (2024-11-23 04:50:53)
- `bootnode-20241123045110` (2024-11-23 04:51:20)
- `bootnode-20241122231321` (2024-11-23 05:21:23)
- `bootnode-20241123052100` (2024-11-23 05:21:32)
- `bootnode-20241123061400` (2024-11-23 06:21:51)
- `bootnode-20241123063540` (2024-11-23 06:51:11)
- `bootnode-20241123070653` (2024-11-23 07:21:28)
- `bootnode-20241123102021` (2024-11-23 09:21:12)
- `bootnode-20241123034802` (2024-11-23 10:21:12)
- `bootnode-20241123113816` (2024-11-23 10:51:29)
- `bootnode-20241123111547` (2024-11-23 11:21:26)
- `bootnode-20241123053901` (2024-11-23 11:51:30)
- `bootnode-20241123132124` (2024-11-23 12:21:46)
- `bootnode-20241123121505` (2024-11-23 13:21:04)
- `bootnode-20241123134359` (2024-11-23 13:21:40)
- `bootnode-20241123135113` (2024-11-23 13:51:23)
- `bootnode-20241123140905` (2024-11-23 14:21:19)
- `bootnode-20241123151137` (2024-11-23 15:21:23)
- `bootnode-20241123165615` (2024-11-23 16:21:14)
- `kubo/0.32.1/d11b528/docker` (2024-11-23 16:51:38)
- `bootnode-20241123185019` (2024-11-23 17:50:59)
- `bootnode-20241123175557` (2024-11-23 18:21:00)
- `bootnode-20241123213133` (2024-11-23 21:51:13)
- `bootnode-20241123215034` (2024-11-23 22:21:06)
- `bootnode-20241123223127` (2024-11-23 23:50:58)
- `bootnode-20241123232844` (2024-11-23 23:51:43)
- `bootnode-20241124012005` (2024-11-24 00:21:30)
- `bootnode-20241123183715` (2024-11-24 00:52:00)
- `bootnode-20241124012047` (2024-11-24 01:21:28)
- `bootnode-20241124025855` (2024-11-24 02:21:54)
- `bootnode-20241124022356` (2024-11-24 03:21:08)
- `bootnode-20241124032122` (2024-11-24 03:21:41)
- `bootnode-20241124042100` (2024-11-24 04:21:11)
- `bootnode-20241123220856` (2024-11-24 04:51:31)
- `bootnode-20241124062012` (2024-11-24 05:21:48)
- `bootnode-20241124041849` (2024-11-24 05:51:07)
- `bootnode-20241124055151` (2024-11-24 05:52:09)
- `bootnode-20241124062140` (2024-11-24 06:22:01)
- `bootnode-20241124065029` (2024-11-24 06:51:07)
- `bootnode-20241124064624` (2024-11-24 07:21:20)
- `someguy/v0.6.0 2024-11-19-bdf542e` (2024-11-24 07:51:03)
- `bootnode-20241124070943` (2024-11-24 07:51:26)
- `bootnode-20241124020638` (2024-11-24 08:21:03)
- `bootnode-20241124085408` (2024-11-24 10:21:13)
- `bootnode-20241124105032` (2024-11-24 10:50:46)
- `bootnode-20241124115100` (2024-11-24 11:51:17)
- `bootnode-20241124122149` (2024-11-24 12:22:07)
- `bootnode-20241124121900` (2024-11-24 13:21:11)
- `bootnode-20241124135031` (2024-11-24 13:50:48)
- `bootnode-20241124155043` (2024-11-24 14:51:19)
- `bootnode-20241124161514` (2024-11-24 15:21:07)
- `bootnode-20241124095029` (2024-11-24 15:50:52)
- `bootnode-20241124144322` (2024-11-24 16:51:02)
- `git.allison.lol/allison/ghostnet-servant@` (2024-11-24 17:21:00)
- `bootnode-20241124171805` (2024-11-24 17:21:47)
- `bootnode-20241124121125` (2024-11-24 18:21:22)
- `bootnode-20241124192044` (2024-11-24 19:20:49)
- `bootnode-20241124123154` (2024-11-24 19:21:02)
- `bootnode-20241124202717` (2024-11-24 19:51:21)
- `bootnode-20241124133200` (2024-11-24 20:21:24)
- `bootnode-20241124215042` (2024-11-24 20:50:51)
- `bootnode-20241124222109` (2024-11-24 21:21:13)
- `bootnode-20241124153206` (2024-11-24 22:21:19)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/orbitdb/heads/orbitdb/zdpuApwbKir1tSM5a4b3GiovQjixFnSgDTKraaL5T3wRtRjGG` (2024-11-19 07:20:56)
- `/re-holepunch/0.0.1` (2024-11-20 09:20:51)
- `/party01` (2024-11-22 00:51:02)
- `/party11` (2024-11-22 00:51:02)
- `defs@stream/request/segment/1.0.0` (2024-11-23 06:21:17)
- `defs@stream/send/segment/1.0.0` (2024-11-23 06:21:17)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `82.180.162.171` | US | 886 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.17.0-dev/1134ffb', 'kubo/0.19.1/958e586/docker', 'kubo/0.22.0/3f884d3/gala.games', 'kubo/0.30.0/846c5cc', 'rust-libp2p/0.44.2', 'rust-libp2p/0.45.0']| False  |
| `152.81.47.227` | FR | 267 | ['kubo/0.32.0/', 'kubo/0.33.0-dev/']| False  |
| `143.110.168.61` | GB | 114 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.26.0/096f510/docker', 'kubo/0.29.0/3f0947b']| True  |
| `139.59.6.4` | IN | 105 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b', 'kubo/0.30.0/']| True  |
| `51.158.233.167` | FR | 94 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.150.159` | FR | 91 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 87 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 87 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 86 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 84 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-11-18` to `2024-11-25` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-11-18` to `2024-11-25` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-11-18` to `2024-11-25` in the DHT and their datacenter association.

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