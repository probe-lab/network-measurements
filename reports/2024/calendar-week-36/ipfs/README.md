# Nebula Measurement Results Calendar Week 36 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 36 - 2024](#nebula-measurement-results-calendar-week-36---2024)
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

The following results show measurement data that were collected in calendar week 36 in 2024 from `2024-09-02` to `2024-09-09`.

- Number of crawls `336`
- Number of visits `23,807,358`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `64,036`
- Number of unique peer IDs discovered in the DHT `63,746`
- Number of unique IP addresses found `108,662`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20240902003409` (2024-09-02 01:51:07)
- `bootnode-20240902044329` (2024-09-02 05:21:08)
- `github.com/harmony-one/harmony@c44c2ea8c` (2024-09-02 07:20:57)
- `bootnode-20240902104643` (2024-09-02 08:51:02)
- `bootnode-20240902083019` (2024-09-02 09:20:56)
- `bootnode-20240902093853` (2024-09-02 10:51:18)
- `bootnode-20240902103311` (2024-09-02 11:20:56)
- `bootnode-20240902123702` (2024-09-02 13:51:22)
- `bootnode-20240902140133` (2024-09-02 14:21:22)
- `kubo/0.30.0-rc2/467fc69e9-dirty` (2024-09-02 17:51:12)
- `bootnode-20240902163731` (2024-09-02 19:20:48)
- `bootnode-20240902192659` (2024-09-02 19:50:54)
- `bootnode-20240902191257` (2024-09-02 20:50:51)
- `bootnode-20240902211724` (2024-09-02 21:51:25)
- `kubo/0.31.0-dev/23ca1dd/docker` (2024-09-02 22:21:24)
- `bootnode-20240902224750` (2024-09-03 00:50:53)
- `bootnode-20240903021647` (2024-09-03 02:51:13)
- `github.com/libp2p/go-libp2p/examples@d55bed5f7-dirty` (2024-09-03 03:21:00)
- `bootnode-20240903051935` (2024-09-03 03:21:07)
- `bootnode-20240903040855` (2024-09-03 04:21:17)
- `bootnode-20240903082052` (2024-09-03 08:21:07)
- `bootnode-20240903092805` (2024-09-03 09:50:50)
- `bootnode-20240903115021` (2024-09-03 09:51:21)
- `bootnode-20240903121912` (2024-09-03 12:21:06)
- `helia/4.2.5 libp2p/1.9.3 UserAgent=v20.12.1` (2024-09-03 12:21:36)
- `bootnode-20240903133926` (2024-09-03 14:21:02)
- `bootnode-20240903152944` (2024-09-03 16:20:48)
- `bootnode-20240826190652` (2024-09-03 19:20:50)
- `bootnode-20240826190745` (2024-09-03 19:21:15)
- `bootnode-20240903200613` (2024-09-03 20:20:54)
- `bootnode-20240903224406` (2024-09-03 23:50:54)
- `bootnode-20240903235431` (2024-09-04 00:21:13)
- `bootnode-20240904032048` (2024-09-04 03:21:09)
- `bootnode-20240904055511` (2024-09-04 06:51:32)
- `bootnode-20240904083840` (2024-09-04 09:21:19)
- `github.com/libp2p/universal-connectivity/go-peer@21cb6bb27` (2024-09-04 12:50:54)
- `github.com/INFURA/ipfs-p2p-server@6173603cc` (2024-09-04 13:21:01)
- `github.com/INFURA/ipfs-p2p-server@dee6a5212` (2024-09-04 13:21:40)
- `bootnode-20240904175059` (2024-09-04 17:51:34)
- `bootnode-20240904194759` (2024-09-04 19:50:57)
- `bootnode-20240904224814` (2024-09-04 22:50:48)
- `bootnode-20240904235109` (2024-09-04 23:51:27)
- `bootnode-20240905012113` (2024-09-05 01:21:18)
- `bootnode-20240905042701` (2024-09-05 02:51:23)
- `bootnode-20240905024436` (2024-09-05 03:20:52)
- `bootnode-20240905032353` (2024-09-05 04:21:21)
- `bootnode-20240904233925` (2024-09-05 04:51:06)
- `bootnode-20240905060021` (2024-09-05 04:51:15)
- `bootnode-20240905050541` (2024-09-05 05:50:56)
- `bootnode-20240905073044` (2024-09-05 05:50:59)
- `bootnode-20240905055832` (2024-09-05 08:51:16)
- `bootnode-20240905115055` (2024-09-05 11:51:08)
- `helia/4.2.5 libp2p/1.9.3 UserAgent=v20.17.0` (2024-09-05 13:50:57)
- `bootnode-20240905133125` (2024-09-05 14:21:21)
- `kubo/0.31.0-dev/cc2402c/docker` (2024-09-05 15:51:03)
- `kubo/0.31.0-dev/cc2402c25-dirty` (2024-09-05 15:51:29)
- `bootnode-20240905164218` (2024-09-05 16:50:51)
- `bootnode-20240905201256` (2024-09-05 18:21:15)
- `bootnode-20240905154234` (2024-09-05 21:20:56)
- `kubo/0.31.0-dev/6454bdb/1234567890123456789012345678901234567890` (2024-09-05 22:20:50)
- `kubo/0.31.0-dev/680d420/docker` (2024-09-05 22:20:54)
- `kubo/0.31.0-dev/6454bdb/docker` (2024-09-05 22:21:34)
- `kubo/0.30.0-rc3/2b1af8d/1234567890123456789012345678901234567890` (2024-09-05 23:50:54)
- `kubo/0.30.0-rc3/` (2024-09-06 00:21:43)
- `bootnode-20240906002840` (2024-09-06 00:51:32)
- `bootnode-20240906012012` (2024-09-06 01:21:22)
- `bootnode-20240906022043` (2024-09-06 02:20:54)
- `bootnode-20240906032053` (2024-09-06 03:21:26)
- `bootnode-20240906053704` (2024-09-06 05:51:12)
- `bootnode-20240906055624` (2024-09-06 06:51:04)
- `libp2p/1.9.4 UserAgent=v22.1.0` (2024-09-06 09:51:13)
- `bootnode-20240906035527` (2024-09-06 10:21:04)
- `bootnode-20240906092744` (2024-09-06 10:51:02)
- `bootnode-20240906135354` (2024-09-06 12:21:18)
- `bootnode-20240906080356` (2024-09-06 13:21:45)
- `bootnode-20240906083704` (2024-09-06 13:50:51)
- `bootnode-20240906085741` (2024-09-06 14:21:04)
- `bootnode-20240906094506` (2024-09-06 15:20:54)
- `kubo/0.31.0-dev/6454bdb4e-dirty` (2024-09-06 15:51:39)
- `helia/4.2.5 libp2p/1.9.4 UserAgent=v22.7.0` (2024-09-06 18:21:17)
- `bootnode-20240906152052` (2024-09-06 20:21:36)
- `bootnode-20240906154536` (2024-09-06 21:21:00)
- `bootnode-20240906211632` (2024-09-06 21:50:59)
- `bootnode-20240906220906` (2024-09-07 02:21:03)
- `bootnode-20240907015938` (2024-09-07 03:20:53)
- `bootnode-20240907014710` (2024-09-07 06:50:55)
- `bootnode-20240907065043` (2024-09-07 06:51:02)
- `bootnode-20240907072036` (2024-09-07 07:20:58)
- `bootnode-20240907090802` (2024-09-07 07:50:50)
- `kubo/0.31.0-dev/6454bdb4e` (2024-09-07 09:21:18)
- `bootnode-20240907052028` (2024-09-07 10:21:05)
- `bootnode-20240907113521` (2024-09-07 11:51:17)
- `bootnode-20240907120259` (2024-09-07 13:20:59)
- `bootnode-20240907164854` (2024-09-07 15:21:17)
- `bootnode-20240907104007` (2024-09-07 15:50:50)
- `bootnode-20240907155020` (2024-09-07 16:21:01)
- `bootnode-20240907113540` (2024-09-07 17:20:52)
- `bootnode-20240907160916` (2024-09-07 17:21:18)
- `bootnode-20240907171206` (2024-09-07 17:51:20)
- `bootnode-20240907172444` (2024-09-07 18:51:54)
- `bootnode-20240907190940` (2024-09-07 19:51:07)
- `bootnode-20240907234955` (2024-09-07 21:51:09)
- `bootnode-20240908020014` (2024-09-08 00:51:46)
- `libp2p/1.3.3 UserAgent=v22.8.0` (2024-09-08 01:51:17)
- `bootnode-20240908012023` (2024-09-08 06:21:12)
- `bootnode-20240908014132` (2024-09-08 06:51:06)
- `bootnode-20240908024710` (2024-09-08 07:51:08)
- `bootnode-20240908025736` (2024-09-08 08:51:00)
- `bootnode-20240908120128` (2024-09-08 10:50:58)
- `bootnode-20240908082724` (2024-09-08 10:51:13)
- `bootnode-20240908111754` (2024-09-08 11:21:02)
- `bootnode-20240908061019` (2024-09-08 11:21:15)
- `seed/<dev>` (2024-09-08 11:21:19)
- `bootnode-20240908065038` (2024-09-08 11:51:13)
- `bootnode-20240908120738` (2024-09-08 13:51:20)
- `bootnode-20240908095017` (2024-09-08 14:50:51)
- `bootnode-20240908151925` (2024-09-08 15:21:04)
- `kubo/0.30.0-rc3/2b1af8d/docker` (2024-09-08 16:20:43)
- `bootnode-20240908153815` (2024-09-08 16:21:14)
- `bootnode-20240909001259` (2024-09-08 22:50:51)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/mobazha/kad/1.0.0` (2024-09-06 01:50:57)
- `/hypermedia/0.4.0` (2024-09-08 11:21:19)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `51.15.247.127` | FR | 88 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.150.159` | FR | 85 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 78 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 78 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | NL | 76 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.42.192` | FR | 76 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 70 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 68 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 68 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `68.183.11.180` | NL | 52 | ['edgevpn']| True  |

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

In the specified time interval from `2024-09-02` to `2024-09-09` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-09-02` to `2024-09-09` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-09-02` to `2024-09-09` in the DHT and their datacenter association.

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