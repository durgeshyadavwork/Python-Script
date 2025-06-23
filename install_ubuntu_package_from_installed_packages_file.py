import subprocess

def is_package_installed(package_name):
    """Check if the package is already installed in Ubuntu."""
    try:
        result = subprocess.run(
            ["dpkg", "-s", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return "install ok installed" in result.stdout.lower()
    except Exception as e:
        print(f"[!] Error checking package '{package_name}': {e}")
        return False

def install_package(package_name):
    """Install the package using apt-get."""
    try:
        print(f"[+] Installing: {package_name}")
        subprocess.run(
            ["sudo", "apt-get", "install", "-y", package_name],
            check=True
        )
    except subprocess.CalledProcessError:
        print(f"[✗] Failed to install: {package_name}")

def install_packages_from_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or " - " not in line:
            continue

        # Split and extract only the package name (ignore version)
        package_name = line.split(" - ")[0].strip()

        print(f"👉 Checking package: {package_name}")
        if is_package_installed(package_name):
            print(f"✅ Already installed: {package_name} — Skipping.\n")
        else:
            install_package(package_name)
            print()

if __name__ == "__main__":
    install_packages_from_file("installed_packages.txt")
