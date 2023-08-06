# GET IPV4 or IPV6 info 

[![PyPI version](https://badge.fury.io/py/hot-magnet.svg)](https://pypi.org/project/hot-magnet/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


> 兼容环境

`Windows`/`Linux`/`MacOs`

<br>

### 1 安装

> pip 安装
```
$ pip install ip_info_all
```

> 源码安装
```
 $ git clone https://github.com/landybird/IPInfo.git
 $ cd ip_info_all
 $ python setup.py install
 ```

<br>

### 2 使用


1 `initial a IPInfo object` 实例化IP对象

```python

ip_info = IPInfo()
```

2 get `all IPV4` or `IPV6 info` --  return value is a dict 获取所有的信息

```python
ip4_info_dict = ip_info.all_ipv4_ip_info_dict
ip6_info_dict = ip_info.all_ipv6_ip_info_dict

```

3 get ip address ,netmask, broadcast info `by link encap` and `param = "addr" or "netmask" or "broadcast"` default is address  根据连接节点 获取指定的ip信息

```python
ip_info.get_ipv6_ip_by_encap("etho1", param="all")
ip_info.get_ipv6_ip_by_encap("etho1", param="addr")

ip_info.get_ipv4_ip_by_encap("etho1", param="all")
ip_info.get_ipv4_ip_by_encap("etho1", param="addr")
```





### License

MIT [©landybird](https://github.com/landybird)
