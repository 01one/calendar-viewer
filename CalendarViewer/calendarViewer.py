#  Copyright 2022-2023 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
import pygame,sys
from pygame.locals import*
import time
import datetime
import calendar
pygame.init()
clock=pygame.time.Clock()
screen_width=1200
screen_height=650
screen=pygame.display.set_mode((screen_width,screen_height),RESIZABLE)
white=(255,255,255)
black=(0,0,0)


shadow=pygame.image.load('shadow.png') 
shadow1=pygame.image.load('shadow1.png') 
background1=pygame.image.load('background11.png')
background_main=pygame.image.load('background_main.png')
shadow11=pygame.image.load('shadow11.png')
shadow_background=pygame.image.load('shadow_background.png')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)        

months=['January','February','March','April','May','June','July','August','September','October','November','December']
days={'Su':'Sunday','Mo':'Monday','Tu':'Tuesday','We':'Wednesday','Th':'Thursday','Fr':'Friday','Sa':'Saturday'}

this_month=time.localtime()
month=this_month.tm_mon
year=this_month.tm_year
day=this_month.tm_yday
today=this_month.tm_mday

calendar.setfirstweekday(calendar.SUNDAY)
cal=calendar.month(year,month)


cal=cal.splitlines()
cal.pop(0)
dates=cal[0]
dates=dates.split(' ')
row2=cal[1]
row2=row2.split(' ')
cal.pop(0)
r_txt=[]


def calculate(row):
	row_txt=[]
	if len(row)%2==0:
		row=[row[i] for i in range(len(row)) if (i+1)%2==0]
	else:
		row=[row[i] for i in range(len(row)) if (i+1)%2!=0]
	x,y=0,len(row)
	x2,y2=x,y
	x3,y3=x,y
	row1=[item for item in row if item!='']
	n=7-len(row1)
	s=['' for i in range(n)]					
	if row[x2]=='' and row[-1]!='':
		while row[x2]=='':
			x2+=1
		new=s[:]+row[x2:]
		row_txt=new
	elif row[x3]!='' and row[-1]=='':
		while row[x3]!='':
			x3+=1
		new=row[:x3]+s[:]
		row_txt=new
	else:
		row_txt=row[:]
	r_txt.append(row_txt)
calculate(row2)
new=[]
row1=cal[1]
row1=row1.split(' ')
row1=[item for item in row1 if item!='']
n1=3
if len(cal)==6:
	n1=4
for i in range(n1):
	a=cal[i+2]
	a=a.split(' ')
	for j in range(1,len(a)+1):
		if a[j-1]!='':
			new.append(a[j-1])

new=[item for item in new if item!='']
x=r_txt[0]
all_txt=dates+r_txt[0]+row1+new
t=all_txt.index(str(today))

all_rect=[]
def draw(x=7,y=7):
	y1=100
	for i in range(x):
		x1=100
		for i in range(y):	
			square=(x1,y1,70,70)
			all_rect.append(square)
			x1+=80
		y1+=80
draw()

class ShowTxt():
	def __init__(self,btn_txt,c_rect,btn_color="#4D4D4D",corner=5,font_s=50,r=True):
		self.btn_txt=btn_txt
		self.x=c_rect[0]
		self.y=c_rect[1]
		self.x1=c_rect[2]
		self.y1=c_rect[3]
		self.btn_font=pygame.font.Font('Genos-Bold.ttf', font_s)
		self.btn_color=btn_color
		self.color0="#AEC7CF"
		self.color1="#D81B1B"
		self.btn_position=pygame.Rect(self.x,self.y,self.x1,self.y1)
		self.button_txt=self.btn_font.render(self.btn_txt,True,self.color0)
		
		if self.btn_position.collidepoint(mouse_position):
			self.btn_color='#08a60d'
		else:
			self.btn_color=self.btn_color
		if r==True:
				pygame.draw.rect(screen,self.btn_color, self.btn_position, border_radius=corner)
		txt_rect=self.button_txt.get_rect()
		txt_rect.center=self.btn_position.center
		screen.blit(self.button_txt,txt_rect)

def draw_txt():

	for i in range(len(all_txt)):
		a=all_rect[i]
		screen.blit(shadow,(a[0],a[1]))
		if i<t:
			ShowTxt(all_txt[i],all_rect[i])
		elif i==t:
			ShowTxt(all_txt[i],all_rect[i],btn_color=black)
			
		else:
			ShowTxt(all_txt[i],all_rect[i],btn_color='#106b21')
		
date_rect=[]
r_new=all_txt
x11=r_new.index('1')
r_new=[item for item in r_new if item!='']
c1=r_new[:7]
c2=r_txt[0]
k=c2.index('1')
k1=c1[k]
date_list=[]
n_d=0
while n_d!=len(r_new):
	x_c=c1[k]
	if (k+1)<=6:
		k+=1
	else:
		k=0
	n_d+=1
	date_list.append(x_c)
t_day=date_list[today-1]
t_day=days[t_day]
r_new=r_new[7:]
r_new_r=[]
txt1=t_day+' '+str(today)+' '+months[month-1]+' '+str(year)
def detail():
	screen.blit(shadow1,(35,35));ShowTxt(txt1,(370,40,20,40),r=False);ShowTxt(txt,(520,580,250,40),font_s=20,r=False)

quote='“If you are depressed you are living in the past. If you are anxious you are living in the future. If you are at peace you are living in the present.”  Lao Tzu                '
x=len(quote)
txt=''
n=0
program_running=True
while program_running:
	now=datetime.datetime.now()
	if today!=now.day:
		pygame.quit()
		sys.exit()
	pygame.display.set_caption(str(time.ctime())+'    '+txt)
	if len(txt)<x:
		txt=quote[:int(n)]
		n+=.40
	else:
		n=0
		txt=quote[:int(n)]
	clock.tick(50)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.VIDEORESIZE:
			screen_width,screen_height=event.size
			background_main=pygame.transform.scale(background_main,(screen_width+50,screen_height+50))
		mouse_position=pygame.mouse.get_pos()
	screen.fill(white)

	screen.blit(shadow_background,(600,0))
	screen.blit(shadow11,(600,300))
	screen.blit(background_main,(-10,-10))
	screen.blit(background1,(50,50))
	draw_txt()
	detail()
	pygame.display.update()
