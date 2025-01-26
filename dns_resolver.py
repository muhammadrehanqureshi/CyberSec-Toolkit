# DNS Resolver Script
import socket

def resolve_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"Domain {domain} resolves to {ip}")
    except Exception as e:
        print(f"Error resolving domain {domain}: {e}")

if __name__ == "__main__":
    domain_name = input("Enter a domain to resolve (e.g., example.com): ")
    resolve_dns(domain_name)