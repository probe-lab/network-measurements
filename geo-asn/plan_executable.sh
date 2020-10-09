#!/usr/bin/env bash
./start_crawl
aws s3 sync output_data_crawls/ s3://$bucketname
