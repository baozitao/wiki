## git 过程图
![[Pasted image 20221104233011.png]]

![[Pasted image 20221104233046.png]]


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
➜ git commit -m "feat: 完成某页面的开发" # 将暂存区的文件发版
➜ git status 			# 再次查看，此时工作区和暂存区就干净了
On branch cs/isiliu
nothing to commit, working tree clean
```

### 提交版本命令详解
-   提交文件，形成版本
```
1. 提交文件并添加说明
git commit -m "说明性文字"
# 一定要写一个简单的说明，方便后续查找版本
# 因为当我们的历史版本多了以后，我们自己也记不住哪个版本做了哪些修改

2. 提交跟踪过的文件（可省略`git add`），不添加文字说明
# 能帮你省一步 git add ，但也只是对修改和删除文件有效， 新文件还是要 git add，不然就是 untracked（未跟踪状态）
git commit -a
# 相当于：
# git add .
# git commit 

3. 提交跟踪过的文件（可省略`git add`），并添加文字说明
# 能帮你省一步 git add ，但也只是对修改和删除文件有效， 新文件还是要 git add，不然就是 untracked（未跟踪状态）
git commit -am "xxx"
# 相当于：
# git add .
# git commit -m "xxx"

4. 查看帮助，还有许多参数有其他效果
git commit --help
```

## Git pull 和 push
-   上传要保证 **历史区** 里面有内容，会把所有的内容上传到远端
### 上传指令
```
# 指定远程仓库名和分支名（第一次）
git push -u origin master
# origin 指定推送的地址
# master 是上传到远程的 master 分支
# 不指定远程仓库名和分支名（第二次）
git push
```

-u 是为了记录一下用户名和密码，下次上传的时候就不需要再写了
第一次上传要指定远程仓库名和分支名
第二次上传的时候，因为有刚才的记录，就不需要再 写 origin 和 master 了， 会默认传递到 origin 这个地址的 master 分支上
如果你要传递到别的分支上的时候，要再次指定远程仓库名和分支名
这个时候本地的文件夹就真的可以删除了， 因为远程有一份我们的内容，本地的删除了，可以直接把远程的拉回来就行
不管是你克隆下来的仓库还是别的方式弄得本地仓库，当人家的代码更新以后，你想获得最新的代码。我们不需要从新克隆。只要拉取一次代码就可以了

### 下拉指令
```
# 将本地代码和远程代码同步：(在本地仓库使用命令)
git pull
```


## 分支指令
###分支指令
```
# 查看本地分支：
git branch

# 查看远程分支：
git branch -r

# 更新远程分支：
git fetch

# 创建分支：
git branch 分支名

### 切换分支：（常用）
git checkout 分支名

### 切换到上个分支：（常用）
git checkout -

### 创建并切换到这个分支：（常用）
git checkout -b 新分支名

### 合并分支：（常用）
git merge 被合并的分支 # 要先跳转到要合并其他分支的分支

# 终止合并分支：
git merge --abort

# 删除分支：(不能自己删自己)
git branch -D 要删除的分支

# 本地分支重命名：
git branch -m oldName  newName

# 删除远程的旧分支：
git push --delete origin oldName

```


### 分支命名
```
master：主分支，永远只存储一个可以稳定运行的版本，不能再这个分支上直接开发
develop： 主要开发分支，主要用于所用功能开发的代码合并，记录一个个的完整版本
	包含测试版本和稳定版本
	不要再这个分支上进行开发
feature-xxx：功能开发分支，从 develop 创建的分支
	主要用作某一个功能的开发
	以自己功能来命名就行，例如 feature-login / feature-list
	开发完毕后合并到 develop 分支上
feature-xxx-fix: 某一分支出现 bug 以后，在当前分支下开启一个fix分支
	解决完 bug 以后，合并到当前功能分支上
	如果是功能分支已经合并之后发现 bug 可以直接在 develop 上开启分支
	修复完成之后合并到 develop 分支上
hotfix-xxx： 用于紧急 bug 修复
	直接在master分支上开启
	修复完成之后合并回 master
```

### 记得养成一个良好git发布流程的习惯
```
# 分支合并发布流程：
git add .			# 将所有新增、修改或删除的文件添加到暂存区
git commit -m "版本发布" # 将暂存区的文件发版
git status 			# 查看是否还有文件没有发布上去
git checkout test	# 切换到要合并的分支
git pull			# 在test 分支上拉取最新代码，避免冲突
git merge dev   	# 在test 分支上合并 dev 分支上的代码
git push			# 上传test分支代码
```

## Git config 设置
> `git config`命令用于获取并设置存储库或全局选项，这些变量可以控制Git的外观和操作的各个方面

```
# 查看git配置信息
git config --list

# 查看git用户名
git config user.name

# 查看邮箱配置
git config user.email

# 全局配置用户名
git config --global user.name "nameVal"

# 全局配置邮箱
git config --global user.email "eamil@qq.com"

# 删除全局配置用户名和邮箱
git config --global unset user.name "用户名"
git config --global unset user.email "注册邮箱"
```

> 对于git来说，配置文件的权重是`「仓库 > 全局 > 系统」`，即 `「local > global > system」`
-   添加配置项：`--add`
-   格式：`git config [-local | -global | -system] add section.key value`（默认是添加在`local`配置中）
```
git config --add sit.name Jack
```

-   删除配置项：`--unset`
-   格式：`git config [-local | -global | -system] -unset section.key`
```
git config --local --unset user.name
```


## 版本回退
```text
使用git log命令，查看分支提交历史，确认需要回退的版本
使用git reset --hard commit_id命令，进行版本回退
eg:git reset --hard 79cb90832ad1cfac65398008a0777e52e0be5d22
```

## 设置默认编辑器为vim
```
git config --global core.editor vim  ##设置默认编辑器
git config --global core.editor vim  ##查看默认编辑器
```


# 设置github连接
**设置公钥私钥**
```
git init
git config --global user.name baozitao
git config --global user.email baozitao@gmail.com
git remote add origin git@github.com:baozitao/key.git
git fetch origin git@github.com:baozitao/key.git
git pull origin master


ssh-keygen -t rsa -C baozitao@gmail.com # 一路回车设置好文件路径和文件名，不要写后缀
chmod 600 ~/.ssh/github.pem
eval `ssh-agent -s`
ssh-add ~/.ssh/github.pem```
```

## git push origin main 遇到‘ fatal: refusing to merge unrelated histories问题
```
git pull origin master --allow-unrelated-histories
```


## git push 遇到问题' git pull origin master --allow-unrelated-histories'
```
git pull origin master --allow-unrelated-histories
```









