## powerscale-node-site-prep-guide-feb2026::chunk_0

PowerScale Node Site Preparation and 
Planning Guide 
February 2026

Notes, cautions, and warnings
NOTE: A NOTE indicates important information that helps you make better use of your product.
CAUTION: A CAUTION indicates either potential damage to hardware or loss of data and tells you how to avoid 
the problem.
WARNING: A WARNING indicates a potential for property damage, personal injury, or death.
Copyright © 2022 - 2025 Dell Inc. All Rights Reserved. Dell Technologies, Dell, and other trademarks are trademarks of Dell Inc. or its 
subsidiaries. Other trademarks may be trademarks of their respective owners.

---

## powerscale-node-site-prep-guide-feb2026::chunk_1

for property damage, personal injury, or death. Copyright © 2022 - 2025 Dell Inc. All Rights Reserved. Dell Technologies, Dell, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

Chapter 1: Introduction................................................................................................................. 4
About this guide...................................................................................................................................................................4
Scale-out NAS overview....................................................................................................................................................4
OneFS storage architecture............................................................................................................................................. 5
Node components............................................................................................................................................................... 5
Network connectivity summary....................................................................................................................................... 7
Chapter 2: Selecting the equipment............................................................................................. 11
Safety and EMI Compliance............................................................................................................................................. 11
Grounding guidelines..........................................................................................................................................................11
Shock and vibration............................................................................................................................................................11
Storage node specifications............................................................................................................................................ 12
Racks and rails.................................................................................................................................................................... 12
Titan HD racks.................................................................................................................................................................... 13
Environmental requirements......................................................................................................................................14
Cabinet clearance.........................................................................................................................................................15
Stabilizing the casters.................................................................................................................................................15
Rail kit components for 4U systems..............................................................................................................................16
Third-party rack specifications for the deep chassis solutions.............................................................................. 19
Rail kit components for 2U systems..............................................................................................................................21
Rail kit components for 1U systems..............................................................................................................................22
Network topology..............................................................................................................................................................23
Leaf-Spine topology..........................................................................................................................................................23
Assisting with installation................................................................................................................................................ 24
Installation and implementation details.................................................................................................................. 24
Switches and cables......................................................................................................................................................... 24
Cable management......................................................................................................................................................24
Supported switches..........................................................................................................................................................26
Chapter 3: Adding functionality to the cluster.............................................................................28
Data management modules.............................................................................................................................................28
SmartQuotas.................................................................................................................................................................28
SmartDedupe................................................................................................................................................................28
Chapter 4: Preparing your facility............................................................................................... 29
Environmental requirements...........................................................................................................................................29
Power requirements................................................................................................................................................... 30
Power Requirements for Equipment.......................................................................................................................32
Radio Frequency Interference (RFI) requirements............................................................................................. 32
Hardware acclimation.................................................................................................................................................33
Air quality requirements............................................................................................................................................. 33
Site floor load-bearing requirements...................................................................................................................... 34
Shipping and storage requirements........................................................................................................................ 34
Fire suppressant disclaimer.......................................................................................................................................35
Contents
Contents
3

---

## powerscale-node-site-prep-guide-feb2026::chunk_2

your facility............................................................................................... 29 Environmental requirements...........................................................................................................................................29 Power requirements................................................................................................................................................... 30 Power Requirements for Equipment.......................................................................................................................32 Radio Frequency Interference (RFI) requirements............................................................................................. 32 Hardware acclimation.................................................................................................................................................33 Air quality requirements............................................................................................................................................. 33 Site floor load-bearing requirements...................................................................................................................... 34 Shipping and storage requirements........................................................................................................................ 34 Fire suppressant disclaimer.......................................................................................................................................35 Contents Contents 3

Introduction to this guide
This section contains the following topics:
About this guide
This guide describes how to prepare and plan for node hardware installation.
Before implementing a cluster into the data workflow, identify the best equipment and software requirements. Be sure to 
confirm that the facility is ready to support the cluster.
Table 1. Node Types 
Node
Description
A200, A2000, H400, H500, H600, F800, F810, and H5600
Gen6 (4U)
A3000 and A300
Purpose-built Archive nodes (4U)
A3100 and A310
Purpose-built Archive nodes (4U)
H7000 and H700
Purpose-built Hybrid nodes (4U)
H7100 and H710
Purpose-built Hybrid nodes (4U)
B100 and P100
Accelerator nodes (1U)
F900
All-flash nodes (2U)
F600 and F200
All-flash nodes (1U)
F210 and F710
All-flash nodes (1U)
F910
All-flash nodes (2U)
PA110
All-flash nodes (1U)
WARNING: Do not install A3000, A300 (archive nodes), H7000, or H700 (hybrid nodes) into existing Gen6 
chassis installations. The archive and hybrid nodes must only be installed in the chassis that is provided from 
the factory. The higher-powered archive and hybrid nodes can cause a fuse to open on the Gen6 chassis 
midplane, which then requires a chassis replacement.
WARNING: The storage conditions for some parts, such as Hard Disk Drives (HDDs), Solid State Drives (SSDs), 
and batteries, affect the wear and life of those parts. Do not exceed six consecutive months of unpowered 
storage from the delivery date.
The information in this guide provides a framework for the research that a System Administrator or Facility Manager must 
conduct before powering on a node.
For detailed information about the OneFS operating system, review OneFS documentation on the Online Support site.
Scale-out NAS overview
The scale-out NAS storage platform combines modular hardware with unified software to harness unstructured data. Powered 
by the OneFS operating system, a cluster delivers a scalable pool of storage with a global namespace.
The unified software platform provides centralized web-based and command-line administration to manage the following 
features:
●
A cluster that runs a distributed file system
1
4
Introduction to this guide

---

## powerscale-node-site-prep-guide-feb2026::chunk_3

delivers a scalable pool of storage with a global namespace. The unified software platform provides centralized web-based and command-line administration to manage the following features: ● A cluster that runs a distributed file system 1 4 Introduction to this guide

●
Scale-out nodes that add capacity and performance
●
Storage options that manage files and tiering
●
Flexible data protection and high availability
●
Software modules that control costs and optimize resources
OneFS storage architecture
PowerScale nodes take a scale-out approach to storage. The nodes create a cluster of nodes that run a distributed file system. 
PowerScale combines the three layers of storage architecture file system, volume manager, and data protection into a scale-out 
NAS cluster.
Each node adds resources to the cluster. Because each node contains a globally coherent RAM, as a cluster becomes larger, 
it becomes faster. Meanwhile, the file system expands dynamically and redistributes content, which eliminates the work of 
partitioning disks and creating volumes.
Nodes work as peers to spread data across the cluster. The process of segmenting and distributing data is called striping. 
This process protects data and enables users to connect to any node, which allows them to take advantage of the cluster 
performance.
PowerScale uses distributed software to scale data across commodity hardware. Primary devices do not control the cluster, 
and secondary devices do not invoke dependencies. Each node helps to control data requests, boost performance, and expand 
cluster capacity.
Node components
A cluster can expand to a maximum of 252 nodes.
A cluster is made up of 3 or more nodes if you are using Gen 6.5 hardware (PowerScale F series) nodes. If the cluster is made 
up of Gen 6 nodes (Archive, Hybrid, or Flash series) nodes, the minimum cluster configuration is 4 nodes.
If you are installing a new cluster with more than 22 nodes or if you are growing an existing cluster to include more than 22 
nodes, follow the instructions in Install a new cluster using Leaf-Spine configuration in the Leaf-Spine Cluster Installation Guide.
NOTE: OneFS supports 61TB and 122TB QLC ISE drives in any PowerScale high-density flash node solution.
There are several types of nodes that can be added to clusters to balance capacity and performance with throughput or I/O 
operations per second (IOPS).
Table 2. Nodes and Use Cases 
Node
Minimum Operating 
System Version
Description and use case
A3100 and A310
OneFS 9.11.0 and later
●
Purpose-built archive nodes (4U) require a minimum cluster 
size of four nodes.
●
Expand cluster size in two node increments.
●
The A310 has an active archive, and the A3100 has a deep 
archive.
H7100 and H710
OneFS 9.11.0 and later
●
Purpose-built hybrid nodes (4U) require a minimum cluster 
size of four nodes.
●
Expand cluster size in two node increments.
●
The H710 and H7100 are performance solutions with 
support for inline software data compression and data 
deduplication.
A3000 and A300
OneFS 9.5.1.1 and later
●
Purpose-built archive nodes (4U) require a minimum cluster 
size of four nodes.
●
Expand cluster size in two node increments.
●
The A300 has an active archive, and the A3000 has a deep 
archive.
H7000 and H700
OneFS 9.5.1.1 and later
●
Purpose-built hybrid nodes (4U) require a minimum cluster 
size of four nodes.
Introduction to this guide
5

---

## powerscale-node-site-prep-guide-feb2026::chunk_4

increments. ● The A300 has an active archive, and the A3000 has a deep archive. H7000 and H700 OneFS 9.5.1.1 and later ● Purpose-built hybrid nodes (4U) require a minimum cluster size of four nodes. Introduction to this guide 5

Table 2. Nodes and Use Cases (continued)
Node
Minimum Operating 
System Version
Description and use case
●
Expand cluster size in two node increments.
●
The H700 and H7000 are performance solutions with 
support for inline software data compression and data 
deduplication.
F200 ISE and FIPS
OneFS 9.0.0.0 and later
All-flash solution, software inline data compression, and data 
deduplication.
●
All-flash nodes (1U) require a minimum cluster size of three 
nodes.
●
Expand cluster size in single node increments.
F600
●
F600 with SED, the 
minimum operating 
system version is 
OneFS 9.3.0.0.
●
F600 with Quad-
Level Cell (QLC), the 
minimum operating 
system version is 
OneFS 9.4.0.0.
●
F600 with QLC 
SEDs, the minimum 
operating system 
version is OneFS 
9.4.0.8.
●
F600 with non-
QLC and non-SED 
drives, the minimum 
operating system 
version is OneFS 
9.0.0.0.
All-flash solution, software inline data compression, and data 
deduplication.
●
All-flash nodes (1U) require a minimum cluster size of three 
nodes.
●
Expand cluster size in a single node increments.
F210 and F710 with ISE, FIPS, and 
SED
OneFS 9.7.0.0
●
All-flash nodes (1U) require a minimum cluster size of three 
nodes.
●
Expand cluster size in a single node increments.
PowerScale F800 and F810
OneFS 9.0.0.0 and later
All-flash solution, fast data access using direct-attached 
NVMe (Non-Volatile Memory Express) SSD Serial Attached 
SCSI (SAS) drives with integrated parallelism. Hardware data 
compression and data deduplication on the F810.
PowerScale F900
OneFS 9.2.0.0 and later 
releases.
●
OneFS F900 with 
Instant Secure Erase 
(ISE) and SEDs: 
9.3.0.0.
●
OneFS F900 with 
QLC: 9.4.0.0.
●
OneFS F900 with 
QLC SEDs: 9.4.0.8.
All-flash solution, fast data access using direct-attached 
NVMe SSDs with integrated parallelism. Software inline data 
compression and data deduplication on the F900.
●
All-flash node (2U) requires a minimum cluster size of three 
nodes.
●
Expand cluster size in single node increments.
F910 with ISE, SED, and FIPS
OneFS 9.8.0.0
●
All-flash node (2U) requires a minimum cluster size of three 
nodes.
●
Expand cluster size in single node increments.
Isilon Hardware H-Series
OneFS 9.0.0.0 and later
●
The H600 is a performance spinning solution.
●
The H400 and H500 have capacity performance.
●
The H5600 has a larger capacity performance.
The following Dell PowerScale nodes improve performance:
6
Introduction to this guide

---

## powerscale-node-site-prep-guide-feb2026::chunk_5

OneFS 9.0.0.0 and later ● The H600 is a performance spinning solution. ● The H400 and H500 have capacity performance. ● The H5600 has a larger capacity performance. The following Dell PowerScale nodes improve performance: 6 Introduction to this guide

Table 3. Accelerator Nodes 
Node
Function
B100
Provides the ability to backup OneFS powered clusters 
through two-way NDMP protocol.
P100
Adds performance to a cluster that is composed of nodes that 
are CPU-bound.
PA110
●
Adds performance to a cluster that is composed of nodes 
that are CPU-bound.
●
Provides the ability to backup OneFS powered cluster 
through two-way NDPM protocol
Software Data Reduction solutions supported in OneFS are enabled by default on most PowerScale nodes.
Table 4. Supported Configurations for OneFS Data Reduction 
Gen6 nodes
PowerScale nodes
PowerScale nodes
Data Reduction Enabled
A200
A300/L
A310/L
False
A2000
A3000/L
A3100/L
False
H400
A300
A310
False
H500
H700
H710
False
H5600
H7000
H7100
True
A200
-
A310
False
-
A300
A310
True
H400
-
A310
False
A2000
-
A3100
False
-
A3000
A3100
True
H500
-
H710
False
-
H700
H710
True
H5600
-
H7100
True
-
H7000
H7100
True
Network connectivity summary
NOTE: Access to the 1 GbE Management ports for F200, F600, and F900 requires OneFS version 9.4.0.3 or later. If the 
nodes were shipped with an older OneFS version, a one-time configuration change could enable management port access 
even if the node is upgraded to OneFS 9.4.0.3 or later. However, 1 GbE Management ports are not available on F200 nodes 
that were obtained before 6 December 2022.
The F210, F710, F910, and PA110 use the LAN on Motherboard (LOM) management ports .
The OneFS CLI Reference Guide provides information to check node status.
Table 5. Network connectivity summary 
Node
Frontend NIC
Transceiver
Backend
Management port
Ethernet
InfiniBand
PA110
100 GbE QSFP28
100 GbE
100/40 GbE 
QSFP28
200 Gb QSFP 56
1 GbE LOM card
40 GbE
Introduction to this guide
7

---

## powerscale-node-site-prep-guide-feb2026::chunk_6

node status. Table 5. Network connectivity summary Node Frontend NIC Transceiver Backend Management port Ethernet InfiniBand PA110 100 GbE QSFP28 100 GbE 100/40 GbE QSFP28 200 Gb QSFP 56 1 GbE LOM card 40 GbE Introduction to this guide 7

Table 5. Network connectivity summary (continued)
Node
Frontend NIC
Transceiver
Backend
Management port
Ethernet
InfiniBand
25/10 GbE SFP28
25 GbE
10 GbE
P100
100 GbE QSFP28
100 GbE
100/40 GbE 
QSFP28
40 Gb QSFP+
1 GbE rNDC
40 GbE
25/10 GbE SFP28
25 GbE
10 GbE
F910
100 GbE QSFP28
100 GbE
100/40 GbE 
QSFP28
200 Gb QSFP 56
1 GbE LOM card
40 GbE
25/10 GbE 
QSFP28
25 GbE
10 GbE
F900
100 GbE QSFP28
100 GbE
100/40 GbE 
QSFP28
40 Gb QSFP+
1 GbE rNDC
40 GbE
25/10 GbE SFP28
25 GbE
10 GbE
F710
100 GbE QSFP28
100 GbE
100/40 GbE 
QSFP28
200 Gb QSFP 56
1 GbE LOM card
40 GbE
25/10 GbE SFP28
25 GbE
10 GbE
F600
100 GbE QSFP28
100 GbE
100/40 GbE 
QSFP28
40 Gb QSFP+
1 GbE rNDC
40 GbE
25/10 GbE SFP28
25 GbE
10 GbE
F210
100 GbE QSFP28
100 GbE
25/10 GbE SFP28
200 Gb QSFP 56
1 GbE LOM card
40 GbE
25/10 GbE SFP28
25 GbE
10 GbE
F200
100/25/10 GbE 
SFP28
25 GbE
100/25/10 GbE 
SFP28
40 Gb QSFP+
1 GbE rNDC
10 GbE
F800
40 GbE QSFP+
40 GbE
40 GbE QSFP+
40 Gb QDR 
QSFP+
A single management 
port, a shared port 
with the BMC
25/10 GbE SFP28
25 GbE
10 GbE SFP+
10 GbE
F810
40 GbE QSFP+
40 GbE
40 GbE QSFP+
N/A
A single management 
port, a shared port 
with the BMC
25/10 GbE SFP28
25 GbE
10 GbE SFP+
10 GbE
H700
100/40 GbE 
QSFP28
100 GbE
100/40 GbE 
QSFP28
40 Gb QDR 
QSFP+
A single management 
port, a shared port 
with the BMC
40 GbE
8
Introduction to this guide

---

## powerscale-node-site-prep-guide-feb2026::chunk_7

25/10 GbE SFP28 25 GbE 10 GbE SFP+ 10 GbE H700 100/40 GbE QSFP28 100 GbE 100/40 GbE QSFP28 40 Gb QDR QSFP+ A single management port, a shared port with the BMC 40 GbE 8 Introduction to this guide

Table 5. Network connectivity summary (continued)
Node
Frontend NIC
Transceiver
Backend
Management port
Ethernet
InfiniBand
25/10 GbE SFP28
25 GbE
25/10 GbE SFP28
10 GbE
H7000
100/40 GbE 
QSFP28
100 GbE
100/40 GbE 
QSFP28
40 Gb QDR 
QSFP+
A single management 
port, a shared port 
with the BMC
40 GbE
25/10 GbE SFP28
25 GbE
25/10 GbE SFP28
10 GbE
H400
25/10 GbE SFP28
25 GbE
10 GbE SFP+
10 Gb QDR QSFP+
A single management 
port, a shared port 
with the BMC
10 GbE
10 GbE SFP+
10 GbE
H500
40 GbE QSFP+
40 GbE
40 GbE QSFP+
40 Gb QDR 
QSFP+
A single management 
port, a shared port 
with the BMC
25/10 GbE SFP28
25 GbE
10 GbE
10 GbE SFP+
10 GbE
H5600
40 GbE QSFP+
40 GbE
40 GbE QSFP+
40 Gb QDR 
QSFP+
A single management 
port, a shared port 
with the BMC
25/10 GbE SFP28
25 GbE
10 GbE
10 GbE SFP+
10 GbE
H600
40 GbE QSFP+
40 GbE
40 GbE QSFP+
40 Gb QDR 
QSFP+
A single management 
port, a shared port 
with the BMC
25/10 GbE SFP28
25 GbE
10 GbE
10 GbE SFP+
10 GbE
B100
100 GbE QSFP28
100 GbE
100/40 GbE 
QSFP28
40 Gb QSFP+
1 GbE rNDC
40 GbE
25/10 GbE SFP28
25 GbE
10 GbE
A300
100/40 GbE 
QSFP28
100 GbE
100/40 GbE 
QSFP28
40 Gb QDR 
QSFP+
A single management 
port, a shared port 
with the BMC
40 GbE
25/10 GbE SFP28
25 GbE
25/10 GbE SFP28
10 GbE
A3000
100/40 GbE 
QSFP28
100 GbE
100/40 GbE 
QSFP28
40 Gb QDR 
QSFP+
A single management 
port, a shared port 
with the BMC
40 GbE
25/10 GbE SFP28
25 GbE
25/10 GbE SFP28
10 GbE
A200
25/10 GbE SFP28
25 GbE
10 GbE SFP+
10 Gb QDR QSFP+
A single management 
port, a shared port 
with the BMC
10 GbE
10 GbE SFP+
10 GbE
Introduction to this guide
9

---

## powerscale-node-site-prep-guide-feb2026::chunk_8

25/10 GbE SFP28 10 GbE A200 25/10 GbE SFP28 25 GbE 10 GbE SFP+ 10 Gb QDR QSFP+ A single management port, a shared port with the BMC 10 GbE 10 GbE SFP+ 10 GbE Introduction to this guide 9

Table 5. Network connectivity summary (continued)
Node
Frontend NIC
Transceiver
Backend
Management port
Ethernet
InfiniBand
A2000
25/10 GbE SFP28
25 GbE
10 GbE SFP+
10 Gb QDR QSFP+
A single management 
port, a shared port 
with the BMC
10 GbE
10 GbE SFP+
10 GbE
10
Introduction to this guide

---

## powerscale-node-site-prep-guide-feb2026::chunk_9

Backend Management port Ethernet InfiniBand A2000 25/10 GbE SFP28 25 GbE 10 GbE SFP+ 10 Gb QDR QSFP+ A single management port, a shared port with the BMC 10 GbE 10 GbE SFP+ 10 GbE 10 Introduction to this guide

Selecting the equipment
The requirements for mixed-node clusters section in the OneFS Supportability and Compatibility Guide provides information on 
installing more than one type of node in a cluster.
Talk to a Sales Account Manager to identify the equipment that is best suited to support your workflow.
Safety and EMI Compliance
This IT Equipment is compliant with the electromagnetic compatibility (EMC) and product safety regulations/standards required 
by the countries in which the product is sold. Compliance is based on FCC part 15, CISPR22/CISPR24 and EN55022/EN55024 
standards, including applicable international variations.
EMC compliant Class A products are marketed for use in business, industrial, and commercial environments. Product Safety 
compliance is based on IEC 62368-1 and EN 62368-1 standards, including applicable national deviations.
This IT Equipment is in compliance with EU RoHS Directive 2011/65/EU.
The devices that are used in this product are approved under a unique regulatory model identifier. The regulatory model that is 
affixed to each device rating label may differ from any marketing or product family name in this data sheet.
For more information, go to the Dell Support Site.
Grounding guidelines
To eliminate shock hazards and facilitate the operation of circuit-protective devices, ensure that the rack is grounded.
●
The rack must have an earth-ground connection as required by applicable codes. Connections such as a grounding rod or 
building steel provide an earth ground.
●
The electrical conduits must be made of rigid metallic material that is securely connected or bonded to panels and electrical 
boxes, which provides continuous grounding.
●
The ground must have the correct low impedance to prevent buildup of voltage on equipment or exposed surfaces. Low-
impedance grounding and lightning protection are recommended.
●
The electrical system must meet local and national code requirements. Local codes might be more stringent than 
national codes. Site floor load-bearing requirements and Safety and EMI Compliance sections in this manual provide more 
information.
Shock and vibration
Products have been tested to withstand the shock and random vibration levels.
The levels apply to all three axes and should be measured with an accelerometer on the equipment enclosures within the cabinet 
and shall not exceed any of the values in this table.
Table 6. Platform Response Levels 
Platform condition
Response measurement level
Nonoperational shock
25 Gs for 3-milliseconds
Operational shock
6 Gs for 11-milliseconds
Nonoperational random vibration
0.40 Grms at 5-500 Hz for 30 minutes
Operational random vibration
0.21 Grms at a frequency range between 5-500 Hz for 10 
minutes
2
Selecting the equipment
11

---

## powerscale-node-site-prep-guide-feb2026::chunk_10

Gs for 3-milliseconds Operational shock 6 Gs for 11-milliseconds Nonoperational random vibration 0.40 Grms at 5-500 Hz for 30 minutes Operational random vibration 0.21 Grms at a frequency range between 5-500 Hz for 10 minutes 2 Selecting the equipment 11

Systems that are mounted on an approved package have completed transportation testing to withstand shock and vibrations in 
the vertical direction only. The levels shall not exceed the values in this table.
Table 7. Packaged System Measurement Levels 
Packaged system condition
Response measurement level
Transportation shock
10 Gs for 12-milliseconds
Transportation random vibration
0.28 Grms at a frequency range between 1-100 Hz for 4 hours
Storage node specifications
To verify specifications for the A200, A2000, A300, A3000, H400, H500, H5600, H600, H700, H7000, F910, F900, F810, F800, 
F710, F600, F210, and F200 nodes, review these technical specifications sheets.
NOTE: NVMe FIPS SED drive support was added for F600 and F900 nodes in OneFS 9.3.0.0. Downgrading nodes with 
these drives to an earlier OneFS version renders them inoperable.
NOTE: OneFS version must be 9.4.0.8 or later for 15TB/30TB QLC SED non-FIPS drives for F600 and F900, or the node 
might not be able to join the cluster. Downgrading nodes with these drives to an earlier OneFS version renders them 
inoperable.
NOTE: OneFS 9.8.0.0 is required for the F910 node. Downgrading nodes with these drives to an earlier OneFS version 
renders them inoperable.
●
Dell PowerScale Archive Family
●
Dell PowerScale Hybrid Family
●
Dell PowerScale All Flash Family
●
Dell PowerScale Accelerator Nodes
Racks and rails
You can secure nodes to standard storage racks with a sliding rail system.
For specific information about the rail solutions compatible with your system, see the Dell Enterprise Systems Rail Sizing and 
Rack Compatibility Matrix available at Dell Technologies Enterprise Systems Rail Sizing and Rack Compatibility Matrix.
For Generation 6 and PowerScale Archive and Hybrid nodes, rail kits are included in all node packaging and are compatible with 
racks with the following types of holes:
●
3/8-inch square holes
●
9/32-inch round holes
●
10-32, 12-24, M5X.8, or M6X1 prethreaded holes
Rail kit mounting brackets adjust in length from 60 cm to 90 cm (24 to 36 inches) to accommodate different rack depths. When 
you select a rack for your nodes, ensure that the rack supports the minimum and maximum rail kit sizes.
Titan HD rail kits can support NEMA spacing 60 cm or 73 cm (24 or 29 inches).
NOTE: Arista switches are incompatible with the Titan S rack.
Table 8. Rack solutions per node type 
Node type
Rack type
●
A300 (standard chassis)
●
A3000 (deep chassis and requires Titan HD)
●
H700 (standard chassis)
●
H7000 (deep chassis and requires Titan HD)
●
A310
●
A3100
●
H710
●
H7100
The following racks with the adequate cable, door, or Power 
Distribution Unit (PDU) clearance:
●
Titan D
●
Titan HD
●
Titan S
12
Selecting the equipment

---

## powerscale-node-site-prep-guide-feb2026::chunk_11

chassis and requires Titan HD) ● A310 ● A3100 ● H710 ● H7100 The following racks with the adequate cable, door, or Power Distribution Unit (PDU) clearance: ● Titan D ● Titan HD ● Titan S 12 Selecting the equipment

Table 8. Rack solutions per node type 
Node type
Rack type
●
F910
●
F900
●
F710
●
F600
●
F210
●
F200
●
P100
●
B100
●
PA110
Table 9. Rack dimensions 
Rack type
Dimensions from the front bezel to the rear door
Titan
24 in W x 39 in D x 40U H
Titan D
24 in W x 44 in D x 40U H
Titan HD
28 in W x 48 in D x 42U H
Titan S
600 mm (23.6 inches) W x 45.2 in D x 42U H
NOTE: The depth that is listed in the table is from the front bezel to the rear door. For more depth, it must be 
approximately 50 mm–60 mm (2 inches-2.5 inches) from the front bezel to the rear door.
Titan HD racks
Titan HD is designed to support fully populated racks of A3000, A2000, H7000, and H5600 chassis/nodes. However, all 
PowerScale and Generation 6 platforms can be installed in the Titan HD racks.
Titan HD PDU jumper locations
The following images illustrate the PDU jumper locations for the Titan-HD PDU. The jumpers should be in J1, J3, and J5 as 
shown in the images.
Figure 1. Single phase PDU
Selecting the equipment
13

Figure 2. 3 phase Delta PDU
Figure 3. 3 Phase Wye PDU
Environmental requirements
Table 10. Titan HD environmental requirements 
Environmental symbol
Environmental requirements
+15°C to +32°C (59°F to 89.6°F) site temperature. A fully 
configured cabinet can produce up to 40,000 BTUs per hour.
40% to 55% relative humidity is the recommended operating 
parameter.
14
Selecting the equipment

---

## powerscale-node-site-prep-guide-feb2026::chunk_12

environmental requirements Environmental symbol Environmental requirements +15°C to +32°C (59°F to 89.6°F) site temperature. A fully configured cabinet can produce up to 40,000 BTUs per hour. 40% to 55% relative humidity is the recommended operating parameter. 14 Selecting the equipment

Table 10. Titan HD environmental requirements (continued)
Environmental symbol
Environmental requirements
NOTE: Contents of the cabinet might be qualified outside 
these limits. The product-specific documentation for the 
system specifications provides complete details.
The Titan HD cabinet weighs 249.48 KG (550 pounds). A 
cabinet that is fully configured with Dell products can weigh 
approximately 1,497 kg (3300 pounds).
NOTE: Ensure that the flooring can safely support 
the configuration. Calculate the minimum load-bearing 
requirements for the site by using the product-specific 
weights for the system components at Power Calculator.
0–2439 meters (0 ft–8,000 ft) above sea level operating 
altitude.
LAN and telephone connections for remote service and 
system operation.
Cabinet clearance
This Dell Technologies cabinet ventilates from front to back. Provide adequate clearance to service and cool the system. 
Depending on component-specific connections within the cabinet, the available power cable length might be shorter than the 
15-foot standard.
Stabilizing the casters
The cabinet bottom includes four caster wheels. The front wheels are fixed, and the two rear casters swivel in a 8.25 cm (3.25 
in.) diameter. The swivel position of the caster wheels determines the load-bearing points on the site floor, but does not affect 
the cabinet footprint. Once you have positioned, leveled, and stabilized the cabinet, the four leveling feet determine the final 
load-bearing points on the site floor.
Cabinet specifications provide details about cabinet dimensions and weight information to plan for system installation at the 
customer site.
Selecting the equipment
15

---

## powerscale-node-site-prep-guide-feb2026::chunk_13

and stabilized the cabinet, the four leveling feet determine the final load-bearing points on the site floor. Cabinet specifications provide details about cabinet dimensions and weight information to plan for system installation at the customer site. Selecting the equipment 15

NOTE: For installations that require a top of the cabinet power feed, a 3 m (118 in.) extension cord is provided. Do not 
move or invert the PDUs.
The table provides cabinet load-rating information.
Table 11. Cabinet load specifications 
Load Type
Casters
Rating
Dynamic
Yes
1,497 kg (3,300 lb) of equipment
Static
No
1,497 kg (3,300 lb) of equipment
More information can be found in the Site floor load-bearing requirements section in Environmental requirements. In addition, 
the pallets that are used to ship cabinets are engineered to withstand the added weight of components that are shipped in the 
cabinet.
Figure 4. Cabinet component dimensions
Rail kit components for 4U systems
Install the adjustable 4U chassis rails in the rack for Generation 6, A3000, A300, H7000, and H700 nodes.
About this task
You can install your 4U chassis in standard ANSI/EIA RS310D 48 cm (19 in.) rack systems, including all Dell EMC racks. The rail 
kit is compatible with rack cabinets with the following hole types.
16
Selecting the equipment

---

## powerscale-node-site-prep-guide-feb2026::chunk_14

this task You can install your 4U chassis in standard ANSI/EIA RS310D 48 cm (19 in.) rack systems, including all Dell EMC racks. The rail kit is compatible with rack cabinets with the following hole types. 16 Selecting the equipment

●
3/8-inch square holes
●
9/32-inch round holes
●
10-32, 12-24, M5X.8, or M6X1 prethreaded holes
The rails adjust in length from 60 cm to 90 cm (24 inches to 36 inches) to accommodate various cabinet depths. The rails are 
not left-specific or right-specific and can be installed on either side of the rack.
NOTE: Check the depth of the racks to ensure that they fit the depth of the chassis being installed.
The two rails are packaged separately inside the chassis shipping container.
Steps
1.
Separate a rail into front and back pieces.
Pull up on the locking tab, and slide the two sections of the rail apart.
2. Remove the mounting screws from the back section of the rail.
The back section is the thinner of the two rail sections. There are three mounting screws that are attached to the back 
bracket. There are also two smaller alignment screws. Do not uninstall the alignment screws.
Selecting the equipment
17

3. Attach the back section of the rail to the rack with the three mounting screws.
Ensure that the locking tab is on the outside of the rail.
4. Remove the mounting screws from the front section of the rail.
The front section is the wider of the two rail sections. There are three mounting screws that are attached to the front 
bracket. There are also two smaller alignment screws. Do not uninstall the alignment screws.
5. Slide the front section of the rail onto the back section that is secured to the rack.
18
Selecting the equipment

---

## powerscale-node-site-prep-guide-feb2026::chunk_15

attached to the front bracket. There are also two smaller alignment screws. Do not uninstall the alignment screws. 5. Slide the front section of the rail onto the back section that is secured to the rack. 18 Selecting the equipment

6. Adjust the rail until you can insert the alignment screws on the front bracket into the rack.
7.
Attach the front section of the rail to the rack with only two of the mounting screws.
Attach the mounting screws in the holes between the top and bottom alignment screws. You will install mounting screws in 
the top and bottom holes after the chassis is installed, to secure the chassis to the rack.
8. Repeat these steps to install the second rail in the rack.
Third-party rack specifications for the deep chassis 
solutions
The A3000, H7000, A2000, and H5600 are deep chassis nodes and can use the third-party rack solution.
The current Dell rack solutions support up to eight PDUs, including four on each side. The figures provide the dimensions and 
guidelines for third-party rack solutions. The table lists the components and dimensions for the labels in the figures.
Selecting the equipment
19

Figure 5. Rear-facing rack
Figure 6. Center-facing rack
20
Selecting the equipment

---

## powerscale-node-site-prep-guide-feb2026::chunk_16

The figures provide the dimensions and guidelines for third-party rack solutions. The table lists the components and dimensions for the labels in the figures. Selecting the equipment 19 Figure 5. Rear-facing rack Figure 6. Center-facing rack 20 Selecting the equipment

Table 12. Third-party rack components and dimensions 
Rack component label
Description
a
Distance between the front surface of the rack and the front 
NEMA rail
b
Distance between NEMA rails, minimum=609.6 mm (24 
inches), max=863.6 mm (34 inches)
c
Distance between the rear of the chassis to the rear of the 
rack, min=58.42 mm (2.3 inches)
d
Distance between inner front of the front door and the NEMA 
rail, min=63.5 mm (2.5 inches)
e
Distance between the inside of the rear post and the rear 
vertical edge of the chassis and rails, min=63.5 mm (2.5 
inches)
f
Width of the rear rack post
g
486.2 mm (19 inches)+(2e), min=609.6 mm (24 inches)
h
486.2 mm (19 inches), NEMA+(2e)+(2f)
NOTE: 
●
Width of the PDU+13 mm (0.5 inches) <=e+f
●
If j=i+c+PDU depth+76.2 mm (3 inches), then h=min 
600 mm (23.6 inches)
Assuming the PDU is mounted beyond i+c.
i
Chassis depth:
●
Normal chassis=909 mm (35.80 inches)
●
Deep chassis=1026 mm (40.40 inches )
NOTE: 
●
The inner rail is fixed at 921 mm (36.25 inches).
●
Allow up to 155 mm (6 inches) for cable bend radius 
when routing up to 32 cables to one side of the rack.
●
Select the greater of the installed equipment.
j
Minimum rack depth=i+c
k
Front
l
Rear
m
Front door
n
Rear door
p
Rack post
q
PDU
r
NEMA
s
NEMA 486.2 mm (19 inches)
t
Rack top view
u
Distance from front NEMA to chassis face.
Rail kit components for 2U systems
The sliding rail assemblies are used to secure the node in the cabinet. The sliding rail assembly extends it from the cabinet 
so that the system cover can be removed to access the internal field replaceable units (FRU). The 2U sliding rail assembly is 
Selecting the equipment
21

---

## powerscale-node-site-prep-guide-feb2026::chunk_17

the node in the cabinet. The sliding rail assembly extends it from the cabinet so that the system cover can be removed to access the internal field replaceable units (FRU). The 2U sliding rail assembly is Selecting the equipment 21

used for installation of the F900 and F910 nodes. Complete installation information is contained in the PowerScale F900 Node 
Installation Guide and Dell PowerScale F910 Installation Guide.
Figure 7. Sliding rail assembly - 2U systems
Rail kit components for 1U systems
The sliding rail assemblies are used to secure the node in the cabinet. They extend from the cabinet so that the system cover 
can be removed to access the internal field replaceable units (FRU). The 1U sliding rail assembly is used to install the F200, 
F210, F600, F710, B100, and P100 nodes.
Figure 8. Sliding rail assembly - 1U systems
1. sliding rail (2)
2. velcro strap (2)
3. screw (4)
4. washer (4)
22
Selecting the equipment

---

## powerscale-node-site-prep-guide-feb2026::chunk_18

assembly is used to install the F200, F210, F600, F710, B100, and P100 nodes. Figure 8. Sliding rail assembly - 1U systems 1. sliding rail (2) 2. velcro strap (2) 3. screw (4) 4. washer (4) 22 Selecting the equipment

Network topology
External networks connect the cluster to the outside world.
NOTE: Do not use the 1 GbE ports on nodes for data services, such as AV scanning, replication, data access, and so on. 
Use of the 1 GbE ports often results in errors and issues.
Subnets can be used in external networks to manage connections more efficiently. Specify the external network subnets 
depending on the topology of the network.
In a basic network topology in which each node communicates to clients on the same subnet, only one external subnet is 
required.
More complex topologies require several different external network subnets. For example, nodes that connect to one external IP 
subnet, nodes that connect to a second IP subnet, and nodes that do not connect externally. Configure the default external IP 
subnet by using IPv4.
External networks provide communication outside the cluster. OneFS supports network subnets, IP address pools, and network 
provisioning rules to facilitate the configuration of external networks.
The node specifications section in this guide provides details on frontend and backend networking options.
NOTE: InfiniBand is supported for A300, A3000, H700, H7000, F900, F600, F200, B100, P100, F210, F710, and F910 nodes.
To configure the cluster, set up an internal network. Then set up a failover network for correct cluster operation.
CAUTION: Information that is exchanged on the backend network is not encrypted. Connecting third-party 
devices to the backend switch creates a security risk.
Leaf-Spine topology
OneFS 9.0.0.0 and later releases support Leaf-Spine network topology for internal networks that communicate with the 
nodes to form clusters up to 252 nodes. For large clusters that are intended to grow over time, the Leaf-Spine topology is 
recommended. For small clusters with fewer than 30 nodes, a flat or Top of Rack (TOR) topology is recommended.
Architecture
In a Leaf-Spine topology, Dell Z9264-ON, Z9100-ON, and S5232-ON switches are arranged in a two-level hierarchy. Leaf 
switches are connected to the top-level switches called Spine switches to provide connectivity for all the nodes in the cluster. 
The Leaf switches are not connected to each other. OneFS requires two independent Leaf-Spine networks for intracluster 
communication. These networks are known as Int-A and Int-B respectively.
NOTE: 
Leaf only configurations are limited to one switch per fabric.
See Dell PowerSwitch specifications:
●
Dell PowerSwitch S5232-ON
●
Dell PowerSwitch Z9264-ON
●
Dell PowerSwitch Z9664F-ON
NOTE: Only supported on flat or TOR topology.
NOTE: 
Mixing of S5232, Z9100, Z9264, and Z9664F-ON switches are supported in a Leaf and Spine architecture. However, it 
requires that all switches run a version of the Dell Networking Operating System (DNOS) qualified by PowerScale. Before 
introducing an S5232 switch into an existing fabric, ensure that all switches are upgraded to the latest PowerScale-qualified 
DNOS version. For the most current list of DNOS versions qualified by PowerScale, see the following Dell Knowledge Base 
article: KB 000195220.
Selecting the equipment
23

---

## powerscale-node-site-prep-guide-feb2026::chunk_19

into an existing fabric, ensure that all switches are upgraded to the latest PowerScale-qualified DNOS version. For the most current list of DNOS versions qualified by PowerScale, see the following Dell Knowledge Base article: KB 000195220. Selecting the equipment 23

Assisting with installation
Contact an Account Manager for help with planning the best workflow for your environment.
Installation and implementation details
Three to four weeks before the installation date, the Professional Services team helps to gather the information necessary to 
configure the cluster.
The project team helps to complete the Configuration Guide worksheet that documents technical details that are needed for the 
installation and implementation of the cluster.
Be prepared to discuss the following information with the project team:
●
Data workflow, including the role of the cluster in that workflow. Some examples consist of production, test, or disaster 
recovery.
●
The OneFS version to install on the cluster.
●
Network connectivity details, including IP ranges for the client and networks.
●
The Domain Name Service (DNS) configuration details, including name servers and search lists.
●
The directory services, such as Active Directory, Lightweight Directory Access Protocol (LDAP), Network Information 
System (NIS), or local user groups.
●
File sharing protocols, such as SMB and Network File System (NFS) and advanced file sharing options such as File Transfer 
Protocol (FTP) and HTTP.
●
The data protection levels, anti-virus solutions, and Network Data Management Protocol (NDMP) backup.
●
Cluster alert solutions, such as SupportIQ and Simple Network Management Protocol (SNMP) monitoring.
Switches and cables
Select network switches and cables that are compatible with the nodes that support the network topology.
Use compliant Dell switches and cables. A complete list of qualified switches and cables is in the PowerScale OneFS 
Supportability and Compatibility Guide.
For frontend switches minimum specifications, see the relevant hardware and PowerScale OneFS operating system 
documentation. Separate switches are required for the frontend and backend interfaces.
●
Nonblocking fabric switch
●
Minimum of 1 MB per port of packet buffer memory
●
Support for jumbo frames
InfiniBand is supported for the backend traffic, which is also called internal traffic on most nodes that are listed in Node 
Components.
CAUTION: Information that is exchanged on the backend network is not encrypted. Connecting third-party 
nodes to the backend switch creates a security risk.
Cable management
To protect the cable connections, organize cables for proper airflow around the cluster, and to ensure fault-free maintenance of 
the nodes.
Protect cables
NOTE: The management port is designed to handle SSH and WebUI traffic only. The management port is not designed nor 
intended for frontend (data) traffic.
Damage to the cables can affect the cluster performance. Consider the following to protect cables and cluster integrity:
24
Selecting the equipment

---

## powerscale-node-site-prep-guide-feb2026::chunk_20

handle SSH and WebUI traffic only. The management port is not designed nor intended for frontend (data) traffic. Damage to the cables can affect the cluster performance. Consider the following to protect cables and cluster integrity: 24 Selecting the equipment

●
Never bend cables beyond the recommended bend radius. The recommended bend radius for any cable is at least 10–12 
times the diameter of the cable. For example, if a cable is 1.6 inches, round up to 2 inches and multiply by 10 for an 
acceptable bend radius. Cables differ, so follow the recommendations of the cable manufacturer.
●
As illustrated in the following figure, the most important design attribute for bend radius consideration is the Minimum-mated 
cable clearance (Mmcc). Mmcc is the distance from the bulkhead of the chassis through the mated connectors or strain 
relief including the depth of the associated 90-degree bend. Multimode fiber has many modes of light (fiber optic) traveling 
through the core. As each of these modes moves closer to the edge of the core, light and the signal may be reduced, 
especially if the cable is bent. In a traditional multimode cable, as the bend radius is decreased, the amount of light that leaks 
out of the core increases, and the signal decreases.
Figure 9. Cable design
●
Keep cables away from sharp edges or metal corners.
●
Never bundle network cables with power cables. If network and power cables are not bundled separately, Electromagnetic 
Interference (EMI) can affect the data stream.
●
When bundling cables, do not pinch or constrict the cables.
●
Avoid using ZIP ties to bundle cables, instead use velcro hook-and-loop ties that do not have hard edges, and can be 
removed without cutting. Fastening cables with velcro ties also reduces the impact of gravity on the bend radius.
NOTE: Gravity decreases the bend radius and results in the loss of light (fiber optic), signal power, and quality.
●
For overhead cable supports:
○
Ensure that the supports are anchored adequately to withstand the significant weight of bundled cables. Anchor cables 
to the overhead supports, then again to the rack to add a second point of support.
○
Do not let cables sag through gaps in the supports. Gravity can stretch and damage cables over time. You can anchor 
cables to the rack with velcro ties at the midpoint of the cables to protect your cable bundles from sagging.
○
Place drop points in the supports that allow cables to reach racks without bending or pulling.
●
If the cable is running from overhead supports or from underneath a raised floor, be sure to include vertical distances when 
calculating necessary cable lengths.
●
See Dell Networking Transceivers and Cables for additional information.
Ensure airflow
Bundled cables can obstruct the movement of conditioned air around the cluster.
●
Secure cables away from fans.
●
To keep conditioned air from escaping through cable holes, employ flooring seals or grommets.
Selecting the equipment
25

---

## powerscale-node-site-prep-guide-feb2026::chunk_21

information. Ensure airflow Bundled cables can obstruct the movement of conditioned air around the cluster. ● Secure cables away from fans. ● To keep conditioned air from escaping through cable holes, employ flooring seals or grommets. Selecting the equipment 25

Prepare for maintenance
To accommodate future work on the cluster, design the cable infrastructure. Think ahead to required tasks on the cluster, such 
as locating specific pathways or connections, isolating a network fault, or adding and removing nodes and switches.
●
Label both ends of every cable to denote the node or switch to which it should connect.
●
Leave a service loop of cable behind nodes. Service technicians can slide a node out of the rack without pulling on power or 
network connections. For Generation 6 nodes, you can slide any of the four nodes out of the chassis without disconnecting 
any cables from the other three nodes.
WARNING: If adequate service loops are not included during installation, downtime might be required to add 
service loops later.
●
Allow for future expansion without the need for tearing down portions of the cluster.
Supported switches
Switches ship with the proper rails or tray to install the switch in the rack.
These internal network switches ship with rails to install the switch. The switch rails are adjustable to fit NEMA front rail to rear 
rail spacing ranging from 22 in. to 34 in. See Dell PowerSwitch specifications:
●
Dell PowerSwitch S4100-ON
●
Dell PowerSwitch S5232-ON
●
Dell PowerSwitch Z9264-ON
●
Dell PowerSwitch Z9664F-ON
Table 13. Arista 7308X3 Chassis Switch 
Switch
Maximum 
number of 
connections
Network
Description
Arista 
7308X3
7300X3-32C 
(32 100 Gb 
ports) and 
7300X3-48YC4 
(48 25 Gb 
ports) line cards
252x100 GbE, 252x10/25GbE
The Arista 7308X3 switch is a modular system that can scale up 
to 8 slots with a choice of 10/25 GbE and 100 GbE line cards.
Table 14. Z9664F-ON Ethernet Switch 
Switch
Maximum 
number of 
connections
Network
Description
Z9664F-
ON
252-port
64 ports of 400 GbE in 
QSFP56-DD form factor or 
252 ports of 100 GbE in a 
2RU design, and can be used 
as a 10/25/40/50/100/200 
switch for a maximum of 252 
ports (with breakout cables).
The Z9664F-ON is a fixed 2RU aggregation switch. Breakout 
cables are only used in the odd-numbered ports. Using one in an 
odd-numbered port disables the corresponding even-numbered 
port. For example, you can use 10 GbE or 25 GbE = 128 (32x 4:1 
breakouts). You can then mix and match by removing 2x 40 GbE 
or 100 GbE and adding 4x 10 GbE or 25 GbE, and conversely.
Table 15. Z9264F-ON Ethernet Switch 
Switch
Maximum 
number of 
connections
Network
Description
Z9264F-
ON
128-port
64x100 GbE, 64x40 GbE, 
128x10 GbE, 128 x 25 GbE 
(with breakout cables)
The Z9264F-ON is a fixed 2U Ethernet switch. The Z9264-F 
provides either 64 ports of 100 GbE or 40 GbE in QSFP28 or 
128 ports of 25 GbE or 10 GbE by breakout. Breakout cables 
are only used in the odd-numbered ports. Using one in an odd-
numbered port disables the corresponding even-numbered port. 
For example, you can use 10 GbE or 25 GbE = 128 (32x 4:1 
26
Selecting the equipment

---

## powerscale-node-site-prep-guide-feb2026::chunk_22

breakout. Breakout cables are only used in the odd-numbered ports. Using one in an odd- numbered port disables the corresponding even-numbered port. For example, you can use 10 GbE or 25 GbE = 128 (32x 4:1 26 Selecting the equipment

Table 15. Z9264F-ON Ethernet Switch 
Switch
Maximum 
number of 
connections
Network
Description
breakouts). You can then mix and match by removing 2x 40 GbE 
or 100 GbE and adding 4x 10 GbE or 25 GbE, and conversely.
Table 16. Z9100-ON Ethernet Switch 
Switch
Maximum 
number of 
connections
Network
Description
Z9100-
ON
128-port
32x100 GbE, 32x40 GbE, 
128x10 GbE, 128 x 25 GbE
The Z9100-ON fixed 1U Ethernet switch can accommodate high 
port density (lower and upper RUs). The switch accommodates 
multiple interface types (32 ports of 100 GbE, 40 GbE in 
QSFP28,128 ports of 25 GbE, or 10 GbE with breakout).
NOTE: The Z9100-ON switch is at end of life.
Table 17. S5232-ON Ethernet Switch 
Switc
h
Maximum 
number of 
connections
Network
Description
S5232
128-port
32x100 GbE, 32x40 GbE, 128x10 GbE (with breakout 
cables), 128 x 25 GbE (with breakout cables)
Only 124 10/25 GE nodes can be 
supported on the S5232 through 
breakout.
Table 18. S4148F-ON Ethernet Switch 
Switch
Maximum 
number of 
connections
Network
Descriptions
S4148F-ON
48-port
2x40 GbE 48x10 GbE
The S4148F-ON is the next-generation family of 10 GbE (48 
ports) top-of-rack, aggregation-switch, or router products that 
aggregate 10 GbE server or storage devices. The switch 
provides multi speed uplinks for maximum flexibility and simple 
management.
NOTE: The S4148F-ON switch is at end of life.
Table 19. S4112F-ON Ethernet Switch 
Switch
Maximum 
number of 
connections
Network
Description
S4112F-
ON
12-port
3x100 GbE (with breakout, connect 
12x10 GbE nodes using the 3x100 GbE 
ports) 12 x10 GbE.
The S4112F-ON supports 10/100 GbE with 12 fixed 
SFP+ ports to implement 10 GbE and three fixed 
QSFP28 ports to implement 4x10 or 4x25 using 
breakout. A total of 24 10 GbE connections, including 
the three fixed QSFP28 ports using 4x10 breakout 
cables.
Table 20. InfiniBand Switches 
Switch
Ports
Network
NVIDIA Neptune MSX6790
36-port
QDR InfiniBand
NVIDIA Scorpion 2 MSB7890-ES2F
36-port
EDR (supports QDR)InfiniBand
NVIDIA QM8790 (Quantum)
40-port
HDR
Selecting the equipment
27

---

## powerscale-node-site-prep-guide-feb2026::chunk_23

including the three fixed QSFP28 ports using 4x10 breakout cables. Table 20. InfiniBand Switches Switch Ports Network NVIDIA Neptune MSX6790 36-port QDR InfiniBand NVIDIA Scorpion 2 MSB7890-ES2F 36-port EDR (supports QDR)InfiniBand NVIDIA QM8790 (Quantum) 40-port HDR Selecting the equipment 27

Adding functionality to the cluster
Advanced cluster features can be obtained through OneFS software modules.
To enable a OneFS module after the cluster is installed, activate a license by entering a license key in OneFS.
More information about features that are offered through optional software modules and licensing is available in the OneFS Web 
Administration Guide or the OneFS CLI Administration Guide or by contacting a sales representative.
Data management modules
PowerScale offers software modules that add advanced data management features to your cluster.
You can install advanced data management modules to optimize storage performance. For more information, see the 
PowerScale OneFS Web Administration Guide.
SmartQuotas
The SmartQuotas module is a quota-management tool that monitors and enforces administrator-defined storage limits.
Through the use of accounting and enforcement quota limits, reporting capabilities, and automated notifications, you can do the 
following:
●
Manage and monitor storage utilization and disk storage.
●
Issue alerts when storage limits are exceeded.
A storage quota defines the boundaries of storage capacity that are allowed for a group, a user, or a directory on a cluster. The 
SmartQuotas module can provision, monitor, report disk-storage usage, and send automated notifications when storage limits 
are approached or exceeded. SmartQuotas also provides flexible reporting options that can help you analyze data usage.
SmartDedupe
The SmartDedupe software module enables you to save storage space on your cluster by reducing redundant data. 
Deduplication maximizes the efficiency of your cluster by decreasing the amount of storage required to store multiple files 
with similar blocks.
SmartDedupe deduplicates data by scanning a cluster for identical data blocks. Each block is 8 KB. If SmartDedupe finds 
duplicate blocks, SmartDedupe moves a single copy of the blocks to a hidden file called a shadow store. SmartDedupe then 
deletes the duplicate blocks from the original files and replaces the blocks with pointers to the shadow store.
Deduplication is applied at the directory level, targeting all files and directories underneath one or more root directories. You 
can first assess a directory for deduplication and determine the estimated amount of space you can expect to save. You can 
then decide whether to deduplicate the directory. After you begin deduplicating a directory, you can monitor how much space is 
saved by deduplication in real time.
You can deduplicate data only if you activate a SmartDedupe license on a cluster. However, you can assess deduplication 
savings without activating a SmartDedupe license.
3
28
Adding functionality to the cluster

---

## powerscale-node-site-prep-guide-feb2026::chunk_24

space is saved by deduplication in real time. You can deduplicate data only if you activate a SmartDedupe license on a cluster. However, you can assess deduplication savings without activating a SmartDedupe license. 3 28 Adding functionality to the cluster

Preparing your facility
To ensure an optimal data center and the long-term health of the cluster, prepare and maintain the environment.
Environmental requirements
Prepare the site to meet the required parameters.
NOTE: For F210, F710, and F910, the appliance must be ASHRAE A2 rated.
NOTE: For the Arista 7308X3 switch, only front-to-rear airflow is supported. There is no reverse airflow support due to 
thermal issues.
NOTE: For the PA110, fan speed and chassis temperature alerts are reported using monitoring systems such as email, 
health checks, CloudIQ, ESRS, and CELOG.
Table 21. Environmental Parameters 
Environmental item
Description
A3000, A300, H7000, and H700 nodes:
●
5 °C–35°C (40 °F–95°F) for continuous operation.
●
35 °C–40°C (95 °F–104°F) for 10% of annual runtime.
NOTE: There are four independent cooling zones so that 
a cooling failure in one node does not affect other nodes.
F210, PA110, F710, and F910: The temperature range for 
altitude <900 meters or 2953 ft is 10 °C–35°C (50 °F–95°F) 
with no direct sunlight on the platform. B100, P100, F210, 
F710, F910, F900, F600, and F200 nodes: 10 °C–35°C (50 
°F–95°F) with no direct sunlight on the equipment.
5% to 95% percent relative humidity with 33°C (91°F) 
maximum dew point. The atmosphere must be non-
condensing at all times.
NOTE: The cluster can be qualified to operate outside 
these limits. Product-specific documentation for system 
specifications provides more information.
F210, PA110, F710, and F910: The humidity percent range is 
8%RH with -12°C minimum dew point to 80%RH with 21°C 
(69.8°F) maximum dew point.
NOTE: The atmosphere must be non-condensing at all 
times.
●
F600 and F200, 21.9 kg (48.28 lbs)
●
F900 26.3 kg (57.98 lb)
●
H700 118.4 kg (261 lb)
●
H7000 141.4 kg (311.7 lb)
●
B100 21.9 kg (48.3 lb)
●
P100 21.9 kg (48.3 lb)
●
F210 21.73 kg (47.9 lb)
●
F710 21.73 kg (47.9 lb)
●
F910 36.1 kg (79.6 lb)
4
Preparing your facility
29

---

## powerscale-node-site-prep-guide-feb2026::chunk_25

H7000 141.4 kg (311.7 lb) ● B100 21.9 kg (48.3 lb) ● P100 21.9 kg (48.3 lb) ● F210 21.73 kg (47.9 lb) ● F710 21.73 kg (47.9 lb) ● F910 36.1 kg (79.6 lb) 4 Preparing your facility 29

Table 21. Environmental Parameters (continued)
Environmental item
Description
A3000, A300, H7000, and H700 nodes in a fully configured 
cabinet must sit on at least two floor tiles. They can weigh 
approximately 1588 kg (3500 lb).
●
0–2439 meters (0 ft–8,000 ft) above sea level operating 
altitude.
●
F210, PA110, F710, and F910:
○
Operational altitude derating: Maximum temperature is 
reduced by 1°C/300 meters (1.8°F/984 ft) above 900 
meters (2,953 ft).
The cluster might be qualified to operate outside of these limits. See the product-specific documentation for system 
specifications.
Power requirements
Depending on the cabinet configuration and input AC power source, the cabinet requires between two and six independent 
power sources. To determine the site requirements, use the published technical specifications and device rating labels to provide 
the current draw of the devices in each rack.
Table 22. Single-phase power connection requirements 
Specification
North American 3 wire connection 
(L = line phase, N = neutral, G = 
ground) (2 L and one G)
International and Australian 3 wire 
connection (1 L, 1 N, and 1 G)
Input nominal voltage
200–240 V ac +/- 10% L - L nominal
220–240 V ac +/- 10% L - L nominal
Frequency
50–60 Hz
50–60 Hz
Circuit breakers
●
30 A
●
40 A for A300, A3000, H700, and 
H7000 nodes
32 A
Power zones
Two
Two
Power requirements at site from 
minimum to maximum
●
Single-phase: six 30 A drops, two per zone
NOTE: The options for the single-phase PDU interface connector are listed in 
the Single-phase AC power input connector options table.
Table 23. Single-phase AC power input connector options 
Single-phase rack connector options
Customer AC source interface 
receptacle
Site
NEMA L6-30P 
NEMA L6-30R 
North America and Japan
Russellstoll 3750DP 
Russellstoll 9C33U0 
North America and Japan
30
Preparing your facility

---

## powerscale-node-site-prep-guide-feb2026::chunk_26

options table. Table 23. Single-phase AC power input connector options Single-phase rack connector options Customer AC source interface receptacle Site NEMA L6-30P NEMA L6-30R North America and Japan Russellstoll 3750DP Russellstoll 9C33U0 North America and Japan 30 Preparing your facility

Table 23. Single-phase AC power input connector options (continued)
Single-phase rack connector options
Customer AC source interface 
receptacle
Site
IEC-309 332P6 
IEC-309 332C6 
International
CLIPSAL 56PA332 
CLIPSAL 56CSC332 
Australia
Table 24. Three-phase AC power connection requirements 
Specification
North American (Delta) 4 wire 
connection (3 L and 1 G) (L = line 
phase, N = neutral, G = ground)
International and Australian (Wye) 5 
wire connection (3 L, 1 N, and 1 G)
Input nominal voltage
200–240 V ac +/- 10% L - L nominal
220–240 V ac +/- 10% L - N nominal
Frequency
50–60 Hz
50–60 Hz
Circuit breakers
50 A
32 A
Power zones
Two
Two
Power requirements at site from 
minimum to maximum
Delta:
●
One to two 50 A, three-phase drops per zone
●
Each rack requires a minimum of two drops to a maximum of four drops. 
The system configuration and the power requirement for that configuration 
determine the number of drops.
Wye:
●
One 32 A, three-phase drop per zone
●
Each Wye rack requires two 32 A drops.
NOTE: The interface connector options for the Delta and Wye three-phase 
PDUs are listed in the following tables,
Table 25. Three-phase Delta-type AC power input connector options 
Three-phase Delta rack connector 
options
Customer AC source interface 
receptacle
Site
Russellstoll 9P54U2 
Russellstoll 9C54U2 
North America and International
Hubbell CS-8365C 
Hubbell CS-8364C 
North America
Preparing your facility
31

---

## powerscale-node-site-prep-guide-feb2026::chunk_27

following tables, Table 25. Three-phase Delta-type AC power input connector options Three-phase Delta rack connector options Customer AC source interface receptacle Site Russellstoll 9P54U2 Russellstoll 9C54U2 North America and International Hubbell CS-8365C Hubbell CS-8364C North America Preparing your facility 31

Table 26. Three-phase Wye-type AC power input connector options 
Three-phase Wye rack connector 
options
Customer AC source interface 
receptacle
Site
GARO P432-6 
GARO S432-6 
International
Power Requirements for Equipment
To support the recommended power parameters of equipment, prepare the site.
Plan to set up redundant power for each rack. Supply the power with a minimum of two separate circuits on the electrical 
system. If one of the circuits fails, one or more remaining circuits could handle the full power load of the rack.
WARNING: Inadequate cooling might cause instability, exposing the customer to Data Unavailable (DU) or Data 
Loss (DL).
●
Power each Power Distribution Panel (PDP) within the rack with a separate power circuit.
●
Power the two IEC 60320 C14 power input connectors in the node by separate PDPs within the rack.
When calculating the power requirements for circuits that supply power to the rack, consider the power requirements for 
network switches and for nodes.
For power allocation for PowerScale F200, F600, F600-Prime, F900, F210, F710, and F910 nodes:
●
Nodes with proper cables can operate with 110 V or 115 V.
●
All power supplies support 110 - 240 VAC, with 50-60 Hz.
●
Use higher input voltages, such as 208 V when possible due to the improved efficiencies.
●
Nodes operated in data centers as an Enterprise Storage product within a cooled environment.
●
A higher voltage produces less current for a given wattage and less heat.
●
Power supply efficiency might vary on 110 V or 115 V compared to 208 V.
●
A UPS is recommended to avoid outages and damage to components or brown outs, avoid data loss, and so on.
○
UPS would support at a minimum:
￭
All nodes
￭
2x backend ( IB or Ethernet) switch
￭
The customer Ethernet edge
Each circuit should be rated appropriately for the node type and input voltage. See product specifications for power 
requirements specific to each node type.
Radio Frequency Interference (RFI) requirements
Electromagnetic fields that include radio frequencies can interfere with the operation of electronic equipment.
The hardware is certified to withstand radio frequency interference in accordance with standard EN61000-4-3. In data centers 
that employ intentional radiators, such as cell phone repeaters, the maximum ambient RF field strength should not exceed 3 
Volts/meter.
Take field measurements at multiple points close to the equipment. Consult with an expert before you install any emitting device 
in the data center. If you suspect high levels of RFI, contract an environmental consultant to evaluate RFI field strength and 
address mitigation efforts.
The ambient RFI field strength is inversely proportional to the distance and power level of the emitting device. To determine if 
the cell phone repeater or other intentional radiator device is at a safe distance from the equipment, use the table as a guide.
Table 27. Minimum recommended distance from RF emitting device 
Repeater power level*
Recommended minimum distance
1 Watt
3 meters
2 Watt
4 meters
32
Preparing your facility

---

## powerscale-node-site-prep-guide-feb2026::chunk_28

at a safe distance from the equipment, use the table as a guide. Table 27. Minimum recommended distance from RF emitting device Repeater power level* Recommended minimum distance 1 Watt 3 meters 2 Watt 4 meters 32 Preparing your facility

Table 27. Minimum recommended distance from RF emitting device (continued)
Repeater power level*
Recommended minimum distance
5 Watt
6 meters
7 Watt
7 meters
10 Watt
8 meters
12 Watt
9 meters
15 Watt
10 meters
* Effective Radiated Power, ERP
Hardware acclimation
Systems and components must acclimate to the operating environment before power is applied to them. Once unpackaged, the 
system must reside in the operating environment for up to 16 hours to thermally stabilize and prevent condensation.
NOTE: The storage conditions for some parts, such as hard drive, SSDs, and batteries, affect the wear and life of those 
parts. Do not exceed six consecutive months of unpowered storage from the delivery date.
NOTE: 
●
If there are signs of condensation after the recommended acclimation time has passed, allow an additional eight hours to 
stabilize.
●
System components must not experience changes in temperature and humidity that are likely to cause condensation to 
form on or in that system or component. Do not exceed the shipping and storage temperature gradient of 25°C per hr 
(45°F per hr).
●
To facilitate environmental stabilization, open both front and rear cabinet doors.
The acclimatization wait time table provides the amount of time that the system or component requires to acclimate to its new 
environment. The number of hours needed is based on the transit or storage environment during the prior 24 hours and the 
operating environment of the equipment.
Table 28. Acclimatization wait time 
Temperature
Relative humidity
Operating environment 
temperature
Acclimatization time
Nominal 20–22°C (68–
72°F)
Nominal 40–55% RH
Nominal 20–22°C (68–72°F) 40–
55% RH
1 hour or less
Cold <20°C (68°F)
Dry <30% RH
<30°C (86°F)
4 hours
Cold <20°C (68°F)
Damp >30% RH
<30°C (86°F)
4 hours
Hot >22°C (72°F)
Dry <30% RH
<30°C (86°F )
4 hours
Hot >22°C (72°F)
Humid 30–45% RH
<30°C (86°F)
4 hours
Hot >22°C (72°F)
Humid 45–60% RH
<30°C (86°F)
8 hours
Hot >22°C (72°F)
Humid >60% RH
<30°C (86°F)
16 hours
Unknown
Unknown
<30°C (86°F)
16 hours
Air quality requirements
Nodes are consistent with the air quality requirements and thermal guidelines of the American Society of Heating, Refrigeration, 
and Air Conditioning Engineers (ASHRAE).
For specifics, see the ASHRAE Environmental Standard Handbook and the most current revision of Thermal 
Guidelines for Data Processing Environments, Second Edition, ASHRAE 2009b.
Preparing your facility
33

---

## powerscale-node-site-prep-guide-feb2026::chunk_29

of the American Society of Heating, Refrigeration, and Air Conditioning Engineers (ASHRAE). For specifics, see the ASHRAE Environmental Standard Handbook and the most current revision of Thermal Guidelines for Data Processing Environments, Second Edition, ASHRAE 2009b. Preparing your facility 33

Most products are best suited for Class 1 datacom environments, which consist of tightly controlled environmental parameters, 
including temperature, dew point, relative humidity, and air quality. These facilities house mission-critical equipment and are 
typically fault-tolerant, including the air conditioners.
The data center should maintain a cleanliness level as identified in ISO 14664-1, Class 8 for particulate dust and pollution control. 
The air entering the data center should be filtered with a MERV 11 filter or better. The air within the data center should be 
continuously filtered with a MERV 8 or better filtration system. Take measures to prevent conductive particles, such as zinc 
whiskers, from entering the facility.
NOTE: For F210, F710, and F910, a MERV 11 or 13 filter is required.
The allowable relative humidity level is 20% to 80% non-condensing. However, the recommended operating environment range 
is 40% to 55%. Lower temperatures and humidity minimize the risk of hardware corrosion and degradation, especially in data 
centers with gaseous contamination, such as high sulfur content. Minimize humidity fluctuations within the data center. Prevent 
outside air contaminants and humidity from entering the facility by positively pressurizing the data center and installing air 
curtains on entryways.
For facilities below 40% relative humidity, use grounding straps when contacting equipment to avoid the risk of electrostatic 
discharge (ESD), which can harm electronic equipment.
As part of monitoring for environmental corrosiveness, place copper and silver coupons per ISA 71.04-1985, Section 6.1 
Reactivity, in representative airstreams. The monthly reactivity rate of the coupons should be fewer than 300 Angstroms. If 
the monitored reactivity rate exceeds 300 Angstroms, analyze the coupon for material species and put a corrective mitigation 
process in place.
Site floor load-bearing requirements
Install the cabinet in raised or unraised floor environments capable of supporting at least 1,495 kg (3,300 lb) per cabinet. The 
system may weigh less, but requires extra floor support margin to accommodate equipment upgrades or reconfiguration.
In a raised floor environment:
●
60 x 60 cm (24 x 24 inches) heavy-duty, concrete filled steel floor tiles are recommended.
●
Use only floor tiles and stringers that are rated to withstand:
○
Concentrated loads of two casters or leveling feet, each weighing up to 818 kg (1,800 lb).
○
Minimum static ultimate load of 1,495 kg (3,300 lb).
○
Rolling loads of 818 kg (1,800 lb) per floor tile. On floor tiles that do not meet the rolling load measurement must use 
coverings, such as plywood to protect floors during system roll.
●
Position that is adjacent cabinets with no more than two casters or leveling feet on a single floor tile.
●
Cutouts in 24 x 24 inches in tiles must be no more than 20.3 cm (8 inches) wide by 15.3 cm (6 inches) deep and centered. 
The front and rear must be 22.9 cm (9 inches), and 20.3 cm (8 inches) from the sides. Since cutouts weaken the tile, you 
can minimize deflection by adding pedestal mounts adjacent to the cutout. The manufacturer recommends that the number 
and placement of additional pedestal mounts relative to a cutout must be in accordance with the floor tile.
When positioning the cabinet, take care to avoid moving a caster into a floor tile cutout.
Ensure that the combined weight of any other objects in the data center does not compromise the structure of the raised or 
sub-floor, which is also referred as the unraised floor.
It is recommended that a certified data center design consultant inspect the site to ensure that the floor can support the 
system and surrounding weight.
NOTE: The cabinet weight depends on the specific product configuration. Calculate the total by using the Power 
Calculator.
Shipping and storage requirements
CAUTION: Systems and components must not experience changes in temperature and humidity that are likely 
to cause condensation to form on or in that system or component. Do not exceed the shipping and storage 
temperature gradient of 45°F per hr (25°C per hr).
34
Preparing your facility

---

## powerscale-node-site-prep-guide-feb2026::chunk_30

changes in temperature and humidity that are likely to cause condensation to form on or in that system or component. Do not exceed the shipping and storage temperature gradient of 45°F per hr (25°C per hr). 34 Preparing your facility

Table 29. Shipping and storage requirements 
Requirement
Description
Ambient temperature
-40° F to 149°F (-40°C to 65°C)
Temperature gradient
45°F per hr (25°C per hr)
Relative humidity
10% to 90% noncondensing
Elevation
-50 ft to 35,000 ft (-16 m to 10,600 m)
Unpowered storage time
Do not exceed six consecutive months of unpowered storage.
Fire suppressant disclaimer
Fire prevention equipment in the computer room should always be installed as an added safety measure. A fire suppression 
system is the responsibility of the customer. When selecting appropriate fire suppression equipment and agents for the data 
center, choose carefully. An insurance underwriter, local fire marshal, and local building inspector are all parties that you should 
consult during the selection of a fire suppression system that provides the correct level of coverage and protection.
Equipment is designed and manufactured to internal and external standards that require certain environments for reliable 
operation. Compatibility claims and recommendations on fire suppression systems are not provided through Dell. It is not 
recommended to position storage equipment directly in the path of high-pressure gas discharge streams or loud fire sirens to 
minimize the forces and vibration adverse to system integrity.
NOTE: The previous information is provided on an as-is basis and provides no representations, warranties, guarantees, or 
obligations on the part of our company. This information does not modify the scope of any warranty set forth in the terms 
and conditions of the basic purchasing agreement between the customer and the manufacturer.
Preparing your facility
35