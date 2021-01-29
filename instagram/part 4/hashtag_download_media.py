import requests
import json

count = 0
end_cursor = ''
while True:
    url1 = 'https://www.instagram.com/explore/tags/coklatbaruenak/?__a=1&max_id={}'.format(end_cursor)
    respon1 = requests.get(url1).json()
    short_codes = respon1['graphql']['hashtag']['edge_hashtag_to_media']['edges']

    for scode in short_codes:
        short_code = scode['node']['shortcode']
        url2 = 'https://www.instagram.com/p/{}/?__a=1'.format(short_code)
        respon2 = requests.get(url2).json()
        username = respon2['graphql']['shortcode_media']['owner']['username']
        print(username)

        count += 1
        #print(f"{count}.{short_code}")
    end_cursor = respon1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    has_next_page = respon1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    if has_next_page == False: break