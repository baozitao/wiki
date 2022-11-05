# Manjaro安装deb包
## 1、安装debtap

使用`yay`安装`debtap`，如果没有`yay`，需要使用`pacman`安装`yay`：
```
sudo pacman -S yay
```

安装`debtap`：
```
sudo yay -S debtap
```

## 2、deb包转换arch包
```
sudo debtap -u
```

使用`debtap`将deb包转换为arch包，假设需要转换的deb包为`xxxxx.deb`：
```
sudo debtap -q xxxxx.deb
```

在转换过程中会提示是否需要编辑相关信息，直接按回车即可，转换完成后，将会生成一个后缀为`.pkg.tar.rst`的文件。

## 3、安装
使用pacman安装转换的arch包：
```
sudo pacman -U xxxx.pkg.tar.rst
```