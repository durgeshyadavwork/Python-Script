
# 🛠️ VPC File Processor Script

This Python script automates the following tasks:

1. Creates a directory named `Config Folder` if it doesn't already exist.
2. Copies the Terraform file (`vpc.tf`) from a source path to `Config Folder` as `newvpc`.
3. Replaces the word `"tags"` with `"tagss"` in the copied file.

---

## 📁 Project Structure

```

project-root/
├── config update.py
├── README.md
└── Config Folder/
└── newvpc

````

---

## ⚙️ Prerequisites

- Python 3.x installed
- The file `vpc.tf` should be present at:

```bash
/home/cadet/Desktop/Daily Code/CICD/vpc.tf
````

---

## 🚀 How to Run

```bash
python3 config\ update.py
```

---

## 🧾 What This Script Does

* Creates a folder named `Config Folder` if it doesn’t exist.
* Changes the current working directory to `Config Folder`.
* Copies `vpc.tf` into `newvpc`.
* Replaces all occurrences of `old_ip` with `new_ip` inside `newvpc`.

---

## 📌 Notes

* Ensure `vpc.tf` contains the word `tags` to see the replacement effect.
* You can modify the `old_ip` and `new_ip` variables to change what gets replaced.



---

## ✍️ Author

Made with ❤️ by \[Durgesh Yadav]

```
