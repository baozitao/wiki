# 在git中忽略文件夹，文件，不跟踪，这里指的/的根目录，是.git所在目录，不是linux根
假如在项目根目录下创建一个.gitignore
dist     忽略整个项目中名字是dist的文件和文件夹
dist/   忽略整个项目中名字叫做dist的文件夹。  
/dist   忽略项目根目录下的名字叫做dist的文件夹和文件
/dist/    只忽略根目录下的名字是dist的文件夹。  根目录下的 dist文件并不忽略

比如，我需要忽略根目录下的.obsidian文件夹及其文件夹内容，则直接在.git/info/exclude文件中新建一行，写上即可
```markdown
/.obsidian/

```
