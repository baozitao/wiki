# git 学习注意事项
1. git diff 都是针对tracted文件，未被tracted的文件是不能被比较的 - 所以，git status 非常重要,可以先看到哪些文件没有被监控
    - git diff HEAD 的内容，就是git diff 和git diff -staged的总和
    - git diff，显示工作区，和暂存区区别，即tracted的文件中，哪些修改add了哪些没add
    - git diff --staged 显示暂存区和本地仓库的区别，即tracted的文件中，哪些修改commit了，哪些没有;
    - git diff HEAD 显示最后一次commit的内容和暂存和工作区区别;
    - gs 可以把未tracted的文件显示出来。
2. 其次才是git相关命令
3. gadd 是从工作区，放到staged区域;
4. git status 是某个分支下最重要的命令，它同时对workspace 、staged 、reposiry三个区域之间文件的对比状态进行粗略显示;
5. git reset <commit> 仅仅只是去掉不想要的提交，并不会立即更新workspace,如果要恢复到以前的文件，用checkout 和 restore 
6. git checkout head～3可以切换指针
    - git switch -   可以让head又指向最新依次commit
7. git 恢复(有两种，一种中commit中恢复，一种从staged中恢复：
    - git checkout HEAD 是从最新的commit恢复(也可以只恢复一个文件）
    - git restore 和上面作用一样，也是从最新的commit中恢复。
    - git restore --source HEAD~1 <file> 是从其他次commit中恢复文件,但要注意，这仅仅只是恢复文件，当前head还是在当前
    - git restore --staged 从staged中恢复
8. git revert和git reset 都能达到恢复到某次commit的效果，但是，reset 是把多于的commit都删掉，而git revert是将commit再拿出来坐一次comminit,原有的commit并没有删除 
