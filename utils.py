import urllib
import re
import random
import datetime


def prepare_record(text):
    text_list = text.split('\n')
    
    month = text_list[0].split(' ')[0].split('/')[0]
    day = text_list[0].split(' ')[0].split('/')[1]
    d = datetime.date(datetime.date.today().year, int(month), int(day))
   
    record_list = []
    
    time_format = '%H:%M'
    
    for i in text_list[1:]:
        temp_list = i.split(' ')
        
        temp_name = temp_list[0]
        temp_training = temp_list[1]
        
        temp_start = datetime.datetime.strptime(temp_list[2].split('-')[0], time_format)
        temp_end = datetime.datetime.strptime(temp_list[2].split('-')[1], time_format)
        temp_duration = temp_end - temp_start
        
        record = (temp_name, temp_training, temp_duration, d)
        record_list.append(record)
        
    return record_list

def prepare_record2(text):
    text_list = text.split(" ")
    
    record_list2 = []
    record2 = (text_list[1], text_list[2])
    record_list2.append(record2)
        
    return record_list2