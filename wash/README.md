清洗的方法
==========

首先已经有了抓取的SogouT格式的网页。

step1.py 主要去处网页中无关的信息
step2.py 主要负责在剩下部分中抽取出正文

整个流程可以这样完成：

    cat xxx.pages | ./step1.py | ./step2.py > xxx.txt

