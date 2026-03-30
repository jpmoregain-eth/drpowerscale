## onefs-release-contents::chunk_0

Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
December 2025 
H18031.14 
 
White Paper 
Abstract 
This document summarizes the new features and functionality 
contained in each OneFS release from OneFS 7.1 to present.

Copyright 
 
 
2 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
The information in this publication is provided as is. Dell Inc. makes no representations or warranties of any kind with respect 
to the information in this publication, and specifically disclaims implied warranties of merchantability or fitness for a particular 
purpose.  
Use, copying, and distribution of any software described in this publication requires an applicable software license. 
Copyright © 2019-2025 Dell Inc. or its subsidiaries. Published in the USA December 2025 H18031.14. 
Dell Inc. believes the information in this document is accurate as of its publication date. The information is subject to change 
without notice.

---

## onefs-release-contents::chunk_1

software license. Copyright © 2019-2025 Dell Inc. or its subsidiaries. Published in the USA December 2025 H18031.14. Dell Inc. believes the information in this document is accurate as of its publication date. The information is subject to change without notice.

Contents 
 
3 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Contents 
Executive summary ....................................................................................................................... 5 
OneFS 7.1 ...................................................................................................................................... 6 
OneFS 7.1.1.................................................................................................................................... 6 
OneFS 7.2 ...................................................................................................................................... 7 
OneFS 7.2.1.................................................................................................................................... 8 
OneFS 8.0 ...................................................................................................................................... 9 
OneFS 8.0.1.................................................................................................................................. 11 
OneFS 8.1 .................................................................................................................................... 14 
OneFS 8.1.1.................................................................................................................................. 14 
OneFS 8.1.2.................................................................................................................................. 15 
OneFS 8.1.3.................................................................................................................................. 15 
OneFS 8.2 .................................................................................................................................... 15 
OneFS 8.2.1.................................................................................................................................. 18 
OneFS 8.2.2.................................................................................................................................. 18 
OneFS 9.0.0.................................................................................................................................. 19 
OneFS 9.1.0.................................................................................................................................. 19 
OneFS 9.2.0.................................................................................................................................. 20 
OneFS 9.2.1.................................................................................................................................. 21 
OneFS 9.3 .................................................................................................................................... 22 
OneFS 9.4 .................................................................................................................................... 23 
OneFS 9.5 .................................................................................................................................... 25 
OneFS 9.6 .................................................................................................................................... 27 
OneFS 9.7 .................................................................................................................................... 27

---

## onefs-release-contents::chunk_2

.................................................................................................................................... 15 OneFS 8.2.1.................................................................................................................................. 18 OneFS 8.2.2.................................................................................................................................. 18 OneFS 9.0.0.................................................................................................................................. 19 OneFS 9.1.0.................................................................................................................................. 19 OneFS 9.2.0.................................................................................................................................. 20 OneFS 9.2.1.................................................................................................................................. 21 OneFS 9.3 .................................................................................................................................... 22 OneFS 9.4 .................................................................................................................................... 23 OneFS 9.5 .................................................................................................................................... 25 OneFS 9.6 .................................................................................................................................... 27 OneFS 9.7 .................................................................................................................................... 27

Contents 
 
 
4 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
OneFS 9.8 .................................................................................................................................... 28 
OneFS 9.9 .................................................................................................................................... 29 
OneFS 9.10................................................................................................................................... 30 
OneFS 9.11................................................................................................................................... 30 
OneFS 9.12................................................................................................................................... 31 
OneFS 9.13................................................................................................................................... 32 
Summary ...................................................................................................................................... 33 
Take the next step ....................................................................................................................... 33

---

## onefs-release-contents::chunk_3

4 Dell PowerScale OneFS Release Contents New Features, Functionality, and Enhancements OneFS 9.8 .................................................................................................................................... 28 OneFS 9.9 .................................................................................................................................... 29 OneFS 9.10................................................................................................................................... 30 OneFS 9.11................................................................................................................................... 30 OneFS 9.12................................................................................................................................... 31 OneFS 9.13................................................................................................................................... 32 Summary ...................................................................................................................................... 33 Take the next step ....................................................................................................................... 33

5 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Executive summary 
 
This document lists and briefly describes the new features and functionality delivered in 
each OneFS release since OneFS 7.1.  
 
Date 
Part number/ 
revision 
Description 
November 2019 
H18031 
Updated for OneFS 8.2.1 
December 2019 
H18031.1 
Updated for OneFS 8.2.2 
June 2020 
H18031.2 
Updated for OneFS 9.0.0 
October 2020 
H18031.3 
Updated for OneFS 9.1.0 
April 2021 
H18031.4 
Updated for OneFS 9.2 
October 2021 
H18031.5 
Updated for OneFS 9.3 
March 2022 
H18031.6 
Updated for OneFS 9.4 
January 2023 
H18031.7 
Updated for OneFS 9.5 
December 2023 
H18031.8 
Updated for OneFS 9.7 
April 2024 
H18031.9 
Updated for OneFS 9.8 
August 2024 
H18031.10 
Updated for OneFS 9.9 
December 2024 
H18031.11 
Updated for OneFS 9.10 
April 2025 
H18031.12 
Updated for OneFS 9.11 
August 2025 
H18031.13 
Updated for OneFS 9.12 
December 2025 
H18031.14 
Updated for OneFS 9.13 
 
 
Dell Technologies and the authors of this document welcome your feedback on this 
document. Contact the Dell Technologies team by email. 
Author: Nick Trimbee 
Note: For links to other documentation for this topic, see the PowerScale Info Hub. 
Overview 
Revisions 
We value your 
feedback

---

## onefs-release-contents::chunk_4

authors of this document welcome your feedback on this document. Contact the Dell Technologies team by email. Author: Nick Trimbee Note: For links to other documentation for this topic, see the PowerScale Info Hub. Overview Revisions We value your feedback

6 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
OneFS 7.1 
Release 
Feature 
Info 
OneFS 
7.1 
October 
2013 
Audit 
• 
SMB file access and configuration auditing, 
recording who did what on files and sending 
out to the Dell Common Event Enabler 
(CEE). CEE 6.0.3 provides support and 
integration with Varonis DatAdvantage for 
Windows. 
Roles Based 
Administration 
• 
Cluster management access control system 
that divides up the powers of the “root” user 
and allows assignment of specific roles to 
other non-privileged users. RBAC has a set 
of built-in roles and the ability to create user-
defined roles. The 3 built-in roles are Audit 
Administrator, System Administrator & 
Security Administrator. 
SmartDedupe 
• 
Post-process deduplication, reducing the 
physical data footprint by locating and 
sharing common elements across files using 
‘shadow store’ containers. 
Job Engine v2 
• 
Simultaneous Jobs: Allowing Multiple Jobs to 
run. 
• 
Impact Control: Adding new Impact control 
rules for CPU and DISK usage.  
• 
Monitoring :Improved monitoring and stats. 
• 
Job Engine Exclusion Sets. 
 
OneFS 7.1.1 
Release 
Feature 
Info 
OneFS 
7.1.1 
July 2014 
L3 Cache 
• 
Using a nodes SSD as a large, cost-
effective, persistent read cache for 
evicted L2 data and metadata blocks.  
Roles Based 
Administration 
• 
WebUI interface and additional roles. 
SMB3 Multi-
channel 
• 
Allows SMB3 storage devices to 
automatically discover and use multiple 
network connections simultaneously,

---

## onefs-release-contents::chunk_5

a large, cost- effective, persistent read cache for evicted L2 data and metadata blocks. Roles Based Administration • WebUI interface and additional roles. SMB3 Multi- channel • Allows SMB3 storage devices to automatically discover and use multiple network connections simultaneously,

7 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Release 
Feature 
Info 
increasing throughput and fault 
tolerance. 
MMC 
Integration 
• 
Allows a cluster’s SMB shares to be 
managed using the MMC tool by 
providing support for the “Shared 
Folders” snap-in to MMC.  
S210 and 
X410 
• 
S210 and X410 Gen5 platform node 
support. 
 
OneFS 7.2 
Release 
Feature 
Info 
OneFS 7.2 
November 
2014 
Userspace 
NFS 
• 
NFS v3 and NFS v4 servers ported to 
userspace. 
• 
Rewritten and multi-instanced OneFS File 
System Driver. 
• 
Added NFS feature: Zone support for 
exports. 
• 
Added NFS feature: Aliases for exported 
paths. 
• 
Added NFS feature: Audit. 
• 
Improved NFS statistics reporting and 
management. 
• 
Improved NFS WebUI, added support for 
new features. 
• 
Improved NFS CLI, added support for 
new features. 
NFS Multi-
tenant 
Access 
Zones 
• 
Ability to authenticate against multiple 
authentication providers, including 
multiple instances of: AD, LDAP, NIS, 
Local User/Group Database. 
• 
Each multi-tenant access zone will be 
associated with:

---

## onefs-release-contents::chunk_6

Improved NFS CLI, added support for new features. NFS Multi- tenant Access Zones • Ability to authenticate against multiple authentication providers, including multiple instances of: AD, LDAP, NIS, Local User/Group Database. • Each multi-tenant access zone will be associated with:

8 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
• 
One or more SmartConnect 
Zones that will be allowed access 
to this zone. 
• 
One set of shares that will be 
accessible through this multi-
tenant access zone. 
• 
One or more Authentication 
providers to authenticate users for 
this multi-tenant access zone. 
Protocol 
Auditing 
• 
File access and configuration auditing for 
the NFS and SMB protocols. 
• 
Recording all file access events (who did 
what on files) and sending out to the Dell 
Common Event Enabler (CEE).  
• 
CEE 6.3.1.0 provides support and 
integration with Varonis DatAdvantage for 
Windows. 
Source 
Based 
Routing 
• 
Routes traffic based on its source IP 
address. 
HD400 
• 
Isilon HD400 Gen5 platform node support. 
FSA 
• 
InsightIQ 3.1 support. 
 
OneFS 7.2.1 
Release 
Feature 
Info 
OneFS 7.2.1 
June 2015 
IPv6 
• 
Support for both IPv6-only and dual-stack 
configurations. 
X210 
• 
X210 Gen5 platform node support. 
NL410 
• 
NL410 Gen5 platform node support.

---

## onefs-release-contents::chunk_7

platform node support. FSA • InsightIQ 3.1 support. OneFS 7.2.1 Release Feature Info OneFS 7.2.1 June 2015 IPv6 • Support for both IPv6-only and dual-stack configurations. X210 • X210 Gen5 platform node support. NL410 • NL410 Gen5 platform node support.

9 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
OneFS 8.0 
Release 
Feature 
Info 
OneFS 8.0 
December 2015 
SMB3 Continuous 
Availability 
• 
Support for SMB3 continuous 
availability and witness. 
NFS and SMB File 
Blocking 
• 
Control what type of files can 
be written via NFS or SMB to a 
cluster, based on include of 
exclude filter lists. 
NFSv4 Failover 
• 
NFSv4 clients can now use 
dynamic IPs which will give 
them more service availability 
and non-disruption during IP 
migration events or NFS 
service interruption. 
• 
When a client’s virtual IP 
address moves, or a OneFS 
group change event occurs, 
the client application will 
continue without disruption. As 
such, no unexpected I/O error 
will propagate back up to the 
client application.  
DNS Per Multi-
tenant Access 
Zone 
• 
Ability to specify separate 
primary and secondary DNS 
servers for each multi-tenant 
access zone. 
• 
DNS servers are configured by 
a new ‘Groupnet’ network 
object which lives above a 
subnet. 
Overlapping Multi-
tenant Access 
Zones 
• 
Ability to create Multi-tenant 
Access Zones with overlapping 
datasets. 
HDFS Audit 
• 
Support for file access and 
configuration auditing for the 
HDFS protocol by recording all 
file access events (who did 
what on files) and sending out

---

## onefs-release-contents::chunk_8

Access Zones • Ability to create Multi-tenant Access Zones with overlapping datasets. HDFS Audit • Support for file access and configuration auditing for the HDFS protocol by recording all file access events (who did what on files) and sending out

10 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
to the Dell Common Event 
Enabler (CEE). 
CloudPools 1.0 
• 
Enables the movement and 
tiering of data via NFS or SMB 
from OneFS clusters to 
Amazon S3, Microsoft Azure, 
or OneFS to OneFS cloud 
storage. 
• 
Archiving files to Cloud 
Storage. 
• 
Recalling files from the 
Cloud Storage. 
• 
NFS & SMB I/Os to the 
cloud data (Note: I/O 
utilizing any other 
protocols, local, HTTP, 
FTP, etc, is not 
supported and will 
return an EIO error). 
• 
Encryption for data 
written to the cloud. 
• 
Compression for data 
written to the cloud. 
• 
Garbage collection for 
orphaned cloud 
objects whose 
retention period has 
expired. 
• 
Feature interoperability 
with NDMP, SyncIQ, 
SnapshotIQ, WORM, 
Quota and etc. 
SmartDedupe Job 
Control 
• 
Allow re-configuration of 
priority and impact level for 
SmartDedupe job defaults. 
CELOG 2.0 
• 
Redesign of OneFS cluster 
event logging and alerting 
infrastructure.

---

## onefs-release-contents::chunk_9

has expired. • Feature interoperability with NDMP, SyncIQ, SnapshotIQ, WORM, Quota and etc. SmartDedupe Job Control • Allow re-configuration of priority and impact level for SmartDedupe job defaults. CELOG 2.0 • Redesign of OneFS cluster event logging and alerting infrastructure.

11 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Release 
Feature 
Info 
NDU and Rollback 
• 
Support for rolling (one node at 
a time) upgrades. 
• 
Ability to rollback to prior 
OneFS version. 
SD Edge 
• 
Software-defined virtual 
OneFS nodes on VMware 
vSphere. 
 
OneFS 8.0.1 
Release 
Feature 
Info 
OneFS 8.0.1 
September 
2016 
SyncIQ 
Compliance Mode 
Failover 
• 
SyncIQ failover and failback with 
compliance mode SmartLock, 
delivering automated disaster 
recovery for financial services 
SEC-17a4 regulatory 
compliance. 
HDFS 
• 
Single management point for 
Ambari operator to manage and 
monitor a Hadoop cluster with 
OneFS as the storage layer. 
• 
Ranger authorization integration 
to ensure proper user access to 
files are governed by Ranger 
policies and OneFS file system 
access control. 
• 
Kerberos encryption to secure 
and encrypt data from HDFS 
client to/from OneFS, preventing 
rogue users from sniffing HDFS 
traffic on network. 
• 
Data-node load balancing, 
avoiding overloading nodes and 
increasing cluster resilience. 
• 
Ambari metrics and alerting .

---

## onefs-release-contents::chunk_10

control. • Kerberos encryption to secure and encrypt data from HDFS client to/from OneFS, preventing rogue users from sniffing HDFS traffic on network. • Data-node load balancing, avoiding overloading nodes and increasing cluster resilience. • Ambari metrics and alerting .

12 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
CloudPools Proxy 
Support 
• 
Multiple nodes can now 
simultaneously tier to the cloud. 
• 
No direct external network 
exposure of OneFS systems for 
CloudPools. 
• 
No network workarounds 
necessary to configure 
CloudPools. 
Mac OSX Support 
• 
Enables Mac OS specific 
features like color tagging of files 
& extended metadata. 
• 
Mac users can leverage 
powerful Mac features to sort, 
tag files for efficient file 
categorization. 
• 
Improved directory listing speed 
from Mac clients, in particular for 
large directories. 
Audit 
Performance 
• 
Audit at scale – up to 50 million 
audit events. 
• 
File access and configuration 
auditing records all file access 
events (who did what on files) 
and sends them out to the Dell 
Common Event Enabler (CEE).  
• 
CEE 6.5 provides support and 
integration with Varonis 
DatAdvantage for Windows, 
specifically allowing: Usable 
Access Auditing; 
Recommendations, Analytics 
and Modeling; and Data Owner 
Identification and Involvement. 
AIMA 
Performance 
• 
Ensuring that proper user 
access to OneFS is maintained 
with server consolidation (e.g. 
forest/domain collapse) by 
supported SID History.

---

## onefs-release-contents::chunk_11

DatAdvantage for Windows, specifically allowing: Usable Access Auditing; Recommendations, Analytics and Modeling; and Data Owner Identification and Involvement. AIMA Performance • Ensuring that proper user access to OneFS is maintained with server consolidation (e.g. forest/domain collapse) by supported SID History.

13 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Release 
Feature 
Info 
• 
Negative caching helps reduce 
the load placed on 
authentication providers by 
caching the information that a 
user or group does not exist in 
any authentication provider. 
Small File 
Efficiency for 
Healthcare PACS 
• 
A policy mechanism to control 
containerization, so that it may 
be optional, allowing customers 
explicitly to opt for better small-
file storage efficiency in 
exchange for some small-file 
performance.  
• 
A class of specialized shadow 
stores to act as containers. 
These shadow stores differ from 
existing shadow stores in a few 
ways in order to isolate 
fragmentation, to support tiering, 
and to support future 
optimizations which will be 
specific to single-reference 
stores.  
• 
A method to pack, unpack, and 
repack data into, out of, and 
between containers.  
UI Scalability 
• 
Improved performance and 
usability for the SMB share and 
NFS export pages.  
• 
WebUI now can handle long 
lists, and the backing stores are 
proven up to 40,000 records. 
The WebUI now returns ten 
items per page. 
Partitioned 
Performance 
Monitoring 
• 
Performance statistics for Job 
Engine and data services.

---

## onefs-release-contents::chunk_12

NFS export pages. • WebUI now can handle long lists, and the backing stores are proven up to 40,000 records. The WebUI now returns ten items per page. Partitioned Performance Monitoring • Performance statistics for Job Engine and data services.

14 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
OneFS 8.1 
Release 
Feature 
Info 
OneFS 8.1 
May 2017 
Gen6 
Hardware 
• 
Support for new Isilon F800, H600, 
H500, H400, A200, and A2000 Gen6 
platform hardware. 
E Licensing 
• 
Support for E Licensing. 
SD Edge 
• 
Software-defined OneFS on single 
VMware vSphere host. 
 
OneFS 8.1.1 
Release 
Feature 
Info 
OneFS 8.1.1 
December 
2017 
SMB3 
Encryption 
• 
Allows OneFS SMB server to be 
configured for SMB3 encryption on 
a per share, zone, or cluster-wide 
basis. 
NFSv3 
Character 
Encoding 
• 
Setting cluster encoding and 
export encoding to the same 
character set will yield RFC 
compliant filenames, enabling 
exports to NFS clients using non-
western characters. 
HDFS Cloudera 
Navigator 
• 
Support for Cloudera Navigator – 
lineage and metadata 
management integration. 
CloudPools for 
GCP 
• 
Enables users to use NFS or SMB 
to move data from OneFS clusters 
to Google Cloud Storage and tier 
it.

---

## onefs-release-contents::chunk_13

western characters. HDFS Cloudera Navigator • Support for Cloudera Navigator – lineage and metadata management integration. CloudPools for GCP • Enables users to use NFS or SMB to move data from OneFS clusters to Google Cloud Storage and tier it.

15 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
OneFS 8.1.2 
Release 
Feature 
Info 
OneFS 8.1.2 
August 2018 
HDFS 
• 
Hadoop 3 Support. 
• 
OneFS Ambari Management Pack. 
• 
WebHDFS support. 
• 
LLAP support. 
• 
Ranger with SSL support. 
 
OneFS 8.1.3 
Release 
Feature 
Info 
OneFS 8.1.3 
January 2019 
In-line 
Compression 
• 
Support for in-line compression 
on F810 with FPGA offload. 
F810 
• 
F810 Gen6 hardware platform 
support. 
 
OneFS 8.2 
Release 
Feature 
Info 
OneFS 8.2 
May 2019 
Cluster Scale 
• 
252 node cluster support. 
SMB Performance 
Dataset Monitoring 
• 
Performance statistics for SMB. 
SmartQuotas 
• 
Support for 500K quotas. 
• 
Percentage based quotas. 
• 
Default directory quotas. 
• 
Client-side reporting 
improvements. 
• 
Application logical quotas.

---

## onefs-release-contents::chunk_14

May 2019 Cluster Scale • 252 node cluster support. SMB Performance Dataset Monitoring • Performance statistics for SMB. SmartQuotas • Support for 500K quotas. • Percentage based quotas. • Default directory quotas. • Client-side reporting improvements. • Application logical quotas.

16 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
SmartPools 
FilePolicy Job 
• 
Efficient changelist-based 
SmartPools file pool policy job. 
HDFS Encryption 
• 
Support for Hadoop data 
encryption (TDE). 
SyncIQ  
• 
SyncIQ encryption for secure 
replication over the WAN and 
other untrusted networks. 
• 
SyncIQ bandwidth throttling. 
SmartConnect 
• 
SmartConnect and Flexnet 
update. 
SnapshotIQ 
Domains 
• 
Re-architecting of SnapshotIQ 
framework to avoid costly 
snapshot painting and drive 
scalability and other efficiencies. 
Small File 
Efficiency 
Defragmenter 
• 
Introduction of small file 
efficiency job for defragmenting 
shadow stores and opening up 
SFSE to low-write archive 
workloads beyond healthcare 
PACS. 
SmartLock 
• 
Introduction of 
ComplianceStoreDelete job. 
Audit 
• 
Support for granular audit event 
selection, avoiding the collection 
of unneeded audit events that 
3rd party audit applications do 
not register for. 
Zone-aware RBAC 
• 
Multi-tenant access zone aware, 
role-based access control. 
CloudPools 2.0 
• 
Support for AWS signature 
authentication version 4. 
• 
Deliver network statistics per 
CloudPools account or file pool 
policy.

---

## onefs-release-contents::chunk_15

that 3rd party audit applications do not register for. Zone-aware RBAC • Multi-tenant access zone aware, role-based access control. CloudPools 2.0 • Support for AWS signature authentication version 4. • Deliver network statistics per CloudPools account or file pool policy.

17 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Release 
Feature 
Info 
• 
Support for Alibaba Cloud and 
Amazon C2S public cloud 
providers. 
• 
Full integration of CloudPools 
and data services like Snapshot, 
Sparse file handling, Quota, 
AVScan and WORM. 
NDMP 2-way FC 
Adapter 
• 
2-way NDMP support for Gen6 
platforms with combo Fibre 
Channel/10GbE  interface card.  
• 
Support of NDMP Redirector 
and Throttler. 
• 
Support of ComboCopy for 
CloudPools. 
SSH Multi-factor 
Auth 
• 
Multi-factor authentication 
support via integration with Duo 
service, using phone call-back 
and SMS passcode. 
Upgrade / NDU 
• 
Support for simultaneous 
firmware upgrade 
• 
Ability to pause and resume 
OneFS upgrade  
• 
Patch installation during OneFS 
upgrade 
WebUI 
• 
Removal of dependency on 
Flash from WebUI.  
• 
Improved internal network config 
pages. 
H5600 
• 
Isilon H5600 Gen6 deep chassis 
introduction. 
Leaf/spine backend 
• 
Dell Z9100 switches supporting 
leaf/spine architecture. 
• 
144 nodes max cluster with 
leaf/spine backend.

---

## onefs-release-contents::chunk_16

WebUI • Removal of dependency on Flash from WebUI. • Improved internal network config pages. H5600 • Isilon H5600 Gen6 deep chassis introduction. Leaf/spine backend • Dell Z9100 switches supporting leaf/spine architecture. • 144 nodes max cluster with leaf/spine backend.

18 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
OneFS 8.2.1 
Release 
Feature 
Info 
OneFS 8.2.1 
September 2019 
In-line Deduplication 
• 
Support for in-line deduplication 
on the F810 platform. 
• 
Data Reduction reporting 
enhancements. 
Serviceability 
Enhancements 
• 
Instant secure erase. 
• 
Improved Healthchecks. 
• 
Patch Framework 
improvements. 
PlatformAPI 
• 
Enhancements for CommVault 
and DataIQ. 
 
OneFS 8.2.2 
Release 
Feature 
Info 
OneFS 8.2.2 
January 2020 
H5600 In-line 
Data Reduction 
• 
Support for in-line 
compression and deduplication 
on the deep-hybrid H5600 
platform. 
Large file support 
• 
Support for 16TB files. 
25GbE support 
• 
Support for front-end 25Gb 
Ethernet connectivity. 
NFS Performance 
Dataset 
Monitoring 
• 
Performance statistics for NFS 
protocol. 
NDU 
• 
Parallel upgrades.

---

## onefs-release-contents::chunk_17

in-line compression and deduplication on the deep-hybrid H5600 platform. Large file support • Support for 16TB files. 25GbE support • Support for front-end 25Gb Ethernet connectivity. NFS Performance Dataset Monitoring • Performance statistics for NFS protocol. NDU • Parallel upgrades.

19 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
OneFS 9.0.0 
Release 
Feature 
Info 
OneFS 9.0.0 
June 2020 
F600 & F200 
• 
OneFS support for the new 
PowerScale F600-NVMe and 
F200 platform. 
In-line Data 
Reduction 
• 
Support for in-line compress 
and deduplication on the all-
flash PowerScale F600-NVMe 
and F200 platforms. 
S3 Protocol 
• 
Support for the S3 protocol, 
expanding the data lake to 
native file and object. 
IPMI 
• 
IPMI support for remote 
console and power control of 
nodes. 
HDFS 
• 
HDFS Ranger NANON 
Support 
 
OneFS 9.1.0 
Release 
Feature 
Info 
OneFS 9.1.0 
October 2020 
CAVA Antivirus 
Support 
• 
CAVA Antivirus support for 
SMB clients using Common 
Event Enabler (CEE) plus 
integration with most AV 
software vendors to scan 
files, providing better 
performance than current 
ICAP. 
Faster Client 
Failovers 
• 
Improved group change time 
for planned shutdowns. 
Shrinks the window for data 
unavailability due to group 
changes to less than 5 
seconds.

---

## onefs-release-contents::chunk_18

with most AV software vendors to scan files, providing better performance than current ICAP. Faster Client Failovers • Improved group change time for planned shutdowns. Shrinks the window for data unavailability due to group changes to less than 5 seconds.

20 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
CloudPools Cloud 
Object Cache  
• 
CloudPools traffic 
optimization, reducing the 
number of network round-trips 
when recalling data from a 
CloudPools target. 
Audit Log Purging 
• 
Ability to automatically and 
periodically purge audit logs. 
Customizable 
CELOG Alerts 
• 
Configurable event thresholds 
allow users to adjust the 
value at which events are 
triggered for various cluster 
statistics. 
In-product 
Activation 
• 
Activate product licenses with 
ELMS over ESRS. 
 
NDMP Multi-
stream BRE 
• 
Restartable backup support 
for multi-stream NDMP. 
 
OneFS 9.2.0 
Release 
Feature 
Info 
OneFS 9.2.0 
April 2021 
PowerScale F900 
• 
OneFS support for the new 
PowerScale F900-NVMe 
platform. 
In-line Data 
Reduction 
• 
Support for in-line compress 
and deduplication on the all-
flash PowerScale F900-
NVMe platform. 
NFSoRDMA  
• 
NFS over RDMA support for 
NFS v3 for PowerScale and 
Isilon nodes which contain 
supported Ethernet interface 
cards. 
Enterprise Key 
Management for 
SEDs 
• 
Support for external KMIP 
compliant key managers such 
as SKLM, SafeNet and 
Vormetric for storing

---

## onefs-release-contents::chunk_19

• NFS over RDMA support for NFS v3 for PowerScale and Isilon nodes which contain supported Ethernet interface cards. Enterprise Key Management for SEDs • Support for external KMIP compliant key managers such as SKLM, SafeNet and Vormetric for storing

21 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Release 
Feature 
Info 
encryption keys on SED 
clusters. 
Full IPv6 Support 
• 
Full IPv6 support that meets 
the requirements for USGv6 
compliance. 
CELOG WebUI 
• 
Addition of a web-based 
graphical user interface for 
CELOG allowing events to be 
displayed, searched, 
categorized, filtered, ignored, 
and resolved.  
 
 
IB Backend for 
PowerScale 
• 
Support for backend 
InfiniBand network interfaces 
on PowerScale nodes, for 
compatibility with legacy IB 
clusters. 
 
Cluster 
Configuration 
Export/Import 
• 
Ability to export cluster 
configuration, which can then 
be used to restore a 
configuration to the original 
cluster or a different cluster. 
 
Drain Based 
Upgrade 
• 
Nodes are prevented from 
rebooting or restarting 
protocol services until all 
SMB clients have 
disconnected from the node. 
 
OneFS 9.2.1 
Release 
Feature 
Info 
OneFS 9.2.1 
May 2021 
PowerScale 
Portfolio Support 
• 
OneFS support for the new 
PowerScale H700, H7000, 
A300, and A3000 platforms.

---

## onefs-release-contents::chunk_20

from rebooting or restarting protocol services until all SMB clients have disconnected from the node. OneFS 9.2.1 Release Feature Info OneFS 9.2.1 May 2021 PowerScale Portfolio Support • OneFS support for the new PowerScale H700, H7000, A300, and A3000 platforms.

22 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
OneFS 9.3 
Release 
Feature 
Info 
OneFS 9.3  
October 2021 
PowerScale 
Portfolio Support 
• 
OneFS support for the new 
PowerScale P100 and B100 
performance and backup 
accelerator nodes. 
Writable Snapshots 
• 
Enables the creation and 
management of a space and 
time efficient, modifiable 
copy of a regular OneFS 
snapshot. 
NFS v4.1 and v4.2 
Support 
• 
Connectivity support for 
versions 4.1 and 4.2 of the 
NFS file access protocol. 
Long filename 
support 
• 
Provision for file names up 
to 1024 bytes, allowing 
support for long names in 
UTF-8 multi-byte character 
sets. 
Inline data in inodes 
• 
Data efficiency feature 
allowing a small file’s data to 
be stored in unused space 
within its inode block. 
HDFS ACLs 
• 
Provide support for HDFS-
4685 access control lists, 
allowing users to manage 
permissions on their 
datasets from Hadoop 
clients. 
Job engine 
exclusions 
• 
Allow Job engine jobs to be 
run on a defined subset of a 
cluster’s nodes. 
 
 
CloudPools Recall  
• 
Improved CloudPools file 
recall & rehydrate 
performance. 
 
Safe SMB client 
disconnects 
• 
Allows SMB clients the 
opportunity to flush their

---

## onefs-release-contents::chunk_21

exclusions • Allow Job engine jobs to be run on a defined subset of a cluster’s nodes. CloudPools Recall • Improved CloudPools file recall & rehydrate performance. Safe SMB client disconnects • Allows SMB clients the opportunity to flush their

23 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Release 
Feature 
Info 
caches prior to being 
disconnected. 
 
S3 protocol 
enhancements 
• 
Added support for S3 
chunked upload, multi-object 
delete, and non-slash 
delimiters for lists. 
 
OneFS 9.4 
Release 
Feature 
Info 
OneFS 9.4  
April 2022 
SmartSync Data 
Mover 
• 
Introduction of a new 
OneFS SmartSync data 
mover, allowing flexible data 
movement and copying, 
incremental resyncs, push 
and pull data transfer, and 
one-time file to object copy. 
IB to Ethernet 
Migration 
• 
Non-disruptive rolling 
Infiniband to Ethernet back-
end network migration for 
legacy Gen6 clusters. 
Secure Boot 
• 
Secure boot support is 
extended to include the 
F900, F600, F200, 
H700/7000, and A300/3000 
platforms. 
Smarter 
SmartConnect 
Diagnostics 
• 
Identifies non-resolvable 
nodes and provides their 
detailed status, allowing the 
root cause to be easily 
pinpointed. 
QLC Drive Support 
• 
Support is added in OneFS 
9.4 to accommodate quad-
level cell (QLC) NVMe 
drives in the F900 and F600 
platform nodes.

---

## onefs-release-contents::chunk_22

non-resolvable nodes and provides their detailed status, allowing the root cause to be easily pinpointed. QLC Drive Support • Support is added in OneFS 9.4 to accommodate quad- level cell (QLC) NVMe drives in the F900 and F600 platform nodes.

24 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
In-line Dedupe 
• 
In-line deduplication will be 
enabled by default on new 
OneFS 9.4 clusters. 
Clusters upgraded to 
OneFS 9.4 will maintain 
their current dedupe 
configuration. 
 
Healthcheck Auto-
updates 
• 
Automatic monitoring, 
download, and installation of 
new healthcheck packages 
as they are released. 
 
CloudIQ Protocol 
Statistics 
• 
New protocol statistics 
‘count’ keys are added, 
allowing performance to be 
measured over a specified 
time window and providing 
point-in-time protocol 
information. 
 
SRS Alerts and 
CELOG Event 
Limiting 
• 
Prevents CELOG from 
sending 151 event types 
(out of 433 total) to Dell 
SRS and restricts CELOG 
alerts from customer-
created channels. 
 
CloudPools 
Statistics 
• 
Automated statistics 
gathering on CloudPools 
accounts and policies 
providing insights for 
planning and 
troubleshooting CloudPools-
related activities.

---

## onefs-release-contents::chunk_23

from sending 151 event types (out of 433 total) to Dell SRS and restricts CELOG alerts from customer- created channels. CloudPools Statistics • Automated statistics gathering on CloudPools accounts and policies providing insights for planning and troubleshooting CloudPools- related activities.

25 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
OneFS 9.5 
Release 
Feature 
Info 
OneFS 9.5  
January 2023 
Security / Federal 
APL 
• 
Authentication: Multi-factor 
authentication with 
CAC/PIV; SSO for WebUI; 
PKI-based authentication. 
• 
Data Encryption: FIPS 140-
2 Data in Flight for major 
protocols; FIPS 140-2 Data 
at Rest via SEDs; SEDs 
Master Key rekey; TLS 1.2 
support. 
• 
Host-Based Firewall: 
Restriction of management 
interface to specified 
subnet & hosts to specified 
IP pools. 
• 
IPV6-only Network Support: 
Support for USGv6R1 
standard. 
• 
Common Criteria 
Certification: International 
security standards 
compliance. 
• 
DoD APL Enablement: 
Implementation of 300+ 
DISA requirements to 
support DoD Approved 
Products List (APL) 
inclusion. 
 
SmartQoS 
• 
Ability to limit NFS3, NFS4, 
NFSoRDMA, S3 or SMB 
protocol operations per 
second (Protocol Ops), 
including mixed traffic to 
the same workload. 
 
SmartPools 
• 
SmartPools tier and node 
pool transfer limits, 
providing spillover 
protection.

---

## onefs-release-contents::chunk_24

Products List (APL) inclusion. SmartQoS • Ability to limit NFS3, NFS4, NFSoRDMA, S3 or SMB protocol operations per second (Protocol Ops), including mixed traffic to the same workload. SmartPools • SmartPools tier and node pool transfer limits, providing spillover protection.

26 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
 
SupportAssist 
• 
Next generation remote 
connectivity framework for 
transmission of  events, 
logs, and telemetry data 
from a PowerScale cluster 
to Dell Support. 
 
F-series 
Performance 
• 
F600 & F900 streaming 
read performance 
enhancement via metadata 
and lock caching, multi-
stream RBM, and SSD L2 
bypass. 
 
F200 Networking 
• 
100GbE frontend & 
backend support for F200 
nodes. 
 
H-series/A-series 
Networking 
• 
Mellanox CX6 support for 
H700, H7000, A300, and 
A3000 nodes. 
 
QLC SED Drives 
• 
QLC non-FIPS 15TB & 
30TB drive support. 
 
Node Management 
• 
Enablement of 1GbE 
management interface on 
PowerScale nodes.

27 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
OneFS 9.6 
Release 
Feature 
Info 
OneFS 9.6  
January 2023 
APEX File Storage 
for AWS 
• 
Cloud-only Release. 
• 
Data mobility to the cloud. 
• 
Up to 1PB per cluster 
namespace. 
• 
Leading file performance. 
• 
Up to 6 SSD nodes per 
cluster. 
• 
Support for OneFS 
enterprise features. 
 
OneFS 9.7 
Release 
Feature 
Info 
OneFS 9.7  
December 2023 
Cloud 
• 
APEX File Storage for AWS 
60% capacity increase. 
• 
Streamlined and automated 
APEX provisioning and 
deployment via Terraform 
scripts. 
• 
HDFS, FTP, and SmartQoS 
support. 
Configuration 
• 
Cluster configuration 
backup and restore utility. 
Networking 
• 
Externally managed IP 
addresses. 
Parallel Restripe 
• 
Job engine support for 
parallel restriper jobs. 
 
Performance 
• 
Streaming write 
performance improvements 
for NVMe-based F710 and 
F210 all-flash platforms.

---

## onefs-release-contents::chunk_25

and SmartQoS support. Configuration • Cluster configuration backup and restore utility. Networking • Externally managed IP addresses. Parallel Restripe • Job engine support for parallel restriper jobs. Performance • Streaming write performance improvements for NVMe-based F710 and F210 all-flash platforms.

28 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
 
Platform 
• 
Infrastructure support for 
next generation all-flash 
node hardware platforms. 
 
SmartConnect 
• 
SmartConnect awareness 
for SMB3 Multichannel. 
 
SmartSync 
• 
SmartSync GCP support. 
 
Authentication 
• 
Single sign-on (SSO) 
lookup enhancements. 
OneFS 9.8 
Release 
Feature 
Info 
OneFS 9.8  
April 2024 
Cloud 
• 
APEX File Storage for 
Azure 
• 
Cirrus single sign-on (SSO) 
support for PowerScale 
WebUI 
NFS Protocol 
• 
RDMA for NFSv4.1 
Networking 
• 
Source-based routing 
support for IPv6 networks.  
SmartThrottling 
• 
Job engine automatic 
impact management and 
resource throttling. 
 
Platform 
• 
Infrastructure support for 
next generation F910 all-
flash node hardware 
platform. 
 
Support 
• 
Smart Log diagnostic 
gathering and HealthCheck 
enhancements. 
• 
IceAge automated core file 
analysis tool.

---

## onefs-release-contents::chunk_26

networks. SmartThrottling • Job engine automatic impact management and resource throttling. Platform • Infrastructure support for next generation F910 all- flash node hardware platform. Support • Smart Log diagnostic gathering and HealthCheck enhancements. • IceAge automated core file analysis tool.

29 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
 
OneFS 9.9 
Release 
Feature 
Info 
OneFS 9.9  
August 2024 
Events and Alerts 
• 
Automatic maintenance 
mode. 
• 
Superfluous alerting 
suppression. 
Upgrade 
• 
NDU improved pre-upgrade 
health checks  
• 
SMB disruption reduction. 
Protocols 
• 
Support for a multipath 
NFS driver for Linux client 
systems. 
• 
Complete removal of 
deprecated SWIFT object 
protocol. 
Networking 
• 
Nvidia Spectrum-4 switch 
support for F710 200GbE.  
• 
Support for in-field Ethernet 
adapter (NIC) swaps.  
CoS / QoS Tagging 
• 
Differentiated Service Code 
Point) (DSCP) support 
added, enabling 
class/quality of service 
tagging. 
 
Platform 
• 
Infrastructure support for 
F710 nodes with 61TB QLC 
drives and a 200Gb/s back-
end Ethernet network. 
 
Support 
• 
IPv6 networking added for 
SupportAssist phone home 
service.

---

## onefs-release-contents::chunk_27

Differentiated Service Code Point) (DSCP) support added, enabling class/quality of service tagging. Platform • Infrastructure support for F710 nodes with 61TB QLC drives and a 200Gb/s back- end Ethernet network. Support • IPv6 networking added for SupportAssist phone home service.

30 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
OneFS 9.10 
Release 
Feature 
Info 
OneFS 9.10  
December 2024 
Metadata Indexing 
• 
Introduction of MetadataIQ 
ElasticSearch-based off-
cluster metadata indexing 
and management solution. 
 
Networking 
• 
Front-end and back-end 
InfiniBand networking 
option for the F910 and 
F710 platforms. 
Platform 
• 
Support for F910 nodes 
with 61TB QLC SSD drives 
and a 200Gb/s back-end 
Ethernet network. 
• 
Support for 24TB HDDs on 
A-series and H-series 
nodes. 
 
Security 
• 
OpenSSL 3.0 and TLS 1.3 
transport layer security 
support. 
• 
WebUI conversion of Ext 
JS Web UI pages to React 
JS. 
 
Support 
• 
Healthcheck WebUI 
improvements 
 
• 
SupportAssist rebranded to 
‘Dell Technologies 
Connectivity’ 
 
OneFS 9.11 
Release 
Feature 
Info 
OneFS 9.11  
April 2025 
Cloud 
• 
Support for Dell 
PowerScale for Microsoft 
Azure

---

## onefs-release-contents::chunk_28

conversion of Ext JS Web UI pages to React JS. Support • Healthcheck WebUI improvements • SupportAssist rebranded to ‘Dell Technologies Connectivity’ OneFS 9.11 Release Feature Info OneFS 9.11 April 2025 Cloud • Support for Dell PowerScale for Microsoft Azure

31 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Release 
Feature 
Info 
Networking 
• 
Dynamic IP pools added to 
SmartConnect Basic 
Platform 
• 
Support for 122TB QLC 
SSD drives on F910 and 
F710 nodes  
 
Protocol 
• 
S3 cluster status API 
 
Replication 
• 
SmartSync Backup-to-
Object 
• 
SyncIQ new policy default 
 
Support 
• 
Seamless ESRS to DTCS 
migration 
 
 
Reliability 
• 
Software Journal Mirroring 
for high-capacity QLC SSD 
nodes. 
OneFS 9.12 
Release 
Feature 
Info 
OneFS 9.12  
August 2025 
Networking 
• 
SmartConnect dynamic as 
default allocation method. 
Platform 
• 
PowerScale PA110 
accelerator front-end 
Infiniband support. 
• 
F-series fast reboots. 
 
Protocol 
• 
S3 Object Lock. 
• 
S3 Immutable SmartLock 
bucket for tamper-proof 
objects. 
• 
S3 protocol access logging. 
• 
S3 bucket logging. 
 
Security 
• 
Multi-party authorization for 
privileged actions.

---

## onefs-release-contents::chunk_29

• PowerScale PA110 accelerator front-end Infiniband support. • F-series fast reboots. Protocol • S3 Object Lock. • S3 Immutable SmartLock bucket for tamper-proof objects. • S3 protocol access logging. • S3 bucket logging. Security • Multi-party authorization for privileged actions.

32 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
Release 
Feature 
Info 
• 
Root lockdown mode. 
• 
Secure Snapshots with 
MPA override to protect 
data when retention period 
has not expired. 
 
Support 
• 
Custer-level inventory 
request API. 
• 
In-field support for back-
end NIC changes. 
 
Reliability 
• 
Auto Remediation self-
diagnosis and healing 
capability. 
 
OneFS 9.13 
Release 
Feature 
Info 
OneFS 9.13  
December 2025 
Data Mobility 
• 
SmartSync incremental file-
to-object enhancements. 
• 
CloudPools support for 
VDC endpoints. 
Platform 
• 
Support for 400GbE NIC 
changes on F910. 
• 
In-field support for back-
end NIC changes for F900, 
F700, & F200. 
 
Protocol 
• 
S3 TCP port configuration 
& multi-part uploads. 
• 
Official SDK support. 
 
Security 
• 
TLS 1.3 transport layer 
security support phase 2. 
 
Serviceability 
• 
Dynamic licensing.

---

## onefs-release-contents::chunk_30

• In-field support for back- end NIC changes for F900, F700, & F200. Protocol • S3 TCP port configuration & multi-part uploads. • Official SDK support. Security • TLS 1.3 transport layer security support phase 2. Serviceability • Dynamic licensing.

33 
Dell PowerScale OneFS Release Contents 
New Features, Functionality, and Enhancements 
 
Summary 
This document summarizes the new features and functionality contained in each OneFS 
release, from OneFS 7.1 in October 2013 to present. OneFS releases are assigned a 
release number (for example, 8.2.1) based on the following criteria: 
Release Digit  
Release Type 
Description 
First 
Major 
A release with functionality that provides a 
substantial move forward in the product 
Second 
Major 
Release with functionality in the same family 
and theme as the parent major release. 
Third 
Minor 
New features and functionality added 
between major releases. 
 
Take the next step 
Contact your Dell sales representative or authorized reseller to learn more about how Dell 
PowerScale NAS storage solutions can benefit your organization. 
Visit Dell PowerScale to compare features and find more information.