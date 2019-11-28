#coding:utf-8
import pyautogui as pag
import time
from PIL import Image
#函数：检查是否已经完成任务
def check():
    if pag.locateOnScreen('unfinished2.png')==None:
        symb = 'pass'
    else:
        symb = 'unpass'
    return symb
#函数：寻找“视频字样”
def video():
    v1 = pag.locateOnScreen('video.png')
    if v1!=None:
        return pag.center(v1)
    else:
        v2 = pag.locateOnScreen('video2.png')
        if v2!=None:
            return pag.center(v2)
        else:
            v3 = pag.locateOnScreen('video3.png')
            if v3!=None:
                return pag.center(v3)
#函数：检查选项的位置并做题
def find_and_do():
    position_generator = pag.locateAllOnScreen('button.png')
    if position_generator != None:
        for position in position_generator:
            pag.click(pag.center(position))
            time.sleep(1)
            pag.click(pag.locateCenterOnScreen('yes.png'))
            time.sleep(1)
            if pag.pixelMatchesColor(1150,196,(66,133,244)): 
                pag.click(1150,196)
                time.sleep(1)
                continue
            else:
                break
    else:
        time.sleep(1)
#函数：任务点标题位置生成器
def getposition(image):
    PosGenerator = pag.locateAllOnScreen(image)
    NewGenerator = (pag.center(PosTup) for PosTup in PosGenerator)
    return NewGenerator
#函数：根据任务点位置推算并点击课程标题
def click(position):
    pag.moveTo(position)
    pag.move(-210,0)
    pag.click()

#主程序
#定义提示视窗并准备运行程序：
start = pag.confirm("仅适用于1920X1080分辨率！请确保：\n\
    1.已将Chrome浏览器置于最上层，并调整至90%缩放\n\
    2.已将需播放的课程置于列表最上方\n\
    3.退出方法：将鼠标移至屏幕左上角并按一次\"Win+D\"\n\
    4.如鼠标移动异常：将指针移动并保持在屏幕左上角\n\
    ***所有注意事项明确后点击OK按钮开始运行***\n")
if start == 'OK':
    time.sleep(3)
    Posgenerator = getposition('2white.png')
    for pos in Posgenerator:
        click(pos) #点击课程标题
        time.sleep(1)
        pag.click(video()) #点击视频按钮
        time.sleep(3)
        pag.click(780,710) #点击播放按钮
        while check() == 'unpass':
            find_and_do() #做题并改变题目状态