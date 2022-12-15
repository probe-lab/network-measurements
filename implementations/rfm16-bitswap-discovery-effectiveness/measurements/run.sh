#!/bin/sh

# IPFS_PATH variable env has to be set
IPFS_PATH="$HOME/.ipfs"

# kill running ipfs instances
killall ipfs
# removes the current IPFS config containing the blockstore
rm -rf $IPFS_PATH

# remove past logs
rm logs.txt
rm ipfs.log
rm bitswap.log
rm packets.log

IPFS="./ipfs"

# initializing the IPFS config files
$IPFS init
# start the ipfs daemon and write logs to txt file
$IPFS daemon

# wait for daemon to start
#sleep 2s
