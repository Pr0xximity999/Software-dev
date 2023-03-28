import requests
from PIL import Image
from PIL.Image import Resampling

imgHeight = 1000
imgWidth = 1000

among1 = [[0, 1, 1, 1],
         [1, 1, 3, 2],
         [1, 1, 1, 1],
         [0, 1, 1, 1],
         [0, 1, 0, 1]]

among2 = [[1, 1, 1, 0],
          [2, 3, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 0],
          [1, 0, 1, 0]]

amongs = [among1, among2]

def amongCheck(x, y, img, newImg, among):
    pix = img.load()
    newPix = newImg.load()
    if x+3 >= imgWidth:
        return False
    if y+4 >= imgWidth:
        return False

    Rs = [-1, -1, -1, -1]
    Gs = [-1, -1, -1, -1]
    Bs = [-1, -1, -1, -1]
    As = [-1, -1, -1, -1]

    for row in range(5):
        for column in range(4):
            r, g, b, a = pix[x+column,y+row]
            amg = among[row][column]
            if Rs[amg] == -1:
                Rs[amg], Gs[amg], Bs[amg], As[amg] = r, g, b, a
            else:
                if amg != 0:
                    if Rs[amg] != r or Gs[amg] != g or Bs[amg] != b or As[amg] != a:
                        return False

    col0 = '#%02x%02x%02x%02x' % (Rs[0], Gs[0], Bs[0], As[0])
    col1 = '#%02x%02x%02x%02x' % (Rs[1], Gs[1], Bs[1], As[1])
    col2 = '#%02x%02x%02x%02x' % (Rs[2], Gs[2], Bs[2], As[2])

    if col0 == col1 or col1 == col2:
        return False

    for row in range(5):
        for column in range(4):
            amg = among[row][column]
            newPix[x+column, y+row] = Rs[amg], Gs[amg], Bs[amg], As[amg]
    return True



img1 = Image.open(requests.get("https://hot-potato.reddit.com/media/canvas-images/1649000522914-0-f-N16oRb9i.png", stream=True).raw).convert("RGBA")


newImg1 = Image.new(mode="RGBA", size=(imgWidth,imgHeight))


for y in range(imgHeight):
    for x in range(imgWidth):
        if not amongCheck(x, y, img1, newImg1, among1):
            if amongCheck(x, y, img1, newImg1, among2):
                print("Soumang")
        else:
            print("AMOUgUS")


img2 = Image.open(requests.get("https://hot-potato.reddit.com/media/canvas-images/1649000522841-1-f-2jJfrhAI.png", stream=True).raw).convert("RGBA")

newImg2 = Image.new(mode="RGBA", size=(imgWidth,imgHeight))


for y in range(imgWidth):
    for x in range(imgHeight):
        if not amongCheck(x, y, img2, newImg2, among1):
            if amongCheck(x, y, img2, newImg2, among2):
                print("Soumang")
        else:
            print("AMOUgUS")


backGround = Image.new("RGBA", (imgWidth * 2, imgHeight))
backGround.paste(img1, (0,0))
backGround.paste(img2, (imgWidth + 1,0))

master = Image.new("RGBA", (imgWidth * 2, imgHeight))
master.paste(newImg1, (0,0))
master.paste(newImg2, (imgWidth + 1, 0))

masterPix = master.load()
bgPix = backGround.load()

for y in range(imgHeight):
    for x in range(imgWidth * 2):
        r, g, b, a = masterPix[x, y]
        if a == 0:
            r, g, b, a = bgPix[x, y]
            masterPix[x, y] = r, g, b, 50

new = master.resize((imgWidth * 10 * 2, imgHeight * 10), resample=Resampling.BOX)
new.save("test.png")