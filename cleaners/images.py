from PIL import Image

def clean_image(path_in, path_out):
    img = Image.open(path_in)
    data = list(img.getdata())
    clean_img = Image.new(img.mode, img.size)
    clean_img.putdata(data)
    clean_img.save(path_out)
