## 1.���ж���ϰ汾docker
```
apt-get remove docker docker-engine docker.io containerd runc
```
## 2.���������
```
sudo apt update
sudo apt upgrade
```
## 3.��װdocker����
```
apt-get install ca-certificates curl gnupg lsb-release
```
## 4.���Docker�ٷ�GPG��Կ
```
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
```

## 5.���Docker���Դ
```
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
```
## 6.��װdocker
```
apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

## 7.����docker
```
systemctl start docker
systemctl status docker
```

## 8.�鿴docker�İ汾
```
sudo docker version
```

## 9.����helloworld
```
sudo docker run hello-world
```

## 10.�鿴docker-compose�汾
```
https://github.com/docker/compose/releases
```

## 11.��װdocker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

## 12.��װdocker-compose
```
sudo chmod +x /usr/local/bin/docker-compose
```

## 13.�鿴docker-compose�İ汾
```
docker-compose version
```









