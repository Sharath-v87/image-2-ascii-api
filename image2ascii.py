import PIL.Image


def img2ascii(img, wid=100):
    # Intensity of pixels in terms of ascii characters ranging from brightest to darkest
    gscale = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    # image resizing to desired width and grayscaling
    width = wid
    W, H = img.size
    ratio = H / (W * 1.65)
    h = int(ratio * width)
    newimg = img.resize((width, h))
    greyimg = newimg.convert("L")

    # getting the entire pixel data from the grayscaled image and adding it to a list
    pix = greyimg.getdata()
    character = "".join([gscale[int(p / 25)] for p in pix])
    return character, width


if __name__ == "__main__":
    img = PIL.Image.open("assets/ros.png")
    character, width = img2ascii(img)
    # printing it out in such a way that it new lines at every multiples of provided width
    f = open("output text file/output.txt", "w")
    for i in range(0, len(character), width):
        f.write(character[i : width + i] + "\n")
    f.close()
    print("done")
