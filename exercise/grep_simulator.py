acl_rules = [
    "access-list 101 permit tcp any any eq 80",
    "access-list 101 deny ip any any",
    "access-list 101 permit udp any any eq 53",
    "access-list 101 deny icmp any any"
]

for rule in acl_rules:
    if "permit" in rule:
        print(rule)
