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

### Incomplete k-buckets

![alt text](../implementations/rfm19-dht-routing-table-health/plots/missing-peers.png)

Show the average number of hosts per bucket, the average number of missing hosts per bucket, and the average number of missing hosts per non full bucket.

### 20 Closest Peers Awareness

![alt text](../implementations/rfm19-dht-routing-table-health/plots/known-peers-among-20-closest.png)

### Closest Peers distribution in k-buckets

![alt text](../implementations/rfm19-dht-routing-table-health/plots/kbucket-distribution-20-closest-peers.png)

![alt text](../implementations/rfm19-dht-routing-table-health/plots/distribution-10-closest-peers.png)

### Peer ID Distribution

![alt text](../implementations/rfm19-dht-routing-table-health/plots/peerid-distribution.png)



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

