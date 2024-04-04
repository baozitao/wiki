## apt时候显示lock
```
E: Could not get lock /var/lib/apt/lists/lock. It is held by process 1898760 (apt-get)
```


sudo fuser -vik -TERM /var/lib/apt/lists/lock