# Nebula Measurement Results Calendar Week 35 - 2024

## Table of Contents

- [Nebula Measurement Results Calendar Week 35 - 2024](#nebula-measurement-results-calendar-week-35---2024)
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

The following results show measurement data that were collected in calendar week 35 in 2024 from `2024-08-26` to `2024-09-02`.

- Number of crawls `336`
- Number of visits `24,284,630`
  > Visiting a peer means dialing or connecting to it. Every time the crawler or monitoring process tries to dial or connect to a peer we consider this as _visiting_ it. Regardless of errors that may occur.
- Number of unique peer IDs visited `66,215`
- Number of unique peer IDs discovered in the DHT `65,908`
- Number of unique IP addresses found `121,053`

Timestamps are in UTC if not mentioned otherwise.

### Agent Versions

Newly discovered agent versions:

- `helia/4.2.5 libp2p/1.9.2 UserAgent=v20.14.0` (2024-08-26 03:51:03)
- `libp2p/1.3.3 UserAgent=v22.7.0` (2024-08-26 12:21:12)
- `kubo/0.31.0-dev/91144f7/docker` (2024-08-26 19:20:52)
- `js-libp2p/0.45.9 UserAgent=v21.6.1` (2024-08-26 23:21:42)
- `kubo/0.29.0/3f0947b-dirty` (2024-08-27 01:51:17)
- `go-ipfs/0.11.0-dev/c00065cc8` (2024-08-27 03:21:57)
- `github.com/harmony-one/harmony@c44c2ea8c-dirty` (2024-08-27 11:20:58)
- `bootnode-20240827132728` (2024-08-27 13:21:18)
- `kubo/0.31.0-dev/91144f7bf` (2024-08-27 14:21:09)
- `github.com/INFURA/ipfs-p2p-server@6fd7ae700` (2024-08-27 18:21:45)
- `bootnode-20240827213825` (2024-08-27 20:51:34)
- `kubo/0.31.0-dev/add45cf/docker` (2024-08-28 01:20:58)
- `github.com/INFURA/ipfs-p2p-server@a7e6b662f` (2024-08-28 13:21:45)
- `bootnode-20240828170037` (2024-08-28 15:21:03)
- `github.com/INFURA/ipfs-p2p-server@b5aecec2e` (2024-08-28 15:21:40)
- `github.com/INFURA/ipfs-p2p-server@900505000` (2024-08-28 15:51:57)
- `kubo/0.31.0-dev/add45cf/1234567890123456789012345678901234567890` (2024-08-28 16:21:40)
- `kubo/0.31.0-dev/2260e35/docker` (2024-08-28 17:20:59)
- `kubo/0.31.0-dev/175aabd/docker` (2024-08-28 17:21:28)
- `kubo/0.30.0-rc2/467fc69/1234567890123456789012345678901234567890` (2024-08-28 18:51:20)
- `kubo/0.30.0-rc2/` (2024-08-28 19:21:50)
- `kubo/0.31.0-dev/5fe9604/docker` (2024-08-28 19:50:55)
- `kubo/0.30.0-rc2/467fc69/docker` (2024-08-28 20:21:08)
- `bootnode-20240829093724` (2024-08-29 09:51:20)
- `bootnode-20240829133148` (2024-08-29 11:50:56)
- `helia/4.0.1 libp2p/1.2.1 UserAgent=v20.16.0` (2024-08-29 14:20:55)
- `bootnode-20240829194244` (2024-08-29 17:50:54)
- `bootnode-20240830004817` (2024-08-30 00:51:27)
- `bootnode-20240830010711` (2024-08-30 01:51:20)
- `bootnode-20240830034849` (2024-08-30 04:21:22)
- `bootnode-20240830045046` (2024-08-30 04:50:56)
- `helia/2.1.0 js-libp2p/0.46.21 UserAgent=v21.7.2` (2024-08-30 05:21:01)
- `bootnode-20240830052117` (2024-08-30 05:21:27)
- `bootnode-20240830061016` (2024-08-30 06:50:55)
- `bootnode-20240830070031` (2024-08-30 07:21:25)
- `bootnode-20240830075056` (2024-08-30 07:51:22)
- `bootnode-20240830094424` (2024-08-30 08:21:02)
- `kubo/0.30.0-rc2/collab.ipfscluster.io` (2024-08-30 14:20:45)
- `helia/4.2.5 libp2p/1.9.3 UserAgent=v22.7.0` (2024-08-30 15:51:10)
- `bootnode-20240830162348` (2024-08-30 16:51:41)
- `helia/4.2.5 libp2p/1.9.3 UserAgent=v20.15.0` (2024-08-30 18:51:58)
- `bootnode-20240830195112` (2024-08-30 19:51:32)
- `bootnode-20240830191535` (2024-08-30 19:51:34)
- `bootnode-20240830220721` (2024-08-30 20:21:11)
- `bootnode-20240831010740` (2024-08-31 00:21:29)
- `bootnode-20240831030233` (2024-08-31 04:21:26)
- `bootnode-20240831080910` (2024-08-31 06:21:11)
- `bootnode-20240831101929` (2024-08-31 08:51:19)
- `bootnode-20240831085514` (2024-08-31 09:20:51)
- `bootnode-20240831114432` (2024-08-31 12:21:18)
- `bootnode-20240831151844` (2024-08-31 15:21:15)
- `bootnode-20240831155901` (2024-08-31 16:20:50)
- `bootnode-20240831184917` (2024-08-31 18:51:51)
- `bootnode-20240901001035` (2024-08-31 22:50:57)
- `bootnode-20240901024145` (2024-09-01 01:21:21)
- `bootnode-20240901011700` (2024-09-01 02:50:53)
- `bootnode-20240901053206` (2024-09-01 04:50:59)
- `bootnode-20240901074106` (2024-09-01 08:21:15)
- `bootnode-20240901114347` (2024-09-01 09:50:57)
- `js-libp2p/0.45.9 UserAgent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36` (2024-09-01 16:21:22)
- `helia/4.2.5 libp2p/1.9.3 UserAgent=v20.14.0` (2024-09-01 16:50:52)

Agent versions that were found to support at least one [storm specific protocol](#storm-specific-protocols):

- `go-ipfs/0.8.0/48f94e2`
- `storm`

### Protocols

Newly discovered protocols:


- `/mobazha/store-and-forward/server/0.1.0` (2024-08-26 07:50:47)
- `/mobazha/app/3.0.0` (2024-08-26 07:50:47)
- `/mobazha/store-and-forward/client/0.1.0` (2024-08-26 07:50:48)

### Top 10 Rotating Nodes

A "rotating node" is a node (as identified by its IP address) that was found to host multiple peer IDs.

| IP-Address    | Country | Unique Peer IDs | Agent Versions | Datacenter IP |
|:------------- |:------- | ---------------:|:-------------- | ------------- |
| `51.159.150.159` | FR | 83 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.158.232.73` | FR | 80 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.247.127` | FR | 77 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.90.150` | FR | 77 | ['kubo/0.18.1/8c234d9fd-dirty', 'kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.210.254` | FR | 75 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.15.86.171` | FR | 72 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `51.159.174.206` | FR | 64 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |
| `68.183.11.180` | NL | 52 | ['edgevpn']| True  |
| `152.81.47.227` | FR | 42 | ['kubo/0.28.0/']| False  |
| `51.15.133.64` | IN | 40 | ['kubo/0.22.0-dev/c95f9e1-dirty']| True  |

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

In the specified time interval from `2024-08-26` to `2024-09-02` we visited `` unique peer IDs.
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

This graph shows all IP addresses that we found from `2024-08-26` to `2024-09-02` in the DHT and their geolocation distribution by country.

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

This graph shows all IP addresses that we found from `2024-08-26` to `2024-09-02` in the DHT and their datacenter association.

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