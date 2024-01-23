# Nebula Measurement Results Calendar Week 47 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 47 - 2023](#nebula-measurement-results-calendar-week-47---2023)
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

The following results show measurement data that were collected in calendar week 47 in 2023 from `2023-11-20` to `2023-11-27`.

- Number of crawls `336`
- Number of visits `37,920,667`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `44,985`
- Number of unique peer IDs discovered in the DHT `43,515`
- Number of unique IP addresses found `61,342`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `github.com/selesy/p2p/badbitswap@` (2023-11-20 17:52:32)
- `kubo/0.24.0/e70db6531-dirty` (2023-11-21 07:21:43)
- `github.com/metis-seq/tss-server@149c90592` (2023-11-21 09:52:32)
- `kubo/0.25.0-dev/48865a9` (2023-11-21 13:52:12)
- `rust-libp2p/0.44.0` (2023-11-21 18:21:50)
- `kubo/0.20.0-dev/684d9dc/docker` (2023-11-22 03:52:35)
- `kubo/0.25.0-dev/3ae04c536` (2023-11-22 22:21:29)
- `go.vocdoni.io/dvote@7f782205f-dirty` (2023-11-23 11:52:25)
- `go.vocdoni.io/dvote@89d1db7f3-dirty` (2023-11-23 14:52:24)
- `go.vocdoni.io/dvote@656988fa2-dirty` (2023-11-23 16:22:25)
- `kubo/0.25.0-dev/3ae04c5/docker` (2023-11-23 23:52:24)
- `github.com/metis-seq/tss-server@9b02353a8` (2023-11-24 03:21:40)
- `github.com/metis-seq/tss-server@2a873b2e7` (2023-11-25 03:52:26)
- `github.com/metis-seq/tss-server@e5a6a04de` (2023-11-25 11:52:37)
- `kubo/0.24.0-rc1/3851311/docker` (2023-11-25 16:52:38)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/tss/keySign/session/75d49b6e-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/8ce0c868-881b-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/72d9b3a3-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/75d49b73-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/7c5f1feb-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/87b7ffb3-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/2e9f71cf-8828-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/eded1d3a-8828-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/cc610c8f-881e-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/0896b3d8-8821-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/82dd8d9b-8821-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/72d8b10b-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/2f31579b-8828-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/77ddc898-8824-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/ed5beeca-8828-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/82dd8da0-8821-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/88d3a3e3-8821-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/3ba78929-8822-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/fa640ae2-8822-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/75d3e960-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/9f9092f1-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/8fdbf362-881b-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/7bcbc1a0-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/72d8af7f-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/7c601802-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/cfd30186-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/2f315776-8828-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/77dd8bcf-8824-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/75d3eb8a-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/75d4161e-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/87b7fbdc-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/884c184f-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/ededc38d-8828-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/736e81e1-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/7bca215f-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/a023a96e-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/ededc389-8828-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/109bf70d-881e-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/d135043e-8824-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/faf800b4-8822-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/766a0b95-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/ad2e0b24-8821-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/75d4190c-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/75d4c798-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/7669bd0f-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/e9476195-881b-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/fa653b64-8822-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/736ee6d1-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/7bca2d1d-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/7c5fef1e-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/884b2b08-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/884bf54a-8827-11ee-afc1-0242c0a60a78` (2023-11-21 04:52:33)
- `/tss/keySign/session/5dd1bd9e-8830-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/c23fe409-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6ecb9bb6-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/c23fe62b-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e05ae4a7-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6b66527b-882a-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/68d57414-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/7ab8eb6a-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/219e50cc-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/c23e8294-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/219d0cb2-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/68d57410-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/7ab7f9b4-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/c2401ae7-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/5dd2090b-8830-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/7ab8be02-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/5dd1c4f0-8830-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6b66533e-882a-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6ecb1f91-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6ecc0fa6-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/219cdb2c-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e0593228-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e0593224-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/219d2ea7-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/665701cb-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/92909922-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e05ab2ab-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6ad553a2-882a-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/65da5013-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/68d59cb1-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/7ab7104e-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e0598e1c-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/68d6a998-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6ecaf61c-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e0598d9b-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/7ab8bf32-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/928ee86a-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/5dd35043-8830-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/65daaba2-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/92909929-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/c23ed843-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/5dd35027-8830-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/9290a38d-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e05ab519-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/7ab79ba5-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/7ab7c742-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/5dd1ef26-8830-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/5dd35225-8830-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/928f4e7d-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/68d5e7b5-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/928f7784-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/c23ed0dc-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6eccb61e-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/928ee870-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e05931f2-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/68d6a99c-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/65d9c1d4-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/e05ab34b-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/68d6a9bd-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6ecb9da2-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6ecce618-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/6ad37c8a-882a-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/219e548f-882e-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/65d99cd6-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/c23e45cb-882d-11ee-afc1-0242c0a60a78` (2023-11-21 05:52:39)
- `/tss/keySign/session/9c2c4137-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/9c368d82-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/6f155bc4-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/993aa5d5-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/a22f75fe-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/993de8a9-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/9c395fe2-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/a22297a1-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/ae10dbd5-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/b40ac53a-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/13b15c76-8939-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/750ec3ef-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/ae0ea755-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/54f4c7ef-8938-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/6f18904b-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/f5964b05-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/9930feb8-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/c5e67e74-8937-11ee-8eae-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/ae144416-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/ae1ba456-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/b40709b9-8937-11ee-95ef-0242c0a60a78` (2023-11-22 13:22:31)
- `/tss/keySign/session/c9e7490b-895f-11ee-aebd-0242c0a60a78` (2023-11-22 17:52:38)
- `/tss/keySign/session/cce2e0b1-895f-11ee-aebd-0242c0a60a78` (2023-11-22 17:52:38)
- `/ubsv/bitcoin/alert-system/1.0.1` (2023-11-23 05:52:48)
- `/tss/keySign/session/264fd67e-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/26512283-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/f9340df2-8a95-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/45407cb1-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/9409a1fc-8a9e-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/ab44d9f3-8a9e-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/265071f8-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/265116f1-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/383488d1-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/df1a9a31-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/6a25890d-8a95-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/eab743d3-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/251493db-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2651684d-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/26e9f7b4-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2c479979-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2ce02831-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/9d7dad4a-8a98-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/322a8176-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/285e9534-8a9e-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/251f0f3e-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/51d446df-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/7fbc429b-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/9dd71d26-8aa2-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/9dd72261-8aa2-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/356944fe-8a98-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/5d19a867-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/45406f79-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/5ee0f6d5-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/deca5c43-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/df19c548-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/48cfb9af-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/50a405d4-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/df19c48e-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/323f8d83-8aa2-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/30623aba-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/33bf4d97-8a9d-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/910e646e-8a9e-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2355d5d0-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/9f9e6853-8aa2-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/ec887257-8a9d-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2a23c412-8a9e-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/38332a22-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/81839aef-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/d8d44028-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/df1a4a07-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/dfb1bb96-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/3061419b-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/8cca1ff2-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/38350fe8-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/7fbc43d1-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/df1a0f2c-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/6a258a1b-8a95-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/f9340c28-8a95-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/500c5c58-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/45a165fc-8a9d-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/285da1c4-8a9e-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/34fefe17-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/8e9048eb-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/264fd683-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/919eaad6-8aa2-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2912f2ac-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/453f7f78-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/28bd6b8d-8aa0-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/26509b06-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/281a339a-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/7c864cee-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/ec28aa35-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/285e9622-8a9e-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2c47ae53-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/38350f18-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/39fc72e6-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/80535e9e-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/1412ed39-8a97-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/234e4fed-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/9dd7801d-8aa2-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/a078cc5e-8a98-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/5d18166a-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/17ffa855-8a9a-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/30625326-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/8cca08e9-8a9b-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2354acea-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/500ceb6f-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/7fbbe5e9-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/9aa16632-8a95-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/0f0403ba-8a9a-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/df1a541d-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/234cf780-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/2e106473-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/500af837-8aa1-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/969a675f-8a95-11ee-b6a8-0242c0a60a78` (2023-11-24 08:22:42)
- `/tss/keySign/session/3d6df86b-8a95-11ee-b6a8-0242c0a60a78` (2023-11-24 09:52:48)
- `/tss/keySign/session/d7ddf817-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 09:52:48)
- `/tss/keySign/session/3d6df525-8a95-11ee-b6a8-0242c0a60a78` (2023-11-24 09:52:48)
- `/tss/keySign/session/4cd6cea8-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 09:52:48)
- `/tss/keySign/session/dbe4d719-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 09:52:48)
- `/tss/keySign/session/30f78608-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 09:52:48)
- `/tss/keySign/session/787f5e47-8a94-11ee-b6a8-0242c0a60a78` (2023-11-24 09:52:48)
- `/tss/keySign/session/b7267ae1-8b3d-11ee-be34-0242c0a60a78` (2023-11-25 02:52:51)
- `/tss/keySign/session/b992034b-8b3d-11ee-a567-0242c0a60a78` (2023-11-25 02:52:51)
- `/tss/keySign/session/b3dae13e-8b3d-11ee-bf64-0242c0a60a78` (2023-11-25 02:53:01)
- `/tss/keySign/session/b3d39196-8b3d-11ee-bf64-0242c0a60a78` (2023-11-25 02:53:01)
- `/tss/keySign/session/7c4d31e1-8b67-11ee-aa98-0242c0a60a78` (2023-11-25 07:52:57)
- `/tss/keySign/session/7f48f877-8b67-11ee-aa98-0242c0a60a78` (2023-11-25 07:52:57)
- `/tss/keySign/session/5b70c583-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/04bfdfb7-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/b793bbd3-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/25383a14-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/f07e9947-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/f379dd18-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/93cfe20b-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/f9700e54-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/025703d0-8c4e-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/51ed8849-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/db050a6a-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/ece7ba68-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/e0fb3c56-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/9fbbfef9-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/528bdb55-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/4f83b390-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/055e8dc4-8c4e-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/9fb8e149-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/46926819-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/46a1e9bd-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/498d9b68-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/e7433fc5-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/055c2162-8c4e-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/1d31b17a-8c4e-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/1d345c61-8c4e-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/3a15b546-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/819d05a0-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/8adc0491-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/93ceffc5-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/d8096b94-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/346ff623-8c4c-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/7348acff-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/2833786b-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/2e298bdc-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/e0fc6cd9-8c4b-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/tss/keySign/session/a2f7f648-8c4d-11ee-949d-0242c0a60a78` (2023-11-26 11:22:45)
- `/hypermedia/0.2.0-dev` (2023-11-26 20:22:56)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 223 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `51.159.129.249` | FR | 139 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `212.47.234.38` | FR | 99 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `172.66.43.100` | US | 59 | ['kubo/0.22.0/3f884d3/docker', 'kubo/0.23.0/3a1a041/docker', 'kubo/0.24.0/e70db65/docker']| True  |
| `172.66.40.156` | US | 58 | ['kubo/0.22.0/3f884d3/docker', 'kubo/0.23.0/3a1a041/docker', 'kubo/0.24.0/e70db65/docker']| True  |
| `151.115.54.82` | PL | 52 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 49 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `172.33.1.5` | US | 48 | ['kubo/0.15.0/3ae52a4', 'kubo/0.22.0/3f884d3/docker']| False  |
| `92.255.108.209` | RU | 37 | ['edgevpn']| False  |
| `51.158.235.20` | FR | 32 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2023-11-20` to `2023-11-27` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-11-20` to `2023-11-27` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-11-20` to `2023-11-27` in the DHT and their datacenter association.

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