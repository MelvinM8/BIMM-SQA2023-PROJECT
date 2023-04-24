import traceback
from graphtaint import getYAMLFiles,getSHFiles
from scanner import isValidUserName, isValidPasswordName, isValidKey

def fuzz():
    func_names = [
        getYAMLFiles,
        getSHFiles,
        isValidUserName,
        isValidPasswordName,
        isValidKey
    ]

    func_args = [
        ["----saa", 422422, False, None],
        ["@@@@#@$@", "[][][]", True, None],
        ["/user/Documents", "admin_domain", 21421421512421, None],
        ["password", False, None, "_hash"],
        [None, True, "mykey", "adminkey", 2141424]
    ]
    
    index = 0

    for func in func_names:
        args = func_args[index]
        for arg in args:
            try:
                result = func(arg)
                if(result != None):
                    print("Result returned is " + str(result) + " for arguments " + str(arg))
            except Exception as e:
                print(str(func.__name__) + " has an issues with arguments " + str(arg))
                traceback.print_exception(e, None, None)
            else:
                print(str(func.__name__) + " passed with arguments " + str(arg))
        index = index  +1

fuzz()
