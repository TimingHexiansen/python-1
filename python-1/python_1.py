
# @Author : ����

'''
����ע��
���������к����һֻСè��ǰ��
��װģ�� pip install sprites
'''
# �Ӿ���ģ�鵼����������
from sprites import *
# �½���ɫ,��������Ϊimages
images = 'res/cat1.png','res/cat2.png'
# �½���ɫ
cat = Sprite(shape=images)
# ��������
cat.play('��.wav')
# ��������ʱ��(�ظ�ִ��)
while True:
    # ǰ��10
    cat.fd(10)
    # ��һ������
    cat.nextcostume()
    # �ȴ�0.3��
    cat.wait(0.3)
