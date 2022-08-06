from tkinter import *
from pytube import YouTube
root =Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Youtube Vedio Downloader")
Label(root,text= "Download vedios for free",font="san-serif 15 bold").pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste the link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 35, y = 100)
#Button(root, text='DOWNLOAD', font='san-serif 16 bold', bg='blue',command="download").place(x=180, y=150)
path="C:/Users/Jyoti/YoutubeVedios"
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download(path)
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'purple', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()