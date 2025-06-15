# Automated Port Scanner in Python

##  Project Overview
This is a Python-based **Automated Port Scanner** that combines both **Socket programming** and **Nmap scanning** to detect open ports on a specified target IP address or hostname. The scanner checks each port for availability and gathers detailed service information using Nmap.

##  Features
✅ Scans target IP or hostname over a specified port range.  
✅ **Socket-based port scanning** to check if ports are open or closed.  
✅ **Nmap scanning integration** for detailed service, version, and product info.  
✅ Logs all results to `scan_results.log` with timestamps.  
✅ Generates a structured **CSV report (`sample_report.csv`)** for easy result analysis.  
✅ User-friendly command-line interface with argument parsing.

##  Tools & Technologies
- **Python 3.x**
- **Socket library** (for basic TCP port scanning)
- **Nmap module (`python-nmap`)** for advanced service detection
- **Logging module** for scan logs
- **CSV module** for result reporting

##  Usage Instructions

### 1. Clone or Download this Repository
```bash
git clone https://github.com/Aish689/PortScannerProject.git
cd PortScannerProject
```

### 2. Install Dependencies
Install the required Python modules:
```bash
pip install -r requirements.txt
```
Or for system-based installation:
```bash
sudo apt install python3-nmap
```

### 3. Run the Scanner
```bash
python3 port_scanner.py <target_ip> <start_port> <end_port>
```
**Example:**
```bash
python3 port_scanner.py 127.0.0.1 20 25
```

##  Output Files

| File Name              | Description                             |
|-----------------------|-----------------------------------------|
| `scan_results.log`     | Detailed log of the scanning process with timestamps. |
| `sample_report.csv`    | CSV file with Nmap scan results (Port, State, Service, Product). |

##  Example Output
```
 Starting Basic Socket Scan...

[-] Port 20 is CLOSED (via socket)
[-] Port 21 is CLOSED (via socket)
...

[*] Starting Nmap Scan on 127.0.0.1 for ports 20-25...

Host: 127.0.0.1 (localhost)
State: up
[Nmap] Port: 20 Service: ftp-data Product: 
[Nmap] Port: 21 Service: ftp Product: 
...
```


##  Future Improvements
- Multi-threaded scanning for faster performance.
- GUI version with interactive interface.
- Live scan progress bar.
- Export options (JSON, XML).
- Automatic detection of local/remote hosts.

##  Author
**Ayesha Atta**  
GitHub: [Aish689](https://github.com/Aish689)  
Project: Automated Port Scanner for Network Security and SOC Analysis.

