
# ssh set


## ssh set
> frpc.ini set

```
vim /home/frp/frpc.ini
```
```
# frpc.ini
[common]
server_addr = 3year.baozitao.com
server_port = 7000

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6000
```

> **frps.ini set**

```
vim /home/frp/frps.ini
```
```
# frps.ini
[common]
bind_port = 7000
```


## auto.sh set
### `client` set auto.sh
add auto .sh
```
vim /home/frp/auto.sh
```
add content
```
#!/bin/bash
/home/frp/frpc -c /home/frp/frpc.ini
```
set permission
```
chmod 777 /home/frp/auto.sh
```
### `server` set auto.sh
add auto .sh
```
vim /home/frp/auto.sh
```
add content
```
#!/bin/bash
/home/frp/frps -c /home/frp/frps.ini
```
set permission
```
chmod 777 /home/frp/auto.sh
```

## same set  frp.service
systemd server add
```
vim /etc/systemd/system/frp.service
```
add content, para `ExecStart` must same with `auto.sh` path
```
[Unit]
Description=Run a Custom Script at Startup
ConditionFileIsExecutable=/home/frp/auto.sh
After=network-online.target firewalld.service

[Service]
ExecStart=/bin/sh /home/frp/auto.sh
Restart=always

[Install]
WantedBy=default.target
```

set permission
```
chmod 777 /etc/systemd/system/frp.service
```

set start
```
systemctl daemon-reload 
systemctl enable frp
systemctl start frp
systemctl status frp
```





















