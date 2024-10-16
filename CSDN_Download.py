import subprocess
import requests
import parsel
import pdfkit

html='''<!doctype html>
 <html>
 <head>
     <meta charset = "UTF-8">
     <title>Document</title>
 </head>
 <body>
     {content}
 </body>
 </html>'''

headers = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
def get_title(url):
    res=requests.get(url=url,headers=headers)
    selector=parsel.Selector(res.text)
    title=selector.xpath('//h1/text()').get()
    return title

def get_html(url):
    title=get_title(url)
    response = requests.get(url,headers = headers)
    selector = parsel.Selector(response.text)
    articel = selector.css('article').get()
    html.format(content=articel)
    myconfig = pdfkit.configuration(wkhtmltopdf="D:/software/wkhtmltopdf/bin/wkhtmltopdf.exe")
    file_name = f'./data/pdf/{title}.pdf'
    html_name=f'./data/html/{title}.html'
    #pdb.set_trace()
    with open(html_name, mode = 'w', encoding = 'utf-8') as f:
         f.write(html.format(content = articel))
         f.close()
    try:
        pdfkit.from_file(html_name,file_name, configuration=myconfig)
        print(title+"--------已下载完成")
        subprocess.Popen(['start', '', file_name], shell = True)
        return True
    except:
        print("title内含有非法字符不能作为文件名保存")
        return False


if __name__=='__main__':
    get_html('https://blog.csdn.net/qq_14873105/article/details/51394026')