
# **CyberSec-Toolkit**

**CyberSec-Toolkit** is a collection of Python scripts designed to help individuals and cybersecurity enthusiasts learn, explore, and perform various ethical hacking and security-related tasks. This toolkit is intended for educational purposes and can be used to gain hands-on experience with fundamental cybersecurity concepts and tools.

---

## **Overview of Tools**

This repository includes the following cybersecurity tools:

1. **Firewall Tester**  
   - Description: Checks for open ports on a target IP address, helping identify potential network vulnerabilities.  
   - Usage: Useful for understanding network security and identifying ports that need to be secured.

2. **Sandbox Script**  
   - Description: Executes potentially risky commands or code in a controlled environment to prevent harm to the system.  
   - Usage: Ideal for testing suspicious scripts or commands safely.

3. **Website Vulnerability Scanner**  
   - Description: Scans websites for common vulnerabilities, such as exposed directories or outdated software.  
   - Usage: Helps identify areas of a website that might be vulnerable to attacks.

4. **Ping Sweeper**  
   - Description: Detects active hosts on a network by sending ICMP echo requests (pings) to a range of IP addresses.  
   - Usage: Useful for network mapping and identifying devices on a subnet.

5. **DNS Resolver**  
   - Description: Resolves domain names into their corresponding IP addresses.  
   - Usage: Helps understand how domain name resolution works and troubleshoot DNS-related issues.

6. **Text Encryption/Decryption**  
   - Description: Encrypts or decrypts plain text using a secret key to ensure secure communication.  
   - Usage: Useful for learning cryptographic principles and securing sensitive data.

7. **File Encryptor**  
   - Description: Encrypts and decrypts files using secure encryption keys to prevent unauthorized access.  
   - Usage: Ensures the confidentiality of sensitive files.

---

## **Requirements**

To run these tools, make sure you have the following installed:  
- **Python 3.x**: Download from [Python's official site](https://www.python.org/).  
- Required Python libraries:
  - `cryptography` (for encryption-related tools)
  
Install dependencies using the following command:  
```bash
pip install cryptography
```

---

## **How to Use**

1. **Clone the Repository**  
   Clone this repository to your local machine using the following command:  
   ```bash
   git clone https://github.com/muhammadrehanqureshi/CyberSec-Toolkit.git
   ```

2. **Navigate to the Project Directory**  
   ```bash
   cd CyberSec-Toolkit
   ```

3. **Run the Scripts**  
   Run each tool individually using Python:  
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of the script you want to run (e.g., `firewall_tester.py`).

---

## **Directory Structure**

```
CyberSec-Toolkit/
│
├── firewall_tester.py         # Script for testing firewall configurations
├── sandbox_script.py          # Script for executing commands in a safe environment
├── vulnerability_scanner.py   # Script for website vulnerability scanning
├── ping_sweeper.py            # Script for identifying active hosts
├── dns_resolver.py            # Script for resolving domain names to IPs
├── text_encryptor.py          # Script for text encryption and decryption
├── file_encryptor.py          # Script for encrypting and decrypting files
├── README.md                  # Documentation for the repository
├── .gitignore                 # File to exclude unnecessary files from Git
└── requirements.txt           # File listing Python dependencies
```

---

## **Contributing**

Contributions are welcome! If you’d like to improve or add more tools to this repository:  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/new-tool`).  
3. Commit your changes (`git commit -m 'Add new tool'`).  
4. Push to the branch (`git push origin feature/new-tool`).  
5. Open a pull request.

---

## **License**

This project is licensed under the **GNU General Public License (GPL)**.  

---

## **Disclaimer**

The tools in this repository are intended for **ethical and educational purposes only**.  
Any misuse of these tools is strictly prohibited and the responsibility of the user.
