#!/bin/bash
response_time=$(ping -c 10 8.8.8.8 | tail -1 | cut -d "=" -f 2 | cut -d "/" -f 1 | tr -d ' ')
#set $response_time=$(date)
echo $response_time
wget --http-user="sensor" --http-password="sensor" -O /dev/null http://192.168.1.214/Api/EasyIoT/Control/Module/Virtual/N3S0/ControlLevel/$response_time >/dev/null 2>&1
