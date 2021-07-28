# 采集猫眼电影《中国医生》观影数据
# 请求地址 https://m.maoyan.com/mmdb/comments/movie/1337700.json?v=yes&offset=0&startTime=2021-07-28 14:00:00
# 1337700 表示中国医生的电影id
from datetime import datetime, timedelta
import time
import requests
import json
import sys

if __name__ == '__main__':
    request_url = 'https://m.maoyan.com/mmdb/comments/movie/1337700.json?v=yes&offset=0&startTime=2021-07-28 14:00:00'


    # 根据url获取数据
    def get_data(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36',
        }
        response = requests.get(url=url, headers=headers)
        html_data = response.text
        return html_data


    # 处理数据
    def parse_data(html):
        # 将json转换成list
        data = json.loads(html)['cmts']
        comments = []
        for item in data:
            comment = {
                'id': item['id'],
                'nickName': item['nickName'],
                # 处理cityName不存在的情况
                'cityName': item['cityName'] if 'cityName' in item else '',
                # 处理评论内容换行的情况
                'content': item['content'].replace('\n', ' ', 10),
                'score': item['score'],
                'startTime': item['startTime']
            }
            comments.append(comment)
        return comments


    # 存储数据，存储到文本文件
    def save_to_data():
        # 获取当前时间，从当前时间向前获取
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        end_time = '2021-07-09 00:00:00'
        while start_time > end_time:

            url = 'https://m.maoyan.com/mmdb/comments/movie/1337700.json?v=yes&offset=0&startTime=' + start_time.replace(
                ' ', '%20')
            html = None

            try:
                html = get_data(url)
            except Exception as e:
                # 当请求过于频繁时，服务器会拒绝连接，服务器的反爬虫策略
                time.sleep(0.5)
                html = get_data(url)
            else:
                time.sleep(1)

            print('html = ', html)
            sys.exit()
            comments = parse_data(html)
            print(comments)
            # 获得末尾评论的时间
            start_time = comments[-1]['startTime']
            # 转换为datetime类型，减1秒，避免获取到重复数据
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(
                seconds=-1)
            # 转换为str
            start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')

            for item in comments:
                with open('ChinaDoctor.txt', 'a', encoding='utf-8') as f:
                    f.write(str(item['id']) + ',' + item['nickName'] + ',' + item['cityName'] + ',' + item[
                        'content'] + ',' + str(item['score']) + ',' + item['startTime'] + '\n')

    save_to_data()
