import os
import time, sys#,queue
from multiprocessing.managers import BaseManager
import subprocess
import sys
import threading

import random,time
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from multiprocessing import Queue

import sys

import win32api
import win32con

from pkg.cmdcolor import *
from pkg.events import *
from pkg.winauto_Functions import *


class SpeakThread (threading.Thread):
    def __init__(self,lock, threadName, _str):


        threading.Thread.__init__(self)


        self.name = threadName
        self.speak_str = _str
        self.lock = lock


    def run(self):
        #print ("开始线程：" + self.name)
        # 获取锁，用于线程同步
        self.lock.acquire()
        self.speak()
        # 释放锁，开启下一个线程
        self.lock.release()
        #print ("结束线程：" + self.name)

    def speak(self):
        '''
        播报线程 threadName, 播放str， 延迟
        '''
        mystr = str(self.speak_str)
        #print('1')
        engine = pyttsx3.init()
        #print('2')
        engine.say(mystr.replace('\n',""))
        #print()
        print ("        speaking at %s" % ( time.ctime(time.time())))

        
        engine.runAndWait()
        #time.sleep(0.1)

class GetResultThread (threading.Thread):
    def __init__(self, _threadName, _result , _threadLock):


        threading.Thread.__init__(self)


        self.name = _threadName
        self.result = _result
        self.threadLock = _threadLock
        #self.lock = lock
        
    def run(self):
        #start 自动运行
        #print ("开始线程：" + self.name)
        # 获取锁，用于线程同步
        #self.lock.acquire()
        #self.speak()
        # 释放锁，开启下一个线程
        #self.lock.release()
        #print ("结束线程：" + self.name)
        while 1 :

            self.get_result()

    def get_result(self):

        try:
            #print('1')
            r = self.result.get()
            #print('2')
        
            if type(r) == type([]):
                #SpeakThread(self.threadLock,"myspeak",r[0]).start()
                #先说

                my_style = r[0].split('，。')
                my_style = '\n\t'.join(my_style)
                if r[2] == 0:
                    printDarkGray(f'    {r[0]}')
                if r[2] == 1:
                    printDarkGreen(f'    {my_style}')
                if r[2] == 2:
                    printRed(f'    {r[0]}')
                printDarkYellow(f'                                                          -From {r[1]}')


                #speak
                #print('speaking')
                



                sys.stdout.flush()
            else:
            
                printDarkWhite(f'        {r}')
                sys.stdout.flush()
        except Queue.Empty:
                print('result queue is empty.')


class GetTaskThread (threading.Thread):
    def __init__(self, _threadName, _task , _threadLock):

        threading.Thread.__init__(self,daemon=True)
        self.winauto= winauto_Functions()

        self.threadHandle = win32api.GetCurrentThreadId()

        self.name = _threadName
        self.task = _task
        self.threadLock = _threadLock
        #self.lock = lock
        
    def run(self):
        #start 自动运行
        #print ("开始线程：" + self.name)
        # 获取锁，用于线程同步
        #self.lock.acquire()
        #self.speak()
        # 释放锁，开启下一个线程
        #self.lock.release()
        #print ("结束线程：" + self.name)
        while 1 :
            self.get_task()

    def get_result(self):

        try:
            #print('1')
            r = self.task.get()
            #print('2')
        
            if type(r) == type([]):
                SpeakThread(self.threadLock,"myspeak",r[0]).start()
                #先说

                my_style = r[0].split('，。')
                my_style = '\n\t'.join(my_style)
                if r[2] == 0:
                    printDarkGray(f'    {r[0]}')
                if r[2] == 1:
                    printDarkGreen(f'    {my_style}')
                if r[2] == 2:
                    printRed(f'    {r[0]}')
                printDarkYellow(f'                                                          -From {r[1]}')


                #speak
                #print('speaking')
                



                sys.stdout.flush()
            else:
            
                printDarkWhite(f'        {r}')
                sys.stdout.flush()
        except Queue.Empty:
                print('result queue is empty.')
    def get_task(self):
        try:
            #print('1')
            r = self.task.get()
            #debug
            print(f"get task ---\n {r}   \n---")
            if type(r) == type([]):
                self.switch(r)
        except:
                print('q error.')
    
    def switch(self,r):
        event_Num = r[0]

        match event_Num:#pythun auto adds 'break'
            case Event_t.EXIT:
                print("exit code")
                win32api.PostThreadMessage(self.threadHandle, win32con.WM_QUIT, 0, 0); #api 退出子线程，主线程无活动子线程，程序退出
            case Event_t.Push_message_V1:
                print("get V1 msg")
                if r[1] =='f2':
                    winauto_Functions.f2();
            
            case _:
                print('un match msg')




class cs_server():

    class MyException(Exception):
        def __init__(self,message):
            Exception.__init__(self)
            self.message=message    

    class MyException2(Exception):
        def __init__(self,message):
            Exception.__init__(self)
            self.message=message        
    
    class QueueManager(BaseManager):  # 从BaseManager继承的QueueManager:
        pass
    # if IP2_enable ==1:
    class QueueManager2(BaseManager):  # 从BaseManager继承的QueueManager:
        pass

    def exit(self):
        print(' Exit cs_server.')
        #win32api.PostThreadMessage(self.thread_handle, win32con.WM_QUIT, 0, 0);
        sys.exit()
    def __init__(self,ip='127.0.0.1',port=5000):
        self.client_name = 'S_' +  os.environ.get("COMPUTERNAME")
        self.server_addr1 = ip
        self.server_port1 = port
        self.IP2_enable =0
        self.server_addr2 = '192.168.10.78'
        self.server_port2 = 5001

        self.server_key = b'abc'
        self.thread_handle = win32api.GetCurrentThreadId()

        # self.QueueManager.register('get_task_queue')
        # self.QueueManager.register('get_result_queue')
        # self.QueueManager.register('get_shared_value')


        print(f'        SERVER端启动中.. {self.client_name}')

        self.task_queue =  Queue()#queue.Queue()  # 发送任务的队列:
        self.result_queue = Queue()#queue.Queue() # 接收结果的队列:
        self.task_queue2 =  Queue()#queue.Queue()  # 发送任务的队列:
        self.result_queue2 = Queue()#queue.Queue() # 接收结果的队列:

    def return_task_queue(self):
        global task_queue
        return self.task_queue  # 返回发送任务队列
    def return_result_queue (self):
        global result_queue
        return self.result_queue # 返回接收结果队列
    def return_task_queue2(self):
        global task_queue2
        return self.task_queue2  # 返回发送任务队列
    def return_result_queue2(self):
        global result_queue2
        return self.result_queue2 # 返回接收结果队列
    
    #@staticmethod
    def run_server_mode(self):
        """get task  ;
        push result """
        global result
        global result2
        #global threadLock

        self.QueueManager.register('get_task_queue', callable=self.return_task_queue)
        self.QueueManager.register('get_result_queue', callable=self.return_result_queue)
        self.manager = self.QueueManager(address=(self.server_addr1,self.server_port1 ), authkey=self.server_key)
        self.manager.start()  # 启动Queue:
        # 获得通过网络访问的Queue对象:
        self.task = self.manager.get_task_queue()
        self.result = self.manager.get_result_queue()


            
        #绑定第二IP
        if self.IP2_enable == 1:
            self.QueueManager2.register('get_task_queue', callable=self.return_task_queue2)
            self.QueueManager2.register('get_result_queue', callable=self.return_result_queue2)
            self.manager2 = self.QueueManager2(address=(self.server_addr2,self.server_port2  ), authkey=self.server_key)
            self.manager2.start()
            self.task2 = self.manager2.get_task_queue()
            self.result2 = self.manager2.get_result_queue()

        #speak 线程锁
        self.threadLock = threading.Lock()


        self.slot1 = GetTaskThread('slot1', self.task  , self.threadLock)
        self.slot1.start()

        
        if self.IP2_enable == 1:
            self.slot2 = GetTaskThread('slot2', self.task2  , self.threadLock)
            self.slot2.start()
            self.slot2.join()
        print("At server mode.")
        #self.slot1.join()

if __name__ == "__main__":
    server_handle = cs_server(ip='127.0.0.1',port=5000)
    server_handle.run_server_mode()

    while 1:
        try:
            input()
        except:
            server_handle.exit()
    #sys.exit()