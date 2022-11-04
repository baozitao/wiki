```
chmod 600 ~/.ssh/github.pem
eval `ssh-agent -s`
ssh-add ~/.ssh/github.pem
```

## git push origin main 遇到‘ `fatal: refusing to merge unrelated histories`’ 问题
```
git pull origin master --allow-unrelated-histories
```