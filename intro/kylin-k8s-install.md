---
title: kylin-k8s-install
description: 
published: true
date: 2022-04-05T14:46:27.680Z
tags: 
editor: markdown
dateCreated: 2022-04-02T15:16:10.846Z
---

# 04.kylin-k8s-install

### 关闭交换分区 ,`注释掉最后swap这一行`
```
vim /etc/fstab
```

### 设置时间同步

```
timedatectl set-timezone Asia/Shanghai
```

### 设置机器名

```
hostnamectl set-hostname master
hostname newname
```

### 设置本机解析名
将127.0.0.1映射为/etc/hostname中的名字
```
vim /etc/hosts
```


### 关闭过滤

```
sudo modprobe br_netfilter
lsmod | grep br_netfilter
```

### 关闭selinux

```
cat > /etc/sysctl.d/k8s.conf << EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
```
### 修改源
```
echo "deb http://archive.kylinos.cn/kylin/KYLIN-ALL 4.0.2sp2-server main restricted universe multiverse" | sudo tee /etc/apt/sources.list > /dev/null
```

### 安装docker
查看[安装docker](/intro/dockerinstall)
或者直接在线安装
```
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

### 配置 Docker daemon，设置cgroupdriver为systemd

```
cat << EOF | sudo tee /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2",
  "insecure-registries": ["10.0.0.231:8082","10.0.0.231:8083"],
  "registry-mirrors": ["http://10.0.0.231:8083"]
}
EOF
```

### 重启 docker 后台服务

```
sudo systemctl daemon-reload
sudo systemctl enable docker
sudo systemctl restart docker
sudo systemctl status docker
```

### 导入kubeadm 相关镜像 ，images

获取所需版本号
```
kubeadm config images list
```
生成文件
```
cat << EOF | sudo tee /home/images.sh
#!/bin/bash
images=(
    kube-apiserver:v1.23.5
    kube-controller-manager:v1.23.5
    kube-scheduler:v1.23.5
    kube-proxy:v1.23.5
    pause:3.6
    etcd:3.5.1-0
    coredns:v1.8.6
)

for imageName in ${images[@]} ; do
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
done
EOF
```
```
chmod +x /home/images.sh && ./home/images.sh
```

### kubeadm、kubelet、kubectl的安装

> 方法一：可以使用离线导入的方式

```
dpkg -i xxxx.deb
```

> 方法二：添加阿里云镜像源

```
apt-get update
echo y | apt-get install apt-transport-https  curl ca-certificates curl gnupg lsb-release 
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add - 
cat << EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF
apt-get update
apt-cache show kubeadm | grep Version
```

> 方法三：添加官方仓库源

```
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
apt-cache show kubeadm | grep Version
```

> 然后可使用所需的版本号直接安装

```
export K8S_VERSION=1.23.5-00
echo y | apt-get install kubelet=${K8S_VERSION} 
echo y | apt-get install kubeadm=${K8S_VERSION} 
echo y | apt-get install kubectl=${K8S_VERSION}
sudo apt-mark hold kubelet kubeadm kubectl
```

### 重启 kubelet 后台服务

```
sudo systemctl daemon-reload
sudo systemctl enable kubelet
sudo systemctl restart kubelet
sudo systemctl status kubelet
```

### 初始化集群,在主节点执行

```
kubeadm init \
--apiserver-advertise-address=10.0.0.121 \
--image-repository registry.aliyuncs.com/google_containers \
--control-plane-endpoint=10.0.0.121 \
--kubernetes-version v1.23.5 \
--service-cidr=10.96.0.0/16 \
--pod-network-cidr=10.244.0.0/16
```

### 安装网络插件

```
##flannel的网络设置要与init里的pod网络设置一致，否则后面能ready但是不能通信。
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

### 查看flennel网络配置

```
cat /run/flannel/subnet.env
```

### coreDns出错

> 日志

```
Forwarding loop detected in "." zone. Exiting. See https://coredns.io/plugins/loop##troubleshooting
```

> 则执行

```
1.kubectl edit cm coredns -n kube-system
2.delete ‘loop’ , save and exit
3.kubctel delete pod xxxxx -n kube-system
```

### 加入节点

> 复制加入节点

### 要使非 root 用户可以运行 kubectl，请运行以下命令，分两种情况

> 假如你目前不是root，则执行以下命令

```
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

> 假如你目前是root，则

```
	export KUBECONFIG=/etc/kubernetes/admin.conf
```

> 或者

```
	echo "export KUBECONFIG=/etc/kubernetes/admin.conf" >> ~/.bash_profile
	source ~/.bash_profile
```

### kubectl completion bash用于生成自动补全脚本

```
source <(kubectl completion bash)                                       
echo "source <(kubectl completion bash)" >> ~/.bashrc  
```
