# Nebula Measurement Results Calendar Week 1 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 1 - 2024](#nebula-measurement-results-calendar-week-1---2024)
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
    - [Peer Classification](#peer-classification)
    - [Storm Specific Protocols](#storm-specific-protocols)


## General Information

The following results show measurement data that were collected in calendar week 1 in 2024 from `2024-01-01` to `2024-01-08`.

- Number of crawls `336`
- Number of visits `42,132,135`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `67,400`
- Number of unique peer IDs discovered in the DHT `64,029`
- Number of unique IP addresses found `87,524`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `kubo/0.26.0-dev/16494692e` (2024-01-01 00:52:44)
- `chat-with` (2024-01-01 16:22:38)
- `kubo/0.22.0/b9000a9d6` (2024-01-02 16:52:12)
- `github.com/metis-seq/tss-server@3078f1b3a` (2024-01-03 00:52:32)
- `kubo/0.26.0-dev/765cffe6c` (2024-01-03 03:52:35)
- `github.com/metis-seq/tss-server@e387e4500` (2024-01-03 16:52:19)
- `kubo/0.26.0-dev/377cdd6ba-dirty` (2024-01-03 22:52:31)
- `kubo/0.26.0-dev/14d1e899d-dirty` (2024-01-04 00:22:40)
- `pw-p2p@f17cdf0bd-dirty` (2024-01-04 03:22:05)
- `pw-p2p@5fc94afa4-dirty` (2024-01-04 03:22:34)
- `github.com/metis-seq/tss-server@396f42130` (2024-01-04 12:53:07)
- `js-libp2p/0.45.9 UserAgent=v20.10.0` (2024-01-04 14:22:08)
- `kubo/0.26.0-dev/b215d73e4` (2024-01-05 04:22:20)
- `github.com/metis-seq/tss-server@63db4258d` (2024-01-06 02:22:41)
- `p2p@` (2024-01-06 08:52:31)
- `github.com/metis-seq/tss-server@6f04a3088` (2024-01-07 13:52:53)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/tss/keySign/session/c262a281-a88c-11ee-94bd-0242c0a60a78` (2024-01-01 10:23:06)
- `/needyleaks/search/0.0.1` (2024-01-01 19:52:22)
- `/ipfs-embed/bitswap/1.0.0` (2024-01-02 14:22:25)
- `/tss/keySign/session/7922c384-aa15-11ee-911c-0242c0a60a78` (2024-01-03 08:52:55)
- `/tss/keySign/session/d2efd4cf-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/24c7af84-aaf9-11ee-8cc0-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/b0e3494d-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/c4020cb0-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/c49aeecc-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/ccf40551-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/b214dda4-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/b4777e52-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/ba7308c1-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/bba47be4-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/be072911-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/c2cc34a3-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/c82f06fa-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/cec2ca56-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/b04a5474-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/b93c9032-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/d08d1b7b-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/d7b4cba3-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/24cdeecd-aaf9-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/c5cc637a-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/cf5b9b2c-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/b9da292d-aaff-11ee-8e05-0242c0a60a78` (2024-01-04 12:53:07)
- `/tss/keySign/session/50016134-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/2fbedcdb-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/3d7ae440-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/1a1291cc-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/1e84d9a6-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/fb98f5d7-abad-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/03f7af56-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/440f460c-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/f9ce990d-abad-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/0e61206d-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/28adc26c-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/3057a888-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/68ff4a83-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/158daa48-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/319fa4ca-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/423fdc22-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/0e1ffcdf-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/213a1872-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/0acd0d06-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/2cdab626-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/600849c2-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/7fb389b8-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/13260c46-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/68612a26-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/1c752d73-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/0bfe8a59-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/145c3d13-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/1cb52cc9-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/7e821371-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/394e0cff-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/43767ce3-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/1678d53e-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:03)
- `/tss/keySign/session/0a33a64c-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/7754b607-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/fdfb9f97-abad-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/078baf71-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/18e12c67-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/6139ac5b-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/639c489c-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/6d2c1745-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/38b0a42f-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/5263f1c8-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/0c50a8dd-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/294698be-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/2a780f70-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/7de938fc-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/821617ac-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/31890cbe-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/4540b4f5-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/17f0439c-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/6ac97e82-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/73c0bed7-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/7c19aff7-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/33eb9e15-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/39e6e013-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/0529156e-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/26ddd803-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/7327e02f-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/4ecff674-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/035ee49b-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/5728d444-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/fa6792ed-abad-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/0f515e43-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/18484bc1-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/5f6f7c25-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/69981f58-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/3b184e08-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/11b3ee42-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/2218e7aa-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/02c0a4b7-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/0d872e52-abae-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/71f109b3-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/74f21a41-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/4c6820ff-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/4e373191-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/13c36a26-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/1debf3b0-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/1fb646e8-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/86db0e83-abaf-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `/tss/keySign/session/47a33d56-abab-11ee-be4e-0242c0a60a78` (2024-01-05 09:53:04)
- `defs@stream:file/download/response/1.0.0` (2024-01-06 06:22:32)
- `defs@stream:file/slice/upload/1.0.0` (2024-01-06 06:22:32)
- `/dep2p/handshake/1.0.0` (2024-01-06 06:22:32)
- `s25_run_v1_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-01-06 12:22:15)
- `s25_run_v1_state_averager::TrainingStateAverager.rpc_join_group` (2024-01-06 12:22:15)
- `s25_run_v1_state_averager::TrainingStateAverager.rpc_download_state` (2024-01-06 12:22:15)
- `lets_run_state_averager::TrainingStateAverager.rpc_aggregate_part` (2024-01-06 16:21:29)
- `lets_run_state_averager::TrainingStateAverager.rpc_join_group` (2024-01-06 16:21:29)
- `lets_run_state_averager::TrainingStateAverager.rpc_download_state` (2024-01-06 16:21:29)
- `/github.com/alx696/polong/remote_control/message` (2024-01-06 18:22:48)
- `/github.com/alx696/polong/remote_control/video` (2024-01-06 18:22:48)
- `/lilu.red/kc/1/info` (2024-01-06 18:22:48)
- `/lilu.red/kc/1/message/text` (2024-01-06 18:22:48)
- `/lilu.red/kc/1/message/file` (2024-01-06 18:22:48)
- `/tss/keySign/session/259bf903-acb4-11ee-8ff8-0242c0a60a78` (2024-01-07 00:53:06)
- `my_cifar_run_grad_averager::GradientAverager.rpc_aggregate_part` (2024-01-07 07:22:20)
- `my_cifar_run_grad_averager::GradientAverager.rpc_download_state` (2024-01-07 07:22:20)
- `my_cifar_run_grad_averager::GradientAverager.rpc_join_group` (2024-01-07 07:22:20)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `159.203.76.161` | US | 225 | ['github.com/ipfs-shipyard/ipfs-counter']| True  |
| `163.172.142.51` | FR | 120 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `212.47.234.38` | FR | 88 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.129.249` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.238.83` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.67.193` | FR | 62 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.235.20` | FR | 58 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 53 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | NL | 43 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `172.33.1.5` | US | 43 | ['go-ipfs/0.12.1/', 'kubo/0.15.0/3ae52a4', 'kubo/0.22.0/3f884d3/docker']| False  |

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

In the specified time interval from `2024-01-01` to `2024-01-08` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-01-01` to `2024-01-08` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-01-01` to `2024-01-08` in the DHT and their datacenter association.

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