## synciq-best-practices::chunk_0

White Paper 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Abstract 
This white paper will give you an understanding of the unique 
features and benefits of the SyncIQ™ architecture, an EMC® 
Isilon® software application that enables you to flexibly manage 
and automate data replication between two Isilon clusters.  In 
this Best Practices Guide you will also discover best practices 
and use cases to help you maximize the benefits of cluster-to-
cluster replication. 
 
April 2011 
 
BEST PRACTICES FOR DATA REPLICATION  
WITH EMC ISILON SYNCIQ

2
Best Practices for Data Replication with EMC Isilon SyncIQ 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Copyright © 2011 EMC Corporation. All Rights Reserved. 
 
EMC believes the information in this publication is accurate of 
its publication date. The information is subject to change 
without notice. 
 
The information in this publication is provided “as is”. EMC 
Corporation makes no representations or warranties of any kind 
with respect to the information in this publication, and 
specifically disclaims implied warranties of merchantability or 
fitness for a particular purpose. 
 
Use, copying, and distribution of any EMC software described in 
this publication requires an applicable software license. 
 
For the most up-to-date listing of EMC product names, see EMC 
Corporation Trademarks on EMC.com. 
 
VMware is a registered trademark of VMware, Inc. All other 
trademarks used herein are the property of their respective 
owners. 
 
Part Number h8224

---

## synciq-best-practices::chunk_1

software license. For the most up-to-date listing of EMC product names, see EMC Corporation Trademarks on EMC.com. VMware is a registered trademark of VMware, Inc. All other trademarks used herein are the property of their respective owners. Part Number h8224

3
Best Practices for Data Replication with EMC Isilon SyncIQ 
Table of Contents 
Executive summary.................................................................................................. 5 
Fast, reliable replication ..................................................................................................... 5 
Use cases ............................................................................................................... 6 
Disaster recovery ................................................................................................................ 6 
Business continuance ........................................................................................................ 6 
Disk-to-disk backup and restore ......................................................................................... 7 
Remote archive .................................................................................................................. 7 
Architecture and features ........................................................................................ 7 
Leveraging clustered storage architecture .......................................................................... 7 
Asynchronous source-based replication ............................................................................. 8 
Flexible policy-driven replication ........................................................................................ 9 
Efficient block-based deltas ............................................................................................. 10 
Source-cluster snapshot integration ................................................................................. 10 
Target-cluster snapshots .................................................................................................. 11 
SmartConnect integration ................................................................................................. 12 
Target Aware Initial Sync................................................................................................... 13 
Tunable replication performance ...................................................................................... 13 
Real-time monitoring and historical reports ...................................................................... 14 
Policy assessment ............................................................................................................ 14 
What’s new in SyncIQ 3.0 ...................................................................................... 14 
Performance improvements .............................................................................................. 14 
Snapshot integration removes need for treewalks ............................................................ 14 
Copy-job changes ............................................................................................................. 15 
Source and target cluster association persistence ........................................................ 17 
Target protection with restricted writes ............................................................................. 17 
Assess SyncIQ changes .................................................................................................... 17 
Improved authentication integration ................................................................................ 17 
Multiple jobs targeting a single directory tree no longer supported ................................... 17 
Hard-link replication now supported ................................................................................ 18 
Report changes ................................................................................................................ 18 
SyncIQ best practices and tips ............................................................................... 18 
Avoiding full dataset replications ..................................................................................... 18 
Selecting the right source replication dataset ................................................................... 19 
Including or excluding source-cluster directories .......................................................... 19 
Configuring SyncIQ policy file selection criteria ............................................................ 20 
Disaster recovery from a target Isilon cluster .................................................................... 21 
Performance tuning .......................................................................................................... 22 
Guidelines .................................................................................................................... 22

---

## synciq-best-practices::chunk_2

18 Selecting the right source replication dataset ................................................................... 19 Including or excluding source-cluster directories .......................................................... 19 Configuring SyncIQ policy file selection criteria ............................................................ 20 Disaster recovery from a target Isilon cluster .................................................................... 21 Performance tuning .......................................................................................................... 22 Guidelines .................................................................................................................... 22

4
Best Practices for Data Replication with EMC Isilon SyncIQ 
Limitations and restrictions .......................................................................................... 23 
Using Isilon SnapshotIQ on the target .......................................................................... 24 
Using SmartConnect with SyncIQ .................................................................................. 24 
Using SmartConnect on the source cluster ....................................................................... 24 
Using SmartConnect zones on the target cluster ........................................................... 25 
Monitoring SyncIQ ............................................................................................................ 26 
Policy job monitoring .................................................................................................... 27 
Performance monitoring ............................................................................................... 27 
Troubleshooting with SyncIQ logs................................................................................. 28 
Target aware initial synchronization ................................................................................. 29 
Version compatibility ............................................................................................. 29 
Additional tips ...................................................................................................... 30 
Conclusion ............................................................................................................ 30

---

## synciq-best-practices::chunk_3

the target cluster ........................................................... 25 Monitoring SyncIQ ............................................................................................................ 26 Policy job monitoring .................................................................................................... 27 Performance monitoring ............................................................................................... 27 Troubleshooting with SyncIQ logs................................................................................. 28 Target aware initial synchronization ................................................................................. 29 Version compatibility ............................................................................................. 29 Additional tips ...................................................................................................... 30 Conclusion ............................................................................................................ 30

5
Best Practices for Data Replication with EMC Isilon SyncIQ 
Executive summary  
Sophisticated, fast, and easy to use, EMC® Isilon® SyncIQ™ replication software 
provides data-intensive businesses with an unparalleled solution for replication over 
the wide area network (WAN) and local area network (LAN). 
Fast, reliable replication 
All businesses want to protect themselves against unplanned outages and data loss.  
Typically, the best way to do this is to create and keep copies of important data so it 
can always be recovered.  There are many approaches to creating and maintaining 
data copies.  The right approach depends on the criticality of the data to the 
business, and its timeliness—how long the business can afford to be without it. 
As the sheer amount of data requiring management grows, it puts considerable strain 
on a company’s ability to protect its data.  Backup windows shrink, single systems 
(heads, controllers, tape, and so on) on the source and destination sites become 
bottlenecks, and logical and physical divisions of data fragment data protection 
processes. The result is increasing risk to your data and more complexity in managing 
it.   
Isilon SyncIQ offers powerful, flexible, and easy-to-manage data replication for 
disaster recovery, business continuance, disk-to-disk backup, and remote disk 
archiving. 
SyncIQ delivers unique replication performance—every node in an Isilon cluster can 
send and receive data, so replication actually gets faster as your data store grows, 
and you can configure the cluster to take advantage of any available network 
bandwidth.  Because both the source and the target can scale to multiple petabytes 
without fragmentation into multiple volumes or file systems, data replication starts 
simple and stays that way as the system scales to provide a solid foundation for 
disaster recovery.   
A simple and intuitive web-based user interface (UI) allows you to easily organize 
SyncIQ replication job rates and priorities to match your business continuance 
priorities. Typically, a SyncIQ recurring job protects the data required for each major 
recovery point objective in a company’s disaster recovery plan—for example, it 
synchronizes customer data every 6 hours, HR data every 2 days, and so on.  You 
would configure a directory, file system, or even specific files for more or less frequent 
replication based on their business criticality.  You would create remote archive 
copies of out-of-use data that needs to be retained so you can reclaim valuable 
capacity in your production system.  
Replication should be nondisruptive, and SyncIQ takes as much or as little system 
resource and network bandwidth as you specify.  By default SyncIQ will take all idle 
system and network resources.  For additional flexibility, you can limit SyncIQ system 
or network resource utilization and schedule synchronization jobs for off-peak hours.

---

## synciq-best-practices::chunk_4

as little system resource and network bandwidth as you specify. By default SyncIQ will take all idle system and network resources. For additional flexibility, you can limit SyncIQ system or network resource utilization and schedule synchronization jobs for off-peak hours.

6
Best Practices for Data Replication with EMC Isilon SyncIQ 
SyncIQ 3.0 includes new features and functionality that dramatically improve most 
customer replication times, secure replicated data against accidental alteration, and 
improve source and target association persistence. 
Use cases  
Isilon SyncIQ offers powerful, flexible, and easy-to-manage data replication for 
disaster recovery, business continuance, disk-to-disk backup, and remote disk 
archive. 
As shown in Figure 1, SyncIQ replicates data from a primary site to a secondary, local 
or remote site, creating a copy for disaster recovery, business continuance, disk-to-
disk backup, or remote archiving purposes.  SyncIQ is powerful and flexible, and can 
deliver the data protection requirements of data-intensive, core, revenue workflows 
across multiple industries.  
 
Figure 1. SyncIQ over LAN or WAN 
Disaster recovery  
Disaster recovery requires quick and efficient replication of critical business data to a 
secondary (local or remote) site. 
SyncIQ delivers high performance, asynchronous replication of data over short (LAN) 
or long distances (WAN), providing protection from site-specific and regional 
disasters.  SyncIQ has a very robust policy-driven engine that allows you to customize 
your replication datasets to minimize system impact while still meeting your data 
protection requirements. 
Business continuance 
By definition, a business continuance solution needs to meet your most aggressive 
recovery point objectives for your most timely, critical data. SyncIQ’s highly efficient

---

## synciq-best-practices::chunk_5

your replication datasets to minimize system impact while still meeting your data protection requirements. Business continuance By definition, a business continuance solution needs to meet your most aggressive recovery point objectives for your most timely, critical data. SyncIQ’s highly efficient

7
Best Practices for Data Replication with EMC Isilon SyncIQ 
architecture—performance that scales to maximize usage of any available network 
bandwidth—gives you the best-case replication time for tight recovery point 
objectives (RPO). You can also integrate SyncIQ with unlimited snapshots, which 
allows you to store as many copies of your data as needed to support secondary 
activities like backup to tape. 
Disk-to-disk backup and restore 
SyncIQ increases the performance of large-scale backups and restores.   
Enterprise IT organizations face increasingly complex backup environments with 
costly operations, shrinking backup and restore windows, and increasing service-
level agreement (SLA) requirements. Backups to tape are traditionally slow and hard 
to manage as they grow, and are compounded by the size and rapid growth of digital 
content and unstructured data. SyncIQ is a superior disk-to-disk backup and restore 
solution that delivers unmatched performance and simplicity, enabling IT 
organizations to reduce backup and restore times and costs, eliminate complexity, 
and minimize risk. With Isilon scale-out network-attached storage (NAS), petabytes of 
backup storage can be managed within a single system—as one volume and one file 
system—and can be the disk backup target for multiple Isilon clusters.  
Remote archive 
For data that is too valuable to throw away, but not time-critical enough to justify 
maintaining it on your production storage, replicate it with SyncIQ to a secondary 
local or remote site and reclaim the space on your primary system.  Deletion of data 
on the source does not affect the target, leaving you with a remote archive for disk-
based tertiary storage applications or for staging data before it moves to offline 
storage. Remote archiving is ideal for intellectual property preservation, long-term 
records retention, or project archiving. 
Architecture and features 
Leveraging clustered storage architecture 
SyncIQ leverages the full complement of resources in an Isilon cluster and maximizes 
the unique capabilities of the OneFS™ file system. SyncIQ uses a policy-driven 
engine to execute replication jobs across all nodes in the cluster. To allow for high 
flexibility and resource management, you can create any number of SyncIQ policies.  
Each SyncIQ policy defines a job profile with a source directory and a target location 
(cluster and directory) that can be executed based on a user-defined schedule or 
started manually.  This flexibility allows you to replicate datasets based on predicted 
cluster usage, network capabilities, and requirements for data availability. 
When a SyncIQ job initiates (from either a scheduled or manual policy), the system 
first takes a snapshot of the data to be replicated. SyncIQ compares this snapshot to 
the snapshot from the previous replication job, which enables it to quickly identify 
the changes that need to be addressed.  SyncIQ then pools the aggregate resources

---

## synciq-best-practices::chunk_6

takes a snapshot of the data to be replicated. SyncIQ compares this snapshot to the snapshot from the previous replication job, which enables it to quickly identify the changes that need to be addressed. SyncIQ then pools the aggregate resources

8
Best Practices for Data Replication with EMC Isilon SyncIQ 
from the cluster, splitting the replication job to smaller work items and farming them 
out to multiple workers across all nodes in the cluster. Each worker scans a part of the 
snapshot differential for changes and transfers those changes to the target cluster.  
While the cluster resources are managed to maximize replication performance, you 
have control of the resources, which allows you to throttle the performance of the job 
engine and decrease the impact on other workflows using the cluster. 
Replication workers on the source cluster are paired with workers on the target cluster 
so the benefits of parallel and distributed data transfer are carried over to the target 
cluster. As more jobs run concurrently, SyncIQ will employ more workers to utilize 
more cluster resources.  As more nodes are added to the cluster, file system 
processing on the source cluster and file transfer to the remote cluster are 
accelerated, a benefit of the Isilon scale-out NAS architecture.  
SyncIQ provides a simple, intuitive, web-based UI to create policies, manage jobs, 
and view reports. In addition to the web-based interface all SyncIQ functionality is 
available through a command line interface that can be launched remotely over SSH 
connections. A full list of CLI commands is available by running the following CLI 
command on an Isilon node: isi sync –h 
 
Figure 2. SyncIQ work distribution across the cluster 
Asynchronous source-based replication 
SyncIQ is an asynchronous remote replication tool. It differs from synchronous remote 
replication tools where writes to the local storage system are not acknowledged back 
to the client until those writes are committed to the remote storage system. SyncIQ

---

## synciq-best-practices::chunk_7

replication SyncIQ is an asynchronous remote replication tool. It differs from synchronous remote replication tools where writes to the local storage system are not acknowledged back to the client until those writes are committed to the remote storage system. SyncIQ

9
Best Practices for Data Replication with EMC Isilon SyncIQ 
asynchronous replication allows the cluster to respond quickly to client file system 
requests while replication jobs run in the background per policy settings. 
SyncIQ is source-based, which means it is aware only of changes that have occurred 
on the source cluster. Those changes can be new files, changed files, metadata 
changes, or file deletions.  
Notes:  
 To better protect distributed workflow data, SyncIQ 3.0 prevents changes on 
target directories that are associated with a SyncIQ job. In previous versions, 
SyncIQ was not aware of changes made on the target cluster, so it was necessary 
that replication destination paths on the target cluster were protected from 
manual changes.  If your workflow requires writeable targets, with SyncIQ 3.0 you 
must break the source/target association before writing data to a target directory, 
and any subsequent re-activation of the synchronize association will require a full 
synchronization. 
 SyncIQ does not support bi-directional replication jobs or replicating a source 
dataset to a target location and then replicating it back from the target location to 
the original source dataset. 
Flexible policy-driven replication 
SyncIQ policies allow you to replicate only directories and files that meet specified 
criteria. Once a policy has run, replication occurs only for data from the changed files. 
File selection criteria are comprehensive, yet easy to use and can be used to build 
flexible policies that support varied workflows. Selection criteria include:  
 filename 
 include/exclude directories 
 file size 
 file accessed 
 created and modified times 
 file system type 
 regular expression (file and path names)   
With policy-driven replication, you can reduce the amount of time, processing 
resources, and network resources by replicating only the data you need. For example, 
in VMware environments you can select individual virtual machines (VMs) based on 
the directory of each VM (unlike other replication tools that require you to choose 
entire volumes with multiple VMs). In the case of user home directories, you can 
exclude large MP3 or JPG/GIF media files that are not critical to the business 
operations.

---

## synciq-best-practices::chunk_8

each VM (unlike other replication tools that require you to choose entire volumes with multiple VMs). In the case of user home directories, you can exclude large MP3 or JPG/GIF media files that are not critical to the business operations.

10
Best Practices for Data Replication with EMC Isilon SyncIQ 
Efficient block-based deltas 
The initial replication of a new policy or a changed policy will perform a full baseline 
replication of the entire dataset based on the directory and file selection policy 
criteria. This baseline replication is necessary to ensure all original data is replicated 
to the remote location. However, every incremental job execution of that policy will 
transfer only the blocks (8K per block) that have changed since the previous run (on a 
per-file basis). SyncIQ uses internal file system structures to identify changed blocks, 
and along with parallel data transfer across the cluster, minimizes the replication 
time window and network use. This is critical in cases where only a small fraction of 
the dataset has changed, as in the case of virtual machine VMDK files in which only a 
block may have changed in a multi-gigabyte virtual disk file.  Another example is 
where an application changed only the file metadata (ACLs, Windows ADS).  In these 
cases while the replication job scans the entire dataset for changes, only a fraction of 
the dataset is transferred to update the target cluster dataset. 
Notes:  
 Certain policy definition changes cause incremental jobs to conduct a full 
baseline dataset replication.  The next section describes how to avoid full 
baseline replication when changing a policy definition.  
 In SyncIQ 3.0, when a file or an entire directory at the source of a replicated 
dataset is moved to a new location, it is simply moved to the target as well. In 
versions earlier than SyncIQ 3.0, the entire file, or files in the directory, will be 
replicated. 
Source-cluster snapshot integration 
To provide point-in-time data protection, when a SyncIQ job starts, it automatically 
generates a snapshot of the dataset on the source cluster. Once it takes a snapshot, 
it bases all replication activities (scanning, data transfer) on the snapshot view; any 
changes that occur to the file system during the replication job execution do not 
affect the replicated dataset (those changes are picked up in incremental job 
executions).  OneFS creates instantaneous snapshots before the job begins so you do 
not have to block application activity for the entire replication operation.  
Source-cluster snapshots are named SIQ-<policy-id>-[new,latest], where <policy-id> is 
the unique system-generated policy identifier. SyncIQ compares the snapshot that is 
currently running with the latest snapshot from the previous job and determines the 
changed files and blocks to transfer. Each time a SyncIQ job completes, the existing 
latest snapshot is replaced with the most recent snapshot, which in turn, becomes 
the latest snapshot. 
Regardless of the existence of other inclusion or exclusion directory paths, only one 
snapshot is created on the source cluster at the beginning of the job based on the 
policy root directory path.

---

## synciq-best-practices::chunk_9

which in turn, becomes the latest snapshot. Regardless of the existence of other inclusion or exclusion directory paths, only one snapshot is created on the source cluster at the beginning of the job based on the policy root directory path.

11
Best Practices for Data Replication with EMC Isilon SyncIQ 
 
Note: This source-cluster snapshot does not require a SnapshotIQ™ module license. 
When a SyncIQ policy is deleted, SyncIQ also deletes any snapshots that the policy 
created. 
 
When application consistency is important, you can integrate the replication job with 
third-party application agents that can execute the replication job remotely by using 
the SyncIQ command line over an SSH session.  
 
For example, in a VMware environment you can quiesce the virtualized application 
(inside a virtual machine) by taking a VMware snapshot before manually running a 
SyncIQ job. After the SyncIQ job finishes, you can remove the VMware snapshot. You 
can implement this sequence of operations by using scripts that call the VMware 
commands from a local host and the remote SyncIQ CLI commands over an SSH 
session that is connected to the source cluster. 
 
 
Figure 3. SyncIQ point-in-time consistent replication 
Target-cluster snapshots 
In addition to integrating OneFS snapshots on the source cluster for point-in-time 
consistency, you can generate a snapshot of the directory on the target cluster. First, 
take a snapshot on the target cluster at the beginning of the replication job (before 
data is transferred) to prevent unintentionally overwriting the existing data. Then take 
a second snapshot on the target cluster when the replication job completes. This

---

## synciq-best-practices::chunk_10

take a snapshot on the target cluster at the beginning of the replication job (before data is transferred) to prevent unintentionally overwriting the existing data. Then take a second snapshot on the target cluster when the replication job completes. This

12
Best Practices for Data Replication with EMC Isilon SyncIQ 
creates multiple, space-efficient versions of the replicated dataset to choose from on 
the target cluster. This is very useful for archiving purposes when you want to use a 
near-line Isilon cluster (typically an NL-Series) to maintain different versions of 
replicated datasets archived from primary Isilon IQ storage (typically S-series or X-
series Isilon IQ clusters). 
Note: SnapshotIQ is a licensed software module that delivers a powerful snapshot 
management tool to create, schedule, and expire an unlimited number of OneFS 
snapshots anywhere in the OneFS file system. To enable target-cluster snapshots you 
must have a SnapshotIQ module license and enable the Isilon SnapshotIQ module on 
the target cluster.  For more details please see http://www.isilon.com/snapshotiq.  
SmartConnect integration 
SyncIQ uses standard Gigabit and10 Gigabit Ethernet ports available on cluster nodes 
to send replication data from the source to the destination cluster. By selecting a 
predefined SmartConnect™ IP address pool you can restrict replication processing to 
specific nodes both on the source and target clusters. This is useful when you want to 
guarantee that replication jobs are not competing with other applications for specific 
node resources. By selecting specific nodes, you can also define which networks are 
used for replication data transfer.   
Once you define a SmartConnect IP address pool on the source cluster through the 
Isilon web administration interface, you can use that IP address pool globally across 
all policies on the source cluster, or you can select different IP address pools for use 
on a per-policy basis. To restrict sending replication traffic to specific nodes on the 
target cluster you can associate (globally or per policy) a SmartConnect zone name 
with the target cluster.  
Note: If you change the Default Policy global settings, the default policy will not 
update existing policies but will be used when creating new policies.

---

## synciq-best-practices::chunk_11

you can associate (globally or per policy) a SmartConnect zone name with the target cluster. Note: If you change the Default Policy global settings, the default policy will not update existing policies but will be used when creating new policies.

13
Best Practices for Data Replication with EMC Isilon SyncIQ 
 
 
Figure 4. SyncIQ web-based management interface 
Target Aware Initial Sync 
The Target Aware Initial Sync advanced feature, available only through the command 
line interface, allows you to reduce network traffic during initial baseline replication.  
In cases where most of the dataset already resides on both the source and target 
cluster, this feature can accelerate the initial baseline replication job by using more 
CPU resources (hashing file data) to reduce the amount of data transferred over the 
network.  This is also helpful in disaster recovery cases where data changes that 
occur on the target cluster after a failover need to be replicated back to the original 
source location with minimal changes to the datasets. 
Tunable replication performance  
SyncIQ uses aggregate resources across the cluster to maximize replication 
performance. In fact, it could potentially consume more resources than it requires, 
thus affecting other cluster operations and client response. In other situations the 
default performance configurations (number of workers, network use, CPU use) may

---

## synciq-best-practices::chunk_12

the cluster to maximize replication performance. In fact, it could potentially consume more resources than it requires, thus affecting other cluster operations and client response. In other situations the default performance configurations (number of workers, network use, CPU use) may

14
Best Practices for Data Replication with EMC Isilon SyncIQ 
not be optimized for certain datasets. SyncIQ allows you to control how resources are 
consumed and balance replication performance with other file system operations. 
You can control how much bandwidth SyncIQ uses and the rate at which it processes 
files on a cluster-wide level, as well as which nodes and how many workers it should 
use on each node on a per-SyncIQ-policy basis.  
Real-time monitoring and historical reports 
SyncIQ allows you to monitor the status of policies and replication jobs with real-time 
performance indicators and resource utilization. This allows you to determine how 
different policy settings affect job execution and impact performance on the cluster. 
In addition, every job execution produces a comprehensive report that can be 
reviewed for troubleshooting and performance analysis. This real-time report provides 
you with information about the amount of data replicated and the effectiveness of 
those jobs, enabling you to tune resources accordingly.  
Policy assessment  
SyncIQ can conduct a trial run of your policy without actually transferring file data 
between locations. SyncIQ can scan the dataset and provide a detailed report of how 
many files and directories were scanned. Running a policy assessment is also useful 
for performance tuning, allowing you to understand how changing worker loads 
affects the file scanning process so you can reduce latency or control CPU resource 
consumption.  
Note: Beginning with SyncIQ 3.0, this functionality is available only after you create a 
new policy and before you attempt a normal synchronization for the first time. 
What’s new in SyncIQ 3.0 
Significant new features and functionality have been added in SyncIQ 3.0 that 
dramatically improve most customer replication times, secure replicated data against 
accidental alteration, and improve source and target association persistence. 
Performance improvements 
Several changes in SyncIQ 3.0 will have significant, positive performance impacts for 
most customer workflows. The most significant changes are:  
 Treewalks have been removed from incremental synchronizations.  
 Rename operations are now treated as a move not a delete. 
Snapshot integration removes need for treewalks 
SyncIQ automatically takes a snapshot of the dataset on the source cluster before 
starting each SyncIQ data-synchronization or copy job; this source-cluster snapshot 
does not require a SnapshotIQ module license.  When a SyncIQ job starts, if the 
system detects a previous source-cluster snapshot, SyncIQ sends to the target only 
those files that are not present in the previous snapshot, as well as any files that

---

## synciq-best-practices::chunk_13

require a SnapshotIQ module license. When a SyncIQ job starts, if the system detects a previous source-cluster snapshot, SyncIQ sends to the target only those files that are not present in the previous snapshot, as well as any files that

15
Best Practices for Data Replication with EMC Isilon SyncIQ 
have changed since the last source-cluster snapshot was taken. Because comparing 
two snapshots is typically miniscule compared with walking the entire tree, the 
performance gain for incremental synchronizations can be significant. 
When a SyncIQ job starts, if the system does not find a previous source-cluster 
snapshot (for example, if a SyncIQ job is running for the first time), SyncIQ takes an 
initial full snapshot of the specified root path on the source cluster. When a SyncIQ 
job completes, the system deletes the previous source-cluster snapshot and retains 
the most recent snapshot. Source-cluster snapshots are named SIQ-<policy-id>-
[new,latest], where <policy-id> is the unique system-generated policy identifier. Each 
time a SyncIQ job finishes, SyncIQ replaces the latest existing snapshot with the most 
recent snapshot, which in turn becomes the latest snapshot. The new label is 
temporary and is used only while the job is running.  
During a SyncIQ job, SyncIQ identifies any changes on the source cluster and then 
replicates those changes to the target cluster. 
Copy-job changes 
 Prior to OneFS 6.5, copy jobs did not remove files from the target that were 
deleted on the source. Also, SyncIQ treated a renamed file operation as a delete 
and a re-create operation, so the target left a copy of the file at the old location. 
Since the release of OneFS 6.5, SyncIQ now keeps track of file moves and no 
longer leaves links to old file locations where the file simply moved within the 
synchronization job or where hard-linked files still contain at least one link in the 
replication set. Additionally, SyncIQ previously considered the deletion of a 
directory and its replacement by an identically named directory as a reuse of a 
directory. SyncIQ 3.0 recognizes the re-created directory as a "new" directory, 
causing the "old" directory to be removed (along with its contents).  
 
Example: 
If you delete “/ifs/old/dir” and all of its contents on the source with a copy policy, 
“/ifs/old/dir” still exists on the target. On the other hand, if you delete 
“/ifs/old/dir” and create a new directory named “/ifs/old/dir” in its place, the old 
“dir” and its contents on the target will be removed.  
 Starting with version 3.0, SyncIQ keeps track of file moves and maintains hard-
link relationships at the target level. Because of this change, the behavior of 
SyncIQ copy jobs is slightly different from that in earlier releases. In earlier 
releases, SyncIQ did not perform delete operations on the target unless it used 
the target path for another file. Starting with version 3.0, SyncIQ removes links 
during repeated replication operations if it points to the file or directory in the 
current replication pass.  
Example:  
If a single linked file is moved within the replication set, SyncIQ removes the old 
link and adds a new link. Assume the following: 
 The SyncIQ policy root directory is set to /ifs/data.

---

## synciq-best-practices::chunk_14

in the current replication pass. Example: If a single linked file is moved within the replication set, SyncIQ removes the old link and adds a new link. Assume the following:  The SyncIQ policy root directory is set to /ifs/data.

16
Best Practices for Data Replication with EMC Isilon SyncIQ 
 /ifs/data/user1/foo is hard-linked to /ifs/data/user2/bar. 
 /ifs/data/user2/bar is moved to /ifs/data/user3/bar.  
With copy replication, on the target cluster, /ifs/data/user1/foo will remain, and 
/ifs/data/user2/bar will be moved to /ifs/data/user3/bar. 
 If a single hard link to a multilinked file is removed, SyncIQ now removes the 
destination link. 
Example: 
Using the example above, if /ifs/data/user2/bar is deleted from the source, copy 
replication also removes /ifs/data/user2/bar from the target. 
 If the last remaining link to a file is removed on the source, SyncIQ no longer 
removes the file on the target unless another source file or directory with the same 
filename is created in the same directory (or unless a deleted ancestor is replaced 
with a conflicting file or directory name). 
Example: 
Continuing with the same example, assume that /ifs/data/user2/bar has been 
removed, which makes /ifs/data/user1/foo the last remaining link. If 
/ifs/data/user1/foo is deleted on the source cluster, with a copy replication, 
SyncIQ does not delete /ifs/data/user1/foo from the target cluster unless a new 
file or directory was created on the source cluster that was named 
/ifs/data/user1/foo. Once SyncIQ creates the new file or directory with this name, 
the old file on the target cluster is removed and re-created upon copy replication. 
 If a file or directory is renamed or moved on the source cluster and still falls within 
the SyncIQ policy1 root path, then when copied, SyncIQ will rename that file on the 
target; it does not delete and re-create the file. However, if the file is moved 
outside of the SyncIQ policy root path, then with copy replication, SyncIQ will 
leave that file on the target but will no longer associate it with the file on the 
source. If that file is moved back to the original source, or even to another 
directory within the SyncIQ policy root path, with copy replication, SyncIQ creates 
a new file on the target since it no longer associates it with the original target file. 
Example: 
If /ifs/data/user1/foo is moved to /ifs/data/user2/foo, with an incremental copy 
replication, SyncIQ simply renames the file on the target preventing deletion and 
re-creation as was the case in versions earlier than SyncIQ 3.0. However, if 
/ifs/data/user1/foo is moved to /ifs/home/foo, which is outside the SyncIQ 
policy root path, then with copy replication, SyncIQ does not delete 
/ifs/data/user1/foo on the target, but it does disassociate (or orphan) it from the 
source file that now resides at /ifs/home/foo. If, on the source cluster, the file is 
moved back to /ifs/data/user1/foo, an incremental copy copies that entire file to 
the target cluster because the association with the original file has been broken. 
                                                     
1 In the policy-configuration content, specifying file criteria in a SyncIQ policy will slow down a copy or synchronization job. 
Using includes or excludes for directory paths does not affect performance, but specifying file criteria does.

---

## synciq-best-practices::chunk_15

file has been broken. 1 In the policy-configuration content, specifying file criteria in a SyncIQ policy will slow down a copy or synchronization job. Using includes or excludes for directory paths does not affect performance, but specifying file criteria does.

17
Best Practices for Data Replication with EMC Isilon SyncIQ 
Source and target cluster association persistence 
Beginning with SyncIQ 3.0, OneFS associates a policy with its specified target 
directory by placing a cookie on the source cluster when the job runs for the first time. 
Even if you modify the name or IP address of the target cluster, the cookie causes the 
association to persist. If necessary, you can manually break a target association, for 
example, if an association is obsolete or was intended for temporary testing 
purposes. Breaking a target association causes the source to fully resynchronize the 
next time the job runs; during this full resynchronization, SyncIQ creates a new 
association between the source and its specified target. 
Target protection with restricted writes 
Earlier versions of SyncIQ highly recommended that you restrict write permissions on 
directories that are SyncIQ targets. This is now enforced in SyncIQ 3.0; that is, all 
writes outside of a SyncIQ process are disabled on any directory that is a target for a 
SyncIQ job. However, if you break the association between a target and a source, the 
target then returns to a writeable state. Resolving a broken association will force a full 
resynchronization to occur at the next job run. This feature is built on the target-side 
association and operation functionality that was introduced in OneFS 6.0. Starting in 
OneFS 6.0, every SyncIQ policy has a direct 1:1 association with its target directory, 
and all sub-directories. Restricted writes prevent modification, creation, deletion, or 
movement of any files within the target path of a SyncIQ job, and prevent movement 
or creation of hard links to any files into or out of the target path of a SyncIQ job. 
Assess SyncIQ changes 
SyncIQ can conduct a trial run of your policy without actually transferring file data 
between locations. Beginning with SyncIQ 3.0, this functionality is only available after 
you create a new policy and before you attempt a normal synchronization for the first 
time. 
Improved authentication integration 
Prior to OneFS 6.5 and SyncIQ 3.0, the UID/GID information was backed up and 
replicated to the target cluster. If you needed the target cluster to become the primary 
cluster, you had to restore the UID/GID information on the target cluster. OneFS 6.5 
and SyncIQ 3.0 no longer require this, since the UID/GID information has been 
replaced with SID numbers and is replicated with the metadata.  The result is much 
easier transition and management. 
Multiple jobs targeting a single directory tree no longer supported 
In versions of SyncIQ before 3.0, it was possible to create multiple jobs that pointed 
to the same target directory on the same target cluster.  
 
Example: 
In versions of SyncIQ before 3.0, if you wanted to replicate the source directory 
/ifs/data/users from the source cluster, except for one particularly large user folder

---

## synciq-best-practices::chunk_16

jobs that pointed to the same target directory on the same target cluster. Example: In versions of SyncIQ before 3.0, if you wanted to replicate the source directory /ifs/data/users from the source cluster, except for one particularly large user folder

18
Best Practices for Data Replication with EMC Isilon SyncIQ 
like /ifs/data/users/ceo, you could set up two SyncIQ policies that were essentially 
the same except the first job excluded the /ifs/data/users/ceo folder, and the second 
policy included only /ifs/data/users/ceo. This essentially split one policy into two 
separate policies, with the target at the same location. This is not possible in SyncIQ 
3.0 due to a change in how the policy associations work. A valid configuration 
requires changing the target location, but this can create complications if you need to 
do a restore or failover. 
Hard-link replication now supported 
SyncIQ now creates hard links at the source as hard links on the target, including 
recombining any files that were split during OneFS 6.0 (or earlier version) 
synchronizations.  
Report changes 
Reports are now customized based on the type of job that is run. Reports generated 
for incremental synchronization are different from these reports: 
 Initial synchronization 
 Jobs that occurred during a pre-OneFS 6.5 run 
 Jobs that occurred during the first run after a OneFS 6.5 upgrade  
SyncIQ best practices and tips 
In this section we present expert advice from our training team and gathered from 
customer use cases that can help you decide how to approach a particular 
configuration option or other product option choice in the way that best suits your 
environment. 
Avoiding full dataset replications 
Certain configuration changes will cause a replication job to run an initial full baseline 
replication as if it was running for the first time; that is, it will copy all data in the 
source path(s) whether or not the data has changed since the last run. Full baseline 
replication typically takes much longer than incremental synchronizations, so to 
optimize performance, avoid triggering full synchronizations when they are not 
necessary.  Changes to the following parameters will cause this behavior:  
 Source path(s): root path, include and exclude paths 
 Source file selection criteria: type, time, and regular expressions 
To prevent full dataset replications from occurring, avoid changing the file selection 
criteria on the source dataset.

---

## synciq-best-practices::chunk_17

will cause this behavior:  Source path(s): root path, include and exclude paths  Source file selection criteria: type, time, and regular expressions To prevent full dataset replications from occurring, avoid changing the file selection criteria on the source dataset.

19
Best Practices for Data Replication with EMC Isilon SyncIQ 
Selecting the right source replication dataset 
SyncIQ policies provide fine-grain control of the dataset you want to replicate, from 
determining what directories to include, or exclude, to creating file filtering regular 
expressions.  
Including or excluding source-cluster directories 
When you configure source-cluster settings in a SyncIQ policy, in addition to 
specifying a root directory on the source cluster, you can optionally include, or 
exclude, specific source-cluster directories.  
Note: Each time the policy runs, the system takes a snapshot of the specified root 
directory. This snapshot becomes the basis for the replication between the two 
specified clusters. 
By default, all files and folders under the specified root directory are synchronized to 
the target cluster. However, if you explicitly included any directories in the policy 
configuration, the system synchronizes only the files that are contained in that 
explicitly included directory to the target cluster. In addition, if you explicitly excluded 
any directories, those directories and any files contained in them, are not 
synchronized to the target cluster. 
Any directories that you explicitly include must be contained in, or under, the 
specified root directory.  Consider a policy in which the specified root directory is 
/ifs/data. In this example, you could explicitly include the /ifs/data/media directory 
because it is under /ifs/data. When the associated policy runs, only the contents of 
the /ifs/data/media directory would be synchronized to the target cluster. 
If you were to explicitly exclude a directory that is contained in the specified root 
directory, and you did not explicitly include any directories, only the contents of the 
excluded directory would not be synchronized to the target cluster.  
If you were to both explicitly include directories and exclude directories, every 
explicitly included directory will be replicated and every other file, or directory, under 
the exclude directory will be excluded from the replication dataset. 
For example, consider a policy in which the specified root directory is /ifs/data, and 
the following directories are explicitly included and excluded: 
Explicitly included directories: 
 /ifs/data/media/music  
 /ifs/data/media/movies  
Explicitly excluded directories: 
 /ifs/data/media/music/working  
 /ifs/data/media  
In this example, excluding /ifs/data/media would exclude all directories below 
/ifs/data/media except those specifically included.  Directories

---

## synciq-best-practices::chunk_18

/ifs/data, and the following directories are explicitly included and excluded: Explicitly included directories:  /ifs/data/media/music  /ifs/data/media/movies Explicitly excluded directories:  /ifs/data/media/music/working  /ifs/data/media In this example, excluding /ifs/data/media would exclude all directories below /ifs/data/media except those specifically included. Directories

20
Best Practices for Data Replication with EMC Isilon SyncIQ 
/ifs/data/media/music, /ifs/data/media/movies, /ifs/data/media/pictures, 
/ifs/data/media/books, /ifs/data/media/games would be excluded because the 
directory /ifs/data/media was explicitly excluded.  In other words, /ifs/data/media 
excludes all files under /ifs/data/media, except music and movies that are explicitly 
included.  
Note: If you exclude a directory that contains the specified root directory, the exclude 
directory setting has no effect.  For example, consider a policy in which the specified 
root directory is /ifs/data. Configuring a policy setting that excludes the /ifs directory 
would have no effect, and all contents of the specified root directory (in this example, 
/ifs/data) would be replicated to the target cluster. 
Configuring SyncIQ policy file selection criteria 
For each SyncIQ policy, you can define file-criteria statements that explicitly include 
or exclude files from the policy action. A file-criteria statement can include one or 
more elements and each file-criteria element contains a file attribute, a comparison 
operator, and a comparison value. To combine multiple criteria elements into a 
criteria statement, use the Boolean AND and OR operators. You can configure any 
number of AND and OR file-criteria definitions. 
You can include or exclude files based on the following predicates depending on 
whether the policy is defined as a Sync or Copy type.  
Sync policies are more restrictive in the file selection criteria and include the 
following: 
 You can use the wildcard characters *, ?, and [ ] or advanced POSIX regular 
expressions (regex). Regular expressions are sets of symbols and syntactic 
elements that match patterns of text. These expressions can be more powerful 
and flexible than simple wildcard characters. Isilon clusters support IEEE Std 
1003.2 (POSIX.2) regular expressions.  For more information about POSIX regular 
expressions, see the BSD man pages. For example: 
 To select all files ending in .jpg, you could type .*\.jpg$.  
 To select all files with either .jpg or .gif file extensions, you could type 
.*\.(jpg|gif)$.  
 You can also include or exclude files based on file size by specifying the file size 
in bytes, KB, MB, GB, TB, or PB. File sizes are represented in multiples of 1,024, 
not 1,000. 
 You can include or exclude files based on the following type options:  regular file, 
directory, or soft link. A soft link is a special type of POSIX file that contains a 
reference to another file or directory.

---

## synciq-best-practices::chunk_19

not 1,000.  You can include or exclude files based on the following type options: regular file, directory, or soft link. A soft link is a special type of POSIX file that contains a reference to another file or directory.

21
Best Practices for Data Replication with EMC Isilon SyncIQ 
 
Figure 5. Policy advanced file selection options 
Note: When managing a Sync type of policy, use care when modifying a file attributes 
comparison option and comparison values. With a Sync type of policy (not Copy type), 
modifying these settings will cause any nonmatching files to be deleted from the 
target the next time the job runs. 
Copy policies also allow you to select files based on file creation time, accessed time, 
and modification time. 
Note: In the policy-configuration content, specifying file criteria in a SyncIQ policy will 
slow down a copy or synchronize job. Using includes or excludes for directory paths 
does not affect performance, but specifying file criteria does. 
Disaster recovery from a target Isilon cluster 
As described above a common use for data replication using SyncIQ is for recovery 
from complete site disasters on a local site by either pointing applications and users 
to the target cluster or by re-creating the dataset on a local cluster with data 
replication from the target cluster. 
Note: Isilon recommends using target cluster snapshots for disaster recovery.  
You can meet specific RPO and reduce recovery time objectives (RTO) by setting the 
right policy schedule interval and using target cluster snapshots.  It is possible to 
accomplish RTO by either failing over to the target cluster, or replicating the necessary 
dataset from the remote cluster back to a local cluster.  
To recover from a disaster and fail over to the target cluster, simply copy the 
replicated dataset from any of the target cluster snapshots, or from the target cluster 
replication path (in cases where target snapshots are not enabled to a local directory 
that can be shared or exported to remote clients).

---

## synciq-best-practices::chunk_20

simply copy the replicated dataset from any of the target cluster snapshots, or from the target cluster replication path (in cases where target snapshots are not enabled to a local directory that can be shared or exported to remote clients).

22
Best Practices for Data Replication with EMC Isilon SyncIQ 
Note: Isilon recommends that you do not export the target replication path. This 
ensures that users cannot change the target dataset and that it is synchronized with 
the source dataset. 
To recover from a disaster by failing back to the original source cluster take the 
following steps: 
1. Disable the SyncIQ policy on the original source cluster. 
2. Create a new policy on the original target cluster where the replicated dataset 
resides. The replicated dataset is the target snapshot (if no changes have been 
made on the original target cluster) or it is a new share on the original target 
cluster with changed data (in the case of a failover scenario on the original target 
cluster). 
3. Start a manual initial synchronization from the original target cluster to the 
original source cluster. Now, the original target cluster is a source cluster and the 
original source cluster is the target cluster. This is a one-time manual 
synchronization to retrieve the replicated dataset back to the original cluster. 
If the original source cluster was brought online with some, or most, of the original 
data intact it may be beneficial to use a target aware initial synchronization to 
avoid replicating files that exist unchanged on both clusters. 
4. After the one-time replication job is complete, disable or delete the replication 
policy on the original target cluster and continue normal operations on the original 
source cluster. 
Note: SyncIQ does not replicate cluster configurations such as shares and exports, 
quotas, snapshots, and networking settings, from the source cluster. Isilon does copy 
over UID/GID ID mapping during replication.  In the case of failover to the remote 
cluster, the ID mapping file must be copied to the right location and other cluster 
settings must be configured manually.  Please consult Isilon Technical Support for 
more information. 
Performance tuning 
SyncIQ uses a multi-worker intelligent job execution engine to take advantage of 
aggregate CPU and networking resources to address the needs of most datasets. 
However, in certain cases you may want to do further tuning.  
Guidelines 
Although no overarching formula exists for making changes to specific performance 
settings, a good methodology for optimizing performance is to use the following 
guidelines: 
 Establish reference network performance by using common tools such as Secure 
Copy (scp) or NFS copy from cluster to cluster. This will provide a baseline for a 
single thread data transfer over the existing network.

---

## synciq-best-practices::chunk_21

use the following guidelines:  Establish reference network performance by using common tools such as Secure Copy (scp) or NFS copy from cluster to cluster. This will provide a baseline for a single thread data transfer over the existing network.

23
Best Practices for Data Replication with EMC Isilon SyncIQ 
 After creating a policy and before running the policy for the first time, use the 
policy assessment option to see how long it takes to scan the source cluster 
dataset with default settings.  
 Increase workers per node in cases where network utilization is low, for example 
over WAN. This can help overcome network latency by having more workers 
generate I/O on the wire. If adding more workers per node does not improve 
network utilization, avoid adding more workers because of diminishing returns 
and worker scheduling overhead. 
 Increase workers per node in datasets with many small files to process more files 
in parallel. Be aware that as more workers are employed, more CPU is consumed, 
due to other cluster operations. 
 Use file rate throttling to control how much CPU and disk I/O SyncIQ consumes 
while jobs are running through the day. 
 Remember that “target aware synchronizations” are much more CPU-intensive 
than regular baseline replication but they potentially yield much less network 
traffic if both source and cluster datasets are already seeded with similar data. 
 Use SmartConnect IP address pools to control which nodes participate in a 
replication job and to avoid contention with other workflows accessing the cluster 
through those nodes. 
 Use network throttling to control how much network bandwidth SyncIQ can 
consume through the day. 
Limitations and restrictions 
 SyncIQ can run up to five jobs at any given time. Additional jobs are queued until 
a new job execution slot is available.  
Note: SyncIQ can be used to cancel already queued jobs.  
 The maximum number of workers per node is eight and the default number of 
workers per node is three.  
 The number of workers per job is a product of the number of workers per node 
setting multiplied by the number of nodes participating in a job (which defaults to 
all nodes unless a SmartConnect IP address pool is used to restrict the number of 
participating nodes to a job). However, the maximum number of workers per job is 
40. At any given time, 200 workers could potentially be running on the cluster (5 
jobs with 40 workers each).  
 Never set file throttling to less than the number of workers per job. This ensures 
that workers are not idle waiting for files to process. Since the maximum number 
of workers per job is 40 it is good practice to set file throttling to 40 files/s (and 
above).  However, a 5-node cluster that is set with 3 workers per node (default) 
will have 15 workers per job. In this case you can set the file throttling to as low as 
15 files/s.

---

## synciq-best-practices::chunk_22

throttling to 40 files/s (and above). However, a 5-node cluster that is set with 3 workers per node (default) will have 15 workers per job. In this case you can set the file throttling to as low as 15 files/s.

24
Best Practices for Data Replication with EMC Isilon SyncIQ 
 Bandwidth restriction should never be below the number of nodes multiplied by 
1 Kb/s (#nodes x 1 Kb/s). So for a 20-node cluster, bandwidth should not be less 
than 20 Kb/s. 
 On the target cluster, there is a limit of configurable workers per node (sworkers) 
to avoid overwhelming the target cluster if multiple source clusters are replicating 
to the same target cluster. Contact Isilon Technical Support if load on the target 
cluster, generated by incoming SyncIQ jobs, needs to be adjusted. 
Using Isilon SnapshotIQ on the target 
By default, taking snapshots on the target cluster is not enabled. To enable 
snapshots on the target cluster, you must acquire a SnapshotIQ license and activate 
it on the target cluster.  
When SyncIQ policies are set with snapshots on the target cluster, SyncIQ will 
automatically take two snapshots during a job execution.  A first snapshot of the 
existing dataset on the target cluster is taken before replication begins; this provides 
a view of the dataset before any data transfers occur.  Then, a second snapshot is 
taken after the data transfer is completed to capture the view of the dataset upon 
replication completion.   
Note:  Prior to initiating a job, SyncIQ will first confirm SnapshotIQ is licensed on the 
target cluster.  If SnapshotIQ is not licensed on the target cluster, the job will proceed, 
but it will not generate a snapshot on the target cluster and SyncIQ will issue an alert 
to that effect. 
You can control how many snapshots of the target replication path are maintained 
over time by defining an expiration period on each of the target-cluster snapshot. For 
example, if you execute a replication job every day for a week (with target snapshots 
enabled), you will have seven snapshots of the dataset on the target cluster, 
representing seven versions of the dataset from which to choose.  
In this example, if you choose to make the target-cluster snapshot expire after seven 
days on a replication policy that is executed once per day, only seven snapshots will 
be available on the target cluster dataset.  
Using SmartConnect with SyncIQ 
In most cases, SyncIQ replication uses the full set of resources on the cluster (that is, 
all nodes in the cluster participate in the job). In cases where you want to limit (and 
control) which nodes in the cluster should participate in SyncIQ jobs, use 
SmartConnect to achieve this.  
Using SmartConnect on the source cluster 
On the source cluster, you can create a SmartConnect IP address pool and assign the 
IP address pool for the source cluster: 
1. Create or use an existing SmartConnect IP address pool in the desired subnet.

---

## synciq-best-practices::chunk_23

on the source cluster On the source cluster, you can create a SmartConnect IP address pool and assign the IP address pool for the source cluster: 1. Create or use an existing SmartConnect IP address pool in the desired subnet.

25
Best Practices for Data Replication with EMC Isilon SyncIQ 
2. If the SmartConnect IP address pool was created exclusively to integrate with 
SyncIQ, you do not need to allocate an IP range for this pool. Simply leave the IP 
range fields empty.  
3. After a node appears in the SmartConnect IP address pool, SyncIQ will use 
network interfaces based on the standard routing on that node to connect with the 
target cluster. 
Note: By default, SyncIQ uses all interfaces in the nodes that belong to the IP address 
pool disregarding any interface membership settings in the pool. If you want to 
restrict SyncIQ to use only the interfaces in the IP address pool, use the following 
command line interface commands to modify the SyncIQ policy: 
isi sync policy  modify --policy <my_policy> --force_interface=on 
 
Using SmartConnect zones on the target cluster 
When you set a policy target cluster name or address, you can use a SmartConnect 
DNS zone name instead of an IP address or a DNS name of a specific node. If you 
choose to restrict the connection to nodes in the SmartConnect zone, the replication 
job will only connect with the target cluster nodes assigned to that zone. During the 
initial part of a replication job, SyncIQ on the source cluster will establish an initial 
connection with the target cluster using SmartConnect. Once connection with the 
target cluster is established, the target cluster will reply with a set of target IP 
addresses assigned to nodes restricted to that SmartConnect zone. SyncIQ on the 
source cluster will use this list of target cluster IP addresses to connect local 
replication workers with remote workers on the target cluster. 
The basic steps are: 
1. On the target cluster, create a SmartConnect zone using the cluster networking UI. 
2. Add only those nodes that will be used for SyncIQ to the newly created zone. 
3. On the source cluster, SyncIQ replication jobs (or global settings) specify the 
SmartConnect zone name as the target server name. 
Note: SyncIQ does not support dynamic IPs in SmartConnect IP address pools. If 
dynamic IPs are specified, the replication job will fail with an error message in the log 
file and an alert. 
You can find more information on how to configure SmartConnect zones in the Isilon 
Administration web interface.

---

## synciq-best-practices::chunk_24

address pools. If dynamic IPs are specified, the replication job will fail with an error message in the log file and an alert. You can find more information on how to configure SmartConnect zones in the Isilon Administration web interface.

26
Best Practices for Data Replication with EMC Isilon SyncIQ 
 
Figure 6. SyncIQ policy-specific SmartConnect integration 
While you can set these settings per SyncIQ policy, often it is more useful to set them 
globally in the SyncIQ Settings page as shown below. Those settings will be applied 
by default to new policies unless you override them on a per-policy basis. However, 
changing these global settings will not affect existing policies. 
 
Figure 7. SyncIQ global settings for SmartConnect integration 
Monitoring SyncIQ 
In addition to including cluster-wide performance monitoring tools, such as the “isi 
statistics” command line interface or the new Isilon InsightIQ™ software module, 
SyncIQ includes module-specific performance monitoring tools. For information on 
“isi statistics” and InsightIQ, please refer to the product documentation and Isilon 
knowledge base.

---

## synciq-best-practices::chunk_25

monitoring tools, such as the “isi statistics” command line interface or the new Isilon InsightIQ™ software module, SyncIQ includes module-specific performance monitoring tools. For information on “isi statistics” and InsightIQ, please refer to the product documentation and Isilon knowledge base.

27
Best Practices for Data Replication with EMC Isilon SyncIQ 
Policy job monitoring 
For high-level job monitoring use the SyncIQ Summary page where job duration and 
total dataset statistics are available. The Summary page includes currently running 
jobs, as well as reports on completed jobs. For more details click the View Details link 
to review job-specific datasets and performance statistics. You can use the Reports 
page to select a specific policy that was run within a specific period and completed 
with a specific job status. 
 
Figure 8. SyncIQ policy job report 
In addition to the Summary and Reports pages, the Alerts page displays SyncIQ 
specific alerts extracted from the general-purpose cluster Alerts system. 
Performance monitoring 
For performance tuning purposes, use the SyncIQ Performance page.  On this page, 
you can review network utilization and files processing rate and you can control the 
network and CPU usage. When reviewing real-time or historical graphs you can control 
the starting time and time interval to provide the level of detail you need. The graphs 
display both cluster-wide performance and per-node performance. Based on this 
information you can set network and file processing threshold limits (to limit CPU 
usage). These limits are cluster-wide and are shared across jobs running 
simultaneously.

---

## synciq-best-practices::chunk_26

detail you need. The graphs display both cluster-wide performance and per-node performance. Based on this information you can set network and file processing threshold limits (to limit CPU usage). These limits are cluster-wide and are shared across jobs running simultaneously.

28
Best Practices for Data Replication with EMC Isilon SyncIQ 
 
Figure 9. Performance monitoring 
Troubleshooting with SyncIQ logs 
To get more detailed job information for troubleshooting purposes, review the SyncIQ 
log files. If necessary, you can log in to the appropriate node through the command 
line interface and view the node's /var/log/isi_migrate.log file.  The output depends 
on the logging level advanced policy setting: 
 Error: Logs only events related to specific types of failures. 
 Notice: Logs job-level and process-level activity, including job starts and stops, as 
well as worker coordination information. This is the default log level and is 
recommended for most SyncIQ deployments.  
 Network Activity: Logs expanded job-activity and work-item information, including 
specific paths and snapshot names. 
 File Activity: Logs a separate event for each action taken on a file. Do not enable 
this logging level without assistance from Isilon Technical Support. 
You can also choose to record log information on files deleted from the target cluster 
during synchronization jobs (these files are deleted from the target cluster when they 
are no longer present on the source cluster).

---

## synciq-best-practices::chunk_27

from Isilon Technical Support. You can also choose to record log information on files deleted from the target cluster during synchronization jobs (these files are deleted from the target cluster when they are no longer present on the source cluster).

29
Best Practices for Data Replication with EMC Isilon SyncIQ 
 
Figure 10. SyncIQ policy log level and synchronization log settings 
Target aware initial synchronization 
In situations where most of the dataset already resides on both clusters, target aware 
initial synchronizations are designed as a one-time manual replication job. Once run, 
you should disable the target aware initial synchronization so that normal replication 
can proceed.  If you do not disable it, incremental replications will continue with 
normal replication; however, if any changes occur to the policy definition (triggering a 
baseline replication), the system will use a target aware initial synchronization 
instead of a normal full baseline replication. 
 
Figure 11. Enabling target aware initial synchronization with the CLI 
Note: Target aware initial synchronization consumes CPU on both source and target 
clusters (comparing hashes of file blocks). It is an advanced feature only available 
through the command line and should be used only in specific cases as described in 
this paper. Please contact Isilon Technical Support for more information. 
Version compatibility 
The target cluster must be running the same or higher OneFS version as the source(s) 
so that it can accept replication from a source cluster with earlier OneFS versions. 
Note: Upgrade the target cluster before upgrading the source cluster to ensure no 
interruptions to replication jobs occur as part of the upgrade process.

---

## synciq-best-practices::chunk_28

the source(s) so that it can accept replication from a source cluster with earlier OneFS versions. Note: Upgrade the target cluster before upgrading the source cluster to ensure no interruptions to replication jobs occur as part of the upgrade process.

30
Best Practices for Data Replication with EMC Isilon SyncIQ 
Additional tips 
 Do not specify a target password unless you create the required password file on 
the target cluster. (This is not the same password as either cluster’s root 
password.) Setting a target cluster password is useful if you want to verify that the 
source cluster is replicating to the right target cluster.  
Note: There can be only one password per target cluster. All replication policies to the 
same target cluster must be set with the same target cluster password. 
 Do not use hyphens or other special characters in bandwidth or throttle rules. 
 When administering or executing SyncIQ jobs remotely over SSH, install SSH 
client certifications on the Isilon cluster to avoid having to enter the user 
password with every policy job activation. 
Conclusion  
With version 3, SyncIQ continues to define the asynchronous replication space for 
modern data architectures.  With snapshot integration in version 3, SyncIQ 
performance allows users to protect data faster and reduce their RPOs.  This 
performance enhancement—combined with SyncIQ’s integration with OneFS, native 
storage tiering, point-in-time snapshots, retention, and leading backup solutions— 
makes SyncIQ a powerful, flexible, and easy-to-manage solution for disaster recovery, 
business continuance, disk-to-disk backup, and remote disk archive.  
For more information on SyncIQ, see the SyncIQ Page on Isilon.com at 
http://www.isilon.com/synciq.  
For online product documentation go to the Isilon Customer Support Center at 
http://www.isilon.com/support/customer-support-center or contact your local Isilon 
sales representative or reseller or Isilon direct sales at the following:  
877-2-ISILON or 206-315-7602  |  Email: info@isilon.com