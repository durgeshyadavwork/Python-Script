## Prerequisites

- system with `sudo` access
- Python 3 installed
- create package.py file


python_package
├── centos_packages.txt
├── centos_ready_packages.txt
├── filter_centos_packages.py                                           // when only centos package centos_packages.txt from this file install on centos (filter package)
├── filter_ubuntu_defaults.python										// when run this file then create centos_ready_packages.txt
├── install_centos_packages.py                                          // when all package installed_packages.txt from this file install on centos 
├── installed_packages.txt                                              // after run step 1 file then create this file
├── install_ubuntu_package_from_installed_packages_file.py              // when run this then listed package file from installed_packages.txt install same ubuntu server
├── package.py                                                          // Step 1 run this
└── README.md