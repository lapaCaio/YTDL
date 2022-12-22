from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


# functions
def select_path():
    # allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title('Baixando...')
    # download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Completo!')


screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# image logo
logo_img = PhotoImage(file='yt-logo.png')
# redimencionar
logo_img = logo_img.subsample(12, 12)
canvas.create_image(250, 80, image=logo_img)

# campo de link
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Link para Download:".upper(), font=('Arial', 12))

# selecionando pasta para salvar o arquivo
path_label = Label(screen, text="Selecione a Pasta do Download".upper(), font=('Arial', 12))
select_btn = Button(screen, text="Selecionar", command=select_path)

# adicionando na janela
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# botões de dowload
download_btn = Button(screen, text="Baixar", command=download_file)

# adicionar á tela
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
