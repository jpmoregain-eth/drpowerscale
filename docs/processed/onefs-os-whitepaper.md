## onefs-os-whitepaper::chunk_0

1 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
Dell EMC OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
DELL EMC POWERSCALE ONEFS 
OPERATING SYSTEM 
 
 
Abstract 
This white paper provides an introduction to the PowerScale OneFS 
operating system, the foundation of the PowerScale scale-out NAS storage 
platform. The paper includes an overview of the architecture of OneFS and 
describes the benefits of a scale-out storage platform. 
October 2020 
 
WHITE PAPER

2 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
Revisions 
Version 
Date 
Comment 
1.0 
November 2013 
Initial release for OneFS 7.1 
2.0 
June 2014 
Updated for OneFS 7.1.1 
3.0 
November 2014 
Updated for OneFS 7.2 
4.0 
June 2015 
Updated for OneFS 7.2.1 
5.0 
November 2015 
Updated for OneFS 8.0 
6.0 
September 2016 
Updated for OneFS 8.0.1 
7.0 
April 2017 
Updated for OneFS 8.1 
8.0 
November 2017 
Updated for OneFS 8.1.1 
9.0 
February 2019 
Updated for OneFS 8.1.3 
10.0 
April 2019 
Updated for OneFS 8.2 
11.0 
August 2019 
Updated for OneFS 8.2.1 
12.0 
December 2019 
Updated for OneFS 8.2.2 
13.0 
June 2020 
Updated for OneFS 9.0 
14.0 
September 2020 
Updated for OneFS 9.1 
 
Acknowledgements 
This paper was produced by the following: 
Author:  
Nick Trimbee 
 
 
 
 
 
The information in this publication is provided “as is.” Dell Inc. makes no representations or warranties of any kind with respect to the information in this 
publication, and specifically disclaims implied warranties of merchantability or fitness for a particular purpose. 
 
Use, copying, and distribution of any software described in this publication requires an applicable software license. 
Copyright © Dell Inc. or its subsidiaries. All Rights Reserved. Dell, EMC, Dell EMC and other trademarks are trademarks of Dell Inc. or its subsidiaries. 
Other trademarks may be trademarks of their respective owners.

---

## onefs-os-whitepaper::chunk_1

publication requires an applicable software license. Copyright © Dell Inc. or its subsidiaries. All Rights Reserved. Dell, EMC, Dell EMC and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

3 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
Table of contents 
Executive summary ................................................................................................................................................................ 1 
Dell EMC PowerScale OneFS operating system ................................................................................................................... 4 
Scalability ........................................................................................................................................................................... 6 
Efficiency ............................................................................................................................................................................ 8 
Performance ....................................................................................................................................................................... 9 
Management ...................................................................................................................................................................... 9 
Data protection ................................................................................................................................................................. 10 
Security ............................................................................................................................................................................ 11 
Interoperability .................................................................................................................................................................. 13 
Conclusion ............................................................................................................................................................................ 13

---

## onefs-os-whitepaper::chunk_2

Table of contents Executive summary ................................................................................................................................................................ 1 Dell EMC PowerScale OneFS operating system ................................................................................................................... 4 Scalability ........................................................................................................................................................................... 6 Efficiency ............................................................................................................................................................................ 8 Performance ....................................................................................................................................................................... 9 Management ...................................................................................................................................................................... 9 Data protection ................................................................................................................................................................. 10 Security ............................................................................................................................................................................ 11 Interoperability .................................................................................................................................................................. 13 Conclusion ............................................................................................................................................................................ 13

4 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
Executive summary 
We are seeing an explosion in the growth of data today. Not surprisingly, many industry experts believe that we have entered a new 
era of Big Data. Along with accelerating growth of new data, the composition of new data is also changing significantly from traditional 
structured, block data to much more unstructured, file-based data. In excess of 85% of new storage capacity installed in organizations 
around the world is for file-based data. 
This new world of Big Data is introducing major challenges for enterprise IT managers as well as significant opportunities for 
businesses across all industry segments. To deliver the optimal storage platform for Big Data, a storage system must provide: 
• Massive capacity: To accommodate very large and growing data stores, or data lakes 
• Extreme performance: To minimize response and data ingest times and thereby keep up with the pace of the business 
• High Efficiency: To reduce storage and related datacenter costs 
• Operational simplicity: To be able to manage a growing, large-scale data environment without adding more IT staff 
While there are certain similarities with the needs of vertical industries’ Big Data, traditional Enterprise IT has its own set of business 
drivers that create a unique set of storage requirements including: 
• Data Security: To minimize risk and meet regulatory and corporate  governance requirements 
• Data Protection: To ensure business continuance and availability to support  business operations 
• Interoperability: To increase business agility and to streamline management 
• Predictable Performance: To increase productivity and better support  business requirements 
• Continuous Availability: To protect users against downtime and ensure that they remain connected to their data. 
Today, the clear delineations that have existed between big data requirements and enterprise IT requirements have now blurred to the 
point that they are no longer distinguishable. The simple fact is that these two worlds are rapidly converging, creating a need for a 
fundamentally different way to meet the storage needs that enterprises will have going forward. To address these needs, organizations 
require an enterprise scale-out storage infrastructure that can meet the combined needs of this new world of Big Data and traditional 
Enterprise IT. We call this the “scale-out” imperative. 
Dell EMC OneFS operating system 
The most important design choice and fundamental difference of Dell EMC scale-out NAS is that with OneFS the storage system does 
not rely on hardware as a critical part of the storage architecture. Rather, OneFS combines the three functions of traditional storage 
architectures—file system, volume manager, and data protection—into one unified software layer, creating a single intelligent file 
system that spans all nodes within a storage system.  
 
Figure 1: Dell EMC Scale-out NAS Architecture

---

## onefs-os-whitepaper::chunk_3

OneFS combines the three functions of traditional storage architectures—file system, volume manager, and data protection—into one unified software layer, creating a single intelligent file system that spans all nodes within a storage system. Figure 1: Dell EMC Scale-out NAS Architecture

5 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
 
The Dell EMC PowerScale and Isilon storage nodes provide the appliance hardware base on which OneFS executes.  
 
 
Figure 2: OneFS Operating System: Running the Dell EMC Scale-out NAS Cluster. 
While the hardware is comprised of industry standard, enterprise quality components produced by manufacturers, such as Intel, 
Seagate, and Mellanox, nearly all aspects of the storage system that are distinctive are provided in software, by OneFS. On this 
commodity hardware base, the OneFS operating system enables data protection and automated data balancing and migration, as well 
as the ability to seamlessly add storage and performance capabilities without system downtime. 
Dell EMC PowerScale OneFS clusters can be architected with a wide variety of node styles and capacities, in order to meet the needs 
of a varied data set and wide spectrum of workloads. These node styles encompass several hardware generations and fall loosely into 
four main categories or tiers. The following table illustrates these tiers, and the associated hardware generations and models: 
 
 
Table 1: Hardware Tiers and Node Generations 
Enterprise Data Protection & Management Suite 
Hardware Platform Nodes: 
Flash, Hybrid, Archive 
OneFS Operating System

---

## onefs-os-whitepaper::chunk_4

four main categories or tiers. The following table illustrates these tiers, and the associated hardware generations and models: Table 1: Hardware Tiers and Node Generations Enterprise Data Protection & Management Suite Hardware Platform Nodes: Flash, Hybrid, Archive OneFS Operating System

6 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
 
OneFS works exclusively with the Dell EMC PowerScale and Isilon storage system, referred to as a “cluster.” A single Gen6 cluster 
consists of one or more chassis, each containing multiple storage “nodes,” which are constructed as rack mountable enterprise 
appliances containing memory, CPU, networking, 40Gb Ethernet or QDR InfiniBand, and storage media, and can scale out as high as 
252 nodes.  
In addition to the Gen6 modular architecture, such as the Isilon F800, where four nodes reside in a 4RU chassis, OneFS 9.0 also 
introduces support for the new 1RU all-flash PowerScale F600 NVMe and PowerScale F200 nodes. Both the traditional Gen6 chassis 
and the PowerScale stand-alone nodes happily co-exist within the same cluster. 
The OneFS total single file system capacity easily spans from 10s of terabytes to 10s of petabytes, supporting individual files up to 
16TB in size. Each node added to a cluster increases aggregate disk, cache, CPU, and network capacity. As a result of this aggregate 
increase, a 252-node cluster can access as much as 65TB of globally coherent, shared cache. With capacity and performance 
delivered in a single storage system, a single file system, and a single volume, the complexity of the system and management time for 
the storage administrator does not increase as the system scales. 
OneFS stripes data across all the storage nodes in a cluster. As data is sent from client machines to the cluster (using industry-
standard protocols, such as NFS, SMB, S3, HTTP, and HDFS), OneFS automatically divides the content and allocates it to different 
storage nodes in parallel. This occurs on the private Ethernet or InfiniBand network, which eliminates unnecessary network traffic. The 
cluster is managed as a single file system and the coordination and data distribution are completely transparent to end-user clients. 
When a client wishes to read a file, OneFS will retrieve the appropriate blocks from multiple storage nodes in parallel, automatically 
recombining the file, and the initiating client sees exactly what was originally written. This ability to automatically distribute data across 
multiple nodes in a transparent manner is fundamental for the ability of OneFS to enable growth, next-generation data protection, and 
extreme performance.  
Scalability  
Traditional storage systems that have a finite maximum size and must be replaced by a bigger storage array when the maximum 
performance or capacity is reached. In contrast, a OneFS powered cluster is able to linearly expand, or “scale out”, performance, 
capacity, or both, seamlessly increasing the existing file system or volume into petabytes of capacity. In addition, with the flexibility of 
OneFS, different node types can be mixed in a single cluster or “pool,” through the use of OneFS SmartPools™ software. The 
automated tiered storage capability of SmartPools provides added flexibility and eliminates the need for “forklift” upgrades when 
different capacity or performance levels are needed. SmartPools (see Figure 2) enables businesses and storage administrators to 
easily deploy a single file system to span multiple tiers of performance and capacity. This single file system automatically adapts to 
business data and application workflows over time. 
As well as tiering data automatically across different nodes, SmartPools can also use solid state drives (SSDs) to accelerate metadata 
and file-based storage workflows. SSDs as a tier can be used within a pool to improve metadata or data access performance, or the 
SSDs in one tier can be leveraged to hold the metadata of files on other tiers—boosting the performance of the entire cluster, including 
nodes that have no SSDs. 
OneFS also allows data to be moved to lower-cost cloud storage with the CloudPools functionality. CloudPools can seamlessly 
connect to Dell EMC-based cloud storage and third-party providers, including Amazon S3, Alibaba, Google Cloud and Microsoft Azure. 
CloudPools expands the SmartPools framework by treating a cloud repository as an additional tier. This enables older or data to be 
stored in a cold or frozen data tier or archive, thereby taking advantage of lower-cost, off-premise storage.

---

## onefs-os-whitepaper::chunk_5

Microsoft Azure. CloudPools expands the SmartPools framework by treating a cloud repository as an additional tier. This enables older or data to be stored in a cold or frozen data tier or archive, thereby taking advantage of lower-cost, off-premise storage.

7 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
 
Figure 3: SmartPools Single File System for Multiple Tiers with Automated, Transparent Data Movement 
In addition to the F-series all-flash nodes and using SSDs with SmartPools as part of the file system, OneFS can also utilize SSDs as 
an integral part of its caching hierarchy. As such, an optional third tier of read cache, SmartFlash, is configurable on nodes that contain 
SSDs. SmartFlash is a persistent eviction cache that is populated from system memory (DRAM) as it ages out.  
There are significant benefits to using SSDs for caching rather than as traditional file system storage devices. For example, when 
allocated for caching, the entire SSD will be used, and writes will occur in a very linear and predictable way. This provides far better 
utilization and also results in considerably reduced wear and increased durability over regular file system usage, particularly with 
random write workloads. The non-volatile nature of SSDs means that data cached by SmartFlash with persist even during node 
reboots. Using SSD for cache also makes sizing SSD capacity a much simpler prospect compared to using use SSDs as a storage 
tier. SmartFlash is ideal for workloads such as rendering, HPC, CAD and software design.  
 
OneFS 
 
Flash 
I/Ops 
Hybrid 
Throughput 
Archive 
Capacity

---

## onefs-os-whitepaper::chunk_6

for cache also makes sizing SSD capacity a much simpler prospect compared to using use SSDs as a storage tier. SmartFlash is ideal for workloads such as rendering, HPC, CAD and software design. OneFS Flash I/Ops Hybrid Throughput Archive Capacity

8 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
 
Figure 4: SmartFlash SSD-Backed Read Caching 
Adding capacity and performance capabilities to a cluster is significantly easier than with other storage systems—requiring only three 
simple steps for the storage administrator: adding another node into the rack, attaching the node to the InfiniBand network, and 
instructing the cluster to add the additional node. The new node provides additional capacity and performance since each node 
includes CPU, memory, and network. The Autobalance™ feature of OneFS will automatically move data across the InfiniBand network 
in an automatic, coherent manner so existing data that resides on the cluster moves onto this new storage node. This automatic 
rebalancing ensures the new node will not become a hot spot for new data and that existing data is able to gain the benefits of a more 
powerful storage system. The Autobalance feature of OneFS is also completely transparent to the end user and can be adjusted to 
minimize impact on high-performance workloads. This capability alone allows OneFS to scale transparently, on-the-fly, from 10s of 
terabytes to 10s of petabytes with no added management time for the administrator, or increased complexity within the storage 
system. 
Allocating data with a single, scalable pool of storage is an often-understated benefit and added efficiency found in a single file system. 
Managing and selecting volumes that have the requisite amount of free space or manually moving data is time-consuming and 
inefficient. If chosen incorrectly, the performance demands of a particular workflow may not be satisfied by a particular volume. Also, if 
the organization cannot address a particular volume, or if the storage administrator cannot move data transparently and quickly, then 
storage efficiency will be sub-optimal A OneFS powered cluster operates with storage utilization typically in excess of 80 percent and 
is, therefore, highly efficient. 
Efficiency 
Storage efficiency in a OneFS powered cluster can be increased with SmartDedupe, OneFS’ native post process data reduction 
technology. SmartDedupe maximizes the storage utilization of a cluster by decreasing the amount of physical storage required to 
house an organization’s data. Efficiency is achieved by scanning the on-disk data for identical blocks and then eliminating the 
duplicates. 
Storage efficiency is further enhanced by in-line data reduction, combining both real-time compression and deduplication, exclusively 
on the Isilon F810, PowerScale F600 & F200 and Isilon H5600 platforms. Isilon F810 nodes use an FPGA-based hardware offload 
engine resident on the backend PCI-e network adapter to perform in-line data reduction. On top of the FPGA, the OneFS hardware 
compression engine uses a proprietary implementation of DEFLATE with the highest level of compression, while incurring minimal to 
no performance penalty for highly compressible datasets. OneFS also provides a software implementation for the PowerScale F600, 
PowerScale F200, and Isilon H5600 nodes. Software compression is also used as fallback in the event of a compression hardware 
failure, and in a mixed cluster, for use in non-F810 nodes without a hardware compression capability. Both hardware and software 
compression implementations are DEFLATE compatible.

---

## onefs-os-whitepaper::chunk_7

nodes. Software compression is also used as fallback in the event of a compression hardware failure, and in a mixed cluster, for use in non-F810 nodes without a hardware compression capability. Both hardware and software compression implementations are DEFLATE compatible.

9 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
Additional features such as SmartQuotas thin provisioning, SnapshotIQ, small file packing, etc, also contribute to the overall efficiency 
equation. However, one of the most significant storage efficiency attributes is the way that OneFS natively manages data protection in 
the file system. Unlike most file systems that rely on hardware RAID, OneFS protects data at the file level and, using software-based 
erasure coding, allows most customers to enjoy raw to usable utilization levels of 85% or higher. This is in contrast to the scale up NAS 
industry mean of around 60% raw disk capacity utilization. In-line data reduction serves to further extend this storage efficiency 
headroom, bringing an even more compelling and demonstrable TCO advantage to primary file-based storage. 
Performance 
A large-scale storage system must provide the performance required for a variety of workflows, whether they be sequential, 
concurrent, or random. Different workflows will exist between applications and within individual applications. OneFS provides for all of 
these needs simultaneously with intelligent software. More importantly, with OneFS (see Figure 4), throughput and IOPS scale linearly 
with the number of nodes present in a single system. Due to balanced data distribution, automatic rebalancing, and distributed 
processing, OneFS is able to leverage additional CPUs, network ports, and memory as the system scales. 
 
 
Figure 5: OneFS Linear Scalability 
 
To fully exploit locality and meet the needs of various workflows, OneFS provides a globally accessible and coherent cache across all 
nodes. Storage nodes can currently utilize up to 384 GB of RAM each, allowing a OneFS powered cluster to contain up to 94.5 TB of 
system memory (252 nodes). This memory is primarily used to cache data that has been placed on that particular storage node and is 
actively being accessed. This cache grows as more nodes are added to a cluster, allowing an increasing working set to continually 
remain in cache. In addition, a variety of SSD configurations are also available for additional read caching. OneFS also allows the 
storage system administrator to specify the type of workload on a per-file or per-directory basis, indicating whether the access pattern 
to a particular file/directory is random, concurrent, or sequential. This unique capability allows OneFS to tailor on-disk layout decisions, 
cache-retention policies, and data pre-fetch policies to maximize performance of individual workflows. 
Management 
As organizations face more data and more management complexity, they are offered a wider variety of potential solutions. The 
emphasis for the next-generation data center is meeting customer requirements in a sustainable, scalable, and efficient fashion and 
the key to success is reducing management complexity. Human capital, traditionally measured by “Operating Expense” (or “OpEx”), 
must be leveraged to focus on the activities that enable a business to do more to improve its productivity, resourcefulness, and 
ultimately, bottom line.

---

## onefs-os-whitepaper::chunk_8

key to success is reducing management complexity. Human capital, traditionally measured by “Operating Expense” (or “OpEx”), must be leveraged to focus on the activities that enable a business to do more to improve its productivity, resourcefulness, and ultimately, bottom line.

10 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
Traditional storage systems require lengthy planning, upgrade, and maintenance activities. Trivial tasks, such as increasing capacity, 
scaling performance, and adding additional users, often require horizontal scaling and reconfiguring applications, and result in a 
disruption of user activities and ultimately lost productivity and revenue. 
OneFS has been designed to simplify administration activities and maintain this simplicity as the overall system scales, as shown in 
Figure 5. The ability to add performance and/or capacity in 60 seconds, avoid manual data and connection rebalancing with 
SmartConnect™ and Autobalance, and allow non-disruptive hardware and software upgrades and rollback is facilitated by OneFS.  
Data protection 
As traditional storage systems scale, techniques that were appropriate at a small size become inadequate at a larger size, and there is 
no better example of this than RAID. RAID can be effective only if the data can be reconstructed before another failure can occur. 
However, as the amount of data increases, the speed to access that data does not and the probability of additional failures continues 
to increase. OneFS does not depend on hardware-based RAID technologies to provide data protection. Instead, OneFS includes a 
core technology, FlexProtect™, which is built on solid mathematical constructs and utilizes Reed-Solomon encodings to provide 
redundancy and availability. FlexProtect provides protection for up to four simultaneous failures of either full nodes or individual drives 
and as the cluster scales in size, FlexProtect delivers on the need to ensure minimal reconstruction time for an individual failure. 
FlexProtect is a key innovation in OneFS and takes a file-specific approach toward data protection, storing protection information for 
each file independently. This independent protection allows protection data to be dispersed throughout the cluster (see Figure 6) along 
with the file data—dramatically increasing the potential parallelism for access and reconstruction when required. When there is a 
failure of a node or drive in a cluster, FlexProtect is able to identify which portions of files are affected by the failure and employs 
multiple nodes to participate in the reconstruction of only the affected files. Since the Autobalance feature in OneFS spreads files out 
across the cluster, the number of spindles and CPUs available for reconstruction far exceeds what would be found in a typical 
hardware RAID implementation. In addition, FlexProtect doesn’t need to reconstruct data back to a single spare drive (which with RAID 
creates an unavoidable bottleneck); instead the file data is reconstructed in available space, providing a virtual “hot spare”. 
 
Figure 6: OneFS +4n Data Protection 
 
OneFS constantly monitors the health of all files and disks within the cluster and if components are at risk, the file system automatically 
flags the problem components for replacement, transparently reallocating those files to healthy components. OneFS also ensures data 
integrity if the file system has an unexpected failure during a write operation. Each write operation is transactionally committed to a 
mirrored file system journal to protect against node or cluster failure. In the case of a write failure, the journal enables a node to rejoin 
the cluster quickly, without the need for a file system consistency check. With no single point of failure, the file system is also 
transactionally safe in the event of a journal failure.

---

## onefs-os-whitepaper::chunk_9

failure, the journal enables a node to rejoin the cluster quickly, without the need for a file system consistency check. With no single point of failure, the file system is also transactionally safe in the event of a journal failure.

11 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
Since the FlexProtect feature in OneFS is file-aware, it also provides file-specific protection capabilities. An individual file (or more 
typically, a directory) can be given a specific protection level and different portions of the file system to be protected at levels aligned to 
the importance of the data or workflow. Critical data can be protected at a higher level whereas less critical data can be protected at a 
lower level. This provides storage administrators with a very granular protection/capacity trade-off that can be adjusted dynamically as 
a cluster scales and a workflow ages. 
To effectively protect a file system that is hundreds of terabytes or petabytes in size, an extensive use of multiple data availability and 
data protection technologies is required. OneFS incorporates several strategies for data protection including data replication, 
synchronization and snapshot capabilities. 
OneFS Snapshots are highly scalable and typically take less than one second to create. They create little performance overhead, 
regardless of the level of activity of the file system, the size of the file system, or the size of the directory being copied. Also, only the 
changed blocks of a file are stored when updating the snapshots, thereby ensuring highly-efficient snapshot storage utilization.  
OneFS, combined with OneFS SnapshotIQ™ software, can be used to create up to 20,000 snapshots on a cluster. This provides a 
substantial benefit over most other snapshot implementations because the snapshot intervals can be far more granular and thereby 
offer significantly improved recovery point objectives (RPO) time frames. OneFS also provides near-immediate restoration of snapshot 
data backups to recover data quickly. With OneFS, snapshot restores are fast, efficient and simple. 
While snapshots provide an ideal solution for infrequent or smaller-scale data loss occurrences, when it comes to catastrophic failures 
or natural disasters, a second, geographically separate copy of a dataset is clearly beneficial.  
OneFS and SyncIQ™ software combine to deliver high-performance, asynchronous replication of data to address a broad range of 
RPO and recovery time objectives (RTO) and is easily optimized for either LAN or WAN connectivity to replicate over short or long 
distances, thereby providing protection from both site-specific and regional disasters. SyncIQ also offers encryption for secure 
replication across untrusted networks. 
Complementary to the manual and scheduled replication policies, SyncIQ also offers a continuous mode, or replicate on change, 
option. SyncIQ will continuously monitor the replication data set and automatically replicate any changes to the target cluster. 
OneFS further simplifies and accelerates disaster recovery and business continuity at scale with integrated, push-button simple failover 
and failback. With faster, easier failover and failback capabilities, most workflows will realize dramatic improvements in sync times. The 
same workflow will also be able to perform multiple syncs in the same time for ‘fresher’ target data. 
OneFS also provides the ability to perform large-scale backup and restore functions across massive, single-volume data sets—while 
leveraging an enterprise’s existing, SAN-based tape and VTL infrastructure. This is enabled by a fibre-channel backup accelerator 
card, in concert with OneFS NDMP support and SnapshotIQ. 
OneFS is certified with a wide range of leading enterprise backup applications, including: 
• Symantec NetBackup & Backup Exec 
• Dell EMC Avamar & Networker 
• IBM Tivoli Storage Manager 
• CommVault Simpana 
• Dell NetVault 
• ASG Time Navigator 
Each of the OneFS enhanced data protection capabilities – FlexProtect, SmartLock, SnapshotIQ, SyncIQ, NDMP will help enterprises 
reduce both RPO and RTO for mission critical applications and big data environments. 
Security 
To help enterprises meet their corporate governance and compliance requirements, OneFS includes robust security options that offer 
unprecedented levels of scale-out NAS security.

---

## onefs-os-whitepaper::chunk_10

will help enterprises reduce both RPO and RTO for mission critical applications and big data environments. Security To help enterprises meet their corporate governance and compliance requirements, OneFS includes robust security options that offer unprecedented levels of scale-out NAS security.

12 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
OneFS and SmartLock™ software combine to provide Write Once Read Many (WORM) data protection to prevent accidental, 
premature or malicious alteration or deletion of your critical data. With OneFS, we also help you meet regulatory and governance 
needs – including stringent SEC 17a-4 requirements - by providing tamper proof data retention and protection of your business-critical 
data. 
To further enhance security, by using the Roles Based Administration capabilities of OneFS, you can establish a secure role 
separation between storage administration and file system access, thereby improving security and preventing malicious or accidental 
changes to your data. 
OneFS also enables you to create Access Zones to provide secure, isolated storage pools for specific departments within your 
organization. This also allows you to consolidate storage resources for increased operating efficiency without compromising 
organizational security. 
 
 
 
Figure 7: OneFS Security Options 
To complement this, OneFS auditing can detect potential sources of data loss, fraud, inappropriate entitlements, access attempts that 
should not occur, and a range of other anomalies that are indicators of risk - especially when the audit associate’s data access with 
specific user identities.  
In the interests of data security, OneFS provides ‘chain of custody’ auditing by logging specific activity on the cluster. This includes 
OneFS configuration changes and SMB client protocol activity, both of which are required for organizational IT security compliance, as 
mandated by regulatory bodies like HIPAA, SOX, FISMA, MPAA, etc.  
OneFS 
Security 
Legal 
Accounting 
IT 
Marketing 
Secure Separation 
Roles-based Administration 
Administration & data access separated 
Secure Isolation 
Authentication Zones 
Secure WORM Data Protection 
OneFS and SmartLock 
SEC 17a-4 Compliance

---

## onefs-os-whitepaper::chunk_11

as mandated by regulatory bodies like HIPAA, SOX, FISMA, MPAA, etc. OneFS Security Legal Accounting IT Marketing Secure Separation Roles-based Administration Administration & data access separated Secure Isolation Authentication Zones Secure WORM Data Protection OneFS and SmartLock SEC 17a-4 Compliance

13 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
OneFS auditing utilizes Dell EMC’s Common Event Enabler (CEE) to provide compatibility with external, 3rd party audit applications 
like Varonis DatAdvantage. This allows OneFS to deliver an end to end, enterprise grade audit solution. 
OneFS also provides a solution for the security of data at rest. This involves dedicated storage nodes containing self-encrypting drives 
(SEDs), in combination with an encryption key management system embedded within OneFS. This means that the data on any SED 
which is removed from its source node cannot be unlocked and read, thereby guarding against the data security risks of physical drive 
theft. SED drives can also be securely wiped before being re-purposed or retired, via cryptographic erasure. 
OneFS encryption of data at rest satisfies a number of industries’ regulatory compliance requirements, including US Federal FIPS 104-
2 Level 2 and PCI-DSS v2.0 section 3.4. 
To further increase the protection and security of in-flight data, OneFS provides encryption for clients that support the SMBv3 protocol 
version. This can be configured on a per-share, zone, or cluster-wide basis. Encryption is also provided for SyncIQ replication over 
untrusted networks. 
Additionally, OneFS provides a hardened profile that can be enabled for sites that are looking for additional security or need to comply 
with the US Department of Defense’s Security Technical Implementation Guide (STIG). 
Finally, OneFS provides support for antivirus detection and remediation via integration with most common AV software vendors, 
including Symantec, TrendMicro, Kaspersky, McAfee, and Sophos. 
Interoperability 
OneFS provides integrated support for a wide range of industry-standard protocols including NFS, SMB, HTTP, FTP, S3, and HDFS. 
This allows you to greatly simplify and consolidate workflows, increase flexibility and get more value from your enterprise applications. 
With OneFS, you can streamline your storage infrastructure by consolidating large-scale file and unstructured data assets and 
eliminate silos of storage.  
To help you address your big data storage and business analytics needs, OneFS is the first and only scale-out NAS platform to provide 
native Hadoop Distributed File System (HDFS) support. This means that with OneFS powered storage, you can readily use your 
Hadoop data with other enterprise applications and workloads while eliminating the need to manually move data around or manage a 
dedicated infrastructure, not integrated with or connected to any other applications, as you would with a direct-attached storage 
approach. This integration simplifies your business analytics initiatives and helps you leverage results faster.  
To provide you with a robust control interface for your cluster, OneFS incorporates a Platform API that directly interfaces with the file 
system and allows you to gain an even more robust control interface to the cluster. The OneFS Platform API is a REST-based HTTP 
interface for automation, orchestration, and provisioning of a cluster. With the Platform API, 3rd-party applications can be used to 
control the administrative capabilities within OneFS—thereby further simplifying management, data protection and provisioning.   
These levels of interoperability help you leverage your large data assets with more flexibility among a broad range of applications and 
workloads, and across a diverse IT infrastructure environment. 
Conclusion 
Scalability, performance, ease of management, data protection, security and interoperability are critical in a storage system that can 
meet user needs and the ongoing challenges of the data center – especially in today’s world of “Big Data” in the enterprise.  
With OneFS, Dell EMC PowerScale and Isilon storage systems are simple to install, manage and scale, at virtually any size -- 
organizations and administrators can scale easily from 10s of terabytes to 10a of petabytes within a single file system, single volume, 
with a single point of administration.  OneFS delivers high performance, high throughput, or both, without adding management 
complexity.  
To meet your data protection needs, OneFS allows you to provide a highly resilient storage environment that far exceeds traditional, 
RAID-based approaches. For data backup and recovery, you can use our fast and efficient snapshot capability to meet specific 
recovery point and recovery time objectives. And for reliable disaster recovery protection, OneFS, combined with our SyncIQ software, 
provides fast local and remote data replication with push-button failover and failback simplicity.

---

## onefs-os-whitepaper::chunk_12

our fast and efficient snapshot capability to meet specific recovery point and recovery time objectives. And for reliable disaster recovery protection, OneFS, combined with our SyncIQ software, provides fast local and remote data replication with push-button failover and failback simplicity.

14 | 
 
 
       Dell EMC PowerScale OneFS Operating System 
© 2020 Dell Inc. or its subsidiaries. 
To help you address your security requirements, OneFS, combined with our SmartLock software, provides Write Once, Read Many 
(WORM) protection to prevent accidental, premature or malicious alteration or deletion of your data. At your option, and to help you 
meet regulatory and governance needs, this capability can be extended to include data protection that meets stringent SEC 17a-4 
requirements. With OneFS, you can also implement roles-based administration and configure Access Zones to create a strict 
separation or shared tenancy between storage administration, users and their file system access. 
With multi-protocol support and unsurpassed interoperability, OneFS can help you leverage your large data assets with more flexibility 
among a broad range of applications and workloads, and across a diverse IT infrastructure environment. 
Next-generation data centers must be built for sustainable scalability. They will harness the power of automation, leverage the 
commoditization of hardware, ensure the full consumption of the network fabric, and provide maximum flexibility for organizations 
intent on satisfying an ever-changing set of requirements. 
OneFS is the next-generation file system designed to meet these challenges. 
 
 
 
 
 
 
 
 
 
 
TAKE THE NEXT STEP 
Contact your Dell EMC sales representative or authorized reseller to learn more about how Dell EMC PowerScale and Isilon scale-out 
NAS storage solutions can benefit your organization. 
Visit Dell EMC PowerScale  to compare features and get more information. 
  
© 2020 Dell Inc. or its subsidiaries. All Rights Reserved. Dell, EMC and other trademarks are trademarks of Dell Inc. or  
its subsidiaries. Other trademarks may be trademarks of their respective owners. Reference Number: H8202.7 
Learn more about Dell 
EMC PowerScale 
solutions 
Contact a Dell EMC Expert 
View more resources 
Join the conversation  
with #DellEMCStorage