#!/bin/bash
download_speed=$(speedtest | grep Download | cut -d ":" -f 2 | cut -d "M" -f 1 | tr -d ' ')
#echo $download_speed
wget --http-user="sensor" --http-password="sensor" -O /dev/null http://192.168.1.214/Api/EasyIoT/Control/Module/Virtual/N4S0/ControlLevel/$download_speed >/dev/null 2>&1
