import urllib.request
import requests
import json

from lxml import etree


def jd():
    data = {
        "keyword": "电脑配件",
        "enc": "utf - 8",
        "wq": "电脑配件",
        "pvid": "765cd0a4985a4a5abdce0418d7419b76",
    }
    handers = {
        "user - agent": "Mozilla / 5.0(Linux;Android6.0;Nexus 5 Build / MRA58N) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 83.0.4103.106MobileSafari / 537.36",
        "referer": "https: // www.jd.com /?cu = true & utm_source = baidu - pinzhuan & utm_medium = cpc & utm_campaign = t_288551095_baidupinzhuan & utm_term = 0f3d30c8dba7459bb52f2eb5eba8ac7d_0_8ed60e328e1440db8db3a12c67b47196",
        "cookie": "__jdu=1278778394; shshshfpa=7c62b438-e046-5cc8-f108-1d77e0255b17-1588141450; shshshfpb=pgVc%2FqRYThZFYwkzyg1h1hg%3D%3D; areaId=2; ipLoc-djd=2-2841-51980-0; o2State={%22webp%22:true%2C%22lastvisit%22:1592480334997}; unpl=V2_ZzNtbUpWQx18ABRceRheUGIBQQ0SX0MRclwTBHwcCQM3V0ZZclRCFnQUR1NnGVUUZAEZX0pcQxxFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsaWgxhBRtfSlJzJXI4dmR7HVQDYwEiXHJWc1chVE9XehpcBCoDEVtLUUUcdwBDZHopXw%3d%3d; pinId=K_VaptbQ0RDRALWj3HCmELV9-x-f3wj7; pin=jd_6f81e51734b39; unick=jd_180193qgo; ceshi3.com=000; _tp=TKO%2B2ryFugbO%2FiIUmW%2BDbMNcdoPxy1n7Bvz2h3EowSE%3D; _pst=jd_6f81e51734b39; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_901989c9303d43baa9156eda64d7aee5|1592494969407; __jda=76161171.1278778394.1588141448.1592490606.1592494759.17; __jdb=76161171.12.1278778394|17.1592494759; __jdc=76161171; shshshfp=2e2fd805905e1c6c163652b29eaab464; shshshsID=73f337b0828e7c5219f44a052e980dc4_6_1592495447853; TrackID=1YB_pvwwPh-5nubf7U39Zm5tcGVceT6rmQHag2q2LRBSAtAmI6Cp9G40mxajexNEWyabv-lCbCY9nY_wwP1f9rQAFZD717OY30u3Wc-MzrlV8UDm1WcdGx1cwBYyDIyKd; thor=3276108707DB2AFF6EB7D8C15042AAAAF24C872B844D53FF2D54E008272B3CCB3D096EB85A57BC3EFA347BB10027F632EAB545CB1D377941C9323131E942C5D834E64AC483B4E2C91FA102AA5698E4287413237A31482730BF11614BBAF893A260A45FB0CDDC81D4ADCB067647724B592D6F9DF8CE35CC9AC3F9062F1354BCC02A2A2DEFE40EC1D6ABD0B66F602E00A27B120B3244D5AAD396B16223FBC8490D; logining=1",
        "accept-encoding": "gzip, deflate, br",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }
    url = "https://www.jd.com/"
    response = requests.get(url=url,params=handers,data=data)
    html = etree.HTML(str(response))
    ul = html.xpath('//div/@text()')  # 获取ul下的所有class标签和lists属性
    # print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
    print(ul)


def jd1(ret):
    # jd()
    url = "https://search.jd.com/Search?keyword="+ret+"enc=utf-8&suggest=1.his.0.0&wq=&pvid=9f513c7daa974702b07b773a17fa2ebc"
    data = {
        "keyword": "电脑配件",
        "enc": "utf-8",
        "suggest": "1.his.0.0",
        "wq":"" ,
        "pvid": "434314a73aa84624aa116272fd3ddc8a",
    }
    handers = {
        "cookie": "__jdu=1278778394; shshshfpa=7c62b438-e046-5cc8-f108-1d77e0255b17-1588141450; shshshfpb=pgVc%2FqRYThZFYwkzyg1h1hg%3D%3D; qrsc=3; areaId=2; ipLoc-djd=2-2841-51980-0; rkv=V0600; unpl=V2_ZzNtbUpWQx18ABRceRheUGIBQQ0SX0MRclwTBHwcCQM3V0ZZclRCFnQUR1NnGVUUZAEZX0pcQxxFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsaWgxhBRtfSlJzJXI4dmR7HVQDYwEiXHJWc1chVE9XehpcBCoDEVtLUUUcdwBDZHopXw%3d%3d; pinId=K_VaptbQ0RDRALWj3HCmELV9-x-f3wj7; pin=jd_6f81e51734b39; unick=jd_180193qgo; ceshi3.com=000; _tp=TKO%2B2ryFugbO%2FiIUmW%2BDbMNcdoPxy1n7Bvz2h3EowSE%3D; _pst=jd_6f81e51734b39; TrackID=1YB_pvwwPh-5nubf7U39Zm5tcGVceT6rmQHag2q2LRBSAtAmI6Cp9G40mxajexNEWyabv-lCbCY9nY_wwP1f9rQAFZD717OY30u3Wc-MzrlV8UDm1WcdGx1cwBYyDIyKd; 3AB9D23F7A4B3C9B=C4HFMDOP6XHTLBWDTYND7SVQXQPAOXWPGT4C6J7HCB3DSPZ3DLKFNSNYIKH3DJDH5CTWBB334PXNHWB5RTIJK6IJLA; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_901989c9303d43baa9156eda64d7aee5|1592496155140; thor=3276108707DB2AFF6EB7D8C15042AAAAF24C872B844D53FF2D54E008272B3CCB3D096EB85A57BC3EFA347BB10027F632831486F12DB9D733B7F13670CD051063734DC4CB7A27A309959903D9087EBEB894A7B5A1206A1A1BD904C0DCC5A09606423E77506977C29D43F6D9AE03F627F1576D1764F657BE955D95DCE9C671E461D4E7AE178EFD984486D667EC9763C49EB7AEE6B29E4B000B4A3EFE201B6A3D99; __jda=122270672.1278778394.1588141448.1592490606.1592494759.17; __jdc=122270672; __jdb=122270672.22.1278778394|17.1592494759; shshshfp=a40ad22ca2b5b9242a8efc973486ecdf; shshshsID=73f337b0828e7c5219f44a052e980dc4_14_1592496985669",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        ":authority": "search.jd.com",
        ":method": "GET",
        ":path": "/ Search?keyword = % E7 % 94 % B5 % E8 % 84 % 91 % E9 % 85 % 8D % E4 % BB % B6 & enc = utf - 8 & pvid = 5024d2c07f4c46a5899494c55bff4217",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }
    response = requests.get(url=url, params=handers, data=data)
    print(response.text)


if __name__ == '__main__':
    jd()
    # jd1("电脑配件")





