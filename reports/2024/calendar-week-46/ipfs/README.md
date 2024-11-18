# Nebula Measurement Results Calendar Week 46 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 46 - 2024](#nebula-measurement-results-calendar-week-46---2024)
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

The following results show measurement data that were collected in calendar week 46 in 2024 from `2024-11-11` to `2024-11-18`.

- Number of crawls `336`
- Number of visits `23,853,824`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `50,629`
- Number of unique peer IDs discovered in the DHT `48,500`
- Number of unique IP addresses found `42,558`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20241110182044` (2024-11-11 00:20:58)
- `bootnode-20241111004756` (2024-11-11 00:21:01)
- `bootnode-20241110232146` (2024-11-11 00:21:33)
- `bootnode-20241111011454` (2024-11-11 01:51:04)
- `kubo/0.32.0-rc2/desktop` (2024-11-11 02:52:13)
- `bootnode-20241111042957` (2024-11-11 03:50:55)
- `bootnode-20241110230335` (2024-11-11 05:51:36)
- `bootnode-20241111055111` (2024-11-11 05:51:43)
- `bootnode-20241111064844` (2024-11-11 06:21:06)
- `kubo/0.31.0/38c8619` (2024-11-11 06:21:26)
- `bootnode-20241111074042` (2024-11-11 07:21:09)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v18.20.3` (2024-11-11 07:21:31)
- `bootnode-20241111072341` (2024-11-11 07:52:12)
- `bootnode-20241111091150` (2024-11-11 08:21:08)
- `bootnode-20241111081536` (2024-11-11 08:51:07)
- `bootnode-20241111082745` (2024-11-11 08:51:25)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v20.9.0` (2024-11-11 08:51:47)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v20.5.1` (2024-11-11 09:22:05)
- `bootnode-20241111093934` (2024-11-11 09:50:53)
- `bootnode-20241111094407` (2024-11-11 10:20:49)
- `bootnode-20241111035747` (2024-11-11 10:22:15)
- `bootnode-20241111115519` (2024-11-11 11:50:53)
- `bootnode-20241111053046` (2024-11-11 11:51:00)
- `bootnode-20241111053825` (2024-11-11 11:51:00)
- `bootnode-20241111113557` (2024-11-11 11:51:25)
- `bootnode-20241111121217` (2024-11-11 11:52:07)
- `bootnode-20241111114739` (2024-11-11 12:20:58)
- `bootnode-20241111112530` (2024-11-11 12:21:27)
- `bootnode-20241111143855` (2024-11-11 13:51:00)
- `bootnode-20241111074420` (2024-11-11 14:21:13)
- `kubo/0.32.0-rc2/4f06b6a00` (2024-11-11 14:52:04)
- `bootnode-20241111091532` (2024-11-11 15:21:05)
- `bootnode-20241111164947` (2024-11-11 15:51:01)
- `bootnode-20241111172002` (2024-11-11 17:20:51)
- `bootnode-20241111184631` (2024-11-11 18:21:51)
- `bootnode-20241111180325` (2024-11-11 19:51:50)
- `bootnode-20241111194924` (2024-11-11 21:50:53)
- `bootnode-20241111215434` (2024-11-11 21:51:24)
- `bootnode-20241111201123` (2024-11-12 02:20:56)
- `bootnode-20241112021900` (2024-11-12 02:21:15)
- `bootnode-20241112025020` (2024-11-12 02:51:00)
- `bootnode-20241112031126` (2024-11-12 02:51:04)
- `bootnode-20241112024557` (2024-11-12 02:51:37)
- `bootnode-20241112032111` (2024-11-12 03:21:23)
- `bootnode-20241112035048` (2024-11-12 03:51:16)
- `bootnode-20241111213501` (2024-11-12 03:51:44)
- `bootnode-20241112043227` (2024-11-12 04:51:11)
- `bootnode-20241112063226` (2024-11-12 06:51:20)
- `bootnode-20241112075722` (2024-11-12 07:20:50)
- `bootnode-20241112082737` (2024-11-12 07:52:08)
- `bootnode-20241112074102` (2024-11-12 07:52:18)
- `bootnode-20241112074617` (2024-11-12 08:21:22)
- `bootnode-20241112022353` (2024-11-12 08:51:05)
- `bootnode-20241112094813` (2024-11-12 09:51:25)
- `bootnode-20241112110600` (2024-11-12 10:21:11)
- `bootnode-20241112074449` (2024-11-12 10:51:10)
- `bootnode-20241112094207` (2024-11-12 10:51:50)
- `bootnode-20241112120644` (2024-11-12 11:21:00)
- `bootnode-20241112131027` (2024-11-12 12:21:28)
- `bootnode-20241112122902` (2024-11-12 13:21:03)
- `bootnode-20241112134109` (2024-11-12 13:21:44)
- `ca-vsc@8651562e6` (2024-11-12 14:51:03)
- `ca-vsc@8651562e6-dirty` (2024-11-12 15:22:13)
- `bootnode-20241112162920` (2024-11-12 15:51:03)
- `bootnode-20241112170238` (2024-11-12 16:22:40)
- `bootnode-20241112165039` (2024-11-12 16:51:05)
- `bootnode-20241112154818` (2024-11-12 17:21:16)
- `bootnode-20241112162753` (2024-11-12 17:21:38)
- `bootnode-20241112181555` (2024-11-12 17:50:54)
- `bootnode-20241112181211` (2024-11-12 18:21:14)
- `bootnode-20241112120948` (2024-11-12 18:51:57)
- `bootnode-20241112195654` (2024-11-12 19:21:20)
- `bootnode-20241112133133` (2024-11-12 20:51:12)
- `bootnode-20241112201051` (2024-11-12 20:51:52)
- `bootnode-20241112131215` (2024-11-12 20:52:05)
- `bootnode-20241112212001` (2024-11-12 21:21:58)
- `bootnode-20241112211929` (2024-11-12 21:22:05)
- `bootnode-20241112223257` (2024-11-12 21:51:17)
- `bootnode-20241112220718` (2024-11-12 21:51:22)
- `bootnode-20241112224132` (2024-11-12 23:50:58)
- `bootnode-20241113014612` (2024-11-13 01:50:56)
- `bootnode-20241113013538` (2024-11-13 02:21:12)
- `bootnode-20241113022624` (2024-11-13 02:50:50)
- `bootnode-20241113025712` (2024-11-13 03:20:49)
- `bootnode-20241112204944` (2024-11-13 03:51:59)
- `pouw/0.9.1` (2024-11-13 04:50:44)
- `bootnode-20241112225045` (2024-11-13 04:50:57)
- `bootnode-20241113033815` (2024-11-13 04:51:39)
- `bootnode-20241113051958` (2024-11-13 05:21:26)
- `bootnode-20241112223611` (2024-11-13 05:22:12)
- `bootnode-20241113045740` (2024-11-13 05:51:07)
- `bootnode-20241113081128` (2024-11-13 07:21:20)
- `bootnode-20241113061136` (2024-11-13 07:21:29)
- `bootnode-20241113080056` (2024-11-13 08:21:58)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v20.18.0` (2024-11-13 08:51:35)
- `kubo/0.32.0-rc2/4f06b6a00-dirty` (2024-11-13 09:21:45)
- `bootnode-20241113083655` (2024-11-13 09:51:00)
- `bootnode-20241113080853` (2024-11-13 09:51:30)
- `bootnode-20241113033858` (2024-11-13 09:51:37)
- `bootnode-20241113100914` (2024-11-13 10:22:23)
- `bootnode-20241113115604` (2024-11-13 11:21:31)
- `bootnode-20241113103015` (2024-11-13 11:22:02)
- `bootnode-20241113112720` (2024-11-13 11:51:21)
- `bootnode-20241113115130` (2024-11-13 11:51:59)
- `bootnode-20241113102059` (2024-11-13 12:22:07)
- `bootnode-20241113123850` (2024-11-13 13:22:24)
- `bootnode-20241113145205` (2024-11-13 14:21:01)
- `bootnode-20241113151956` (2024-11-13 14:21:02)
- `bootnode-20241113135554` (2024-11-13 14:21:20)
- `github.com/ipfs-cluster/ipfs-cluster@a5dab45c1` (2024-11-13 14:22:19)
- `bootnode-20241113142524` (2024-11-13 14:51:30)
- `bootnode-20241113082356` (2024-11-13 14:51:37)
- `bootnode-20241113143618` (2024-11-13 14:52:23)
- `bootnode-20241113134138` (2024-11-13 15:21:37)
- `bootnode-20241113093555` (2024-11-13 15:51:14)
- `bootnode-20241113162651` (2024-11-13 16:51:12)
- `bootnode-20241113105613` (2024-11-13 17:21:42)
- `bootnode-20241113174316` (2024-11-13 18:52:12)
- `bootnode-20241113175828` (2024-11-13 18:52:44)
- `bootnode-20241113200403` (2024-11-13 19:21:24)
- `bootnode-20241113124027` (2024-11-13 19:21:57)
- `kubo/0.33.0-dev/fd1f6736a` (2024-11-13 19:22:21)
- `bootnode-20241113202126` (2024-11-13 19:51:14)
- `bootnode-20241113203319` (2024-11-13 20:52:25)
- `kubo/0.32.0-rc2/4f06b6a` (2024-11-13 21:20:55)
- `kubo/0.33.0-dev/fd1f673` (2024-11-13 21:21:00)
- `bootnode-20241113200323` (2024-11-13 22:21:25)
- `bootnode-20241113230904` (2024-11-13 22:21:29)
- `bootnode-20241113222250` (2024-11-13 22:51:09)
- `kubo/0.33.0-dev/e80e821/docker` (2024-11-13 23:21:41)
- `kubo/0.32.0-rc2/136ed3c/1234567890123456789012345678901234567890` (2024-11-13 23:51:38)
- `bootnode-20241113182009` (2024-11-14 00:20:49)
- `bootnode-20241114005336` (2024-11-14 00:21:07)
- `kubo/0.32.0/ad1055c` (2024-11-14 00:50:45)
- `kubo/0.32.0/ad1055c/docker` (2024-11-14 00:50:48)
- `kubo/0.32.0/ad1055c/1234567890123456789012345678901234567890` (2024-11-14 00:51:29)
- `bootnode-20241114013458` (2024-11-14 01:51:11)
- `bootnode-20241114015434` (2024-11-14 02:22:20)
- `bootnode-20241113201947` (2024-11-14 02:51:22)
- `bootnode-20241114013056` (2024-11-14 02:51:38)
- `kubo/0.32.0/` (2024-11-14 02:51:44)
- `bootnode-20241113212024` (2024-11-14 03:21:01)
- `bootnode-20241113210405` (2024-11-14 03:21:43)
- `kubo/0.33.0-dev/720663d/docker` (2024-11-14 03:21:44)
- `bootnode-20241114024513` (2024-11-14 03:51:15)
- `bootnode-20241113220149` (2024-11-14 04:21:40)
- `github.com/JackalLabs/sequoia@ff651917c` (2024-11-14 04:23:30)
- `bootnode-20241114035859` (2024-11-14 04:50:57)
- `bootnode-20241114044714` (2024-11-14 04:51:37)
- `bootnode-20241114054012` (2024-11-14 05:51:19)
- `bootnode-20241114054018` (2024-11-14 05:51:59)
- `bootnode-20241113235655` (2024-11-14 06:21:17)
- `bootnode-20241114042607` (2024-11-14 06:51:02)
- `bootnode-20241114064145` (2024-11-14 06:51:25)
- `kubo/0.32.0/ad1055c1a` (2024-11-14 07:21:02)
- `bootnode-20241114010714` (2024-11-14 07:21:18)
- `bootnode-20241114062416` (2024-11-14 07:51:03)
- `bootnode-20241114072933` (2024-11-14 07:51:21)
- `bootnode-20241114094507` (2024-11-14 09:21:30)
- `bootnode-20241114022153` (2024-11-14 10:21:10)
- `bootnode-20241114105017` (2024-11-14 10:51:57)
- `bootnode-20241114044649` (2024-11-14 11:21:02)
- `bootnode-20241114102543` (2024-11-14 11:21:09)
- `bootnode-20241114111107` (2024-11-14 11:51:30)
- `bootnode-20241114123938` (2024-11-14 11:51:51)
- `bootnode-20241114122122` (2024-11-14 12:21:28)
- `bootnode-20241114120432` (2024-11-14 12:21:36)
- `bootnode-20241114073103` (2024-11-14 13:51:14)
- `bootnode-20241114135715` (2024-11-14 14:51:26)
- `ca-vsc@1c1a7eba0` (2024-11-14 15:21:13)
- `bootnode-20241114092151` (2024-11-14 15:51:13)
- `ca-vsc@8b6738418` (2024-11-14 16:21:27)
- `bootnode-20241114172203` (2024-11-14 17:22:18)
- `bootnode-20241114174756` (2024-11-14 18:21:18)
- `bootnode-20241114191044` (2024-11-14 18:21:54)
- `bootnode-20241114182847` (2024-11-14 18:51:20)
- `bootnode-20241114193843` (2024-11-14 19:50:53)
- `bootnode-20241114211057` (2024-11-14 20:22:05)
- `bootnode-20241114205901` (2024-11-14 20:51:14)
- `bootnode-20241114202831` (2024-11-14 20:51:18)
- `bootnode-20241114155020` (2024-11-14 21:51:01)
- `bootnode-20241114225043` (2024-11-14 21:51:10)
- `bootnode-20241114223947` (2024-11-14 21:51:14)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v22.1.0` (2024-11-14 22:50:56)
- `bootnode-20241114162752` (2024-11-14 22:51:01)
- `bootnode-20241114225131` (2024-11-14 22:51:42)
- `bootnode-20241114224120` (2024-11-14 22:52:16)
- `kubo/0.29.0/e46c892/docker` (2024-11-14 22:53:28)
- `bootnode-20241114232121` (2024-11-14 23:21:32)
- `bootnode-20241114165905` (2024-11-14 23:21:56)
- `bootnode-20241114174951` (2024-11-14 23:51:24)
- `bootnode-20241115003210` (2024-11-15 00:22:05)
- `bootnode-20241115011017` (2024-11-15 00:51:05)
- `bootnode-20241115002245` (2024-11-15 00:51:14)
- `bootnode-20241114195105` (2024-11-15 01:52:04)
- `bootnode-20241115032048` (2024-11-15 02:21:19)
- `bootnode-20241115015816` (2024-11-15 02:21:25)
- `kubo/0.33.0-dev/9abadc4` (2024-11-15 02:22:07)
- `github.com/libp2p/go-libp2p/examples@7268c9844-dirty` (2024-11-15 02:22:26)
- `bootnode-20241115043755` (2024-11-15 04:51:12)
- `bootnode-20241114225116` (2024-11-15 04:51:35)
- `bootnode-20241115051229` (2024-11-15 05:21:07)
- `bootnode-20241115000625` (2024-11-15 06:21:17)
- `bootnode-20241115071125` (2024-11-15 06:21:22)
- `bootnode-20241115063004` (2024-11-15 06:52:14)
- `ca-vsc@af8369165` (2024-11-15 06:52:30)
- `bootnode-20241115072122` (2024-11-15 07:51:01)
- `github.com/harmony-one/harmony@a5b59de8d` (2024-11-15 08:52:00)
- `bootnode-20241115091129` (2024-11-15 09:20:56)
- `bootnode-20241115100911` (2024-11-15 09:20:56)
- `bootnode-20241115094013` (2024-11-15 09:50:52)
- `bootnode-20241115104133` (2024-11-15 09:51:00)
- `v1@` (2024-11-15 09:51:15)
- `bootnode-20241115093503` (2024-11-15 09:51:42)
- `bootnode-20241115102106` (2024-11-15 10:21:12)
- `bootnode-20241115112057` (2024-11-15 11:21:03)
- `v1@dd4e397b8-dirty` (2024-11-15 11:21:27)
- `bootnode-20241115112516` (2024-11-15 11:22:36)
- `bootnode-20241115115533` (2024-11-15 12:21:43)
- `bootnode-20241115063018` (2024-11-15 12:50:51)
- `github.com/ipfs/go-ds-crdt/examples/globaldb@b43de73a3-dirty` (2024-11-15 13:22:12)
- `bootnode-20241115073141` (2024-11-15 13:51:48)
- `bootnode-20241115143620` (2024-11-15 14:21:38)
- `sp2p@` (2024-11-15 14:21:46)
- `bootnode-20241115144118` (2024-11-15 14:51:27)
- `bootnode-20241115142355` (2024-11-15 14:51:33)
- `bootnode-20241115151335` (2024-11-15 15:21:04)
- `bootnode-20241115093940` (2024-11-15 15:51:34)
- `bootnode-20241115155146` (2024-11-15 15:51:55)
- `bootnode-20241115161655` (2024-11-15 15:52:13)
- `bootnode-20241115102028` (2024-11-15 16:21:04)
- `bootnode-20241115102013` (2024-11-15 16:21:14)
- `kubo/0.29.0/544528c87` (2024-11-15 16:22:11)
- `bootnode-20241115171913` (2024-11-15 16:51:01)
- `bootnode-20241115164647` (2024-11-15 16:51:10)
- `kubo/0.33.0-dev/83b06f1/docker` (2024-11-15 17:50:57)
- `bootnode-20241115185136` (2024-11-15 17:51:50)
- `bootnode-20241115191108` (2024-11-15 19:50:49)
- `bootnode-20241115194906` (2024-11-15 19:50:55)
- `kubo/0.29.0/544528c/docker` (2024-11-15 19:52:46)
- `kubo/0.32.1/9017453` (2024-11-15 20:20:41)
- `kubo/0.32.1/9017453/docker` (2024-11-15 20:20:46)
- `kubo/0.32.1/9017453/1234567890123456789012345678901234567890` (2024-11-15 20:21:12)
- `bootnode-20241115192943` (2024-11-15 20:51:23)
- `bootnode-20241115214151` (2024-11-15 21:51:12)
- `bootnode-20241115214230` (2024-11-15 21:51:25)
- `kubo/0.33.0-dev/c292203/docker` (2024-11-15 21:52:07)
- `kubo/0.32.1/` (2024-11-15 23:21:41)
- `kubo/0.33.0-dev/f5b8555/docker` (2024-11-15 23:50:48)
- `bootnode-20241116003901` (2024-11-16 00:52:09)
- `bootnode-20241116021623` (2024-11-16 01:21:08)
- `bootnode-20241116013615` (2024-11-16 01:21:15)
- `bootnode-20241116023715` (2024-11-16 01:50:56)
- `bootnode-20241116010607` (2024-11-16 01:51:01)
- `kubo/0.32.1/901745353` (2024-11-16 01:51:13)
- `bootnode-20241115193800` (2024-11-16 01:51:53)
- `bootnode-20241116025027` (2024-11-16 02:50:55)
- `bootnode-20241115203343` (2024-11-16 02:51:11)
- `bootnode-20241116021216` (2024-11-16 03:21:33)
- `bootnode-20241116043337` (2024-11-16 04:21:05)
- `bootnode-20241116052103` (2024-11-16 05:21:20)
- `bootnode-20241115231543` (2024-11-16 05:21:37)
- `bootnode-20241116051557` (2024-11-16 05:51:10)
- `bootnode-20241116002102` (2024-11-16 06:22:00)
- `bootnode-20241116002320` (2024-11-16 06:52:03)
- `bootnode-20241116081718` (2024-11-16 07:51:22)
- `bootnode-20241116082910` (2024-11-16 08:51:11)
- `bootnode-20241116025110` (2024-11-16 08:51:29)
- `bootnode-20241116040507` (2024-11-16 10:20:56)
- `bootnode-20241116105751` (2024-11-16 11:22:14)
- `bootnode-20241116053952` (2024-11-16 11:51:01)
- `p2proxy@5a46d6879-dirty` (2024-11-16 11:51:28)
- `bootnode-20241116062033` (2024-11-16 12:21:50)
- `bootnode-20241116111245` (2024-11-16 12:51:05)
- `bootnode-20241116062241` (2024-11-16 12:51:11)
- `bootnode-20241116071328` (2024-11-16 13:21:03)
- `bootnode-20241116133046` (2024-11-16 13:50:53)
- `bootnode-20241116142853` (2024-11-16 13:51:14)
- `bootnode-20241116141455` (2024-11-16 14:51:02)
- `bootnode-20241116160227` (2024-11-16 16:21:05)
- `bootnode-20241116174635` (2024-11-16 17:21:36)
- `bootnode-20241116184927` (2024-11-16 18:21:25)
- `bootnode-20241116185005` (2024-11-16 18:51:55)
- `bootnode-20241116212005` (2024-11-16 20:21:38)
- `bootnode-20241116145023` (2024-11-16 20:50:57)
- `kubo/0.32.1/desktop` (2024-11-16 20:51:09)
- `bootnode-20241116230053` (2024-11-16 22:20:49)
- `bootnode-20241116231108` (2024-11-16 23:21:10)
- `bootnode-20241117004134` (2024-11-16 23:51:45)
- `kubo/0.33.0-dev/f5b8555/1234567890123456789012345678901234567890` (2024-11-16 23:52:06)
- `bootnode-20241117015848` (2024-11-17 01:21:34)
- `bootnode-20241117003108` (2024-11-17 01:51:48)
- `bootnode-20241117024620` (2024-11-17 02:52:00)
- `bootnode-20241117031843` (2024-11-17 03:21:01)
- `bootnode-20241117031125` (2024-11-17 03:22:03)
- `bootnode-20241117045146` (2024-11-17 03:52:04)
- `bootnode-20241117052817` (2024-11-17 05:21:12)
- `bootnode-20241117055049` (2024-11-17 05:50:52)
- `bootnode-20241116232655` (2024-11-17 05:50:58)
- `bootnode-20241117053935` (2024-11-17 05:51:20)
- `bootnode-20241117085043` (2024-11-17 07:50:53)
- `bootnode-20241117092308` (2024-11-17 09:21:12)
- `bootnode-20241117094232` (2024-11-17 09:21:22)
- `bootnode-20241117110440` (2024-11-17 10:51:23)
- `bootnode-20241117111648` (2024-11-17 11:51:07)
- `bootnode-20241117122138` (2024-11-17 12:21:53)
- `bootnode-20241117140757` (2024-11-17 14:21:03)
- `bootnode-20241117082142` (2024-11-17 14:21:57)
- `bootnode-20241117082544` (2024-11-17 14:51:09)
- `bootnode-20241117091303` (2024-11-17 15:20:52)
- `bootnode-20241117165030` (2024-11-17 15:50:47)
- `bootnode-20241117090622` (2024-11-17 15:51:08)
- `bootnode-20241117165137` (2024-11-17 16:21:03)
- `bootnode-20241117162137` (2024-11-17 16:22:08)
- `bootnode-20241117173554` (2024-11-17 17:51:17)
- `bootnode-20241117122019` (2024-11-17 18:20:53)
- `bootnode-20241117133603` (2024-11-17 20:21:59)
- `bootnode-20241117205758` (2024-11-17 20:50:58)
- `bootnode-20241117145650` (2024-11-17 21:21:27)
- `bootnode-20241117214544` (2024-11-17 22:21:27)
- `bootnode-20241117222434` (2024-11-17 22:21:52)
- `bootnode-20241117171420` (2024-11-17 23:21:05)
- `bootnode-20241117230938` (2024-11-17 23:21:31)
- `bootnode-20241117233817` (2024-11-17 23:51:06)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/tari_direct_peer_info/5` (2024-11-11 13:21:53)
- `/share_chain_sync/5` (2024-11-11 13:21:53)
- `/catch_up_sync/5` (2024-11-11 13:21:53)
- `/tari/peersync/0.0.1` (2024-11-12 11:21:06)
- `/hypermedia/0.9.0` (2024-11-12 14:51:30)
- `/vpn/1.0.0` (2024-11-13 14:21:13)
- `/postTlp` (2024-11-14 00:20:44)
- `/oos-dataplane/1.0.0` (2024-11-14 01:52:18)
- `/sp2p/1.0.0` (2024-11-14 19:50:57)
- `/orbitdb/heads/orbitdb/zdpuB22rJi5scyL9zmWf48W1HsRqVbzGk7dNhL24jqsGLQc58` (2024-11-17 09:50:56)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `82.180.162.171` | US | 360 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.25.0/', 'kubo/0.30.0/846c5cc', 'kubo/0.30.0/desktop']| False  |
| `2001:41d0:8:e55c::1` | FR | 355 | ['helia/5.1.0 libp2p/2.2.1 UserAgent=v20.9.0', 'kubo/0.16.0/', 'kubo/0.22.0/3f884d3/gala.games', 'rust-libp2p/0.45.0']| True  |
| `5.135.162.92` | FR | 355 | ['helia/5.1.0 libp2p/2.2.1 UserAgent=v20.9.0', 'kubo/0.16.0/', 'kubo/0.22.0/3f884d3/gala.games', 'rust-libp2p/0.45.0']| True  |
| `64.227.156.187` | IN | 150 | ['kubo/0.29.0/3f0947b']| True  |
| `139.59.6.4` | IN | 149 | ['kubo/0.29.0/3f0947b']| True  |
| `143.110.168.61` | GB | 140 | ['kubo/0.28.0/e7f0f34/docker', 'kubo/0.29.0/3f0947b']| True  |
| `152.81.47.227` | FR | 139 | ['kubo/0.28.0/', 'kubo/0.31.0/', 'kubo/0.32.0/', 'kubo/0.33.0-dev/']| False  |
| `142.93.215.219` | IN | 135 | ['kubo/0.29.0/3f0947b']| True  |
| `64.227.134.114` | IN | 118 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.26.0/', 'kubo/0.29.0/3f0947b']| True  |
| `64.227.166.181` | IN | 115 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| True  |

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

In the specified time interval from `2024-11-11` to `2024-11-18` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-11-11` to `2024-11-18` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-11-11` to `2024-11-18` in the DHT and their datacenter association.

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