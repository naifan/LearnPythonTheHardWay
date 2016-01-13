# LearnPythonTheHardWay
Ex10.py 
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
这里用到了\r的含义，区分\r(回车)和\n(换行)。i后面的comma是指不换行。

ex11.py
MINtty(git bash)和CMD运行程序顺序不一样，因为buffering mode不同，CMD直接输出，MINGtty需要通过pipe。可通过python - u解决。
参考：http://stackoverflow.com/questions/34668972/cmd-and-git-bash-have-a-different-result-when-run-a-python-code/34669237#34669237

ex15.py
注意argv的使用

ex20.py
file.seek(0) #文件归位
print , 避免在print后面多加"\n"