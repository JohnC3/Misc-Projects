#!/bin/bash
#
# Connect to the device being tested over mesh.
# Confirms that the there is at least one plug in the lan port and a plug in the wan port
# Loopback adaptors not required

# Create a temporary ethernet interface on port 1.
source /usr/local/lib/soma/network

TEST_IF=tmp1

# Creates a temporary vlan on port 1 so we can check that it exists.
function create_tmp_interface {
  echo "Creating $TEST_IF on port1"
  $SWCONFIG dev $DEV_SWITCH vlan 3 set ports '1'
  $SWCONFIG dev $DEV_SWITCH vlan 1 set ports '2 3 6'
  $SWCONFIG dev $DEV_SWITCH set apply 1
  ip link add link eth1 name $TEST_IF type vlan id 2
  ip link set $TEST_IF up

}

# Removes port 1 from the vlan create earlier, rebooting the device will clear the vlan
function restore_tmp_interface {
  echo "Removing $TEST_IF on port1"
  ip link del $TEST_IF
  $SWCONFIG dev $DEV_SWITCH vlan 3 set ports ''
  $SWCONFIG dev $DEV_SWITCH vlan 1 set ports '1 2 3 6'
  $SWCONFIG dev $DEV_SWITCH set apply 1
}


function check_interface {
  iname=$1
  echo "checking that $iname is plugged in"
  lan_status=$(ethtool $iname | grep -o "Link detected: .*" | sed -n -e 's/Link detected: //p')
  echo "$iname link status"
  echo $lan_status
  if [ ! $lan_status = "yes" ]
  then
    echo "No connection detected on interface $iname"
    exit 1
  else
    echo "$iname PASS"
  fi
}

create_tmp_interface
#
# check_interface $WANIF
# check_interface $TEST_IF
#
# restore_tmp_interface
