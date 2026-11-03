import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from cut import build
V=os.path.expanduser('~/projects/thedjaone-site/assets/video/')
R=[('nashville',0.5,2.0),('nashville',168,2.2),('mia-22',36,2.0),('mia-22',42,2.2),('nashville',210,2.2),('mia-22',90,2.0),('mia-22',147,2.0),('nashville',434,2.2),('nashville',476,2.2),('40th-birthday',24,2.0),('40th-birthday',69,1.2),('mia-22',203,2.0),('atl-22',200,2.2),('atl-22',400,2.0),('birmingham',30,2.4),('mia-22',381,2.0),('mia-22',417,2.0),('nashville',560,2.2),('mia-22',358,2.0),('nashville',364,2.4)]
build('reel',R,1920,1080,True,V+'reel-1080.mp4',24)
