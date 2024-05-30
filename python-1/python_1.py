
# @Author : 辣条

'''
多行注释
本程序运行后会有一只小猫向前走
安装模块 pip install sprites
'''
# 从精灵模块导入所有命令
from sprites import *
# 新建角色,造型序列为images
images = 'res/cat1.png','res/cat2.png'
# 新建角色
cat = Sprite(shape=images)
# 播放喵声
cat.play('喵.wav')
# 当成立的时候(重复执行)
while True:
    # 前进10
    cat.fd(10)
    # 下一个造型
    cat.nextcostume()
    # 等待0.3秒
    cat.wait(0.3)
