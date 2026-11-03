import sys,os
from PIL import Image, ImageDraw, ImageOps
out=sys.argv[1]; fs=sys.argv[2:]
W=300;H=200;cols=6;rows=(len(fs)+cols-1)//cols
s=Image.new('RGB',(W*cols,(H+16)*rows),(30,30,30));d=ImageDraw.Draw(s)
for i,f in enumerate(fs):
  try:
    im=Image.open(f);im.draft('RGB',(W*2,H*2));im=ImageOps.exif_transpose(im).convert('RGB');im.thumbnail((W,H))
  except Exception as e: continue
  x,y=(i%cols)*W,(i//cols)*(H+16);s.paste(im,(x+(W-im.width)//2,y));d.text((x+3,y+H+2),f"{i} {os.path.basename(f)}",fill=(255,255,0))
s.save(out,quality=80)
