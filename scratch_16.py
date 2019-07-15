from tkinter import *
pencere=Tk()
asilisim="saniye"
asilsifre="nur"
def girisyap():
    sifre=sifregiris.get()
    isim=isimgiris.get()
    if(sifre==asilsifre and isim==asilisim):
        girisdurumu.config(text="yanlış")
    else:
        girisdurumu.config(text="dogru")
    isim=Label(pencere,text="Adınız")
    isim.grid(now=0,column=0)
    isimgiris=Entry(pencere,width="8")
    isimgiris.grid(now=0,column=1)
    sifre = Label(pencere, text="şfreniz")
    sifregiris=Entry(pencere,width="8")
    sifre.grid(now=1,column=0)
    sifregiris.grid(now=1,column=1)
    giris = Button(pencere, text="giriş", command=girisyap())
    giris.grid(row=3, column=1)
    girisdurumu = Label(pencere, text="")
    girisdurumu.grid(row=3, column=2)


    pencere.mainloop()