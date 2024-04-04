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
