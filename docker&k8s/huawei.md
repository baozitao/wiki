## 查看接口ip地址
[Huawei]display ip interface brief

## 设备命名
sysname RouterA


## 设置vlan接口为dhcp功能
    # 创建VLAN10并将GE0/0/1接口加入到VLAN10中。

    <HUAWEI> system-view
    [HUAWEI] sysname SwitchA
    [SwitchA] vlan 10
    [SwitchA-vlan10] quit
    [SwitchA] interface gigabitethernet 0/0/1
    [SwitchA-GigabitEthernet0/0/1] port link-type trunk
    [SwitchA-GigabitEthernet0/0/1] port trunk allow-pass vlan 10
    [SwitchA-GigabitEthernet0/0/1] quit
    # 在VLANIF10接口上使能DHCP客户端功能。
    [SwitchA] interface vlanif 10
    [SwitchA-Vlanif10] ip address dhcp-alloc

## 设置某个接口dhcp
system-view
interface interface-type interface-number[.subinterface-number ]
ip address dhcp-alloc

## 查看设备时间
<Huawei>display clock

## 设置时区
 clock timezone bj add 08:00:00
 
####################################################################################
## 配置SSH登录
#
 rsa peer-public-key rsakey001 encoding-type pem  //配置RSA公共密钥编码格式是PEM
  public-key-code begin
  ---- BEGIN SSH2 PUBLIC KEY ----
  AAAAB3NzaC1yc2EAAAADAQABAAABAQCmxyAhs37Q7HhoCCjw2cIe7Vi7O6Q6ocZi
  NiYmgrmE2nMMDemxm/DHUJly/95V5723RQhTHUvu+KLV8DMpTcvkVGIMkMH30Hpv
  kYPMdz0BqgoF7S4RSHMpsh+JK+0Ig6O+lMgzfuQNS4oCJIjH4/fO1CMHVwwIvsDf
  YpNHw/Vv0pl6o7mKowHsY6XpF3DPCyBmnlgu8xF4dHojp+Aa9Skup17epHCdRdmo
  UuDSEM561jv8mfSPkpWXzEigX+nQq4jQNdhH8mSnYRBlWA3sKiQoFRyo9V/W2QIz
  WHAGMoRBioW3xwfQ2cf7TxxBfG4Q+8EMnCWsxzoL3KjAAXgmtFfv
  ---- END SSH2 PUBLIC KEY ----                                               
 public-key-code end                                                            
peer-public-key end  //生成本地密钥对
#
aaa
 local-user baojt password irreversible-cipher   //创建本地用户，用户名为baojt，密文密码为Helloworld@6789。对于“password irreversible-cipher”后面的字段，可以是明文也可以是密文
 local-user baojt privilege level 15  //配置本地用户baojt的优先级为15
 local-user baojt service-type ssh //配置本地用户baojt的接入方式为Stelnet
#
interface GigabitEthernet1/0/0
 ip address 10.137.217.159 255.255.255.0  //配置连接HostA的接口的IP地址
#
 ssh user baojt authentication-type rsa  //配置本地用户baojt的认证方式为RSA
 ssh user baojt assign rsa-key rsakey001  //指定本地用户baojt要连接的SSH服务器端的主机公钥名称
 stelnet server enable  //使能SSH服务器功能
#
user-interface vty 0 4
user privilege level 15  //配置用户的优先级为15
 authentication-mode aaa  //配置VTY类型用户界面的验证方式为AAA
 protocol inbound ssh  //配置VTY类型用户界面只支持SSH协议
#

####################################################################################


### 设置ntp 服务器
ntp-service unicast-peer ntp.aliyun.com


### 查看ntp状态
display ntp-service status
