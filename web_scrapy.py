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

def scrapTumangaonline(url,arrayCaps,acept=0):
    manga_name=str(url).replace("https://tumangaonline.site/manga/","")
    same=scrapPageTumangaOnline(url)
    for x in arrayCaps:
        url_l=url + "/"+str(x)
        if(url_l in same):
            url_l=url + "/"+str(x)+"/"
        else:
            url_l=url + "/ "+str(x)+"/"
        acept=0
        i=1
        while i<40:
            if(acept>1):
                break
            if(i>0):
                url_i=url_l + str(i)
                r=requests.get(url_i)
                soup=BeautifulSoup(r.content,'lxml')
                tags=soup.find_all('img',{'class','img-responsive scan-page'})
                for tag in tags:
                    url_d=tag.get('src')
                    #url_f=url_d.replace(" ","")
                    url_f=url_d.strip()
                    try:
                        folder='manga/'+manga_name+'/'+str(x)
                        os.makedirs(folder)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise
                    route='manga/'+manga_name+"/"+str(x)+'/'+str(i)+".png"
                    file=requests.get(url_f)
                    if(file.status_code==404):
                        acept+=1
                    #wget.download(url_f,route)
                    open(route,'wb').write(file.content)
                    #os.system('wget '+url_f)
            i+=1
    return True


def scrapPageTumangaOnline(url):
    r=requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    tags= soup("a")
    caps=[]
    caps_f=[]
    for tag in tags:
        caps.append(tag.get('href'))

    for cap in caps:
        if(url+'/' in cap):
            caps_f.append(cap)
    return caps_f
 

