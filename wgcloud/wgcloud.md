## 制作arm64的镜像
将jdk1.8.0的包解压到Dockerfile同级目录下名字为jre
将tomcat 包解压到Dockerfile同级目录下名字为apache
将wgcloud-3.4.0包解压到Dockerfile同级目录下，命名为server
替换arm64-daemon到server中，替换同名文件，因为同名文件默认是X86架构的
将4个文件chmod 为可执行体
移除/config目录下的文件
建立Dockerfile文件，并制作镜像

## 以下为Dockerfile文件内容
```
ARG BUILD_FROM=arm64v8
FROM ${BUILD_FROM}/ubuntu:16.04

ADD apache/ /opt/tomcat
ADD jre/ /opt/jdk

RUN sed -i '$a\JAVA_HOME=/opt/jdk\nJAVA_BIN=/opt/jdk/bin\nJRE_HOME=/opt/jdk/jre\nCLASSPATH=/opt/jdk/jre/lib:/opt/jdk/lib:/opt/jdk/jre/li    b/charsets.jar\nexport  JAVA_HOME  JAVA_BIN JRE_HOME  PATH  CLASSPATH' /etc/profile
RUN sed -i '$a\export JAVA_HOME=/opt/jdk/\nexport PATH=$JAVA_HOME/bin:$PATH\nexport CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/too    ls.jar' ~/.bashrc

ENV JAVA_HOME=/opt/jdk
ENV JAVA_BIN=/opt/jdk/bin
ENV JRE_HOME=/opt/jdk/jre
ENV CLASSPATH=/opt/jdk/jre/lib:/opt/jdk/lib:/opt/jdk/jre/lib/charsets.jar
ENV PATH=/opt/jdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 作者
MAINTAINER wgcloud
#切换镜像目录，进入/usr目录
WORKDIR /wgcloud
RUN mkdir wgcloud
#将宿主机的wgcloud目录下的文件拷至镜像的/wgcloud目录下
ADD server/ /wgcloud/
EXPOSE 9997 9998 9999

#设置启动命令
CMD ["/wgcloud/start.sh"]
```
## 制作镜像
docker build --build-arg BUILD_FROM=arm64v8 -t wgcloud:v3.4.0 .

## 运行镜像
端口9999  9998  9997 开放
映射/etc/localtime /etc/timezone
映射配置文件到容器的 /wgcloud/config/ 目录
启动方式总是重启
