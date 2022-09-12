# Existing metrics

- The Protocol Labs Metrics Group is doing highly relevant work in defining and collecting metrics https://github.com/protocol/metrics

# Survey

## IPFS & libp2p

### Papers

|                                                                                                                                                                                                                                 | Venue                      | Year | Code                                                | Data                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|------|-----------------------------------------------------|-----------------------------------------------------------------------|
| [Mapping the Interplanetary Filesystem.](https://dl.ifip.org/db/conf/networking/networking2020/1570620406.pdf)                                                                                                                  | IFIP Networking Conference | 2020 | [Yes](https://github.com/wiberlin/ipfs-crawler)     | No                                                                    |
| [Crawling the IPFS Network.](http://dl.ifip.org/db/conf/networking/networking2020/1570644207.pdf)                                                                                                                               | IFIP Networking Conference | 2020 | [Yes](https://github.com/wiberlin/ipfs-crawler)     | No                                                                    |
| [Measuring Decentralized Video Streaming: A Case Study of DTube](https://ieeexplore.ieee.org/abstract/document/9142739?casa_token=nqT_TXYf108AAAAA:9g6Q0sNkPK7t9mrQy8HJsJoLW-tERV60BqMmgxcnwIMuWBbSLD9lUjvM0CWXlcJzHFfOkBcRXZM) | IFIP Networking Conference | 2020 | [Yes](https://github.com/tv-doan/ifip-net-2020-app) | [Yes](https://github.com/tv-doan/ifip-net-2020-analysis)              |
| [Monitoring Data Requests in Decentralized Data Storage Systems: A Case Study of IPFS](https://arxiv.org/abs/2104.09202)                                                                                                        | ICDCS                      | 2022 | No                                                  | [On Request](https://monitoring.ipfs.trudi.group/privacy_policy.html) |
| [Design and evaluation of IPFS: a storage layer for the decentralized web](https://dl.acm.org/doi/pdf/10.1145/3544216.3544232)                                                                                                  | SIGCOMM                    | 2022 | Probably                                            | Probably                                                              |

### Datasets and Tools

#### IPFS Crawlers

| Tool                                                                    | Description                                                                                                                                                                        | Languages     | Status   | Documentation        | Working                                                                                                                                                       |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|----------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [vyzo/ipfs-crawl](https://github.com/vyzo/ipfs-crawl)                   | A simple crawler for diagnosing connectivity issues in the ipfs network                                                                                                            | Go            | Inactive | Installation only    | No. Opened an [issue](https://github.com/vyzo/ipfs-crawl/issues/8). Author commented that it's not maintained anymore and should be ported to go mod to work. |
| [dzhelezov/ipfs-crawler](https://github.com/dzhelezov/ipfs-crawler)     | A simple ifps crawler to estimate the IPFS network size and node churn.                                                                                                            | Go            | Active   | Basic                | Yes. It outputs the peer IDs that need to be mapped to IP addresses with follow-up queries.                                                                   |
| [trudi-group/ipfs-crawler](https://github.com/trudi-group/ipfs-crawler) | Crawler for the IPFS network, code for the paper "Mapping the Interplanetary Filesystem". Also holds scripts to evaluate the obtained data and make similar plots as in the paper. | Go, Python, R | Active   | Extensive            | Not successfully. The crawler finishes immediately with empty output. Opened an [issue](https://github.com/wiberlin/ipfs-crawler/issues/1). Now fixed.        |
| [manuelpolzhofer/ipfs-mon](https://github.com/manuelpolzhofer/ipfs-mon) | A crawler for IPFS nodes to estimate the number of nodes and daily churn in IPFS                                                                                                   | Go            | Active   | Installation + Usage | Yes, but outputs only PeerID                                                                                                                                  |
| [BasitAwan/IPFS-Crawler](https://github.com/BasitAwan/IPFS-Crawler)     | This crawler crawls the IPFS to get a snapshot of the peers in the network                                                                                                         | Go            | Active   | Basic logic          | No, seems to be stuck and produces no output                                                                                                                  |

#### Monitoring Tools

| Tool                                                                                                         | Description                                                                                                                                                                                           | Language | Status |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------|
| [IPFS Metrics Exporter Plugin](https://github.com/trudi-group/ipfs-metric-exporter)                          | Kubo (go-ipfs) plugin to export additional metrics from large, well-connected monitoring nodes. Exports Bitswap traffic in real-time and metrics via Prometheus. Used for the ICDCS monitoring paper. | Go       | Active |
| [IPFS Public Gateway Finder](https://github.com/trudi-group/ipfs-tools/tree/master/ipfs-gateway-finder)      | Finds overlay addresses of public IPFS gateways through a traffic-correlation attack on their HTTP side.                                                                                              | Rust     | Active |
| [Bitswap Monitoring Client](https://github.com/trudi-group/ipfs-tools/tree/master/bitswap-monitoring-client) | Connects to multiple monitors running the Metric Exporter Plugin and analyzes Bitswap traffic in real-time. Exports metrics via Prometheus.                                                           | Rust     | Active |

#### Dashboards

| Dashboard                                                               | Description                                                                                                                                                           | Code       | Data                                                                  |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------|
| [IPFS Monitoring Metrics](https://grafana.monitoring.ipfs.trudi.group/) | Various metrics extracted from IPFS nodes with unlimited connection capacity and the Bitswap messages they receive. Uses the monitoring plugin and associated client. | Not yet :) | [On Request](https://monitoring.ipfs.trudi.group/privacy_policy.html) | 


## Bittorrent

### Papers

|                                                                                                                                                                                                                                                                               | Venue                                            | Year | Code           | Data |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|------|----------------|------|
| [Characterization of BitTorrent swarms and their distribution in the Internet](https://www.sciencedirect.com/science/article/pii/S1389128610003622?casa_token=5q2Sv0tvSYQAAAAA:0xMHei4r7RLSwRINM60KijY6ysM1Bf_aBdtKGPg420ga85yaBnR7RP0AYC-Q1BqB4VwRL_gG7rA)"                  | Elsevier Computer Networks                       | 2011 | No             | No   |
| [The bittorrent peer collector problem.](https://ieeexplore.ieee.org/abstract/document/7987311/)                                                                                                                                                                              | IFIP IM                                          | 2017 | No             | No   |
| [A measurement study on the topologies of BitTorrent networks.](https://ieeexplore.ieee.org/abstract/document/6585893/?casa_token=W35m1VwXPeoAAAAA:EQAZUUxc8Q09mZxXocX6hoD1TGIulU6dJKUOJzSh3DffWxM87wa5cpTNa9RF2wtOogyVgFVFj7Q)                                               | IEEE Journal on Selected Areas in Communications | 2013 | No             | No   |
| [Analysis of topology dynamics for unstructured P2P networks.](https://www.sciencedirect.com/science/article/pii/S0140366416300020?casa_token=AHWqoidOKwgAAAAA:HiyCglYkrmsV72rbCKE_0s-5F2gul9lAISHLaTop0OxrCWPvuv_x2fkFWEHCT5oNNKH--o-FkDA)                                   | Elsevier Computer Communications                 | 2016 | No             | No   |
| [Big torrent measurement: A country-, network-, and content-centric analysis of video sharing in BitTorrent.](https://ieeexplore.ieee.org/abstract/document/8406243/?casa_token=GcH83DSy3cIAAAAA:d70m7jjHEQvVrscmb2nIokvuzLOrDm2Djon88EZcL7wkBHl6pGEez3NMYs0aYjfCwnyALhC_7CQ) | IEEE NOMS                                        | 2018 | No             | No   |
| [Inference on the Network Evolution in BitTorrent Mainline DHT.](https://arxiv.org/pdf/1412.0103)                                                                                                                                                                             | arxiv                                            | 2014 | No             | No   |
| [Measuring the bittorrent ecosystem: Techniques, tips, and tricks.](http://www.netcom.it.uc3m.es/sites/default/files/pdf/publications/2011/Measuring_BitTorrent_Ecosystem_2011.pdf)                                                                                           | IEEE Communications Magazine                     | 2011 | No             | No   |
| [Crawling BitTorrent DHTs for Fun and Profit.](https://static.usenix.org/event/woot10/tech/full_papers/Wolchok.pdf)                                                                                                                                                           | USENIX WOOT                                      | 2010 | No (dead link) | No   |

                                                                                                                                                                                                                                                                      
### Measurement Tools

| Tool                                                                         | Description                                                                                              | Languages       | Status   | Documentation         | Working |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------|----------|-----------------------|---------|
| [mmathys/dht-crawler](https://github.com/mmathys/dht-crawler)                | Minimal BitTorrent DHT-Protocol crawler                                                                  | Javascript      | Inactive | Good (in parent repo) | ?       |
| [node-dht-peer-crawler](https://github.com/Covertness/node-dht-peer-crawler) | A fast and stable DHT crawler.                                                                           | NodeJS          | Inactive | Good                  | ?       |
| [polcak/DHT-crawler](https://www.fit.vut.cz/research/product/581/.en)        | Implementation of peer finder as part of Bachelor work.                                                  | Python 3, Shell | Inactive | Excellent             | ?       |
| [BitInsight](https://github.com/simionrobert/BitInsight)                     | Bittorrent Network Overview through Infohash Indexing, Metadata and IP visualisations of the DHT network | NodeJS          | Active   | Good                  | ?       |

## Bitcoin

### Papers on Bitcoin topology mapping

| Title                                                                                                                                                                                                                                                                             | Venue                                                                                                            | Year | Code                                                                                             | Data                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Discovering bitcoin’s public topology and influential nodes](https://www.cs.umd.edu/projects/coinscope/)                                                                                                                                                                         | University of Michigan technical report                                                                          | 2015 | [Yes](https://github.com/jameslitton/coinscope)                                                  | No                                                                                    |
| [Txprobe: Discovering bitcoin’s network topology using orphan transactions](https://arxiv.org/pdf/1812.00942.pdf)                                                                                                                                                                 | Conference on Financial Cryptography and Data Security                                                           | 2019 | No                                                                                               | No                                                                                    |
| [Btcmap: Mapping bitcoin peer-to-peer network topology](https://www.researchgate.net/profile/Varun_Deshpande8/publication/329299820_BTCmap_Mapping_Bitcoin_Peer-to-Peer_Network_Topology/links/5cbddfe4299bf1209778bdc2/BTCmap-Mapping-Bitcoin-Peer-to-Peer-Network-Topology.pdf) | IFIP/IEEE International Conference on Performance Evaluation and Modeling in Wired and Wireless Networks (PEMWN) | 2018 | No                                                                                               | No                                                                                    |
| [Timing analysis for inferring the topology of the bitcoin peer-to-peer network](https://dsn.tm.kit.edu/publications/files/323/bitcoin_timing_analysis_dsn.pdf)                                                                                                                   | IEEE SmartWorld                                                                                                  | 2016 | No                                                                                               | [Daily datasets from July 2015 until today](https://dsn.tm.kit.edu/bitcoin/data.html) |
| [All that Glitters is not Bitcoin-Unveiling the Centralized Nature of the BTC (IP) Network](https://orbi.uliege.be/bitstream/2268/243592/1/paper.pdf)                                                                                                                             | IEEE/IFIP Network Operations and Management Symposium (NOMS)                                                     | 2020 | No                                                                                               | No                                                                                    |
| [The Bitcoin peers network](http://blockchain.cs.ucl.ac.uk/wp-content/uploads/2016/11/P2PFISY2016_paper_32.pdf)                                                                                                                                                                   | Int. Workshop P2P Financial Systems                                                                              | 2016 | No                                                                                               | No                                                                                    |
| [Characterization of the topology of the Bitcoin network](https://core.ac.uk/download/pdf/288502346.pdf)                                                                                                                                                                          | Bachelor Thesis - UCL                                                                                            | 2019 | [Java Bitcoin crawler](https://github.com/GuillermoEscobero/bitcrawler/blob/master/Crawler.java) | No                                                                                    |
| [Nodes in the bitcoin network: comparative measurement study and survey.](https://ieeexplore.ieee.org/abstract/document/8703385/)                                                                                                                                                 | IEEE Access                                                                                                      | 2019 | No                                                                                               | No                                                                                    |

### Tools and Datasets on Bitcoin Topolgy

#### BitNodes

https://bitnodes.io/  

From the project description:
> Bitnodes is currently being developed to estimate the size of the Bitcoin network by finding all the reachable nodes in the network. The current methodology involves sending getaddr messages recursively to find all the reachable nodes in the network, starting from a set of seed nodes. Bitnodes uses Bitcoin protocol version 70001 (i.e. >= /Satoshi:0.8.x/), so nodes running an older protocol version will be skipped. The crawler implementation in Python is available from GitHub (ayeowch/bitnodes) and the crawler deployment is documented in Provisioning Bitcoin Network Crawler.

## BTC Crawler

https://github.com/agamble/btc-crawler

A Bitcoin network crawler in Go. Hasn't been maintained for the past 5 years.

A more recent fork: https://github.com/Kleissner/btc-crawler

## BitBus Bitcoin Crawler

https://docs.bitbus.network/

## Ethereum

1. Kim, Seoung Kyun, Zane Ma, Siddharth Murali, Joshua Mason, Andrew Miller, and Michael Bailey. "[Measuring ethereum network peers](http://joshm.web.engr.illinois.edu/imc18_ethereum.pdf)." In Proceedings of the Internet Measurement Conference 2018, pp. 91-104. 2018.

1. Gao, Yue, Jinqiao Shi, Xuebin Wang, Qingfeng Tan, Can Zhao, and Zelin Yin. "[Topology Measurement and Analysis on Ethereum P2P Network.](https://ieeexplore.ieee.org/abstract/document/8969695/?casa_token=6gYa35u6RVYAAAAA:4jUU8TG1hQLN743pZ4dUOOHB52E8s6sbqjR_FIYsHfOMrn4oUuv0C6JyQr6h8CTr8Y29iOBtgLw)" In 2019 IEEE Symposium on Computers and Communications (ISCC), pp. 1-7. IEEE, 2019.

## Filecoin