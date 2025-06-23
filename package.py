import subprocess
import platform
import os

def get_installed_packages():
    # Try detecting OS using modern approach
    distro = ""
    try:
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("ID="):
                        distro = line.strip().split("=")[1].replace('"', '').lower()
                        break
    except Exception as e:
        print("Could not detect distribution:", e)
        return

    output_lines = []

    try:
        if "debian" in distro or "ubuntu" in distro:
            print("Detected Debian/Ubuntu system.")
            result = subprocess.run(["dpkg", "-l"], capture_output=True, text=True, check=True)
            lines = result.stdout.strip().split('\n')[5:]  # Skip header lines
            for line in lines:
                parts = line.split()
                if len(parts) >= 3:
                    package_info = f"{parts[1]} - {parts[2]}"
                    print(package_info)
                    output_lines.append(package_info)
        elif "centos" in distro or "rhel" in distro or "fedora" in distro:
            print("Detected RHEL/CentOS/Fedora system.")
            result = subprocess.run(["rpm", "-qa", "--qf", "%{NAME} - %{VERSION}-%{RELEASE}\n"],
                                    capture_output=True, text=True, check=True)
            print(result.stdout)
            output_lines = result.stdout.strip().split('\n')
        else:
            print("Unsupported or unknown Linux distribution.")
            return
    except subprocess.CalledProcessError as e:
        print("Error running package listing command:", e)
        return

    # Write to file
    try:
        with open("installed_packages.txt", "w") as f:
            for line in output_lines:
                f.write(line + "\n")
        print("\nPackage list saved to 'installed_packages.txt'")
    except Exception as e:
        print("Failed to write to file:", e)

if __name__ == "__main__":
    get_installed_packages()
