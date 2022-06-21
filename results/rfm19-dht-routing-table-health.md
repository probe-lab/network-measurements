# RFM19 Report: DHT Routing Table Health

Author: [Guillaume Michel](https://github.com/guillaumemichel)\
Date: 2022-06-14

## Table of Contents

- [Motivation](#motivation)
- [Measurement Methodology](#measurement-methodology)
- [Measurement Results](#measurement-results)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [References](#references)

## Motivation

_[What was the need for this RFM and why is it important? What was the expected impact?]_

We are building a decentralized system that we are not operating ourselves. We want to continuously improve this system to make it faster, easier to use etc. If we want to improve something, we have to measure it first. The goal of this project is to study Kademlia Routing Table Health in the IPFS network. This will allow us to understand if the routing tables behave as we expect, to monitor if any routing attack (DHT eclipse etc.) is being performed, and to propose some improvements to Kademlia Routing.

## Measurement Methodology

_[Provide details on the methodology used in a way that others can reproduce the experiments. Please reason about your choices and why your chosen methodology meets the needs of the RFM.]_

### Nebula Crawler

We used the [Nebula Crawler](https://github.com/dennis-tra/nebula-crawler) to get the content of the routing table of nodes in the IPFS network. The Nebula Crawler starts with a couple of bootstrap peers, ask them for handcrafted CIDs in order to discover all peers in the network. To fetch the routing table from a node, the crawler will request `k=20` handcrafted CIDs uniformely distributed in each of the kbuckets of the peer.

The Nebula Crawler provides us the peerIDs of the nodes in the IPFS networks, as well as the routing tables of these nodes at each crawl.

Once the Nebula Crawler returns all the routing tables, we can reconstruct the kbuckets of each peer using the peerIDs.

Given all the alive nodes in the network at the time of the crawl, we can have a _global_ vision of what is supposed to be in the nodes' kbuckets.

#### Technical limitations

The Nebula Crawler may be unaware of nodes that are not well connected to the IPFS network, or in a network split. Thus, when we talk about the resilience of the network, we talk about the resilience of the largest partition, provided by the Nebula Crawler.

### Binary Trie

Kademlia XOR distance is non linear. Thus it is computationnaly expensive to build the kbuckets. The Binary Trie structure is a good data representation for this purpose. We built a simple python [Binary Trie](https://github.com/guillaumemichel/py-binary-trie) to compute XOR distance in the Kademlia keyspace.

The Binary Trie provides functions to get the `n` closest keys to a specific key. It is thus helpful to determine the Kademlia _closeness_ of the IPFS peers.

### Reproducing the Measurements

The python scripts used to produce the following plots live in the [`implementations/rfm19-dht-routing-table-health/`](https://github.com/protocol/network-measurements/tree/master/implementations/rfm19-dht-routing-table-health) folder.

The data **will be** available in the `data/` subfolder if not too large.

## Measurement Results

_[Summary of main results together with a description of what we see behind the plots. What do these results mean wrt your initial goal and how do they answer the motivation?]_

### Peers distribution in the k-buckets

The plot below shows the buckets in which the peers from the routing table belong. Note that it is not exactly the bucket in which they belong on the host, because of the implementation. The bucket shown on the plot is the theoretical bucket, computer from the distance between the hosts.

![alt text](../implementations/rfm19-dht-routing-table-health/plots/kbucket-filling-distribution.png)

Kademlia [1] routing table is composed of `k-buckets`, sorting remote peers according to the XOR distance between the peer's own 256-bits ID and the remote peer ID. Peer `P0` will have peer `P1` in its `k-bucket` if `P0`'s ID and `P1`'s ID share a common `k-bit` prefix. Each bucket is capped at a maximum of `20` peers by design. Note that in theory, the routing table should contain 256 buckets, with most of them totally empty. The actual `libp2p` implementation only create the necessary buckets, and the bucket with the highest ID will contain up to 20 peers with the longest CPL, even though the peer IDs would theoretically belong to different buckets. **[TODO: add reference to implementation]** We will discuss only the theoretical buckets, represented by the CPL.

This boxplot represents the filling status of Kademlia `k-bucket` in the IPFS network. We removed the outliers from the boxplot for sake of readability because the high number of samples induce a high number of outliers. The yellow bar indicate the mean number of peers in each bucket. The bottom of the box represents the 25th percentile, or `Q1` and the top of the box represents the 75th percentile or `Q3`. **[TODO: outliers as Circle with various radius / whisker representing 95th percentile]**.

Statistically, bucket `i` is expected to have $\frac{N}{2+i}$ candidates with `N` being the network size. 

**[TODO: correct plot with online peers only]**
Buckets `0-8` are full, which is expected as $N=???$ **[TODO: verify numbers]** $N/10 >= 20$. Then we can see that the amount of peers in buckets `9` to `14` approvimatively halves at each bucket (**[TODO: add exact average]**). Buckets 15 and above contain no peers, with the exception of a few outliers.

From these numbers, we can say that the filling status of the `k-buckets` is as expected.

### Dead peers

**[TODO: add dead peers plot]**

### Incomplete k-buckets

![alt text](../implementations/rfm19-dht-routing-table-health/plots/missing-peers.png)

**[TODO: check if columns reordering is needed]**
**[TODO: shift columns to the center]**
**[TODO: add a "-" to non-full]**

A _missing_ peer is defined as a peer ID that would fit a non-full k-bucket, but is not included. We define the maximum number of missing peers per k-buckets to be $m=20-\#peers$. The plot shows the average number of missing peers per bucket, compared with the average number of missing peers per non-full k-bucket and with the average total number of peers per bucket. 

The buckets that are almost always full (19.XX peers on average **[TODO: INSERT NUMBER]**), IDs `0` to `8` have a very low number of missing peers, 0.XX **[TODO: INSERT NUMBER]** on average. However, the same buckets have a quite high number of missing peer per non-full bucket, 4.XX on average **[TODO: INSERT NUMBER]**. This implies that most of these buckets 9X.XX% **[TODO: INSERT NUMBER]** are full, but the non-full bucket are missing multiple peers on average **[TODO: INCLUDE ZOOM GRAPH ON THESE NON FULL BUCKETS?]**. One possible explanation is that the peers recently joined the network, and their routing table isn't fully populated yet. **[TODO: CHECK if it is the same peerIDs for which the different buckets are not full]**

Concerning buckets with ID `9` and above, the number of missing peers per bucket almost always matches the number of missing peers per non-full bucket, for the buckets are rarely full. Less than `0.X` **[TODO: INSERT NUMBER]** peer on average is missing for each bucket, meaning that the network is healthy. We will focus more on the 20 closest peers in the next section.

**[TODO: plot ratio of missing peers for buckets 9+]**

### 20 Closest Peers Awareness

![alt text](../implementations/rfm19-dht-routing-table-health/plots/known-peers-among-20-closest.png)

The plot displays the Probability Density Function (PDF) and Cumulative Distribution Function (CDF) of the number of peers, among the 20 closest, in a node's routing table **[FEEDBACK WELCOME: IS IT CLEAR? REFORMULATION WELCOME]**. It shows that 59.XX% **[TODO: INSERT NUMBER]** of the peers have all of their 20 closest peers in their routing table, which is expected in a network with no churn. Only 5.XX% of the nodes **[TODO: INSERT NUMBER]** know 17 or less of their 20 closest peers. These results show how resilient is the Kademlia routing table in the IPFS network. **[TODO: ADD SOMETHING CONCRETE TO UNDERLINE THE PERFORMANCE]**

### Closest Peers distribution in k-buckets

In the following plots, we will study the `k-bucket` distribution of the peers in a close locality.

**[TODO: replace avg line with x's]**

![alt text](../implementations/rfm19-dht-routing-table-health/plots/kbucket-distribution-20-closest-peers.png)

This plot shows the k-bucket distribution for the $n^{th}$ closest peer. The standard deviation is higher for the $1^{st}$ to $3^{rd}$ closest peers, then it gets smaller for other peers, which is expected for the peer distribution. One average, the closest peer lies in bucket `14`, and the $20^{th}$ closest peer in bucket `9`. As the minimum k-bucket ID for the closest peer is `10` it implies that any peer in the IPFS network shares a Common Prefix of Length of at least `10` with at least another node in the network. In other words, the most isolated nodes have their closest neighbor at a XOR distance of $2^{256-10} = 2^{246}$. This distance is on average the same as the $11^{th}$ closest peer. Note that the measurements apply to the largest partition of the IPFS network, as provided by the Nebula Crawler. Network splits and unreachable peers were not taken into consideration.

![alt text](../implementations/rfm19-dht-routing-table-health/plots/distribution-10-closest-peers.png)

**[TODO: CHANGE GRID DIRECTION]**

Distribution of the 10 closest peers in the k-buckets. Note that buckets `9` to `12` contain more peers that are not in the 10 closest ones.

### Peer ID Distribution

![alt text](../implementations/rfm19-dht-routing-table-health/plots/peerid-distribution.png)

The plot above shows the distribution of the Peer IDs over the keyspace. For a better visualization, the keyspace has been broken down to 128 (=$2^7$) keyspace chunks. `libp2p` uses a 256 bits keyspace $\{0, 1\}^{256}$, each chunk contains keys from $bin(i)+0^{249}$ to $bin(i) + 1^{249}$ for `i` in $[0, 127]$, $bin(i)$ being the binary representation of `i`, **[FEEDBACK WELCOME]** $X^n$ being the bitstring representation of bit `X` repeated `n` times (e.g $0^3=000$). All the keys falling in the same chunk share a common 7-bit prefix.

The represented data is the average number of alive peer over **[TODO: INSERT TIME PERIOD]** crawls falling in each keyspace chunk. We can see that the Peer IDs are almost evenly distributed in the 128 keyspace chunks. **[TODO: INSERT AVG AND STD]** We would have expected such a distribution **[TODO: order chunks to show a gaussian curve]**. There is a single peek high above the average at `360`, which is only `1.5x` the average `240` **[TODO: CHECK NUMBERS]**, which is too little to perform any eclipse attack. **[TODO: FIND REFERENCE FOR ECLIPSE ATTACK]**. **[TODO: ADD ZOOM IN PLOT FOR HIGH PEAK]**


## Future Work

- Churn impact in routing tables
- Perfect routing table

## Conclusion

_[Please include the main take-home points. What are the 2-3 most important findings that someone should remember if they forgot about everything else in this report? If appropriate, include this short list as a TL;DR at the beginning of the report. This is a good place to point to any items that need further attention, or a separte RFM.]_

The DHT is healthy =D

## References

_[Pointers to related works, studies, papers, or repos]_

[1] Petar Maymounkov and David Mazières. Kademlia: A peer-to-peer information system based on the XOR metric. In Proceedings of the 1st International Workshop on Peer-to-Peer Systems (IPTPS '02), pages 53-65, March 2002. [paper](https://ipfs.io/ipfs/QmaVrnwZrnoG4YramcN75mbE5AUfCymiEErrHGXoQR968V)

[2] [Nebula Crawler](https://github.com/dennis-tra/nebula-crawler) from  [Dennis Trautwein](https://github.com/dennis-tra)

[3] [DHT Routing Table Health Notion Page](https://www.notion.so/pl-strflt/DHT-Routing-Table-Health-f8e6836c4b09440baa909a4448a88fbf)

