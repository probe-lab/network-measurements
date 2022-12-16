# Measurements scripts

Author: [Guillaume Michel](https://github.com/guillaumemichel)

Date: 2022-12-16

This folder contains all scripts used to run measurements and analyse the data resulting from them.

## Running the measurements

```bash
./update      # compiles the modified ipfs and copies the binary in this folder
./run         # prepares removes old data files and reinitialize ipfs
./ipfs daemon # run the ipfs daemon

# in another terminal session
python requests.py # manages ipfs get requests on N threads
```

After a run, all data can be moved to a new folder in [data/](data).

## Analysing the results

[bitswap-analysis.ipynb](bitswap-analysis.ipynb) analyses the main log file `bitswap.log`. It provide useful statistics and plots about requests.

[packets-analysis.ipynb](packets-analysis.ipynb) analyses the packets log file `packets.log` containing logs for each packet sent and received by Bitswap. It provides statistics about the number of packets exchanged for each Bitswap request.