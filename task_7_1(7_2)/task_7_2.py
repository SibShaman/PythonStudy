# Написать скрипт, создающий из config.yaml стартер для проекта 
import os


with open('task_7_1(7_2)/config.yaml', 'r', encoding='utf8') as dir_name:
    
    # парсим config в список
    temp_path = [i.strip().split('\\') for i in dir_name.readlines()]
    # из полученного списка, надо взять каждый отдельный список и проверить последний элемент, 
    # если он содержит точку, то берем предыдущие значения и составляем в путь, 
    # а этот элемент будет названием файла
    # если точку не содержит то это и есть путь и надо создать папку

    for item in temp_path:        
        if not '.' in item[-1]:
            dir_path = os.path.join('//'.join(item))  
            if not os.path.exists(dir_path): 
                os.makedirs(dir_path)  
        else:
            file_path = os.path.join('//'.join(item))           
            if not os.path.exists(file_path): 
                open(file_path, 'tw', encoding='utf-8')
                
            
            
                      
            
            
  
        

        

        
        

