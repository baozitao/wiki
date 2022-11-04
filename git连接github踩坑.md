## git 初始化
```
git init
1. 我们必须要把我们电脑中的某一个文件夹授权给 `git`
2. `git` 才能对这个文件夹里面的内容进行各种操作
3. 而 `git init` 就是在进行这个授权的操作
4. `git` 不光管理这一个文件夹，包括所有的子文件夹和子文件都会被管理
5. 只有当一个文件夹被 git 管理以后，我们才可以使用 git 的功能去做版本管理
6. 只有执行了git init后，git才知道，仓库在这里
7. git init会在文件夹下生成.git文件等，用于管理后续各种记录合并
```

## ## Git 工作区
### git status
**工作区**：我们书写的源码就在工作区里面
```
➜ git status
On branch cs/isiliu
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/App.vue		# 在工作区的文件路径将为红色
no changes added to commit (use "git add" and/or "git commit -a")```


```

## Git 暂存区
### git add
**暂存区**：把我们想要存储的内容放在暂存区，文件路径为绿色
```
➜ git add . #将工作区的文件添加到暂存区
➜ git status
On branch cs/isiliu
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   src/App.vue		# 在暂存区的文件路径将为绿色
```

### git commit
**历史区**：把暂存区里面的内容拿出来形成一个历史版本
```

```



## 设置github连接
设置公钥私钥git config --global user.name baozitao
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









