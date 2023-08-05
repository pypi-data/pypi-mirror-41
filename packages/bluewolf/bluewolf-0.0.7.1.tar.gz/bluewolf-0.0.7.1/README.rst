Bluewolf - Bluetooth tracker

- A proof of concept proximity tracker for bluetooth and BLE devices.
- Uses raw linux sockets and bluetooth ioctl commands to directly interogate BT hardware devices.
- Multithreaded to maximize bluetooth connections
- A true "pythonic" implementation of the l2ping and hcitool rssi interrogation commands
- With fancy colors!

Installation: pip install bluewolf

Usage: bluewolf 00:11:22:33:44:55 [11:22:33:44:55:66]...

Depending on your bluetooth hardware you may be limited on the number of simultaneous connections (<7)

TODO: Add ability to assign BT device. Currently takes default kernel bluetooth device

TODO: Some devices will not respond to pings from non-conneced devices. We should fall back to bluetooth pairing broadcasts to determine
RSSI in these cases.

