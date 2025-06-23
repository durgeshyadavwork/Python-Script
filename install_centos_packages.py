import subprocess

def is_package_installed(package_name):
    """Check if a package is already installed on CentOS."""
    try:
        result = subprocess.run(
            ["rpm", "-q", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"[!] Error checking package '{package_name}': {e}")
        return False

def install_package(package_name):
    """Try to install a package using yum."""
    try:
        print(f"[+] Installing: {package_name}")
        subprocess.run(
            ["sudo", "yum", "install", "-y", package_name],
            check=True
        )
    except subprocess.CalledProcessError:
        print(f"[✗] Failed to install: {package_name}")

def install_packages_from_file(file_path):
    with open(file_path, "r") as f:
        packages = [line.strip() for line in f if line.strip()]

    for pkg in packages:
        print(f"👉 Checking package: {pkg}")
        if is_package_installed(pkg):
            print(f"✅ Already installed: {pkg} — Skipping.\n")
        else:
            install_package(pkg)
            print()

if __name__ == "__main__":
    install_packages_from_file("centos_ready_packages.txt")
