# PowerScale OneFS NFS Best Practices

**Source:** Dell Support KB Article 000063022  
**Title:** PowerScale: OneFS: Best practices for NFS client settings  
**Date:** January 2, 2026  
**URL:** https://www.dell.com/support/kbdoc/en-us/000063022/emc14001361-best-practices-for-nfs-client-settings

---

## Supported Protocol Versions

PowerScale OneFS currently supports Network File System (NFS) versions 3 and 4. NFS version 2 is not supported.

### NFSv3

NFS version 3 is the most widely used version of the NFS protocol today, and is considered to have the widest client and filer adoption. Key characteristics:

- **Stateless** - A client does not technically establish a new session if it has the correct information to ask for files. This allows for simple failover between OneFS nodes using dynamic IP pools.

- **User and Group info is presented numerically** - Client and Server communicate user information by numeric identifiers, allowing the same user to appear as different names between client and server.

- **File Locking is out of band** - Version 3 of NFS uses a helper protocol called NLM to perform locks. This requires the client to respond to RPC messages from the server to confirm locks have been granted.

- **Can run over TCP or UDP** - This version can run over UDP instead of TCP, leaving handling of loss and retransmission to the software instead of the operating system. Dell Technologies always recommend using TCP.

### NFSv4

NFS version 4 is the newest major revision of the NFS protocol, and is increasing in adoption. Key differences from v3:

- **Stateful** - NFSv4 uses sessions to handle communication; both client and server must track session state.
  - Prior to OneFS 8.X this meant that NFSv4 clients required static IP pools on the PowerScale or could encounter issues.

- **User and Group info is presented as strings** - Both client and server must resolve the names of the numeric information stored.

- **File Locking is in band** - Version 4 no longer uses a separate protocol for file locking; instead it's compounded with OPENs, CREATES, or WRITES.

- **Compound Calls** - Version 4 can bundle a series of calls in a single packet, reducing the number of calls for common operations.

- **Only supports TCP** - Version 4 leaves loss and retransmission up to the underlying operating system.

#### NFSv4.1 and Beyond

NFSv4.1 and v4.2 are available starting in OneFS version 9.3.

---

## Mount Options

### Read and Write Size (rsize / wsize)

PowerScale support recommends:
- Minimum `wsize` and `rsize` of 128K (based on native block size)
- **Recommendation:** For most modern Linux distros, do NOT explicitly configure these settings - let the client renegotiate automatically
- Modern Linux distributions support NFS read/write block sizes up to 1 MB and will automatically negotiate optimal block size

**Exception:** Only set explicitly if an application or vendor specifically requires a smaller size.

When not explicitly set, your NFS client uses the PowerScale NFS server FSINFO data as defined in the NFS export configuration:

- **NFSv3:** 512KB writes / 1MB reads
- **NFSv4:** 1MB writes / 1MB reads

**Note:** Lab testing has shown no discernible performance change through adjusting read/write size once the native block size (128K) is met.

### Defining Retries and Timeouts

PowerScale generally recommends:
- **Timeout:** 60 seconds to account for worst-case failover scenario
- **Retries:** 2 times before reporting failure

### Soft vs Hard Mounts

- **Hard mounts** (recommended) - Client retries operations indefinitely on timeout/error, ensuring the mount doesn't disconnect when IP addresses move between nodes
- **Soft mounts** - Will error out and expire the mount requiring a remount after IP address moves

### Allowing Interrupt

Include the `intr` mount option to allow interrupt signals (ctrl+c) to end waiting processes when the cluster is not responding.

### Local vs. Remote Locking

- **Remote locking** (default) - Best when multiple clients access the same directory
- **Local locking** - Can provide performance benefits when a client doesn't share directory access; some databases require this

### Attribute Caching (ac/noac)

- **Default:** Attribute caching is enabled
- Use `noac` to achieve attribute cache coherence among multiple clients
- Disabling attribute caching forces application writes to become synchronous
- Enable attribute caching to improve performance and reduce NFS operation latency

**Note:** Settings depend on specific needs - refer to the NFS Design Considerations white paper for detailed guidance.

---

## Performance

Based on lab testing, PowerScale Support has not found any discernable performance differences between different versions of NFS in the latest, supported versions of OneFS.

---

## Checking Export Settings

To see the wsize/rsize values of a particular NFS export:

```bash
# List all exports with verbose output
isi nfs exports ls -v --zone <zone name>

# View specific export
isi nfs export view <export id>
```

Example output:
```
Read Transfer Max Size: 1.00M
Read Transfer Size: 128.00k
Write Transfer Max Size: 1.00M
Write Transfer Size: 512.00k
```

---

## Additional Resources

- **Primary Reference:** PowerScale OneFS NFS Design Considerations and Best Practices  
  https://infohub.delltechnologies.com/en-us/t/powerscale-onefs-nfs-design-considerations-and-best-practices-3/
- **PowerScale OneFS Info Hubs:** https://www.dell.com/support/kbdoc/en-us/000152189/powerscale-onefs-info-hubs
