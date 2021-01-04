import requests
import json
import time

url = 'https://www.instagram.com/graphql/query'

short_code = input('Please enter the shot code: ')

endcursor = ''

count = 0
while 1:
    var = {
        "shortcode":short_code,
        "first":100,
        'after':endcursor
    }

    headers = {'cookie':'sessionid=1530372735%3Abx34GUeT1hOVsz%3A12'}
    params = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(var)
    }
    respon = requests.get(url, headers=headers, params=params).json()
    try: users = respon['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('Wait for 30 secs')
        time.sleep(30)
        continue

    for user in users:
        username = user['node']['username']
        fullname = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        count += 1
        print(count, username,'-', fullname)


    endcursor = respon['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    hasnextpage = respon['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if hasnextpage == False: break
    time.sleep(2)
    # print(endcursor)