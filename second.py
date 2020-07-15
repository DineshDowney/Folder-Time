import os,sys
from pymediainfo import MediaInfo
arg_ls = os.listdir(os.getcwd())
main_dir=os.getcwd()
formats= {'.mp4','.mkv',".avi"}

def main_func(arg):
    counter=0
    try:        
        os.chdir(os.path.join(os.getcwd(), arg))
        file_list = os.listdir(os.getcwd())
        for file_name in file_list:
            if(file_name[-4:] in formats):
                counter = counter+find_time(file_name)
        print(arg+" : "+str(round(counter//60))+" hours and " + str(round(counter%60)) + " minutes")
        os.chdir(main_dir)
    except NotADirectoryError:
        print("Skipped "+ arg + " because it's not a folder")

def find_time(file):
    media_info = MediaInfo.parse(file)
    duration_in_ms = media_info.tracks[0].duration
    amount=duration_in_ms/1000/60
    return amount

for arg in arg_ls:
    main_func(arg)
