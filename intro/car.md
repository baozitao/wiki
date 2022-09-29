#  安装potainer
> 安装服务端
```
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

> 访问potainer
```
https://IP:9443
```

> 在其他需要一起被监控的机器上，编辑/usr/lib/systemd/system/docker.service,添加-H tcp://0.0.0.0:2375也就是添加成
```
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H fd:// --containerd=/run/containerd/containerd.sock
```

> 被监控机器重载配置，并重启

```
systemctl daemon-reload
systemctl restart docker
```
> 在主机网页上，选择setting ，在enviroment里选择api填写对应ip,进行监控


# 安装wgcloud及代理
> 1.server所在主机需要JDK1.8环境（JDK11也可以），OpenJDK1.8也可以的
```
java -version
```
> 2.启动mysql容器
```
1.创建数据库
2.MYSQL_ROOT_PASSWORD环境变量设置密码
3.创建端口3306
4.拷贝sql文件：docker cp /home/wgcloud-MySQL.sql container:/home/
5.设置时间与主机一致：-v /etc/localtime:/etc/localtime:ro
```

> 3.创建wgcloud数据库，并导入数据
```
1.登录进mysql容器
2.登录数据库：mysql -uroot -p
3.CREATE DATABASE wgcloud DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
4.show databases;
5.use wgcloud;
6.source /home/wgcloud-MySQL.sql;# 导入备份数据库
```

> 4.允许数据库允许root远程登录访问（因为容器也是一个主机，宿主机访问容器，也是外部访问，所以需要开启，除非运行在容器中）
查看版本、状态：
```
select version();
status;
```

> 5.mysql-8允许远程访问修改方式
```
use mysql;
select host,user from user where user='root';
update user set host='%' where user='root' and host='localhost';
flush privileges;
select host,user from user where user='root';
alter user 'root'@'%' identified with mysql_native_password by '99131456';
flush privileges;
```

> 6.修改server配置文件，内容包括
```
vim server/config/application.yml
数据库所在ip、端口
username
password
```

> 7.server部署在ARM上时，server目录中的wgcloud-daemon-release需要替换wgcloud-daemon-arm64.tar.gz
```
tar -xzvf wgcloud-daemon-arm64.tar.gz
mv  wgcloud-daemon-release server/wgcloud-daemon-release
```

> 8.修改服务端所有可执行程序权限
```
cd server/
chmod 777 wgcloud-daemon-release start.sh  stop.sh wgcloud-server-release.jar
```

> 9.修改代理端所有可执行程序权限
```
cd wgcloud-agent
chmod 777 start.sh  stop.sh  wgcloud-agent-release
```

> 10.启动服务端
```
cd server/
./start.sh
tail -f log/wgcloud.XXXX
查看是否有Started WgcloudServiceApplication in 13.655 seconds (JVM running for 14.998)
```

> 11.如果有登录成功则可以访问了
```
http://192.168.1.1:9999/wgcloudcd 
账号：admin
密码：111111
```

> 12.启动代理端
```
cd wgcloud-agent/
./start.sh
tail -f agent/log/XXX
查看是否有错误。
```

docker run --name wgcloud -d -v /etc/timezone:/etc/timezone:ro -v /etc/localtime:/etc/localtime:ro -p 9999:9999 -p 9998:9998 -p 9997:9997 wgcloud

