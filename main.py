#Download and install image magic with convert feature
import glob,os,subprocess
heicImg = glob.glob(r"C:\Users\Hitesh\Desktop\Print\img\*.heic")
imageMagickPath = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI"
print(heicImg)

print('=====start heic2jpg=====')
for heicName in heicImg:
    # print(heicName)
    input = heicName
    dirname = os.path.dirname(input)
    basename_without_ext = os.path.splitext(os.path.basename(input))[0]
    output = os.path.join(dirname,basename_without_ext+".jpg")
    print('=====')
    print("input: "+input)
    print("output: "+output)
    print('=====Run ImageMagick=====')
    print('Command')
    print(os.path.join(imageMagickPath,"magick convert")+input+ " " + output)
    subprocess.run(os.path.join(imageMagickPath,"magick convert")+input+ " " + output)

print('=====finished=====')
