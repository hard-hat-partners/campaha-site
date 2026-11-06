from PIL import Image,ImageDraw,ImageFont
W,H=1200,630;NAVY=(40,39,52);BLUE=(28,174,237);YEL=(255,210,63);PINK=(255,79,139)
c=Image.new('RGB',(W,H),NAVY);d=ImageDraw.Draw(c)
# halftone dots on navy
for y in range(0,H,14):
  for x in range(0,W,14): d.ellipse((x,y,x+3,y+3),fill=(45,72,95))
# photo panel, right side, tilted-ish comic frame
ph=Image.open('/tmp/ca/src/img/hallway-group-lockers.jpg').convert('RGB')
pw,phh=600,470
src=ph.crop((60,250,1340,1190*0+250+int(1280*phh/pw)))
ch=ph.height;cw=int(ch*pw/phh);x0=(ph.width-cw)//2;src=ph.crop((x0,0,x0+cw,ch))
src=src.resize((pw,phh),Image.LANCZOS)
px,py=560,70
d.rectangle((px+14,py+14,px+pw+14,py+phh+14),fill=BLUE)
d.rectangle((px-6,py-6,px+pw+6,py+phh+6),fill=(255,255,255))
c.paste(src,(px,py));d.rectangle((px-6,py-6,px+pw+6,py+phh+6),outline=NAVY,width=0)
# logo on white sticker
logo=Image.open('/tmp/ca/src/img/logo-campaha.png').convert('RGBA');lw=380;logo=logo.resize((lw,int(logo.height*lw/logo.width)),Image.LANCZOS)
lx,ly=48,56;pad=18
d.rounded_rectangle((lx+7,ly+7,lx+lw+pad*2+7,ly+logo.height+pad*2+7),18,fill=YEL)
d.rounded_rectangle((lx,ly,lx+lw+pad*2,ly+logo.height+pad*2),18,fill=(255,255,255),outline=NAVY,width=4)
c.paste(logo,(lx+pad,ly+pad),logo)
# headline
F=ImageFont.truetype('/tmp/ca/be-vietnam-pro-latin-900-italic.ttf',64)
def mis(x,y,t,col):
  d.text((x+4,y+4),t,font=F,fill=PINK);d.text((x-3,y-2),t,font=F,fill=BLUE);d.text((x,y),t,font=F,fill=col)
y0=230
for i,(t,col) in enumerate([('ROLE MODELS',(255,255,255)),('SHOW UP.',(255,255,255)),('CAREERS',YEL),('OPEN UP.',YEL)]):
  mis(52,y0+i*70,t,col)
M=ImageFont.truetype('/tmp/ca/permanent-marker-latin-400-normal.ttf',26)
d.text((54,y0+4*70+18),'Dallas  +  Houston  ·  campaha.org',font=M,fill=BLUE)
# sticker on photo
S=ImageFont.truetype('/tmp/ca/permanent-marker-latin-400-normal.ttf',28)
t='Real role models. Real classrooms.';tb=d.textbbox((0,0),t,font=S);tw=tb[2]-tb[0];sx,sy=px+pw-tw-50,py+phh-30
st=Image.new('RGBA',(tw+40,60),(0,0,0,0));sd=ImageDraw.Draw(st);sd.rectangle((0,0,tw+39,59),fill=YEL,outline=NAVY,width=4);sd.text((20,8),t,font=S,fill=NAVY)
st=st.rotate(4,expand=True,resample=Image.BICUBIC);c.paste(st,(sx,sy),st)
c.save('/tmp/ca/og-v2.jpg',quality=86,optimize=True)
