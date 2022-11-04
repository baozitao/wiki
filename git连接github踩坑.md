## git 初始化
```

```

## 设置github连接
> 设置公钥私钥
```
git config --global user.name baozitao
git config --global user.email baozitao@gmail.com
ssh-keygen -t rsa -C baozitao@gmail.com # 一路回车设置好文件路径和文件名，不要写后缀
```
```

```
chmod 600 ~/.ssh/github.pem
eval `ssh-agent -s`
ssh-add ~/.ssh/github.pem
```

## git push origin main 遇到‘ `fatal: refusing to merge unrelated histories`’ 问题
```
git pull origin master --allow-unrelated-histories
```


## git push 遇到问题' git pull origin master --allow-unrelated-histories'
```
git pull origin master --allow-unrelated-histories
```









