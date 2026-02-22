# Assign the mock log data to a variable
log_data = """2026-02-21 18:00:01 INFO [xApp-Monitor] E2 connection established successfully.
2026-02-21 18:05:22 ERROR [RIC-Interface] Connection refused from IP 10.23.45.67
2026-02-21 18:10:05 INFO [xApp-Monitor] Processing traffic statistics.
2026-02-21 18:12:33 ERROR [RIC-Interface] Connection refused from IP 192.168.1.105
2026-02-21 18:15:00 WARNING [Node-B] High latency detected on interface eth0.
2026-02-21 18:18:10 ERROR [RIC-Interface] Connection refused from IP 10.23.45.67
2026-02-21 18:20:00 INFO [xApp-Monitor] E2 connection teardown initiated.
"""
unique_ips = set() # Use a set to automatically handle uniqueness

# Split the multiline string into a list of individual lines
for line in log_data.split('\n'):
    # Check if the specific error message is in the current line
    if "Connection refused from IP" in line:
        # Split the line by spaces and grab the very last element (the IP)
        ip = line.split()[-1]
        unique_ips.add(ip)

# Convert back to a list if the interviewer specifically requested a list
print(list(unique_ips))
