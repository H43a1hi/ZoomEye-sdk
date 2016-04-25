# ZoomEye-sdk
ZoomEye sdk_v1.0.1


使用  python ./setup.py install即可。


使用范例 ZoomEye_test.py

运行之后会在本地生成ip.txt
手动添加https://

![](http://images.sebug.net/contribute/1c37ad4c-7026-4612-a9cc-a2b85afa5e38)

使用pocsuite 的-f 选项读取进行验证
```
pocsuite -r tests/ac2300.py -f /Desktop/ZoomEye/ip.txt --verify
```

验证结果：
![](http://images.sebug.net/contribute/de326f18-9dab-4053-a602-4aa10e05e1ed)

