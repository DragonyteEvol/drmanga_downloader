from web_scrapy import *
def starDownload(url,from_cap,to,bar,text):
    if(scrapTumangaonline(url,generateCaps(from_cap,to))):
        bar.grid_forget()
        text.grid_forget()

