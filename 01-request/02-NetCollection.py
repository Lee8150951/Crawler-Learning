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
