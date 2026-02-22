cpu_metrics = [45, 82, 100, 30, 95, 12]

for value in cpu_metrics:
    if value == 100:
        print("CRITICAL")
    elif value > 80:
        print("WARNING")
    else:
        print("OK")
