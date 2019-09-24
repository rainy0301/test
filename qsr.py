import segno 
from PIL import Image 

def qr_make(content,qr_name,icon_img=None,error='L'):
    qr = segno.make(content,error=error)
    qr.save(qr_name+'.png',scale=10,border=1)

    img = Image.open(qr_name+'.png')
    img = img.convert('RGBA')
    img_w, img_h = img.size
    factor = 3
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon = Image.open(icon_img+'.png')
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)
    img.save(qr_name+"_new_.png")

if __name__ == "__main__":
    qr_make('http://xuelifinance.com/news','test',icon_img='345',error='H')