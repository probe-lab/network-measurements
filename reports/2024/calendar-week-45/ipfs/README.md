# Nebula Measurement Results Calendar Week 45 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 45 - 2024](#nebula-measurement-results-calendar-week-45---2024)
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

The following results show measurement data that were collected in calendar week 45 in 2024 from `2024-11-04` to `2024-11-11`.

- Number of crawls `336`
- Number of visits `29,542,265`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `59,484`
- Number of unique peer IDs discovered in the DHT `57,793`
- Number of unique IP addresses found `46,759`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20241103184947` (2024-11-04 00:51:04)
- `bootnode-20241104014112` (2024-11-04 01:21:05)
- `kubo/0.32.0-rc1/desktop` (2024-11-04 03:21:28)
- `bootnode-20241103192206` (2024-11-04 03:51:01)
- `bootnode-20241103222251` (2024-11-04 04:50:51)
- `bootnode-20241104050851` (2024-11-04 05:50:55)
- `bootnode-20241103232105` (2024-11-04 05:51:11)
- `bootnode-20241104000427` (2024-11-04 06:21:19)
- `ca-vsc@cefab5caa-dirty` (2024-11-04 06:21:23)
- `bootnode-20241104064257` (2024-11-04 07:51:05)
- `bootnode-20241104082625` (2024-11-04 09:22:00)
- `bootnode-20241104013437` (2024-11-04 09:22:47)
- `bootnode-20241104104221` (2024-11-04 10:20:59)
- `ca-vsc@714afdc56` (2024-11-04 10:51:41)
- `bootnode-20241104040650` (2024-11-04 10:52:48)
- `kubo/0.33.0-dev/1ca0ae0af` (2024-11-04 13:21:05)
- `github.com/flamingotv/lib@746bc3acb-dirty` (2024-11-04 13:21:09)
- `ca-vsc@83d071d95` (2024-11-04 13:21:30)
- `bootnode-20241104074038` (2024-11-04 13:51:31)
- `github.com/flamingotv/lib@90eb99719-dirty` (2024-11-04 15:21:36)
- `bootnode-20241104100302` (2024-11-04 16:21:04)
- `bootnode-20241104152340` (2024-11-04 17:21:00)
- `bootnode-20241104175308` (2024-11-04 17:21:24)
- `github.com/flamingotv/lib@9dd66842c-dirty` (2024-11-04 17:21:31)
- `bootnode-20241104112409` (2024-11-04 18:20:57)
- `kubo/0.33.0-dev/d4ae7fa81-dirty` (2024-11-04 19:50:56)
- `kubo/0.33.0-dev/d4ae7fa/docker` (2024-11-04 19:51:33)
- `bootnode-20241104225506` (2024-11-04 23:20:52)
- `bootnode-20241104221751` (2024-11-04 23:20:57)
- `bootnode-20241104165722` (2024-11-04 23:21:03)
- `bootnode-20241105010528` (2024-11-05 01:50:55)
- `bootnode-20241105020441` (2024-11-05 01:51:08)
- `bootnode-20241105030812` (2024-11-05 02:21:02)
- `bootnode-20241104202636` (2024-11-05 02:51:42)
- `bootnode-20241104205803` (2024-11-05 03:21:28)
- `bootnode-20241104215445` (2024-11-05 03:51:06)
- `bootnode-20241104235003` (2024-11-05 05:51:01)
- `bootnode-20241105063028` (2024-11-05 06:51:02)
- `bootnode-20241105004218` (2024-11-05 07:51:15)
- `ca-vsc@efaab0004` (2024-11-05 07:51:33)
- `bootnode-20241105073939` (2024-11-05 09:21:03)
- `bootnode-20241105021643` (2024-11-05 09:50:53)
- `bootnode-20241105033234` (2024-11-05 09:51:41)
- `bootnode-20241105081509` (2024-11-05 10:20:50)
- `bootnode-20241105105031` (2024-11-05 10:51:08)
- `bootnode-20241105115051` (2024-11-05 11:51:13)
- `bootnode-20241105130451` (2024-11-05 12:20:57)
- `bootnode-20241105115134` (2024-11-05 13:21:03)
- `bootnode-20241105064711` (2024-11-05 13:21:07)
- `bootnode-20241105132118` (2024-11-05 13:21:31)
- `bootnode-20241105124350` (2024-11-05 13:21:57)
- `hyprspace` (2024-11-05 14:22:47)
- `bootnode-20241105133621` (2024-11-05 14:50:54)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v20.15.1` (2024-11-05 14:52:08)
- `kubo/0.33.0-dev/e17dc21/docker` (2024-11-05 15:50:51)
- `bootnode-20241105143158` (2024-11-05 15:51:01)
- `kubo/0.33.0-dev/4009ad3/docker` (2024-11-05 16:21:54)
- `bootnode-20241105152638` (2024-11-05 16:51:13)
- `bootnode-20241105155154` (2024-11-05 16:51:44)
- `bootnode-20241105113759` (2024-11-05 18:22:05)
- `bootnode-20241105135424` (2024-11-05 18:50:55)
- `bootnode-20241105191603` (2024-11-05 19:50:47)
- `bootnode-20241105203617` (2024-11-05 19:50:50)
- `bootnode-20241105200550` (2024-11-05 20:21:05)
- `bootnode-20241105200648` (2024-11-05 20:51:08)
- `bootnode-20241105221619` (2024-11-05 22:22:11)
- `bootnode-20241105211716` (2024-11-05 22:22:15)
- `bootnode-20241106004624` (2024-11-06 01:50:50)
- `kubo/0.33.0-dev/4009ad3e5` (2024-11-06 01:54:37)
- `bootnode-20241106044704` (2024-11-06 04:20:53)
- `bootnode-20241105231722` (2024-11-06 05:21:19)
- `bootnode-20241106062012` (2024-11-06 06:21:04)
- `bootnode-20241106012045` (2024-11-06 07:21:38)
- `bootnode-20241106083725` (2024-11-06 07:51:34)
- `bootnode-20241106082731` (2024-11-06 08:50:59)
- `bootnode-20241106091052` (2024-11-06 10:21:16)
- `bootnode-20241106041854` (2024-11-06 10:21:49)
- `bootnode-20241106112735` (2024-11-06 11:50:59)
- `libp2p/alpha1` (2024-11-06 12:21:37)
- `bootnode-20241106072047` (2024-11-06 13:21:44)
- `bootnode-20241106152927` (2024-11-06 16:20:59)
- `bootnode-20241106105140` (2024-11-06 17:22:10)
- `kubo/0.30.0/debox/0.3.0` (2024-11-06 18:20:52)
- `bootnode-20241106202047` (2024-11-06 20:21:01)
- `bootnode-20241106135432` (2024-11-06 20:51:18)
- `bootnode-20241106205232` (2024-11-06 21:51:10)
- `p2proxy@74dfae987` (2024-11-06 22:21:24)
- `github.com/functionland/go-fula@ef7c3c5b8` (2024-11-06 23:51:04)
- `kubo/0.33.0-dev/617eb29fd-dirty` (2024-11-06 23:51:21)
- `bootnode-20241106212908` (2024-11-07 00:22:16)
- `bootnode-20241106175257` (2024-11-07 00:22:19)
- `bootnode-20241107005058` (2024-11-07 00:51:48)
- `bootnode-20241106232328` (2024-11-07 01:51:07)
- `bootnode-20241106201900` (2024-11-07 02:21:33)
- `kubo/0.33.0-dev/e14a8a3/1234567890123456789012345678901234567890` (2024-11-07 02:50:56)
- `bootnode-20241107033925` (2024-11-07 02:51:08)
- `bootnode-20241107052005` (2024-11-07 05:21:03)
- `bootnode-20241107021854` (2024-11-07 06:20:57)
- `bootnode-20241107022045` (2024-11-07 08:22:26)
- `bootnode-20241107102007` (2024-11-07 09:20:50)
- `bootnode-20241107100951` (2024-11-07 09:20:53)
- `bootnode-20241107095029` (2024-11-07 09:50:51)
- `bootnode-20241107033058` (2024-11-07 09:50:55)
- `kubo/0.31.0/docker` (2024-11-07 10:50:49)
- `kubo/0.31.0-dev/docker` (2024-11-07 11:21:11)
- `ca-vsc@a4372ab77` (2024-11-07 11:51:43)
- `bootnode-20241107043650` (2024-11-07 13:21:11)
- `bootnode-20241107172018` (2024-11-07 16:20:55)
- `bootnode-20241107111440` (2024-11-07 17:51:35)
- `bootnode-20241107184159` (2024-11-07 19:22:06)
- `bootnode-20241107183342` (2024-11-07 20:21:10)
- `bootnode-20241107121457` (2024-11-07 20:50:56)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v22.10.0` (2024-11-07 20:52:06)
- `bootnode-20241107203730` (2024-11-07 21:21:00)
- `kubo/0.32.0-rc1/b87d512/1234567890123456789012345678901234567890` (2024-11-07 21:50:50)
- `kubo/0.33.0-dev/1512ec5/docker` (2024-11-07 21:51:40)
- `bootnode-20241108000044` (2024-11-07 23:51:20)
- `kubo/0.32.0-rc2/4f06b6a/1234567890123456789012345678901234567890` (2024-11-08 00:20:48)
- `bootnode-20241108001928` (2024-11-08 00:21:21)
- `bootnode-20241108001920` (2024-11-08 00:21:36)
- `bootnode-20241108003334` (2024-11-08 00:21:43)
- `bootnode-20241107180846` (2024-11-08 00:51:14)
- `bootnode-20241108012111` (2024-11-08 01:21:18)
- `bootnode-20241107184611` (2024-11-08 01:21:44)
- `bootnode-20241108005511` (2024-11-08 01:51:09)
- `kubo/0.32.0-rc2/` (2024-11-08 02:21:49)
- `bootnode-20241108034147` (2024-11-08 03:21:05)
- `github.com/JackalLabs/sequoia@56bfca9ea` (2024-11-08 03:51:40)
- `bootnode-20241107222004` (2024-11-08 04:21:18)
- `bootnode-20241108043431` (2024-11-08 04:51:03)
- `bootnode-20241107225036` (2024-11-08 04:51:07)
- `bootnode-20241107234020` (2024-11-08 05:51:22)
- `bootnode-20241108015432` (2024-11-08 06:21:05)
- `bootnode-20241108002026` (2024-11-08 06:51:09)
- `bootnode-20241108011055` (2024-11-08 07:21:02)
- `bootnode-20241108055213` (2024-11-08 07:21:04)
- `bootnode-20241108085238` (2024-11-08 08:52:16)
- `kubo/0.32.0-rc2/4f06b6a/docker` (2024-11-08 09:51:02)
- `bootnode-20241108094623` (2024-11-08 10:51:38)
- `bootnode-20241108103846` (2024-11-08 11:20:59)
- `bootnode-20241108113545` (2024-11-08 11:51:13)
- `bootnode-20241108120021` (2024-11-08 12:21:11)
- `bootnode-20241108114804` (2024-11-08 12:21:20)
- `someguy/v0.5.3 2024-10-30-4903832` (2024-11-08 12:21:30)
- `bootnode-20241108125045` (2024-11-08 12:51:05)
- `bootnode-20241102231208` (2024-11-08 13:52:09)
- `bootnode-20241108151341` (2024-11-08 14:20:57)
- `bootnode-20241108081530` (2024-11-08 14:51:06)
- `bootnode-20241108143236` (2024-11-08 14:51:13)
- `bootnode-20241108075425` (2024-11-08 14:51:16)
- `bootnode-20241108085639` (2024-11-08 15:51:18)
- `p2proxy@8225be87d` (2024-11-08 16:21:00)
- `bootnode-20241108164722` (2024-11-08 16:51:02)
- `bootnode-20241108100843` (2024-11-08 16:51:08)
- `bootnode-20241108165040` (2024-11-08 16:51:09)
- `kubo/0.33.0-dev/71048b7/docker` (2024-11-08 17:21:05)
- `bootnode-20241108182631` (2024-11-08 18:51:45)
- `bootnode-20241108112915` (2024-11-08 19:21:08)
- `bootnode-20241108182552` (2024-11-08 19:51:28)
- `bootnode-20241108142642` (2024-11-08 20:51:15)
- `bootnode-20241108214804` (2024-11-08 21:21:04)
- `bootnode-20241108195727` (2024-11-08 21:21:06)
- `bootnode-20241108201232` (2024-11-08 21:21:56)
- `bootnode-20241108223643` (2024-11-08 22:51:19)
- `bootnode-20241109001827` (2024-11-08 23:21:17)
- `bootnode-20241108182111` (2024-11-09 00:21:37)
- `bootnode-20241109005831` (2024-11-09 00:50:59)
- `bootnode-20241109003143` (2024-11-09 01:21:01)
- `Helia libp2p/2.1.10 UserAgent=v23.1.0` (2024-11-09 01:21:48)
- `bootnode-20241108200234` (2024-11-09 02:21:03)
- `bootnode-20241109020903` (2024-11-09 02:21:07)
- `bootnode-20241109055029` (2024-11-09 05:21:27)
- `bootnode-20241109021332` (2024-11-09 05:21:31)
- `bootnode-20241109033942` (2024-11-09 05:22:35)
- `bootnode-20241108231400` (2024-11-09 05:50:53)
- `bootnode-20241109065043` (2024-11-09 05:50:57)
- `bootnode-20241109004026` (2024-11-09 06:51:14)
- `bootnode-20241109003704` (2024-11-09 06:51:14)
- `bootnode-20241109064411` (2024-11-09 06:51:51)
- `bootnode-20241109080959` (2024-11-09 07:51:00)
- `bootnode-20241109015034` (2024-11-09 07:51:46)
- `bootnode-20241109091104` (2024-11-09 08:21:13)
- `bootnode-20241109081157` (2024-11-09 08:51:06)
- `bootnode-20241109083507` (2024-11-09 09:21:07)
- `bootnode-20241109034821` (2024-11-09 09:51:05)
- `bootnode-20241109105230` (2024-11-09 10:20:56)
- `bootnode-20241109092323` (2024-11-09 10:20:57)
- `bootnode-20241109094427` (2024-11-09 10:21:01)
- `bootnode-20241109045122` (2024-11-09 11:20:58)
- `bootnode-20241109105003` (2024-11-09 11:21:56)
- `bootnode-20241109051416` (2024-11-09 11:51:01)
- `bootnode-20241109054304` (2024-11-09 11:51:08)
- `bootnode-20241109112607` (2024-11-09 12:21:10)
- `bootnode-20241109124019` (2024-11-09 12:52:18)
- `bootnode-20241109132430` (2024-11-09 13:21:01)
- `bootnode-20241109133047` (2024-11-09 13:51:47)
- `bootnode-20241109141645` (2024-11-09 14:51:06)
- `libp2p/2.2.1 UserAgent=v22.8.0` (2024-11-09 14:51:54)
- `bootnode-20241109151106` (2024-11-09 15:21:33)
- `bootnode-20241109155129` (2024-11-09 15:51:55)
- `bootnode-20241109163702` (2024-11-09 16:51:15)
- `bootnode-20241109095942` (2024-11-09 17:21:17)
- `bootnode-20241109110750` (2024-11-09 17:22:47)
- `bootnode-20241109175530` (2024-11-09 17:51:09)
- `bootnode-20241109163132` (2024-11-09 17:51:10)
- `bootnode-20241109121826` (2024-11-09 18:21:01)
- `bootnode-20241109124003` (2024-11-09 18:51:08)
- `bootnode-20241109184001` (2024-11-09 18:52:27)
- `bootnode-20241109191157` (2024-11-09 19:20:57)
- `bootnode-20241109200524` (2024-11-09 19:21:04)
- `bootnode-20241109142047` (2024-11-09 20:21:21)
- `bootnode-20241109141157` (2024-11-09 20:21:30)
- `bootnode-20241109203629` (2024-11-09 20:51:02)
- `bootnode-20241109154158` (2024-11-09 21:51:06)
- `bootnode-20241109160427` (2024-11-09 22:20:56)
- `bootnode-20241109222604` (2024-11-09 22:21:07)
- `bootnode-20241109221801` (2024-11-09 22:51:08)
- `bootnode-20241109230655` (2024-11-09 23:21:02)
- `bootnode-20241109232528` (2024-11-09 23:51:00)
- `libp2p/1.4.2 UserAgent=v20.7.0` (2024-11-09 23:52:02)
- `bootnode-20241110011739` (2024-11-10 00:21:34)
- `bootnode-20241110003652` (2024-11-10 00:51:25)
- `bootnode-20241109183838` (2024-11-10 00:51:27)
- `bootnode-20241109185750` (2024-11-10 01:21:27)
- `bootnode-20241110032730` (2024-11-10 02:51:02)
- `bootnode-20241109203813` (2024-11-10 03:20:57)
- `bootnode-20241110042903` (2024-11-10 03:51:50)
- `bootnode-20241110053933` (2024-11-10 05:20:52)
- `bootnode-20241110064956` (2024-11-10 05:50:55)
- `bootnode-20241110060530` (2024-11-10 06:20:54)
- `bootnode-20241110072020` (2024-11-10 06:20:59)
- `bootnode-20241110002055` (2024-11-10 06:21:01)
- `bootnode-20241110065925` (2024-11-10 07:22:16)
- `bootnode-20241110010830` (2024-11-10 07:22:45)
- `bootnode-20241110071946` (2024-11-10 08:21:09)
- `bootnode-20241110083140` (2024-11-10 08:21:12)
- `bootnode-20241110083438` (2024-11-10 08:50:59)
- `bootnode-20241110084016` (2024-11-10 08:51:58)
- `bootnode-20241110092052` (2024-11-10 09:21:09)
- `bootnode-20241110095201` (2024-11-10 09:51:08)
- `bootnode-20241110043251` (2024-11-10 10:52:09)
- `bootnode-20241110104453` (2024-11-10 11:20:57)
- `bootnode-20241110131108` (2024-11-10 12:21:01)
- `kubo/0.33.0-dev/71048b768` (2024-11-10 12:21:39)
- `helia/5.1.0 libp2p/2.2.1 UserAgent=v22.11.0` (2024-11-10 12:50:55)
- `bootnode-20241110122418` (2024-11-10 13:21:00)
- `bootnode-20241110082038` (2024-11-10 14:21:11)
- `bootnode-20241110135433` (2024-11-10 14:22:06)
- `bootnode-20241110150002` (2024-11-10 15:21:49)
- `bootnode-20241110153058` (2024-11-10 15:51:12)
- `bootnode-20241110162506` (2024-11-10 15:52:20)
- `bootnode-20241110160124` (2024-11-10 16:51:14)
- `bootnode-20241110101444` (2024-11-10 16:51:42)
- `bootnode-20241110171814` (2024-11-10 17:21:49)
- `bootnode-20241110171627` (2024-11-10 17:50:54)
- `bootnode-20241110171147` (2024-11-10 17:51:50)
- `bootnode-20241110175849` (2024-11-10 18:21:34)
- `bootnode-20241110180204` (2024-11-10 18:50:59)
- `bootnode-20241110182924` (2024-11-10 18:52:29)
- `bootnode-20241110203705` (2024-11-10 19:51:10)
- `bootnode-20241110200119` (2024-11-10 20:51:05)
- `bootnode-20241110184831` (2024-11-10 21:21:42)
- `bootnode-20241110220643` (2024-11-10 21:22:00)
- `bootnode-20241110154359` (2024-11-10 22:21:02)
- `bootnode-20241110164852` (2024-11-10 22:50:51)
- `bootnode-20241110214530` (2024-11-10 23:51:15)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/hypermedia/0.8.0` (2024-11-04 12:51:21)
- `/file-transfer/1.0.0` (2024-11-04 14:50:54)
- `/flamingotv/content/1.0.0` (2024-11-04 15:21:36)
- `/hyprspace/service/0.0.1` (2024-11-05 14:22:47)
- `/lpweb/http/1.0.0` (2024-11-06 12:21:37)
- `/lpweb/ws/1.0.0` (2024-11-06 12:21:37)
- `/hypermedia/0.8.0-dev` (2024-11-07 02:21:37)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `157.173.99.87` | GB | 1549 | ['kubo/0.18.1/675f8bd/docker', 'kubo/0.29.0/3f0947b']| False  |
| `82.180.162.171` | US | 1175 | ['helia/4.2.6 libp2p/1.4.3 UserAgent=v20.11.0', 'kubo/0.29.0/', 'kubo/0.30.0/846c5cc', 'kubo/0.30.0/846c5cc/docker']| False  |
| `5.135.162.92` | FR | 319 | ['kubo/0.16.0/', 'rust-libp2p/0.45.0']| True  |
| `2001:41d0:8:e55c::1` | FR | 319 | ['kubo/0.16.0/', 'rust-libp2p/0.45.0']| True  |
| `172.98.12.34` | US | 255 | ['go-ipfs/0.11.0/d6518322f4', 'rust-libp2p/0.45.0']| False  |
| `178.128.39.79` | GB | 135 | ['kubo/0.29.0/3f0947b']| True  |
| `51.158.233.167` | FR | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `152.81.47.227` | FR | 81 | ['kubo/0.28.0/', 'kubo/0.31.0/']| False  |
| `51.159.150.159` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
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

In the specified time interval from `2024-11-04` to `2024-11-11` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-11-04` to `2024-11-11` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-11-04` to `2024-11-11` in the DHT and their datacenter association.

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