import subprocess

def check_open_ports(link):
    try:
        print("\n [+] Checking for open ports...")
        command = ["nmap", link, "--open"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Failed to scan")

def check_vulnerabilities(link):
    try:
        print("\n [+] Checking for outdated versions..")
        command = ["nikto","-h", link]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Failed to scan")


target = input("Enter the target URL: ")

ports = check_open_ports(target)
vuln = check_vulnerabilities(target)

print("\n [+] Done")

with open("results.txt", "w") as f:
    f.write("Target: " + target + "\n")
    f.write(ports)
    f.write("\n\n")
    f.write(vuln)

print("\n [+] Results saved to results.txt")