# Smartphone USB tethering



## Introduction
USB tethering is used to connect your OpenWrt Router to the Internet by using the your smartphone. It's more convenient and has better performance (lower latency) than turning your smartphone into an access point and using that. It also is less of a CPU load on your phone, charges your phone, and allows you the flexibility of doing things with your OpenWrt router that you cannot do with your phone like connecting multiple devices with ease, both wireless and wired, to each other and to the internet. In order to maximize performance, you should turn your tethered phone Wi-Fi and Bluetooth off.
- USB tethering is known to be problematic on iOS 14 devices. works without patch on latest trunk 01/2022, 21.02.1 needs patch
- Connecting your whole network to the Internet using the Smartphone might consume your monthly traffic quota very fast.
- Follow USB reverse tethering to share the internet from router to the smartphone over USB.

## 1. Installation
For the easiest installation, have a wired upstream internet connection to boot-strap this process. You will need: the router, your tethering phone, necessary cables, a laptop and an upstream internet connection via Ethernet for initial setup. Instead of a wired upstream connection to plug into the router WAN port, is also possible to download necessary packages below, through your laptop while tethered to your phone, the same way you can get the OpenWrt distribution for your router.
A common protocol for Android based devices for tethering via USB is RNDIS:
```openwrt cmd
opkg update
opkg install kmod-usb-net-rndis
```

However Android devices come with great diversity, therefor some require different protocols. For instance newer devices may use NCM, others may require EEM or even need a subset implementation.

**NOTE** : Try the following protocol(s) if you don't have a `usb0` interface come up or device keeps disconnecting:
```openwrt cmd
opkg install kmod-usb-net-cdc-ncm

# Huawei may need its own implementation!
opkg install kmod-usb-net-huawei-cdc-ncm

# More protocols:
kmod-usb-net-cdc-eem
kmod-usb-net-cdc-ether
kmod-usb-net-cdc-subset
```

<Right>Extra steps depending on USB type and drivers for your router:
```openwrt cmd
opkg update
opkg install kmod-nls-base kmod-usb-core kmod-usb-net kmod-usb-net-cdc-ether kmod-usb2
```

Additional steps for iOS devices:
```OpenWrt cmd 
opkg update
opkg install kmod-usb-net-ipheth usbmuxd libimobiledevice usbutils
 
# Call usbmuxd
usbmuxd -v
 
# Add usbmuxd to autostart
sed -i -e "\$i usbmuxd" /etc/rc.local
```
If you need to manually download the packages on another device for bootstrapping, see get_additional_software_packages. The Kernel modules will be in the URL of form downloads.openwrt.org/releases/[your release]/targets/[your target]/generic/packages/ and other packages (iOS stuff in this case) in downloads.openwrt.org/releases/[release]/packages/[instruction set]/packages/.



## 2. smartphone
Connect the smartphone to the USB port of the router with the USB cable, and then enable USB Tethering from the Android settings. Turn on the phone's Developer Options [Find the Build information in the About Phone menu, and tap rapidly 7 x]. There is a Default USB Configuration: USB Tethering option. The phone will now immediately turn on USB Tethering mode when plugged into a configured router [or laptop], without further commands. However, **it is necessary to remove the screen lock on the phone. A locked phone will not start USB Tethering by itself.** 

For iPhones, you may have to disable and re-enable the Personal Hotspot/Allow Others to Join setting on the iPhone to force the OpenWrt DHCP client to get an IP address from the eth1 iPhone interface. Disabling and re-enabling the Personal Hotspot/Allow Others to Join setting on the iPhone is also required if you disconnect the iPhone from the OpenWrt USB port and re-connect it later, unless you cache Trust records (see watchdog section and/or LeJeko's Github repository in reference section).

iPhones starting from iOS 11 will terminate the USB data connections after one hour by default to improve security. This can easily be changed via:

> iPhones starting from iOS 11 will terminate the USB data connections after one hour by default to improve security. This can easily be changed via:


## 3.a Command-line interface

On the router, enter:
```openwrt cmd
# Enable tethering
uci set network.wan.ifname="usb0"
uci set network.wan6.ifname="usb0"
uci commit network
/etc/init.d/network restart
```

> For iPhones, replace the interface name usb* with eth* depending on router.
It should be all working at this point. To activate wireless connections to the router, go to Network, Wireless and set then enable the interfaces.


## 3.b Web interfaces

Go to Network, Interfaces. You can either assign the existing WAN to usb0 like 3.a above, or create a whole new interface if you want to swap between the WAN Ethernet port and your tethering device (such as in a dual-wan fail-over situation). To make changes in the web interface equivalent to the above command line instructions: simply edit the existing default WAN interface, and change the physical device to usb0, then Save & Apply.

Instead, to create a whole new interface, make a new one called TetheringWAN, and bind to it the new *usb0* network device (restart if you do not see it yet. And, for some cases, the new interface may be called '*eth1*: check what the log is showing in your case). Set the protocol to DHCP client mode or DHCPv6 client mode if the ISP assigns IPv6, and under the Firewall Settings tab, place it into the WAN zone. Save changes.

See the following screenshots.


![First page of the Create Interface wizard.](https://openwrt.org/_media/docs/guide-user/advanced/image_create_new_interface.png) 
![Firewall tab of the Create Interface Wizard. Very important to set it as WAN.](https://openwrt.org/_media/docs/guide-user/advanced/image_create_new_interface_set_firewall_region.png) 
![](https://openwrt.org/_media/docs/guide-user/advanced/image_create_new_interface_end_result.png) 
And the end result in the Interfaces page.

After committing the changes the new TetheringWAN should be activated. Otherwise, restart it with the buttons you find in the Interface page of LuCI web interface.


## Troubleshooting

If all went well, you should be able to see something like the following in the kernel log

- click on Status and then on Kernel Log to see this log from the LuCi web interface
- or write “dmesg” in the console over SSH.
```openwrt cmd 
[  168.599245] usb 1-1: new high-speed USB device number 2 using orion-ehci
[  175.997290] usb 1-1: USB disconnect, device number 2
[  176.449246] usb 1-1: new high-speed USB device number 3 using orion-ehci
[  176.654650] rndis_host 1-1:1.0 usb0: register 'rndis_host' at usb-f1050000.ehci-1, RNDIS device, ee:da:c0:50:ff:44
```

Note how the last line tells us that this new “RNDIS device” was bound to interface **usb0**.
