## smartquotas-management::chunk_0

White Paper 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Abstract 
This white paper describes how EMC Isilon SmartQuotas 
software helps enterprises drive down storage costs with a 
simple to use, highly scaleable and flexible storage quota and 
provisioning application for scale-out storage environments.  
 
April 2012 
 
 
 
 
 
 
 
 
 
STORAGE QUOTA MANAGEMENT AND 
PROVISIONING WITH EMC ISILON SMARTQUOTAS

2
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
 
 
 
 
 
Copyright © 2012 EMC Corporation. All Rights Reserved. 
 
EMC believes the information in this publication is accurate as 
of its publication date. The information is subject to change 
without notice. 
 
The information in this publication is provided “as is.” EMC 
Corporation makes no representations or warranties of any kind 
with respect to the information in this publication, and 
specifically disclaims implied warranties of merchantability or 
fitness for a particular purpose. 
 
Use, copying, and distribution of any EMC software described in 
this publication requires an applicable software license. 
 
For the most up-to-date listing of EMC product names, see EMC 
Corporation Trademarks on EMC.com. 
 
VMware is a registered trademark or trademark of VMware, Inc. 
in the United States and/or other jurisdictions. All other 
trademarks used herein are the property of their respective 
owners. 
 
Part Number h10575

---

## smartquotas-management::chunk_1

product names, see EMC Corporation Trademarks on EMC.com. VMware is a registered trademark or trademark of VMware, Inc. in the United States and/or other jurisdictions. All other trademarks used herein are the property of their respective owners. Part Number h10575

3
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
Table of Contents 
Introduction .................................................................................. 4	  
Overview of SmartQuotas ................................................................ 4	  
Accounting Quotas ............................................................................................................ 4	  
Enforcement Quotas .......................................................................................................... 5	  
How does SmartQuotas Accounting work? ......................................... 5	  
Domains ............................................................................................................................ 5	  
Default Domains and Linked Quotas: ............................................................................. 6	  
Accounting ........................................................................................................................ 6	  
QuotaScan Job ................................................................................................................... 8	  
SmartQuotas Enforcement ............................................................... 9	  
Enforcement Types & States .............................................................................................. 9	  
Exceptions to enforcement ................................................................................................ 9	  
Quota Notification ........................................................................ 10	  
Notification settings ........................................................................................................ 10	  
Notification conditions .................................................................................................... 10	  
Notification Actions ......................................................................................................... 11	  
How does Notification work? ............................................................................................ 11	  
System Alerts .................................................................................................................. 12	  
Quota Reports ............................................................................. 12	  
Quota report format ......................................................................................................... 12	  
Quota Report Management .............................................................................................. 13	  
Use Cases for SmartQuotas ........................................................... 13	  
Summary ..................................................................................... 14

---

## smartquotas-management::chunk_2

conditions .................................................................................................... 10 Notification Actions ......................................................................................................... 11 How does Notification work? ............................................................................................ 11 System Alerts .................................................................................................................. 12 Quota Reports ............................................................................. 12 Quota report format ......................................................................................................... 12 Quota Report Management .............................................................................................. 13 Use Cases for SmartQuotas ........................................................... 13 Summary ..................................................................................... 14

4
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
Introduction 
File-based data continues to grow at a remarkable rate—nearly doubling each year—
making the need for optimized data storage and its management more important 
than ever.  
To help enterprises maximize the long-term value of their critical business data and 
drive down storage management cost and complexity, EMC Isilon offers SmartQuotas:  
a simple, scalable and flexible quota management and provisioning software 
application that integrates with the EMC Isilon OneFS® operating system.   
SmartQuotas allows administrators to control and limit storage usage across 
their organization and provision a single pool of Isilon clustered storage to best meet 
their unique storage challenges. SmartQuotas also provides Thin Provisioning to 
present more storage capacity to applications and users than is physically present. 
SmartQuotas requires a separate license to be used on a cluster node. 
This paper examines how SmartQuotas can be applied by storage administrators to 
establish storage usage quotas and how these quotas can be enforced. The paper 
also describes notification and reporting options available to streamline management 
of scale-out NAS storage environments. 
Overview of SmartQuotas 
A quota by definition is the permissible share or proportional part of a total. Applied 
to storage requirements, it is the amount of storage capacity that is permissible to a 
certain entity within the Isilon cluster. At its core, a quota system is a combination of 
accounting, enforcement and reporting. Accounting refers to keeping counts of 
blocks, inodes, and files owned by resource entities like users, groups and 
directories. Enforcement refers to setting and forcing limits for certain counts and 
Reporting refers to the mechanism by which such enforcement can be conveyed to 
the administrators or users.  
To apply SmartQuotas, two types of capacity quotas need to be considered: 
Accounting Quotas and Enforcement Quotas: 
Accounting Quotas 
Accounting quotas monitor but do not limit disk storage utilization, are useful for 
auditing, planning, or billing purposes. For example, with SmartQuotas accounting 
quotas, you can: 
• Track the amount of disk space used by various users or groups to bill each entity 
for only the disk space used. 
• Review and analyze reports that help you identify storage usage patterns. In turn, 
these can used to define storage policies for the organization and educate end 
users of the file system about using storage more efficiently. 
• Intelligently plan for capacity expansions and future storage needs.

---

## smartquotas-management::chunk_3

you identify storage usage patterns. In turn, these can used to define storage policies for the organization and educate end users of the file system about using storage more efficiently. • Intelligently plan for capacity expansions and future storage needs.

5
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
Enforcement Quotas 
There are four levels of enforcement quotas: hard, soft, advisory or none. Each of 
these are described in Table 1. 
Enforcement	  
Level 
Description 
Hard 
A limit that cannot be exceeded. If an operation, such as a file write, causes a 
quota target to exceed a hard quota, the operation fails, an alert is logged to the 
cluster, and a notification is issued to any specified recipients. 
Soft 
A limit that can be exceeded until a grace period has expired. When a soft quota 
is exceeded, an alert is logged to the cluster and a notification is issued to any 
specified recipients; however, data writes are permitted during the grace period. 
If the soft threshold is still exceeded when the grace period expires, data writes 
fail, and a hard-limit notification is issued to any specified recipients. 
Advisory 
An informational limit that can be exceeded. When an advisory quota threshold is 
exceeded, an alert is logged to the cluster and a notification is issued to any 
specified recipients. Reaching an advisory quota threshold does not prevent data 
writes. 
None 
No enforcement; It is an accounting only quota 
Table 1: Quota Enforcement Levels 
How does SmartQuotas Accounting work? 
Domains  
SmartQuotas works on the basis of domains, which is the cornerstone of the quota 
accounting. A domain is a set of resources and an accounting of each resource type 
for that set. SmartQuotas use the concept of a domain to represent all traditional 
quota types, but also gives the Administrator, ways to express complex domains in a 
straightforward manner.  A simple domain defined as “identity@directory” could be 
the set of files under “directory”, owned by “identity”, which could be a user or group. 
The files accounted include all files reachable from the given path without following 
soft links. “identity” can be ALL (and /ifs is an effective ALL for directory). 
SmartQuotas can be applied to a variety of entities as shown in Table 2. 
Entity/Resource Type 
Description 
Directory 
A specific directory and all its subdirectories. 
User 
A specific user.  
Group 
All members of a specific group.  
Table 2: Entity and Resource Types

---

## smartquotas-management::chunk_4

be applied to a variety of entities as shown in Table 2. Entity/Resource Type Description Directory A specific directory and all its subdirectories. User A specific user. Group All members of a specific group. Table 2: Entity and Resource Types

6
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
With SmartQuotas it is possible to form more traditional domain types fairly quickly 
by using ALL. The following are examples of domain types: 
• All files belonging to user John: user:John@/ifs 
• All files under /ifs/cs, belonging to any user: ALL@/ifs/cs. 
• All files under /ifs/cs that belong to user John: user:John@/ifs/cs 
Domains cannot be formed on anything but directories. More specifically, domains 
are associated with directories, not directory paths. If the domain is 
ALL@/ifs/cs/data, but /ifs/cs/data gets renamed to /ifs/cs/files, the domain stays 
with the directory.  
Domains can be nested and may overlap. For example: 
• A hard quota is set on /ifs/data/finance for 5TB 
• 1 TB soft quotas are then placed on individual users in the finance department 
• This ensures that the finance directory as a whole never exceeds 5TB while 
limiting the users in the finance department to 1TB each. 
Default Domains and Linked Quotas: 
A default domain is a domain that does not account for any specific set of files, but 
instead specifies policy for new domains that match a specific trigger. In short, 
default domains are templates for actual domains. SmartQuotas use the identity 
notation default-user and default-group to describe domains with default user and 
group policies. The domain default-user@/ifs/cs becomes specific-user@/ifs/cs for 
each specific-user that is not otherwise defined. All enforcements on default-user are 
copied to specific-user when specific-user allocates within the domain, and the new 
inherited domain quota is termed as a Linked Quota. There may be overlapping 
defaults (i.e. default-user@/ifs and default-user@/ifs/cs may both be defined). 
If enforcements on defaults change, SmartQuotas will propagate the changes to the 
Linked Quota domains asynchronously with some lag before updates take effect. If a 
default domain is deleted, SmartQuotas will delete all children marked as inherited. 
As an option, an administrator may delete the default without deleting the children, 
but this will break inheritance on all inherited children.  
Accounting 
Domains account for physical space and logical space resources:  
• Physical Space - All space used to store files and directories. This includes both 
data and metadata, but only those pieces within the domain in question. This 
space does not account for sparse regions. For example, only the data portions of 
a file will be accounted, snapshots of files and directories will not be accounted. 
• Logical Space - The sum of all file sizes. This does not include file metadata and 
sparse regions..

---

## smartquotas-management::chunk_5

For example, only the data portions of a file will be accounted, snapshots of files and directories will not be accounted. • Logical Space - The sum of all file sizes. This does not include file metadata and sparse regions..

7
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
Logical space is meant to account for space occupied by user data, and not for the 
overhead of keeping that space safe. The impetus for logical space is that normal file 
systems have traditionally provided quota systems that are physical, but, because 
they lack the same protection mechanisms, the typical accounting is fairly close to 
the user data plus some metadata overhead. However, typical quota systems still 
charge accounts for things like the metatree. Because SmartQuotas offer both logical 
and physical, it goes a step further with logical space and is used to account only the 
logical space, the data within files. SmartQuotas cannot, however, be used to charge 
for user data alone. This would open up cases where an adversarial user could hide 
away data in strange places. For example, if directory entries were not accounted for 
in some fashion, data could be hidden in directories using zero length files. To avoid 
this, SmartQuotas charges for certain metadata attributes, as defined in Table 3. 
Data Type 
Accounting 
Regular file data 
Every non-sparse 8k region of the file 
Directories 
Sum of all directory entries 
Symlinks 
Data Size 
ACL and similar 
Data Size 
ADS 
Each ADS is charged as a file and a container as a directory 
Table 3: Data accounting for different entity types 
Here are some additional interesting cases during Quota accounting: 
Hard Links - Each logical inode  is accounted exactly once in every domain to which 
it belongs. If an inodeis present in multiple domains, it is accounted in multiple 
domains. Alternatives such as shared accounting were considered. However, if 
inodes are not accounted once in every domain, it is possible for the deletion of a 
hard link in one domain to put another domain over quota. 
Alternate Data Stream (ADS)	  -­‐	  A file with ADS is accounted as the sum of the 
resource usage of the individual file, the usage for the container directory, and the 
usage for each ADS. SmartQuotas handles the rename of a file with ADS 
synchronously despite the fact that the ADS container is just a directory. SmartQuotas 
will store an accounting summary on the ADS container to handle renames.  
Directory Rename – A directory rename presents a unique challenge to a per-
directory quota system.  Renames of directories within a domain are trivial - if both 
the source and target directories have the same domain membership, no accounting 
changes. However, non-empty directories are not permitted to be moved when the 
SmartQuotas configuration is different on the source and the target parent 
directories. If a user trusts the client operating systems to copy files and preserve all 
the necessary attributes, then the user may set dir_rename_errno to EXDEV,  which 
causes most Unix and Windows clients to do a copy and delete of the directory tree to 
effect the move.

---

## smartquotas-management::chunk_6

operating systems to copy files and preserve all the necessary attributes, then the user may set dir_rename_errno to EXDEV, which causes most Unix and Windows clients to do a copy and delete of the directory tree to effect the move.

8
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
Snapshot Accounting – Quota Domains can include snapshot usage in its 
accounting. SmartQuotas will only support snapshots created after the quota domain 
was created. This is because determining quota governance (including QuotaScan 
job) for existing snapshots is a very time and resource consuming operation. As most 
administrators cycle their snapshots through timed expirations, this means that 
SmartQuotas will eventually accrue enough accounting information to include the 
entire set of relevant snapshots on the system. 
QuotaScan Job 
The QuotaScan is the cluster maintenance process responsible for scanning the 
cluster to performing accounting activities to bring the desired governance to each 
inode. In essence it is a distributed tree walk that is performed based on the state of 
the domain. 
A domain may be in one of three accounting states: 
• Ready - A domain in the ready state is fully accounted. SmartQuotas displays 
“ready” domains in all interfaces, and all enforcements apply to such domains.  
• Accounting - Any time a domain's accounting must be updated by a QuotaScan, 
the domain is placed in the Accounting state. SmartQuotas displays accounting 
domains in all interfaces, including usage data, but indicate they are in the 
process of being “Accounted”. SmartQuotas applies all enforcements to 
accounting domains, even when it might reject an allocation that would have 
proceeded if it had completed the QuotaScan.  
• Deleting - Domain removal may be a lengthy process. After a request to delete a 
domain, SmartQuotas will place the domain in the deleting state until tear-down 
is complete. SmartQuotas hide domains in the deleting state from all interfaces, 
and the top-level directory of a domain may be deleted while the domain is still in 
the deleting state (assuming there are no domains in “Ready” or “Accounting” 
state defined on the directory). No enforcements are applied for domains in 
“Deleting” state. 
A Quotascan is performed when the domain is in an Accounting State. This can 
occur during quota creation to account the new domain if a quotas has been set for 
the domain and quota deletion to un-account the domain. A QuotaScan is required 
when creating a quota on a non-empty directory.  If quotas are created up-front on an 
empty directory, no QuotaScan is necessary. 
In addition, a QuotaScan job may be started from the command line (using the “isi 
job” command). Any path specified on the command line is treated as the root of a 
tree that should be processed. This is provided primarily as a means to re-scan a 
directory or maintenance reasons.

---

## smartquotas-management::chunk_7

command line (using the “isi job” command). Any path specified on the command line is treated as the root of a tree that should be processed. This is provided primarily as a means to re-scan a directory or maintenance reasons.

9
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
SmartQuotas Enforcement 
Now that accounting is relatively well defined, quotas are simply a matter of 
enforcement on accounting. Note that since all domains account for every resource 
type, a domain may be created for accounting only, with no enforcement. 
Enforcement Types & States 
Advisory - When an advisory threshold is reached, a notification condition is met. 
Notification rules are described in the next section. Advisory thresholds are 
parameterized by threshold value. There can only be one advisory threshold per 
domain.  
• Soft - When a soft threshold is reached, a notification is sent as in the case of 
advisory thresholds. In addition, if the usage stays over the soft threshold past a 
specified grace period, the soft threshold becomes a hard threshold. If the usage 
goes below the soft threshold, the timer for the grace period is reset. Soft 
thresholds are parameterized by threshold value and grace period. There can only 
be one soft threshold per domain. The grace period cannot be infinite, nor can it 
be zero. For those cases, advisory and hard thresholds are available, respectively. 
• Hard - When a hard threshold is reached, a notification is sent as for advisory and 
soft thresholds. In addition, all further allocations within the domain fail. Hard 
thresholds are parameterized by threshold value. There can only be one hard 
threshold per domain. 
SmartQuotas defines the following enforcement states: 
• U (Under) - If the usage is less than the enforcement threshold, the enforcement is 
in state U. 
• O (Over) - If the usage is greater than the enforcement threshold, the enforcement 
is in state O. 
• E (Expired) - If the usage is greater than the soft threshold, and the usage has 
remained over the enforcement threshold past the grace period expiration, the 
soft threshold is in state E. If an administrator modifies the soft threshold but not 
the grace period, and the usage still exceeds the threshold, the enforcement is in 
state E. 
Exceptions to enforcement 
There are a few exceptions to enforcement of Quotas including the following 
scenarios: 
• If a domain has an accounting only quota, enforcements for the domain are not 
applied. 
• Any administrator action may push a domain over quota. Examples include 
changing protection, taking a snapshot, removing a snapshot, etc. The 
administrator may write into any domain without obeying enforcements.

---

## smartquotas-management::chunk_8

only quota, enforcements for the domain are not applied. • Any administrator action may push a domain over quota. Examples include changing protection, taking a snapshot, removing a snapshot, etc. The administrator may write into any domain without obeying enforcements.

10 
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
• Any system action may push a domain over quota, including repair etc. OneFS 
maintenance processes are as powerful as the administrator. 
Quota Notification 
A crucial part of the quota system is to provide user notifications regarding 
enforcement violations, both when a violation event occurs and while violation state 
persist on a scheduled basis. An enforcement may have several notification rules 
associated with it. Each notification rule specifies a condition and an action to be 
executed when the condition is met. Notification rules are considered part of 
enforcements. Clearing an enforcement also clears any notification rules associated 
with it.  
Notification settings 
Enforcement quotas support the notification settings described in Table 4. Note that 
any given quota can use only one of these settings. 
Notification 
Setting 
Description 
Global default 
Uses the global default notification for the specified type of quota. 
None 
Disables all notifications for the quota. 
Custom – Basic 
Enables administrators to create basic custom notifications that will apply 
to a specific quota. Basic notifications can be configured for any or all of 
the threshold types (hard, soft, or advisory) for the specified quota. 
Custom - 
Advanced 
Enables the creation of advanced custom notifications that will apply to a 
specific quota. Advanced notifications can be configured for any or all of 
the threshold types (hard, soft, or advisory) for the specified quota. 
Table 4: Notification Settings 
Notification conditions 
A notification condition is an event that can trigger an action specified in a 
notification rule. A rule may specify a schedule (e.g. “every day at 1:00 AM") for 
executing an action or immediate notification of certain classes of state transitions. 
Examples of notification conditions include: 
• Quota exceeded (when enforcement states is “O” – Over) 
• Grace period specified for a Soft Advisory limit has expired. 
• Write Access denied when attempting to write to file after quota has exceeded the 
limit.

---

## smartquotas-management::chunk_9

notification conditions include: • Quota exceeded (when enforcement states is “O” – Over) • Grace period specified for a Soft Advisory limit has expired. • Write Access denied when attempting to write to file after quota has exceeded the limit.

11 
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
Notification Actions 
Each notification rule is allowed to execute one or none of each of the Notification 
Actions shown in Table 5. 
Notification Action 
Description 
Alert 
Send an alert for one of the actions described in the next section 
Email Manual Address 
Email to a specific address 
Email Owner 
Email owner mapping based on identity source  
Table 5: Notification Actions 
The email owner mapping is as follows: 
• Active Directory: Lookup is performed against the domain controller (DC).  If the 
user does not have an email setting, a configurable transformation from user 
name and DC fully qualified domain name is performed to generate an email 
address . 
• LDAP: LDAP user email resolution is similar to AD users. In this case, only the 
email attribute looked up in the LDAP server is configurable by an administrator 
based on the LDAP schema for the user account information. 
• NIS: Only the configured email transformation for the NIS fully qualified domain 
name is used.  
• Local users: Only the configured email transformation is used.  
How does Notification work? 
The Quota notification is handled by a notification daemon which performs the 
following functions: 
• Process Kernel notification events that get sent out. They are matched to 
notification rules to generate instant notifications (or other actions as specified in 
the notification rule) 
• Process notification schedules – The daemon will check notification rules on a 
scheduled basis. These rules specify what violation condition should trigger a 
notification on a regular scheduled basis. 
• Execute notifications based on rule configuration to generate emails or alert 
notifications 
• Manage persistent notification states by recording the state persistently so that in 
the event of a restart, outstanding events that have yet to be notified, are 
handled. 
• Process rescan requests by responding to kernel requests for Quota Rescan (when 
quotas are created or modified)

---

## smartquotas-management::chunk_10

recording the state persistently so that in the event of a restart, outstanding events that have yet to be notified, are handled. • Process rescan requests by responding to kernel requests for Quota Rescan (when quotas are created or modified)

12 
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
System Alerts 
Various system alerts are sent out to the standard cluster Alerting system when 
specific events occur. These are described in Table 6. 
Name 
Level 
Event Description 
NotifyFailed 
Warning 
An attempt to process a notification rule failed 
externally, such as an undeliverable e-mail. 
NotifyConfig 
Warning 
An attempt to process a notification rule failed due 
to configuration, such as nonexistent user, or 
missing e-mail address. 
ThresholdViolation 
Info 
A quota threshold was exceeded. The conditions 
under which this alert is triggered are defined by 
notification rules.  
DomainError 
Error 
An invariant was violated that resulted in a forced 
domain rescan.  
Table 6: System Alerts 
Quota Reports 
SmartQuotas software supports flexible reporting options that enable administrators 
to more effectively manage cluster resources and analyze usage statistics. The goal of 
Quota Reporting is to provide a summarized view of the past or present state of the 
Quota Domains. There are three methods of data collection and reporting that are 
supported:  
• Scheduled reports are generated and saved on a regular interval.  
• Ad-hoc reports are generated and saved per request of the user.  
• Live reports are generated for immediate and temporary viewing.  
The CLI export functionality makes use of the same data generation and storage 
format as quota reporting, but should not require any extra requirements beyond the 
three types of reports. After the collection of the raw reporting data, data summaries 
can be produced given a set of filtering parameters and sorting type.   
Reports can be viewed from historical sampled data or a live system. In either case, 
the reports are views of usage data at a given time. SmartQuotas does not provide 
reports on aggregated data over time (i.e. trending reports). However, the raw data 
can be used by a Quota Administrator to answer trending questions. 
Quota report format 
The storage format needs to handle consistency within domains and usability outside 
the context of a changing filesystem. The quota report format is a serialization of the 
quota configuration. A quota report is a time-stamped XML file that starts off with 
global configuration settings and global notification rules:

---

## smartquotas-management::chunk_11

domains and usability outside the context of a changing filesystem. The quota report format is a serialization of the quota configuration. A quota report is a time-stamped XML file that starts off with global configuration settings and global notification rules:

13 
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
<quota-report time="1161852536"> 
<global-config>INSERT QUOTA GLOBAL CONFIG</global-config> 
<domains> 
... 
</domains> 
</quota-report> 
When listing domains, a few special considerations are made to handle LIN-to-path 
mapping, UID/GID-to-name mapping, notification rules and inherited domains. Both 
inode/path as well as ID/name  are stored with each domain. The path and name are 
resolved at the time of writing the domain to the report. This mitigates problems that 
arise from changes to the mappings during or after domain iteration. Quota 
Notification Rules are read and inserted into a domain entry only if the domain is not 
inherited. This method mitigates changes to Quota Notification Rules by accessing 
each rule set only once as well as limiting performance impacts of reading the Quota 
Notification Rules with each and every domain. 
Quota Report Management 
Report management needs to provide proper locking during report generation, atomic 
publishing of a completed reports and deletion of old reports. This is to ensure that 
the report is generated as an unambiguous point-in-time report of the quota/data 
usage.  Scheduled and ad-hoc reports both maintain a set of completed reports that 
are rotated out as new reports become available. A set is parameterized by path, 
filename prefix and retained count. The temporal ordering is determined through a 
timestamp in the filenames. A single lock file per set is used to serialize access. 
Though only addition to the set needs to be serialized, creation of reports is serialized 
under the same lock to simplify the process. 
The following are the steps followed given a path of /ifs/reports, filename prefix of 
schedule_quota_report and a retention count of 3: 
1. Acquire a lock on /ifs/reports/.scheduled_quota_report.lock 
2. Open /ifs/reports/.scheduled_quota_report.tmp truncated 
3. Execute the API function to generate the quota report on (quota_report_generate) 
on the temporary file 
4. Close the temporary file and record the time 
5. Move the temporary file to /ifs/reports/scheduled_quota_report_<timestamp>.xml 
6. Perform pruning to keep to the retention count of 3 
7. Release lock 
Use Cases for SmartQuotas 
Use Case 1: Quota management - A university wants to give their students and 
groups a fixed amount of storage to control and keep storage growth in check

---

## smartquotas-management::chunk_12

the retention count of 3 7. Release lock Use Cases for SmartQuotas Use Case 1: Quota management - A university wants to give their students and groups a fixed amount of storage to control and keep storage growth in check

14 
Storage Quota Management and Provisioning with EMC Isilon SmartQuotas
§ The storage administrator wants to know how much each student is 
consuming & limit them 
§ Set default user hard or soft quotas 
§ Email alerts to students to encourage self-cleanup of file usage  
• Use Case 2: Thin Provision and Scale-Out – A company in the Media and 
Entertainment industry wants to overprovision storage and only add capacity 
when needed.   
§ The company buys a 20TB cluster and gives 100 users 500GB each ~ 
effectively thin provisioned 50TB’s 
§ Set directory quotas for each user with hard quota of 500GB each 
§ Set up system alert to the storage admin to add capacity (nodes) when the 
20TB is 3/4 full 
§ Scale-out effectively by adding additional capacity only when needed. 
Summary 
Traditional systems with volume quotas are limited to a single storage device— and to 
a single volume. Volume-level solutions are limited in management flexibility once 
they are initially set up. For example, typical implementations require the 
management of quotas across different volumes, multiple storage systems and 
multiple file systems. This approach creates challenges when making changes to 
resources, tracking specific users and groups, moving directory structures or moving 
data between file systems and volumes. As more storage silos are added, the 
complexity only increases.  
With EMC Isilon SmartQuotas, these management challenges are eliminated. 
Because SmartQuotas is fully cluster-aware and spans across all nodes, regardless of 
the cluster size, IT managers can administer quotas from a single point of view, 
provision storage exactly how they want, and change quota policy options on 
demand. 
Administrators can define named quotas for specific individual users or groups, or 
create default quotas that control disk usage for anyone accessing the cluster. 
Administrators can manage storage across their enterprise so that specific users and 
groups are only allowed to “see” the storage they have been provisioned. Hard, soft 
and advisory limits can be set across the organization for specific users and groups, 
and across the various directory structures.  
Administrators can also configure alerts and send e-mail notifications to end-users 
letting them know that quota limits are approaching, enforcing hard stops on writes 
or providing a grace period of several days before enforcing thresholds. When new 
users need to be added or directory structures need to be changed, SmartQuotas 
allows IT managers to change their quota policies on the fly—easily meeting the 
changing storage demands of the enterprise.