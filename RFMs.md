# **RFMs: Requests for Measurements - Proposals &amp; Ideas**

This page lists measurements that are useful to understand the dynamics and the current state of the live IPFS network. RFMs are categorized in priority order (i.e., **Current Priority** and **Next Priority**), according to current needs and funding opportunities.

## Completed

**[RFM 2 | Uptime and churn P2P network nodes](#rfm-2--uptime-and-churn-of-ipfs-network-nodes)**

**[RFM 17 | Provider Record Liveness](#rfm-17--provider-record-liveness)**

**[RFM 19 | DHT Routing Table Health](#rfm-19--dht-routing-table-health)**

## Ongoing 

**[RFM 3 | Location of IPFS end users and requested content](#_rd50td3ym8dy)**

**[RFM 7 | Distribution of DHT lookup times and Breakdown of Content Routing Latency](#_mjvqjcvas5uh)**

**[RFM 15 | Decentralized NAT Hole-Punching Performance](#rfm-15--decentralized-nat-hole-punching-performance)**

**[RFM 16 | Effectiveness of Bitswap Discovery Process](#rfm-16--effectiveness-of-bitswap-discovery-process)**

## Current Priority - Batch 1

**[RFM 4 | IP address Churn (Roaming) & PeerID distribution for nodes in the IPFS Network](#_1mu1tfaw8au3)**

**[RFM 6 | Mapping the AS-level topology of P2P networks](#_1xjatm7vfujn)**

**[RFM 11 | Compare how distributed is IPFS compared to Web2](#_5jccmpwaow0)**

**[RFM 18 | TTFB through different architecture components](#rfm-18--ttfb-through-different-architecture-components)**

## Next Priority

**[RFM 1 | Lifetime of a document in the IPFS Network](#_o575jad7aotj)**

**[RFM 5 | IP Geolocation of P2P networks](#_fld2sr9emn3m)**

**[RFM 8 | Path length and Latency measurements](#_22mtgvvx3kv0)**

**[RFM 9 | Compare the lifetime of content in the Web 2.0 vs Web 3.0](#_shcpqw274ty2)**

**[RFM 10 | Compare the content delivery latency of content hosted in IPFS to Web2](#_nzea2tn76odd)**

**[RFM 12 | Bandwidth heat map](#_raqcome2o67l)**

**[RFM 13 | The Impact of Gateways to IPFS as a content delivery network](#_ksnbuwtki94z)**

**[RFM 14 | How efficient is caching in the IPFS network?](#_j426cm9u3j1h)**

**[RFM 20 | Data volume stored on IPFS and file size distribution](#data-volume)**

## Other

**[Tooling/Other notes](#tooling)**

---

<a id="_o575jad7aotj"></a>
## RFM 1 | Liveness of a document in the IPFS Network


* _Status:_ **draft**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_ NONE
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

We want to learn what is the liveness (or lifetime) of documents (webpages, images, videos, etc) in the Public IPFS Network in order to understand better the resilience of the P2P network. We want to understand better the different behaviours and patterns that emerge around popular and non-popular content, as well as whether the IPFS protocol settings serve well the purposes of content liveness.

Measuring this over time will also be a strong indication of Network growth and adoption.

#### Measurement Plan (DRAFT)

- Collect the list of CIDs being requested on the IPFS Gateways for a good list of IPFS files being requested in the network.
  - Collecting CIDs through Gateways is restricting the set of queries we see to those requested through browsers. An altrnative, or complementary approach would be to use bitswap, increase the connection limit set per node, so that progressively the node gets connected to as many other peers in the network as it can and capture all the queries that others make (given that Bitswap is flooding all peers in its swarm).

- Then, leverage the Hydra Booster nodes to track all the Provide Queries to check the presence of a document.
  - We keep track of the number of providers per item we are tracking. This will later give us interesting insights on the relation between `# of providers` <-> `liveness` period. For instance are there items that live on one provider only, but have a very long lifetime? How common is this?

- Attempt fetching the file regularly to confirm that it is still present in the network.
  - Instead of trying to actually fetch the file, which will add considerable traffic in the network depending on the number of CIDs we're doing this for, we could again leverage Bitswap to send WANT_HAVE messages. Assuming that nodes won't lie, we can count positive responses as "liveness" for that CID. In this way, we avoid extra traffic.
  - We will have to define: i) the frequency at which the test is run, and ii) the number of items we will query, iii) our assumptions for the intervals between queries, e.g., if we query an item once a month, it is likely that the item has disappeared for a brief period of time, even if both of our queries are successful.
  - A proposed algorithm to scale up the tests:
    - we start with a number of items which we query on an hourly basis for 24hrs,
    - those CIDs that the queries prove successful, we increase the probing time to once in 24hrs for one week and leave the rest in the previous category where they're probed hourly,
    - we continue by adavncing the probe to a weekly basis for those that have proved alive on every 24hr period for seven consequtive days,
    - in order to avoid overloading the probing nodes, we set a maximum number of queries each node can do and insert new CIDs into its set as previously probed items move to the "daily" and "weekly" probing periods.

Additionally, expand the set of files known by looking at the Provide Queries and resolving the queries to rebuild the graphs of files and directories.

#### Success Criteria

We have a dashboard that shows the lifetime of documents, differentiated by different file size and type.
- We will have to run the test periodically (e.g., daily) so that we get some statistical convergence. The resulting graph would have to display the number of items queried and be able to infer averages based on some percentile error rate.

##

## RFM 2 | Uptime and churn P2P network nodes

* _Status:_ **completed**
* _DRI/Team:_ [`@dennis-tra`](https://github.com/dennis-tra)
* _Effort Needed:_ **HIGH**
* _Prerequisite(s):_ NONE
* _Value:_ **HIGH**
* _Report:_ [`./results/rfm2-uptime-and-churn.md`](./results/rfm2-uptime-and-churn.md)

#### Proposal

This proposal seeks to identify the participation and contribution of DHT server peers in the Public IPFS Network.

We want to learn:

- Average session length
- Average uptime per day and month (and eventually per year)

#### Measurement Plan

Approach 1:

- Develop a crawler and monitoring tool that initially finds nodes in the network and then dials into them.
- The tool should continue dialling periodically into the nodes, so that we have a view of the session length.
- From the session length we should be able to calculate the interarrival time of peers, i.e., how soon after a peer leaves the network it comes back online.

Approach 2:

- Leverage the Hydra Booster nodes to track all the FindPeer Queries to check the presence of `multiaddr`.
- In addition to that we can borrow some of the methodology sketched above for the liveness of content (periodic pings) and adapt it to probe peerIDs instead.

#### Success Criteria

We have a dashboard or plots that are produced periodically (e.g., daily or weekly) and show the lifetime distribution of nodes.

##

<a id="_rd50td3ym8dy"></a>
## RFM 3 - Location of IPFS end users and requested content.

* _Status:_ **ready**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_ IP Geolocation, IP-to-ASN
* _Value:_ **MEDIUM**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

Based on data from public IPFS gateways, get the location of IPFS users and the requested content. This would allow us to measure the locality of CIDs in relation to the users that issue requests. Also it would allow us to understand at which locations are nodes actually involved in serving content.

#### Measurement Plan

For each request received by an IPFS gateway we will get the CID and the IP address of the requestor. We will then resolve the IP address to a location (city, country) and we will find the providers (peer IDs) that offer the requested CID at the time of the request. By also mapping the Peer IDs to a location we will be able to understand the locality of requests in IPFS.

#### Success Criteria

We have a heatmap-style plot that visualizes the volume of requests between different geographic locations. A visualization like a [Chord diagram](https://python-graph-gallery.com/chord-diagram/) or a heatmap can be used in addition to a map. The plot/dashboard should also ideally provide statistics on which ASNs and locations serve and consume most content.

##

<a id="_1mu1tfaw8au3"></a>
## RFM 4 | IP address Churn (Roaming) & PeerID distribution for nodes in the IPFS Network

* _Status:_ **ready**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

We want to learn about how stable are the IPFS nodes' location and how much peers generally move between IP addresses (e.g. Laptop moving from home to coffee shop to work). We also want to be able to identify peers that rotate their PeerIDs. PeerID rotation is critical for the performance of the DHT and if done too often leads to orphan content, i.e., content that exists in the network but its provider record cannot be found.

PeerID distribution is useful to identify whether malicious nodes generate PeerIDs and concentrate around a given part of the name space, e.g., to eclipse some particular content/CID.

For additional context check this [Notion page](https://pl-strflt.notion.site/Rotating-PeerIDs-22e9ebebae0440ef873dc5143943e762).

#### Measurement Plan

Approach 1:

- Take crawler data for a long period (e.g., one month or more)
    - Expected schema: `<peer_id, all IPs, ASN, location, crawl timestamp, crawl_id>`
    - Remove hydra nodes from data set
- Identify:
    - Changing IP addresses for constant PeerID:
    - Changing PeerID for a constant IP
    - Rotating both IP and PeerID:
- Find out whether nodes with Rotating PeerIDs end up storing provider records within the period that they appear with a given PeerID.
- How frequent is PeerID rotation and how many records remain orphan?
- Represent the hash space in a 0-1 line and depict the PeerIDs on this line to show the distribution of PeerIDs and whether there is unusual concentration of PeerIDs around a specific part of the hash space.

For additional context check this [Notion page](https://pl-strflt.notion.site/Rotating-PeerIDs-22e9ebebae0440ef873dc5143943e762).

Approach 2:

Using the Hydra Booster nodes, track PeerIds to `multiaddr`s and check how often these change by executing FindPeer queries regularly.

In order to avoid getting measurements for a huge number of peers, we can leverage results from the proposed algorithm in RFM-1 and RFM-2 and target only nodes that we have previously found to disconnect often and focus on those.

#### Success Criteria

We have detailed results, similar to: [[Week 42, 2021](https://github.com/dennis-tra/nebula-crawler-reports/blob/main/calendar-week-42/ipfs/README.md#top-10-rotating-hosts)], [[Week 43, 2021](https://github.com/dennis-tra/nebula-crawler-reports/blob/main/calendar-week-43/ipfs/README.md#top-10-rotating-hosts)], [[Week 44, 2021](https://github.com/dennis-tra/nebula-crawler-reports/blob/main/calendar-week-44/ipfs/README.md#top-10-rotating-hosts)] on what fraction of nodes rotate their PeerIDs, what fraction of PeerIDs do the rotating IDs account for and what is the impact on the DHT, i.e., the discovery process through other peers' routing tables.

We have a plot that shows the hash-space from 0 to 1 and the PeerIDs distributed acros the x-axis. We can see the distribution and identify whether there is concentration of PeerIDs across any part of the name space.

Additional ideas: we have a dashboard that shows the IP address churn of nodes:

- Churn dashboard: we can have a dashboard where the y-axis measures churn rate and the x-axis is increasing reliability. On the x-axis nodes are "listed" according to the churn rate we have measured.
- Roaming dashboard: we can have a dashboard where the y-axis shows change in location per 24hr period. The x-axis can again "list" nodes in increasing reliability in terms of location change.

##

<a id="_fld2sr9emn3m"></a>
## RFM 5 - IP Address Geolocation of peers in the IPFS Network

* _Status:_ **draft**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_ IPFS Network Crawler
* _Value:_ **MEDIUM**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

Map the IPs of IPFS nodes to city-level granularity. Knowing the geolocation of nodes is necessary for a lot of RFMs and follow-up analysis, as well as understanding the geographic penetration of the IPFS network.

#### Measurement Plan

Using a geolocation database, such as MaxMind, will be the first step. However, Maxmind alone can yield inaccurate results. We can augment the MaxMind data with RIPE's IPMap which combines an array of data sources, including ping measurements, rDNS resolution and crowdsourced information to confirm the location of an IP.

In contrast to RFM-3, in this RFM we will not only leverage requested content in order to find peer location, but we will also use IPFS network crawlers.

#### Success Criteria

We will have a dynamic database that will map IPs to geographic coordinates, and a real-time map of the location of the IPFS nodes.

##

<a id="_1xjatm7vfujn"></a>
## RFM 6 - Mapping the AS-level topology of the IPFS Network

* _Status:_ **ready**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_ IPFS Network Crawler
* _Value:_ **MEDIUM**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

Map the IPs of IPFS nodes to the corresponding AS Numbers (ASNs). Such a mapping will help us infer the network-level topology of the P2P nodes, which enables better-informed analysis of performance and resilience characteristics of the P2P network.

#### Measurement Plan

The IP addresses of the IPFS Network will be collected by a crawler. The collected IPs will be mapped to an AS using BGP data obtained from BGPStream (real-time stream of BGP paths from RouteViews and RIPE RIS) as well as WHOIS and RIR data to filter artifacts of BGP paths, or some similar alternative. We can also use some free services, such as the API by [Team Cymry](https://team-cymru.com/community-services/ip-asn-mapping/) that can be used to assist in this task.

#### Success Criteria

We have a dashboard or plot that shows the distribution of nodes to ASNs, and an API that would allow the querying of the IP-to-ASN mapping.

##

<a id="_mjvqjcvas5uh"></a>
## RFM 7 - Distribution of DHT lookup times and Breakdown of Content Routing Latency

* _Status:_ **ready**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

With this measurement we are looking to understand how the DHT performs in terms of lookup latencies, depending on several parameters, such as the specific file being searched (e.g., popular vs unpopular), the location of nodes in the network, the size of the file, the time required to perform a connection, and the load of the nodes. The result of this measurement should be a distribution of the time required to perform DHT lookups, as well as a breakdown of latencies in the different stages of the content routing process. Ideally, we should have the option (e.g., in a dashboard-style tool) to chose to see the distribution of DHT lookups of the last 7 days, which will output a histogram with the time invested to perform a lookup in the DHT by the different probes.

In order to achieve higher confidence in the results, we want to have nodes spun up in different locations across the planet, which publish content that is then retrieved from other locations.

We want to find out, among others:

- distribution of DHT lookup latencies over time (e.g., below 500ms, below 1s, below 2s, above 10s etc).
- correlation between slow lookups and geolocation or ASN. This will give us an insight on whether some part of the wider internet is slower, or if a particular node is either on a slow connection or overloaded.
- stability of measurements over time, i.e., is a node consistently being involved in slow lookups?

These results will give us a good sense of the state of the network at a specific epoch. We should think of this as a "snapshot" of the network at a particular point in time.

Additionally, we could show the distribution of lookups in a specific probe, i.e. in a specific section of the network, in order to have a sense of the DHT lookup times to be expected for someone in the probe's premises.

#### Measurement Plan

To achieve the end goal, a set of probes would need to be deployed in different locations. Each of these probes would perform random lookups in the DHT and track the time until it succeeds. In order to get accurate results, lookups should be performed from different vantage points in the network. For instance connect from a "us-central" probe to a peer whose geolocation is "eu-central" and compare the result against a lookup from the same probe ("us-central") to "us-west". Intuitively, the latter pair should have shorter lookup time, but due to the DHT structure this might not be the case.

Lookup requests should be performed with both newly-published content (CIDs), in order to get the worst-case performance (i.e., content not cached anywhere), but also, existing, ideally popular content that might be cached in the network.

In order to get a complete picture of the liffecycle of content in the IPFS network (i.e., from content publication to content retrieval), measurements should distinguish between GET and PUT operations. According to the implementation of the underlying DHT, doing a GET lookup (until the specific content is found) is likely to be faster than putting new content in the network (where we only need to find the nearest peer to the content).

An important parameter to test against is the duration of the requesting peers being live in the network. The uptime of peers is likely to affect their routing table, so that would be an important parameter to test against.

#### Success Criteria

We have a dashboard, or a range of plots that show different buckets with the number of requests for the different delays for a specific period of time. We should be able to answer questions such as: how does the geolocation of a peer correlate with the geolocation of the vantage point from where we initiate the lookup?

##

<a id="_22mtgvvx3kv0"></a>
## RFM 8 - Path length and Latency measurements

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_ IP Geolocation, IP-to-ASN
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

Develop a map of pairwise path lengths and latencies between different tuples of (ASN, city) points. Such measurements can potentially inform the design of DHT construction, the selection of content providers (when a CID is available from multiple providers), and the deployment of Hydra Booster nodes or relays.

#### Measurement Plan

We will collect ping and traceroute measurements from multiple distributed vantage points available through platforms such as SpeedChecker and RIPE Atlas. The measurements vantage points and destinations will be selected based on the locations of the nodes in the IPFS network so that we map only the relevant (ASN, city) tuples and not the entire Internet. The measurements will be repeated periodically (for instance daily) to maintain an updated dataset that will capture changes in the network layer.

#### Success Criteria

A real-time observatory of latencies and path lengths in the form of a dashboard.

##

<a id="_shcpqw274ty2"></a>
## RFM 9 - Compare the availability and lifetime of content in the Web 2.0 vs Web 3.0

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **LOW**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

We will find which content is common between Web2 and IPFS. Then we will compare a number of metrics, such as stability, performance, and popularity in IPFS against HTTP-based web. Note that in this RFM we're interested in the availability of content (available or not) instead of the stability of the nodes that host that content.

#### Measurement Plan (DRAFT)

Based on projects such as the HTTP Archive ([https://httparchive.org/reports/state-of-the-web](https://httparchive.org/reports/state-of-the-web)) or Common Crawl (https://commoncrawl.org), we will extract the files that are part of the most popular web pages (e.g. top 100K according to Alexa). We will map this content to CIDs and search IPFS for this content. This first measurement will allow us to map the availability of Web 2.0 content in IPFS, namely quantify the overlap. Then by parsing periodic snapshots of the above mentioned archives and Hydra Booster logs we will keep track of content availability over time.

#### Success Criteria

A dashboard that will provide statistics on content overlap and content availability.

##

<a id="_nzea2tn76odd"></a>
## RFM 10 - Compare the content delivery latency of content hosted in IPFS to Web2

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_ RFM 8
* _Value:_ **LOW**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

Measure and analyze the performance of retrieving content between IPFS and Web2 for overlapping content, e.g. time to first byte.

#### Measurement Plan

...

#### Success Criteria

...

##

<a id="_5jccmpwaow0"></a>
## RFM 11 | Compare how distributed is IPFS compared to Web2

* _Status:_ **ready**
* _Area/Project of Measurement:_ IPFS
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

While IPFS is in theory less centralized than Web2, it will be interesting to measure that decentralization in practice.

There are a lot of nodes deployed in cloud operators, adding an element of centralized operation in the system, which has not been quantified until now.

Excessive dependency on centralized cloud operators may have performance and resilience implications that are not apparent and which should be investigated further.

#### Measurement Plan

- Crawl and find all the DHT server (i.e., dialable) nodes.
- From the IP address of those nodes, identify whether they are hosted in one of the big cloud providers, which make their IP address ranges publicly available.
- We currently cannot do the same for DHT client peers, as these are not shown in the DHT. But it would be great to be able to do that too.
- Exclude the nodes that are hosted in cloud infrastructure (as these should be dialable from everywhere) and cross-check the rest of the DHT server nodes from several vantage points (to avoid the case were a peer is reachable from one peer, but not from some other). In fact, in order to be able to do this, it would be great if we could run the crawler from several DHT servers _not_ operating from within cloud infrastructure.

#### Success Criteria

- Percentage of nodes operating from within cloud infra as compared to "normal" peers.
- Stability of the above result: if we get snapshots of those measurements (or re-run the crawl several times), are results consistent, or do they fluctuate?

##

<a id="_raqcome2o67l"></a>
## RFM 12 | Bandwidth heat map

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **MEDIUM**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

Once we have mapped the topology of the network, it may be useful to map the links (or sections of the network) that have the capacity to exchange more traffic at a faster rate. Measuring this may not be trivial, but we can have a good sense of what is happening with a latency map.

#### Measurement Plan

...

#### Success Criteria

...

##

<a id="_ksnbuwtki94z"></a>
## RFM 13 - The Impact of Gateways to IPFS as a content delivery network

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

It would be great to have an idea of the percentage of content that is served through the IPFS Gateways, as compared to regular IPFS server nodes. If we find that the vast majority of content is served from gateways, we need to further investigate the reason why.

- Are gateways more trusted by users, i.e., are users explicitly requesting content through gateways?
- Are they constantly more dialable than other nodes and therefore requests end up being served by them?
- Do they have bigger cache than normal DHT server nodes?

What are the implications if gateways serve most of the content?
- Excessive reliance on IPFS gateways needs to be investigated further: are there any risks with that mode of operation? Could such a result mean that the network is more centralised than we previously thought?
- There is an increase in the bandwidth requirement for public gateways if they end up serving a big amount of traffic. It is worth noting that in many cases this will not be traffic pinned on the specific gateway.

As a further step it would be great to take measurements to see the delivery latency between serving content through the gateway and through normal DHT server nodes.

#### Measurement Plan (DRAFT)

- Gather a large number of CIDs, e.g., from Hydra nodes, or by sniffing bitswap WANT_LISTs.
- Disable the DHT and initiate Bitswap queries for the list of CIDs.
- Disable Bitswap and initiate DHT queries for the list of CIDs.
- Gather the Multiaddresses of nodes that respond positively (with a WANT_HAVE in case of Bitswap or with the content in case of DHT).
- Filter out the addresses that correspond to Public IFPS Gateways.

Note: we need to figure out what is the right CID population we need in order to arrive to statistically correct results.

#### Success Criteria

A plot to show the times content has been fetched from Gateways as compared to regular DHT server nodes for the two cases of Bitswap (with DHT disabled) and for DHT (for Bitswap disabled).

##

<a id="_j426cm9u3j1h"></a>
## RFM 14 | How efficient is caching in the IPFS network?

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

It would be interesting to figure out what is the performance improvement that caching provides in the IPFS network. Given some distribution of a content item in the network and some request distribution, how efficient is the content resolution mechanism in resolving the closest copy? Is the network actually delivering the closest copy to the requestor? From what point onwards (in terms of the item distribution) is Bitswap becoming effective in discovering the content before the user needs to go through the DHT path?

NOTE: This is an important RFM, as it relates a lot to our projects Multi-Level DHTs (ML-DHTs). Depending on the outcome of this RFM, we will be able to quantify the value and the results that a ML-DHT approach will bring.

#### Measurement Plan (DRAFT)

- We have/control a number of clients located in different geographic locations (different countries and continents).
- We have/control a number of servers located in different geographic locations (different continents).
- We plant a copy of some content in some (or all) of the servers and make a request from a client (or another server) in the same continent.
- We repeat requests for the same content item progressively from different clients, but in a managed way, that is, not at once, but phased out. In the meantime we monitor the lookup latency of requests, both at the DHT level, but also (perhaps separately?) at the Bitswap level.

#### Success Criteria

- We have a plot that shows how the lookup time evolves (y-axis) as time goes by (x-axis), which also has to translate to more requests from clients entering the network.
- The above can be measured either in an aggregated manner (i.e., from all nodes), but also from the point of view of individual client nodes themselves. This last point would require that the client makes subsequent requests for the same item over time.


## RFM 15 | Decentralized NAT Hole-Punching Performance

* _Status:_ **ready to implement**
* _DRI/Team:_ @dennis-tra
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>
* _Material:_ https://github.com/dennis-tra/punchr

#### Proposal

NAT traversal is a quintessential problem in peer-to-peer networks.

We currently utilize relays, which allow us to traverse NATs by using a third party as proxy. Relays are a reliable fallback, that can connect peers behind NAT albeit with a high-latency, low-bandwidth connection. Unfortunately, they are expensive to scale and maintain if they have to carry all the NATed node traffic in the network.

It is often possible for two peers behind NAT to communicate directly by utilizing a technique called [hole punching](https://en.wikipedia.org/wiki/Hole_punching_(networking)). The technique relies on the two peers synchronizing and simultaneously opening connections to each other to their predicted external address. It works well for UDP, and reasonably well for TCP - at least, so we think.

In this RFM we try to find out the success rate and general performance of the new [Direct Connection Upgrade through Relay](https://github.com/libp2p/specs/blob/master/relay/DCUtR.md) (DCUtR) protocol.

#### Measurement Plan

Build a "**honeypot**" libp2p host to attract inbound connections from DCUtR capable peers behind NATs. These are then saved into a database which get served to hole punching **clients** via a **server** component. The hole punching clients ask the server if it knows about DCUtR capable peers. If it does the clients connect to the remote peer via a relay and waits for the remote to initiate a hole punch. The result is reported back to the server.

All three components need to be build.

#### Success Criteria

- We have a setup that allows continuous measurement of performance metrics. This includes but is not limited to:
  - success rate over time
  - success rate by transport used (TCP/QUIC)
  - success rate by type of router (could be inferred by the ISP which could be inferred by the IP address's Autonomous System)
  - time it takes for the hole protocol to terminate (success + error cases)
- The data should come from a large sample set. Hence, plenty (in the order of 10^1) of clients should be deployed and many (in the order of 10^3) peers should be hole punched continously

##

## RFM 16 | Effectiveness of Bitswap Discovery Process

* _Status:_ **ready**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>


#### Proposal

Bitswap is involved in the content discovery process and precedes the DHT walk. Nodes ask all of their connected peers for the CID they?re interested in, wait for 1sec to receive responses and in case of a negative result resort to the DHT.

**We argue that the 1sec delay is too long to wait for**, unless the chances of finding content are high. We suspect that unless content is popular, then the vast majority of Bitswap discovery attempts are unsuccessful and add a significant delay to the discovery process. Our latest results show that content discovery through the DHT (DHT walk) can be pretty fast - in many cases sub-second. Adding an extra 1sec increases the discovery time by at least 50% in all cases, reaching up to 100% in many cases.

Unless we find that the Bitswap content discovery success rate is worth the wait, we propose to get rid of this step, i.e., either disable the content discovery attempt through Bitswap, or initialise content discovery in parallel through the DHT and through Bitswap.

Additional context can be found in this [Notion doc](https://pl-strflt.notion.site/Effectiveness-of-Bitswap-Discovery-Process-aab515ebc1774bee8193da415bfb98f4).

#### Measurement Plan

- Sniff Bitswap requests from the network. The WIBerlin/TUDarmstadt team already has most of the CIDs requested in the past year.
- Spin up IPFS nodes in several areas around the globe and let them run for a long time to setup connections.
- Pick a large number of random CIDs (as many as needed in order to be able to arrive to a statistically safe conclusion) and share them with all the nodes involved in the experiment.
- Carry out Bitswap discovery for these CIDs.
    - Not all of the spun up peers should be requesting the same CIDs.
- CIDs should be requested at random time intervals after been seen (in wantlists received by other peers), not only (or not at all?) immediately after.
    - The experiment should be extended to request CIDs periodically after 1hr, 5hrs, 10hrs, etc.
- Observe success rate and the TTFB through the Bitswap discovery process.
- Disable the Bitswap discovery process, or set it to run in parallel to the DHT discovery (set `ProvSearchDelay` to 0 in the [bitswap_defaults](https://github.com/ipfs/go-bitswap/blob/dbfc6a1d986e18402d8301c7535a0c39b2461cb7/internal/defaults/defaults.go#L10)), request the same CIDs as before and observe success rate, as well as lookup latency and TTFB.

#### Success Criteria

We carry out a sensitivity analysis based on the success rate we have observed to assess whether the Bitswap discovery delay is worthy or not.


## RFM 17 | Provider Record Liveness

* _Status:_ **complete**
* _DRI/Team:_ [`@cortze`](https://github.com/cortze)
* _Effort Needed:_ 
* _Prerequisite(s):_ **NONE**
* _Value:_ **HIGH**
* _Report:_ [`rfm17-provider-record-liveness.md`](./results/rfm17-provider-record-liveness.md)


#### Proposal

Provider records are replicated in the system to `k=20` peers and are re-provided after 12hrs in the hope that, despite network churn, at least one of them will be alive to provide the record throughout the 12hr interval. However, we have not tested whether provider records indeed stay alive for 12hrs. In addition, we have found that the network has very high churn rate (at times in the order of 50% per hour).

Back of the envelope calculation suggests that with this rate of churn all 20 peers are likely to have gone offline after only 6hrs. In turn, this suggests that records might be unreachable for ~6hrs, which should be considered **unacceptable**. Of course, peers do not only leave, but also come back - our results suggest that the interarrival time is of similar levels as the churn rate - so it is likely that records become available again.

Despite the above argumentation, the network seems to work fine (although there have been reports of content being unreachable), so there are three things that might be happening:

- **Hydras help tremendously.** Hydras should not be seen as a component of the core architecture and more like a supporting component. So we should not assume full dependence on hydras and have the settings configured correctly.
- **Peers churn, but come back online very often.** Peers go offline very often, but come back online again too, so if interarrival time is small enough, this helps with keeping records alive.
- **Churn rate calculation is not accurate.** The actual churn rate is not as calculated and we?re missing something.

Additional context can be found [here](https://pl-strflt.notion.site/Provider-Record-Liveness-0b777eb2a3164c67974097eb97be23ad).

#### Measurement Plan

- Spin up a node that generates random CIDs (ideally CIDs that will eventually cover the majority of the hash space, but hopefully hash-function randomness will take care of that) and publishes provider records.
- Keep track of the peers that are chosen to provide the record.
- Keep dialling into all of these provider nodes (or requesting the provider record, or both) for the following 12hrs, until republish takes place. The frequency of dialling should be less than one hour.
- Keep track of when a provider node goes offline and then comes back online.
- Confirm whether or not there is at least one provider live at any given point during the 12hr period.
- Depending on the result, consider increasing or decreasing the replication factor `k=20` and repeat experiments to confirm.

#### Success Criteria

We have numbers to justify how often do provider records expire and have carried out experiments with alternative replication settings to justify new proposed settings.

## RFM 17.1 | Sharing Porvider Records with Multiaddress

* _Status:_ **complete**
* _DRI/Team:_ [`@cortze`](https://github.com/cortze)
* _Prerequisite(s):_ **NONE**
* _Value:_ **Medium**
* _Report:_ [`rfm17.1-.md`](./results/rfm17.1-.md)

#### Proposal
Achieving an appropriate content retrieval time for content in IPFS is key milestone to place Web3 as a real competition to centralized services. At the moment, in the process of retrieving content from the IPFS network, the user willing to retrieve some content first needs to find the content provider that hosts it. To do so with the `kubo` implementation, the interested client will try to retrieve the content itself using the Bitswap protocol to ask its immediate connected peers if they have the content of that CID. If this process fails, `kubo` falls back into the public DHT lookup process to find the Provider Records for the CID (the timeout for the Bitswap discovery is set to 1s). 

However, If this process of walking the DHT looking for the PR succeeds, the `kubo` client will get the link between the CID and the PeerID that host the content. Thus, the user still has to make a second DHT lookup to find the latest public multiaddress of that specific peer. 

Each of the public multiaddress for any peer in the network has assigned a Time To Live (TTL) duration, which can vary between `go-ipfs` or  `kubo` versions. It was originally set to 10 mins, but was incremented to 30 mins in the `go-libp2p@v0.22.0` update on August 18, 2022. In some occasions, if the user fetching the PRs inside the time window where the multiaddress of the provider didn't provide, the multiaddress of the provider will be share among the PRs so that the client can fetch directly the content from it.

This RFM, which is an extension of the RFM17 for its close relation to the PR retrievability aspect, aims to measure whether the shared PRs for a given CID actually contain the multiaddress of the provider and for how long are they actually shared. The final intention of the RFM is to discuss whether we can avoid this second DHT lookup by increasing the TTL of the multiaddress linked to the PR to 24h (same as the expiration of the PRs). 

#### Measurement Plan

- Spin up a node that generates random CIDs and publishes provider records.
- Periodically attempt to fetch the PR from the DHT, tracking whether they are retrievable and whether they are shared among the multiaddresses.

#### Success Criteria

- The measurements should show that the PRs are shared together with the PRs for the 10-30 mins after the publication of the CIDs (depending of the go-version the remote peers use)
- If so, we could consider increasing the expiration-time of the PeerID-Multiaddress records matching the PR expiration time. 


## RFM 18 | TTFB through different architecture components

* _Status:_ **ready**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>


#### Proposal

The IPFS architecture has grown to include several ways to retrieve content, sometimes referred to "content routing subsystems". These include the original go-ipfs approach, but also pinning services, which normally work through a public gateway. The addition of Hydra nodes, which help to keep content (i.e., provider records) alive, but also help with faster retrieval of those records, presents a separate boost to the architecture.

We have not yet studied the latency (particularly the Time To First Byte - TTFB) observed by clients using these different content retrieval methods in a systematic way.

#### Measurement Plan

We'd like to have a benchmark and comparison of the performance when retrieving content through the following Retrieval Methods (RMs):

- RM-1. Through go-ipfs.
- RM-2. Through go-ipfs, but without interacting with/using the Hydra boosters. Two ways to do that:
  - By ignoring responses from Hydras at request time.
  - By completing the experiment with all responses (including those from Hydras) and post-processing to filter out those that included responses from a Hydra peer.
- RM-3. Through a clustered node, when content is pinned/cached in a clustered node's storage. The experiment should repeat for:
  - content stored in the same clustered node's storage.
  - content stored in other clustered nodes.
- RM-4. Through a clustered node, when content is not pinned/cached.

Requirements to get valid results:
- All retrievals should be carried out (roughly) simultaneously to achieve similar network conditions across all retrievals.
- Retrievals should be carried out from several different geographic locations to observe differences in latency from several vantage points.
- The experiments should be carried out with a new CID for each experiment, in order to avoid content being cached in more peers and obtain baseline performance. For RM-3 content should be handled accordingly (i.e., cached) in order to achieve the RM's objective. Comparisons with existing, where possible popular CIDs will also be interesting to have.
- The experiments involving requests from go-ipfs clients should repeat for both newly spun-up client/requesting peers and long-running peers. This should be done to identify differences in the routing table entries of new vs old peers.
- If using cloud infrastructure to store and retrieve content, it would be good to experiment with diverse cloud infrastructures (i.e., not both client and provider in the same cloud provider's infra).
- For all retrievals we should be collecting results for the Time To First Byte (TTFB).

#### Sucess Criteria

- We have enough results, in the order of hundreds of retrievals for each Retrieval Method, to draw conclusive results on the latencies observed with each.
- The primary metric of interest is the Time To First Byte (TTFB).
- The experiments and scripts developed as part of this RFM should be easy to re-deploy and re-use.

Intuitively, we are expecting the following order in terms of latency: RM-3 < RM-1 < RM-2 < RM-4. Large differences, unusual spikes, or unexpected results should be investigated further to be able to explain these events.

## RFM 19 | DHT Routing Table Health

* _Status:_ **completed**
* _DRI/Team:_ @guillaumemichel
* _Effort Needed:_
* _Prerequisite(s):_ None
* _Value:_ **HIGH**
* _Report:_ 
[`rfm19-dht-routing-table-health.md`](./results/rfm19-dht-routing-table-health.md)
* _Material:_ [Implementation](./implementations/rfm19-dht-routing-table-health/), [Notion page](https://www.notion.so/pl-strflt/DHT-Routing-Table-Health-f8e6836c4b09440baa909a4448a88fbf)

#### Proposal

Distributed Hash Tables (DHTs) are a core component of decentralized peer-to-peer systems.
We want to measure the health of the [Kademlia](https://www.scs.stanford.edu/~dm/home/papers/kpos.pdf) routing table in the running IPFS network. The measurements will help us understand better the state of the routing table in practice and will provide hints on how to improve routing in libp2p/IPFS.

#### Measurement Plan

The [Nebula Crawler](https://github.com/dennis-tra/nebula-crawler) can be used to crawl the IPFS network to get information about all online peers and their routing table. Given a peer ID and the peers in its routing table, it is possible to reconstruct its k-buckets and to monitor them over time.

A [binary trie](https://github.com/guillaumemichel/py-binary-trie) implementation is necessary to compute XOR distances efficiently.

#### Sucess Criteria

- Get the routing table entries ditribution in the k-buckets
- Verify if each node has its 20 closest neighbors in its routing table
- Check if non-full k-buckets are missing any reachable peer
- Unresponsive nodes rate in the routing table

<a id="data-volume"></a>
## RFM 20 | Data volume stored on IPFS and file size distribution

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_
* _Prerequisite(s):_
* _Value:_ **MEDIUM**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

The idea is to get a view of the amount of data currently stored on IPFS as well as the file size distribution. Regular measurements can help us estimate whether IPFS use is increasing or decreasing and what type of files are stored (file size). This can help us detect what are the most common use cases for IPFS(music, movies, NFTs).

#### Measurement Plan

- Get the total number of records stored on hydra nodes
- Listen through Bitswap to CID requests.
- Fetch a large-enough number of those CIDs to have statistical significance over the entire number of provider records
- Fetch smaller number of CIDs and compare with a large number to determine the minimum number of CIDs that is still statistically robust
- From that data derive the distribution of content items published/stored on IPFS
- Apply that distribution to the number of records seen on hydra nodes and get a relatively good estimate of the volume ￼

#### Sucess Criteria

- Get a statistically robust view of the file size distribution over time
- Get a good estimate of the data volume stored on IPFS


<a id="tooling"></a>
## Tooling/Other notes

### Longitudinal repository of IPFS crawling snapshots

Currently we have no clear view of how the IPFS evolves over time.

It would be very useful to collect periodic (e.g. daily if possible) snapshots of the IPFS crawling results.

From each crawling we should store the following information at minimum for each node:

- IP address of node

- CIDs hosted in the node

- Peer table of the node

- Agent version

This measurement will probably require adequate storage space.

### Map the AS/city-level topology to RIPE Atlas

After collecting the AS-level and IP-level topology of p2p networks, we can map these topologies on top of [RIPE Atlas](https://atlas.ripe.net/).

Consequently, we can check if RIPE Atlas provides the necessary abstraction for measurements.

