
opkg update
opkg remove luci-app-openclash
uname -m
opkg print-architecture

下载内核更新包，在官网的包库中找到内核更新包，连接：https://downloads.openwrt.org/snapshots/targets/x86/64/packages/

更新内核
opkg install kernel_5.15.77-1-a8f70ac7e23248637deb1b31a7a117aa_x86_64.ipk--force-overwrite

安装openclash依赖
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