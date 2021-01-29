import requests
import json
import time
import csv

queryhash = 'bc3296d1ce80a24b1b6e40b1e72903f5'
url = 'https://www.instagram.com/graphql/query'

endcursor = ''
short_code = 'CI75SaQsAJW'
count = 0
counter_file = 1
jml_per_file = 1000

writer = csv.writer(open('hasil_comments/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
header_csv = ['Username', 'Text']
writer.writerow(header_csv)

while 1:
    var = {"shortcode":short_code,"first":50, "after":endcursor}
    headers = {'cookie':'sessionid=1530372735%3Abx34GUeT1hOVsz%3A12'}
    params = {
        'query_hash': queryhash,
        'variables': json.dumps(var)
    }
    respon = requests.get(url, headers=headers, params=params).json()

    try:
        users = respon['data']['shortcode_media']['edge_media_to_parent_comment']['edges']
    except:
        print('Wait for a second')
        time.sleep(2.5)
        continue

    # count = 0
    for user in users:
        if count % jml_per_file == 0 and count!=0:
            counter_file += 1
            writer = csv.writer(open('hasil_comments/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
            header_csv = ['Username', 'Text']
            writer.writerow(header_csv)
        count += 1
        username = user['node']['owner']['username']
        text = user['node']['text']
        writer = csv.writer(open('hasil_comments/{} {}.csv'.format(short_code, counter_file), 'a', newline='', encoding='utf-8'))
        data = [username, text]
        writer.writerow(data)
        print(f"{count}. {username} - {text}")

    endcursor = respon['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor']
    hasnextpage = respon['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['has_next_page']
    if hasnextpage == False: break
    time.sleep(1)