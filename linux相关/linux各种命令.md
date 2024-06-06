## 修改ssh端口
```
vim /usr/lib/systemd/system/ssh.socket
systemctl daemon-reload
systemctl restart sshd
systemctl restart sshd
ss -nulpt
```

## 查看dns
```
resolvectl status | grep -i "DNS Serve"
```

## 释放53端口
```
systemctl stop systemd-resolved
vim /etc/systemd/resolved.conf,DNS=8.8.8.8  #取消注释，增加dns,DNSStubListener=no  #取消注释，把yes改为no
ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf
```

## 将本地监听的dns ，127.0.0.53,去掉，使得域名指向dhcp指定的服务器
```
sudo sed -i 's/#DNSStubListener=.*/DNSStubListener=no/' /etc/systemd/resolved.conf && sudo systemctl restart systemd-resolved
```

##  dial tcp: lookup registry-1.docker.io on 127.0.0.53:53: read udp
/etc/resolv.conf
nameserver 8.8.8.8
nameserver 8.8.4.4

sudo systemctl daemon-reload
sudo systemctl restart docker

##  systemd-journal [301]: failed to write entry  XXXX  ignoring: Read-only file system
1.进入recover模式
2.修改/etc/default/grub 中 GRUB_CMDLINE_LINUX_DEFAULT变量
3.增加fsck.mode=force fsck.repair=yes
4.update-grub
5.reboot


## 删除所有exited状态的容器
```
docker rm $(docker ps -a -q -f status=exited)
```


## apt时候显示lock
```
E: Could not get lock /var/lib/apt/lists/lock. It is held by process 1898760 (apt-get)
sudo fuser -vik -TERM /var/lib/apt/lists/lock
```

## apt更新必要工具
apt install -y curl vim wireshark sockperf fio hdparm sdparm netcat net-tools kazam openssh-server htop ntpdate chrony tree nmap  git python3-pip wget tftp tmux filezilla ufw




## apt更新python
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.12
```

## apt安装ansible 
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

## 代理
export http_proxy=http://10.0.0.12:7890
export https_proxy=http://10.0.0.12:7890


## docker加速
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
    "registry-mirrors": [
        "https://dockerproxy.com",
        "https://docker.mirrors.ustc.edu.cn",
        "https://docker.nju.edu.cn"
    ]
}
