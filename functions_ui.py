from web_scrapy import *
from progress_bar import *
from tkinter import messagebox
import notify2
import sys

#FUNTIONAL FUNCT
def starDownload(url,from_cap,to,frame,button):
    button.config(state="disabled")
    progress_bar = Progress_Bar(frame)
    if(scrapTumangaonline(url,generateCaps(from_cap,to))):
        progress_bar.grid_forget()
        button.config(state="normal")
        #NOTIFY
        try:
            notify2.init("wee-notifier")
            wn = notify2.Notification("Manga Downloader","La descarga ha terminado", "gtk-ok")
            wn.set_urgency(notify2.URGENCY_CRITICAL)
            wn.set_timeout(5000)
            wn.show()
        except Exception as error:
            print('', 'notify2: {0}'.format(error))
        return True
    else:
        progress_bar.grid_forget()
        button.config(state="normal")

#FUNCTIONS MENU
def closeProgram():
    sys.exit()

def about():
    messagebox.showinfo("Dragonyte","Version 1.0 unstable")

def clearData(l1,l2,l3):
    l1.delete(0,'end')
    l2.delete(0,'end')
    l3.delete(0,'end')
