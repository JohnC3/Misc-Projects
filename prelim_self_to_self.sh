#!/bin/bash

source /usr/local/lib/soma/network

echo "Verifying link quality, please connect both ports to the switch"
read  -n 1 -p "Press any key to continue"

printf "configuring interfaces...\t"

ip netns add ns_lan

ip link set eth1 netns ns_lan

ip netns exec ns_lan ip link set eth1 up

# Adding an ip address to eth0 so communication gets through
ip addr add dev eth0 145.168.75.100/24

ip netns exec ns_lan ip addr add dev eth1 145.168.75.101/24

echo " COMPLETE"

printf "Sending traffic...\t"

ping 145.168.75.101 -I 145.168.75.100
#
# ip netns exec ns_lan iperf -s -I eth1
#
# iperf -c 192.145.168.75.101 -i 1 -t 20
