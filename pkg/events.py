
from enum import IntEnum
class Event_t(IntEnum):
    '''add event accordingly'''
    EXIT = 1
    Cmd_list_V1 = 2
    Back_massage_V1 = 3
    Push_message_V1 = 4 
    Push_message_Multiple_V1 = 5

    @classmethod
    def form_data(cls,number):
        if number == cls.EXIT:
            return  ["Event_t number",]
        if number == cls.Cmd_list_V1:
            return ["Event_t number","some commands run in cmd,may have multiple columns,end with END","END"]
        if number == cls.Back_massage_V1:
            return ["Event_t number","message;","client_name","color_number"]
        if number == cls.Push_message_V1:
            return ["Event_t number","ONE message;","client_name","color_number"]
        if number == cls.Push_message_Multiple_V1:
            return ["Event_t number","message1","msg2...","MSG_END","client_name","color_number"]