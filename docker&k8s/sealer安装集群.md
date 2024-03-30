# sealer 安装集群操作步骤
## 访问外网
> 设置代理
```
cat >> /etc/profile << EOF
export  http_proxy="http://10.0.0.121:7890/"
EOF
```
> 代理生效
```
source     /etc/profile   
```


## 下载安装sealer
```
wget https://github.com/sealerio/sealer/releases/download/v0.8.6/sealer-v0.8.6-linux-arm64.tar.gz && \
tar zxvf sealer-v0.8.6-linux-arm64.tar.gz && mv sealer /usr/bin
```

## 启动集群
```
sealer run kubernetes:v1.22.5 \
  --masters 10.0.0.135,10.0.0.140 \
  --nodes 10.0.0.103,10.0.0.108,10.0.0.112 --passwd bao99131456tao
```