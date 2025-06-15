import socket
import argparse
import logging
import csv
import nmap

# Configure logging
logging.basicConfig(filename='scan_results.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def socket_scan(ip, start_port, end_port):
    print("\n[***] Starting Basic Socket Scan...\n")
    results = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                msg = f"[+] Port {port} is OPEN (via socket)"
            else:
                msg = f"[-] Port {port} is CLOSED (via socket)"
            print(msg)
            logging.info(msg)
            results.append([port, "OPEN" if result == 0 else "CLOSED", "Socket", "-"])
    return results

def nmap_scan(ip, start_port, end_port):
    print(f"\n[*] Starting Nmap Scan on {ip} for ports {start_port}-{end_port}...\n")
    nm = nmap.PortScanner()
    nm.scan(ip, f'{start_port}-{end_port}', arguments='-sV')

    nmap_results = []

    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                state = nm[host][proto][port]['state']
                name = nm[host][proto][port]['name']
                product = nm[host][proto][port].get('product', '')
                msg = f"[Nmap] Port: {port} Service: {name} Product: {product}"
                print(msg)
                logging.info(msg)
                nmap_results.append([port, state.upper(), "Nmap", f"{name} {product}".strip()])
    return nmap_results

def write_csv_report(results):
    with open('sample_report.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Status", "Scan_Type", "Service/Product"])
        writer.writerows(results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Port Scanner with Socket & Nmap")
    parser.add_argument("ip", help="Target IP Address")
    parser.add_argument("start_port", type=int, help="Starting Port Number")
    parser.add_argument("end_port", type=int, help="Ending Port Number")
    args = parser.parse_args()

    socket_results = socket_scan(args.ip, args.start_port, args.end_port)
    nmap_results = nmap_scan(args.ip, args.start_port, args.end_port)

    combined_results = socket_results + nmap_results
    write_csv_report(combined_results)

    print("\n[***] Scan Completed. Results saved to 'sample_report.csv' and 'scan_results.log'.\n")
