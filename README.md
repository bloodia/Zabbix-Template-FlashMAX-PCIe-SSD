# Zabbix Template FlashMAX PCIe SSD
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/bloodia/Zabbix-Template-FlashMAX-PCIe-SSD/blob/master/LICENSE)

## Overview
Monitoring HGST PCIe Flash Drive（4,800GB or 2,200GB or 1,100GB）status with Zabbix template.  

## Requires
### Hardware
- HGST PCIe Flash Drive（4,800GB or 2,200GB or 1,100GB）

### OS
- CentOS 5.x - 7.x

### Modules
- vgc-monitor (FlashMAX Utility Command)

### Zabbix
- 3.4
- 4.0

### Python
- 2.6
- 2.7
- 3.3
- 3.4
- 3.5
- 3.6

### Python Modules
- json
- subprocess
- argparse

## Script Usage
```
usage: lld-vgc.py [-h] [-v] [-p]

optional arguments:
  -h, --help       show this help message and exit
  -v, --version    show version and exit
  -p, --partition  show all partition

for example: /usr/local/bin/lld-vgc.py
```

## How to Install
### Script
- Create directory "/usr/local/bin" and copy "Custom Script" file (py) to inside.  
- Change "Custom Script" file (py) to 555 or dr-xr-xr-x using chmod.  

### UserParameter Config
- Copy "UserParameter Config" file (conf) to /etc/zabbix/zabbix_agentd.d and restart Zabbix agent.  

### Template
- Import the template file (xml) and assign it to the host monitored.

## Author
[@bloodia](https://twitter.com/bloodiadotnet)
