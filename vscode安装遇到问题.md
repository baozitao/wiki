dpkg -i code_1.72.0-1664925838_arm64.deb
遇到问题
```
正在选中未选择的软件包 code。
(正在读取数据库 ... 系统当前共安装有 268648 个文件和目录。)
正准备解包 code_1.72.0-1664925838_arm64.deb  ...
正在解包 code (1.72.0-1664925838) ...
dpkg: 依赖关系问题使得 code 的配置工作不能继续：
 code 依赖于 libstdc++6 (>= 6)；然而：
系统中 libstdc++6:arm64 的版本为 5.4.0-6kord1~16.04.12。

dpkg: 处理软件包 code (--install)时出错：
 依赖关系问题 - 仍未被配置
正在处理用于 desktop-file-utils (0.22-1kord5) 的触发器 ...
正在处理用于 bamfdaemon (0.5.3~bzr0+16.04.20160415-0kord1) 的触发器 ...
Rebuilding /usr/share/applications/bamf-2.index...
正在处理用于 mime-support (3.59kord1) 的触发器 ...
正在处理用于 shared-mime-info (1.5-2kord) 的触发器 ...
Unknown media type in type 'all/all'
Unknown media type in type 'all/allfiles'
在处理时有错误发生：
 code
```

原因：
gcc g++版本太低，低于要求的libstdc++6 (>= 6)
主要是g++

查看版本
gcc -v 及 g++ -v

解决办法：下载（麒麟下可以换成ubuntu 18.04的源，因为16.04的源已经比较老了）
apt remove gcc
apt  remove g++

apt install gcc g++
