from PIL import Image 
def get_position(file_name1, file_name2):

    """
    传入需要获得坐标的小图路径
    返回值为空表示没找到
    """

    im1 = Image.open(file_name1)
    im2 = Image.open(file_name2)
    pix1 = im1.load()
    pix2 = im2.load()
    width1 = im1.size[0]
    height1 = im1.size[1]
    width2 = im2.size[0]
    height2 = im2.size[1]
 
    rgb2 = pix2[0, 0][:3]  # 左上角起始点
    for x in range(width1):
        for y in range(height1):
            rgb1 = pix1[x, y][:3]
            if rgb1 == rgb2:
                # 判断剩下的点是否相同
                status = 0
                # 图二的坐标是(s, j) --- (s-x, j-y)
                for s in range(x, x + width2):
                    for j in range(y, y + height2):
                        # 设置阈值范围
                        if abs(pix2[s-x,j-y][0]-pix1[s,j][0]) > 60 and  abs(pix2[s-x,j-y][1]-pix1[s,j][:3][1]) > 60 and abs(pix2[s-x,j-y][1]-pix1[s,j][:3][1]) > 60:
                            status = 1
                if status:
                    continue
                else:
                    return x + round(0.5 * width2), y + round(0.5 * height2)