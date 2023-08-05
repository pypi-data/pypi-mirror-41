**benyo_zbx**

It is a test module which build by Benyo Yuan,
it test the python module that can install by pip and use in py2.7 and py3.7.

*Introduction*

from benyo_zbx import ZabbixFace as zf

zf_demo = zf(auth=(), host="")
print(zf_demo)

# 获取host清单
host_lists = zf_demo.host.get()


*Supports* 
Tested on Python 2.7, 3.7

pip install benyo_zbx
Download: https://pypi.org/project/benyo-zbx/#description
Documentation: https://pypi.org/project/benyo-zbx/#files

`Your feedback is always welcome!`