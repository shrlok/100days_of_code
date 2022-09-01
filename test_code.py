var = 1
def one_var():
    global var
    var += 1


one_var()
print(var)