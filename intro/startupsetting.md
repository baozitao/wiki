# start set
```
echo root:99131456 | sudo chpasswd
su
99131456
timedatectl  set-timezone Asia/Shanghai
perl -pi -e 's/(.*(?=ssh-rsa))//g' /root/.ssh/authorized_keys
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
service sshd restart
```