import moviepy,random,string,json,os,sys
import platform
def tryremove(file):
    try:
        os.remove(file)
    except Exception as e:
        return e
def clean():
    pass
clean()
tryremove("./VIDEO/.DS_Store")
tryremove("./PNG/.DS_Store")
tryremove("./MUSIC/.DS_Store")
tryremove("./US/.DS_Store")
donefiles=[]
#from skimage.filters import *
from skimage.filters import gaussian
# Подгрузка настроек
afps=[-1,1]
angles=[-3,3]
settings = json.loads(open('settings.json','r').read())
randeffectslimit=settings['rel']
doRotate = settings['doRotate']
doBlurIn = settings['doBlurIn']
doMirror = settings['doMirror']
vidc = settings['vidc']
mind = settings['mind']
maxd = settings['maxd']
showEffect = settings['showEffect']
doblur = settings['doblur']
blursigma = settings['blursigma']
from moviepy.editor import *
from pathlib import Path

def create_file_list(folder):
    return [str(f) for f in Path(folder).iterdir()]

def create_image_list(folder):
    image_list=[]
    folder = Path(folder)
    if folder.is_file():
        image = ImageClip(str(folder),duration=1)
        image_list.append(image)
    if folder.is_dir():
        for file in sorted(folder.iterdir(), reverse=True):
            image = ImageClip(str(file),duration=1)
            image_list.append(image)
    return image_list

def filename(folder):
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    file_name = str(Path(folder).joinpath(file_name + '.mp4'))
    return file_name

def filenamepre(folder):
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    file_name = str(Path(foldertmp).joinpath(file_name + '-PRE.mp4'))
    return file_name

def filenameprepre(folder):
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    file_name = str(Path(foldertmp).joinpath(file_name + '-PRE-pre.mp4'))
    return file_name

def blur(image):
    return gaussian(image.astype(float), sigma=blursigma)

#Папка для сохранения видео
result_folder = os.path.join(sys.argv[0].replace("main.py",""),'US')
foldertmp = os.path.join(sys.argv[0].replace("main.py",""),'TEMP')
#Папка с картиками
images = create_image_list(r'./PNG')
#Папка с видео которые будут обработаны
video_ls = create_file_list(os.path.join(sys.argv[0].replace("main.py",""),'VIDEO'))
print(result_folder)
#Фильтрыpip
unq_filter_params =["colorbalance=rs=.3","colorbalance=gs=-0.20","colorbalance=gs=0.20","colorbalance=bs=-0.30","colorbalance=bs=0.30","colorbalance=rm=0.30","colorbalance=rm=-0.30","colorbalance=gm=-0.25","colorbalance=bm=-0.25","colorbalance=rh=-0.15","colorbalance=gh=-0.20","colorbalance=bh=-0.20"]
noises=[10,12,14,15]
for video in video_ls:
    for vvv in range(0,vidc):
        noises_var=[['-vf',f'noise=c0s={random.choice(noises)}:c0f=t+u']]
        print(f"Processing video {vvv+1}/{vidc}")
        clip = VideoFileClip(video)
        if doRotate:
            print("Preparing..")
            fnpre=filenameprepre(result_folder)
            clip.write_videofile(fnpre,ffmpeg_params=["-vf",f"rotate={random.choice(angles)}*PI/180"])
            print("Closing")
            print(clip.close())
            print("Closed")
            clip = VideoFileClip(fnpre)
        clip=clip.set_fps(clip.fps+random.choice(afps))
        rmaxd=maxd
        if(clip.duration < maxd):
            rmaxd=clip.duration
        #
        clip = clip.subclip(mind,rmaxd)#.set_audio(AudioFileClip(random.choice(create_file_list("MUSIC"))))
        #Эффект появления
        if showEffect:
            clip = vfx.fadein(clip, duration=2)
        #Отражаем видос
        if doMirror:
            clip_mirror = vfx.mirror_x(clip)
        else:
            clip_mirror=clip
        if doblur:
            print("blurring..")
            clip_mirror=clip.fl_image(blur)
        if doBlurIn:
            print("blur first sec")
            smclip=clip_mirror.subclip(0,1)
            ogclip=clip_mirror.subclip(1,clip_mirror.duration)
            smclip=smclip.fl_image(blur)
            clip_mirror=concatenate_videoclips([smclip,ogclip])
            print("done!")
        #Настройки картинки: set_duration - длительность, resize - изменение размера
        #Сохраняем видос
        fn=filenamepre(result_folder)
        oneparam=""
        unq_filter_paramsstr=[]
        for i in range(0,randeffectslimit):
            unq_filter_paramsstr.append(random.choice(unq_filter_params))
        unq_filter_paramsstr=','.join(unq_filter_paramsstr)
        if(unq_filter_paramsstr!="" and unq_filter_paramsstr!=[]):
            oneparam="-filter_complex"
        if(len(video.split(".png."))==2 or len(video.split(".jpg."))==2 or len(video.split(".jpeg."))==2 or len(video.split(".bmp."))==2):
            unq_filter_paramsstr=""
            oneparam=""
        clip=clip_mirror
        addargs=[oneparam,unq_filter_paramsstr]
        if(addargs[0] == "" or addargs[1] ==""):
            addargs=[]
        clip.write_videofile(fn, ffmpeg_params=['-fflags','+bitexact','-flags:v','+bitexact','-flags:a','+bitexact']+addargs)
        new_video=VideoFileClip(fn)
        clip=new_video
        print("FFFFFFFFFFFFFFN")
        fffn=filename(result_folder)
        print(fffn)
        print(result_folder)
        if(len(video.split(".png."))==2 or len(video.split(".jpg."))==2 or len(video.split(".jpeg."))==2 or len(video.split(".bmp."))==2):
            new_video.write_videofile(fffn,ffmpeg_params=["-c:a","aac"])
        else:
            new_video.write_videofile(fffn, ffmpeg_params=random.choice(noises_var)+["-c:a","aac"])
        donefiles.append(fffn)
        print(fffn)
print("Done! Filenames:")
for fn in donefiles:
    print(fn)