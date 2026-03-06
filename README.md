# Python Port Scanner

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Cybersecurity-red?style=for-the-badge)

A simple TCP port scanner written in Python using raw sockets — built to understand 
how port scanning works at a network level.

---

## Features

- Scan ports from **1 to 1024**
- Detect **open and closed ports**
- Hostname to IP resolution
- Scan execution time measurement

---

## Usage
```bash
python portscanner.py
```

Then enter the target host:
```
Enter target IP or hostname: localhost
```

Example output:
```
Scanning 127.0.0.1...

[CLOSED] Port 1
[CLOSED] Port 2
[OPEN]   Port 22

Scan completed in 2.31 seconds
Open ports found: 1
```

---

## How It Works

The scanner attempts a TCP connection to each port in the range 1–1024.
If the connection succeeds, the port is open — meaning a service is actively 
listening on it. This mimics the basic logic of tools like `nmap`.

Each connection attempt uses Python's `socket` library to perform a TCP handshake. 
Open ports respond; closed or filtered ports reject or time out.

---

## What I Learned

- How TCP connections work at the socket level
- The difference between open, closed, and filtered ports
- How tools like `nmap` approach network reconnaissance
- Practical use of Python's `socket` module for low-level networking

---

## Technologies

- Python
- Socket programming
- TCP/IP networking

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.  
Only use it on systems you own or have **explicit permission** to scan.  
Unauthorized port scanning may be illegal in your jurisdiction.

---

## License

MIT License
