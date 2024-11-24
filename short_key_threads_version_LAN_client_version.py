import threading
import win32api
import win32con
from threading import Timer
from pywinauto.win32_hooks import Hook
from pywinauto.win32_hooks import KeyboardEvent
from pywinauto.win32_hooks import MouseEvent
import pyperclip
import time
import pywinauto


#Event_t
from pkg.events import *
from pkg.winauto_Functions import *

#快捷键调用的功能用threading实现，避免阻塞 event——handler





class My_shortKeys():

    def __init__(self, outer_handel=False):
        self.msg_h = outer_handel
    def f4_pressed(self):
        time.sleep(2)
        print("F4 was pressed")
        #pywinauto.keyboard.send_keys("^w")
        if self.msg_h != False:
            self.msg_h.push_task_to_server([Event_t.Push_message_V1, "f2", a.client_name,'Red'])






    def on_event(self,args):#callback
        global monitor_thread_id
        global hk
        import json
        """Callback for keyboard and mouse events"""
        if isinstance(args, KeyboardEvent):
            
            if args.current_key == 'F2' and args.event_type == 'key down':
                global TRIGER_1
                TRIGER_1 = 1


            if args.current_key == 'F4' and args.event_type == 'key down':
                global TRIGER_2
                TRIGER_2 = 1
                #print("F4 was pressed")
                #time.sleep(0.4)
                #pywinauto.keyboard.send_keys("^w")
                foo_thread = threading.Thread(target=self.f4_pressed,name='f4_pressed')
                foo_thread.start()
                
            if args.current_key == 'F6' and args.event_type == 'key down':
                print("F6 was pressed")


            if args.current_key == 'F8' and args.event_type == 'key down':
                print("F8 was pressed")
                # x, y = win32api.GetCursorPos()
                # print(x,y)

                # time.sleep(0.1)
                # pywinauto.mouse.click(button='right',coords=(x,y))
                # time.sleep(0.1)
                # pywinauto.keyboard.send_keys("k")
                # time.sleep(3)
                # pywinauto.keyboard.send_keys("{ENTER}")
                # #time.sleep(0.1)
                # #pywinauto.keyboard.send_keys("^+{TAB}")
                

            if args.current_key == 'F9' and args.event_type == 'key down':
                print("F9 was pressed")


            if args.current_key == 'F11' and args.event_type == 'key down' and 'Rcontrol' in args.pressed_key:
                #print("R c + f11 was pressed")

                #处理txt文件
                #out_list =[]
                #CP_1
                global CP_1
                # __c__ =pywinauto.keyboard.send_keys("^c")
                # cc = pyperclip.paste()
                # if cc == "新建文件夹" :
                #     pyperclip.copy(CP_1)
                #     time.sleep(0.1)
                #     pywinauto.keyboard.send_keys("^v")
                #     pywinauto.keyboard.send_keys("{ENTER}")
                # else:
                #     cc= cc.replace("/", "_")
                #     cc= cc.replace("*", "[星号]")
                #     cc= cc.replace("\n", "")
                #     cc= cc.replace(":", "：")
                #     CP_1 = cc
                #     print(CP_1)

            if args.current_key == 'F12' and args.event_type == 'key down' and 'Rcontrol' in args.pressed_key:
                #print("R c + f12 was pressed")
                #CP_2
                global CP_2
                # __c__ =pywinauto.keyboard.send_keys("^c")
                # cc = pyperclip.paste()
                # if cc == "新建文件夹"  or cc == "":
                #     pyperclip.copy(CP_2)
                #     time.sleep(0.1)
                #     pywinauto.keyboard.send_keys("^v")
                #     pywinauto.keyboard.send_keys("{ENTER}")
                # else:
                #     cc =cc.replace("/", "[左斜]").replace("*", "[星号]").replace(":", "[冒号]").replace("\r\n", "[]").replace("（本文来自哥特动漫王国www.gtloli.live）", "_")
                    
                #     CP_2 = cc
                #     print(CP_2)

            if args.current_key == 'F10' and args.event_type == 'key down' and 'Rcontrol' in args.pressed_key:
                print("R c + f10 was pressed")

                #处理txt文件
                #out_list =[]

            if args.current_key == 'F1' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                print("Ctrl + f1 was pressed")

                
            if args.current_key == 'E' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                print("Ctrl + e was pressed")
                global TRIGER_3
                hk.unhook_mouse()
                hk.unhook_keyboard()
                TRIGER_3 = 1
                win32api.PostThreadMessage(monitor_thread_id, win32con.WM_QUIT, 0, 0); #api 退出子线程，主线程无活动子线程，程序退出
                
                #win32api.PostThreadMessage(monitor_thread_id2, win32con.WM_QUIT, 0, 0);


            #if args.current_key == 'K' and args.event_type == 'key down':
            #    print("K was pressed");

            #if args.current_key == 'M' and args.event_type == 'key down' and 'U' in args.pressed_key:
            #    hk.unhook_mouse()
            #    print("Unhook mouse")

            #if args.current_key == 'K' and args.event_type == 'key down' and 'U' in args.pressed_key:
            #    hk.unhook_keyboard()
            #    print("Unhook keyboard")
            #if args.current_key == 'T' and args.event_type == 'key down' and 'S' in args.pressed_key:
            #    hk.unhook_keyboard()
            #    print("Unhook keyboard")
            #    win32api.PostThreadMessage(monitor_thread_id, win32con.WM_QUIT, 0, 0);

        if isinstance(args, MouseEvent):
            if args.current_key == 'RButton' and args.event_type == 'key down':
                print ("Right button pressed")

            if args.current_key == 'WheelButton' and args.event_type == 'key down':
                print("Wheel button pressed")



    def mouse_key_hook(self):#hook处理thread
        global monitor_thread_id
        global hk
        global CP_1
        global CP_2
        CP_1 = ""
        CP_2 = ""
        monitor_thread_id = win32api.GetCurrentThreadId()
        hk = Hook()
        hk.handler = self.on_event
        
        hk.hook(keyboard=True, mouse=False)
        
        
    def mouse_key_hook_helper(self):
        #启动钩子线程
        monitor_thread = threading.Thread(target=self.mouse_key_hook,name='monitor01')
        monitor_thread.start()
        #grab_screen_thread = threading.Thread(target=grab_screen_hook,name='monitor02')
        #grab_screen_thread.start()

        
        main_thread_id = win32api.GetCurrentThreadId()
        #monitor_thread.join()#zu se
        #thread2.join()#zu se
        #print(threading.active_count())
        #print(threading.enumerate())
        #print(threading.current_thread())
        print('begin mouse_key_hook_helper...')
        #阻塞
        #monitor_thread.join()

    def run(self):
        self.mouse_key_hook_helper()


        
import os
import time, sys
from multiprocessing.managers import BaseManager
import subprocess
import sys
import threading
from multiprocessing import Queue

class cs_clinet():

    class MyException(Exception):
        def __init__(self,message):
            Exception.__init__(self)
            self.message=message    

    class MyException2(Exception):
        def __init__(self,message):
            Exception.__init__(self)
            self.message=message        
    
    class QueueManager(BaseManager):
        pass

    def __init__(self,ip='127.0.0.1',port=5000):

        self.client_name = 'S_' +  os.environ.get("COMPUTERNAME")
        self.server_addr = '127.0.0.1'
        self.server_port = 5000
        self.server_key = b'abc'
        self.thread_handler = 0

        self.QueueManager.register('get_task_queue')
        self.QueueManager.register('get_result_queue')
        self.QueueManager.register('get_shared_value')


        print(f'        客户端启动中.. {self.client_name}')

        self.m = self.QueueManager(address=(self.server_addr, self.server_port), authkey=self.server_key)
        try:
            self.m.connect()
        except ConnectionRefusedError:
            print(f"服务器连接错误 {self.server_addr}:{self.server_port}")
            exit()
        self.task = self.m.get_task_queue()#任务队列
        self.result = self.m.get_result_queue()#结果写入result队列
        print(f" server {self.server_addr}:{self.server_port} connected.")

    def build_return_list(self,str_1,str_2,color_):
        '''
        构建 返回列表
        '''
        list_ = []
        list_.append(str_1)
        list_.append(str_2)
        list_.append(color_)
        return list_

    def run_cmd_code(self,str_):
        
        # 执行命令
        sp = subprocess.Popen(str_, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,bufsize=1) #universal_newlines=True,

        while 1:
            run_result = sp.stdout.readline()
            if sp.poll() is (not None) :
                break
            if run_result == b'':
                break
            #print(sp.poll())
            run_result_ = run_result.decode('gbk')


            #打印标准输出
            print(run_result_)
            #sys.stdout.flush()
            

            #标准输出至控制台
            
            return_list = self.build_return_list(run_result_,self.client_name,0)
            self.result.put(return_list)
            
            sys.stdout.flush()
            #sys.stdout.flush()
            
            #result.put(f'                        ----FROM {client_name}')
            #sys.stdout.flush()
            
            #time.sleep(1)

        return sp.poll()


    def stdoutprocess(self,o):
        while 1:
            stdoutdata = o.stdout.readline()
            if stdoutdata:
                sys.stdout.write(stdoutdata)
            else:
                break

    def push_task_to_server(self,_data):
        self.task.put(_data);

        

    def get_result_from_server(self):
        #self.thread_handler = win32api.GetCurrentThreadId()
        while 1:
            try:
                n=self.result.get(timeout=5)
                print(n)
                sys.stdout.flush()
                if type(n)== type([]):
                    #deduce it is a event data
                    if n[0] == Event_t.EXIT:
                        raise self.MyException("Exit...from server_msg")
                    if n[0] == Event_t.Back_massage_V1:
                        print(n[1])
            

            except Queue.Empty:
                print(f"result queue empty, to spin")

                time.sleep(5)
                self.close()
                pass
            except self.MyException:
                time.sleep(100)



    def close(self):
        win32api.PostThreadMessage(self.thread_handler, win32con.WM_QUIT, 0, 0); #操作系统api 退出线程


    def client_helper(self):
        # self.push_thread = threading.Thread(target=self.push_task_to_server,name='push_c')
        # self.push_thread.start()
        self.get_thread = threading.Thread(target=self.get_result_from_server,name='get_result_c')
        self.get_thread.start()
        #grab_screen_thread = threading.Thread(target=grab_screen_hook,name='monitor02')
        #grab_screen_thread.start()

        
        self.thread_handler = win32api.GetCurrentThreadId()
        #monitor_thread.join()#zu se
        #thread2.join()#zu se
        #print(threading.active_count())
        #print(threading.enumerate())
        #print(threading.current_thread())
        print('begin client_helper...')
    
    def run(self):
        #self.client_helper();
        pass


if __name__ == "__main__":  #启动

    m_client = cs_clinet()
    m_client.push_task_to_server('sdfsdfds')


    b=My_shortKeys(outer_handel=m_client)
    b.run()

    print('Main done')

