
##烧写mmc
1、可以用Rufus软件将下载的IMG写入到一个空白的U盘，一定要使用DD模式
2、 插入R86S，开机按F7选择U盘启动
3、启动后直接激活控制台。开始写入命令。
4、输入
dd if=/dev/sda of=/dev/mmcblk0 bs=1M count=600 然后回车确定(不要忽略空格)
4.1这个地方的count=600 需要根据img大小来定。如果是500多M那就600，600多M那就700
5、上面完成后还需要修复分区表。fdisk /dev/mmcblk0 然后会显示红字。 然后w 回车退出就好了。
6、安装完成。必须要拔掉之前的U盘。否则可能配置会写错磁盘。



## 修改IP配置




opkg update
opkg remove luci-app-openclash
uname -m
opkg print-architecture

下载内核更新包，在官网的包库中找到内核更新包，连接：https://downloads.openwrt.org/snapshots/targets/x86/64/packages/

kernel_5.15.77-1-a8f70ac7e23248637deb1b31a7a117aa_x86_64.ipk

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

安装openclash里的版本更新，一共三个：
clash 
tun
meta
可以在线装，如果连不上，可以去github下载包，分别解压为
/etc/openclash/core/clash
/etc/openclash/core/clash_tun
/etc/openclash/core/clash_meta
即可自动识别更新

chmod 777 * /etc/openclash/core/
然后上传yaml配置文件，即可上网。


#给还需要把lan口的dhcp,默认网关和dns都设置好，才行。