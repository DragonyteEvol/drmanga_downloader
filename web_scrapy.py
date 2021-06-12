from bs4 import BeautifulSoup
import requests
import os
import errno
import wget

def generateCaps(num_1,num_2):
    caps=[num_1]
    numvariable=num_1
    while num_2>num_1:
        numvariable=numvariable+1
        caps.append(numvariable)
        num_1+=1
    return caps

def scrapTumangaonline(url,arrayCaps):
    manga_name=str(url).replace("https://tumangaonline.site/manga/","")
    for x in arrayCaps:
        url_l=url + "/"+str(x)+"/"
        for i in range(20):
            if(i>0):
                url_i=url_l + str(i)
                r=requests.get(url_i)
                soup=BeautifulSoup(r.content,'lxml')
                tags=soup.find_all('img',{'class','img-responsive scan-page'})
                for tag in tags:
                    url_d=tag.get('src')
                    url_f=url_d.replace(" ","")
                    try:
                        folder='manga/'+manga_name+'/'+str(x)
                        os.makedirs(folder)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise
                    route='manga/'+manga_name+"/"+str(x)+'/'+str(i)+".png"
                    file=requests.get(url_f)
                    #wget.download(url_f,route)
                    open(route,'wb').write(file.content)
                    #os.system('wget '+url_f)
    return True


def scrapPageTumangaOnline(url):
    r=requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    tags=soup.find_all('a',{'tabindex','0'})
    for tag in tags:
        print(tag.find('span',{'class','text'}).getText())



