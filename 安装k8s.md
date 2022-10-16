## 树莓派增加,开启cgroup的memory，其他系统可以用cat /proc/cgroups查看下，开启了就不用了
```
vim /boot/cmdline.txt
增加cgroup_enable=memory cgroup_memory=1在文件首部，变成这样
cgroup_enable=memory cgroup_memory=1 net.ifnames=0 dwc_otg.lpm_enable=0 console=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
开启cgroups的memory
查看
cat /proc/cgroups
开启了
```

## docker pull 错误，有可能只是没有这个镜像
```
Error response from daemon: pull access denied for helloworld, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
```


## 随便找一个节点，安装镜像仓库
> 运行仓库，registry_config.yml很重要，否则web界面无法访问仓库
```
docker run -d \
    --name registry \
    --restart=unless-stopped \
    -p 5000:5000 \
    -v /data/docker-registry/registry_config.yml:/etc/docker/registry/config.yml \
    -v /data/docker-registry:/var/lib/registry \
    registry:2.8.1
```

> 修改http访问（集群中的每一个机器都要搞）
```
vim /etc/docker/daemon.json
增加
"insecure-registries": ["http://dockerhub.kubekey.local:5000"]

systemctl daemon-reload
systemctl restart docker
```

> 增加registry的web界面
```
docker pull joxit/docker-registry-ui:2.3.2-debian

docker run -d --name registry-web -e REGISTRY_URL=http://10.0.0.135:5000 -e DELETE_IMAGES=true --restart=unless-stopped -p 5050:80 joxit/docker-registry-ui:2.3.2-debian
```


> 仓库操作
```
docker tag registry:2.8.1 dockerhub.kubekey.local:5000/registry:2.8.1 #标记镜像
docker push dockerhub.kubekey.local:5000/registry:2.8.1 #推送镜像
curl http://10.0.0.135:5000/v2/_catalog    #查看仓库中有哪些镜像
``` 
> 



## 开始搞集群
> 这个是要代理才搞，否则不用
export http_proxy=http://10.0.0.121:7890/
上面下面2选1，都行
export KKZONE=cn

> 安装 kk工具
dpkg -i kubekey-v2.3.0-rc.3-linux-arm64.deb

> 

> 在有网络的机器上搞，编辑manifest.yaml文件，下载需要用的东西，**假如有3个及以上的主节点，则需要开启本地负载均衡，并且使用haproxy，此时manifest就需要开启均衡和 haproxy**
kk artifact export -m manifest.yaml -o kubecluster.tar.gz


## 管理集群
> 创建集群，并且安装操作系统依赖（需要artifact中包含目标集群中节点的操作系统依赖文件）。
```
kk create cluster -f config-sample.yaml -a kubecluster.tar.gz

```

## 如果要使用lens ,把集群配置添加到lens，**注意 需要将server的内容改成ip,或者在lens本地添加域名ip映射**
```
kubectl config view --minify --raw
```


> 添加节点。
```
kk add nodes -f config-sample.yaml -a kubekey-artifact.tar.gz
```
> 升级集群
```
kk upgrade -f config-sample.yaml -a kubekey-artifact.tar.gz
```



## 异常记录
### 竟然重新下载helm 
```
downloading arm64 helm v3.9.0 ...
```