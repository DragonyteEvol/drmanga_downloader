import threading
from progress_bar import *
from tkinter import *
from functions_ui import *
from PIL import Image,ImageTk
from messagebox import * 
from io import BytesIO

#TUMANGAONLINE


root= Tk()
root.title("Manga Downloader")
frame = Frame(root,bg="#f8f5f1")
frame.pack()

#MENU
barmenu=Menu(root,bg="#f8f5f1",border=0,borderwidth=0)
root.config(menu=barmenu)

menu_archivo=Menu(barmenu,tearoff=0,bg="#f8f5f1")
menu_archivo.add_command(label="Salir",command=lambda:closeProgram())


menu_edicion=Menu(barmenu,tearoff=0,bg="#f8f5f1")
menu_edicion.add_command(label="Borrar Datos",command=lambda:clearData(entry_url_masive,entry_desde,entry_hasta))

menu_ayuda=Menu(barmenu,tearoff=0,bg="#f8f5f1")
menu_ayuda.add_command(label="Acerca de",command=lambda:InfoMessageBox(root,title="Dragonyte",btn_text="Aceptar",msg="Dragonyte\nV.1.0(unstable)\nPython 3.6"))
menu_ayuda.add_command(label="Guia")

#datayuda.add_command(label="Acerca de",command=infoAdicional)

barmenu.add_cascade(label="Archivo",menu=menu_archivo)
barmenu.add_cascade(label="Edicion",menu=menu_edicion)
barmenu.add_cascade(label="Ayuda",menu=menu_ayuda)



#URL ENTRY-LABEL
entry_url_masive=Entry(frame,width=50,borderwidth=0)
entry_url_masive.config(font=("Courier",10))
entry_url_masive.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
label_url=Label(frame,text="ejemplo: https://tumangaonline.site/manga/boku-no-hero-academia",bg="#f8f5f1")
label_url.config(font=("Courier",8))
label_url.grid(row=1,column=0,columnspan=3)

#SEARH ENTRY-LABEL
entry_search=Entry(frame,fg="#d8e3e7",borderwidth=0)
entry_search.config(font=("Courier",10),state="disabled")
entry_search.grid(row=0,column=3,padx=5,pady=5)
entry_search.insert(0,'Buscar')
label_search=Label(frame,text="ej:boku-no-hero-academia",bg="#f8f5f1")
label_search.config(font=("Courier",8))
label_search.grid(row=1,column=3)

#TITLE
label_title=Label(frame,text="AGREGA O BUSCA UN MANGA",bg="#f8f5f1")
label_title.config(font=("Courier bold",12),justify=LEFT)
label_title.grid(row=2,column=0,columnspan=3)


#DESCRIPTION
label_title=Label(frame,text="Copia y pega un link en la barra de la pagina tumangaonline.site sin capitulo como se muestra en el ejemplo, elige desde que capitulo hasta que capitulo quieres descargar y da click en play",bg="#f8f5f1",wraplength=300)
label_title.config(font=("Courier bold",8),justify=LEFT)
label_title.grid(row=3,column=0,columnspan=3)


#DOWNLOAD PART
label_desde=Label(frame,text="Desde:",bg="#f8f5f1")
label_desde.config(font=("Courier",8))
label_desde.grid(row=4,column=0)
entry_desde=Entry(frame,borderwidth=0)
entry_desde.config(font=("Courier",8))
entry_desde.grid(row=5,column=0,padx=5,pady=5)

label_hasta=Label(frame,text="Hasta:",bg="#f8f5f1")
label_hasta.config(font=("Courier",8))
label_hasta.grid(row=4,column=1)
entry_hasta=Entry(frame,borderwidth=0)
entry_hasta.config(font=("Courier",8))
entry_hasta.grid(row=5,column=1,padx=5,pady=5)

#IMG
img_base=Image.open("img/poster_null.jpg")
img_base=img_base.resize((160,200), Image.ANTIALIAS)
img_base=ImageTk.PhotoImage(img_base)
label_img=Label(frame,image=img_base)
label_img.grid(row=2,column=3,padx=5,pady=5,rowspan=6)



img_button=Image.open("img/icons/icon_play.png")
img_button=img_button.resize((55,50), Image.ANTIALIAS)
img_button=ImageTk.PhotoImage(img_button)
button_start=Button(frame,borderwidth=0,image=img_button,command=lambda:startProcessDownload(entry_url_masive.get(),entry_desde.get(),entry_hasta.get(),frame))
button_start.grid(row=4,column=2,rowspan=2)


#HILO
def startProcessDownload(url,from_cap,to,frame,button_start=button_start):
    thread = threading.Thread(target=starDownload,args=(url,int(from_cap),int(to),frame,button_start))
    thread.start()
    


root.mainloop()
