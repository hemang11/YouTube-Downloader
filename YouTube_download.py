import tkinter as tk
from tkinter import ttk,font,filedialog
from tkinter import messagebox as m_box
from pytube import YouTube
from PIL import ImageTk,Image
from threading import Thread 
import os

win=tk.Tk()
win.title('You Tube Downloader (~By Hemang)')
win.geometry('700x400')
win.resizable(0,0)
win.wm_iconbitmap('YouTube.ico')

## Code here 

# variables
url=os.getcwd()
file_size=0

# Image and Search Box
image=ImageTk.PhotoImage(Image.open('A.png').resize((90,90)))
image_label=ttk.Label(win,image=image)
image_label.grid(pady=15)
search=tk.StringVar()
search=tk.Entry(win,width=100,textvariable=search,bd=4) # to use furthur prop tk class of entry is used than tkinter
search.grid(padx=50)

# Functions

def thread():                        # Thread is Handling our GUI so that our main program doesn't gets hanged 
    thread=Thread(target=click)      # On click button thread function is called and then thread is calling click function
    thread.start()                   # So our Main gui doesn't gets affected
 
def browse():
    global url,browse
    try:
        url=filedialog.askdirectory() # Ask directory is used to fetch the directory
        browse.configure(text='Selected')
    except:
        m_box.showerror('Error','Unexpected Results.Select the correct Directory')
        browse.configure(text='Browse folder..')

# Button function
def progress(stream=None, chunk=None, file_handle=None,remaining=0):
    global file_size
    #print(file_size,remaining,type(remaining)) remaining is NoneType and cannot be converted to integer so it is set to 0
    file_downloaded=(file_size-remaining)    # Percentage of file downloaded
    per=(file_downloaded/file_size)*100
    btn.config(text="{:00.0f} % downloaded".format(per))

def click():
    global btn,search,file_size
    search_var=search.get()
    selected=select.get()
    btn.config(text='Please Wait',fg='black',bg='white',state=tk.DISABLED)
    try:
        yt=YouTube(search_var,on_complete_callback=progress) # It checks the progress of the video downloaded

        if selected=='Video':
            video=yt.streams.filter(progressive=True).filter(subtype='mp4').order_by('resolution').desc().first()
        elif selected=='Audio':
            video=yt.streams.filter(only_audio=True).desc().first()
        else:
            print('RadioButton Selection Error')

        file_size=video.filesize
        size=(file_size/1024000)
        size=round(size,2)
        video.download(url)
        m_box.showinfo('Success',f'Download Successfully Completed.The Size of Downloaded {selected} file is {size} MB')
        btn.configure(fg='white',bg='green',text='Download',state=tk.NORMAL)
        browse.configure(text='Browse folder..')
        search.delete(0,tk.END)
    except Exception as e:
        print(e)
        m_box.showerror('Error','Video cannot be downloaded.Enter the Url again or make sure Url is Correct !!!!')
        btn.configure(fg='white',bg='green',text='Download',state=tk.NORMAL)
        search.delete(0,tk.END)

# Browse option
browse=tk.Button(win,text='Browse folder..',command=browse)
browse.configure(fg='black')
browse.grid(pady=19)

# Radio Buttons
select=tk.StringVar()
radio_font=font.Font(family='Arial',size=12,weight='bold')
video_r=tk.Radiobutton(win,text='Video',value='Video',variable=select,font=radio_font)
video_r.select()
video_r.grid()
audio_r=tk.Radiobutton(win,text='Audio',value='Audio',variable=select,font=radio_font)
audio_r.grid()

# Download Button
btn=tk.Button(win,text='Download',command=thread)
font_measure=font.Font(family='Helvetica',size='18',weight='bold')
btn.configure(fg='white',bg='green')
btn['font']=font_measure
btn.grid(pady=10)

# status Bar
status_font=font.Font(family='Helvetica',size='10',weight='bold')
status_bar=ttk.Label(win,text='The Application will Download the Best Video/Audio Quality for You')
status_bar.configure(background='red',foreground='white')
status_bar['font']=status_font
status_bar.grid(pady=25)

win.mainloop()
# # We can also download a complete Youtub Playlist

# yt=YouTube('https://www.youtube.com/watch?v=lTTajzrSkCw')
# t=yt.streams.filter(only_audio=True).first()
# print(t.filesize)
# win.mainloop()