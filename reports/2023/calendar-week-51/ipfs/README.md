# Nebula Measurement Results Calendar Week 51 - 2023

## Table of Contents

- [Nebula Measurement Results Calendar Week 51 - 2023](#nebula-measurement-results-calendar-week-51---2023)
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

The following results show measurement data that were collected in calendar week 51 in 2023 from `2023-12-18` to `2023-12-25`.

- Number of crawls `336`
- Number of visits `45,962,902`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `70,859`
- Number of unique peer IDs discovered in the DHT `66,934`
- Number of unique IP addresses found `85,213`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `xcp` (2023-12-18 06:52:39)
- `kubo/0.25.0/413a52d0e/desktop` (2023-12-20 15:52:30)
- `changeme@b111a7e17-dirty` (2023-12-20 17:22:18)
- `kubo/0.26.0-dev/0fdd97911-dirty` (2023-12-21 16:21:55)
- `kubo/0.25.0/desktop` (2023-12-21 16:52:34)
- `kubo/0.26.0-dev/f71ae39/docker` (2023-12-21 18:52:14)
- `kubo/0.20.0-dev/1f5763f78` (2023-12-22 01:22:32)
- `kubo/0.24.0/e70db65-dirty` (2023-12-22 23:21:52)
- `kubo/0.26.0-dev/58ebfd29e-dirty` (2023-12-23 19:52:29)
- `kubo/0.26.0-dev/58ebfd29e` (2023-12-24 09:21:34)
- `kubo/0.25.0/18fa415-dirty` (2023-12-24 17:23:52)
- `kubo/0.26.0-dev/58ebfd2/docker` (2023-12-24 18:21:59)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/tss/keySign/session/ea6d758a-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/77bf3bbc-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/f282164c-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/7592fb09-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/3450719d-9d3e-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55cd4b3a-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/d05ee90c-9d4b-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/58d675c9-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/e56feda5-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd630a2-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd6c8de-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/fc12a14e-9d46-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/58db083c-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd66545-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/b243fed8-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/d05efa6c-9d4b-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd6c9b4-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/8294c859-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/48ca19bb-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd6c470-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/7592fb9e-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/07eab4c4-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/65dc77ec-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/11a24f61-9d4b-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4dd83435-9d4d-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/48dba268-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/a2e2c146-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/58d7b05e-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/13d6e888-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/5b6d1fbb-9d47-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55db1a54-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/82927ed5-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/8292a710-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/8292c9c1-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/2baf6c8e-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/babe0860-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/797a5ccf-9d40-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/62e10dec-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/63758532-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/6abd157a-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/48c9e694-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/ea6afc41-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/1ea6d285-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/1ea6d3f3-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/1ea6d4ea-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/5ecdd19b-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4dd8374e-9d4d-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/fef77839-9d3e-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/1ea6d665-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55dc6e9f-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/5ed12b01-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55dae72d-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55dc0fea-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/bf478ef8-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/1f382b68-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/9100950d-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd53a96-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/7592c555-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/848b3088-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/ae47dcba-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55db8237-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/58d625a8-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/48daeb77-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/51cd3b9a-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/2bb122f1-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/62d77489-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/65dbd6a6-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/58d67625-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/d05ef527-9d4b-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/7592fee5-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd58a56-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/58d6abb8-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/1f394c78-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55db30cf-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55dc0fd3-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/7592fd07-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/65dc77e6-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/6c66e62c-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/ddf6acf7-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/b2402d46-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/48db2f00-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/f6f37e81-9d41-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/6ab87698-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/11a0f5a2-9d4b-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd63313-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/51cd3855-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/902aab60-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55dfea73-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4bd6654a-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/3154aa8e-9d3e-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/1ea6d7e1-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/8292a452-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/75930272-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55cd577a-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/f1e4381d-9d44-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/dd634bc8-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/119fc495-9d4b-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/747c9a4c-9d4b-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/55cd4c55-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/4dd83555-9d4d-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/72e642d2-9d3e-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/67e5eb74-9d41-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/48ca136f-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/96f6ac20-9d3f-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/58d746e3-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/dd634780-9d45-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/82927804-9d4a-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/759303f8-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 02:52:57)
- `/tss/keySign/session/c35edeba-9d51-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/04a223f1-9d51-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/c35ecd28-9d51-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/c35ee293-9d51-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/c35ee1ac-9d51-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/a5430eef-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/a542e10e-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/c35ee08d-9d51-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/a542e02c-9d50-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/c35f0fef-9d51-11ee-93fa-0242c0a60a78` (2023-12-18 03:22:56)
- `/tss/keySign/session/cfdc790b-9db0-11ee-9429-0242c0a60a78` (2023-12-18 14:22:19)
- `MediaLibrary/kad/1.0.0` (2023-12-23 02:52:49)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 209 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `212.47.234.38` | FR | 196 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.67.193` | FR | 92 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.189.73` | FR | 87 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 51 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `163.172.142.51` | FR | 46 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `172.33.1.5` | US | 44 | ['go-ipfs/0.12.1/', 'kubo/0.15.0/3ae52a4', 'kubo/0.17.0/4485d6b', 'kubo/0.22.0/3f884d3/docker']| False  |
| `51.159.154.220` | FR | 41 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `54.246.7.156` | IE | 39 | ['avail-light-client/rust-client']| True  |
| `51.158.240.182` | FR | 31 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2023-12-18` to `2023-12-25` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2023-12-18` to `2023-12-25` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2023-12-18` to `2023-12-25` in the DHT and their datacenter association.

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

Code can be found here: [dennis-tra/parsec](https://github.com/dennis-tra/parsec) (we plan to move this to our [ProbeLab organization](https://github.com/plprobelab))

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