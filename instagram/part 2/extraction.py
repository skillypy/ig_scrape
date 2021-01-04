import requests
import json
import time
import csv

url = 'https://www.instagram.com/graphql/query'

short_code = input('Please enter the shot code: ')

endcursor = ''
count = 0
counter_file = 1
jml_per_file = 1000

writer = csv.writer(open('hasil_csv/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
header_csv = ['Username', 'Fullname', 'Profil pic']
writer.writerow(header_csv)
while 1:
    var = {
        "shortcode":short_code,
        "first":50,
        "after":endcursor
    }

    headers = {'cookie':'sessionid=1530372735%3Abx34GUeT1hOVsz%3A12'}
    params = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(var)
    }
    respon = requests.get(url, headers=headers, params=params).json()
    try: users = respon['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('Wait for a second')
        time.sleep(2.5)
        continue

    for user in users:
        if count % jml_per_file == 0 and count!=0:
            counter_file += 1
            writer = csv.writer(open('hasil_csv/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
            header_csv = ['Username', 'Fullname', 'Profil pic']
            writer.writerow(header_csv)
        username = user['node']['username']
        fullname = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        count += 1
        print(count, username, fullname, profile_pic)
        writer = csv.writer(open('hasil_csv/{} {}.csv'.format(short_code, counter_file), 'a', newline='', encoding='utf-8'))
        data = [username, fullname, profile_pic]
        writer.writerow(data)


    endcursor = respon['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    hasnextpage = respon['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if hasnextpage == False: break
    time.sleep(0.5)
    # print(endcursor)