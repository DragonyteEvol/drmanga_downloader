from warnings import catch_warnings
from web_scrapy import *
from progress_bar import *
def starDownload(url,from_cap,to,frame,button):
    button.config(state="disabled")
    progress_bar = Progress_Bar(frame)
    if(scrapTumangaonline(url,generateCaps(from_cap,to))):
        progress_bar.grid_forget()
        button.config(state="normal")
        return True
    else:
        progress_bar.grid_forget()
        button.config(state="normal")

