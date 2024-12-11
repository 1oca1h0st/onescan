import nmap3

nmap = nmap3.Nmap()


def port_scan(ip: str):
    results = nmap.scan_top_ports(ip)
    return results
