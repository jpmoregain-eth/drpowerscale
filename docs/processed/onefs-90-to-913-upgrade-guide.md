## onefs-90-to-913-upgrade-guide::chunk_0

PowerScale OneFS 
Upgrade Planning and Process Guide
9.0.0.0 - 9.13.0.0
December 2025

Notes, cautions, and warnings
NOTE: A NOTE indicates important information that helps you make better use of your product.
CAUTION: A CAUTION indicates either potential damage to hardware or loss of data and tells you how to avoid 
the problem.
WARNING: A WARNING indicates a potential for property damage, personal injury, or death.
© 2013 - 2025 Dell Inc. or its subsidiaries. All rights reserved. Dell Technologies, Dell, and other trademarks are trademarks of Dell Inc. or its 
subsidiaries. Other trademarks may be trademarks of their respective owners.

---

## onefs-90-to-913-upgrade-guide::chunk_1

damage, personal injury, or death. © 2013 - 2025 Dell Inc. or its subsidiaries. All rights reserved. Dell Technologies, Dell, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

Chapter 1: Introduction to this guide.............................................................................................6
About this guide...................................................................................................................................................................6
Where to get help................................................................................................................................................................6
Additional options for getting help............................................................................................................................ 6
Chapter 2: Planning an upgrade.....................................................................................................7
Upgrade planning overview ..............................................................................................................................................7
Planning an upgrade - summary.................................................................................................................................7
Prerequisites for completing an upgrade.......................................................................................................................7
Review required documentation...................................................................................................................................... 8
Types of OneFS upgrades.................................................................................................................................................8
Parallel upgrades............................................................................................................................................................8
Simultaneous upgrades................................................................................................................................................ 9
Verify the upgrade path.....................................................................................................................................................9
Upgrade Paths for supported versions of OneFS................................................................................................10
Check supportability and compatibility requirements............................................................................................... 10
Assess upgrade impact.....................................................................................................................................................10
Consider upgrade limitations......................................................................................................................................11
Upgrading a previously hardened cluster to OneFS 9.5.0.0 or later................................................................11
Review feature changes and known issues............................................................................................................11
Plan an upgrade schedule.................................................................................................................................................11
Chapter 3: Completing pre-upgrade tasks....................................................................................13
Pre-upgrade process - Overview...................................................................................................................................13
Pre-upgrade - Summary............................................................................................................................................. 13
Collect cluster information...............................................................................................................................................14
Review and save information about cluster status .............................................................................................14
Gathering cluster logs................................................................................................................................................. 14
Check cluster readiness....................................................................................................................................................14
Check hardware health - web administration interface..................................................................................... 15
Check hardware health - CLI.................................................................................................................................... 15
Check the available free space.................................................................................................................................15
Resolve outstanding events and errors.................................................................................................................. 17
Verify configurations and settings................................................................................................................................. 17
Upgrading in a Cloudpools environment................................................................................................................. 17
Upgrading in a FIPS or STIG environment............................................................................................................. 17
Preserve the Kerberos keytab file............................................................................................................................17
Install a supported version of DataIQ or InsightIQ............................................................................................... 18
Upgrade compatibility check...........................................................................................................................................18
Run the pre-upgrade compatibility check utility using the CLI.........................................................................18
Run the pre-upgrade compatibility check using the web interface.................................................................18
Pre-upgrade compatibility check..............................................................................................................................19
Reconfigure unsupported SMB settings................................................................................................................20
Reduce disruption to SMB connections during upgrades................................................................................. 20
Contents
Contents
3

---

## onefs-90-to-913-upgrade-guide::chunk_2

18 Upgrade compatibility check...........................................................................................................................................18 Run the pre-upgrade compatibility check utility using the CLI.........................................................................18 Run the pre-upgrade compatibility check using the web interface.................................................................18 Pre-upgrade compatibility check..............................................................................................................................19 Reconfigure unsupported SMB settings................................................................................................................20 Reduce disruption to SMB connections during upgrades................................................................................. 20 Contents Contents 3

Maintenance Mode........................................................................................................................................................... 20
On-Cluster Analysis tool...................................................................................................................................................21
HealthCheck tool................................................................................................................................................................21
Backup data.........................................................................................................................................................................21
SyncIQ backup.............................................................................................................................................................. 21
NDMP backup............................................................................................................................................................... 21
Back up custom settings........................................................................................................................................... 22
Complete or stop jobs in progress................................................................................................................................ 23
Complete system jobs................................................................................................................................................ 23
Update Node Firmware Package...................................................................................................................................23
Update Drive Support Package..................................................................................................................................... 23
Configure IPMI ports........................................................................................................................................................ 23
Enable Dell Technologies connectivity services ....................................................................................................... 23
Enabling Dell Technologies connectivity services - connect directly to Dell support.................................24
Configure the cluster for upgrade notifications........................................................................................................ 24
Configure OneFS automatic upgrade notifications.............................................................................................24
Download the OneFS installation bundle file.............................................................................................................. 25
Chapter 4: Performing the OneFS upgrade..................................................................................26
Upgrade process overview............................................................................................................................................. 26
Upgrade - Summary....................................................................................................................................................26
Completing a parallel upgrade of OneFS..................................................................................................................... 26
Performing a parallel upgrade using the web administration interface.......................................................... 27
Performing a parallel upgrade using the CLI.........................................................................................................27
Client connections during parallel upgrades......................................................................................................... 28
Completing a simultaneous upgrade of OneFS..........................................................................................................29
Perform a simultaneous upgrade using the web administration interface.................................................... 29
Perform a simultaneous upgrade using the CLI................................................................................................... 29
Adding a node to the cluster while an upgrade is in progress................................................................................30
Committing an upgrade of OneFS................................................................................................................................ 30
Commit an upgrade using the web interface....................................................................................................... 30
Commit an upgrade using the CLI...........................................................................................................................30
Rolling back an upgrade of OneFS.................................................................................................................................31
Roll back an upgrade using the web interface...................................................................................................... 31
Roll back an upgrade using the CLI..........................................................................................................................31
Verify the OneFS installation using the CLI.................................................................................................................31
Chapter 5: Completing post-upgrade tasks................................................................................. 32
Post-upgrade process - Overview................................................................................................................................32
Post-upgrade - Summary.......................................................................................................................................... 32
Allow the Upgrade job to run..........................................................................................................................................32
Verify operational status using the CLI........................................................................................................................33
Re-establish user privileges............................................................................................................................................ 34
Check client connections, and test the workflow.....................................................................................................34
Verify Kerberos migration............................................................................................................................................... 35
Verify Kerberos migration using the web administration interface.................................................................35
Verify Kerberos migration using the CLI................................................................................................................35
Reapply custom settings................................................................................................................................................. 35
Test custom scripts..........................................................................................................................................................35
4
Contents

---

## onefs-90-to-913-upgrade-guide::chunk_3

the CLI........................................................................................................................33 Re-establish user privileges............................................................................................................................................ 34 Check client connections, and test the workflow.....................................................................................................34 Verify Kerberos migration............................................................................................................................................... 35 Verify Kerberos migration using the web administration interface.................................................................35 Verify Kerberos migration using the CLI................................................................................................................35 Reapply custom settings................................................................................................................................................. 35 Test custom scripts..........................................................................................................................................................35 4 Contents

Install the latest roll-up patch........................................................................................................................................ 35
Verify Maintenance Mode...............................................................................................................................................36
Verify Dell Technologies connectivity services..........................................................................................................36
Chapter 6: Troubleshooting your upgrade....................................................................................37
Troubleshooting an upgrade........................................................................................................................................... 37
Contents
5

---

## onefs-90-to-913-upgrade-guide::chunk_4

Verify Kerberos migration using the CLI................................................................................................................35 Reapply custom settings................................................................................................................................................. 35 Test custom scripts..........................................................................................................................................................35 4 Contents Install the latest roll-up patch........................................................................................................................................ 35 Verify Maintenance Mode...............................................................................................................................................36 Verify Dell Technologies connectivity services..........................................................................................................36 Chapter 6: Troubleshooting your upgrade....................................................................................37 Troubleshooting an upgrade........................................................................................................................................... 37 Contents 5

Introduction to this guide
Topics:
•
About this guide
•
Where to get help
About this guide
This guide provides important information and steps that you must review and follow when upgrading your OneFS 9.0.x or later 
versions.
NOTE: For upgrades from OneFS 9.0.0.0 and earlier, contact Dell Technologies technical support.
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
PowerScale OneFS Documentation 
Info Hubs
●
PowerScale OneFS Info Hubs
Dell Knowledge Base (KB) articles
KB articles are available on the Dell Technologies support site.
1
6
Introduction to this guide

---

## onefs-90-to-913-upgrade-guide::chunk_5

country or region are available at Contact Technical Support. PowerScale OneFS Documentation Info Hubs ● PowerScale OneFS Info Hubs Dell Knowledge Base (KB) articles KB articles are available on the Dell Technologies support site. 1 6 Introduction to this guide

Planning an upgrade
Topics:
•
Upgrade planning overview 
•
Prerequisites for completing an upgrade
•
Review required documentation
•
Types of OneFS upgrades
•
Verify the upgrade path
•
Check supportability and compatibility requirements
•
Assess upgrade impact
•
Plan an upgrade schedule
Upgrade planning overview
This chapter provides information to help you create an upgrade plan. Your upgrade plan helps you estimate the time that it 
takes to complete tasks and determine who must complete them.
Create an upgrade plan by evaluating how the upgrade affects users and workflow, assessing the impact of the new version of 
OneFS on your cluster, and analyzing upgrade risks.
NOTE: To provide you with the best user experience, Dell Technologies recommends using Dell Remote Proactive Services 
for upgrade assistance. The support services team is available to perform OneFS pre-upgrade health checks and can 
complete the OneFS upgrade remotely for most customers.
Planning an upgrade - summary
The following is a summary of steps to perform during the upgrade planning phase:
1.
Review required documentation.
2. Determine the type of upgrade.
3. Verify the upgrade path.
4. Check supportability and compatibility.
5. Assess upgrade impact.
6. (Optional) Upgrade a test cluster.
Prerequisites for completing an upgrade
Permissions and interfaces
To complete the tasks described in this guide, you must be able to log in to the cluster as the root user through the following 
interfaces:
●
OneFS command-line interface
●
OneFS web administration interface
2
Planning an upgrade
7

---

## onefs-90-to-913-upgrade-guide::chunk_6

To complete the tasks described in this guide, you must be able to log in to the cluster as the root user through the following interfaces: ● OneFS command-line interface ● OneFS web administration interface 2 Planning an upgrade 7

Review required documentation
Reviewing the documentation in this list helps you to understand the upgrade process and the impact the upgrade could have on 
your workflow. Some links require a support login.
Required documentation
See the PowerScale OneFS InfoHub for the version of OneFS that corresponds with your deployment.
●
PowerScale OneFS Supportability and Compatibility Guide
Confirm that your PowerScale software and PowerScale hardware is compatible with the version of OneFS to which you are 
upgrading. Check on releases, release dates, and version status.
●
PowerScale OneFS Release Notes
Read the OneFS release notes for each version between your current version and your target version for information about 
new features, changes, resolved issues, and known issues.
●
PowerScale OneFS Current Patches
Review patches that have been released for the version of OneFS to which you are upgrading. 
Other documentation
●
OneFS Technical and Security Advisories
Determine whether any PowerScale Technical Advisories or Security Advisories have been issued for the version of OneFS 
to which you are upgrading. 
●
For more information about tips and tricks from the services team, see KB article 200890
Types of OneFS upgrades
Depending on the version of OneFS installed on your cluster, there are two types of upgrades available: parallel upgrades or 
simultaneous upgrades.
NOTE: In PowerScale OneFS 9.11.0.0 and later versions, Dell Technologies recommends the parallel upgrade option. Rolling 
upgrades are deprecated in PowerScale OneFS 9.11.0.0 and later. If you need to perform a rolling upgrade, refer to KB 
000273297.
CAUTION: The rolling upgrade option should be used only in exceptional circumstances, as it may have 
unintended consequences.
NOTE: See the Verify the upgrade path topic in this guide for information about which types of upgrades are supported 
between OneFS versions.
Parallel upgrades
Dell Technologies recommends using the parallel upgrade option when upgrading any size cluster running OneFS 8.2.2 and 
later. Parallel upgrades require a smaller maintenance window and do not require the interruption of service like simultaneous 
upgrades.
A parallel upgrade installs the new operating system on a subset of nodes and restarts that subset of nodes simultaneously. 
Each subset of nodes attempts to make a reservation for their turn to upgrade until all nodes are upgraded. Node subsets and 
reservations are based on diskpool and node availability.
In OneFS 9.11 and later, parallel upgrades are enhanced to incorporate network pool availability into the reservation logic to 
ensure that network pools do not go offline during an upgrade.
During a parallel upgrade, node subsets that are not being upgraded remain online and can continue serving clients. However, 
clients that are connected to a restarting node are disconnected and reconnected. How the client connection behaves when 
8
Planning an upgrade

---

## onefs-90-to-913-upgrade-guide::chunk_7

a parallel upgrade, node subsets that are not being upgraded remain online and can continue serving clients. However, clients that are connected to a restarting node are disconnected and reconnected. How the client connection behaves when 8 Planning an upgrade

a node is restarted depends on several factors including client type, client configuration (mount type, timeout settings), IP 
allocation method, and how the client connected to the cluster. In OneFS 9.2.0.0 and later, client connection behavior is 
managed by the disruption manager settings.
Simultaneous upgrades
A simultaneous upgrade installs the new operating system and restarts all nodes in the OneFS cluster at the same time. 
Simultaneous upgrades require a temporary interruption of service during the upgrade process. All client connections to the 
cluster must be terminated before completing the upgrade and data is inaccessible until the installation of the new OneFS 
operating system is complete and the cluster is back online.
Verify the upgrade path
Verify that the current version of OneFS on your cluster can be upgraded to the target version.
All upgrades follow one of these scenarios:
●
Upgrade to the patched target OneFS version
●
Upgrade to the target OneFS version, and then add patches
●
Upgrade to an intermediate OneFS version, upgrade to the target OneFS version, and then add patches
To view which version of OneFS is running on all nodes in your cluster, run the following command:
isi_for_array uname -r
Find your version of OneFS in the supported OneFS Upgrade Paths matrix and confirm which versions of OneFS are supported 
upgrade paths.
Planning an upgrade
9

---

## onefs-90-to-913-upgrade-guide::chunk_8

running on all nodes in your cluster, run the following command: isi_for_array uname -r Find your version of OneFS in the supported OneFS Upgrade Paths matrix and confirm which versions of OneFS are supported upgrade paths. Planning an upgrade 9

Upgrade Paths for supported versions of OneFS
The following table can be used to determine the supported upgrade path from the current version of OneFS on your cluster to 
a target version of OneFS. The upgrade paths table displays the supported upgrade paths from major OneFS version to major 
OneFS version, but does not include patch information.
Key:
●
"O" : Rolling and Simultaneous upgrades available
●
"=" : Parallel, Rolling, and Simultaneous upgrades available
●
"x" : Unsupported upgrade path
●
"–": For upgrades from OneFS 9.0.0 and earlier, contact Dell Technologies technical support.
NOTE: These supported upgrade paths do not guarantee issue fixes and feature parity. For more information about using 
patches to achieve issue fixes and feature parity, contact Dell Technologies technical support. If you are upgrading from an 
earlier version of OneFS than is listed in the following upgrade matrix, contact contact Dell Technologies technical support 
for assistance.
Table 1. OneFS Upgrade Paths 
Upgrade 
from 
current 
version
Upgrade to target version
End of 
Standard 
Support 
(EOSS)
9.5.0
9.6.0
9.7.0
9.8.0
9.9.0
9.10.0
9.11.0
9.12.0
9.13.0
9.5.0
2026/05/31
x
=
=
=
=
=
=
=
9.6.0*
=
=
=
=
=
=
=
9.7.0
2026/12/31
=
=
=
=
=
=
9.8.0
2027/04/30
=
=
=
=
=
9.9.0
=
=
=
=
9.10.0
=
=
=
9.11.0
=
=
9.12.0
=
9.13.0
NOTE: *Dell PowerScale for AWS and Dell PowerScale for Azure 9.6.x releases do not support an upgrade to 9.9.x. If you 
are on OneFS 9.6.x, you must upgrade to 9.7.0.1 or 9.8.x before the upgrade to 9.9.x and later versions.
NOTE: For OneFS versions 9.4 through 9.7, the datasets that SmartSync generates are not eligible for the backup format 
in the file-to-object workflow in 9.11. For OneFS versions 9.8 and later, the datasets that SmartSync generates cannot be 
replicated to the target OneFS version from 9.4 to 9.7 in the file-to-file workflow.
Check supportability and compatibility requirements
Review the PowerScale Supportability and Compatibility Guide on the Dell Support site to confirm that your current 
hardware components, software components, and protocol versions are compatible with the version of OneFS to which you are 
upgrading.
For information about OneFS compatibility with Hadoop, see the Hadoop - Info Hub page.
Assess upgrade impact
Consider all the areas of your environment that might be affected by upgrading to a new version and plan a strategy for 
performing the tasks that must be completed and addressing issues that might occur. Assessing the impact of the upgrade on 
your environment, clients, and performance helps ensure that the upgrade does not disrupt your cluster, workflow, or users.
10
Planning an upgrade

---

## onefs-90-to-913-upgrade-guide::chunk_9

tasks that must be completed and addressing issues that might occur. Assessing the impact of the upgrade on your environment, clients, and performance helps ensure that the upgrade does not disrupt your cluster, workflow, or users. 10 Planning an upgrade

NOTE: If you have a performance-sensitive workload, PowerScale recommends that you consult your Sales Engineer for 
assistance during the pre-upgrade planning process. 
Consider upgrade limitations
If the upgrade cannot be completed for any reason—for example, if there is insufficient space on the cluster or if the upgrade 
process detects a stalled drive—the system will revert to the current version and the upgrade will be cancelled. Preparing your 
cluster as recommended in this guide will help you to avoid situations that might result in a cancelled upgrade.
NOTE: In OneFS 8.2.0 and newer, you have the ability to pause and resume the upgrade process in order to resolve 
blocking issues.
Upgrading a previously hardened cluster to OneFS 9.5.0.0 or later
The Hardening Module in releases before OneFS 9.5.0.0 is not compatible with the Hardening Module in OneFS 9.5.0.0 and 
later. For this reason, hardening must be turned off on the cluster before upgrading to OneFS 9.5.0.0 or later.
The upgrade workflow for previously hardened clusters is:
1.
Before upgrading, use the appropriate hardening command to revert hardening on the cluster.
2. Perform all upgrade activities.
3. Reapply the STIG hardening profile on the cluster using the isi hardening apply command.
When upgrading from OneFS 9.5.0.0 and later, the hardening engine reapplies any previously applied profiles, thus resetting any 
manually applied settings that are set by the hardening profile. This ensures that the cluster remains in a hardened state after 
new configurations are applied, and ensures any updates to the hardening configuration are also applied.
Review feature changes and known issues
Familiarize yourself with new, modified, and deprecated features as well as known issues in the target version of OneFS to 
which you are upgrading.
Functionality changes and new features in the target version might impact the performance, configuration, or functionality of 
your cluster after upgrading. If the target version contains an issue that affects your environment, you should consider waiting 
to upgrade until after the issue is resolved in a later version of OneFS.
See the release notes for the target version of OneFS for a summary of new features, feature changes, and known issues. It 
is recommended to also review the release notes for each OneFS release between your current OneFS version and the target 
version.
NOTE: The new features and known issues for all supported OneFS versions have been compiled into this guide in the 
appendix.
Plan an upgrade schedule
An upgrade schedule can help ensure that the upgrade goes smoothly. The schedule should consider all the factors that go into 
an upgrade and estimate how long each stage of the upgrade process might take.
The upgrade process begins with ensuring that your OneFS cluster is ready to be upgraded. It is recommended that you set 
aside two weeks to check the cluster health and resolve software and hardware issues before performing the upgrade itself.
Upgrade 
maintenance window
The maintenance window should encompass the pre-upgrade, upgrade, and post-upgrade phases. 
Estimate the time that it takes to run the upgrade considering cluster size and upgrade type (parallel 
or simultaneous). Schedule a time to inform users when the upgrade will take place and that client 
connections might be slow, file access might be affected, and clients might be disconnected. A best 
practice is to upgrade the cluster during an off-hours maintenance window.
Schedule time for node and drive health checks and replacement of bad hardware. Include time to 
update configurations and settings that are not supported in the new version.
Estimate the time that it takes to back up your data, considering cluster size, number of files, types of 
files, and file size. Also include time to collect information about the cluster such as status, logs, and 
settings.
Planning an upgrade
11

---

## onefs-90-to-913-upgrade-guide::chunk_10

time that it takes to back up your data, considering cluster size, number of files, types of files, and file size. Also include time to collect information about the cluster such as status, logs, and settings. Planning an upgrade 11

If performing a parallel upgrade, consider whether you will configure client connection drain times, 
which will extend the required maintenance window, but lower the impact on client connections.
Build in time to let the upgrade jobs run to completion and to reestablish permissions and connections. 
Schedule time or extend the maintenance window to accommodate post-upgrade tasks such as 
reconfiguring custom settings, updating scripts to reflect command and functionality changes in the 
upgrade version, and potential troubleshooting.
(Optional) Upgrade 
a test cluster
If available, upgrading a test cluster with the same current version of OneFS before you upgrade your 
production cluster can expose issues that could slow down or prevent the upgrade of your production 
system.
After you upgrade a test cluster, verify that the cluster is operational and validate key workflows on 
the test cluster by simulating how administrators, users, and applications interact with the system.
12
Planning an upgrade

---

## onefs-90-to-913-upgrade-guide::chunk_11

upgrade of your production system. After you upgrade a test cluster, verify that the cluster is operational and validate key workflows on the test cluster by simulating how administrators, users, and applications interact with the system. 12 Planning an upgrade

Completing pre-upgrade tasks
Topics:
•
Pre-upgrade process - Overview
•
Collect cluster information
•
Check cluster readiness
•
Verify configurations and settings
•
Upgrade compatibility check
•
Maintenance Mode
•
On-Cluster Analysis tool
•
HealthCheck tool
•
Backup data
•
Complete or stop jobs in progress
•
Update Node Firmware Package
•
Update Drive Support Package
•
Configure IPMI ports
•
Enable Dell Technologies connectivity services 
•
Configure the cluster for upgrade notifications
•
Download the OneFS installation bundle file
Pre-upgrade process - Overview
Performing the pre-upgrade tasks described in this guide helps to ensure that the OneFS cluster hardware, software modules, 
configuration, features, and file system do not have preexisting issues that could adversely affect the upgrade process. 
Performing the pre-upgrade tasks also ensures that important cluster data is collected and any custom configuration settings 
are recorded.
Pre-upgrade - Summary
The following is a summary of steps to perform during the pre-upgrade phase:
1.
Collect cluster information.
a.
Collect cluster status.
b. Gather cluster logs.
c.
Check cluster hardware health.
d. Check cluster available space.
2. Resolve events and errors.
3. Verify cluster configuration.
a.
Preserve the Kerberos keytab file.
b. Install DataIQ or InsightIQ.
4. Download the OneFS installation file.
5. Run the upgrade compatibility check utility.
a.
Reconfigure unsupported SMB settings.
6. Enter Maintenance Mode.
7.
Run the On-Cluster Analysis tool.
8. Run the HealthCheck tool.
9. Back-up cluster data.
10. Complete system jobs.
11. Update Node Firmware Package.
12. Update Drive Support Package.
3
Completing pre-upgrade tasks
13

---

## onefs-90-to-913-upgrade-guide::chunk_12

SMB settings. 6. Enter Maintenance Mode. 7. Run the On-Cluster Analysis tool. 8. Run the HealthCheck tool. 9. Back-up cluster data. 10. Complete system jobs. 11. Update Node Firmware Package. 12. Update Drive Support Package. 3 Completing pre-upgrade tasks 13

13. Configure IPMI ports.
14. Enable Dell Technologies connectivity services.
Collect cluster information
Before you upgrade, collect and record key information about your OneFS cluster and how it is configured.
Review and save information about cluster status 
Before you upgrade, run the isi status command to get the status of your cluster, events, and jobs then save the 
information to a file.
Run the isi status > /ifs/data/isi_status_output command to save the output of the isi status command 
to a file named isi_status_output in the /ifs/data directory.
NOTE: Run the isi status command to view the status of the cluster, events, and jobs without saving the output to a 
file.
Gathering cluster logs
You can gather cluster logs and send the logs to Dell Technologies Support for analysis. Cluster logs can be sent automatically or 
manually through the cluster command-line and web administration interfaces.
NOTE: Your cluster must be connected to the Internet to be able to send log files directly. In newer versions of OneFS, you 
must also have Dell Technologies connectivity services enabled. For more information about how to gather and send cluster 
log files, see the PowerScale OneFS administration guide for your version of OneFS.
Gather cluster logs - Web UI
1.
To gather the log files, go to Cluster Management > Diagnostics.
2. Click Start Gather to open the Start Gather window.
3. Configure the log gather and click Start Gather.
For information about configuring the log gather, see the administration guide for your version of OneFS.
After the log gathering process is complete, a link to the file that the process generates appears under Filename in the 
Archived Info Manager section.
Gather cluster logs - CLI
To gather the log files in OneFS 8.0.1.0 and later, run the following command:
isi diagnostics gather start
NOTE: The user needs the ISI_PRIV_SYS_SUPPORT privilege to run this command.
The files that are generated during the log gathering process are stored on the cluster in the /ifs/data/
Isilon_Support/pkg directory.
Check cluster readiness
Completing pre-upgrade tasks such as checking the health of the hardware components on the cluster, ensuring that storage 
space requirements are met, and managing outstanding cluster events and errors are recommended for a successful upgrade.
14
Completing pre-upgrade tasks

---

## onefs-90-to-913-upgrade-guide::chunk_13

readiness Completing pre-upgrade tasks such as checking the health of the hardware components on the cluster, ensuring that storage space requirements are met, and managing outstanding cluster events and errors are recommended for a successful upgrade. 14 Completing pre-upgrade tasks

Check hardware health - web administration interface
Use the OneFS web administration interface to evaluate the health of the clusters hardware components. Log in as root user 
and perform the following steps on your cluster:
1.
Click Cluster Management > Hardware Configuration.
2. In the Nodes tab, check that each node has a healthy status.
3. In the Drives tab, check that each drive has a healthy status.
4. If any correctable or fatal errors are reported, do not continue the upgrade. If the errors cannot be resolved, contact Dell 
Technologies Support.
NOTE: Certificate expiration issues may affect Dell Networking switches running Dell Network Operating System (DNOS) 
version 10.5.0.6C1 or earlier that are used for backend traffic and configured as a single switch (also known as a flat switch, 
or a Top of Rack (TOR) switch). For more information, including a list of affected switches and a workaround, see DTA 
190714.
Check hardware health - CLI
Run the following commands from the OneFS command-line interface as root user to evaluate the health of the cluster's 
hardware components and the status of job engine jobs.
1.
To return information about cluster health and check for jobs or devices that report a status of ATTENTION, SMARTFAIL, 
or DOWN.
isi status -v
2. To check for drives that do not report a status of HEALTHY, L3, or JOURNAL.
isi_for_array -s 'isi devices drive list | egrep -v "HEALTHY|L3|JOURNAL"'
3. To check the mirror status of the boot drives on each node.
isi_for_array -s 'gmirror status'
NOTE: If a drive is degraded, do not continue with the upgrade until the issue is resolved.
4. If the cluster has a backend InfiniBand network, confirm whether a node has been assigned the OpenSM (subnet manager) 
main role.
isi_for_array -s 'ps -auwwwx | grep opensm' | grep master
Confirm that the output displays only one node in the cluster as the main (opensm). The output should be similar to the 
following:
node-2: root   1610   0.0   2.3   436292   384672   ??   Ss   20May15   97:31.63   
opensm: 0x00151b00007a671b main (opensm)
Check the available free space
Ensure that the minimum available-space requirements for the cluster, nodes, node pools, and critical directories are met before 
you upgrade. Do not continue with the upgrade if the minimum available-space requirements are not met.
Completing pre-upgrade tasks
15

---

## onefs-90-to-913-upgrade-guide::chunk_14

free space Ensure that the minimum available-space requirements for the cluster, nodes, node pools, and critical directories are met before you upgrade. Do not continue with the upgrade if the minimum available-space requirements are not met. Completing pre-upgrade tasks 15

Available space requirements for clusters, nodes, node pools, and 
directories
The cluster, nodes, node pools, and several critical directories in the file system must meet available space requirements before 
upgrading OneFS. If the available space for any of these items falls below the minimum requirement, make more space available 
before upgrading. Otherwise, the upgrade process fails and might not return an error indicating available space as the cause.
Table 2. Item Requirements 
Item
Minimum Requirement
Task
Cluster
The cluster cannot be more than 
90 percent capacity.
Make more space available.
Node
Each node cannot be more than 
92 percent capacity.
Make more space available.
Node pool
Each node pool cannot be more 
than 90 percent capacity.
Make more space available.
root partition (/)
The root partition cannot be more 
than 94 percent capacity.
If this directory is at or near the minimum available-
space requirement, see the following resources for 
steps to address the issue:
●
Event ID 100010003: The /(root) partition is near 
capacity.
/ifs
The /ifs directory cannot be 
more than 90 percent capacity.
If this directory is at or near the minimum available-
space requirement, see the following resources for 
steps to address the issue:
●
Event ID 100010004: The cluster's /ifs partition 
is near capacity.
/var
The /var partition cannot be 
more than 90 percent capacity.
If this directory is at or near the minimum available-
space requirement, see the following resources for 
steps to address the issue:
●
Event ID 100010001: The /var partition is near 
capacity.
/var/crash
The /var/crash directory 
cannot be more than 90 percent 
capacity.
If this directory is at or near the minimum available-
space requirement, see the following resources for 
steps to address the issue:
●
Event ID 100010002: The /var/crash partition is 
near capacity.
Confirm used and available space
●
To confirm how much space is being used on the cluster and on each node, run the following command:
isi stat
●
To confirm how much space is being used in each node pool, run the following command:
isi stat -p
●
To confirm how much space is being used by critical directories on the cluster, run the following command:
isi_for_array -s 'df -h'
The isi_for_array output is similar to the following for each node in the cluster:
virtual-demo-3: Filesystem   Size  Used  Avail  Capacity  Mounted on
--------------------------------------------------------------------
virtual-demo-3: /dev/imdd0a  495M  418M  38M    92%       /
16
Completing pre-upgrade tasks

---

## onefs-90-to-913-upgrade-guide::chunk_15

following command: isi_for_array -s 'df -h' The isi_for_array output is similar to the following for each node in the cluster: virtual-demo-3: Filesystem Size Used Avail Capacity Mounted on -------------------------------------------------------------------- virtual-demo-3: /dev/imdd0a 495M 418M 38M 92% / 16 Completing pre-upgrade tasks

virtual-demo-3: devfs        1.0K  1.0K  0B     100%      /dev
virtual-demo-3: /dev/imdd1a  495M  6.7M  449M   1%        /var
virtual-demo-3: /dev/imdd2a  496M  5.9M  451M   1%        /var/crash
virtual-demo-3: OneFS        40G   283M  20G    1%        /ifs
virtual-demo-2: Filesystem   Size  Used  Avail  Capacity  Mounted on
--------------------------------------------------------------------
virtual-demo-2: /dev/imdd0a  495M  417M  38M    92%       /
virtual-demo-2: devfs        1.0K  1.0K  0B     100%      /dev
virtual-demo-2: /dev/imdd1a  495M  6.1M  449M   1%        /var
virtual-demo-2: /dev/imdd2a  496M  5.9M  451M   1%        /var/crash
virtual-demo-2: OneFS        40G   283M  20G    1%        /ifs
Resolve outstanding events and errors
Before you begin your upgrade, resolve any outstanding critical events, errors, and failures, as these issues can disrupt the 
OneFS upgrade process.
1.
Run the following command to view all events on the cluster:
isi event groups list --sort=severity
●
If the command returns any critical errors, check the log files in the following directories for more information:
○
/var/log
○
/var/log/messages
○
/var/crash
●
NOTE: If any log files contain messages about a dynamic sector recovery (DSR) failure or a Data Integrity (IDI) 
failure, contact PowerScale before you upgrade.
2. Cancel non-critical events before upgrading to prevent a recurrence of notifications that you know to be harmless.
If you have critical events that you are unable to resolve, contact support before upgrading.
Verify configurations and settings
Confirm that your OneFS configurations for CloudPools, NIC aggregation, Kerberos, InsightIQ, and SMB are supported by the 
target version of OneFS to which your are upgrading.
Upgrading in a Cloudpools environment
If you're upgrading a OneFS 8.x cluster to OneFS 8.2.x. or later with a Cloudpools environment, there are additional items to 
consider. For more information on pre-upgrade and upgrade steps, see KB article 000020736
Upgrading in a FIPS or STIG environment
If you are upgrading to OneFS 9.5 or later, and you have enabled Federal Information Processing Standard (FIPS) or Security 
Technical Implementation Guides (STIG) on your cluster, you must disable FIPS or STIG before you upgrade. For more 
information about FIPS or STIG, see the OneFS Security Configuration Guide.
Preserve the Kerberos keytab file
If Kerberos authentication is configured on the cluster, upgrading OneFS might delete the local /etc/<name>.keytab file 
that is on each node. Choose one of the following methods to preserve the keytab file during the upgrade:
●
Copy the keytab file to the /ifs directory where it can be accessed by all nodes on the cluster instead of saved locally on 
each node.
Completing pre-upgrade tasks
17

---

## onefs-90-to-913-upgrade-guide::chunk_16

methods to preserve the keytab file during the upgrade: ● Copy the keytab file to the /ifs directory where it can be accessed by all nodes on the cluster instead of saved locally on each node. Completing pre-upgrade tasks 17

●
Add the following text to the /etc/mcp/override/user_preserve_files.xml file of each node on the cluster 
where <name> is the name of the keytab file:
<?xml version="1.0" encoding="UTF-8"?>
<user_preserve>
<files>
<file name="etc/allow_unsupported_boot" recursive="no">
</file>
...
...
<file name="etc/<name>.keytab" recursive="no" />
</files>
</user_preserve>
Install a supported version of DataIQ or InsightIQ
Before you upgrade OneFS, confirm the version of InsightIQ that you are running is compatible with the target version of OneFS 
to which you are upgrading. If the versions are not compatible, upgrade InsightIQ before upgrading OneFS.
See the Supportability and Compatibility Guide on the Dell Support site for OneFS compatibility information.
See the InsightIQ - Info hub for documents and content related to InsightIQ.
Upgrade compatibility check
The pre-upgrade compatibility check examines cluster settings, activities, and statuses to verify whether your cluster is 
compatible with the target version of OneFS to which you are upgrading.
The pre-upgrade compatibility check utility is included in each OneFS installation package.
In OneFS 9.9.0 and later versions, the pre-upgrade compatibility check is also included in the web interface.
You can run the utility alone or as part of the upgrade process.
Run the pre-upgrade compatibility check utility using the CLI
To confirm that your OneFS cluster is compatible with the target version that you are upgrading to, run the pre-upgrade 
compatibility check utility in the OneFS command-line interface.
NOTE: The pre-upgrade compatibility check utility is in each OneFS installation package, which must be downloaded and 
accessible in the /ifs directory.
1.
Open a secure shell (SSH) connection to any node in the cluster and log in to the cluster with the root account.
2. Start the pre-upgrade compatibility check utility by running the following command, where <install-image-path> is the file 
path of the upgrade installation file.
isi upgrade cluster assess start <install-image-path> 
NOTE: The pre-upgrade compatibility check utility might take several minutes to run. If the utility returns errors, resolve 
the errors before continuing with the upgrade. Warnings are informational and do not prevent an upgrade.
3. When a pre-upgrade check fails, view the results of the pre-upgrade assessment results by running the following command 
as a starting point for debugging:
isi upgrade cluster assess view
4. To retry the last action when a previous upgrade attempt fails and skip an optional check, run the following command:
isi upgrade retry-last-action --skip-optional
Run the pre-upgrade compatibility check using the web interface
In OneFS 9.9.0 and later versions, you can confirm that your cluster is compatible with the target version that you are upgrading 
to by running the pre-upgrade compatibility check in the web interface. The web interface reports the pre-upgrade optional 
18
Completing pre-upgrade tasks

---

## onefs-90-to-913-upgrade-guide::chunk_17

later versions, you can confirm that your cluster is compatible with the target version that you are upgrading to by running the pre-upgrade compatibility check in the web interface. The web interface reports the pre-upgrade optional 18 Completing pre-upgrade tasks

assessments (warnings) and mandatory assessments (failures that block the upgrade), but does not display what hooks failed. 
Run the pre-upgrade compatibility check utility using the CLI to view the upgrade failed checks.
Run the pre-upgrade compatibility check by performing the following steps using the OneFS web interface:
1.
On the Cluster Management > Upgrade screen, click the Overview tab.
2. Click Start Precheck to start the pre-upgrade assessment.
3. In the Precheck modal window, browse to the file path of the upgrade installation file and then click Start Precheck.
During the pre-upgrade assessment, a progress bar displays the percentage of completion. When the pre-upgrade 
assessment completes successfully without failures, a table displays the results of the HookPreUpgradeOptional and 
HookPreUpgradeMandatory tests. If tests fail, the web interface reports the warnings and what will block the upgrade. It 
does not report what specific hooks failed. To view the upgrade failed checks, go to the next step.
4. To view the pre-upgrade failed checks, run the isi upgrade assess view command by running the CLI command 
isi upgrade assess view.
Resolve any failed checks before continuing with the upgrade. Optional pre-upgrade checks are informational and do not 
prevent an upgrade. When optional pre-upgrade checks fail, you can either fix and resume the upgrade or skip and resume 
the upgrade. Mandatory pre-upgrade checks block an upgrade when they fail. The only option when mandatory checks fail is 
to resolve the issues or to rollback the upgrade.
5. After resolving the failed checks, click the Upgrade OneFS button. In the Upgrade OneFS modal window, provide the file 
path to the upgrade image, the upgrade type, and relevant configurations. By default, the Drain time out is set to 5 minutes 
and the Alert time out is set to off. Close the window to start the upgrade.
A progress bar indicates the upgrade status for each node. To stop the upgrade, click Cancel.
6. The progress bar turns green after a successful upgrade. Click either Rollback Upgrade or Commit Upgrade.
After a failed upgrade, resolve the issues, and then click the Retry Upgrade button to retry the upgrade operation. The 
Node Details tab displays a table listing all nodes in the cluster along with their versions. You can filter the node data based 
on version and search for specific nodes or versions.
Pre-upgrade compatibility check
The pre-upgrade compatibility check assesses the cluster and returns warnings or errors if something is not compatible with 
the version of OneFS to which you are upgrading. In OneFS 9.9.0 and later versions, additional pre-upgrade compatibility 
checks are included in the pre-upgrade compatibility check utility that you can run on the command-line interface or in the web 
administration interface. The pre-upgrade compatibility check examines the following areas:
Table 3. Pre-upgrade Compatibility Check Specifications 
Check type
Description
Recommendation
Disk load
Checks the cluster usage level and 
returns a warning if the disk load is 
greater than 50%.
Disconnect all client connections and 
stop all system jobs before upgrading.
Free Space
Checks cluster free space and returns 
a warning if capacity thresholds are 
exceeded for the following partitions:
●
/
●
/var
●
/ifs
●
/root
●
Node pools
Free up space in the necessary partitions 
before upgrading.
Drive stalls
Checks the health of the drives in the 
cluster.
Smartfail and resolve the stalled drive 
issue before upgrading.
Smartfail operation status
Determines if a Smartfail operation is 
running on the cluster.
Wait for the Smartfail operation to 
complete before upgrading.
IntegrityScan job status
Determines if an IntegrityScan job is 
running on the cluster.
Wait for the job to complete before 
upgrading.
Unresolved critical alerts
Checks for any critical alerts on the 
cluster.
Resolve all critical alerts before 
upgrading.
Unsupported SMB configuration
Checks for unsupported SMB settings 
on the cluster.
Reconfigure any unsupported SMB 
settings before upgrading.
Completing pre-upgrade tasks
19

---

## onefs-90-to-913-upgrade-guide::chunk_18

upgrading. Unresolved critical alerts Checks for any critical alerts on the cluster. Resolve all critical alerts before upgrading. Unsupported SMB configuration Checks for unsupported SMB settings on the cluster. Reconfigure any unsupported SMB settings before upgrading. Completing pre-upgrade tasks 19

Table 3. Pre-upgrade Compatibility Check Specifications (continued)
Check type
Description
Recommendation
SMB access zone association
Checks if any SMB shares are associated 
with multiple access zones where the 
share paths overlap.
Resolve issues where the share paths 
overlap before upgrading. The upgrade 
will succeed, but you cannot create new 
SMB shares until the overlap issue is 
resolved.
Kerberos keytab
Checks if the Kerberos keytab file will be 
preserved after the upgrade.
You must configure the Kerberos 
settings to preserve the keytab file 
before upgrading.
HDFS Kerberos keytab
Checks if the HDFS Kerberos keytab file 
will be preserved after the upgrade.
You must configure the Kerberos 
settings to preserve the keytab file 
before upgrading.
Swift active
Checks the cluster to determine if Swift 
is enabled or if a swift account is 
configured on the cluster.
You must disable Swift and remove a 
Swift account before upgrading.
Reconfigure unsupported SMB settings
If the SMB settings on the cluster are not supported by the target version of OneFS to which you are upgrading, the upgrade 
might fail. The upgrade compatibility check utility confirms whether your current SMB settings are supported.
If the upgrade compatibility check utility detects unsupported SMB settings, remove or modify the unsupported SMB settings 
through the command-line interface or web administration interface before you upgrade.
NOTE: SMB1 is disabled during the upgrade process which might cause some clients to have authentication issues. Due to 
security concerns, Dell Technologies does not recommend enabling the SMB1 protocol. To ensure long-term compatibility, 
consider transitioning away from this protocol.
Reduce disruption to SMB connections during upgrades
During parallel upgrades, SMB connections must be moved from one node to another during the upgrade process. In OneFS 
9.9.0 and later versions, the disruption manager is enabled by default and the cluster default drain timeout is set to 5 minutes to 
reduce disruptions to SMB connections during upgrades.
When the disruption manager is enabled, OneFS delays rebooting nodes until one of the following conditions is met:
●
All SMB clients have disconnected from the node.
●
SMB clients are still connected to the node upon expiration of the drain time-out. This minimizes disruptions to cluster 
operations.
In OneFS 9.9.0 and later versions, you are no longer required to set the cluster upgrade default drain timeout value by running 
the isi upgrade cluster drain timeout --timeout <integer> command. In the web interface, the Cluster 
Management > Upgrade > Upgrade OneFS > Enable Disruption Manager setting is enabled by default, and the Drain time 
out value is set to 5 minutes.
NOTE: Setting the Drain time out value to less than 5 minutes may not allow SMB connections to transition gracefully 
which may lead to further disruptions during upgrades. Note that the Alert time out value, which is the timeout when an 
alert is triggered, must be set to less than the Drain time out value.
Maintenance Mode
When enabled, Maintenance Mode detects certain maintenance tasks and automatically starts a maintenance window that 
suppresses CELOG alerts while the mode is active.
In OneFS 9.9.0.0 and later releases, Maintenance Mode has been updated to allow a cluster to enter maintenance mode 
automatically when certain maintenance tasks are detected. Tasks such as simultaneous upgrades, patch installation, rolling 
reboots, and hardware replacement.
20
Completing pre-upgrade tasks

---

## onefs-90-to-913-upgrade-guide::chunk_19

9.9.0.0 and later releases, Maintenance Mode has been updated to allow a cluster to enter maintenance mode automatically when certain maintenance tasks are detected. Tasks such as simultaneous upgrades, patch installation, rolling reboots, and hardware replacement. 20 Completing pre-upgrade tasks

This feature can be disabled, which allows administrators to manually start and end maintenance windows. Manual maintenance 
windows are limited to 199 hours to avoid indefinite maintenance windows.
You can manage maintenance mode status using the web interface and view the maintenance window history.
See the OneFS Web Administration Guide or the OneFS CLI Administration Guide for information about managing maintenance 
mode.
On-Cluster Analysis tool
The PowerScale On-Cluster Analysis (OCA) tool analyzes the health status of a running cluster and helps you prepare for 
an upgrade. The OCA tool analyzes your cluster and displays any issues that it encounters, a summary of the issue, and any 
associated KB articles to help you resolve the issue. The OCA tool also has a feature that provides you with an estimated 
upgrade plan based on the analysis.
For more information about the OCA tool, please see the KB article: How to run the On-Cluster Analysis tool
HealthCheck tool
The HealthCheck tool enables you to evaluate the status of specific software and hardware components of your cluster and 
your cluster environment. For more information about the HealthCheck tool, see the PowerScale OneFS Administration Guide 
for your version of OneFS.
Backup data
It is recommended to backup your cluster data immediately before you upgrade. Schedule sufficient time for the back up to 
complete before the upgrade window.
SyncIQ backup
SyncIQ is one option that you can use to backup your OneFS cluster. SyncIQ creates and references snapshots to replicate a 
consistent point-in-time image of a root directory.
For more information about backing up your OneFS cluster, see the OneFS CLI Administration Guide or the OneFS Web 
Administration Guide for your version of OneFS.
NOTE: If you are upgrading your cluster from OneFS 8.1.0.x or earlier to OneFS 8.1.1.x, 8.1.2.x, or 8.1.3.x, and your cluster 
is in Compliance mode, you must ensure that all SyncIQ partners are on the same code and patch level OneFS before 
restarting SyncIQ backups, or the backups fail. This issue is resolved in OneFS 8.2.0 and later.
NOTE: If you are upgrading your cluster to OneFS 8.2.0 through 9.2.1.0, are using SyncIQ, and have non-networked 
(NANON) nodes on your source cluster, SyncIQ jobs might fail after the upgrade. For more information including a 
workaround, see the KB article SyncIQ jobs failing with NANON after upgrade
NDMP backup
Other OneFS cluster backup options include using the Network Data Management Protocol (NDMP).
From a backup server, you can perform both NDMP three-way backup and NDMP two-way backup processes between a cluster 
and backup devices such as tape devices, media servers, and virtual tape libraries (VTLs).
See the OneFS Web Administration Guide or the OneFS CLI Administration Guide for information about backing up data using 
NDMP.
Complete NDMP backups
Before you upgrade, you must wait for Network Data Management Protocol (NDMP) backups to finish so you have saved 
copies of your data.
Completing pre-upgrade tasks
21

---

## onefs-90-to-913-upgrade-guide::chunk_20

Administration Guide for information about backing up data using NDMP. Complete NDMP backups Before you upgrade, you must wait for Network Data Management Protocol (NDMP) backups to finish so you have saved copies of your data. Completing pre-upgrade tasks 21

NOTE: If you cannot wait for NDMP backups to finish, stop the active NDMP backups 30– 60 minutes before the upgrade. 
The NDMP backup process requires this additional time to come to a stop.
For instructions on how to stop backup jobs, see the documentation for your backup application.
NOTE: If you are upgrading from OneFS version 8.0.x or 8.1.x to OneFS 8.2.x, you must disable the NDMP service before 
performing the upgrade.
Back up custom settings
Most settings are preserved during a OneFS upgrade. However, documenting and backing up custom settings enables you to 
reapply any settings that are not preserved during the upgrade process.
Document and back up the following custom settings:
Table 4. Custom Settings Specifications 
Setting
Description
Recommendation
System 
Administration 
Manager (SAM) 
database
The SAM database contains 
checksums and other binary data.
As a best practice, back up the SAM database that is located in / 
ifs/.ifsvar/modules/auth/sam/sam.db before you upgrade.
SMB audit 
logging
If you have an audit log directory 
in /ifs, you might have custom 
SMB logging settings configured.
After upgrading, you must reconfigure SMB audit logging. See File 
System Auditing with the Common Event Enabler (CEE) for more 
information about SMB audit logging.
Passwords for 
local user 
accounts
After you upgrade, you might 
have to reset the passwords 
of the local user accounts that 
you configured on the cluster. 
Other users should be prepared to 
reset the passwords of their local 
accounts after the upgrade.
Make a list of the local accounts and their passwords before you 
upgrade.
sysctl 
parameters
If you changed the default 
value that is assigned to one 
or more sysctl parameters 
by editing the /etc/mcp/
override/sysctl.conf file, 
the etc/mcp/templates 
directory, or the /etc/local/
sysctl.conf file, you might 
need to reset the parameter after 
you upgrade.
If you modified a sysctl 
parameter by editing another 
file—for example, the /etc/
sysctl.conf file—the change 
will not be preserved during the 
upgrade.
PowerScale does not recommend modifying sysctl parameters 
unless you are instructed to do so by Dell Technologies Support. If 
you must modify a sysctl parameter, configure the parameter in 
the /etc/mcp/override/sysctl.conf file to ensure that the 
change is preserved when you upgrade a node or a cluster.
Before you upgrade, document your custom sysctl parameters and 
back up the /etc/mcp/override/sysctl.conf, the etc/mcp/
templates directory, and the /etc/local/sysctl.conf files.
For more information about making sysctl changes persist through 
upgrades, see KB article 000102543 and KB article 000083411.
Cron jobs
Cron jobs settings that were 
not configured in the /etc/mcp/
override/crontab.smbtime 
file are not preserved during an 
upgrade.
Document and back up custom cron job settings or configure them 
in the /etc/mcp/override/crontab.smbtime file before you 
upgrade.
After you upgrade, you might have to modify a cron job to 
accommodate changes to OneFS commands.
22
Completing pre-upgrade tasks

---

## onefs-90-to-913-upgrade-guide::chunk_21

upgrade. Document and back up custom cron job settings or configure them in the /etc/mcp/override/crontab.smbtime file before you upgrade. After you upgrade, you might have to modify a cron job to accommodate changes to OneFS commands. 22 Completing pre-upgrade tasks

Complete or stop jobs in progress
You should ensure that there are no jobs running on your OneFS cluster before beginning the upgrade. Wait for jobs to fully 
complete or stop jobs before upgrading.
Complete system jobs
Ensure that no system jobs are running during the upgrade by allowing system jobs to finish before the upgrade starts or by 
canceling them. OneFS performs system jobs through a service that runs in the background, and if any system jobs are running 
during the upgrade, the upgrade process might fail.
1.
To check for running system jobs, run the following command, and make a note of the job ID for any jobs that you want to 
cancel:
isi job status
2. To cancel a job, run the following command where <job_id> is the ID of the job you want to cancel:
isi job jobs cancel <job_id>
NOTE: Do not cancel the Upgrade, FlexProtect, FlexProtectLin, or IntegrityScan jobs. If any of these four system jobs 
are running, you cannot continue the upgrade. If an Upgrade, FlexProtect, FlexProtectLin, or IntegrityScan system job 
takes longer than expected to complete, contact Dell Technologies Support.
Update Node Firmware Package
Before upgrading your OneFS cluster, ensure that your nodes are running the most recent version of firmware that is found in 
the Node Firmware Package.
For additional information about updating node firmware, see the OneFS Node Firmware Package site.
NOTE: In OneFS 9.2.0.0 and later, you can choose to update the Node Firmware Package during a parallel upgrade. If you 
choose to perform the Node Firmware update during an upgrade, delay this step until the Performing a Parallel Upgrade 
chapter.
Update Drive Support Package
Before upgrading your OneFS cluster, ensure that your drives are running the most recent version of firmware found in the 
Drive Support Package.
For more information, see the OneFS Drive Support Package site.
Configure IPMI ports
If you have enabled Intelligent Platform Management Interface (IPMI) ports, it is recommended that you change the IPMI 
port IP configuration to static in the BIOS settings for each affected node before the upgrade. If you change the IPMI port 
configuration during the upgrade process, and your workflow requires the IPMI ports be enabled, you must manually re-enable 
the ports after the upgrade process is complete.
NOTE: Use of IPMI ports is supported in OneFS version 8.2.2 and later.
Enable Dell Technologies connectivity services
Dell Technologies connectivity services allow remote support access to your cluster.
Completing pre-upgrade tasks
23

---

## onefs-90-to-913-upgrade-guide::chunk_22

ports after the upgrade process is complete. NOTE: Use of IPMI ports is supported in OneFS version 8.2.2 and later. Enable Dell Technologies connectivity services Dell Technologies connectivity services allow remote support access to your cluster. Completing pre-upgrade tasks 23

NOTE: Dell Technologies connectivity services are recommended for all clusters that can send telemetry data off-cluster 
and is a replacement for the legacy connectivity system - Secure Remote Services (SRS). SRS has reached end-of-service-
life.
●
SRS-enabled clusters are automatically migrated to Dell Technologies connectivity services when upgrading from OneFS 
9.10.0.0 or earlier to 9.11.0.0 or later. In order for this migration to be effective, SRS should remain enabled throughout the 
course of the upgrade.
Enabling Dell Technologies connectivity services - connect directly 
to Dell support
Enable Dell Technologies connectivity services to connect directly to Dell support by performing the following steps:
1.
On the Cluster Management > General settings screen, click the Connectivity Services tab.
2. Click the Connect now button to connect to Dell Technologies connectivity services.
3. To accept the Telemetry Notice, check the box and click the Accept button.
4. Enter the Primary Support Contact and Secondary Support Contact information and click the Next button.
5. Select one or more IPv4-family or IPv6 network pools or subnets to use when connecting.
6. Click the Connect now button.
7.
Enter the Access key and PIN.
NOTE: On newly installed clusters, a hardware key is automatically used instead of an Access Key and PIN.
8. Click the Remote support tab to enable remote support services, configure telemetry and CloudIQ, and create support 
cases automatically.
9. Click Finish Setup.
Configure the cluster for upgrade notifications
In PowerScale OneFS 9.12.0.0 and later versions: If you have Dell Technologies connectivity services enabled, the PowerScale 
OneFS cluster can subscribe to upgrade notifications.
You can configure OneFS to automatically download the available upgrade packages and install them with one click from the 
web administration interface. Available upgrade package names and information are managed by Dell Technologies according 
to cluster telemetry data and are automatically displayed in the web administration interface. You can also enable upgrade 
notifications from the command-line interface by running the isi upgrade package setting modify command.
Configure OneFS automatic upgrade notifications
You can use the web administration interface or the command-line interface to configure the cluster to subscribe to upgrade 
notifications.
Available upgrade packages are managed by Dell according to the cluster telemetry data. You must enable Dell Technologies 
connectivity services to automatically display the available upgrade packages in the web administration interface. For more 
information, see the section entitled Enabling Dell Technologies connectivity services - connect directly to Dell support in this 
guide.
1.
To enable upgrade notifications from the command-line interface, run the following command:
isi upgrade package setting modify --enable-subscription <true | false>
2. To automatically display available upgrade package names and information from the web administration interface, log in to 
any node in the cluster with the root account.
3. Click Cluster Management > Upgrade.
4. To perform an upgrade precheck, click the Overview tab and then click Start Precheck . A precheck will assess the 
readiness of the cluster before the upgrade to avoid interruptions or failures.
5. To configure optional automatic upgrade package downloads, click the Settings tab.
6. Cick Download new package (OneFS package + Firmwares + Drivers).
24
Completing pre-upgrade tasks

---

## onefs-90-to-913-upgrade-guide::chunk_23

the readiness of the cluster before the upgrade to avoid interruptions or failures. 5. To configure optional automatic upgrade package downloads, click the Settings tab. 6. Cick Download new package (OneFS package + Firmwares + Drivers). 24 Completing pre-upgrade tasks

7.
Select Latest LTS Maintenance Release, Latest LTS Package for OneFS, or Latest Package.
Download the OneFS installation bundle file
1.
NOTE: If you have not configured OneFS for automatic upgrade notifications and one-click upgrades, you can manually 
download the installation bundle using the following instructions.
From the OneFS Downloads page, download the installation bundle file for the target version of OneFS to which you are 
upgrading.
NOTE: It is recommended that you use a OneFS installation bundle file that includes the latest patches. If the 
installation bundle is used, you can skip the patch installation task in the post-upgrade steps.
2. Open a secure shell (SSH) connection to any node in the cluster and log in using the root account.
3. Move the downloaded install bundle tarfile into the /ifs/data directory on the cluster that you want to upgrade.
4. To extract files from the zipped tarfile, run the following command where <installation-file-name>.tgz is the name of the 
OneFS zipped tarfile:
tar xvfp /ifs/data/<installation-file-name>.tgz /ifs/data/
5. After unpacking the zipped tarfile, run the following commands:
a.
To import the package into the OneFS Catalog, run the isi upgrade catalog import /ifs/data/
<filename>.isi command.
b. To verify the package, run the isi upgrade catalog verify --file /ifs/data/<filename>.isi 
command.
c.
To list the OneFS Catalog entries, run the isi upgrade catalog list command.
Completing pre-upgrade tasks
25

---

## onefs-90-to-913-upgrade-guide::chunk_24

the isi upgrade catalog import /ifs/data/ <filename>.isi command. b. To verify the package, run the isi upgrade catalog verify --file /ifs/data/<filename>.isi command. c. To list the OneFS Catalog entries, run the isi upgrade catalog list command. Completing pre-upgrade tasks 25

Performing the OneFS upgrade
Topics:
•
Upgrade process overview
•
Completing a parallel upgrade of OneFS
•
Completing a simultaneous upgrade of OneFS
•
Adding a node to the cluster while an upgrade is in progress
•
Committing an upgrade of OneFS
•
Rolling back an upgrade of OneFS
•
Verify the OneFS installation using the CLI
Upgrade process overview
Upgrading OneFS can be done using either the web interface or the command-line interface and includes a series of tasks 
that Administrators must perform before, during, and after the upgrade. A OneFS installation image is required to upgrade your 
cluster. See the Download the OneFS image section for more information.
In PowerScale OneFS 9.12.0.0 and later versions, if you have Dell Technologies connectivity services enabled, the PowerScale 
OneFS cluster can subscribe to upgrade notifications. Available upgrade package names and information are managed by Dell 
Technologies according to cluster telemetry data and are automatically displayed in the WebUI. You can configure OneFS 
to automatically download the available upgrade packages and install them with one click from the WebUI or command-line 
interface.
There are two options available for upgrading your OneFS cluster: parallel upgrades or simultaneous upgrades.
●
Parallel upgrade (for OneFS 8.2.2 and later)
●
Simultaneous upgrade
NOTE: In PowerScale OneFS 9.11.0.0, rolling upgrades have been deprecated. A parallel upgrade is the recommended 
upgrade option.
Upgrade - Summary
The following is a summary of steps to perform during the upgrade phase:
1.
Perform the upgrade.
2. Commit the upgrade.
3. Verify the upgrade.
Completing a parallel upgrade of OneFS
If you perform a parallel upgrade, subsets of nodes within the OneFS cluster are restarted in an undetermined order. During 
a parallel upgrade, client connections to the restarting subset of nodes are disconnected, but other subsets of nodes remain 
available for client connection.
NOTE: The parallel upgrade feature is available in OneFS version 8.2.2 and later. It is recommended that you use parallel for 
non-disruptive upgrades.
NOTE: If optional compatibility checks fail during an upgrade, run the command isi upgrade retry-last-action 
--skip-optional.
4
26
Performing the OneFS upgrade

---

## onefs-90-to-913-upgrade-guide::chunk_25

is available in OneFS version 8.2.2 and later. It is recommended that you use parallel for non-disruptive upgrades. NOTE: If optional compatibility checks fail during an upgrade, run the command isi upgrade retry-last-action --skip-optional. 4 26 Performing the OneFS upgrade

You can also run the following commands for more information if a cluster fails during the pre-upgrade steps:
isi upgrade cluster assess view
isi upgrade view
Performing a parallel upgrade using the web administration 
interface
You can use the web administration interface to upgrade the version of OneFS that is running on your cluster.
Perform the pre-upgrade steps in this guide, confirm cluster health, and resolve any compatibility issues before upgrading to the 
new version of OneFS.
1.
Log in to any node in the cluster through the web administration interface with the root account.
2. Click Cluster Management > Upgrade.
3. Click Upgrade OneFS.
4. Enter the file path location of the upgrade image to install. The file path must be accessible in an /ifs directory.
5. (Optional) In OneFS 9.2.0.0 and later, to update node firmware during the upgrade, enter the file path location of the node 
firmware package.
6. In the Upgrade Type drop-down list, select Parallel Upgrade.
7.
(Optional) To skip optional pre-upgrade checks related to compatibility, cluster health, or cluster readiness, select Skip 
optional pre-upgrade checks.
8. (Optional) In OneFS 9.2.0.0 and later, to manage disruption to SMB client connections, follow these steps:
a.
Check Enable disruption manager
b. (Optional) Check Wait Forever to wait for all SMB clients to disconnect from a node before upgrading.
c.
Enter the Drain time out to specify the amount of time OneFS waits for clients to manually disconnect before the node 
reboots and upgrades.
d. Enter the CELOG time out to specify the amount of time OneFS waits for clients to disconnect before alerting the 
OneFS administrator. This time out allows the administrator to work with the connected clients before rebooting the 
node.
9. Click Start Upgrade to begin the upgrade.
The cluster might display several confirmation messages. Confirm each message to continue the upgrade process.
NOTE: In 9.2.0.0 and later, you can use the upgrade status screen to monitor the progress of your upgrade, view 
connected clients, and delay draining clients from specific nodes.
After the upgrade, a number of upgrade-related jobs may continue to run on the cluster for some time. During this time, the 
cluster is accessible, but you might experience a decrease in cluster performance. After the jobs complete, performance will 
return to normal. At this stage, the upgrade is complete, but is not committed. You can still roll back to the previous version of 
OneFS. Some new features in the upgrade might not be available until the upgrade is committed.
Performing a parallel upgrade using the CLI
You can use the command-line interface to upgrade the version of OneFS that is running on your cluster.
Perform the pre-upgrade steps in this guide, confirm cluster health, and resolve any compatibility issues before upgrading to the 
new version of OneFS.
1.
Open a secure shell (SSH) connection on any node in the cluster and log in with the root account.
2. In OneFS 9.2.0.0 and later, you can manage the amount of time OneFS waits to disconnect client connections using the isi 
upgrade cluster drain command and sub-commands.
3. To perform a parallel upgrade, run the following command, where <install-image-path> is the file path of the upgrade install 
image. The file path must be accessible in an /ifs directory.
isi upgrade cluster start --parallel <install-image-path> 
Performing the OneFS upgrade
27

---

## onefs-90-to-913-upgrade-guide::chunk_26

perform a parallel upgrade, run the following command, where <install-image-path> is the file path of the upgrade install image. The file path must be accessible in an /ifs directory. isi upgrade cluster start --parallel <install-image-path> Performing the OneFS upgrade 27

In OneFS 9.2.0.0 and later, you can include the firmware upgrade with your OneFS upgrade. To perform a parallel upgrade 
that includes a firmware upgrade, run the following command where <install-image-path> is the file path of the upgrade 
install image and <firmware-path> is the file path of the firmware package.
isi upgrade cluster start --parallel <install-image-path> --fw-pkg <firmware-path>
NOTE: The isi upgrade cluster command runs asynchronously. The command does not run the entire upgrade 
process; instead, it sets up the upgrade process, which nodes take turns controlling. For this reason, the command 
returns quickly. To view the progress of the upgrade, use the isi upgrade view command or the web administration 
interface.
4. You can specify the following parallel upgrade options:
Options
Description
Nodes to 
select for 
upgrade
Upgrade specific nodes with the --nodes <integer_range_list> option.
Specify the nodes in their upgrade order as a comma-separated list (for example, --nodes 7,3,2,5) or as 
a dash-separated range (for example, --nodes 1-7) of logical node numbers (LNNs).
NOTE: We recommend that you upgrade all the nodes. If you upgrade some nodes, a weekly alert is 
sent to confirm that the upgrade is making progress. Do not leave the cluster in a partially upgraded 
state for a prolonged period. Some new features in the upgrade might not be available until all the nodes 
in the cluster have been upgraded and the upgrade is committed. Refer to the release notes for the 
OneFS version that you are upgrading to for information about features that require all the nodes to be 
upgraded.
OneFS 9.2.0.0 and later ignores the node restart order. Instead, OneFS restarts any node that is ready, as long as only one 
node is restarting at a time.
The following example for OneFS 9.0.0.0 through OneFS 9.1.0.x starts a parallel upgrade on nodes 7,3,2,5, in that order:
isi upgrade cluster start --parallel <install-image-path> --nodes 7,3,2,5 
5. To add nodes to a current upgrade, run the following command, where <nodes> is the list of LNNs:
isi upgrade add-nodes <nodes>
6. To add any remaining nodes to the upgrade, run the following command:
isi upgrade add-remaining-nodes
After the upgrade, a number of upgrade-related jobs may continue to run on the cluster for some time. During this time, the 
cluster is accessible, but you might experience a decrease in cluster performance. After the jobs complete, performance will 
return to normal. At this stage, the upgrade is complete, but is not committed. You can still roll back to the previous version of 
OneFS. Some new features in the upgrade might not be available until the upgrade is committed.
Client connections during parallel upgrades
Parallel upgrades allow users to access data before, during, and after the upgrade. However, as groups of nodes are upgraded 
and restarted, users may experience brief pauses in the time it takes to complete a read or write operation.
If the cluster is configured for dynamic IP allocation, client connections to restarted nodes are automatically reconnected. If 
a client is reconnected to a node that has not yet been upgraded and restarted, the client might be required to reestablish a 
connection to the cluster more than once.
The following table describes the expected client behavior when a node is restarted on a cluster that is configured for dynamic 
IP allocation:
28
Performing the OneFS upgrade

---

## onefs-90-to-913-upgrade-guide::chunk_27

be required to reestablish a connection to the cluster more than once. The following table describes the expected client behavior when a node is restarted on a cluster that is configured for dynamic IP allocation: 28 Performing the OneFS upgrade

Table 5. Client Behaviors 
Client
Expected client behavior
SMB1
Client is in a data unavailable (DU) state for the duration of the upgrade if you are upgrading from a 
version prior to OneFS 9.6.
SMB2
Client transitions from the restarting node to a new node, but the client is disrupted.
NOTE: In OneFS 9.3.0.0 and later, client transitions from the restarting node to a new node 
without disruption.
SMB3
Client transitions from the restarting node to a new node without disruption.
NFSv2 and NFSv3
Client transitions from the restarting node to a new node without disruption.
NFSv4
Client transitions from the restarting node to a new node without disruption. Clients use NFSv4 
failover support.
NOTE: For more information about NFS settings, see article 457328, Best practices for NFS client settings.
Completing a simultaneous upgrade of OneFS
If you run a simultaneous upgrade, the OneFS cluster is upgraded simultaneously and then all of the nodes in the cluster are 
restarted simultaneously. During a simultaneous upgrade, the entire cluster is down and unavailable for client connections.
Perform a simultaneous upgrade using the web administration 
interface
You can use the web administration interface to upgrade the OneFS version that is running on a cluster.
1.
Log in to any node in the cluster through the web administration interface with the root account.
2. Click Cluster Management > Upgrade.
3. Click Upgrade OneFS.
4. Browse to the location of the installation image that you want to install. The file path must be accessible in an /ifs 
directory. Then click Select.
5. In the Upgrade Type list, select Simultaneous Upgrade.
6. (Optional) To skip the pre-upgrade checks for compatibility issues, select Skip optional pre-upgrade checks.
NOTE: It is recommended that you run the optional pre-upgrade checks. Before starting an upgrade, OneFS checks that 
your cluster is healthy enough to complete the upgrade process. Some of the pre-upgrade checks are mandatory, and 
will be performed even if you choose to skip the optional checks. All pre-upgrade checks contribute to a safer upgrade.
7.
Click Start Upgrade.
The cluster might display several confirmation messages. Confirm each message to continue the upgrade process.
After the upgrade, a number of upgrade-related jobs may continue to run on the cluster for some time. During this time, the 
cluster is accessible, but you might experience a decrease in cluster performance. After the jobs complete, performance will 
return to normal. At this stage, the upgrade is complete, but is not committed. You can still roll back to the previous version of 
OneFS. Some new features in the upgrade might not be available until the upgrade is committed.
Perform a simultaneous upgrade using the CLI
You can use the command-line interface to upgrade the version of OneFS that is running on the cluster.
1.
Open a secure shell (SSH) connection on the lowest-numbered node in the cluster and log in with the root account.
2. To perform a simultaneous upgrade, run the following command, where <install-image-path> is the file path of the upgrade 
install image. The file path must be accessible in an /ifs directory.
isi upgrade cluster start --simultaneous <install-image-path> 
Performing the OneFS upgrade
29

---

## onefs-90-to-913-upgrade-guide::chunk_28

perform a simultaneous upgrade, run the following command, where <install-image-path> is the file path of the upgrade install image. The file path must be accessible in an /ifs directory. isi upgrade cluster start --simultaneous <install-image-path> Performing the OneFS upgrade 29

NOTE: The isi upgrade cluster command runs asynchronously. The command does not run the entire upgrade 
process; instead, it sets up the upgrade process, which nodes take turns controlling. For this reason, the command 
returns quickly. To view the progress of the upgrade, use the isi upgrade view command or the web administration 
interface.
After the upgrade, a number of upgrade-related jobs may continue to run on the cluster for some time. During this time, the 
cluster is accessible, but you might experience a decrease in cluster performance. After the jobs complete, performance will 
return to normal. At this stage, the upgrade is complete, but is not committed. You can still roll back to the previous version of 
OneFS. Some new features in the upgrade might not be available until the upgrade is committed.
Adding a node to the cluster while an upgrade is in 
progress
In some circumstances, you might need to add a node to the cluster while an upgrade is in progress and before the upgrade has 
been committed.
To add a node during an upgrade, at least one node in the cluster must have been successfully upgraded to the target version 
of OneFS. When a new node is added to the cluster during an upgrade, the system images the new node with the previously 
committed version of OneFS. Then as the cluster upgrade continues, the new node is upgraded to the target version of OneFS. 
If the cluster upgrade is stopped and rolled back, all the nodes in the cluster are returned to the previously committed version of 
OneFS.
NOTE: Before adding new hardware to the cluster, first confirm that the hardware is compatible with the current version 
of OneFS that is installed and the target version of OneFS that you are upgrading to. See the OneFS Supportability and 
Compatibility Guide for more information.
Committing an upgrade of OneFS
You must commit an upgrade to complete the upgrade process. Once you commit the upgrade, you cannot roll back to the 
previous version of OneFS.
New features in the target version of OneFS are not available until the upgrade has been committed.
Commit an upgrade using the web interface
You can use the web interface to commit an upgrade of OneFS. Once you commit the upgrade, you cannot roll back to the 
previous version of OneFS.
1.
Log in to any node in the cluster through the web administration interface with the root account.
2. Click Cluster Management > Upgrade.
3. Click the Commit Upgrade to OneFS <version> button.
The cluster might display several confirmation messages. Confirm each message to continue the commit process.
Commit an upgrade using the CLI
You can use the command-line interface to commit an upgrade of OneFS. Once you commit the upgrade, you cannot roll back to 
the previous version of OneFS.
1.
Open a secure shell (SSH) connection on the lowest-numbered node in the cluster and log in with the root account.
2. To commit the upgrade, run the following command:
isi upgrade cluster commit
30
Performing the OneFS upgrade

---

## onefs-90-to-913-upgrade-guide::chunk_29

OneFS. 1. Open a secure shell (SSH) connection on the lowest-numbered node in the cluster and log in with the root account. 2. To commit the upgrade, run the following command: isi upgrade cluster commit 30 Performing the OneFS upgrade

Rolling back an upgrade of OneFS
The upgrade rollback feature allows you to stop the upgrade that is in progress and restore all the upgraded nodes to the 
previous committed version of OneFS.
NOTE: The rollback process must restart all the upgraded nodes simultaneously. This process temporarily disrupts cluster 
services and data availability.
Roll back an upgrade using the web interface
You can use the web administration interface to stop an upgrade and return to the previous committed version of OneFS.
NOTE: The rollback process must restart all the upgraded nodes simultaneously. This process temporarily disrupts cluster 
services and data availability.
1.
Log in to any node in the cluster through the web administration interface with the root account.
2. Click Cluster Management > Upgrade.
3. Click the Roll Back to OneFS <version> button. In OneFS 9.2.0.0 and later, click the Halt and roll back current upgrade 
button.
The cluster might display several confirmation messages. Confirm each message to continue the rollback process.
The cluster displays the rollback progress.
Roll back an upgrade using the CLI
Rolling back stops an upgrade and returns the cluster to the previous committed version of OneFS.
Command-Line Interface instructions:
NOTE: The rollback process must restart all the upgraded nodes simultaneously. This process temporarily disrupts cluster 
services and data availability.
1.
Open a secure shell (SSH) connection on the lowest-numbered node in the cluster and log in with the root account.
2. To roll back the upgrade, run the following command:
isi upgrade cluster rollback 
Verify the OneFS installation using the CLI
After you install OneFS, verify that the installation was successful.
1.
Confirm that the health of all the nodes in the cluster is OK by running the following command:
isi stat
2. Remove the installation files from the /ifs/data directory by running the following command where 
<installation_file_name> is the name of the installation file:
rm /ifs/data/<installation_file_name>
3. Collect information about the cluster in OneFS 9.0.0.0 and earlier, by running the following command:
isi_gather_info
Collect information about the cluster in OneFS 9.1.0.0 and later, by running the following command:
isi diagnostics gather start
Performing the OneFS upgrade
31

---

## onefs-90-to-913-upgrade-guide::chunk_30

Collect information about the cluster in OneFS 9.0.0.0 and earlier, by running the following command: isi_gather_info Collect information about the cluster in OneFS 9.1.0.0 and later, by running the following command: isi diagnostics gather start Performing the OneFS upgrade 31

Completing post-upgrade tasks
Topics:
•
Post-upgrade process - Overview
•
Allow the Upgrade job to run
•
Verify operational status using the CLI
•
Re-establish user privileges
•
Check client connections, and test the workflow
•
Verify Kerberos migration
•
Reapply custom settings
•
Test custom scripts
•
Install the latest roll-up patch
•
Verify Maintenance Mode
•
Verify Dell Technologies connectivity services
Post-upgrade process - Overview
After an upgrade, you should perform restoration and change management tasks to ensure that your cluster performs and 
behaves as expected. It is recommended that you build time into your upgrade plan to re-establish custom settings and 
privileges, and re-enable connections and features. You should also make time to modify settings for new and changed features.
Post-upgrade - Summary
The following is a summary of steps to perform during the post-upgrade phase:
1.
Allow upgrade jobs to run.
2. Verify operational status.
3. Re-establish user privileges.
4. Restore client connections and workflows.
5. Verify Kerberos migration.
6. Restore custom settings.
7.
Test custom scripts.
8. (Optional) Install the latest patch.
9. Verify Maintenance Mode.
Allow the Upgrade job to run
After an upgrade, an important job titled Upgrade that upgrades on-disk data structures, might continue to run for a while. The 
Upgrade job must be allowed to run to completion.
Although the cluster remains accessible while the Upgrade job is running, the job might temporarily decrease the cluster's 
performance.
NOTE: For more information about the Upgrade job, see KB Article 194551.
5
32
Completing post-upgrade tasks

---

## onefs-90-to-913-upgrade-guide::chunk_31

to run to completion. Although the cluster remains accessible while the Upgrade job is running, the job might temporarily decrease the cluster's performance. NOTE: For more information about the Upgrade job, see KB Article 194551. 5 32 Completing post-upgrade tasks

Verify operational status using the CLI
You can run a series of CLI commands as root to help verify that the PowerScale cluster is working correctly after an upgrade.
If you find an unresolvable issue, contact Dell Technologies Support.
1.
Check the new version number of the cluster:
isi_for_array -s uname -a
2. View the status of the cluster and ensure all the nodes are operational:
isi status
3. Check the devices in the nodes to validate the status of the drives:
isi_for_array -s "isi devices list"
4. Check the status of jobs and resume any paused jobs:
isi job status
isi job jobs resume <jobID>
5. Review the list of events, and address any critical events:
isi event groups list --sort=severity
6. To verify network connectivity and SmartConnect functionality, ping all internal and external interfaces on the cluster.
7.
Run the isi network pool status command for business critical pools.
isi network pool status <pool_id>
8. Verify the network interfaces:
isi network interfaces list --verbose
9. Verify the subnets:
isi network subnets list --verbose
10. Verify the pools:
isi network pools list --verbose
11. To check for issues, review the log files on the cluster:
isi_upgrade_logs
cat /var/log/messages
12. Check the input and output:
isi statistics system
Completing post-upgrade tasks
33

---

## onefs-90-to-913-upgrade-guide::chunk_32

subnets list --verbose 10. Verify the pools: isi network pools list --verbose 11. To check for issues, review the log files on the cluster: isi_upgrade_logs cat /var/log/messages 12. Check the input and output: isi statistics system Completing post-upgrade tasks 33

13. Check the global SMB settings:
isi smb settings global view
14. Check the status of the node firmware to ensure it is consistent across nodes:
For OneFS 9.0.0 and later:
 isi_upgrade_logs --get-fw-report
For OneFS 8.2.2 and earlier:
isi upgrade firmware devices
15. Ensure that all the licenses carried over and remain up to date:
isi license licenses list
16. Check the status of the authentication providers to ensure that they remain active:
isi auth status --verbose
17. Review the list of SyncIQ jobs:
isi sync jobs list
18. Check the SyncIQ job reports:
isi sync reports list
19. Review the list of the scheduled snapshots:
isi snapshot schedules list
20. If you use Dell Technologies connectivity services, confirm that the service is still enabled. To verify Dell Technologies 
connectivity services is enabled and the connection status is connected, run the following command:
isi connectivity settings view
Re-establish user privileges
After you upgrade, re-establish user privileges and roles. You can log in to the cluster through SSH as root or though an 
administrator account if that role has been assigned to any users.
NOTE: If the system administered the user roles through RBAC before the upgrade, any custom roles that existed are still 
in place. However, if the privileges assigned to built-in roles have changed in the new version, the users who are assigned to 
those built-in roles have those new privileges.
See the OneFS CLI Administration Guide or the OneFS Web Administration Guide for more information.
Check client connections, and test the workflow
NOTE: If you are using NDMP backups on your cluster, re-enable the NDMP service and test that it is working correctly.
1.
After the OneFS upgrade, check client connections and confirm that all users, clients, and applications can access the 
cluster.
2. Test your workflows to ensure that they function correctly.
34
Completing post-upgrade tasks

---

## onefs-90-to-913-upgrade-guide::chunk_33

test that it is working correctly. 1. After the OneFS upgrade, check client connections and confirm that all users, clients, and applications can access the cluster. 2. Test your workflows to ensure that they function correctly. 34 Completing post-upgrade tasks

Verify Kerberos migration
If you are using Kerberos authentication, you must verify that the Kerberos providers and settings have been migrated 
successfully.
Verify Kerberos migration using the web administration interface
Verify that Kerberos authentication providers and settings are correct:
1.
Click Access > Authentication Providers > Kerberos Provider.
2. In the Kerberos Realms, Kerberos Domains, and Kerberos Providers tables, verify that the Kerberos providers are 
correct.
3. In the Kerberos Settings area, verify that the Kerberos authentication settings are correct.
Verify Kerberos migration using the CLI
Verify that Kerberos authentication providers, and settings are correctly represented in the output of each of these commands:
●
isi auth krb5 realm list
●
isi auth krb5 domain list
●
isi auth krb5 spn list
●
isi auth settings krb5 view
Reapply custom settings
Some custom settings might not have been preserved during the upgrade. Reapply the custom settings that you backed up and 
recorded when you performed the pre-upgrade tasks.
The custom settings include:
●
SMB audit logging
●
Passwords for local user accounts
●
Changes to system controls
●
Aspera
●
Cron jobs
●
Certificates
●
Static routes
Test custom scripts
Test any custom scripts that you have implemented to confirm they continue to work. If command syntax changes were made in 
the target version of OneFS, some custom scripts might not work as intended.
NOTE: It is recommended to ensure that your custom scripts work on a test cluster before implementing them on a 
production system.
Install the latest roll-up patch
Install the latest patch for the target version of OneFS to which you upgraded.
Confirm if your version of OneFS requires a patch. Most OneFS images already include the latest patch. For more information, 
check the OneFS image download, or contact Dell Technologies technical support.
1.
See PowerScale OneFS Current Patches to view a list of patches that are available for your version of OneFS.
2. Download and install the latest roll-up patch using the instructions found in the README.txt file included with the patch 
download.
Completing post-upgrade tasks
35

---

## onefs-90-to-913-upgrade-guide::chunk_34

Patches to view a list of patches that are available for your version of OneFS. 2. Download and install the latest roll-up patch using the instructions found in the README.txt file included with the patch download. Completing post-upgrade tasks 35

Verify Maintenance Mode
If Maintenance Mode is enabled to automatically detect maintenance tasks, your maintenance window ends when the upgrade is 
completed.
If a maintenance window was manually configured, end your maintenance window to allow cluster event alerts to continue.
See the OneFS Web Administration Guide or the OneFS CLI Administration Guide for information about ending a maintenance 
window.
Verify Dell Technologies connectivity services
After the upgrade, verify that Dell Technologies connectivity services for remote support are working correctly.
Using the OneFS web interface, go to the Cluster Management > General Settings window, and click the Connectivity 
Services tab. To ensure that remote support for use with Dell Technologies connectivity services is enabled, click the Enable 
Remote support toggle. To enable automatic support case creation, click the Enable Dell Technologies connectivity 
services toggle.
See the OneFS Web Administration Guide for information about Dell Technologies connectivity services.
36
Completing post-upgrade tasks

Troubleshooting your upgrade
Topics:
•
Troubleshooting an upgrade
Troubleshooting an upgrade
If you experience problems with your upgrade, try the following:
●
Check the upgrade logs and review for errors.
●
Search for OneFS upgrade information within the knowledge base on the PowerScale support site.
●
Contact your Dell Technologies Support representative.
6
Troubleshooting your upgrade
37