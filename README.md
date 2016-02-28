This is a complete Vagrant configuration, to create, start and configure a Ubuntu V.M. to test this script.

#Attention
This repo, is pre-configured to use these V.M to test: https://github.com/fellipeh/vagrant_lampwebserver

#Requirements:
* VirtualBox
* Vagrant
* Python 2.7
* Vagrant file cloned: from https://github.com/fellipeh/vagrant_lampwebserver

#How to install:
* Clone this repository.
* Run: ```vagrant up```
* Access your VM using:  ```vagrant ssh```

#How to use:
* python check_services.py <IP>

#How to configure the Port Files (port.json)
* This file is a normal JSON file, and you need to create one record per port, that you want to test with the service name, like this:
```
[
  {
    "port": 80,
    "service": "apache"
  },
  {
    "port": 22,
    "service": "sshd"
  },
  {
    "port": 3306,
    "service": "mysql"
  }
]
```


