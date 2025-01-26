# Firewall Tester Script
import socket

def test_firewall(ip, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((ip, port)) == 0:
                    open_ports.append(port)
        except Exception as e:
            print(f"Error testing port {port}: {e}")
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the IP address to test: ")
    port_range = range(20, 1025)  # Common ports
    open_ports = test_firewall(target_ip, port_range)
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports detected.")