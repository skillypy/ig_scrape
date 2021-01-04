import requests
import json

url = 'https://www.instagram.com/graphql/query'

short_code = input('Please enter the shot code: ')

var = {"shortcode":short_code,"first":100}
headers = {'cookie':'sessionid=1530372735%3Abx34GUeT1hOVsz%3A12'}
params = {
    'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
    'variables': json.dumps(var)
}
respon = requests.get(url, headers=headers, params=params).json()

users = respon['data']['shortcode_media']['edge_liked_by']['edges']

count = 0
for user in users:
    username = user['node']['username']
    fullname = user['node']['full_name']
    profile_pic = user['node']['profile_pic_url']
    count += 1
    print(username,fullname, profile_pic)
    print(count)