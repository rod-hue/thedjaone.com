import subprocess, sys, os
SRC=os.path.expanduser('~/projects/thedjaone-site/_src/dropbox/')
TMP=os.path.expanduser('~/projects/thedjaone-site/_src/cuts/')
GRADE={'atl-22':'eq=contrast=1.22:saturation=1.35:gamma=0.92,'}
def seg(name, src, t, d, w, h, audio):
    out=f'{TMP}{name}.mp4'
    g=GRADE.get(src,'')
    vf=f"{g}scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1,fps=30000/1001"
    cmd=['ffmpeg','-v','error','-y','-ss',str(t),'-i',f'{SRC}v-{src}.mp4','-t',str(d),'-vf',vf]
    if audio: cmd+=['-af',f'afade=t=in:d=0.04,afade=t=out:st={d-0.06}:d=0.06,aresample=48000','-ac','2','-c:a','aac','-b:a','160k']
    else: cmd+=['-an']
    cmd+=['-c:v','libx264','-preset','medium','-crf','16','-pix_fmt','yuv420p',out]
    subprocess.run(cmd,check=True); return out
def build(listfile, clips, w, h, audio, final, crf, extra=[]):
    outs=[seg(f'{listfile}_{i:02d}',s,t,d,w,h,audio) for i,(s,t,d) in enumerate(clips)]
    with open(f'{TMP}{listfile}.txt','w') as f:
        for o in outs: f.write(f"file '{o}'\n")
    cmd=['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{TMP}{listfile}.txt']+extra
    if audio: cmd+=['-af','loudnorm=I=-16:TP=-1.5:LRA=11','-c:a','aac','-b:a','160k']
    else: cmd+=['-an']
    cmd+=['-c:v','libx264','-preset','slow','-crf',str(crf),'-pix_fmt','yuv420p','-movflags','+faststart',final]
    subprocess.run(cmd,check=True)
    print(final, os.path.getsize(final)//1024,'KB')
