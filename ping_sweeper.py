# Ping Sweeper Script
import os

def ping_sweep(subnet):
    active_hosts = []
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        response = os.system(f"ping -c 1 -w 1 {ip} > /dev/null 2>&1")
        if response == 0:
            active_hosts.append(ip)
    return active_hosts

if __name__ == "__main__":
    subnet_input = input("Enter the subnet (e.g., 192.168.1): ")
    active = ping_sweep(subnet_input)
    if active:
        print("Active hosts:")
        for host in active:
            print(host)
    else:
        print("No active hosts detected.")