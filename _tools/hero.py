import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from cut import build
V=os.path.expanduser('~/projects/thedjaone-site/assets/video/')
H=[('40th-birthday',69,1.2),('nashville',154,1.4),('nashville',168,1.4),('mia-22',36,1.4),('nashville',210,1.4),('mia-22',42,1.4),('atl-22',580,1.4),('nashville',196,1.4),('mia-22',203,1.4),('nashville',364,1.4),('nashville',560,1.4),('mia-22',21,1.4),('atl-22',200,1.6),('mia-22',46,1.4)]
build('hero',H,1920,1080,False,V+'hero-1080.mp4',27)
build('herom',H,720,1280,False,V+'hero-m.mp4',27)
