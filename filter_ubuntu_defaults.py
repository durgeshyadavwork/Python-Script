# filter_ubuntu_defaults.py

# Ubuntu/Debian specific keywords
ubuntu_keywords = [
    "ubuntu", "gnome", "snapd", "dpkg", "apt", "unity", "yaru", "whoopsie", "xserver",
    "fonts", "gtk", "nautilus", "indicator", "update-manager", "software-properties",
    "systemd-", "ubuntu-wallpapers", "ubuntu-session", "xdg", "grub", "udisks2",
    "upower", "libreoffice", "printer", "avahi", "fwupd", "thunderbird", "gnome-shell",
    "xauth", "xorg", "wayland", "xinput", "lightdm", "gdm3", "gstreamer", "tracker",
    "dbus", "bluez", "snap", "plymouth", "brltty", "speech", "espeak", "locale", "i386",
    "gtk", "xdg", "x11", "xfonts", "xdg", "xdg-utils", "xdg-desktop", "cups", "udisks",
    "modemmanager", "udisks", "policykit", "colord", "hplip", "geoclue", "cheese",
    "totem", "network-manager", "nvidia", "intel", "vdpau", "vulkan", "fwupd"
]

input_file = "installed_packages.txt"
output_file = "centos_ready_packages.txt"

filtered_packages = []

with open(input_file, "r") as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split(" - ")
    if len(parts) < 2:
        continue
    pkg_name = parts[0].strip().lower()

    # Ubuntu-only package detection
    if any(keyword in pkg_name for keyword in ubuntu_keywords):
        continue

    filtered_packages.append(parts[0].strip())

# Save final list
with open(output_file, "w") as f:
    for pkg in filtered_packages:
        f.write(pkg + "\n")

print(f"✅ Ubuntu-specific packages removed. Clean list saved to '{output_file}' with {len(filtered_packages)} packages.")
