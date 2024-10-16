import requests
import parsel
##获取当如热点并用字典格式返回目标网址标题和网址
def check_redian():
    url='https://www.csdn.net/'
    cookies={"Cookie":"uuid_tt_dd=10_19728111350-1591782585631-689724; UN=Clannad47; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19728111350-1591782585631-689724!5744*1*Clannad47; dc_session_id=10_1639052218276.971305; p_uid=U010000; __bid_n=18382ddfec8f77811f4207; ssxmod_itna=QuD=iKYKYvqGx7wqBao=Ti0=dDtZhwpmxv4QAqQD/bDfO4iNDnD8x7YDvIfdSAzC0pwt8F=CDKHqGjfqm46F9e4natU+O4GLDmKDy4=EueDxpq0rD74irDDxD3DbSdDSDWKD9D0+kSBuqtDm4GWCqGfDDoDYR=nDitD4qDBIEdDKqGgCdP5Ck2UzlUdLkGPTYxyD0UQxBdH8cuo1PF5SkrTrp0aiqGySPGuRMtV/SbDCoUVnw0otYfvvDYRCEpxbAwP30xItrhvfSGqK7hoKiqP9Dhhn++dCDDAb0hdG74HeD===; ssxmod_itna2=QuD=iKYKYvqGx7wqBao=Ti0=dDtZhwpmxv4QAqG9W5NDBd2rdx7pwqG8fh3QzcWqidMbAgchhqfOlcbhdkUT70Qt5FZBnfiza775I51Qe+7XpNkw3uUNu/+j0mFH51lik=HLXkRgvo515Z511=c1Homz5ZmhAxcOdr9zcighFz9HWfaIFO9H=xSOMeaHhanrsPSrIZ7ioFSOo1o8QzPv2BOHolam5jhHV6G8P99dhx7Tkzj=gUTUQynm5q6mQ1Qcon2aZhe9=rkuzzmu5dzpgbg==rIE2aqL0VtOqtsG7qQl906iAFq5G2+jhOSyx4aAR2dIT4Nu+QwQCYq7Rwe42m5k0BHz5GjHmUc+DHH4oYryY=v495T3DlCHx7O562D804ETrK04y7PcqKwbNEB24oKpEeLrrS+M0vZbfa4gbxyrCS2f5/f5eSG3D071D5dYKW3eC+s1=KSoj+2KNGHW8khr5mEqYAjQE6yY5cT5spUH6KqAqMiqPGkoiNOYQ/15NAqD7=DYIq+u4KiX3M7YCQSGDD==; UserName=Clannad47; UserInfo=a4a5e645223a48729d9d55798477873e; UserToken=a4a5e645223a48729d9d55798477873e; UserNick=Clannad47; AU=88A; BT=1679883302157; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22Clannad47%22%2C%22scope%22%3A1%7D%7D; FPTOKEN=pYJcsuG+IuKzRTdDKTNo6yo+iH8aBJ+VY6XFPQJXQIE/Fh3Gq+b3pYgdkIbLVR3Ehr5NfKE7YqcNwy9djcikuKY+LfCJYzobXnzcYVJVlIbqi96Hay6MZsOU+GWn+Kvz6V7ZMoaPcE/inlgSlap/N1yLUOoHhc9NQ9ht7ujPwKyTFPCYT3NSukyp0qf7RHEOa7C0w2bjQ8QDgl6pIhyhJKrbyAyJxCGT9qSZehlEANHHYFraxr3tBAHsAe36mJAumXj0d1GkQK/lJ2JouOpuI3uGU8YCcOsK3jhUFivjGk60ZNg650jU4ozCwK+TRzGFMiBk3BtxXM8TuWCT09W9INsAGdRpQnWUUJTUMhNHghJjiEsGQOHVNW8hDu0k+yNSkLjvLeByvZFnSYzAjzs1Gw==|J1Hvmk9F1qpUNqyNQ9pBHWnjU36G7/j4sk7CzL42ptw=|10|4ddc620696709252b8c63d84564f1353; log_Id_view=2565; dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjY1NDY5OSwiZXhwIjoxNjkwNzczNjU3LCJpYXQiOjE2OTAxNjg4NTcsInVzZXJuYW1lIjoiQ2xhbm5hZDQ3In0.e_atP1dgtnlehfdhnq6wwIaW3sLYN9ElYocPRG0sMBo; c_dl_prid=1690173506171_158625; c_dl_rid=1690204073341_931282; c_dl_fref=https://huanmin.blog.csdn.net/article/details/124092793; c_dl_fpage=/download/qq_27595745/85002058; c_dl_um=-; log_Id_click=490; FCNEC=%5B%5B%22AKsRol8RfFxaO0_cS-GNqvZnRXiPBi_ECSp2d983If8sngAb2s2OKFc2jRt0_2dCutxKr3f-Uyz9llof6YrE6LikUiDIC9FeGB1S9k8U-h9hNJ8sdKYA2tqFnHWXfjxUUDUQScegBWdLgnXhs2tsqxxwZX_LV7gAYA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; https_ydclearance=c63fa6de566e01890370baea-c08b-4a06-808c-94fc2ef1b9a9-1690777748; https_waf_cookie=96b2ebf7-6316-4a02ae94e188f6b28cdfd8ceb339d776fc44; dc_sid=0c22e980f5095e34e1b0b02fc3e1c3c4; csrfToken=x3rcqw2Flute6QE2dYZte4OE; c_segment=12; dc_session_id=10_1639052218276.971305; www_red_day_last=red; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1690264739,1690265561,1690274054,1690770551; c_pref=https%3A//www.csdn.net/; c_ref=https%3A//cn.bing.com/; c_first_ref=cn.bing.com; c_first_page=https%3A//blog.csdn.net/SanyHo/article/details/115625778; c_dsid=11_1690770614948.671555; c_page_id=default; log_Id_pv=667; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1690770616; firstDie=1; __gads=ID=5ed3b46cd5f2c245-224fdafbb9dc0058:T=1679883306:RT=1690770618:S=ALNI_MZp70Q2opqEaRv0r-MQUhpz9ABDrw; __gpi=UID=00000be1ef37849d:T=1679883306:RT=1690770618:S=ALNI_MZfIXyOdHKale_bN-EAC_0DWEP54Q; dc_tos=ryn2yq"}
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.86"}
    res=requests.get(url=url,headers=headers)
    selecter=parsel.Selector(res.text)
    redian=selecter.xpath('//div[@class="headswiper-item"]/a/text()').getall()
    href=selecter.xpath('//div[@class="headswiper-item"]/a[@class="title"]/@href').getall()
    dict_redian={}
    redian_list=[]
    for i in redian:
        index=redian.index(i)
        dict_redian[i]=href[index]
    redian_list.append(dict_redian)
    return redian_list

if __name__=="__main__":
    print(check_redian())
  














