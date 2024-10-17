# Nebula Measurement Results Calendar Week 40 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 40 - 2024](#nebula-measurement-results-calendar-week-40---2024)
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

The following results show measurement data that were collected in calendar week 40 in 2024 from `2024-09-30` to `2024-10-07`.

- Number of crawls `336`
- Number of visits `23,492,811`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `45,888`
- Number of unique peer IDs discovered in the DHT `44,456`
- Number of unique IP addresses found `43,868`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `bootnode-20240930003643` (2024-09-30 00:50:58)
- `bootnode-20240930013642` (2024-09-30 01:51:07)
- `bootnode-20240930021111` (2024-09-30 02:21:01)
- `bootnode-20240929231109` (2024-09-30 04:20:53)
- `bootnode-20240930034130` (2024-09-30 04:20:54)
- `kubo/0.30.0/cdf59db-dirty` (2024-09-30 04:21:07)
- `bootnode-20240930051531` (2024-09-30 05:51:27)
- `bootnode-20240930005623` (2024-09-30 06:20:57)
- `bootnode-20240930061650` (2024-09-30 07:21:26)
- `bootnode-20240930112439` (2024-09-30 09:51:06)
- `bootnode-20240930095914` (2024-09-30 11:20:51)
- `bootnode-20240930124524` (2024-09-30 11:21:15)
- `bootnode-20240930111809` (2024-09-30 11:51:09)
- `helia/4.2.6 libp2p/1.9.4 UserAgent=v20.12.2` (2024-09-30 12:50:51)
- `bootnode-20240930084856` (2024-09-30 13:51:26)
- `bootnode-20240930144927` (2024-09-30 14:51:33)
- `bootnode-20240930111357` (2024-09-30 16:21:24)
- `bootnode-20240930180703` (2024-09-30 18:20:50)
- `bootnode-20240930171932` (2024-09-30 18:21:24)
- `bootnode-20240930121943` (2024-09-30 18:51:02)
- `bootnode-20240930214732` (2024-09-30 19:51:06)
- `bootnode-20240930222100` (2024-09-30 22:21:07)
- `bootnode-20241001021748` (2024-10-01 00:21:24)
- `bootnode-20240930211031` (2024-10-01 02:21:05)
- `bootnode-20240930225056` (2024-10-01 03:51:12)
- `bootnode-20240930235017` (2024-10-01 04:50:57)
- `bootnode-20241001065828` (2024-10-01 05:50:51)
- `bootnode-20241001014948` (2024-10-01 06:50:47)
- `bootnode-20241001072405` (2024-10-01 08:21:20)
- `bootnode-20241001075552` (2024-10-01 08:51:09)
- `bootnode-20241001094110` (2024-10-01 09:50:57)
- `bootnode-20241001094712` (2024-10-01 09:51:09)
- `bootnode-20241001135908` (2024-10-01 14:51:38)
- `bootnode-20241001110834` (2024-10-01 16:20:57)
- `bootnode-20241001110959` (2024-10-01 16:21:06)
- `bootnode-20241001115111` (2024-10-01 16:51:26)
- `bootnode-20241001181453` (2024-10-01 19:21:14)
- `bootnode-20241001182447` (2024-10-01 19:21:26)
- `bootnode-20241001221958` (2024-10-01 20:21:03)
- `bootnode-20241001142310` (2024-10-01 21:20:51)
- `bootnode-20241001215034` (2024-10-01 21:50:54)
- `bootnode-20241001214026` (2024-10-01 21:51:00)
- `bootnode-20241002005048` (2024-10-01 22:51:26)
- `bootnode-20241001185653` (2024-10-02 00:21:13)
- `bootnode-20241002023112` (2024-10-02 01:21:12)
- `bootnode-20241001181227` (2024-10-02 02:20:57)
- `bootnode-20241002001720` (2024-10-02 02:51:20)
- `bootnode-20241002033535` (2024-10-02 03:50:55)
- `bootnode-20241002010613` (2024-10-02 06:21:01)
- `bootnode-20241002073138` (2024-10-02 07:20:58)
- `bootnode-20241002024702` (2024-10-02 08:20:59)
- `bootnode-20241002055004` (2024-10-02 10:50:59)
- `bootnode-20241002115425` (2024-10-02 12:21:07)
- `bootnode-20241002124033` (2024-10-02 13:21:31)
- `bootnode-20241002133848` (2024-10-02 13:51:10)
- `bootnode-20241002135636` (2024-10-02 14:21:03)
- `bootnode-20241002094744` (2024-10-02 14:51:08)
- `bootnode-20241002152054` (2024-10-02 15:21:10)
- `bootnode-20241002172122` (2024-10-02 17:21:29)
- `bootnode-20241002200000` (2024-10-02 20:21:01)
- `bootnode-20241002205042` (2024-10-02 20:50:54)
- `bootnode-20241002194300` (2024-10-02 20:51:24)
- `kubo/0.30.0/debox/0.1.0` (2024-10-02 22:20:58)
- `bootnode-20241002181024` (2024-10-02 23:50:56)
- `bootnode-20241003011627` (2024-10-03 00:20:59)
- `bootnode-20241002193131` (2024-10-03 01:21:02)
- `bootnode-20241003004147` (2024-10-03 01:21:06)
- `bootnode-20241003014011` (2024-10-03 01:51:00)
- `bootnode-20241003022054` (2024-10-03 02:21:18)
- `bootnode-20241003012246` (2024-10-03 06:51:07)
- `bootnode-20241003035038` (2024-10-03 08:51:15)
- `kodentsov.ru/studio@` (2024-10-03 10:20:48)
- `bootnode-20241003052150` (2024-10-03 10:51:11)
- `bootnode-20241003060228` (2024-10-03 11:21:10)
- `bootnode-20241003115039` (2024-10-03 11:50:57)
- `bootnode-20241003135027` (2024-10-03 13:51:01)
- `fsp2p@6773182c9` (2024-10-03 14:51:16)
- `bootnode-20241003143314` (2024-10-03 15:20:59)
- `bootnode-20241003185943` (2024-10-03 17:21:09)
- `bootnode-20241003130644` (2024-10-03 18:51:14)
- `bootnode-20241003141743` (2024-10-03 19:21:17)
- `bootnode-20241003144753` (2024-10-03 19:51:09)
- `kubo/0.31.0-dev/e1955a8/docker` (2024-10-03 20:51:00)
- `kubo/0.31.0-dev/52b0062/docker` (2024-10-03 21:51:15)
- `bootnode-20241003204310` (2024-10-03 21:51:18)
- `bootnode-20241003172011` (2024-10-03 22:21:00)
- `kubo/0.31.0-dev/52ca370/docker` (2024-10-03 23:51:01)
- `bootnode-20241003200402` (2024-10-04 01:51:00)
- `github.com/ipfs/go-ds-crdt/examples/globaldb@431e8f368` (2024-10-04 03:20:59)
- `bootnode-20241003222024` (2024-10-04 03:21:04)
- `bootnode-20241004023752` (2024-10-04 03:21:04)
- `bootnode-20241004032800` (2024-10-04 03:50:55)
- `bootnode-20241003225110` (2024-10-04 03:51:18)
- `kubo/0.31.0-rc1/a55215c/1234567890123456789012345678901234567890` (2024-10-04 04:21:17)
- `bootnode-20241004051006` (2024-10-04 05:51:17)
- `bootnode-20241004025004` (2024-10-04 07:51:03)
- `kubo/0.31.0-dev/a17830754-dirty/desktop` (2024-10-04 08:21:22)
- `bootnode-20241004092018` (2024-10-04 09:21:22)
- `bootnode-20241004095052` (2024-10-04 09:51:13)
- `bootnode-20241004111636` (2024-10-04 10:20:57)
- `bootnode-20241004110928` (2024-10-04 11:21:32)
- `github.com/harmony-one/harmony@1588c05bf` (2024-10-04 12:50:56)
- `bootnode-20241004071727` (2024-10-04 12:50:58)
- `kubo/0.32.0-dev/6e5df580a` (2024-10-04 13:51:03)
- `kubo/0.28.0-dev/19d49271c` (2024-10-04 13:51:18)
- `kubo/0.31.0-rc1/` (2024-10-04 14:20:49)
- `bootnode-20241004090017` (2024-10-04 14:20:59)
- `kubo/0.32.0-dev/00e1f81/docker` (2024-10-04 14:50:58)
- `bootnode-20241004095103` (2024-10-04 14:51:29)
- `bootnode-20241004155728` (2024-10-04 15:20:47)
- `bootnode-20241004102759` (2024-10-04 15:51:00)
- `bootnode-20241004113904` (2024-10-04 16:50:50)
- `bootnode-20241004173755` (2024-10-04 16:51:11)
- `bootnode-20241004203800` (2024-10-04 20:51:27)
- `bootnode-20241004150908` (2024-10-04 21:21:15)
- `bootnode-20241004165034` (2024-10-04 21:51:05)
- `bootnode-20241004222906` (2024-10-04 22:20:58)
- `bootnode-20241004180107` (2024-10-04 23:21:01)
- `bootnode-20241005012005` (2024-10-05 00:51:07)
- `bootnode-20241004205040` (2024-10-05 01:51:26)
- `bootnode-20241005020526` (2024-10-05 03:21:25)
- `bootnode-20241005055027` (2024-10-05 03:51:07)
- `bootnode-20241005044757` (2024-10-05 04:50:54)
- `bootnode-20241005052231` (2024-10-05 05:52:19)
- `bootnode-20241005032838` (2024-10-05 06:20:56)
- `bootnode-20241005012028` (2024-10-05 06:21:11)
- `bootnode-20241005040256` (2024-10-05 06:51:15)
- `bootnode-20241005081123` (2024-10-05 07:21:08)
- `bootnode-20241005020126` (2024-10-05 07:21:28)
- `bootnode-20241005035526` (2024-10-05 09:21:12)
- `bootnode-20241005082024` (2024-10-05 13:20:57)
- `bootnode-20241005082124` (2024-10-05 13:50:56)
- `bootnode-20241005163241` (2024-10-05 17:21:04)
- `bootnode-20241005172301` (2024-10-05 18:50:54)
- `bootnode-20241005145039` (2024-10-05 19:51:15)
- `github.com/libp2p/go-libp2p/examples@299f96444-dirty` (2024-10-05 20:21:01)
- `bootnode-20241005195439` (2024-10-05 20:21:08)
- `bootnode-20241005202026` (2024-10-05 20:21:12)
- `bootnode-20241005214336` (2024-10-05 20:51:03)
- `bootnode-20241005155042` (2024-10-05 20:51:23)
- `bootnode-20241005204800` (2024-10-05 21:20:57)
- `bootnode-20241005220518` (2024-10-05 22:50:55)
- `bootnode-20241006013727` (2024-10-06 01:51:04)
- `bootnode-20241006025044` (2024-10-06 02:50:59)
- `bootnode-20241006035053` (2024-10-06 03:50:59)
- `bootnode-20241005222806` (2024-10-06 03:51:08)
- `bootnode-20241006055234` (2024-10-06 06:21:31)
- `bootnode-20241006065044` (2024-10-06 06:50:52)
- `bootnode-20241006072306` (2024-10-06 07:51:00)
- `bootnode-20241006085028` (2024-10-06 08:50:54)
- `bootnode-20241006082751` (2024-10-06 09:51:15)
- `bootnode-20241006040713` (2024-10-06 09:51:33)
- `bootnode-20241006094332` (2024-10-06 10:21:05)
- `bootnode-20241006122735` (2024-10-06 10:51:06)
- `bootnode-20241006123651` (2024-10-06 12:51:30)
- `bootnode-20241006160858` (2024-10-06 18:20:50)
- `bootnode-20241006184040` (2024-10-06 18:51:20)
- `bootnode-20241006202924` (2024-10-06 19:21:27)
- `bootnode-20241006140323` (2024-10-06 19:51:04)
- `bootnode-20241006190253` (2024-10-06 19:51:22)
- `bootnode-20241006225427` (2024-10-06 23:50:56)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/hypermedia/0.4.1-dev` (2024-09-30 17:51:48)
- `/studio/1.0.0` (2024-10-03 10:20:48)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `51.159.150.159` | FR | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.233.167` | FR | 78 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 78 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.240.182` | FR | 78 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.247.127` | FR | 78 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 73 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | NL | 71 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.64.186` | FR | 71 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `68.183.11.180` | NL | 50 | ['edgevpn']| True  |
| `143.110.168.61` | GB | 46 | ['kubo/0.22.0/3f884d3/gala.games', 'kubo/0.29.0/3f0947b']| True  |

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

In the specified time interval from `2024-09-30` to `2024-10-07` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-09-30` to `2024-10-07` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-09-30` to `2024-10-07` in the DHT and their datacenter association.

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