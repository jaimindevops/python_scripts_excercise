import subprocess

# Example real command (Linux):
# result = subprocess.run(
#     ["ping", "-c", "4", "8.8.8.8"],
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE
# )
# output = result.stdout.decode()

# Mock output for parsing practice
output = """PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=14.2 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=14.5 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=117 time=14.1 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=117 time=14.4 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 14.120/14.300/14.510/0.160 ms
"""

avg_latency = None

# Step 1: Split output into lines
for line in output.splitlines():
    if "min/avg/max" in line:
        # Step 2: Split at '=' and take right-hand side
        stats_part = line.split("=")[1].strip()
        
        # Step 3: Remove ' ms'
        stats_part = stats_part.replace(" ms", "")
        
        # Step 4: Split by '/'
        values = stats_part.split("/")
        
        # avg is second value
        avg_latency = float(values[1])
        break

if avg_latency is not None:
    print(f"Average latency: {avg_latency} ms")
else:
    print("Average latency not found.")
