# requests 使用
import requests
import json

r = requests.get('https://www.zhonghuakouqiang.com/htm/yaowen/2020/1214/1854.html')
# print(r.encoding)
# 响应里的encoding = ISO-8859-1 , 为了解决输出乱码，可以设置 encoding
# r.encoding = 'GBK'
# print(r.text)


# response = requests.get('https://api.github.com/events', verify=False)

# print(response.encoding)
# with open('github_events.json', 'w', encoding='utf-8') as f:
#     json.dump(response.json(), f, ensure_ascii=False)

print('ok')






