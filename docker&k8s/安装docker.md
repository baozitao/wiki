## 1.检查卸载老版本docker
```
apt-get remove docker docker-engine docker.io containerd runc
```
## 2.更新软件包
```
sudo apt update
sudo apt upgrade
```
## 3.安装docker依赖
```
apt-get install ca-certificates curl gnupg lsb-release
```
## 4.添加Docker官方GPG密钥
```
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
```

## 5.添加Docker软件源
```
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
```
## 6.安装docker
```
apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

## 7.运行docker
```
systemctl start docker
systemctl status docker
```

## 8.查看docker的版本
```
sudo docker version
```

## 9.运行helloworld
```
sudo docker run hello-world
```

## 10.查看docker-compose版本
```
https://github.com/docker/compose/releases
```

## 11.安装docker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

## 12.安装docker-compose
```
sudo chmod +x /usr/local/bin/docker-compose
```

## 13.查看docker-compose的版本
```
docker-compose version
```









