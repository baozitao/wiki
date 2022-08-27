Ubuntu 系统搭建方法
现在介绍 Ubuntu 系统搭建离线软件源的方法，但该方法也适用于 Debian、Deepin 等发行版。我实际操作使用的是基于 Ubuntu 的发行版 elementary OS Loki 0.4.1 或 elementary OS Juno 5.0。目前 elementary OS 和 Ubuntu 非常相近，配置过程可以相互参考。

获取所需程序包
Ubuntu 系统的安装光盘仅包含很少量的程序包，这些程序包位于光盘的 /pool 文件夹内。但 Ubuntu 有一个特性：安装或更新过的程序，其安装包会缓存在 /var/cache/apt/archives 目录下。如果你还有一台能够联网的 Ubuntu 系统计算机（可使用虚拟机代替），并且你要安装的程序已经包含在网络上的软件源内，你可以利用这个特性来方便地获取所需的程序安装包。在 Ubuntu 操作系统上，你可以使用如下命令通过软件源下载程序：

1
$ apt-get -d install <software>
这个命令中的 <software> 代表你要安装的程序名。该命令将下载你需要的程序及其所需要的依赖程序的安装包，将其放在 /var/cache/apt/archives 目录下。拷贝该目录下的所有文件即可获取到所需的安装包了。

为 Ubuntu 制作离线软件源需要使用一个程序 “dpkg-dev”，Ubuntu 系统默认通常不会安装它（elementary OS Loki 0.4.1 中已经安装了）。但是其安装方法非常简单，只需要在联网的计算机上执行：

1
$ sudo apt-get install dpkg-dev
创建本地软件源
在联网的计算机上，将你准备好的程序包拷贝到某个文件夹下，例如 /mnt/localpacks，我们将为该文件夹内的所有安装包创建索引以作为本地的软件源。在终端中执行以下命令来创建索引：

1
2
cd /mnt/localpacks
dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz
程序扫描所有的软件包后，将会在 /mnt/localpacks 目录中生成一个名为 Packages.gz 的文件，存放这个文件夹中的软件包的信息及其依赖关系。

现在这个文件夹就可以作为一个离线的软件仓库来使用了。你可以利用这个文件夹直接为本机创建离线的软件源，当然也可以将其拷贝到其它的计算机上使用。

应用配置
要应用上文生成的文件夹作为离线软件源，需要编辑文件 /etc/apt/sources.list，该文件保存了 Ubuntu 操作系统可用的软件源列表。编辑前切记备份以前的文件：

1
$ cp /etc/apt/sources.list /etc/apt/sources.list.bak
然后编辑 /etc/apt/sources.list，添加离线软件仓库的目录，此处依然假设离线软件源位于 /mnt/localpacks 文件夹。如果你使用的是 Ubuntu 16.04 LTS，在 sources.list 文件中添加以下内容：

1
deb file:/mnt/localpacks ./
在较新的操作系统版本中（如 Ubuntu 18.04 LTS），系统默认将拒绝使用未认证过的软件源。因此在配置 sources.list 文件时，需要同时设置对我们搭建的软件源不做安全校验：

1
deb [ allow-insecure=yes ] file:/mnt/localpacks ./
保存，退出。最后，更新系统软件源以应用配置：

1
$ apt-get update
至此，离线软件源配置完成，你可以安装程序试试了。比如安装 dos2unix 程序：

1
$ apt-get install dos2unix
