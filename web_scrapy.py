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
    same=scrapPageTumangaOnline(url)
    for x in arrayCaps:
        url_l=url + "/"+str(x)
        if(url_l in same):
            url_l=url + "/"+str(x)+"/"
        else:
            url_l=url + "/ "+str(x)+"/"
        for i in range(505):
            if(downloadPage(i+1,url_l,manga_name,x)==False):
                break
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
 
def downloadPage(i,url_l,manga_name,x):
    url_i=url_l.replace(" ","") + 'p/' +str(i)
    print(url_i)
    r = requests.get(url_i)
    f= open('lala.txt','w')
    f.write(str(r.content))
    soup=BeautifulSoup(r.content,'lxml')
    # wp-manga-chapter-img img-responsive effect-fade lazyloaded
    tags=soup.find_all('img',{'class','wp-manga-chapter-img'})
    if(len(tags)==0):
        print("nada")
        return False
    for tag in tags:
        url_d=tag.get('data-src')
        print("entre")
        print(url_d)
        print("entre esto")
        #url_f=url_d.replace(" ","")
        url_f=url_d.strip()
        try:
            folder='manga/'+manga_name+'/'+str(x)
            os.makedirs(folder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        route='manga/'+manga_name+"/"+str(x)+'/'+str(i)+".webp"
        file=requests.get(url_f)
        print(i)
        #wget.download(url_f,route)
        open(route,'wb').write(file.content)
        #os.system('wget '+url_f)
    return True

def downloadAllCaps(url_z):
    same=scrapPageTumangaOnline(url_z)
    for url in same:
        manga_name=str(url_z).replace("https://tumangaonline.site/manga/","")
        manga_cap=str(url).replace("https://tumangaonline.site/manga/","")
        for i in range(505):
            url_i=url+'/'+str(i)
            r = requests.get(url_i)
            soup=BeautifulSoup(r.content,'lxml')
            tags=soup.find_all('img',{'class','img-responsive scan-page'})
            if(len(tags)==0):
                return False
            for tag in tags:
                url_d=tag.get('src')
                #url_f=url_d.replace(" ","")
                url_f=url_d.strip()
                try:
                    folder='manga/'+manga_name+'/'+manga_cap
                    os.makedirs(folder)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
                route='manga/'+manga_name+"/"+manga_cap+'/'+str(i)+".png"
                file=requests.get(url_f)
                print(i)
                #wget.download(url_f,route)
                open(route,'wb').write(file.content)
                #os.system('wget '+url_f)

        


