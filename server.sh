#!/bin/bash
nohup /usr/local/bin/linuxVirtualization/server "$(ip route get 1 | awk '{print $7}')" &
