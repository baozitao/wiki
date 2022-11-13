
opkg update
opkg remove luci-app-openclash
uname -m
opkg print-architecture


更新内核

opkg install coreutils-nohup --force-overwrite
opkg install bash --force-overwrite
opkg install iptables --force-overwrite
opkg install dnsmasq-full --force-overwrite
opkg install curl --force-overwrite
opkg install ca-certificates --force-overwrite
opkg install ipset --force-overwrite
opkg install ip-full --force-overwrite
opkg install iptables-mod-tproxy --force-overwrite
opkg install iptables-mod-extra --force-overwrite
opkg install libcap --force-overwrite
opkg install libcap-bin --force-overwrite
opkg install ruby --force-overwrite
opkg install ruby-yaml --force-overwrite
opkg install kmod-tun --force-overwrite

安装openclash
opkg install luci-app-openclash_0.45.70-beta_all.ipk
--force-overwrite