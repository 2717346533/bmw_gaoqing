#开发人员：林泽鑫
#开发实践：2019/8/1 0:38
#文件名称：os_demo.py
#开发工具: PyCharm
import os
images_path= os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
if not os.path.exists(images_path):
    os.mkdir(images_path)
else:
    print("images文件夹存在")