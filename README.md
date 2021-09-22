# CountKey

A mac app that records the number of keystrokes on the keyboard.


## Usages

1、直接运行

2、将 `CountKey.app` 拷贝到访达里的 `应用程序` 中，这样使用更方便

Tips: 按住 `Command` 键不松，鼠标点击菜单栏图标向右拖动到可以看到的位置，可以避免图标被遮挡导致看不到

软件不联网，也不储存什么文件，只需要获取读键盘的权限就行，软件重启会从零开始重新计数。

## Build


```bash
python setup.py py2app
```

生成的 app 中会缺少 `libffi.7.dylib` ，需要手动拷贝到 `/Contents/Frameworks/` 里边。

## TODO

- [ ] 去除 Dock 上的图标显示
- [ ] 在本地保存日志，记录每天的次数以及高频按键
- [ ] 自动化打包问题，即不需要手动拷贝依赖

## About

CountKey v1.0.0 was made in 2021 by YangShu.

Don't be sedentary!
Protect your waist, shoulders, neck and wrists!
Here's to your health, longevity!

Welcome to email me!
Let me know you are using this app.
Since this app is not networked, it is convenient for me to tell you by email after this app is upgraded.

Contact Me: yangshu1109@gmail.com
