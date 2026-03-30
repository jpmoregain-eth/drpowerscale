## isilon-network-design::chunk_0

Isilon Network Design Considerations
Aqib Kazi
Isilon Technical Marketing
September 11, 2019

© Copyright 2017 Dell Inc.
2
Introduction
This document provides design considerations for understanding, configuring, and troubleshooting 
Isilon Scale-Out NAS external networking. In a Scale-Out NAS environment, the overall network 
architecture must be configured to maximize the user experience. Many factors contribute to overall 
network performance. This document examines network architecture design and best practices 
including factors such as Latency, Flow Control, ICMP, MTU, jumbo frames, congestion, TCP/IP 
parameters, and IPv6.
Note: This technical deck is based on and is a supplement to the Isilon Network Design 
Considerations paper, but is a more graphical representation. For all of the details, please read 
through the paper, available at: 
https://www.dellemc.com/resources/en-us/asset/white-papers/products/storage/h16463-isilon-
advanced-networking-fundamentals.pdf

---

## isilon-network-design::chunk_1

and IPv6. Note: This technical deck is based on and is a supplement to the Isilon Network Design Considerations paper, but is a more graphical representation. For all of the details, please read through the paper, available at: https://www.dellemc.com/resources/en-us/asset/white-papers/products/storage/h16463-isilon- advanced-networking-fundamentals.pdf

© Copyright 2017 Dell Inc.
3
Notice to Readers
Test! Test! Test! Confirm! Implement.
It is important to understand that the best practices stated in this document are based on general network 
design and are provided as guidance to Isilon administrators. Each network is unique, not only from a 
design perspective but also from a requirements and workloads perspective. Before making any changes 
based on the guidance in this document, it is important to discuss modifications with the Network 
Engineering team. Additionally, as a customary requirement for any major IT implementation, changes 
should first be tested in a lab environment that closely mimics the workloads of the live network.
Measure performance and 
collect metrics on current 
production network
Configure lab 
emulating 
production network
Test network 
updates in lab 
environment
Collect lab 
performance 
metrics
Implement 
production network 
updates with 
limited scope
Confirm impacts of 
limited scope 
updates
Update production 
network with 
expanded scope

© Copyright 2017 Dell Inc.
4
Contents
•
Network Architecture Design
•
Latency, Bandwidth & Throughput
–
Bandwidth Delay Product
–
Isilon Network Stack Tuning
•
Ethernet Flow Control
•
Ethernet, MTU & IP Overhead
–
Jumbo Packets
–
IP Packet Overhead
•
Access Zones
•
IPv6
–
IPv6 Security, Efficiency, and Quality of Service
–
IPv6 Addresses
–
OneFS IPv6 Configuration
•
Network Troubleshooting
–
Netstat
–
InsightIQ
–
DNS

Network Architecture 
Design

---

## isilon-network-design::chunk_2

Overhead – Jumbo Packets – IP Packet Overhead • Access Zones • IPv6 – IPv6 Security, Efficiency, and Quality of Service – IPv6 Addresses – OneFS IPv6 Configuration • Network Troubleshooting – Netstat – InsightIQ – DNS Network Architecture Design

© Copyright 2017 Dell Inc.
6
Avoid Single Points of Failure
•
Network design requires layers of redundancy
•
Eliminate dependence on a single link or device
•
Implement load sharing for multiple paths
•
Always assume links and hardware will fail
•
In the image shown, if the router, a single switch, or 
node fail, access will not be available.

© Copyright 2017 Dell Inc.
7
Data Flow of Application and Protocol Traffic
Understanding the application data flow from clients to the Isilon cluster across the network is 
important for network design. This allows for resources to be allocated to minimize latency and hops 
along this flow.

© Copyright 2017 Dell Inc.
8
Available Bandwidth
As traffic traverses the different layers of the network, the available bandwidth should not be 
significantly different. Compare this available bandwidth with the workflow requirements and ensure 
bandwidth is consistent between links.

© Copyright 2017 Dell Inc.
9
Minimizing Latency
Ensuring latency is minimal from the client endpoints to the Isilon nodes maximizes performance and 
efficiency. Several steps can be taken to minimize latency, but latency should be considered 
throughout network design.

© Copyright 2017 Dell Inc.
10
Prune VLANs
•
Limit VLAN propagation to applicable areas
•
Trunking all VLANs is not a best practice
•
Unneeded VLANs impose strain on endpoints and switches
•
Broadcasts are propagated across the VLAN and impact clients

---

## isilon-network-design::chunk_3

Dell Inc. 10 Prune VLANs • Limit VLAN propagation to applicable areas • Trunking all VLANs is not a best practice • Unneeded VLANs impose strain on endpoints and switches • Broadcasts are propagated across the VLAN and impact clients

© Copyright 2017 Dell Inc.
11
VLAN Hopping
Switch spoofing:
•
Hosts imitate the behavior of a trunking switch, allowing access to other VLANs
Double Tagging:
•
Packets contain two VLAN tags rather than one, with the correct VLAN tag as empty and the 
second as the VLAN where access is not permitted
–
Recommendation: Assign the native VLAN to an ID that is not in use or tag the native VLAN. Only allow 
trunk ports between trusted devices and assign access VLANs on ports that are different from the default 
VLAN.

© Copyright 2017 Dell Inc.
12
Triangle Looped Topology
Most widely implemented architecture in enterprise data centers
•
Extends VLANs between the aggregation switches
•
Spanning Tree is implemented, using Rapid PVST+ or MST. 
•
For each path, a redundant path also exists, which is 
blocking until the primary path is not available. 
•
Access layer uplinks load balance VLANs. 
•
Utilization of the inter-switch link between the Distribution 
switches must be monitored closely as this is used to reach 
active services.
•
The Looped Triangle Access Topology supports VLAN 
extension and L2 adjacency across the Access layer. 
Multiple Access Switches interface with the external 
network of the Isilon Scale-Out NAS environment.

---

## isilon-network-design::chunk_4

monitored closely as this is used to reach active services. • The Looped Triangle Access Topology supports VLAN extension and L2 adjacency across the Access layer. Multiple Access Switches interface with the external network of the Isilon Scale-Out NAS environment.

© Copyright 2017 Dell Inc.
13
Link Aggregation
It should not be thought of as mandatory, it is based on workload requirements
Link Aggregation  ≠Higher Bandwidth Link
•
Applying link aggregation to multiply bandwidth by the number of interfaces for a single session is incorrect
•
A single session is limited to a single interface ensuring packets are delivered in order and without duplication
•
Aggregate bandwidth increases when carrying multiple simultaneous sessions in an active/active configuration and may not 
provide a linear multiple of each link’s data rate, as each individual session utilizes a single link.

© Copyright 2017 Dell Inc.
14
Link Aggregation 
Advantages
•
Higher aggregate bandwidth for multiple 
sessions. A single session is confined to a 
single link.
•
Link resiliency
•
Ease of management with a single IP 
address
•
Load balancing
Link Aggregation 
Limitations
•
Provides resiliency for interface and cabling 
failures, but not for switch failures.
•
Bandwidth for a single session is not 
improved as a single link is used for each 
session.
•
Depending on the workload, each protocol 
has varying limitations and advantages of 
Link Aggregation

© Copyright 2017 Dell Inc.
15
Protocols and Link Aggregation
Protocols impact the benefits on link aggregation
•
Stateful protocols, such as NFSv4 and SMBv2 
benefit from link aggregation as a failover 
mechanism. 
•
SMBv3 Multichannel automatically detects multiple 
links, utilizing each for maximum throughput and 
link resilience.

---

## isilon-network-design::chunk_5

Link Aggregation Protocols impact the benefits on link aggregation • Stateful protocols, such as NFSv4 and SMBv2 benefit from link aggregation as a failover mechanism. • SMBv3 Multichannel automatically detects multiple links, utilizing each for maximum throughput and link resilience.

© Copyright 2017 Dell Inc.
16
Multi-Chassis Link Aggregation (MCLAG)
IEEE 802.1AX standard doesn't define Link Aggregation between multiple switches and a host
•
Switch vendors provide MCLAG through proprietary features. 
•
Multiple switches connect via an Inter-Switch link or other proprietary cable and communicate via 
a proprietary protocol forming a virtual switch. Each vendor has a proprietary implementation of 
Multi-Chassis Link Aggregation, but externally the virtual switch created is compliant with the IEEE 
802.1AX standard.
•
The virtual switch is perceived as a single switch to an Isilon node, with links terminating on a 
single switch. 
MCLAG provides network redundancy in the event of a single chassis (switch) failing

Latency, Bandwidth & 
Throughput

© Copyright 2017 Dell Inc.
18
Latency
Latency in a packet-switched network is defined as the time from when a source endpoint sends a 
packet to when it is received by the destination endpoint. 
Round trip latency, sometimes referred to as round trip delay, is the amount of time for a packet to be 
sent from the source endpoint, to the destination endpoint, and returned from the destination to the 
source endpoint.
Minimizing latency is a key component of network design. Minimal latency between clients and an 
Isilon node ensures performance is not impacted.

© Copyright 2017 Dell Inc.
19
Latency – Hops 
Minimizing hops required between endpoints decreases latency and not only applies at the physical 
level with the number of switches between the endpoints but also applies logically to network 
protocols and algorithms

---

## isilon-network-design::chunk_6

Copyright 2017 Dell Inc. 19 Latency – Hops Minimizing hops required between endpoints decreases latency and not only applies at the physical level with the number of switches between the endpoints but also applies logically to network protocols and algorithms

© Copyright 2017 Dell Inc.
20
Latency – ASICs 
Consider the ASICs within a switch. If a packet enters through one ASIC and exits through the other, 
latency could increase. If at all possible, it is recommended to keep traffic as part of the same ASIC 
to minimize latency.
Contact the switch vendor to confirm which ports belong to each ASIC

© Copyright 2017 Dell Inc.
21
Latency – Routing
Example Ingress Policies
Example Egress Policies
IP Traffic Export
Output ACL Check
Input ACL
DoS Tracker
Input QoS Marking
Output QoS Marking
NAT Outside-Inside
Output Policing
IPsec Decryption
IPsec Encryption
Policy Routing
Policy Accounting
Ingress Netflow
Egress NetFlow
Unicast RPF Check
NAT Inside-Outside
Packets that pass through a router may induce additional latency. Packets are checked for a match 
against defined rules, in some cases requiring packet header modification.

© Copyright 2017 Dell Inc.
22
Latency – MTU Mismatch
Depending on the MTU size configuration of each hop between two endpoints, an MTU mismatch 
may exist. Therefore, packets must be split to conform to upstream links, creating additional CPU 
overhead on routers and NICs, creating higher processing times, and leading to additional latency.

© Copyright 2017 Dell Inc.
23
Latency – Firewalls 
•
Firewalls provide protection by filtering through packets against set rules, consuming time and 
could create further latency. 
•
Processing times are heavily dependent upon the number of rules in place. 
•
Recommended to ensure outdated rules are removed to minimize processing times.

---

## isilon-network-design::chunk_7

protection by filtering through packets against set rules, consuming time and could create further latency. • Processing times are heavily dependent upon the number of rules in place. • Recommended to ensure outdated rules are removed to minimize processing times.

© Copyright 2017 Dell Inc.
24
Bandwidth & Throughput
•
Bandwidth is the theoretical maximum speed a specific medium can deliver if all factors are 
perfect without any form of interference. 
•
Throughput is the actual speed realized in a real-world scenario, given interference and other 
environmental factors such as configuration, contention, and congestion.
Ensure bandwidth is available throughout the network hierarchy, eliminating bottlenecks and ensuring 
consistent bandwidth. The bandwidth from the Access Switches to the Isilon nodes should be a ratio 
of what is available back to the distribution and core switches. 
For example, if an Isilon cluster of 4 nodes has all 40 GbE connectivity to access switches, the link 
from the core to distribution to access should be able to handle the throughput from the access 
switches. Ideally, the link from the core to distribution to access should support roughly a bandwidth 
of 160 Gb (4 nodes * 40 GbE).

© Copyright 2017 Dell Inc.
25
Bandwidth Delay Product (BDP)
BDP = Bandwidth * Round Trip Delay
The amount of data which can be transmitted on a network link at a given time
•
For example, a link with a bandwidth of 1 Gigabit per second and a 1 millisecond round trip time, 
would be calculated as: 
–
Bandwidth * RTT = 1 Gigabit per second * 1 millisecond =
–
1,000,000,000 bits per second * 0.001 seconds = 1,000,000 bits = 0.125 MB
•
0.125 MB may be sent per TCP message

---

## isilon-network-design::chunk_8

would be calculated as: – Bandwidth * RTT = 1 Gigabit per second * 1 millisecond = – 1,000,000,000 bits per second * 0.001 seconds = 1,000,000 bits = 0.125 MB • 0.125 MB may be sent per TCP message

© Copyright 2017 Dell Inc.
26
Isilon Network Stack Tuning
Note: All Isilon clusters do not require TCP stack tuning by default. 
•
Adapting the TCP stack to bandwidth, latency, and MTU requires tuning to ensure the cluster provides optimal 
throughput.
•
Ensures on inbound, the full BDP is accepted, and on outbound, it must be retained for a possible retransmission. 
Prior to modifying the TCP stack, it is important to measure the current I/O performance and then again after 
implementing changes.
•
The spreadsheet below provides the necessary TCP stack changes based on the bandwidth, latency, and MTU. 
The changes below must be implemented in the order below and all together on all nodes. Modifying only some 
variables could lead to unknown results. After making changes, it is important to measure performance again. For 
access to the spreadsheet, please contact the appropriate Isilon sales representative or contact Isilon support.

© Copyright 2017 Dell Inc.
27
Ethernet Flow Control
IEEEs 802.3x standard defines an Ethernet Flow Control mechanism at the data link layer
•
Isilon OneFS listens for pause frames but does not send them, meaning it is only applicable when an Isilon node is 
the source. OneFS recognizes pause frames from the destination.
•
For Flow Control to be successfully implemented, it must be configured throughout the network hops that the 
source and destination endpoints communicate through. Otherwise, the pause flow control frames will not be 
recognized and will be dropped.
Note: If destination clears its buffers sooner than the specified wait time 
earlier, it could send a new pause frame with a ‘zero’ specified as the wait 
time, notifying the source to restart transmission.

---

## isilon-network-design::chunk_9

be recognized and will be dropped. Note: If destination clears its buffers sooner than the specified wait time earlier, it could send a new pause frame with a ‘zero’ specified as the wait time, notifying the source to restart transmission.

© Copyright 2017 Dell Inc.
28
Is Flow Control Needed?
Check if pause frames are being sent to OneFS
If the network or cluster performance does not seem optimal, it is easy to check for pause frames on 
an Isilon cluster. To check for pause frames received by an Isilon cluster, execute the following 
command from the shell: isi_for_array -a <cluster name> sysctl dev | grep pause 
Check for any values greater than zero – The cluster below has not received any pause frames 
For more information on 
managing pause frames, 
refer to Dell EMC 
Knowledge Base Article 
000454131.

Ethernet, MTU & IP 
Overhead

© Copyright 2017 Dell Inc.
30
Maximum Transmission Unit (MTU)
MTU is the largest packet size permitted by a link – IEEE 802.3 specifies limit as 1500 bytes
•
TCP uses MTU to determine the 
maximum size of a packet per 
transmission
•
Large MTU sizes provide less 
overhead as packet headers and 
acknowledgments are not 
consuming space and bandwidth 
•
Generally, the MTU across the 
internet is 1500 bytes

---

## isilon-network-design::chunk_10

uses MTU to determine the maximum size of a packet per transmission • Large MTU sizes provide less overhead as packet headers and acknowledgments are not consuming space and bandwidth • Generally, the MTU across the internet is 1500 bytes

© Copyright 2017 Dell Inc.
31
ICMP & MTU With Isilon
Internet Control Message Protocol (ICMP) gathers communications related information. ICMP is capable of 
sending error messages but also delivers operational information. ‘Ping’ and ‘TraceRoute’ both send ICMP 
messages to provide connectivity information including latency and network hops.
Isilon OneFS determines MTU size specific to each transaction with the following steps:
1.
Initial TCP handshake
2.
Isilon node sends an ICMP message for Path MTU Discovery (PMTUD), RFC 1191, gathering the 
maximum supported MTU size. 
3.
If for any reason ICMP is disabled, or PMTUD is not supported, this causes OneFS to default the MTU 
size to 536 bytes, which typically leads to a performance degradation. 
Note: The MTU size can be manually updated through a sysctl command.

---

## isilon-network-design::chunk_11

any reason ICMP is disabled, or PMTUD is not supported, this causes OneFS to default the MTU size to 536 bytes, which typically leads to a performance degradation. Note: The MTU size can be manually updated through a sysctl command.

© Copyright 2017 Dell Inc.
32
Checking MTU Sizes
Use Ping to Confirm the maximum MTU to an endpoint
•
It is recommended to start with the largest MTU and work down to 
find the limit.
•
For example, to check if an MTU size of 8900 bytes is transmitted 
to an endpoint, from the OneFS CLI, use the following command: 
ping –s 8900 –D <IP Address>. The ‘-s’ specifies the packet 
size and the ‘-D’ specifies the not to fragment the packet.
•
If the ping is successful, the MTU size is transmitted across. If the 
ping is unsuccessful, gradually lower the MTU size until it is 
successfully transmitted. Confirm the MTU size can be transmitted 
from both endpoints.
•
OneFS is based on FreeBSD. FreeBSD also has options for 
gradually increasing the MTU size by performing a ‘sweeping ping’ 
using the –g option. For more information on ping options in 
FreeBSD, access the FreeBSD manual at the following link: 
https://www.freebsd.org/cgi/man.cgi?ping(8)

© Copyright 2017 Dell Inc.
33
Ethernet Packet
Ethernet frame carries a payload of data and is carried by an Ethernet packet.
Packet structure on the wire is vital to understanding packet overhead and the other components 
required to send a payload.

---

## isilon-network-design::chunk_12

2017 Dell Inc. 33 Ethernet Packet Ethernet frame carries a payload of data and is carried by an Ethernet packet. Packet structure on the wire is vital to understanding packet overhead and the other components required to send a payload.

© Copyright 2017 Dell Inc.
34
Ethernet Packet Fields
•
Interpacket Gap: Serves as a gap between each frame, similar to a spacer. The Interpacket gap is only part of 
Layer 1. The field originates from a time when hubs were common, and collisions were more commonplace.
•
Preamble: Composed of alternating 1 and 0 bits for receiver clock synchronization. The Preamble is only part of 
Layer 1.
•
Start Frame Delimiter: Identifies the start of an Ethernet frame.
•
Destination MAC: Contains the MAC address of the destination station for which the data is intended.
•
Source MAC: Contains the MAC address of the sending station.
•
VLAN 802.1Q: Optional field utilized if a VLAN is identified.
•
Type: Also known as the EtherType field, this defines the type of protocol that is encapsulated in the payload. In 
the example above, it is an Ethernet II Frame, the most widely accepted type.
•
Payload: Spans from 46 to 1500 bytes and contains user data. If it is smaller than 46 bytes, blank values are 
entered to bring this up to 46 bytes as it is the minimum value. The Payload consists of protocol data for TCP, 
UDP or RTP and IPv4 or IPv6. The next section explains the Payload field in greater depth.
•
CRC: Cyclic Redundancy Check is part of the Frame Check Sequence (FCS) to detect errors within the frame. The 
CRC code should result in a zero if the data does not contain any errors.

---

## isilon-network-design::chunk_13

Payload field in greater depth. • CRC: Cyclic Redundancy Check is part of the Frame Check Sequence (FCS) to detect errors within the frame. The CRC code should result in a zero if the data does not contain any errors.

© Copyright 2017 Dell Inc.
35
Ethernet Payload
Combination of either TCP, UDP, or RTP header with an IPv4 or IPv6 header and actual payload
The amount of actual data sent within an Ethernet Frame is dependent upon the number of bytes 
consumed by the other fields. Other options are available which are not listed here. The most 
common is Linux hosts automatically adding a timestamp to the TCP stack which adds another 12 
bytes.

© Copyright 2017 Dell Inc.
36
Jumbo Frames
Ethernet frames with an MTU greater than 1500 bytes and up to 9000 bytes
•
Larger MTU size provides greater efficiency as less overhead and fewer acknowledgments are 
required, reducing interrupt load on endpoints
•
Must be enabled end-to-end on all hops between endpoints. Otherwise, the MTU could be lowered 
through PMTUD or packets could be fragmented. The fragmentation and reassembly impacts the 
CPU performance of each hop, which impacts the overall latency.
•
Jumbo frames utilize the same Ethernet packet structure but the size of the data within the 
payload is greater

© Copyright 2017 Dell Inc.
37
IP Packet Overhead
Standard and Jumbo packets have the same overhead, making the ratio of data sent greater with Jumbo
Jumbo frames are recommended to maximize throughput on Isilon node’s front-end 10 and 40 GbE
interfaces
Every payload sent to Layer 1 on the wire, requires the following fields:
•
Every payload requires an additional 38 bytes to be sent, irrespective of the payload size

© Copyright 2017 Dell Inc.
38
IP Packet Overhead – Example 1
Standard 1500 Byte Payload – IPv4/TCP
Standard 1500 byte packet with IPv4 and TCP headers equals a data to Ethernet frame percentage 
of: 
(Data Bytes) / (Total Ethernet Frame Bytes) = 
(1500 – 40) / (1500 + 38) = 1460/1538 = .949 => 94.9%

---

## isilon-network-design::chunk_14

– IPv4/TCP Standard 1500 byte packet with IPv4 and TCP headers equals a data to Ethernet frame percentage of: (Data Bytes) / (Total Ethernet Frame Bytes) = (1500 – 40) / (1500 + 38) = 1460/1538 = .949 => 94.9%

© Copyright 2017 Dell Inc.
39
IP Packet Overhead – Example 2
Jumbo 9000 Byte Payload – IPv4/TCP
Jumbo 9000 byte packet with IPv4 and TCP headers equals a data to Ethernet frame percentage of: 
(Data Bytes) / (Total Ethernet Frame Bytes) = 
(9000 – 40) / (9000 + 38) = 8960/9038 = .991 => 99.1%

© Copyright 2017 Dell Inc.
42
Data Payload to Ethernet Frame Efficiency
Examples of the amount of data sent for standard and jumbo frames
Jumbo frames deliver between 98%-99% efficiency depending on the packet type. The efficiencies 
are only maximized when all hops from the client endpoint to an Isilon node support jumbo frames. 
Otherwise, packets may be fragmented leading to additional processing overhead on devices or 
PMTUD finding the lowest MTU along the path.
Note: NFS v2 is UDP. 
NFS v3 and v4 are 
TCP. SMB is TCP.

SmartConnect 
Considerations

© Copyright 2017 Dell Inc.
44
SmartConnect Considerations
DNS delegation server for SmartConnect zones, load-balancing connections to the cluster. 
•
[Blue Arrow – Step 1] The client makes a DNS request for sc-zone.domain.com by sending a 
DNS request packet to the site DNS server.
•
[Green Arrow – Step 2] The site DNS server has a delegation record for sc-zone.domain.com 
and sends a DNS request to the defined nameserver address in the delegation record, the 
SmartConnect service (SmartConnect Service IP Address).
•
[Orange Arrow – Step 3] The cluster node hosting the SmartConnect Service IP (SSIP) for this 
zone receives the request, calculates the IP address to assign based on the configured connection 
policy for the pool in question (such as round robin), and sends a DNS response packet to the site 
DNS server.
•
[Red Arrow – Step 4] The site DNS server sends the response back to the client.

---

## isilon-network-design::chunk_15

configured connection policy for the pool in question (such as round robin), and sends a DNS response packet to the site DNS server. • [Red Arrow – Step 4] The site DNS server sends the response back to the client.

© Copyright 2017 Dell Inc.
45
SmartConnect Network Hierarcy
Pre OneFS 8.2
•
For releases prior to OneFS 8.2, consider that a single SSIP is defined per subnet. However, 
under each subnet, pools are defined, and each pool will have a unique SmartConnect Zone 
Name. It is important to recognize that multiple pools lead to multiple SmartConnect Zones 
utilizing a single SSIP. As shown in the diagram above, a DNS provider is defined per Groupnet, 
which is a feature in OneFS 8.0 and newer releases. In releases before 8.0, a DNS per Groupnet
was not supported.

© Copyright 2017 Dell Inc.
46
SmartConnect Load Balancing
•
The most common load balancing policies are Round Robin and Connection Count, but this may 
not apply to all workloads.  
•
It is important to understand whether the front-end connections are being evenly distributed, 
either in count or by bandwidth. Front-end connection distribution may be monitored with 
InsightIQ or the webUI. 
•
Generally speaking, starting with Round Robin is recommended for a new implementation or if 
the workload is not clearly defined. As the workload is further defined and based on the Round 
Robin experience, another policy can be tested in a lab environment.
Load 
Balancing 
Policy 
Workload 
General 
or Other 
Few Clients with 
Extensive Usage 
Many Persistent NFS 
& SMB Connections 
Many Transitory 
Connections 
(HTTP, FTP) 
NFS Automounts 
or UNC Paths 
Round Robin 
 
 
 
 
 
Connection 
Count* 
 
 
 
 
 
CPU Utilization* 
 
 
 
 
 
Network 
Throughput*

---

## isilon-network-design::chunk_16

or Other Few Clients with Extensive Usage Many Persistent NFS & SMB Connections Many Transitory Connections (HTTP, FTP) NFS Automounts or UNC Paths Round Robin      Connection Count*     CPU Utilization* Network Throughput*

© Copyright 2017 Dell Inc.
47
Static Allocation
•
The Static Allocation Method assigns a single 
persistent IP address to each interface 
selected in the pool, leaving additional IP 
addresses in the pool unassigned if the 
number of IP addresses is greater than 
interfaces. 
•
In the event a node or interface becomes 
unavailable, this IP address does not move to 
another node or interface.
•
When the node or interface becomes 
unavailable, it is removed from the 
SmartConnect Zone, and new connections 
will not be assigned to the node. 
•
The Dynamic Allocation Method splits all 
available IP addresses in the pool across all 
selected interfaces. OneFS attempts to 
assign the IP addresses evenly if at all 
possible, but if the interface to IP address 
ratio is not an integer value, a single interface 
may have more IP addresses than another.
Dynamic Allocation

---

## isilon-network-design::chunk_17

all selected interfaces. OneFS attempts to assign the IP addresses evenly if at all possible, but if the interface to IP address ratio is not an integer value, a single interface may have more IP addresses than another. Dynamic Allocation

© Copyright 2017 Dell Inc.
48
Dynamic Failover
Dynamic Failover provides high-availability by transparently migrating IP addresses to another node 
when an interface is not available. If a node becomes unavailable, all of the IP addresses it was 
hosting are re-allocated across the new set of available nodes in accordance with the configured 
failover load balancing policy. The default IP address failover policy is round-robin, which evenly 
distributes IP addresses from the unavailable node across available nodes. As the IP address 
remains consistent, irrespective of which node it resides on, this results in a transparent failover to 
the client, providing seamless high availability.
The other available IP address failover policies are the same as the initial client connection balancing 
policies, i.e., connection count, throughput, or CPU usage. In most scenarios, round-robin is not only 
the best option, but also the most common. However, the other failover policies are available for 
specific workflows. As mentioned previously, with the initial load balancing policy, test the IP failover 
policies in a lab environment to find the best option for a specific workflow.

Dynamic Failover 
Example

---

## isilon-network-design::chunk_18

However, the other failover policies are available for specific workflows. As mentioned previously, with the initial load balancing policy, test the IP failover policies in a lab environment to find the best option for a specific workflow. Dynamic Failover Example

© Copyright 2017 Dell Inc.
50
Dynamic zone with 3 IP addresses per node – 1/2
•
Dynamic SmartConnect zones require a greater number of IP addresses than the number of 
nodes at a minimum to handle failover behavior. In the example below, the formula used to 
calculate the number of IP addresses required is N*(N-1), where ‘N’ is the number of nodes. The 
formula is used for illustration purposes only to demonstrate how IP addresses, and in turn clients, 
move from one node to another, and how this could potentially lead to an imbalance across nodes. 
Every workflow and cluster is unique, and this formula is not applicable to every scenario.
•
This example considers the same four node cluster as the previous example, but now following 
the rule of N*(N-1). In this case 4*(4-1) = 12, equaling three IPs per node, as shown in the figure 
below.

© Copyright 2017 Dell Inc.
51
Dynamic zone with 3 IP addresses per node – 2/2
When a node or interface failure occurs, the three IP addresses are spread over all the other nodes in 
that SmartConnect zone. This failover results in each remaining node having 200 clients and four IP 
addresses. Although performance may degrade to a certain degree, it may not be as drastic as the 
failure in the first scenario, and the experience is consistent for all users, as shown in the following 
figure.

---

## isilon-network-design::chunk_19

clients and four IP addresses. Although performance may degrade to a certain degree, it may not be as drastic as the failure in the first scenario, and the experience is consistent for all users, as shown in the following figure.

© Copyright 2017 Dell Inc.
52
Suggested Protocol and Zone Types
Protocol 
Protocol Category 
Suggested Zone Type 
NFSv2 (not supported in 
OneFS 7.2 and above) 
Stateless 
Dynamic 
NFSv3 
Stateless 
Dynamic 
NFSv4 
Stateful 
Dynamic or Static – Depending on mountd daemon 
and OneFS version. Refer to the NFS section above. 
SMBv1 
Stateful 
Dynamic or Static – Refer to SMB section above 
SMBv2 / SMBv2.1 
Stateful 
SMBv3 Multi-Channel 
Stateful 
FTP 
Stateful 
Static 
SFTP / SSH 
Stateful 
Static 
HDFS 
Stateful – Protocol is 
tolerant of failures 
Refer to EMC Isilon Best Practices Guide for Hadoop 
Data Storage 
HTTP / HTTPS 
Stateless 
Static 
SyncIQ 
Stateful 
Static Required 
 
For additional details for each protocol, refer to the Network Design Considerations white paper

OneFS 8.2 :
SmartConnect Multi-SSIP

© Copyright 2017 Dell Inc.
54
SmartConnect Multi-SSIP
Providing SSIP Failover and Fault Tolerance
• Dependence on a single SSIP caused issues during node maintenance, reboots, 
or interface issues. The issues are further magnified considering the lowest 
available NodeID is usually the node that is rebooted first or is scheduled for 
maintenance first.
• Multi-SSIP provides fault tolerance and a failover mechanism, ensuring the 
SmartConnect service continues to load balance clients according to the selected 
policy. 
• How many SSIPs? Depends on the license
SmartConnect License
Basic
Advanced
SSIPs per subnet
2
6

---

## isilon-network-design::chunk_20

• Multi-SSIP provides fault tolerance and a failover mechanism, ensuring the SmartConnect service continues to load balance clients according to the selected policy. • How many SSIPs? Depends on the license SmartConnect License Basic Advanced SSIPs per subnet 2 6

© Copyright 2017 Dell Inc.
55
SmartConnect Multi-SSIP
• At ‘Step 2’ the site DNS server sends a DNS request to the to the SSIP and awaits 
a response in the ‘Step 3’ for a node’s IP address based on the client connection 
policy. 
• If the response in ‘Step 3’ is not received in 30 seconds the connection times out. 
The DNS server tries the next SSIP and awaits a response in ‘Step 3’.

© Copyright 2017 Dell Inc.
56
SmartConnect Network Hierarchy
OneFS 8.2 introduces support for multiple SSIPs per subnet

© Copyright 2017 Dell Inc.
57
Multi-SSIP is not a load balancer
SSIPs are Active-Passive
• SmartConnect Multi-SSIP is not an additional layer of load balancing for client 
connections. 
• Additional SSIPs provide redundancy and reduce failure points in the client 
connection sequence.
• Although the additional SSIPs are in place for failover, the SSIPs configured are 
active and respond to DNS server requests. 
• The Multi-SSIP configuration is Active-Passive, each node hosting an SSIP is 
independent and ready to respond to DNS server requests
• SmartConnect continues to function correctly if the DNS server contacted SSIPs in 
a round-robin sequence

© Copyright 2017 Dell Inc.
58
Multi-SSIP
Node 1
Node 2
Node 3
Node 4
SSIP 1
Node 5
Node 6
Node 7
Node 8
SSIP 2
Multi-SSIP
Load Balancing Policy – Round Robin
1st Request
Node 1
2nd Request
Node 2
3rd Request
Node 3
4th Request
Node 1
Configure DNS with SSIPs 
as DNS A record failover IPs

---

## isilon-network-design::chunk_21

6 Node 7 Node 8 SSIP 2 Multi-SSIP Load Balancing Policy – Round Robin 1st Request Node 1 2nd Request Node 2 3rd Request Node 3 4th Request Node 1 Configure DNS with SSIPs as DNS A record failover IPs

© Copyright 2017 Dell Inc.
59
Configuring Multi-SSIP
Add a new subnet or edit a subnet
--sc-service-addrs option with an 
IP address range
isi network subnets modify 
subnet --help | grep sc-
service-addrs
--add-sc-service-addrs 
<ip_address_range> | --
remove-sc-service-addrs
--clear-sc-service-addrs
--remove-sc-service-addrs
User Interface
CLI

© Copyright 2017 Dell Inc.
60
Multi-SSIP Node Assignment
No longer a dependence on the lowest Node DevID
• SSIP Resource File introduced – First set of nodes to create a lock host the SSIP
To confirm which of the nodes are hosting SSIPs, use the following commands:
• isi_for_array ifconfig | grep <SSIP>
• isi_for_array ifconfig | grep “zone 0”  - Provides where all of the SSIPs are

Access Zones

© Copyright 2017 Dell Inc.
62
Access Zone Hierarchy
SCzoneName
AccessZone
/ifs/root_based_path/data
Subnet
SSIP
SCZoneName
Step 1
Step 2
Step 3

© Copyright 2017 Dell Inc.
63
What are they? Each Access Zone requires a root based path
Access Zone Root Based Path
•
What – Every Access Zone must have a root based path – Recommended to use cluster name, a 
numerical AZ number, and a directory
•
AZ1 - /ifs/clustername/az1/<data dirs>*
•
AZ2 - /ifs/clustername/az2/<data dirs>
•
Why
•
Data separation/ Multi-tenancy story
•
Best Practice: 
•
Don’t use system zone
•
Don’t use the root of the zone – Always create a subdirectory under the access zone
•
No overlap of root based paths

© Copyright 2017 Dell Inc.
64
Importance of following root based path best practices
Root Based Path Best Practices
Makes failover and failback easy with Superna Eyeglass

IPv6

---

## isilon-network-design::chunk_22

subdirectory under the access zone • No overlap of root based paths © Copyright 2017 Dell Inc. 64 Importance of following root based path best practices Root Based Path Best Practices Makes failover and failback easy with Superna Eyeglass IPv6

© Copyright 2017 Dell Inc.
66
IPv6
Internet Protocol version 6 (IPv6) is the newest version and ultimately replaces IPv4
•
IPv6 uses 128-bit addresses supporting 340 undecillion addresses
•
Most regulatory agencies now mandate IPv6 or have set target dates for an IPv6 migration. 
•
Enterprises have requirements for IPv6 migration or have a plan to migrate gradually. 
•
IPv6 brings innovation and takes connectivity to a new level with enhanced user experiences. 
•
IPv6 should be recommended to all Isilon customers for several reasons, as the following slides 
explain
Total possible IPv4 addresses:
Total possible IPv6 addresses:

© Copyright 2017 Dell Inc.
67
IPv6 Security
IPv6 was built from the ground up with security as a tenet
•
IPv6 offers protection similar to a VPN, by supporting IPSEC directly. 
•
Current VPNs offer encryption and integrity checks, which are standard in IPv6 for all devices and 
connections, making the ‘man in the middle’ attacks much more challenging.
•
Using IPv4, a hacker can redirect traffic between two hosts, in some cases observing the traffic, 
but in others manipulating it. IPv6 makes this more challenging with a secure name resolution 
feature. The Secure Neighbor Discovery (SEND) protocol provides cryptographic confirmation of 
host identity, minimizing hostname based attacks like Address Resolution Protocol (ARP) 
poisoning, leading to devices placing more trust in connections.

---

## isilon-network-design::chunk_23

makes this more challenging with a secure name resolution feature. The Secure Neighbor Discovery (SEND) protocol provides cryptographic confirmation of host identity, minimizing hostname based attacks like Address Resolution Protocol (ARP) poisoning, leading to devices placing more trust in connections.

© Copyright 2017 Dell Inc.
68
IPv6 Efficiency
Overall data transmission is faster and simplified
•
IPv4’s limited address space led to the introduction of Network Address Translation (NAT). IPv6’s 
large address space means many devices no longer require NAT translation
•
IPv6 has a simpler packet header, minimizing time and resources for processing
•
IPv4 required a check for packet integrity – Eliminated in IPv6
IPv6 Multicast
IPv6 supports multicast rather than broadcast
•
Allows media streams to be sent to multiple destinations simultaneously leading to bandwidth 
savings. 
•
IPv4 required every host to process broadcast packets.

© Copyright 2017 Dell Inc.
69
IPv6 Quality of Service
QoS implementation is far simplified in IPv6 with a new packet header.
•
IPv6 header contains a new field, Flow Label, identifies packets belonging to the same flow. 
•
Flow Label associates packets from a specific host and head with a particular destination. 
•
Peer-to-peer applications benefit from the Flow Label as the QoS marking cannot be modified by 
intermediate hops and provides a higher degree of QoS.

© Copyright 2017 Dell Inc.
70
IPv6 Address
•
128 bits 
•
Series of eight segments – Separated by a colon
•
Segment is a 4-character hexadecimal number – Ranging from 0000 to FFFF – 16 bits each

© Copyright 2017 Dell Inc.
71
IPv6 Address (continued)
IPv6 addresses may be written without the leading zeroes:
Further, consecutive fields of zeros may be replaced with a double-colon:

---

## isilon-network-design::chunk_24

number – Ranging from 0000 to FFFF – 16 bits each © Copyright 2017 Dell Inc. 71 IPv6 Address (continued) IPv6 addresses may be written without the leading zeroes: Further, consecutive fields of zeros may be replaced with a double-colon:

© Copyright 2017 Dell Inc.
72
IPv6 Address Types
•
Unicast: one-to-one – Single Address to Single Interface
•
Anycast: one-to-nearest – Assigned to a group of interfaces, with packets being delivered only to a 
single (nearest) interface
•
Multicast: one-to-many – Assigned to a group of interfaces, and is typically delivered across 
multiple hosts.

© Copyright 2017 Dell Inc.
73
IPv6 Unicast Address Format
•
Global Routing Prefix: Network ID or prefix of the address for routing
•
Subnet ID: Similar to the netmask in IPv4 but is not part of the IP address in IPv6 
•
Interface ID: Unique identifier for a particular interface. For Ethernet networks, the Ethernet MAC 
address (48 bits) may be used for the Interface Identifier, by inserting 16 additional bits, forming 
what is referred to as an EUI-64 address

© Copyright 2017 Dell Inc.
74
IPv6 Header
IPv6 header is easier to process for all devices
Field 
Description 
Length 
Version 
Specifies if the packet is IPv4 or IPv6 
4 Bits 
Traffic Class 
Similar to an IPv4 Type of Service field and includes support for Differentiated Services Code Point 
(DSCP) providing congestion control. 
8 Bits 
Flow Label 
Provides the ability to track certain traffic flows at the network layer for QoS management. 
20 Bits 
Payload Length 
Similar to the IPv4 ‘Length’ field – Provides length of the data portion 
16 Bits 
Next Header 
Similar to the IPv4 ‘Protocol’ field – Provides what to expect after the basic header, including 
options for a TCP or UDP header 
8 Bits 
Hop Limit 
Similar to the IPv4 ‘Time to Live’ field – Provides the maximum number of hops 
8 Bits

---

## isilon-network-design::chunk_25

‘Protocol’ field – Provides what to expect after the basic header, including options for a TCP or UDP header 8 Bits Hop Limit Similar to the IPv4 ‘Time to Live’ field – Provides the maximum number of hops 8 Bits

© Copyright 2017 Dell Inc.
75
IPv6 to IPv4 Translation
•
Options available to facilitate IPv4 and IPv6 communication are dual-stack networks, tunneling, 
and translation
•
Translation technologies are the Network Address Translation IPv6 to IPv4 (NAT64) and Stateless 
IP/ICMP Translation (SIIT). NAT64 is similar to the IPv4 Network Address Translation but is 
specific to IPv6. SIIT is capable of replacing IPv4 and IPv6 as part of the translation.

© Copyright 2017 Dell Inc.
76
OneFS IPv6 Configuration
Implementing IPv6 on an Isilon cluster is a simple process 
as IPv6 and IPv4 are supported as a dual stack. In order 
to provision an IPv6 subnet with Isilon, follow these steps:
1.
From the “Cluster Management” drop-down, select 
“Network Configuration”
2.
Edit an existing ‘groupnet’ or create a new one
3.
Enter DNS servers and add subnet
4.
Create ‘Subnet’ by selecting IPv6 in the IP Family
5.
Create network address pool and assign interfaces

Network Troubleshooting

---

## isilon-network-design::chunk_26

select “Network Configuration” 2. Edit an existing ‘groupnet’ or create a new one 3. Enter DNS servers and add subnet 4. Create ‘Subnet’ by selecting IPv6 in the IP Family 5. Create network address pool and assign interfaces Network Troubleshooting

© Copyright 2017 Dell Inc.
78
Netstat
Network status by each connection or socket
•
Proto: Protocol of the active connection. The protocol is 
TCP or UDP and the ‘4’ or ‘6’ associated specifies if its 
IPv4 or IPv6.
•
Recv-Q and Send-Q: Value of the receiving and sending 
queue in bytes. Non-zero values specify the number of 
bytes in the queue that are awaiting to be processed. The 
preferred value is zero. If several connections have non-
zero values, this implies something is causing processing 
to be delayed.
•
Local Address and Foreign Address: Lists the hosts and 
ports the sockets are connected with. 
•
State: Displays the current state of the TCP connection, 
based on the TCP protocol. As UDP is a stateless 
protocol, the ‘State’ column will be blank for UDP 
connections. The most common TCP states include:
–
Listen: Waiting for an external device to establish a connection
–
Established: Ready for communication on this connection
–
Close Wait: The remote machine has closed the connection, but 
the local device has not closed the connection yet.
–
Time Wait: The local machine is waiting for a period of time after 
sending an ACK to close a connection.
For more information about the states of a TCP connection, see RFC 793.
Understanding Netstat:
•
Recv-Q has a value greater than zero but is in a 
‘Close Wait’ state. This indicates that these sockets 
should be torn down but are hanging. If several 
sockets are in this state, it could imply the 
application is having difficulty tearing down the 
connection and may warrant additional 
investigation. 
•
Connections that have localhost as the ‘Local’ and 
‘Foreign’ address denote an internal process using 
the TCP stack to communicate. These connections 
are not concerning and are standard practice.

---

## isilon-network-design::chunk_27

difficulty tearing down the connection and may warrant additional investigation. • Connections that have localhost as the ‘Local’ and ‘Foreign’ address denote an internal process using the TCP stack to communicate. These connections are not concerning and are standard practice.

© Copyright 2017 Dell Inc.
79
Netstat –s –p tcp
‘-s’ is statistics by protocol and ‘-p’ displays the net to media tables limited to ‘tcp’
The fields highlighted in red are reviewed as a ratio of the total 
packets that are transmitted and received. Additionally, these 
statistics should be monitored for sudden increments. As a 
rule of thumb, under 1% is not concerning but this also 
depends on the workload. These fields provide the following: 
•
Retransmitted Packets: Packets that are retransmitted 
consume network bandwidth and could be the reason for 
further investigation. However, examining the percentage 
is critical. In this case, 249379 out of 235829612 were 
retransmitted, which is 0.105%. 
•
Duplicate Acknowledgements: High latency between 
endpoints may lead to duplicate acknowledgments, but the 
ratio must be examined. In this case, it is 0.419%. This 
number varies depending on the workload. 
•
Out of Order Packets: Out of order packets are placed in 
order by TCP before presenting to the application layer, 
which impacts the CPU and overall stack performance as 
additional effort is involved in analyzing the packets. 
Performance is impacted the most when packets arrive out 
of order with a significant time gap, or a number of packets 
are out of order. The ratio, in this case, is 0.197%, which is 
negligible.

© Copyright 2017 Dell Inc.
80
Netstat –i
Interface display – Cumulative statistics for packets transferred, errors, MTU, and collisions

---

## isilon-network-design::chunk_28

gap, or a number of packets are out of order. The ratio, in this case, is 0.197%, which is negligible. © Copyright 2017 Dell Inc. 80 Netstat –i Interface display – Cumulative statistics for packets transferred, errors, MTU, and collisions

© Copyright 2017 Dell Inc.
81
Netstat –i (continued)
netstat –i, lists the following columns:
•
Name: Network Interface Card (NIC) name. Loopback interfaces are listed as ‘lo0,’ and ‘ib’ specifies InfiniBand.
•
MTU: Lists the MTU specified for the interface.
•
Network: Specifies the network associated with the interface.
•
Address: MAC address of the interface.
•
Ipkts: Input packets are the total number of packets received by this interface.
•
Ierrs: Input errors are the number of errors reported by the interface when processing the ‘Ipkts.' These errors include 
malformed packets, buffer space limitation, checksum errors, errors generated by media, and resource limitation errors. 
Media errors are errors specific to the physical layer, such as the NIC, connection, cabling, or switch port. Resource 
limitation errors are generated at peak traffic when interface resources are exceeded by usage.
•
Idrop: Input drops are the number of packets that were received, but not processed and consequently dropped on the wire. 
Dropped packets typically occur during heavy load.
•
Opkts: Output packets are the total number of packets transmitted by this interface
•
Oerrs: Output errors are the number of errors reported by the interface when processing the ‘Opkts.' Examples of errors 
include the output queue reaching limits or an issue with the host.
•
Coll: Collisions are the number of packet collisions that are reported. Collisions typically occur during a duplex mismatch or 
during high network utilization.

---

## isilon-network-design::chunk_29

‘Opkts.' Examples of errors include the output queue reaching limits or an issue with the host. • Coll: Collisions are the number of packet collisions that are reported. Collisions typically occur during a duplex mismatch or during high network utilization.

© Copyright 2017 Dell Inc.
82
Netstat –i (continued)
What to check
Errors and dropped packets require closer examination. However, the percentage of errors and 
dropped packets are the main factor. The following are some of the points to consider for further 
analysis: 
•
‘Ierrs’ should typically be less than 1% of the total ‘Ipkts.' If greater than 1%, check ‘netstat –m’ 
for buffer issues and consider increasing the receive buffers. Prior to implementing changes on 
production system, buffer changes should be tested in a lab environment. Refer to the Isilon
Network Stack Tuning Section for additional details. 
•
‘Oerrs’ should typically be less than 1% of the total ‘Opkts’. If greater than 1%, it could be a result 
of network saturation, otherwise consider increasing the send queue size. 
•
The ratio of ‘Coll’ to ‘Opkts,' should typically be less than 10%. If greater than 10%, it could be a 
result of high network utilization.

© Copyright 2017 Dell Inc.
83
Netstat -m
Displays the current status of network memory requests as mbuf clusters
•
If mbufs are exhausted, the node cannot accept any additional network traffic.
•
The area below highlighted in red, confirms if any memory requests have been denied.

© Copyright 2017 Dell Inc.
84
InsightIQ External Network Errors
‘External Network Errors’ are reported using the output from ‘netstat –i’ on external interfaces only. 
The total of the ‘Ierrs’ and ‘Oerrs’ is combined and displayed in the graph. Refer to the previous 
section for interpreting the output from ‘netstat –i’.

© Copyright 2017 Dell Inc.
85
InsightIQ External Network Errors by Node
In order to find the exact interfaces the errors, sort the graph by ‘Node’, as shown below:

---

## isilon-network-design::chunk_30

to the previous section for interpreting the output from ‘netstat –i’. © Copyright 2017 Dell Inc. 85 InsightIQ External Network Errors by Node In order to find the exact interfaces the errors, sort the graph by ‘Node’, as shown below:

© Copyright 2017 Dell Inc.
86
InsightIQ External Network Errors by Direction
In order to find the exact interfaces the errors, sort the graph by ‘Direction’, as shown below:

© Copyright 2017 Dell Inc.
87
InsightIQ External Network Errors by Interface
In order to find the exact interfaces the errors, sort the graph by ‘Interface’, as shown below:
After sorting the network errors, it is concluded that the external network errors reside on the interface 
‘7/10gige-1’ of Node 7, on the input or receive side. Further analysis must be performed on this 
interface to conclude the root cause. Refer to the ‘netstat –i’ section in this deck for the next 
troubleshooting steps.

---

## isilon-network-design::chunk_31

on the interface ‘7/10gige-1’ of Node 7, on the input or receive side. Further analysis must be performed on this interface to conclude the root cause. Refer to the ‘netstat –i’ section in this deck for the next troubleshooting steps.

© Copyright 2017 Dell Inc.
88
Domain Name Service (DNS)
Resolves hostnames to IP addresses
A local DNS resolves local hostnames, while a public internet 
DNS resolves external hostnames. ‘nslookup’ and ‘dig’ are 
utilities for troubleshooting DNS. ‘dig’ is more detailed and 
displays the following sections:
•
Header: Provides the version of ‘dig’, options the ‘dig’ 
command used and the flags that are displayed.
•
Question Section: Displays the original input provided to the 
command. In the case above, dell.com was queried. The 
default is to query the DNS A record. Other options are 
available for querying MX and NS records.
•
Answer Section: Output received by dig from the DNS 
server queried. 
•
Authority Section: Lists the available Name Servers of 
dell.com. They have the authority to respond to this query.
•
Additional Section: Resolves the hostnames from the 
Authority Section to IP addresses.
•
Stats Section: Footer at the end of the query displays the 
when, where, and time the query consumed.
Dig supports an array of options. The most common options include a 
reverse look-up using ‘dig –x [IP address]’ to find a host name. The other is 
to specify a DNS server to query using ‘dig @[dns server] [hostname]’.

---

## isilon-network-design::chunk_32

consumed. Dig supports an array of options. The most common options include a reverse look-up using ‘dig –x [IP address]’ to find a host name. The other is to specify a DNS server to query using ‘dig @[dns server] [hostname]’.

© Copyright 2017 Dell Inc.
89
Tools and References
•
Technical Marketing Engineering:
–
https://esg.one.dell.com/sites/StorageEng/Collateral/SitePages/
UDS%20Collateral.aspx
•
Brocade Virtual Router: 
http://www.brocade.com/en/products-services/software-
networking/network-functions-virtualization/vrouter.html
•
Cisco Nexus 5000 Series Configuration Guide: 
http://www.cisco.com/c/en/us/td/docs/switches/datacenter/
nexus5000/sw/configuration/guide/cli/CLIConfigurationGui
de/QoS.html#pgfId-1138522
•
Cisco Catalyst 6500 Best Practices:                                                     
http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst
6500/ios/12-
2SX/best/practices/recommendations.html#wp1039880
•
Brocade Switching Configuration Guide:                                                                           
http://www.brocade.com/content/html/en/configuration-
guide/NI_05800a_SWITCHING/GUID-8B890954-65A7-
41DA-8E10-7A88DFDA687C.html
•
Arista Product Documentation: 
https://www.arista.com/en/support/product-documentation
•
Configuration of Jumbo MTU on Nexus 5000 and 
7000 Series:                                
http://www.cisco.com/c/en/us/support/docs/switc
hes/nexus-5000-series-switches/112080-config-
mtu-nexus.html
•
IEEE Standards: 
https://standards.ieee.org/findstds/standard/802.
1AX-2008.html
•
SMBv3 Multi-Channel: 
https://blogs.technet.microsoft.com/josebda/2012
/06/28/the-basics-of-smb-multichannel-a-feature-
of-windows-server-2012-and-smb-3-0/
•
RFCs:                                                                                        
http://www.faqs.org/rfcs/rfc1812.html
http://www.faqs.org/rfcs/rfc1122.html
http://www.faqs.org/rfcs/rfc1123.html
https://tools.ietf.org/html/rfc3971
https://tools.ietf.org/html/rfc792
https://tools.ietf.org/html/rfc3513