arp_table = {
    "192.168.1.1": "00:1A:2B:3C:4D:5E",
    "10.0.0.5": "5E:4D:3C:2B:1A:00",
    "172.16.0.10": "AA:BB:CC:DD:EE:FF"
}

def get_mac_address(ip_address):
    return arp_table.get(ip_address, "IP not found")


# Test cases
print(get_mac_address("10.0.0.5"))  # 5E:4D:3C:2B:1A:00
print(get_mac_address("8.8.8.8"))   # IP not found
