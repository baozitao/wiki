import paramiko

def install_docker(ssh):
    # 从本地计算机上传 Docker 二进制安装包到远程服务器的 /tmp 目录
    scp = ssh.open_sftp()
    scp.put('docker.tar.gz', '/tmp/docker.tar.gz')
    scp.close()

    # 解压 Docker 安装包并安装
    ssh.exec_command('tar -xf /tmp/docker.tar.gz -C /tmp')
    ssh.exec_command('cd /tmp/docker && sudo ./install.sh')

def install_docker_compose(ssh):
    # 从本地计算机上传 Docker Compose 二进制文件到远程服务器的 /usr/local/bin 目录
    scp = ssh.open_sftp()
    scp.put('docker-compose.tar.gz', '/tmp/docker-compose.tar.gz')
    scp.close()

    # 解压 Docker Compose 安装包并移动到 /usr/local/bin 目录
    ssh.exec_command('tar -xf /tmp/docker-compose.tar.gz -C /tmp')
    ssh.exec_command('sudo mv /tmp/docker-compose /usr/local/bin/docker-compose')

def load_docker_images(ssh):
    # 从本地计算机上传 Docker 镜像到远程服务器的 /app 目录
    scp = ssh.open_sftp()
    scp.mkdir('/app')
    scp.put('redis.tar', '/app/redis.tar')
    scp.put('postgres.tar', '/app/postgres.tar')
    scp.close()

    # 在远程服务器上加载 Docker 镜像
    ssh.exec_command('docker load -i /app/redis.tar')
    ssh.exec_command('docker load -i /app/postgres.tar')

def start_containers(ssh):
    # 在远程服务器上使用 Docker Compose 启动容器
    ssh.exec_command('docker-compose -f /app/docker-compose.yml up -d')

# 创建 SSH 客户端连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 密钥文件路径
private_key_path = '/path/to/private_key'

# 密钥登录远程服务器
ssh.connect('your_server_ip', username='your_username', key_filename=private_key_path)

# 安装 Docker
install_docker(ssh)

# 安装 Docker Compose
install_docker_compose(ssh)

# 将 Docker 镜像从本地计算机上传到远程服务器的 /app 目录，并加载镜像
load_docker_images(ssh)

# 在远程服务器上使用 Docker Compose 启动容器
start_containers(ssh)

# 关闭 SSH 连接
ssh.close()