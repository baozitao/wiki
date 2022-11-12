## 安装k8s

## 关闭交换分区
```
swapoff -a
cp -p /etc/fstab /etc/fstab.bak$(date '+%Y%m%d%H%M%S')
sed -i "s/\/dev\/mapper\/centos-swap/\#\/dev\/mapper\/centos-swap/g" /etc/fstab
systemctl daemon-reload
systemctl restart kubelet
```


## 关闭防火墙
```
ufw disable
ufw status
```


>关闭selinux
>设置时间，三个机器同步，
>设置所有流量均通过三层转发；

```
cat > /etc/sysctl.d/k8s.conf << EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
```


>改主机名
```
hostnamectl set-hostname master
timedatectl set-timezone Asia/Shanghai
sudo modprobe br_netfilter
lsmod | grep br_netfilter
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
systemctl enable docker
systemctl start docker
sudo apt-get install -y apt-transport-https ca-certificates curl
```


> 更新 apt 包索引并安装使用 Kubernetes apt 仓库所需要的包
```
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
```


## 上面的步骤可以改为国内源
```
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add - 
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF
apt-get update
```



## 如果update 失败
```
添加源之后，使用 apt-get update 命令会出现错误，原因是缺少相应的key，可以通过下面命令添加(E084DAB9 为上面报错的key后8位)。
gpg --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 
gpg --export --armor E084DAB9 | sudo apt-key add -
```



## 可以看看版本号
```
查看最新版本
apt show kubelet
apt show kubeadm
apt show kubectl

查看有多少个版本
apt-cache madison kubelet


apt-get install -y kubelet=${K8S_VERSION} kubeadm=${K8S_VERSION} kubectl=${K8S_VERSION}
export K8S_VERSION=1.23.5-00
apt-get install kubelet=${K8S_VERSION} 
apt-get install kubeadm=${K8S_VERSION} 
apt-get install kubectl=${K8S_VERSION}
sudo apt-mark hold kubelet kubeadm kubectl
```


  

## 配置 Docker daemon，设置cgroupdriver为systemd
```
vim /etc/docker/daemon.json

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
```


## 重启 docker 后台服务

sudo systemctl daemon-reload
sudo systemctl restart docker

## 启动kubelet，并设置开机自启动

systemctl restart kubelet

## 下载k8s镜像

### 方法一：通过k8s配置文件修改，拉取
>查看需要哪些镜像
```
kubeadm config images list
```

>修改拉取镜像的仓库
```
kubeadm config print init-defaults > kubeadm.conf

## 修改
vim kubeadm.conf

## 内容
修改 imageRepository: k8s.gcr.io 为 registry.cn-beijing.aliyuncs.com/imcto
imageRepository: registry.cn-beijing.aliyuncs.com
# 修改kubernetes版本kubernetesVersion: v1.23.0
# 改为kubernetesVersion: v1.23.0
kubernetesVersion: v1.23.0
```

>看看修改成功没有
```
kubeadm config images list --config kubeadm.conf


##输出应该是这样
registry.cn-beijing.aliyuncs.com/imcto/kube-apiserver:v1.13.1
registry.cn-beijing.aliyuncs.com/imcto/kube-controller-manager:v1.13.1
registry.cn-beijing.aliyuncs.com/imcto/kube-scheduler:v1.13.1
registry.cn-beijing.aliyuncs.com/imcto/kube-proxy:v1.13.1
registry.cn-beijing.aliyuncs.com/imcto/pause:3.1
registry.cn-beijing.aliyuncs.com/imcto/etcd:3.2.24
registry.cn-beijing.aliyuncs.com/imcto/coredns:1.2.6
```

>拉取镜像
```
kubeadm config images pull --config kubeadm.conf
```


###  方法二：通过脚本文件拉取

>运行以下命令，获取对应的版本号
```
kubeadm config images list
```


使用kubeadm config images pull可以直接拉取所需镜像。
kubeadm config images list and kubeadm config images pull 
can be used to list and pull the images that kubeadm requires.

搞文件：sudo tee ./images.sh <<-'EOF'

文件内容：

#!/bin/bash
images=(
    k8s.gcr.io/kube-apiserver:v1.23.5
    k8s.gcr.io/kube-controller-manager:v1.23.5
    k8s.gcr.io/kube-scheduler:v1.23.5
    k8s.gcr.io/kube-proxy:v1.23.5
    k8s.gcr.io/pause:3.6
    k8s.gcr.io/etcd:3.5.1-0
    k8s.gcr.io/coredns/coredns:v1.8.6
)

for imageName in ${images[@]} ; do
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
done
EOF

chmod +x ./images.sh && ./images.sh
```



或者直接：
docker pull k8s.gcr.io/kube-apiserver:v1.23.5
docker pull k8s.gcr.io/kube-controller-manager:v1.23.5
docker pull k8s.gcr.io/kube-scheduler:v1.23.5
docker pull k8s.gcr.io/kube-proxy:v1.23.5
docker pull k8s.gcr.io/pause:3.6
docker pull k8s.gcr.io/etcd:3.5.1-0
docker pull k8s.gcr.io/coredns/coredns:v1.8.6

docker save $(docker images | grep -v REPOSITORY | awk 'BEGIN{OFS=":";ORS=" "}{print $1,$2}') -o haha.tar

## 各个节点设置主机名

## 19.初始化集群,在主节点执行：

  

### 可以通过配置文件初始化集群

kubeadm init --config kubeadm.conf

  

  

### 可以自己手动初始化

打印kubeadm init时的默认配置信息
kubeadm config print init-defaults

kubeadm init \
--apiserver-advertise-address=10.0.0.107 \
--image-repository registry.aliyuncs.com/google_containers \
--control-plane-endpoint=10.0.0.107 \
--kubernetes-version v1.23.5 \
--service-cidr=10.96.0.0/16 \
--pod-network-cidr=10.244.0.0/16\

  

  

## 20.要使非 root 用户可以运行 kubectl，请运行以下命令，分两种情况，

①假如你目前不是root，则执行以下命令
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

②假如你目前是root，则
	export KUBECONFIG=/etc/kubernetes/admin.conf
③或者
	echo "export KUBECONFIG=/etc/kubernetes/admin.conf" >> ~/.bash_profile
	source ~/.bash_profile

## 安装网络插件

#flannel的网络设置要与init里的pod网络设置一致，否则后面能ready但是不能通信。
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml



flannel
需要在kubeadm init 时设置 --pod-network-cidr=10.244.0.0/16，
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/v0.10.0/Documentation/kube-flannel.yml

calico
 kubeadm init 时设置 --pod-network-cidr=192.168.0.0/16
kubectl apply -f https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/rbac-kdd.yaml
kubectl apply -f https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml 

## 去除master的污点，单节点，设置master节点也可以运行Pod

kubernetes官方默认策略是worker节点运行Pod，master节点不运行Pod。如果只是为了开发或者其他目的而需要部署单节点集群，可以通过以下的命令设置：
kubectl taint nodes --all node-role.kubernetes.io/master-

## 部署其他插件

由于很多官方的插件所需镜像也在 http://gcr.io 上，所以遇到这种情况，可以通过下面的方式获取：
将yaml文件中镜像地址的k8s.gcr.io替换成registry.cn-hangzhou.aliyuncs.com/google_containers
查看是否安装成功
kubectl get pods -n kube-system
如果出现类似下面的情况就说明安装完成了，接下来就可以开始k8s之旅了。

### 设置所有主节点污点取消

kubectl taint nodes --all node-role.kubernetes.io/master-

  

  

## 查看flennel网络配置

cat /run/flannel/subnet.env

## 加入主节点

打印join默认信息
kubeadm config print join-defaults

kubeadm join 10.0.0.241:6443 --token q6tmo4.rp3ehpf4pp12ce47 \
        --discovery-token-ca-cert-hash sha256:56f96e713636b4b5c5759a788ba15c6cedaf5fc58d4f8174f5864856d39fd4ed \
        --control-plane

## 在各个Node加入集群

忘记了可以重新生成
kubeadm token create --print-join-command --ttl 0 

kubeadm join 10.0.0.241:6443 --token q6tmo4.rp3ehpf4pp12ce47 \
        --discovery-token-ca-cert-hash sha256:56f96e713636b4b5c5759a788ba15c6cedaf5fc58d4f8174f5864856d39fd4ed

## 修改kube-apiserver.yaml文件，加入链接；

vim /etc/kubernetes/manifests/kube-apiserver.yaml
- --feature-gates=RemoveSelfLink=false

## kubectl completion bash用于生成自动补全脚本；

source <(kubectl completion bash)                                       
echo "source <(kubectl completion bash)" >> ~/.bashrc