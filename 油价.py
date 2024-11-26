import requests
from parsel import Selector

# 定义URL和headers
url = 'http://www.qiyoujiage.com/anhui.shtml'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.0'
}

# 发送请求
response = requests.get(url, headers=headers)

# 确保响应状态码为200
if response.status_code == 200:
    # 解析HTML内容
    selector = Selector(response.text)
    
    # 使用CSS选择器获取92#油价
    yj = selector.css('#youjia > dl:nth-child(1) > dd::text').get()
    
    # 使用XPath选择器获取下次油价调整时间和预计下调油价
    ts = selector.xpath('//*[@id="youjiaCont"]/div[2]/text()').get()
    ts1 = selector.css('#youjiaCont > div:nth-child(2) > span:nth-child(2)::text').get()
    
    # 格式化输出油价信息
    msg = '\n' + '⛽ 安徽92#油价：' + yj + ' 元.' + ts + '⚡️' + '\n' + ts1
    
    # # PushMe 推送部分
    api_token = 'x250zqWf8QdPnMANJM8u'
    title = '⛽ 安徽92#油价推送'
    push_url = f'https://push.i-i.me/?push_key={api_token}'
    data = {
        'title': title,
        'content': msg
    }

    # 发送POST请求进行推送
    push_response = requests.post(push_url, data=data)

    # 检查推送响应
    if push_response.status_code == 200:
        print("推送成功")
    else:
        print("推送失败，状态码：", push_response.status_code)
else:
    print("Failed to retrieve the webpage")