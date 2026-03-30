## onefs-913-release-notes::chunk_0

December 2025
PowerScale OneFS 9.13.0.0 Release Notes
These release notes contain descriptions of the new features, resolved issues, and known issues that are in this version of 
OneFS.
Current Release Version: 9.13.0.0
Release Type: Major (MA)
Topics:
•
Revision history
•
Product description
•
New features
•
Resolved issues
•
Known Issues
•
Where to get help
Revision history
This section provides a description of document changes.
Table 1. Revision history 
Document revision
Date
Description
1.0
December 16, 2025
Initial release version.
Product description
The scale-out NAS storage platform combines modular hardware with unified software to harness unstructured data. The 
OneFS operating system powers your clusters to deliver a scalable pool of storage with a global namespace.
For information about supported hardware and software, see the PowerScale OneFS Supportability and Compatibility Guide on 
the Dell Technologies Support site.
New features
This section summarizes the new features in OneFS 9.13.0.0.
Support for S3 
HTTPS port 443
The S3 HTTPS port must be 443 or in the range of 1024 to 65535.
TLS 1.3 Support 
Phase 2
Additional support for:
●
Apache data path: HTTP, RAN, HDFS access
●
S3 HTTP access
●
HDFS communication to KMS, NameNode, and Ambari
●
SmartSync
●
CloudPools: External connections and proxies
1

---

## onefs-913-release-notes::chunk_1

1024 to 65535. TLS 1.3 Support Phase 2 Additional support for: ● Apache data path: HTTP, RAN, HDFS access ● S3 HTTP access ● HDFS communication to KMS, NameNode, and Ambari ● SmartSync ● CloudPools: External connections and proxies 1

●
Customer to Dell connections: ESE, SRS/SCG, CloudIQ, isi_gather_info
Dynamic Licensing
Dynamic Licensing provides streamlined, cloud-based management of Dell product licenses. Dynamic 
Licensing is available for OneFS 9.13.0.0 and later.
Support for Multipart 
Upload (MPU)
MPU is a method that is used to upload large files to a PowerScale S3 bucket. You can now upload 
a single object in multiple parts independently and in any order. If a part fails to upload, it can be 
retransmitted without affecting the rest of the upload. Once all parts are uploaded, S3 assembles 
them to create the final object.
Support for user 
account lockout 
parameters
New parameters in the CLI and WebUI provide user account lockout support when failed logging 
attempts occur. Locking out a root account can render the system unmaintainable and could be 
exploited as a Denial of Service (DoS) vulnerability. To avoid this scenario, administrators can add an 
account to the isi_gconfig file exclusion list for system or nonsystem providers to disable user lockouts 
for specified users.
Support for AWS 
Intelligent Tiering
A new AWS_S3 storage class target available for the SmartSync File-to-Object Copy and File-to-
Object Backup to Cloud workflows named INTELLIGENT_TIERING is supported for AWS_S3 account 
types. Amazon S3 Intelligent-Tiering is a cloud storage class that automatically moves data between 
standard tiers and infrequently accessed tiers without performance impacts or additional overhead.
Support for cloud 
statistics
A new cloud statistics section is displayed in the output of the isi dm jobs view CLI for 
SmartSync cloud replication jobs.
CloudPools – Support 
for VPC Endpoint
CloudPools now supports AWS VPC Endpoints, enabling secure and private connectivity between your 
on-premises environment and AWS services without requiring an Internet gateway, NAT device, VPN 
connection, or AWS Direct Connect. This enhancement lays the foundation for GovCloud support in 
the future, ensuring compliance and improved security for sensitive workloads. By leveraging VPC 
Endpoints, data transfer occurs entirely within the AWS private network, reducing exposure to the 
public Internet and enhancing reliability. This solution offers several key benefits, including Private 
connectivity for CloudPools without Internet dependency, Simplified architecture, Future-ready for 
GovCloud compliance, and Improved security and performance.
Support for Back-
End NIC Upgrade/
Downgrade
Enables in-field backend NIC upgrades or swaps on PowerScale nodes (14G and 16G) to support 
evolving network needs while maintaining supported configurations.
Resolved issues
This section describes issues that are resolved in this release of PowerScale OneFS.
Data Mobility
PSCL03E-926
This fix resolves an issue where the coalescer_insert thread would get stuck while snap_create was in 
progress, which blocked all file system operations.
PSCL03E-744
The SmartSync isi_dm_d service may crash and create a core file during Cloud transfers of 
exceedingly large directories due to running out of memory when trying to complete too much of this 
work in parallel. A new SmartSync config value, max-sparks-cloud-acct, has been added to limit 
the maximum amount of simultaneous work done during Cloud transfers by default, reducing memory 
usage and preventing a crash. This can be overridden if necessary. See the PowerScale OneFS CLI 
Administration Guide for details.
PSCL03F-178
SmartSync extends Alternate Data Streams (ADS) support to symlinks and special file types (block, 
character, FIFO, and socket). In previous releases, if a job encountered ADS on file types other than 
files or directories, it would pause with an Invalid argument error. After upgrading to PowerScale 
OneFS 9.13.0.0, you can resume the job, and it will complete successfully without interruption.
2

---

## onefs-913-release-notes::chunk_2

if a job encountered ADS on file types other than files or directories, it would pause with an Invalid argument error. After upgrading to PowerScale OneFS 9.13.0.0, you can resume the job, and it will complete successfully without interruption. 2

File System
IME01A-508
This fixes an issue where ElasticSearch port numbers below 1024 were not configurable.
IME01A-276
This fix resolves an issue where event generation increased frequently and caused lock contention.
IME01A-178
This fix resolves an issue where specific object attributes could not sync from source to target cluster.
IME01C-292
This fix resolves an issue where a cluster group change was prevented from occurring leading to 
either node panic or client protocol interruption.
IME01C-279
This fix resolves an issue with a deadlock in coalescer.
PSCL05C-265
This fix resolves an issue where a race between vnode recycling and vnode allocation could have 
resulted in node panic on a system with many active files.
PSCL05H-314
This fixes an issue where a node in an SJM-enabled cluster could potentially panic shortly after 
rebooting due to any unrelated issue, if file system operations were run on the cluster immediately 
after the reboot.
PSCL05Q-392
This fix provides improved performance levels under client workloads which create a lot of vnodes by 
creating or accessing files.
PSCL09A-867
This fix allows the CELOG monitor component to use less expensive operations to determine leader 
eligibility.
Networking
IME01D-275
This fix resolves an issue where high isi_lbfo_d CPU usage during IB to ethernet migration could have 
caused data unavailability.
PSCL07H-633
This fix resolves a rare issue with dynamic IP address allocation when a node is split from the cluster. 
In previous versions, there was a chance that a node rejoining the cluster after quorum loss would 
incorrectly try to move all dynamic IP addresses to itself.
Performance
IME01A-412 
This fix resolves an issue with node panic during pcdata collection.
Platform
CPE05G-515
This fix addresses an issue where drive stall evaluation and recovery may exceed a client's protocol 
timeout, resulting in data unavailability or performance issues.
IME01B-305
This fix resolves an issue where isi_drive_d became unresponsive during a drive firmware update.
IME01B-312
This fix resolves an issue where a node could lose several disk mirrors due to 
agtiapi_CheckIOTimeout errors and/or node panics.
Protocols
IME01A-421
This fix adds a config parameter to disable unauthenticated access to an S3 bucket.
IME01A-348
This fix resolves an issue where HDFS could fail when handling a GETDELEGATIONTOKEN call to a 
target cluster with simple_only auth.
3

---

## onefs-913-release-notes::chunk_3

panics. Protocols IME01A-421 This fix adds a config parameter to disable unauthenticated access to an S3 bucket. IME01A-348 This fix resolves an issue where HDFS could fail when handling a GETDELEGATIONTOKEN call to a target cluster with simple_only auth. 3

IME01A-278
This fix resolves an issue where an empty/null LDAP bind resulted in storing "DEPRECATED..." 
message to keystore on upgrade-commit.
IME01A-249
This fix resolves an issue where NfsExportOptionsGetSecurityContextWithCache resulted in incorrect 
maproot access rights when accessing two or more exports.
IME01A-139
This fix resolves an issue where the delete request resulted in the error 
"STATUS_NOT_A_DIRECTORY."
IME01A-46
This fix provides the Key Management System (KMS) with High Availability (HA) support in OneFS so 
that PowerScale can support multiple KMS instances in the Cloudera.
IME01B-244
Resolved an issue where Kerberos was not advertised in the SPNEGO mechtlist due to missing 
acceptor keytab initialization, preventing clients relying on mechlist like macOS, especially in FIPS 
mode, from using Kerberos for SMB authentication.
IME01B-205
The fix resolves issues in the latest krb5 release which prevented the witness protocol from working 
correctly.
IME01C-486
This fix resolves an issue where I/O blockslots were leaked, causing data unavailability for NFS clients.
IME01C-320
This fix resolves an issue where the notification of completion status was not returned correctly.
IME01C-238
This fix resolves an issue where an HDFS proxy user in the format primary/hostname@realm could not 
be found by the authentication service. A gconfig configuration, HdfsAllowedSpnSimplifiers, has been 
added to allow a value such as "primary" to be looked up.
IME01C-232
This fix resolves an issue where a local user was marked as inactive when there were S3 workloads.
IME01D-248
This fix prevents internal S3 operations from being audited, ensuring the correct client IP appears in 
audit logs.
PSCL07D-515
This fix improves local user database lock contention.
PSCL07D-498
Fixes a problem in which upgrading across the 9.10 boundary (especially from 9.4) could potentially 
cause local users to lose their passwords, requiring an administrator to reset them.
PSCL07D-492
Certain upgrade failures caused some local users to be marked as Expired. This fix attempts to 
automatically remedy the situation so as not to mark the user as expired, creating a smoother upgrade 
experience.
PSCL07D-486
Fixes an issue in which if Active Directory is configured to use RFC2307 and a user is incorrectly 
configured in Active Directory, that user could end up with group 0 (wheel).
PSCL07F-444
This fix resolves an issue where an I/O limited operation could consume FHA slots, which could block 
I/O from all users.
PSCL07F-426
This fix resolves an issue where heavy concurrency to a single file could have caused excessive 
latency.
PSCL07F-364
This fix resolves an issue where NFS zone synchronization was blocked due to a suspended 
NfsZoneRefreshInternal thread during startup.
PSCL07G-303
This fix resolves an issue where the last part of a recovered file did not append correctly to the final 
file.
Security
IME01C-301
A fix has been implemented to minimize exclusive locking, and to retry rollback up to 10 times on 
specific transient error codes. If rollback cannot succeed after these retries, the process will core to 
avoid leaving the database locked indefinitely.
4

---

## onefs-913-release-notes::chunk_4

fix has been implemented to minimize exclusive locking, and to retry rollback up to 10 times on specific transient error codes. If rollback cannot succeed after these retries, the process will core to avoid leaving the database locked indefinitely. 4

IME01D-215
This fix moved the bash and zsh shell configuration files to the appropriate directory. This change 
allows the STIG Hardening profile to be applied correctly, and allows a timeout for idle CLI sessions to 
be configured.
UDSS01C-850
This fix resolves an issue where changing security settings unrelated to FIPS mode would cause the 
SSH configuration to reset.
SmartPools
IME01D-102
This fix resolves an issue where the data protection level was set incorrectly during a node addition 
that triggered a disk pool split.
Snapshots
PSCL05G-447
This fix resolves an issue where SnapshotDelete opened STFs in read/write mode.
Supportability
IME01C-272
This fix resolves an issue where a node could panic when decreasing the max client through sysctl 
isi.stats.client.nfs.max_clients.
IME01C-244
This fix resolves an issue where a critical alert regarding SupportAssist failure generated without 
cause.
SyncIQ
IME01A-378
This fix resolves an issue where a sync job would fail to get a pdm domain membership for a file if the 
domain number exceeded the maximum, resulting in an EOVERFLOW error.
IME01A-292
This fix resolves an issue where failure to locate a file or directory caused SyncIQ jobs to fail.
Upgrades
IME018-138
The fix resolves an issue where an upgrade fails due to non-UTF8 files under the /etc/local directory.
IME018-104
The fix resolves an issue where a vulnerability for an Apache icons directory capable of being listed is 
not preserved after a PowerScale OneFS upgrade.
Known Issues
This section describes issues that are known to affect this release of OneFS.
For information about issues that are known to affect other OneFS releases, log in to the PowerScale OneFS Product Page and 
view the available OneFS Release Notes.
File System
PSCL05A-605
When Multi-Party Authorization (MPA) is enabled, users should use the command-line interface (CLI) 
to modify snapshots or snapshot schedules. Using the web administration interface (WebUI) may 
generate unnecessary MPA requests or error messages. In the CLI, list only the fields that are 
5

---

## onefs-913-release-notes::chunk_5

(MPA) is enabled, users should use the command-line interface (CLI) to modify snapshots or snapshot schedules. Using the web administration interface (WebUI) may generate unnecessary MPA requests or error messages. In the CLI, list only the fields that are 5

intended to be modified, listing extraneous fields when using the CLI may generate unnecessary MPA 
requests.
Workaround: Use the command-line interface (CLI) to make modifications to a Snapshot or Snapshot 
schedule when Multi-Party Authorization (MPA) is enabled and only list the fields intended to be 
modified.
PSCL05N-308
Invalidate threads on sparse files could restart infinitely due to EOPRESTART errors from LIN lock 
contention. This caused delayed shutdowns and blocked upgrades in certain scenarios.
Protocol
PSCL07F-608
A problem has been seen in NFS with file handle misuse during NFS shutdown, where a file handle is 
closed twice, potentially causing an error in some other (unrelated) code path if that same file handle 
had been reused in that path. Since this problem occurs only during shutdown, it has minimal impact 
on NFS operation, but could result in an NFS core.
Remote Connectivity
IME01B-156
The isi connectivity reset and isi connectivity restore commands have been 
introduced in OneFS 9.12.0.0, enabling controlled SupportAssist reset functionality on compliance-
mode clusters, however their use is not recommended due to a potential issue with file permissions. 
The commands may set incorrect file permissions, preventing the ESE service from starting. Users 
are advised to continue using the existing isi_supportassist_debug command until the issue is 
resolved. If you run these commands unintentionally, contact Support Services.
Supportability
PSCL09A-805
When a customer runs an individual health-check or a checklist (a group of health checks), there are 
instances where the result file may not be generated within the expected time. This may happen due 
to system slowness, reboot, so forth As a result, the health-check evaluation may fail with a "Missing 
result" error. However, during the next scheduled run or if the health-check or checklist is executed 
manually in the meantime, it typically proceeds as expected and displays the correct result.
Where to get help
The Dell Technologies Support site contains important information about products and services including drivers, installation 
packages, product documentation, knowledge base articles, and advisories.
A valid support contract and account might be required to access all the available information about a specific Dell Technologies 
product or service.
Additional options for getting help
This section contains resources for getting answers to questions about PowerScale products.
Dell Technologies Support
●
Contact Technical Support 
Telephone support
●
United States: 1-800-SVC-4EMC (1-800-782-4362)
●
Canada: 1-800-543-4782
●
Worldwide: 1-312-725-5401
●
Local phone numbers for a specific country or region are available at Contact 
Technical Support.
6

---

## onefs-913-release-notes::chunk_6

about PowerScale products. Dell Technologies Support ● Contact Technical Support Telephone support ● United States: 1-800-SVC-4EMC (1-800-782-4362) ● Canada: 1-800-543-4782 ● Worldwide: 1-312-725-5401 ● Local phone numbers for a specific country or region are available at Contact Technical Support. 6

PowerScale OneFS Documentation 
Info Hubs
●
PowerScale OneFS Info Hubs
Dell Knowledge Base (KB) articles
KB articles are available on the Dell Technologies support site.
Installation and upgrade considerations
This section includes resources to consider when installing and upgrading OneFS.
OneFS information and documentation
You can access technical information about Dell Technologies PowerScale products, OneFS product documentation, and other 
resources through the following channels.
Table 2. More PowerScale resources 
Channel
Description
PowerScale Info Hubs
PowerScale info hubs organize PowerScale documentation into topic areas, making it 
simple to find content.
PowerScale OneFS Product Page
The Dell Technologies PowerScale OneFS product page provides access to PowerScale 
product documentation and current software releases. Access to this page requires that 
you log in to the Dell Technologies Online Support site.
PowerScale OneFS Patches
For the most up-to-date list of patches that are available for the version of OneFS 
running on your cluster, see the Current Patches article on the Dell Technologies Online 
Support site.
Dell Advisories (DSA, DTA)
A Dell Technologies security advisory (DSA) is published when a Dell Technologies 
product is impacted by a security vulnerability. A DSA provides a fix that customers must 
apply.
A Dell Technologies technical advisory (DTA) is published when Dell Technologies 
identifies an issue that may cause serious negative impact to a production environment.
For the most up-to-date list of PowerScale Advisories, see Dell Advisories for PowerScale 
OneFS. You can also subscribe to receive advisories automatically. See article 000018135 
for steps to subscribe.
Healthcheck Info Hub
The isi healthcheck command enables you to evaluate the status of specific 
software and hardware components of the cluster and the cluster environment. See the 
Dell Technologies PowerScale Healthcheck Info Hub for details.
Online Help
Select Online Help from the Help menu in the OneFS web administration interface.
7

---

## onefs-913-release-notes::chunk_7

status of specific software and hardware components of the cluster and the cluster environment. See the Dell Technologies PowerScale Healthcheck Info Hub for details. Online Help Select Online Help from the Help menu in the OneFS web administration interface. 7

Notes, cautions, and warnings
NOTE: A NOTE indicates important information that helps you make better use of your product.
CAUTION: A CAUTION indicates either potential damage to hardware or loss of data and tells you how to avoid the 
problem.
WARNING: A WARNING indicates a potential for property damage, personal injury, or death.
Copyright © 2016 - 2025 Dell Inc. All Rights Reserved. Dell Technologies, Dell, and other trademarks are trademarks of Dell Inc. or its 
subsidiaries. Other trademarks may be trademarks of their respective owners.