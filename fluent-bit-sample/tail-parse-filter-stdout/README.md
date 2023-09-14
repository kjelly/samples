# fluent-bit sample

示範 fluent-bit parser 與 filter 功能。已知限制，如果型別是 int ，無法使用任何filter。filter只有支援 string 。


```
./generate-metric.py
fluent-bit -c main.conf -R parser.conf
```

## 使用指令代替 main.conf

目前不完全一樣，只是示範
```
fluent-bit -R parser.conf -i tail -p path=a.log -p parser=bill -F parser -p parser=json -m '*' -p key_name=message -o stdout
```


