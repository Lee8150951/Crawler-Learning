# Python爬虫笔记

## 一、概述

基本概念：通过编写程序，**模拟浏览器上网**，让其去互联网上抓取数据的过程

通过爬取数据对数据进行产品化，商业化，深度挖掘数据中的隐藏价值

:::tip

爬虫合法性

- 在法律中并不被禁止
- 具有一定的法律风险
- 违法：爬虫干扰了被访问网站的正常运行
- 违法：爬虫抓取了被法律保护的特定类型数据或信息

:::

爬虫的分类：

- 通用爬虫：抓取系统重要组成部分，抓取的是一整张页面中的数据
- 聚焦爬虫：是建立在通用爬虫的基础之上的，抓取的是页面中特定的局部内容
- 增量式爬虫：检测网站中数据的更新情况，只会抓取网站中最新更新出来的数据

**robots.txt协议**：君子协议，说明了网站上哪些数据可以爬取，哪些数据不可以被爬取

## 二、http和https协议

http协议：指的就是客户端与服务器进行数据交互的一种形式

### 1、常用请求头信息

- User-Agent：表示请求载体的身份标识
- Connection：表示成功之后是断开连接还是保持连接（Close、Keep-alive）

### 2、常用响应头信息

- Connect-Type：服务器响应回客户端的数据类型

### 3、Https和Http之间的区别

Https表示安全的超文本传输协议，在客户端、服务端进行数据交互时涉及到了数据加密

涉及加密方式：①对称密钥加密；②非对称密钥加密；③证书密钥加密

## 三、Request模块

python中原生的一款基于网络请求的模块，功能强大，简单便捷，效率极高。

**作用：模拟浏览器发起请求**

:::tip

使用流程：

- 指定URL
- 向指定网址发送请求
- 获取响应数据
- 持久化存储响应数据

:::

环境安装：`pip install requests`

```python
# 1、导入模块
import requests
if __name__ == "__main__":
    # 2、指定URL
    url = 'https://www.sogou.com/'
    # 3、发起请求(get方法会获取一个响应对象)
    response = requests.get(url)
    # 4、获取响应数据(.text返回一组字符串)
    page_text = response.text
    print(page_text)
    # 5、持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('Success!')
```

### 1、UA伪装

UA伪装指的就是User-Agent（请求载体的身份标识）这个请求头

**UA检测**：门户网站的服务器会检测对应请求载体的身份标识，如果检测到请求的载体身份标识为一款浏览器，表明属于正常请求；如果请求的载体身份标识不是基于某一款浏览器的，则表示该请求不正常

**UA伪装**：将对应的User-Agent封装到一个字典中

```python
import requests
if __name__ == "__main__":
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
    # 指定URL
    url = 'https://www.sogou.com/web'
    # 处理携带参数
    kw = input('Enter a word: ')
    param = {
        'query': kw
    }
    # 通过字典形式封装参数，动态拼接在url后面
    # headers表示所携带头信息
    response = requests.get(url, param, headers=headers)

    page_text = response.text
    fileName = kw + '.html'
    with open('result/' + fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('Success!')
```

