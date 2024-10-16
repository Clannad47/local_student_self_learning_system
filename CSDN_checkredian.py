import requests
import parsel
##获取当如热点并用字典格式返回目标网址标题和网址
def check_redian():
    url='https://www.csdn.net/'
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
  














