## 服务端
docker run --restart=unless-stopped --network host -d -v /home/docker-frps/frps.ini:/etc/frp/frps.ini --name frps snowdreamtech/frps


### frps.ini文件内容
```
[common]
bind_port = 6666 
vhost_http_port = 8080
vhost_https_port = 443
```





## 客户端
docker run --restart=always --network host -d -v /data/frpc/frpc.ini:/etc/frp/frpc.ini --name frpc snowdreamtech/frpc

### frpc.ini文件内容
```
[common]
server_addr = 3year.baozitao.com 
server_port = 6666

[ssh-ubuntu]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 4001
```
