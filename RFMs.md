# **RFMs - Proposals &amp; Ideas**

This page lists measurements that can potentially bit useful in developing the P2P observatory

**[RFM 1 | Lifetime of a document in the IPFS Network](#_o575jad7aotj)**

**[RFM 2 | Uptime  and churn P2P network nodes](#_3k3jj6wgwrra)**

**[RFM 3 | Location of IPFS end users and requested content](#_rd50td3ym8dy)**

**[RFM 4 | IP Churn (Roaming) for nodes in the IPFS Network](#_1mu1tfaw8au3)**

**[RFM 5 | IP Geolocation of P2P networks](#_fld2sr9emn3m)**

**[RFM 6 | Mapping the AS-level topology of P2P networks](#_1xjatm7vfujn)**

**[RFM 7 | Distribution of DHT lookups time](#_mjvqjcvas5uh)**

**[RFM 8 | Path length and Latency measurements](#_22mtgvvx3kv0)**

**[RFM 9 | Compare the lifetime of content in the Web 2.0 vs Web 3.0](#_shcpqw274ty2)**

**[RFM 10 | Compare the content delivery latency of content hosted in IPFS to Web2](#_nzea2tn76odd)**

**[RFM 11 | Compare how distributed is IPFS compared to Web2](#_5jccmpwaow0)**

**[RFM 12 | Bandwidth heat map](#_raqcome2o67l)**

**[RFM 13 | The Impact of Gateways to IPFS as a content delivery network](#_ksnbuwtki94z)**

**[RFM 14 | How efficient is caching in the IPFS network?](#_j426cm9u3j1h)**

**[Tooling/Other notes](#tooling)**


#### List of RFM statuses

:thinking: **brainstorm**  
:memo: **draft**  
:monocle_face:	**ready for review**  
:ok_hand: **ready to implement**  

#### List of RFM priorities

:red_medium_square::white_medium_square::white_medium_square: **LOW**  
:red_medium_square::red_medium_square::white_medium_square: **MEDIUM**  
:red_medium_square::red_medium_square::red_medium_square: **HIGH**

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

<a id="_3k3jj6wgwrra"></a>
## RFM 2 | Uptime and churn of IPFS network nodes

* _Status:_ **draft**
* _DRI/Team:_
* _Effort Needed:_ 
* _Prerequisite(s):_ NONE
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

This proposal seeks to identify the participation and contribution of peers in Public IPFS Network.

We want to learn:

- Average session length
- Average uptime per year, month and day
- Ideally differentiate between DHT client and DHT server nodes

#### Measurement Plan (DRAFT)

- Leverage the Hydra Booster nodes to track all the FindPeer Queries to check the presence of `multiaddr`.
- In addition to that we can borrow some of the methodology sketched above for the liveness of content (periodic pings) and adapt it to probe peerIDs instead.

#### Success Criteria

We have a dashboard or plots that show the lifetime distribution of nodes. As a final target we will want to have a map of nodes with "server" vs "client" profile. A server profile would have stable connectivity and high upstream bandwidth. With this RFM we should cover the connectivity aspect.

## 

<a id="_rd50td3ym8dy"></a>
## RFM 3 - Location of IPFS end users and requested content.

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_ 
* _Prerequisite(s):_ IP Geolocation, IP-to-ASN
* _Value:_ **MEDIUM**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

Based on data from public IPFS gateways, get the location of IPFS users and the requested content. This would allow us to measure the locality of CIDs in relation to the users that issue requests. Also it would allow us to understand which nodes are actually involved in serving content.

#### Measurement Plan (DRAFT)

For each request received by an IPFS gateway we will get the CID and the IP address of the requestor. We will then resolve the IP address to a location (city, country) and we will find the providers (peer IDs) that offer the requested CID at the time of the request based on data collected from HydraBooster nodes. By also mapping the Peer IDs to a location we will be able to understand the locality of requests in IPFS.

#### Success Criteria

We have a dashboard that visualizes the volume of requests between different relationships. A visualization like a [Chord diagram](https://python-graph-gallery.com/chord-diagram/) can be used in addition to a map. The dashboard will also provide statistics on which ASNs and locations serve and consume most content.

##

<a id="_1mu1tfaw8au3"></a>
## RFM 4 | IP address Churn (Roaming) for nodes in the IPFS Network

* _Status:_ **draft**
* _DRI/Team:_
* _Effort Needed:_ 
* _Prerequisite(s):_ 
* _Value:_ **LOW**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

We want to learn about how stable are the IPFS nodes' location and how much peers generally move between IP addresses (e.g. Laptop moving from home to coffee shop to work).

#### Measurement Plan (DRAFT)

Using the Hydra Booster nodes, track PeerIds to `multiaddr`s and check how often these change by executing FindPeer queries regularly.

- In order to avoid getting measurements for a huge number of peers, we can leverage results from the proposed algorithm in RFM-1 and RFM-2 and target only nodes that we have previously found to disconnect often and focus on those.

#### Success Criteria

We have a dashboard that shows the IP address churn of nodes. Ideas for dashboard:

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

* _Status:_ **draft**
* _DRI/Team:_
* _Effort Needed:_ 
* _Prerequisite(s):_ IPFS Network Crawler
* _Value:_ **MEDIUM**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

Map the IPs of IPFS nodes to the corresponding AS Numbers (ASNs). Such a mapping will help us infer the network-level topology of the P2P nodes, which enables better-informed analysis of performance and resilience characteristics of the P2P network.

#### Measurement Plan (DRAFT)

The IP addresses of the IPFS Network will be collected by a crawler. The collected IPs will be mapped to an AS using BGP data obtained from BGPStream (real-time stream of BGP paths from RouteViews and RIPE RIS) as well as WHOIS and RIR data to filter artifacts of BGP paths. We can also use some free services, such as the API by [Team Cymry](https://team-cymru.com/community-services/ip-asn-mapping/) that can be used to assist in this task.

#### Success Criteria

We have a dashboard or plot that shows the distribution of nodes to ASNs, and an API that would allow the querying of the IP-to-ASN mapping.

##

<a id="_mjvqjcvas5uh"></a>
## RFM 7 - Distribution of DHT lookup times

* _Status:_ **brainstorm**
* _DRI/Team:_
* _Effort Needed:_ 
* _Prerequisite(s):_ 
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

With this measurement we look to understand how DHT lookups behave throughout time according to the specific file being searched, the status of the network, the location of nodes in the network, the time required to perform a connection, or load of the nodes. The result of this measurement should be a distribution of the time required to perform DHT lookups. For instance, if we chose to see the distribution of DHT lookups of the last 7 days we will output a histogram with the time invested to perform a lookup in the DHT by the different probes.

We want to find out, among others:

- % of requests below 500 ms
- % of requests between 500ms and 1 s.
- correlation between slow lookups and geolocation or ASN. This will give us an insight on whether some part of the wider internet is slower, or if a particular node is either on a slow connection or overloaded.
- stability of measurements over time, i.e., is a node consistently being involved in slow lookups?

This gives a good sense of the state of the network at a specific epoch. We should think of this as a "snapshot" of the network at a particular point in time.

Additionally, we could show the distribution of lookups in a specific probe, i.e. in a specific section of the network, in order to have a sense of the DHT lookup times to be expected for someone in the probe's premises.

#### Measurement Plan (DRAFT)

To measure this, a set of probes would be deployed in different locations. Each of these probes would perform random lookups in the DHT and track the time until it succeeds. It would also be interesting to try and (artificially) connect (i.e., do a lookup) to the same node from different vantage points in the network. For instance connect from a "us-central" probe to a peer whose geolocation is "eu-central" as compared to "eu-west" probe to to the same peer in "eu-central" geolocation. Intuitively, the latter pair should have shorter lookup time, but due to the DHT structure this might not be the case.

To increase the accuracy and granularity of the measurement, we could distinguish between GET and PUT operations. According to the implementation of the underlying DHT in the network doing a GET lookup (until the specific content is found) may be faster than putting new content in the network (where we always try to find the nearest peer to the content possible).

An extension to this RFM is to accompany lookups and the PUT/GET operation mentioned above with a file of specific size. This will further allow us to build "server vs client" profiles for peers, as discussed in RFM-2.

#### Success Criteria

We have a dashboard that shows different buckets with the number of requests for the different delays for a specific period of time. We can also have the distribution of nodes with a "server" profile and how this correlates with the vantage point of the probe. For instance, how does the geolocation of a peer correlate with the geolocation of the vantage point from where we initiate the lookup?

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

* _Status:_ **draft**

* _Area/Project of Measurement:_ IPFS
* _DRI/Team:_
* _Effort Needed:_ 
* _Prerequisite(s):_ 
* _Value:_ **HIGH**
* _Report:_ \<insert link to report once work is complete\>

#### Proposal

While IPFS is in theory less centralized than Web2, it is interesting to measure that decentralization in practice.

There are a lot of nodes deployed in cloud operators, while most users are located in certain eyeballs so in reality the decentralization may be limited.

That may have performance implications that are not apparent.

#### Measurement Plan

- Crawl and find all the DHT server (i.e., dialable) nodes.
- From the IP address of those nodes, identify whether a node is a peer with a public address or an AWS-hosted node.
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

##

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
