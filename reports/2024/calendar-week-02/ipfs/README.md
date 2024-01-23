# Nebula Measurement Results Calendar Week 2 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 2 - 2024](#nebula-measurement-results-calendar-week-2---2024)
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

The following results show measurement data that were collected in calendar week 2 in 2024 from `2024-01-08` to `2024-01-15`.

- Number of crawls `332`
- Number of visits `48,609,342`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `71,226`
- Number of unique peer IDs discovered in the DHT `69,528`
- Number of unique IP addresses found `89,057`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/metis-seq/tss-server@7ef5e71e0` (2024-01-08 04:52:24)
- `github.com/metis-seq/tss-server@119841fe4` (2024-01-08 10:52:27)
- `github.com/metis-seq/tss-server@9b154f524` (2024-01-08 11:23:00)
- `github.com/metis-seq/tss-server@2a3d32967` (2024-01-08 11:52:30)
- `kubo/0.26.0-dev/d9663a518` (2024-01-08 23:22:26)
- `kubo/0.26.0-dev/2f91074/docker` (2024-01-09 14:22:06)
- `kubo/0.26.0-dev/2f91074b5` (2024-01-09 21:51:31)
- `helia/2.1.0-17e85f9 libp2p/1.1.0 UserAgent=v21.5.0` (2024-01-10 11:52:53)
- `kubo/0.18.1/8c234d9fd-dirty` (2024-01-11 12:51:00)
- `kubo/0.18.1/8ee057a47-dirty` (2024-01-11 12:51:10)
- `kubo/0.23.0/825124fd5-dirty` (2024-01-11 12:51:17)
- `kubo/0.26.0-dev/02ea518/docker` (2024-01-11 12:52:05)
- `kubo/0.21.0/fa1cd82` (2024-01-11 13:20:55)
- `kubo/0.19.0-dev/cf715b6/docker` (2024-01-11 13:51:27)
- `github.com/diadata-org/diaprotocol@` (2024-01-11 13:52:47)
- `kubo/0.26.0-dev/3932fdfe5` (2024-01-11 14:22:17)
- `kubo/0.23.0-dev/a9737e4d6` (2024-01-11 14:22:34)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.6.1` (2024-01-11 14:50:56)
- `kubo/0.23.0-dev/c5868a8/docker` (2024-01-11 14:51:36)
- `kubo/0.26.0-rc1/` (2024-01-11 15:20:46)
- `kubo/0.26.0-dev/b215d73/docker` (2024-01-11 15:20:55)
- `kubo/0.22.0/DangleBat` (2024-01-11 15:50:50)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.9.0` (2024-01-11 15:52:33)
- `kubo/0.26.0-dev/0fdd97911` (2024-01-11 17:21:00)
- `kubo/1.23.0/` (2024-01-11 17:21:12)
- `kubo/0.22.0-dev/873c6e1/docker` (2024-01-11 17:52:03)
- `kubo/0.27.0-dev/8978b54/docker` (2024-01-11 18:51:24)
- `kubo/0.25.0-dev/01cc5eab5` (2024-01-11 21:22:55)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v21.5.0` (2024-01-12 00:21:25)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v18.17.1` (2024-01-12 00:51:31)
- `kubo/0.24.0-rc2/bd06ef7/docker` (2024-01-12 09:51:00)
- `helia/3.0.0 libp2p/1.1.1 UserAgent=v21.4.0` (2024-01-12 10:20:57)
- `kubo/0.27.0-dev/` (2024-01-12 13:52:57)
- `eTermio/0.0.1 libp2p/1.1.1 UserAgent=v21.5.0` (2024-01-12 15:21:59)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v20.10.0` (2024-01-12 15:51:27)
- `helia/3.0.1 libp2p/1.1.1 UserAgent=v21.4.0` (2024-01-12 17:52:40)
- `kubo/0.27.0-dev/982d8a9/docker` (2024-01-12 18:51:02)
- `kubo/0.25.0-dev/b47928bb6` (2024-01-12 21:21:09)
- `kubo/0.27.0-dev/982d8a92c-dirty` (2024-01-13 08:52:04)
- `kubo/0.25.0-dev/d88264216` (2024-01-13 12:21:11)
- `neuron/sdk@f24dea16e-dirty` (2024-01-13 16:21:53)
- `helia/3.0.1 libp2p/1.1.2 UserAgent=v20.10.0` (2024-01-14 04:22:43)
- `kubo/0.23.0-dev/7977f26-dirty` (2024-01-14 05:21:05)
- `kubo/0.26.0-dev/b215d73e4-dirty/docker` (2024-01-14 16:51:43)
- `example.com/pain@` (2024-01-14 17:22:03)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/tss/keySign/session/61a666c2-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/6cfc7ae9-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/1da43034-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/01962e78-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/7ab483df-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/7ab55189-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/8c9a4409-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/9f19a799-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/a80c8da6-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/c2e824f6-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/68cf2843-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/dd2ab161-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/e6213b36-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/137e83cb-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/75ef927b-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/9e7fdc5e-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/b493ad47-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/def78dfd-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/fc364d5d-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/12e396a1-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/83a7401f-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/844110c8-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/e7eba122-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/09efa1e3-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/958db9c5-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/bb254de7-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/cbdc2b9c-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/e6ba3a8b-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/1bd9cf28-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/68ce0397-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/8e654b91-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/cb4320d9-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/f342818e-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/0e1eaab6-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/6a99e2ad-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/a7739e55-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/aba0e25d-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/dd2ce9b8-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/99babedb-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/a04b15e0-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/b066ba51-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/bd87e14f-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/d865b32c-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/f8077a4b-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/7ee24641-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/857281a8-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/9e80c21e-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/c24ebfc3-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/c4199ef3-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/f0dfde77-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/71c231ff-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/7b4e40d9-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/d4355cc7-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/052a71a8-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:11)
- `/tss/keySign/session/1bd7b363-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/71c16b85-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/f9d3b5d1-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/b95acc87-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/d437bd03-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/e15a3c53-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/f8a24a25-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/d4d16fe5-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/ddc5e0b2-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/ef154d96-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/0bbc1173-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/958cd614-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/ea4e4dcd-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/14b009ab-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/1c72b951-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/87d5433a-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/8d33dcfb-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/83a84014-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/a93e2640-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/6074dfe9-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/90c7dec4-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/a2adafba-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/d2e08cde-adbd-11ee-81bd-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/a772b4ae-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/7c7fac03-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/975807a9-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/b9f3d30d-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/efae605d-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/1712a038-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/d2de4735-adbd-11ee-81bd-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/5fd85d82-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/96268fa6-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/b065ef49-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/b958984a-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/0a8a7e67-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/f8094573-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/02c7c339-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/b230fcc6-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/cb412110-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/cf704f1e-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/6409063b-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/12e56ab0-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/725b70b2-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/738d0115-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/c67c307d-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/cd0d9a74-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/d602e582-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/09f1af26-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/00fd4885-adc0-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/8c9b0f92-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/b0ff8765-adbf-11ee-bd8f-0242c0a60a78` (2024-01-08 00:52:12)
- `/tss/keySign/session/2624d762-ae03-11ee-bd37-0242c0a60a78` (2024-01-08 08:52:31)
- `/tss/keySign/session/258ad99b-ae03-11ee-bd37-0242c0a60a78` (2024-01-08 08:52:31)
- `/tss/keySign/session/258be48d-ae03-11ee-bd37-0242c0a60a78` (2024-01-08 08:52:31)
- `/tss/keySign/session/2756592e-ae03-11ee-bd37-0242c0a60a78` (2024-01-08 08:52:31)
- `/tss/keySign/session/29b8eb86-ae03-11ee-bd37-0242c0a60a78` (2024-01-08 08:52:31)
- `/tss/keySign/session/3dd39d8e-ae03-11ee-bd37-0242c0a60a78` (2024-01-08 08:52:31)
- `/tss/keySign/session/3dd45389-ae03-11ee-bca7-0242c0a60a78` (2024-01-08 08:52:31)
- `/tss/keySign/session/b0486cbc-ae0b-11ee-8490-0242c0a60a78` (2024-01-08 09:52:57)
- `/tss/keySign/session/b04eff62-ae0b-11ee-8da4-0242c0a60a78` (2024-01-08 09:52:57)
- `/tss/keySign/session/b0536b75-ae0b-11ee-8727-0242c0a60a78` (2024-01-08 09:52:57)
- `/tss/keySign/session/b71cf052-ae0b-11ee-8da4-0242c0a60a78` (2024-01-08 09:53:13)
- `/tss/keySign/session/b71fadff-ae0b-11ee-8490-0242c0a60a78` (2024-01-08 09:53:13)
- `/tss/keySign/session/b712f8c1-ae0b-11ee-8727-0242c0a60a78` (2024-01-08 09:53:13)
- `/tss/keySign/session/bcf368c7-ae0b-11ee-8727-0242c0a60a78` (2024-01-08 09:53:23)
- `/tss/keySign/session/bcfeff84-ae0b-11ee-8da4-0242c0a60a78` (2024-01-08 09:53:23)
- `/tss/keySign/session/bcf379d9-ae0b-11ee-8490-0242c0a60a78` (2024-01-08 09:53:23)
- `/tss/keySign/session/4185fbf9-ae18-11ee-81eb-0242c0a60a78` (2024-01-08 11:23:00)
- `/tss/keySign/session/418d4fbe-ae18-11ee-a93d-0242c0a60a78` (2024-01-08 11:23:00)
- `/tss/keySign/session/4181f0cf-ae18-11ee-a2ba-0242c0a60a78` (2024-01-08 11:23:00)
- `/tss/keySign/session/60372aa5-ae1c-11ee-ae37-0242c0a60a78` (2024-01-08 11:52:30)
- `/tss/keySign/session/60406825-ae1c-11ee-8c5f-0242c0a60a78` (2024-01-08 11:52:30)
- `/tss/keySign/session/6041ccc5-ae1c-11ee-ac9a-0242c0a60a78` (2024-01-08 11:52:30)
- `/tss/keySign/session/69cb1645-ae1c-11ee-ac9a-0242c0a60a78` (2024-01-08 11:52:53)
- `/tss/keySign/session/aafff026-ae48-11ee-bcca-0242c0a60a78` (2024-01-08 18:22:56)
- `/tss/keySign/session/ad62b315-ae48-11ee-bcca-0242c0a60a78` (2024-01-08 18:22:56)
- `use_local_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-01-09 18:22:43)
- `use_local_state_averager::TrainingStateAverager.rpc_join_group` (2024-01-09 18:22:43)
- `use_local_state_averager::TrainingStateAverager.rpc_download_state` (2024-01-09 18:22:43)
- `/edgevpn/egress/0.1` (2024-01-11 12:50:51)
- `src-vtx-frame_grad_averager::GradientAverager.rpc_download_state` (2024-01-11 12:51:25)
- `src-vtx-frame_grad_averager::GradientAverager.rpc_aggregate_part` (2024-01-11 12:51:25)
- `src-vtx-frame_grad_averager::GradientAverager.rpc_join_group` (2024-01-11 12:51:25)
- `src-vtx-frame_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-01-11 12:51:25)
- `src-vtx-frame_state_averager::TrainingStateAverager.rpc_join_group` (2024-01-11 12:51:25)
- `src-vtx-frame_state_averager::TrainingStateAverager.rpc_download_state` (2024-01-11 12:51:25)
- `/go-orbit-db/direct-channel/1.2.0` (2024-01-11 14:22:34)
- `/wesh/contact_req/1.0.0` (2024-01-11 14:22:34)
- `wesh/p2p/localrecord` (2024-01-11 14:22:34)
- `s25_run_v2_state_averager::TrainingStateAverager.rpc_join_group` (2024-01-12 17:20:51)
- `s25_run_v2_state_averager::TrainingStateAverager.rpc_download_state` (2024-01-12 17:20:51)
- `s25_run_v2_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-01-12 17:20:51)
- `my-protocol-id` (2024-01-13 16:21:53)
- `/nrn-protocol-id/1.0.0` (2024-01-13 19:50:56)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `172.33.1.5` | US | 371 | ['go-ipfs/0.12.1/', 'kubo/0.15.0/3ae52a4', 'kubo/0.19.1/', 'kubo/0.22.0/3f884d3/docker']| False  |
| `159.203.76.161` | US | 195 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `212.47.234.38` | FR | 98 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.128.68` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.129.249` | FR | 75 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.67.193` | FR | 60 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 59 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 57 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 57 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.128.68` | IN | 48 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-01-08` to `2024-01-15` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-01-08` to `2024-01-15` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-01-08` to `2024-01-15` in the DHT and their datacenter association.

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