#Scope
def myfunc():
    global global_variable
    global_variable = 300
    print(global_variable)
myfunc()
print(global_variable)