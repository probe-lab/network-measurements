# **RFMs - Proposals &amp; Ideas**

This page lists measurements that can potentially bit useful in developing the P2P observatory

**[RFM 1 | Lifetime of a document in the IPFS Network vs Bittorrent vs DAT vs FreeNet](#_o575jad7aotj)**

**[RFM 2 | Uptime  and churn P2P network nodes](#_3k3jj6wgwrra)**

**[RFM 3 | Location of IPFS end users and requested content](#_rd50td3ym8dy)**

**[RFM 4 | IP Churn (Roaming) for nodes in the IPFS Network](#_1mu1tfaw8au3)**

**[RFM 5 | IP Geolocation of P2P networks](#_fld2sr9emn3m)**

**[RFM 6 | Mapping the AS-level topology of P2P networks](#_1xjatm7vfujn)**

**[RFM 7 | Distribution of DHT lookups time](#_mjvqjcvas5uh)**

**[RFM 8 | Path length and Latency measurements](#_22mtgvvx3kv0)**

**[RFM 9 | Compare the lifetime of content in the Web 2.0 vs Web 3.0](#_shcpqw274ty2)**

**[RFM 10 | Compare the performance of content hosted in IPFS to Web2](#_nzea2tn76odd)**

**[RFM 11 | Compare how distributed is IPFS compared to Web2](#_5jccmpwaow0)**

**[RFM 12 | Bandwidth heat map](#_raqcome2o67l)**

**[RFM 13 | The Impact of Gateways to IPFS as a content delivery network](#_ksnbuwtki94z)**

**[RFM 14 | How efficient is caching in the IPFS network?](#_j426cm9u3j1h)**

**[Tooling/Other notes](#tooling)**

:thinking: **brainstorm** ; :memo: **draft** ; :monocle_face:	**ready for review** ; :ok_hand: **ready to implement** \&gt;

\&lt;? **LOW** ; **MEDIUM** ; **HIGH** \&gt;

---

<a id="_o575jad7aotj"></a>
## RFM 1 | Lifetime of a document in the IPFS Network vs Bittorrent vs DAT vs FreeNet


* * _Status:_ **draft**
* * _Area/Project of Measurement:_ IPFS, Bittorrent, DAT, FreeNet
* * _Delta:_ 
* * _Effort Needed:_ 
* * _Prerequisite(s):_ NONE
* * _Value:_ **HIGH**

#### Proposal

We want to learn what is the lifetime of documents (webpages, images, videos, etc) in different P2P Network to understand better the resiliency of these networks when it comes to permanency of data and the different behaviours and patterns that emerge around popular and non-popular content.

Measuring this overtime will also be a strong indication of Network growth and adoption.

#### Measurement Plan

For IPFS:

- Collect the list of CIDs being requested on the IPFS Gateways for a good list of IPFS files being requested in the network.

- Then, leverage the Hydra Booster nodes to track all the Provide Queries to check the presence of a document

- Regularly, try to fetch the file to confirm that it is still presence in the network

Additionally, expand the set of files known by looking at the Provide Queries and resolving the queries to rebuild the graphs of files and directories.

For DAT:

- ??

For Bittorrent

- Get access to multiple bittorrent trackers and harvest all torrent files
- Check regularly for the amount of seeders and leechers for that content.

For Freenet

- ??

#### Success Criteria

We have a dashboard that shows the lifetime of documents in the multiple networks, differentiated by different file size and type.

##

<a id="_3k3jj6wgwrra"></a>
## RFM 2 | Uptime  and churn P2P network nodes

* _Status:_ **draft**

* _Area/Project of Measurement:_ IPFS, Bittorrent, DAT, FreeNet

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ NONE

* _Value:_ 

#### Proposal

This proposal seeks to compare the amount of regular participation in different P2P Networks. Comparing IPFS, Bittorrent, DAT and FreeNet.

For the purposes of this measurement, we declare a node to any process in these P2P networks that speaks the network protocol and stays online contributing to the network (e.g. Both IPFS Full DHT and DHT clients are content as nodes, same goes for Bittorrent and WebTorrent nodes).

We want to learn:

- Average session length
- Average uptime per year, month and day

#### Measurement Plan

For IPFS:

- Leverage the Hydra Booster nodes to track all the FindPeer Queries to check the presence of multiaddr

For DAT:

- ??

For Bittorrent

- ??

For Freenet

- ??

#### Success Criteria

We have a dashboard that shows the lifetime distribution of nodes

## 

<a id="_rd50td3ym8dy"></a>
## RFM 3 - Location of IPFS end users and requested content.

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ IP Geolocation, IP-to-ASN

* _Value:_ **MEDIUM**

#### Proposal

Based on data from public IPFS gateways, get the location of IPFS users and the requested content. This would allow us to measure the locality of CIDs in relation to the users that issue requests. Also it would allow us to understand which nodes are actually involved in serving content.

#### Measurement Plan

For each request received by an IPFS gateway we will get the CID and the IP address of the requestor. We will then resolve the IP address to a location (city, country) and we will find the providers (peer IDs) that offer the requested CID at the time of the request based on data collected from HydraBooster nodes. By also mapping the Peer IDs to a location we will be able to understand the locality of requests in IPFS.

#### Success Criteria

We have a dashboard that visualizes the volume of requests between different relationships. A visualization like a [Chord diagram](https://python-graph-gallery.com/chord-diagram/) can be used in addition to a map. The dashboard will also provide statistics on which ASNs and locations serve and consume most content.

##

<a id="_1mu1tfaw8au3"></a>
## RFM 4 | IP Churn (Roaming) for nodes in the IPFS Network

* _Status:_ **draft**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ 

* _Value:_ **LOW**

#### Proposal

We need to learn about how stable are the IPFS nodes location and if not, how much each roam (e.g. Laptop moving from home to coffee shop to work).

#### Measurement Plan

Using the Hydra Booster nodes, track PeerIds to multiaddrs and check how often these change by executing FindPeer queries regularly.

#### Success Criteria

We have a dashboard that shows the IP churn of nodes. Ideas for dashboard:

- Churn dashboard: we can have a dashboard where the y-axis measures churn rate and the x-axis is increasing reliability. On the x-axis nodes are &quot;listed&quot; according to the churn rate we have measured.
- Roaming dashboard: we can have a dashboard where the y-axis shows change in location per 24hr period. The x-axis can again &quot;list&quot; nodes in increasing reliability in terms of location change.

##

<a id="_fld2sr9emn3m"></a>
## RFM 5 - IP Geolocation of P2P networks

* _Status:_ **draft**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ NONE

* _Value:_ **MEDIUM**

#### Proposal

Map the IPs of p2p nodes to city-level granularity. Knowing the geolocation of nodes is necessary for a lot of RFMs and follow-up analysis, as well as understanding the geographic penetration of the different p2p networks.

#### Measurement Plan

Using a geolocation database, such as MaxMind, will be the first step. However, Maxmind alone can yield inaccurate results. We will augment the MaxMind data with RIPE&#39;s IPMap which combines an array of data sources, including ping measurements, rDNS resolution and crowdsourced information to confirm the location of an IP.

#### Success Criteria

We will have a dynamic database that will map IPs to geographic coordinates, and a real-time map of the location of the P2P nodes.

##

<a id="_1xjatm7vfujn"></a>
## RFM 6 - Mapping the AS-level topology of P2P networks

* _Status:_ **draft**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ P2P Crawler

* _Value:_ **MEDIUM**

#### Proposal

Map the IPs of p2p nodes to the corresponding AS Numbers (ASNs). Such a mapping will help us infer the network-level topology of the P2P nodes, which enables better-informed analysis of performance and resilience characteristics of the P2P network.

#### Measurement Plan

The IP addresses of each P2P network (e.g. IPFS, BitTorrent) will be collected by a crawler. The collected IPs will be mapped to an AS using BGP data obtained from BGPStream (real-time stream of BGP paths from RouteViews and RIPE RIS) as well as WHOIS and RIR data to filter artifacts of BGP paths. We can also use some free services, such as the API by [Team Cymry](https://team-cymru.com/community-services/ip-asn-mapping/) that can be used to assist in this task.

#### Success Criteria

We have a dashboard that shows the distribution of nodes to ASNs, and an API that would allow the querying of the IP-to-ASN mapping.

##

<a id="_mjvqjcvas5uh"></a>
## RFM 7 - Distribution of DHT lookups time

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ 

* _Value:_ 

#### Proposal

With this measurement we look to understand how DHT lookups behave throughout time according to the specific file being searched, the status of the network, the location of nodes in the network, the time required to perform a connection, or load of the nodes. The result of this measurement should be a distribution of the time required to perform DHT lookups. For instance, if we chose to see the distribution of DHT lookups of the last 7 days we will output an histogram with the time invested to perform a lookup in the DHT by the different probes.

- % of requests below 500 ms
- % of requests between 500ms and 1 s.
-

This gives a good sense of the state of the network at a specific epoch.

Additionally, we could show the distribution of lookups in a specific probe, i.e. in a specific section of the network, in order to have a sense of the DHT lookup times to be expected for someone in the probe&#39;s premises.

#### Measurement Plan

To measure this, a set of probes would be deployed in different locations. Each of these probes would perform random lookups in the DHT and track the time until it succeeds up to a timeout (of 30 seconds?).

To increase the accuracy and granularity of the measurement, we could distinguish between GET and PUT operations. According to the implementation of the underlying DHT in the network doing a GET lookup (until the specific content is found) may be faster than putting new content in the network (where we always try to find the nearest peer to the content possible).

#### Success Criteria

We have a dashboard that shows different buckets with the number of requests for the different delays for a specific period of time.

##

<a id="_22mtgvvx3kv0"></a>
## RFM 8 - Path length and Latency measurements

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ IP Geolocation, IP-to-ASN

* _Value:_ 

#### Proposal

Develop a map of pairwise path lengths and latencies between different tuples of (ASN, city) points. Such measurements can potentially inform the design of DTH construction, the selection of content providers (when a CID is available from multiple providers), and the deployment of Hydra Booster nodes or relays.

#### Measurement Plan

We will collect ping and traceroute measurements from multiple distributed vantage points available through platforms such as SpeedChecker and RIPE Atlas. The measurements vantage points and destinations will be selected based on the locations of the nodes in the P2P network so that we map only the relevant (ASN, city) tuples and not the entire Internet. The measurements will be repeated periodically (for instance daily) to maintain an updated dataset that will capture changes in the network layer.

#### Success Criteria

A real-time observatory of latencies and path lengths in the form of a dashboard.

##

<a id="_shcpqw274ty2"></a>
## RFM 9 - Compare the availability and lifetime of content in the Web 2.0 vs Web 3.0

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ 

* _Value:_ 

#### Proposal

find which content is common between Web2 and IPFS. Then we will compare a number of metrics, such as stability, performance, and popularity in IPFS against HTTP-based web. Note that in this RMF we&#39;re interested in the availability of content (available or not) instead of the stability of the nodes that host that content.

#### Measurement Plan

Based on projects such as the HTTP Archive ([https://httparchive.org/reports/state-of-the-web](https://httparchive.org/reports/state-of-the-web)) or Common Crawl (https://commoncrawl.org), we will extract the files that are part of the most popular web pages (e.g. top 100K according to Alexa). We will map this content to CIDs and search IPFS for this content. This first measurement will allow us to map the availability of Web 2.0 content in IPFS, namely quantify the overlap. Then by parsing periodic snapshots of the above mentioned archives and Hydra Booster logs we will keep track of content availability over time.

#### Success Criteria

A dashboard that will provide statistics on content overlap and content availability.

##

<a id="_nzea2tn76odd"></a>
## RFM 10 - Compare the speed of delivery of content hosted in IPFS to Web2

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ RFM 8

* _Value:_ 

#### Proposal

Measure and analyze the performance of retrieving content between IPFS and Web2 for overlapping content, e.g. time to first byte.

#### Measurement Plan

...

#### Success Criteria

...

##

<a id="_5jccmpwaow0"></a>
## RFM 11 | Compare how distributed is IPFS compared to Web2

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ 

* _Value:_ 

#### Proposal

While IPFS is in theory less centralized than Web2, it is interesting to measure that decentralization in practice.

There are a lot of nodes deployed in cloud operators, while most users are located in certain eyeballs so in reality the decentralization may be limited.

That may have performance implications that are not apparent.

#### Measurement Plan

...

#### Success Criteria

...

##

<a id="_raqcome2o67l"></a>
## RFM 12 | Bandwidth heat map

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ 

* _Value:_ 

#### Proposal

Once we&#39;ve mapped the topology of the network, it may be useful to map the links (or sections of the network) that exchange more information. Measuring this may not be trivial, but we can have a good sense of what is happening with a latency map.

#### Measurement Plan

...

#### Success Criteria

...

##

<a id="_ksnbuwtki94z"></a>
## RFM 13 - The Impact of Gateways to IPFS as a content delivery network

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ 

* _Value:_ 

#### Proposal

It would be great to have an idea of the percentage of content that is served through the IPFS Gateways (PL-operated or not, it doesn&#39;t matter), as compared to regular IPFS server nodes. If we find that the vast majority of content is served from gateways, we need to further investigate the reason why. Are gateways more trusted by users? Is it just that it&#39;s difficult to get a public IP address in order to become a server? Excessive reliance on IPFS gateways could mean that the network is more centralised than we previously thought.

As a further step it would be great to take measurements to see the delivery latency between serving content through the gateway and through some server nodes.

#### Measurement Plan

...

#### Success Criteria

...

##

<a id="_j426cm9u3j1h"></a>
## RFM 14 | How efficient is caching in the IPFS network?

* _Status:_ **brainstorm**

* _Area/Project of Measurement:_ IPFS

* _Delta:_ 

* _Effort Needed:_ 

* _Prerequisite(s):_ 

* _Value:_ 

#### Proposal

It would be interesting to figure out what is the performance improvement that caching provides in the IPFS network. Given some distribution of a content item in the network and some request distribution, how efficient is the content resolution mechanism in resolving the closest copy? Is the network actually delivering the closest copy to the requestor?

#### Measurement Plan

- …We have/control a number of clients located in different geographic locations (different countries and continents)
- We have/control a number of servers located in different geograpich locations (different continents)
- We plant a copy of some content in some (or all) of the servers and make a request from a client (or another server) in the same continent.

#### Success Criteria

...

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
