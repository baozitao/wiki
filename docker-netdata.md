# 建立文件夹，修改权限
mkdir netdata \
mkdir netdata/{cache,config,lib} \
chmod -R 775 netdata \
sudo chown -R 201:201 /netdata 

# 容器运行
docker run -d --name=netdata \
  -p 19999:19999 \
  -v /home/netdata/lib:/var/lib/netdata \
  -v /home/netdata/cache:/var/cache/netdata \
  -v /etc/passwd:/host/etc/passwd:ro \
  -v /etc/group:/host/etc/group:ro \
  -v /proc:/host/proc:ro \
  -v /sys:/host/sys:ro \
  -v /etc/os-release:/host/etc/os-release:ro \
  --restart unless-stopped \
  --cap-add SYS_PTRACE \
  --security-opt apparmor=unconfined \
  netdata/netdata

