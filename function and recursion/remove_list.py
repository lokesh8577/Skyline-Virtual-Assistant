# def remo(list,name):
#     i=0
#     for i in list:
#         if list[i]==name:
#             list.remove(name)
#         else:
#             print("element not exist in list")    
            

#     print(list)    

# list = ['supra','skyline','tesla','bmw']
# remo(list,'tesla')       
def remo(lst, name):
    return [item for item in lst if item != name]

# Example usage
my_list = ['supra', 'skyline', 'tesla', 'bmw']
result = remo(my_list, "tesla")
print(result)
