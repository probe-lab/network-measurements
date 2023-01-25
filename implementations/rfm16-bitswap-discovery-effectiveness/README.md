# RFM-16: Effectiveness of Bitswap Discovery Process

Author: [Guillaume Michel](https://github.com/guillaumemichel)

Date: 2022-12-16

This folder contains the tools and scripts that were used to generate and analyse the data of RFM-16.

## [go-bitswap/](go-bitswap)

Contains the modified bitswap implementation. [go-bitswap](https://github.com/ipfs/go-bitswap) has been modified to prevent the Bitswap session to use the DHT, and is configured to log a lot of useful information.

## [kubo/](kubo)

Contains a slightly modified version of [kubo](https://github.com/ipfs/kubo) preventing to resolve all parts of a file when a root CID is requested. Moreover, it depends on the modified [go-bitswap](go-bitswap).

## [measurements](measurements)

Contains all scripts to run the measurements.

## [plots/](plots)

Contains the scripts from the [report](../../results/rfm16-bitswap-discovery-effectiveness.md).
