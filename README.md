# IPFS Network Observatory 

## Motivation & Vision

The dynamics of public, user-run, permissionless, P2P networks are rather unpredictable due to the multiple types of applications and services that leverage them. Because they are not owned by a single user, or operated by a single entity, analysing their behavior needs to be done through (non-invasive) proxies and probes, rather than through (invasive) controls as is the case in a centralized system. Because of this hard challenge, most P2P networks put observability as a secondary goal. However, they should not!

We argue that it is this dynamicity, unpredictability and lack of central control of permissionless networks that should make measurement and observability of those systems a top priority. Measurement, observability and benchmarking of protocol and network performance is the primary means through which optimizations can be identified.

In order to promote a healthy ecosystem of protocol developers, users and businesses, where hypotheses are tested and verified through real world measurements, we envisioned the IPFS Network Observatory, a project focused on measuring all metrics and performance indicators of the Public IPFS Network. The project will not stay at high-level metrics, but instead, will dive into protocol settings in order to _identify the available space for protocol optimization as well as justify design decisions_.

We believe that having the ability to get information from the real-time performance of the network will help tremendously in both real-time decision-making (e.g., request routing and forwarding) and in long-term protocol design (e.g., best ways to populate routing tables). Depending on the metric, or protocol setting identified, the methodologies laid out here fall, largely, into two categories: i) continuous probing, or ii) on-demand monitoring.

There are numerous decentralized, P2P networks. This projoect focuses primarily on the Public IPFS Network. Follow-up iterations of the project will expand to libp2p-based networks more generally.

## How to use this repository

**RFMs:** We organize work around Requests for Measurements (RFMs). RFMs are micro-projects that individuals or teams can take up and deliver. The [RFMs](RFMs.md) document containts the proposals for measurements that have been suggested so far and will be implemented as part of the IPFS Network Observatory.

**Results:** The results of this project are reported in the form of technical reports in the [Reports](reports/) folder. Each RFM, once completed, should be accompanied by one report to document the findings.

**Get Involved:** There are two ways you can get involved:
- You can choose an RFM you want to take on from the list of existing [RFMs](RFMs.md).
- You can propose a new RFM, if the aspect of monitoring and measurement you want to work on is not on the list. In order to do this, please submit a PR to add your proposed RFM to the list of existing [RFMs](RFMs.md), using the template.
- You can propose a new RFM if you have ideas about valuable things, even if you don't have the capacity to do the actual work. RFMs will be picked up by others, based on priorities.

## Important Notes

**Open Source:** All of our work is open-source. Work associated with this project (scripts, infrastructure setup) should be open source and submitted to, or linked from this repository.

**Funding:** There will soon be funding options available to take on work related to existing or new RFMs. Get in touch if you are interested.