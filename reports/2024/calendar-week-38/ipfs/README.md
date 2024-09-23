# Nebula Measurement Results Calendar Week 38 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 38 - 2024](#nebula-measurement-results-calendar-week-38---2024)
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

The following results show measurement data that were collected in calendar week 38 in 2024 from `2024-09-16` to `2024-09-23`.

- Number of crawls `336`
- Number of visits `23,291,646`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `64,788`
- Number of unique peer IDs discovered in the DHT `64,576`
- Number of unique IP addresses found `103,004`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20240915211400` (2024-09-16 02:20:51)
- `bootnode-20240916020313` (2024-09-16 02:51:22)
- `bootnode-20240916035804` (2024-09-16 04:21:04)
- `bootnode-20240916044139` (2024-09-16 04:21:10)
- `bootnode-20240916062051` (2024-09-16 06:51:33)
- `bootnode-20240916080232` (2024-09-16 08:21:02)
- `bootnode-20240916042716` (2024-09-16 09:51:02)
- `bootnode-20240916072052` (2024-09-16 12:21:15)
- `bootnode-20240916123206` (2024-09-16 13:21:04)
- `bootnode-20240916074126` (2024-09-16 13:21:15)
- `bootnode-20240916105122` (2024-09-16 13:51:47)
- `bootnode-20240916160309` (2024-09-16 14:20:59)
- `bootnode-20240916100318` (2024-09-16 15:50:58)
- `bootnode-20240916131153` (2024-09-16 18:51:00)
- `bootnode-20240916211830` (2024-09-17 02:50:53)
- `bootnode-20240917022341` (2024-09-17 02:51:46)
- `bootnode-20240916225033` (2024-09-17 03:51:20)
- `bootnode-20240917035938` (2024-09-17 04:20:56)
- `bootnode-20240917032132` (2024-09-17 04:21:40)
- `bootnode-20240916235525` (2024-09-17 05:21:09)
- `bootnode-20240917084548` (2024-09-17 09:21:42)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v22.4.1` (2024-09-17 09:51:38)
- `bootnode-20240917091948` (2024-09-17 10:21:22)
- `bootnode-20240917044918` (2024-09-17 10:50:52)
- `bootnode-20240917061948` (2024-09-17 11:20:52)
- `bootnode-20240917142648` (2024-09-17 12:51:23)
- `kubo/0.31.0-dev/b71cf0d/docker` (2024-09-17 13:50:51)
- `bootnode-20240917085102` (2024-09-17 13:51:12)
- `bootnode-20240917123751` (2024-09-17 14:21:24)
- `kubo/0.30.0/846c5ccf6-dirty` (2024-09-17 15:51:30)
- `bootnode-20240917110833` (2024-09-17 16:21:07)
- `bootnode-20240917130129` (2024-09-17 18:21:39)
- `bootnode-20240917134454` (2024-09-17 18:50:53)
- `bootnode-20240917164845` (2024-09-17 20:20:59)
- `bootnode-20240917145801` (2024-09-17 20:21:01)
- `bootnode-20240917204628` (2024-09-17 21:20:59)
- `bootnode-20240917172036` (2024-09-17 22:20:50)
- `bootnode-20240917204924` (2024-09-17 22:21:06)
- `bootnode-20240917215350` (2024-09-17 22:21:20)
- `bootnode-20240917225757` (2024-09-17 23:21:00)
- `bootnode-20240918000123` (2024-09-18 00:20:58)
- `bootnode-20240918005206` (2024-09-18 01:21:28)
- `bootnode-20240918013816` (2024-09-18 01:51:17)
- `bootnode-20240918004540` (2024-09-18 02:20:59)
- `bootnode-20240918045035` (2024-09-18 04:50:49)
- `bootnode-20240918055051` (2024-09-18 05:50:59)
- `bootnode-20240918080621` (2024-09-18 08:21:11)
- `bootnode-20240918075223` (2024-09-18 09:51:06)
- `bootnode-20240918062524` (2024-09-18 11:50:56)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v20.15.1` (2024-09-18 11:52:08)
- `libp2p/1.3.3 UserAgent=v22.9.0` (2024-09-18 12:51:09)
- `helia/4.2.6 libp2p/1.8.3 UserAgent=v20.15.1` (2024-09-18 12:51:56)
- `github.com/flamingotv/manager@48701e575-dirty` (2024-09-18 13:50:50)
- `bootnode-20240918130917` (2024-09-18 14:20:58)
- `kubo/0.31.0-dev/4236207/docker` (2024-09-18 14:51:10)
- `bootnode-20240918150136` (2024-09-18 15:21:01)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v20.17.0` (2024-09-18 16:21:54)
- `bootnode-20240918124436` (2024-09-18 18:21:07)
- `bootnode-20240918191022` (2024-09-18 19:51:12)
- `bootnode-20240918202040` (2024-09-18 20:20:55)
- `bootnode-20240918215210` (2024-09-18 20:51:17)
- `bootnode-20240918204113` (2024-09-18 21:21:01)
- `bootnode-20240918222052` (2024-09-18 22:21:14)
- `bootnode-20240918183725` (2024-09-19 00:21:03)
- `bootnode-20240919004909` (2024-09-19 01:50:53)
- `bootnode-20240919041241` (2024-09-19 04:51:16)
- `bootnode-20240919045925` (2024-09-19 05:20:51)
- `bootnode-20240919015023` (2024-09-19 06:51:06)
- `bootnode-20240919082045` (2024-09-19 08:20:51)
- `bootnode-20240919084437` (2024-09-19 08:20:56)
- `kubo/0.31.0-dev/b71cf0d15` (2024-09-19 08:50:52)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v20.16.0` (2024-09-19 10:21:12)
- `bootnode-20240919055029` (2024-09-19 10:50:51)
- `bootnode-20240919125915` (2024-09-19 13:21:06)
- `bootnode-20240919131430` (2024-09-19 13:50:51)
- `bootnode-20240919145039` (2024-09-19 14:50:48)
- `libp2p/2.0.2 UserAgent=v20.17.0` (2024-09-19 15:21:02)
- `bootnode-20240919121007` (2024-09-19 17:51:10)
- `bootnode-20240919194456` (2024-09-19 19:50:57)
- `bootnode-20240919184051` (2024-09-19 21:21:24)
- `bootnode-20240919224551` (2024-09-19 22:51:01)
- `kubo/0.31.0-dev/3d6cb4d3c-dirty` (2024-09-19 23:21:02)
- `bootnode-20240920005847` (2024-09-19 23:51:12)
- `bootnode-20240920002035` (2024-09-20 00:20:56)
- `bootnode-20240920011103` (2024-09-20 01:21:19)
- `bootnode-20240920002644` (2024-09-20 01:50:58)
- `kubo/0.30.0/qkpay` (2024-09-20 03:21:18)
- `bootnode-20240920072039` (2024-09-20 05:20:58)
- `bootnode-20240920052102` (2024-09-20 05:21:15)
- `bootnode-20240920083054` (2024-09-20 06:51:28)
- `bootnode-20240920093109` (2024-09-20 08:21:07)
- `kubo/0.30.0/collab.ipfscluster.io` (2024-09-20 08:51:06)
- `github.com/zzz136454872/upgradeable-consensus@3a17458df-dirty` (2024-09-20 08:51:38)
- `bootnode-20240920074957` (2024-09-20 09:51:15)
- `bootnode-20240920042547` (2024-09-20 09:51:30)
- `bootnode-20240920102804` (2024-09-20 10:51:31)
- `bootnode-20240920062016` (2024-09-20 11:20:50)
- `Foggie` (2024-09-20 11:20:52)
- `js-libp2p-bootstrapper` (2024-09-20 11:21:07)
- `bootnode-20240920072044` (2024-09-20 12:21:12)
- `bootnode-20240920122153` (2024-09-20 12:50:57)
- `kubo/0.31.0-dev/60588af/docker` (2024-09-20 14:51:05)
- `feishup2prelay` (2024-09-20 14:51:12)
- `bootnode-20240920145750` (2024-09-20 15:51:36)
- `kubo/0.31.0-dev/b71cf0d15-dirty` (2024-09-20 16:50:44)
- `bootnode-20240920184238` (2024-09-20 16:50:50)
- `bootnode-20240920115419` (2024-09-20 18:51:09)
- `bootnode-20240920201007` (2024-09-20 20:20:50)
- `bootnode-20240920194712` (2024-09-21 01:20:51)
- `bootnode-20240921015048` (2024-09-21 01:51:02)
- `kubo/0.31.0-dev/58434ecbd-dirty` (2024-09-21 02:51:13)
- `bootnode-20240920225007` (2024-09-21 03:51:07)
- `bootnode-20240920225332` (2024-09-21 04:20:56)
- `bootnode-20240921042415` (2024-09-21 05:20:54)
- `bootnode-20240921060435` (2024-09-21 05:50:56)
- `bootnode-20240921005552` (2024-09-21 06:51:02)
- `bootnode-20240921063813` (2024-09-21 06:51:11)
- `bootnode-20240921100629` (2024-09-21 08:51:25)
- `bootnode-20240921020607` (2024-09-21 09:21:04)
- `bootnode-20240921102037` (2024-09-21 10:20:59)
- `bootnode-20240921071827` (2024-09-21 12:20:51)
- `bootnode-20240921121554` (2024-09-21 14:21:16)
- `bootnode-20240921091956` (2024-09-21 14:21:35)
- `bootnode-20240921141703` (2024-09-21 15:21:13)
- `bootnode-20240921145611` (2024-09-21 15:51:34)
- `bootnode-20240921133637` (2024-09-21 16:21:11)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v20.11.1` (2024-09-21 16:21:45)
- `bootnode-20240921120117` (2024-09-21 17:20:59)
- `bootnode-20240921164855` (2024-09-21 17:21:06)
- `bootnode-20240921175042` (2024-09-21 17:51:04)
- `bootnode-20240921183727` (2024-09-21 17:51:25)
- `bootnode-20240921203753` (2024-09-21 19:50:53)
- `bootnode-20240921215846` (2024-09-21 20:21:12)
- `bootnode-20240921152245` (2024-09-21 22:20:53)
- `bootnode-20240921173321` (2024-09-21 23:51:23)
- `bootnode-20240921200551` (2024-09-22 01:21:09)
- `bootnode-20240922012816` (2024-09-22 01:50:59)
- `bootnode-20240922013919` (2024-09-22 02:20:55)
- `bootnode-20240922033833` (2024-09-22 05:20:58)
- `bootnode-20240922004847` (2024-09-22 05:51:02)
- `bootnode-20240922014009` (2024-09-22 07:20:57)
- `bootnode-20240922070853` (2024-09-22 07:50:55)
- `bootnode-20240922025050` (2024-09-22 07:50:58)
- `bootnode-20240922082912` (2024-09-22 08:51:03)
- `rust-libp2p/owlnest/0.0.1` (2024-09-22 08:51:19)
- `kubo/0.31.0-dev/58434ecbd` (2024-09-22 10:20:54)
- `bootnode-20240922122026` (2024-09-22 12:20:56)
- `bootnode-20240922113017` (2024-09-22 13:20:58)
- `bootnode-20240922070215` (2024-09-22 13:21:01)
- `bootnode-20240922133643` (2024-09-22 13:51:03)
- `bootnode-20240922144211` (2024-09-22 13:51:14)
- `bootnode-20240922105049` (2024-09-22 15:51:04)
- `bootnode-20240922164808` (2024-09-22 16:50:56)
- `bootnode-20240922185225` (2024-09-22 17:51:10)
- `bootnode-20240922184358` (2024-09-22 18:50:50)
- `bootnode-20240922164212` (2024-09-22 18:51:18)
- `bootnode-20240922203938` (2024-09-22 20:51:05)
- `bootnode-20240922195405` (2024-09-22 22:50:55)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `ReachabilityProtocol.rpc_check` (2024-09-20 17:20:48)
- `/fsp2p/vpn/0.0.1` (2024-09-21 04:20:56)
- `/owlnest/blob/0.0.1` (2024-09-22 08:51:19)
- `/owlnest/advertise/0.0.1` (2024-09-22 08:51:19)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `51.159.150.159` | FR | 84 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 81 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.247.127` | FR | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 79 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 74 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `68.183.11.180` | NL | 53 | ['edgevpn']| True  |
| `178.128.39.79` | GB | 41 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| True  |

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

In the specified time interval from `2024-09-16` to `2024-09-23` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-09-16` to `2024-09-23` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-09-16` to `2024-09-23` in the DHT and their datacenter association.

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