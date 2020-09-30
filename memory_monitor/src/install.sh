#!/bin/sh
echo "Checking Python3"
if ! command -v python3 >/dev/null ;
then
    echo "Python3 not found, please install python3"
    exit 1
fi
echo "Python3 found"

echo "Installing pip3"
sudo apt update
sudo apt install python3-pip
if [ $? != 0 ];
then
    echo "Error installing pip3"
    exit 1
fi

echo "Installing psutil"
sudo python3 -m pip install psutil
if [ $? != 0 ];
then
    echo "Error installing psutil"
    exit 1
fi

_dir="${1:-${PWD}}"
_user="${USER}"
_service="
[Unit]
Description=Memory Monitor Service
After=multi-user.target

[Service]
Type=idle
User=${_user}
ExecStart=/usr/bin/python3 ${_dir}/memory_checker.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
"
_file="/lib/systemd/system/memory_monitor.service" 

echo "Creating Memory Monitor service"
if [ -f "${_file}" ]; 
then
    sudo rm "${_file}"
fi

sudo touch "${_file}"
sudo echo "${_service}" | sudo tee -a "${_file}" > /dev/null

echo "Enabling Memory Monitor service to run on startup"
sudo systemctl daemon-reload
sudo systemctl enable memory_monitor.service
if [ $? != 0 ];
then
    echo "Error enabling Memory Monitor service"
    exit 1
fi
sudo systemctl restart memory_monitor.service
echo "Memory Monitor service enabled"
exit 0

