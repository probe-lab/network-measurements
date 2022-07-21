# RFM 19: DHT Routing Table Health

Author: [@guillaumemichel](https://github.com/guillaumemichel)

## What is in this folder?

This folder contains the data, plots, and scripts used for RFM19, DHT Routing Table Health. The report can be found [here](../../results/rfm19-dht-routing-table-health.md).

## [`plots/`](./plots/)

All plots from [RFM19 report](../../results/rfm19-dht-routing-table-health.md) can be found in this [folder](./plots/).

## [`data/`](./data/)

Contains the data useful to run the measurement scripts. All data was obtained from the Nebula Crawler, and only the necessary information is inculuded in `csv` files.

- [`data/all-peerids.csv`](./data/all-peerids.csv) contains the mapping `nebula_id <-> peer_id` of all nodes observed by the Nebula Crawler between `2022-02-16` and `2022-05-03`
- [`data/nebula-peers-2crawls.csv`](./data/nebula-peers-2crawls.csv) contains data from 2 successive Nebula crawls on `2022-05-03` at `06:00` and `07:00` UTC. Each row of this file follows the format `crawl_id, nebula_id, peer_id, neighbor0_nebula_id, neighbor1_nebula_id, ..., neighborN_nebula_id`. It corresponds to a row for each peer, for each crawl, the peer ID of the node and the nebula ID of all of the nodes in its routing table. Note that unreachable peers have an row, but don't have any `neighborX_nebula_id` entries. This data is enough to reconstruct the _global_ routing table.

Two additional data files were too large to upload to Github, they are accessible on [web3.storage](https://web3.storage).

- [`data/nebula-peers-5crawls.csv`](ipfs://bafybeiaqr6csdcnxrkpx23oithpjtuhpzudq43pkciavygsfr3i5qz6dcy) [CID: `bafybeiaqr6csdcnxrkpx23oithpjtuhpzudq43pkciavygsfr3i5qz6dcy`] contains data from 5 successive Nebula crawls on `2022-05-03` from `03:00` to `07:00` UTC.
- [`data/nebula-peers-1week.csv`](ipfs://bafybeif6u5pukl3szezll4myp77eebeyq6ywp7hveahyllutsj7hepxltq) [CID: `bafybeif6u5pukl3szezll4myp77eebeyq6ywp7hveahyllutsj7hepxltq`] contains data from 28 non successive Nebula crawls from `2022-04-19` until `2022-04-26` every day at `21:00`, `03:00`, `09:00` and `15:00` UTC.

## Scripts

The following python notebook helped us analyse the data coming from the Nebula Crawler.

- [postgres_to_csv.ipynb](./postgres_to_csv.ipynb) is used to query the Nebula Crawler database and generate the data `csv` files used in the data analysis.
- [dht-routing-table-health.ipynb](./dht-routing-table-health.ipynb) contains the analysis of the DHT routing table health, and generates the plots.

## How to reproduce the results

In order to reproduce the results, you can download the data files and simply run the [dht-routing-table-health.ipynb](./dht-routing-table-health.ipynb) python notebook. You can generate new data from the Nebula Crawler and [postgres_to_csv.ipynb](./postgres_to_csv.ipynb) or from any other data source, and use the script to produce the plots associated with the data.

[`py-binary-trie`](https://pypi.org/project/binary-trie/0.0.7/) package version 0.0.7 has to be installed using `pip install binary-trie==0.0.7`
