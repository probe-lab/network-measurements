#!/bin/sh

# kill all running ipfs instance
killall ipfs

# build kubo again
cd ../kubo
#cd ../kubo
make build
#cd ../measurements
cd ../measurements

# copy ipfs executable here
cp ../kubo/cmd/ipfs/ipfs .
