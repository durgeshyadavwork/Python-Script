# import subprocess

# # Ubuntu-only identifiers to exclude
# ubuntu_only_keywords = [
#     "ubuntu", "gnome", "ubuntu-desktop", "snapd", "dpkg", "apt", "unity", "systemd-oomd", "yaru",
#     "ubuntu-session", "ubuntu-wallpapers", "xserver-xorg", "winehq", "xdg", "whoopsie", "fonts", "gtk", "systemd-"
# ]

# def is_available_on_centos(pkg_name):
#     try:
#         result = subprocess.run(["yum", "list", pkg_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         return pkg_name in result.stdout
#     except Exception:
#         return False

# # Input and output files
# input_file = "installed_packages.txt"
# output_file = "centos_packages.txt"

# filtered_packages = []

# with open(input_file, "r") as f:
#     lines = f.readlines()

# for line in lines:
#     parts = line.strip().split(" - ")
#     if len(parts) < 2:
#         continue
#     name = parts[0].strip()

#     # Skip obviously Ubuntu-only packages
#     if any(keyword in name for keyword in ubuntu_only_keywords):
#         continue

#     # Optional: check availability on CentOS
#     if is_available_on_centos(name):
#         filtered_packages.append(name)
#     else:
#         print(f"[!] Skipping not found in CentOS: {name}")

# # Save to new file
# with open(output_file, "w") as f:
#     for pkg in filtered_packages:
#         f.write(pkg + "\n")

# print(f"\n✅ Filtered CentOS-compatible packages written to '{output_file}'")



# Fixed: Only filter based on Ubuntu-specific package name patterns

# Ubuntu-only identifiers to exclude
ubuntu_only_keywords = [
    "ubuntu", "gnome", "snapd", "dpkg", "apt", "unity", "systemd-oomd", "yaru",
    "ubuntu-session", "ubuntu-wallpapers", "xserver-xorg", "winehq", "xdg",
    "whoopsie", "fonts", "gtk", "indicator", "nautilus", "update-manager", "software-properties"
]

input_file = "installed_packages.txt"
output_file = "centos_packages.txt"

filtered_packages = []

with open(input_file, "r") as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split(" - ")
    if len(parts) < 2:
        continue
    name = parts[0].strip()

    # Skip Ubuntu-only packages
    if any(keyword in name.lower() for keyword in ubuntu_only_keywords):
        continue

    filtered_packages.append(name)

# Write result
with open(output_file, "w") as f:
    for pkg in filtered_packages:
        f.write(pkg + "\n")

print(f"✅ Filtered list saved to '{output_file}' with {len(filtered_packages)} packages.")
