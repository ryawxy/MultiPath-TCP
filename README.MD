# MultiPath-TCP

## Overview
MultiPath-TCP is a networking project that implements or explores the Multipath TCP (MPTCP) protocol, which enables simultaneous use of multiple network paths for improved throughput and reliability.

## Features
- Support for multiple concurrent network paths
- Load balancing across available connections
- Seamless failover between paths
- Improved network resilience

## Getting Started

### Prerequisites
- Python 3.x
- `matplotlib` (for generating failover visualization graphs)

### Installation
```bash
git clone <repository-url>
cd MultiPath-TCP
[your installation commands]
```

### Usage
To simulate the multipath connection, you will need to run the server and client in separate terminal instances:

```bash
# Terminal 1: Start the server (Receiver)
python src/server.py

# Terminal 2: Start the client (Sender with failover logic)
python src/client.py

# Terminal 3: Generate the performance graph after the transmission completes
python src/plot.py
```

## Project Structure
```
MultiPath-TCP/
├── src/
│   ├── server.py   
│   ├── client.py  
│   └── plot.py      
├── results/       
├── docs/          
│   ├── slides.pdf   
│   └── report.pdf   
└── README.md        
```

## Documentation
This project relies on a custom scheduler at the application layer to emulate kernel-level MPTCP behavior. The client attempts to send data via the primary socket. If a ConnectionError is raised (simulating a link failure or cable cut), the try-except block immediately catches it and reroutes the payload to the backup socket, ensuring continuous transmission without crashing the application.


## References
- [RFC 6824 - The Multipath TCP Protocol](https://tools.ietf.org/html/rfc6824)
- [MPTCP Community](https://www.multipath-tcp.org/)

---


