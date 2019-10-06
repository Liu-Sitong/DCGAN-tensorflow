from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=192, height=192):
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.basename(jpgfile))
    except Exception as e:
        print(e)


for jpgfile in glob.glob("D:\\CSProject\\tensorflow\\DCGAN-tensorflow\\data\\imgs\\*.jpg"):
    convertjpg(jpgfile, "actress")
