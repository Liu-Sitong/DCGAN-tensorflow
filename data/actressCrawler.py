import requests
from bs4 import BeautifulSoup
import os
import traceback


def download(url, filename):
    headers = {
        'Host': "bj.lianjia.com",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, sdch",
        'Accept-Language': "zh-CN,zh;q=0.8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
        'Connection': "keep-alive",
    }
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60,headers=headers)

        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        # url = 'https://oimagea3.ydstatic.com/image?id=-1318783469322185060&product=xue'
        r.close()
        # ir = requests.get(url)
        # if ir.status_code == 200:
        #     open(filename, 'wb').write(ir.content)

        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)


# def download(url, filename):
#     if os.path.exists(filename):
#         print('file exists!')
#         return
#     try:
#         r = requests.get(url, stream=True, timeout=60)
#         r.raise_for_status()
#         with open(filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=1024):
#                 if chunk:  # filter out keep-alive new chunks
#                     f.write(chunk)
#                     f.flush()
#         return filename
#     except KeyboardInterrupt:
#         if os.path.exists(filename):
#             os.remove(filename)
#         raise KeyboardInterrupt
#     except Exception:
#         traceback.print_exc()
#         if os.path.exists(filename):
#             os.remove(filename)


if os.path.exists('imgs') is False:
    os.makedirs('imgs')

start = 1
end = 30
search_items = ['あ', 'か', 'さ', 'た', 'な', 'は', 'ま', 'や', 'ら', 'わ']
for si in search_items:
    for i in range(start, end + 1):
        url = 'https://xxx.xcity.jp/idol/?kana=' + si + '&num=90&page=' + str(i)
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        avidol = soup.find('div', id='avidol')
        for img in avidol.find_all('img', class_="actressThumb"):
            target_url = 'http:' + img['src']
            filename = os.path.join('imgs', target_url.split('/')[-1].split('?')[0])
            download(target_url, filename)
        print(si + '%d / %d' % (i, end))
