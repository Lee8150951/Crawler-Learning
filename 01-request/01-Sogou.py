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
    with open('result/sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('Success!')
