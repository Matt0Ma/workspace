#coding:utf-8
class User(object):
    def __init__(self,Host,Name,Passwd):
        self.host = Host
        self.name = Name
        self.passwd = Passwd

Matt = User('39.106.208.60' , 'matt' , '120552')
root = User('39.106.208.60' , 'root' , '120552Mbx')

dic = {'matt':Matt,'root':root}