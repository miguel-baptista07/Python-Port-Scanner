# Python Port Scanner

A simple TCP port scanner written in Python using sockets.

## Features

* Scan ports from **1 to 1024**
* Detect **open and closed ports**
* Hostname to IP resolution
* Scan execution time measurement

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

## Technologies

* Python
* Socket programming
* TCP networking

## License

MIT License
