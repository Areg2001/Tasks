new_list = []
dict_ = {}
with open('text.txt', 'r') as f:
    for line in f:
        new_list.extend(line.split())
        
    for i in range(len(new_list)):
        dict_[new_list[i]] = new_list.count(new_list[i])        
            
        
print(dict_)
    
   
                        
            
            
        
        