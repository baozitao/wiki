import docker

def export_image(image_name, output_file):
    client = docker.from_env()
    image = client.images.pull(image_name, platform='linux/arm64')
    image.save(output_file)

# 需要下载的镜像列表
images = [
    "moelin/1panel:v1.9.6",
    "postgres:16.2",
    "mysql:8.3.0",
    "adminer:4.8.1",
    "postgres:16.2",
    "redis:7.2.4",
    "cnrancher/autok3s:v0.9.2",
    "nicolargo/glances:4.0.2",
    "traefik:v2.11.2",
    "emilevauge/whoami:v1.0.2",
    "lissy93/dashy:3.0.0",
    "amir20/dozzle:v6.5.0",
    "portainer/portainer-ce:2.19.5",
    "netdata/netdata:v1.45.3",
    "portainer/agent:2.19.5",
    "jgraph/drawio:24.2.7",
    "linuxserver/librespeed:5.3.0",
    "pihole/pihole:2024.03.2",
    "apache/hertzbeat:v1.5.0",
    "pschiffe/pdns-mysql:4.8",
    "mariadb:11.3.2",
    "powerdnsadmin/pda-legacy:v0.4.2"
]

# 循环下载并导出每个镜像
for image_name in images:
    output_file = f"{image_name.replace('/', '_').replace(':', '_')}.tar"
    export_image(image_name, output_file)
    print(f"Exported {image_name} to {output_file}")