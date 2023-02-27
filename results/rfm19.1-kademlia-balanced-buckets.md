# Balanced Buckets Report

Date: 2023-02-24

DRI: [Guillaume Michel](https://github.com/guillaumemichel)

Implementation: [`balanced_buckets.ipynb`](../implementations/rfm19-dht-routing-table-health/balanced_buckets.ipynb)

# Motivation

Kademlia is a distributed hash table (DHT) protocol used by decentralized peer-to-peer networks like IPFS. One of the key features of Kademlia is its efficient lookup algorithm, which allows nodes to find the value associated with a given key by querying a subset of the network.

In Kademlia, nodes are organized into a binary tree structure called the "routing table". Each node maintains a list of other nodes that are close to it in the network, based on the XOR distance metric. When a node needs to find a value associated with a given key, it starts by querying nodes that are close to it in the routing table, and then gradually expands its search to nodes that are farther away.

The hop count in Kademlia lookup refers to the number of intermediate nodes that a query must traverse in order to reach the node that holds the value associated with the key. A small hop count is desirable for the following reasons:

- Efficiency: Each hop in the network introduces latency and consumes bandwidth. By minimizing the number of hops required to reach the target node, Kademlia can achieve faster and more efficient lookup times.
- Robustness: Kademlia is designed to work well in large-scale networks with many nodes. However, as the number of hops in a lookup increases, the probability of encountering a failed node or a slow network link also increases. This can lead to timeouts, delays, and other performance issues. By minimizing the hop count, Kademlia can better tolerate churn.

# Summary of Findings

In theory balancing the routing table’s buckets is expected to result in a lower average hop count. However, determining the exact formula to calculate the hop count based on the bucket selection strategy is not a straightforward task. Instead, we used a simulator to compare the performance of different bucket selection strategies. We observed that the hop count only get reduced by `~2-3%`, which is lower than what we expected initially.

# Balancing Kademlia buckets

Currently, the bucket selection strategy implemented in the IPFS DHT is to add peers to the bucket they fit if the bucket isn’t full yet. The peers in all buckets are periodically probed, and evicted if they fail to answer. This results in a bucket selection strategy of first peer discovered first peer in the bucket, and unstable peers eventually being evicted, thus only keeping stable peers.

A balanced bucket is one where the members of the bucket create a balanced binary trie. This means that there are equal numbers of peers with prefix `0` as there are with prefix `1`, and the same goes for peers with prefixes `00`, `01`, `10`, and `11`, and so on. By *prefix*, we refer to the initial part of the peer's identifier within the bucket. For instance, let’s consider bucket 3 of a peer with the identifier `001011...`. In that case, bucket 3 will contain all peers with identifiers starting with `0011`. The prefix is the part of the identifier that follows the `0011`, the peer with identifier `0011010...` has prefixes like `0`, `01`, or `010`, and so on.

There are two important binary tries to take into account: the binary trie of peerids, and the binary trie of CIDs. There are much more CIDs than peerids in the IPFS DHT. The distribution of CIDs in the keyspace can be considered as constant in comparison with the peerids distribution, for the number of CIDs is much larger than the number of peerids. Each peerid is located at a specific depth in the peerids binary trie, and the depth of the peerids follows a [logarithmic distribution](https://www.youtube.com/watch?v=0dKz_K-7eoI), meaning that the peerids binary trie cannot be exactly balanced by design.

In the current Kademlia implementation, the buckets can be totally unbalanced, e.g only peers starting with prefix `00`. In this case this is bad if a client is looking up for a key with prefix `1`, because the lookup will certainly cost one additional hop.

To balance the Kademlia buckets, random peers are added just like in the current implementation. However, when a new peer is added that matches a prefix of length $\leq \lceil log_2(bucket\_size)\rceil$ which is not already in the bucket, it replaces a peer that has a prefix of length $\geq \lceil log_2(bucket\_size)\rceil$ which is already represented at least twice in the bucket. The newly added peer evicts the peer that joined the bucket most recently. Balanced buckets are expected to have a lower average lookup hop count compared with random bucket compositions.

# Simulation Setup

We’ve built a simple [python simulator](../implementations/rfm19-dht-routing-table-health/balanced_buckets.ipynb) to test the performance benefit that the system would see if all nodes had balanced buckets in their routing tables. The simulator takes as system parameters: the key size (`256` bits), the number of peers in the network (`25’000` used in the simulation), a concurrency parameter (`10`), a replication factor (`20`), and the bucket size (`20`). All parameters are standard for the IPFS network.

Please note that concurrency is exactly concurrent in the simulator, while in the IPFS network it depends on the network latency. In the simulator, all requests at hop `1` are sent concurrently, and come back at the same time. At hop `2`, all responses from hop `1` are taken into account and all requests are sent concurrently again. In real world IPFS, at hop `1` all requests are sent concurrently. However, as soon as the fastest request comes back, hop `2` is starting. One request is sent to the best peer returned by the fastest request at hop `1`. Then when the second request from hop `1` comes back, a new message will be sent to either the nearest peer from the second fastest response or the second nearest peer from the fastest response.

The simulation first generates random keys, serving as peerids. Then using the generated peers, it builds a *random routing table*, and a *balanced routing table*. For each peer, it generates empty buckets, and the buckets are filled with random peers. There are no constraints for the *random routing table*. For the *balanced routing table*, the only constraint is that all buckets must be balanced if possible, the selection is random if multiple peers fit the same spot.

The lookup process is simulated as follows. A random key is generated, and the `repl` closest peers are computed. A peer `p` is selected at random to perform the lookup. If `p` is among the `repl` closest peers, the lookup took `0` hops. Otherwise `p` looks in its own routing table for the `concurrency` closest peers (`peer1`) to `k`. If one of these peers is among the `repl` closest peers, the lookup took `1` hop. Else, take the union of the routing tables of all peers in `peer1`, and find the `concurrency` closest peers (`peers2`) to `key`. If one of these peers is among the `repl` closest peers, the lookup took `2` hops. And so on and so forth.

The experiment consisted in generating `5` peers sets. For each set, a *random routing table* and a *balanced routing table* were built. Then `10'000` lookup requests are performed from a peer randomly selected in the initial peers set for both routing tables. We record the hop count for all requests.

# Results

```bash
hop count (random, balanced):
[(1.9287, 1.8931),
 (1.923, 1.893),
 (1.9263, 1.8902),
 (1.9347, 1.8914),
 (1.9332, 1.896)]

Average random buckets: 1.929
Average balanced buckets: 1.893
Improvement: 1.89%
```

We observe a minor improvement of on average `1.89%` for lookup with a balanced routing table in comparison with a random routing table.

If we make the bucket size vary from `10` to `100` we get the following results

```bash
{10: [(2.173, 2.0841),
  (2.1698, 2.0799),
  (2.1568, 2.0891),
  (2.1686, 2.0895),
  (2.159, 2.0849)],
 20: [(1.9298, 1.8848),
  (1.9234, 1.8918),
  (1.9229, 1.8925),
  (1.9262, 1.8952),
  (1.9292, 1.891)],
 30: [(1.8677, 1.8426),
  (1.8679, 1.8404),
  (1.8677, 1.8459),
  (1.8658, 1.8457),
  (1.8738, 1.8385)],
 40: [(1.8329, 1.8125),
  (1.838, 1.8051),
  (1.8326, 1.8054),
  (1.8323, 1.8099),
  (1.8338, 1.8123)],
 50: [(1.8062, 1.7731),
  (1.8019, 1.7749),
  (1.8087, 1.7795),
  (1.8054, 1.7773),
  (1.8083, 1.7721)],
 60: [(1.7664, 1.742),
  (1.7862, 1.7458),
  (1.7789, 1.7396),
  (1.7823, 1.7488),
  (1.7751, 1.7394)],
 70: [(1.7575, 1.7157),
  (1.7575, 1.7133),
  (1.7561, 1.7039),
  (1.7551, 1.7182),
  (1.7546, 1.7122)],
 80: [(1.7316, 1.6825),
  (1.7265, 1.6859),
  (1.7343, 1.6871),
  (1.7285, 1.6769),
  (1.7239, 1.6872)],
 90: [(1.7144, 1.6609),
  (1.7039, 1.6495),
  (1.7105, 1.6741),
  (1.7069, 1.6662),
  (1.7074, 1.6678)],
 100: [(1.7009, 1.6315),
  (1.6875, 1.6344),
  (1.6958, 1.6317),
  (1.6899, 1.6345),
  (1.6888, 1.6312)]}

(avg_random, avg_balanced, improvement)
{10: (2.165, 2.085, 3.69%),
 20: (1.926, 1.891, 1.83%),
 30: (1.868, 1.842, 1.39%),
 40: (1.834, 1.809, 1.36%),
 50: (1.806, 1.775, 1.7%),
 60: (1.777, 1.743, 1.95%),
 70: (1.756, 1.712, 2.48%),
 80: (1.728, 1.683, 2.61%),
 90: (1.708, 1.663, 2.63%),
 100: (1.692, 1.632, 3.54%)}
```

The overall improvement rate observed is limited to less than `4%` for the performed simulations.

This means that the routing tables are *naturally* *balanced enough*, and aren’t performing much worse than the theoretical maximum.

# Conclusion

We observed that the measured improvement from having balanced buckets over random buckets is minimal. In a perfect world, balanced buckets would be implemented in the DHT implementation. However, as this implementation change requires non negligible engineering work and adds complexity to the code base, we consider that this is not worth the effort at this point in time and decided not to proceed with the implementation. We suggest that this modification be implemented when a 2-3% enhancement in hop count becomes crucial.
