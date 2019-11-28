#coding:utf-8
import paramiko
from user import dic
import os
import time
#初始化用户数据
user = input('Welcome !\nUser name ? ')
User = dic[str(user)]
#初始化ssh连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(User.host , 22 , User.name , User.passwd , timeout=10)
#选择模式并进行操作
ExitSymb = 'yes'#初始化一个控制重复使用的变量
while ExitSymb == 'yes' or ExitSymb == '':
    Func = str(input('Which mode? (remote_download / download / upload / check)'))#选择模式
    if Func == 'remote_download':
        DownLdAdds = input('\tInput the address of what you want to download remotely:')
        shell = ssh.invoke_shell()
        shell.send(f"cd /home/{User.name}/Uploads ; nohup wget {DownLdAdds} & \n")
        time.sleep(1)

    elif Func == 'download':
        FileName = input('\tInput the name of what you want to download:')
        os.system(f'scp {User.name}@{User.host}:/home/{User.name}/Uploads/{FileName} C:\\Users\\Public')
        Del = input('\t\tDo you want to delete the file online (yes/no) ?')
        if Del == 'yes' or Del == '':
            ssh.exec_command(f'cd /home/{User.name}/Uploads;rm {FileName}')
            print('\n\t\tHas Deleted this file.\n')

    elif Func == 'upload':
        FileAdds = input('Input the address of what you want to upload:')
        os.system(f'scp {FileAdds} {User.name}@{User.host}:/home/{User.name}/Uploads')
        
    elif Func == 'check':
        Stdin,Stdout,Stderr = ssh.exec_command("ps -aux | grep wget")
        stdout = str(Stdout.read())
        if stdout.find('https') != -1 or stdout.find('http') != -1 :
            print('\n\tSome thing is downloading...\n')
            #status = 0 #"未完成"状态标识符
        else:
            #status = 1 #"已完成"状态标识符
            print('\n\tDownload finished!\n')
        #若未完成则循环检查直到完成为止
        #while status == 0:
        #    Stdin,Stdout,Stderr = ssh.exec_command("ps -aux | grep wget")
        #    stdout = str(Stdout.read())
        #    if stdout.find('https') != -1 or stdout.find('http') != -1 :
        #        status = 0
        #    else:
        #        break
        #print("Download finished!")
    else:
        print('Get Wrong argvs!!!')
    ExitSymb = input('Do you want to do something else (yes/no) ?')
while True:
    Clean = input('Do you want to clean the nohup.out (yes/no) ?')
    if Clean == 'yes' or Clean == '':
        ssh.exec_command(f'cd /home/{User.name}/Uploads;rm nohup.out')
        ssh.close()
        print('\nFinished! Disconnect!\n')
        break
    elif Clean == 'no':
        ssh.close()
        print('\nDisconnect!\n')
        break
    else:
        print('\nGet Wrong argvs!!!\n')
a = input('\nPress any key to exit.')