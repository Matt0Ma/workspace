#coding:utf-8
import easygui as gui
import paramiko
from user import dic
import os
import time
#输入用户名
User = dic[str(gui.enterbox(msg = 'Welcome!\nInput user name',title = 'SSH Assistant'))]
#初始化ssh连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(User.host , 22 , User.name , User.passwd , timeout=10)
#控制循环
LoopSymb = 1#初始化一个控制重复使用的变量
nohup = 'no'#初始化一个判断是否存在nohup的变量
while LoopSymb == 1:
#进行模式选择
    mode = gui.choicebox(msg = 'Choice mode',title = f'{User.name}@{User.host}:Connected', \
    choices = ['Remote Download','Download','Upload','Check'])
    #开始操作
    if mode == 'Remote Download':
        DownLdAdds = str(gui.enterbox(msg = 'Input download address',title = mode))
        shell = ssh.invoke_shell()
        shell.send(f"cd /home/{User.name}/Uploads ; nohup wget {DownLdAdds} & \n")
        time.sleep(1)
        nohup = 'yes'
    elif mode == 'Download':
        FileName = str(gui.enterbox(msg = 'Input the name of what you want to download',title = mode))
        os.system(f'scp {User.name}@{User.host}:/home/{User.name}/Uploads/{FileName} C:\\Users\\Public\\Downloads')
        gui.msgbox(msg = 'Saved at C:\\Users\\Public\\Downloads.',title = mode)
        Del = gui.choicebox(msg = 'Do you want to delete the file online?',title = mode,choices = ['Yes','No'])
        if Del == 'Yes' or Del == '':
            ssh.exec_command(f'cd /home/{User.name}/Uploads;rm {FileName}')
            gui.msgbox(msg = 'Has Deleted this file.')
    elif mode == 'Upload':
        FileAdds = gui.enterbox(msg = 'Input the address of what you want to upload',title = mode)
        os.system(f'scp {FileAdds} {User.name}@{User.host}:/home/{User.name}/Uploads')
    elif mode == 'Check':
        Stdin,Stdout,Stderr = ssh.exec_command("ps -aux | grep wget")
        stdout = str(Stdout.read())
        if stdout.find('https') != -1 or stdout.find('http') != -1 :
            gui.msgbox(msg = 'Some thing is downloading...',title = mode)
        else:
            gui.msgbox(msg = 'Download finished!',title = mode)
    elif mode == None:
        break
    else:
        gui.msgbox(msg = 'Get wrong argvs!',title = 'ERROR')
    Symb = gui.choicebox(msg = 'Do you want to do something else?',title = 'What Else',choices = ['Yes','No'])
    if Symb == 'Yes':
        LoopSymb = 1
    else:
        LoopSymb = 0
if nohup == 'yes':
    Clean = gui.choicebox(msg = 'Do you want to clean the nohup.out ?',title = 'Clean',choices = ['Yes','No'])
    if Clean == 'yes' or Clean == '':
        ssh.exec_command(f'cd /home/{User.name}/Uploads;rm nohup.out')
        ssh.close()
        gui.msgbox(msg = 'Cleaning Finished!',title = 'Clean')
gui.msgbox(msg = f'{User.host} Disconnected.',title = 'Disconnected')