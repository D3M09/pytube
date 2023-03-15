#Simple Yt Video Downloader
import os,sys,time
from time import sleep as ghum
from pytube import YouTube as ytt

W = "\033[1;97m"
D = '\033[94m'
G = "\033[1;32m"
R = "\033[1;31m"
H = '\033[1;30m'
Y = '\033[96m'
S = '\033[92m'
Q = '\033[1;37m'
T = '\033[1;34m'

os.system('clear')
os.system('#')
link = input(f'{D}[{R}!{D}] {Y}Input Link :{W}')
yt = ytt(link)
print(f'{D}[{R}•{D}] {Y}Title:{G}', yt.title)
print(f'{D}[{R}•{D}] {Y}Total Views:{G}', yt.views)
print(f'{D}[{R}•{D}] {Y}Length:{G}',yt.length )

ghum(5)

yts = yt.streams.get_highest_resolution()

print(f'{Y}[{R}•{D}]{Y} Downloading Please Wait..!!')
yts.download()
print(f'{Y}[{R}•{D}]{Y} Download Completed! \n({link})')
