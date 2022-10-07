	1. kubectl api-resources 可以看当前支持的资源
	2. 生成yaml：kubectl create deployment redisserver --image=redis -o yaml --dry-run > xxxxxxxxxxxxxxx.yaml
	3. 或者从现有pod复制一个，kubectl get deployments XXXXXX -o=yaml > XXXXX.yaml
	4. 通过kubectl edit svc xxxx 可以修改service的运行yaml文件，可以实时修改
	5. Kubectl get deploy --namespace=XXXX获取某个非默认命名空间下的部署；
	6. Kubectl edit deploy --namespace=XXXX YYYYY编辑镜像
	7. 也可以通过kubectl patch XXX修改镜像
	8. 证书有效期：
      	1. cd /etc/kubernetes/pki
      	2. openssl x509 -in apiserver.crt -text -noout | grep Not
	9. Kubectl explain svc可以给出service的字段解释
	10. Kubectl explain svc.spec可以给出service中spec的字段解释
	11. Kubectl get ns 获取所有命名空间；
	12. kubectl get po XXXX yaml 查看XXX的yaml文件
	13. 通过 Kubectl explain XXX,xxx填写资源，来确定某种资源的apiVersion应该写什么，不是随便写的。
	14. 可以查看pods监听了哪些端口，就是kubectl exe XXXX -- ntestat -tnl 就是在pods内执行命令行，注意，命令行是两个-线，且两个杠前后有空格
	15. kubeadm安装的集群，1.6 版本以上的都默认开启了RBAC，查看是否开启了RBAC授权：cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep authorization-mode
	16. helm search hub wordpress，在官方仓库查找wordpress的chart
	17. 查看命名空间下所有资源：kubectl get all -n xxxxxx
	18. 删除命名空间下所有资源：kubectl delete all --all -n XXXX
	19. 查看客户端kubectl和服务端版本kubectl version
	20. 检查pod输出，kubectl logs
	21. 设置Host文件：echo "10.0.0.241 master-node" >> /etc/hosts
	22. 重新获取加入命令 kubeadm token create --print-join-command 。
	23. 查看网卡，ip a
	24. Kubectl top nodes 可以查看节点资源占用情况；
	25. Kubectl top pod -A可以查看po占用多少资源
	26. 向文件追加：cat << KK >>test.sh
	27. 向文件覆盖：cat << DD >test.sh
	28. houst文件立即生效。sudo /etc/init.d/networking restart
	29. Vim
    	1.  /etc/vim/vimrc,在行尾加上set number，永久显示行号
    	2.  删除光标至本行开头：d0
    	3.  删除光标至本行结尾：D
	30. 更改root密码：sudo passwd
	31. docker load -i xxxxx.tgz加载chart对应的离线镜像
	32. find / -name docker.service -type f 查找文件位置
	33. docker ps -a | grep xxxxx查看已创建的容器，无论是否运行。
	34. docker image inspect (docker image名称):latest|grep -i version 查看latest镜像版本
	35. systemctl status docker
	36. journalctl -xe
	37. journalctl -xefu kubelet
	38. 强制删除pod的办法：kubectl delete pods <pod> --grace-period=0 --force
	39. 替换某个目录下所有文件中某个单词
	40. sed -i "s/要查找的文本/替换后的文本/g" `grep -rl "要查找的文本" ./`
	41. 统计当前目录下文件的个数（不包括目录）: ls -l  | grep "^-" | wc -l
	42. 统计当前目录下文件的个数（包括子目录）: ls -lR | grep "^-" | wc -l
	43. 查看某目录下文件夹(目录)的个数（包括子目录）: ls -lR | grep "^d" | wc -l
	44. Wc 计算行数，单词数，字符数
	45. lsb_release -a 查看linux 的版本及发布代码（动物名字），使用的源，要用本系统发布版本号对应的源头；
	46. Traceroute 查看数据包到目的IP走过的路径，-n 直接显示IP，不解析为域名，可以减少域名解析时间；
	47. github下载文件，用raw模式打开文件，然后wget 链接就行；
	48. 所有镜像都打包
    	1.  docker save $(docker images |grep-v REPOSITORY |awk'BEGIN{OFS=":";ORS=" "}{print $1,$2}') -o iammages.tar
    	2.  docker load -i haha.tar
	49. 保存镜像
	    ```
	    #!/bin/sh
	    sum=` docker image list |wc -l`
	    COUNT=`expr $sum - 1`
	    echo 镜像数量：$COUNT
	    TAG=`docker image list|grep -v REPOSITORY|awk '{print $1":" $2}'|awk 'ORS=NR%"'$COUNT'"?" ":"\n"{print}'`
	    echo TAG值：$TAG
	    docker save $TAG -o images.tar
	    ```
  	50 linux 的抓包 tcpdump udp port 18290 -XX -vvv -nn
		-v：当分析和打印的时候，产生详细的输出。
		-vv：产生比-v更详细的输出。
		-vvv：产生比-vv更详细的输出。
		-XX：输出包的头部数据，会以16进制和ASCII两种方式同时输出。
		-nn ：直接以IP以及PORT number显示，而非主机名与服务名称
	51 lsof
		lsof -i:8080：查看8080端口占用
		lsof abc.txt：显示开启文件abc.txt的进程
		lsof -c abc：显示abc进程现在打开的文件
		lsof -c -p 1234：列出进程号为1234的进程所打开的文件
		lsof -g gid：显示归属gid的进程情况
		lsof +d /usr/local/：显示目录下被进程开启的文件
		lsof +D /usr/local/：同上，但是会搜索目录下的目录，时间较长
		lsof -d 4：显示使用fd为4的进程
		lsof -i -U：显示所有打开的端口和UNIX domain文件
	52 通过UDP向指定IP（10.0.0.102）端口（1234）发送数据：echo “hello” > /dev/udp/10.0.0.102/1234
        53.下载github 文件夹，直接复制文件夹地址到 https://minhaskamal.github.io/DownGit/#/home?url=https:%2F%2Fgithub.com%2Ffeathericons%2Ffeather%2Ftree%2Fmaster%2Ficons
   	54只下载，不安装 apt-get install --download-only  XXXXX，存放在 下载包存放路径：/var/cache/apt/archives/
	55.阻止apt清理缓存的方法是：echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/01keep-debs
    53.下载github 文件夹，直接复制文件夹地址到 https://minhaskamal.github.io/DownGit/#/home?url=https:%2F%2Fgithub.com%2Ffeathericons%2Ffeather%2Ftree%2Fmaster%2Ficons
    54只下载，不安装 apt-get install --download-only  XXXXX，存放在 下载包存放路径：/var/cache/apt/archives/
    55.阻止apt清理缓存的方法是：echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/01keep-debs
    56.linux查看做了硬件raid的物理信息，通过megacli命令看比如：MegaCli -PDList -aAll 
    57.麒麟系统，查看操作系统是sp几，cat /etc/*release，应该是cat /etc/.kylin
    58.麒麟4.0.2-arm架构源地址：http://archive.kylinos.cn/kylin/KYLIN-ALL
    59.麒麟v10地址，arm架构：http://archive2.kylinos.cn/rpm/kylin/Library/custom/kylin-server/KY10-GFB-aarch64/
    60.tcpdump -i eth0 -nnvv -c 10 '((udp) and (port 1234) and ((src host 200.200.200.1) and (dst host 200.200.200.2)))'
    61.tcpdump -i eth0 -nntvv -c 10 '((tcp) and (port 22) and ((dst host 200.200.200.1) or (dst host 200.200.200.2)))'
    62.netstat -nap查看哪些端口被哪些程序占用
    63.查看本机架构：uname -m
    64. rsync -aozghpP source dst
	    *****************************************************************************************
	一般最常用的选项组合：-avzP 来进行传输,

	rsync的同步参数选项：
	-a ：归档模式，表示以递归模式传输文件，并保持文件所有属性相当于-rtopgdl
	-v :详细模式输出，传输时的进度等信息
	-z :传输时进行压缩以提高效率—compress-level=num可按级别压缩
	-r :对子目录以递归模式，即目录下的所有目录都同样传输。
	-t :保持文件的时间信息—time
	-o ：保持文件属主信息owner
	-p ：保持文件权限
	-g ：保持文件的属组信息
	-P :--progress 显示同步的过程及传输时的进度等信息
	-e ：使用的信道协议，指定替代rsh的shell程序。例如：ssh
	-D :保持设备文件信息
	-l ：--links 保留软连接
	--progress  :显示备份过程
	--delete    :删除那些DST中SRC没有的文件
	--exclude=PATTERN 　指定排除不需要传输的文件模式
	-u, --update 仅仅进行更新，也就是跳过所有已经存在于DST，并且文件时间晚于要备份的文件。(不覆盖更新的文件)
	-b, --backup 创建备份，也就是对于目的已经存在有同样的文件名时，将老的文件重新命名为~filename。
	-suffix=SUFFIX 定义备份文件前缀
	-stats 给出某些文件的传输状态
	-R, --relative 使用相对路径信息  如：rsync foo/bar/foo.c remote:/tmp/   则在/tmp目录下创建foo.c文件，而如果使用-R参数：rsync -R foo/bar/foo.c remote:/tmp/     则会创建文件/tmp/foo/bar/foo.c，也就是会保持完全路径信息。
	--config=FILE 指定其他的配置文件，不使用默认的rsyncd.conf文件
	--port=PORT 指定其他的rsync服务端口
    65. 代理下载：export http_proxy=http://proxyAddress:port
    66.dpkg -i --print-architecture 
	67.查看库中软件版本apt show package_name
	68.docker 拉取指定架构镜像docker pull --platform=<plartform> <image-name>:<tag>
