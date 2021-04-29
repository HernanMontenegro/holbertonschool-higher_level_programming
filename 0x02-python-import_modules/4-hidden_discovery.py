#!/usr/bin/python3
if __name__ == "__main__":
    import imp
    compiled = imp.load_compiled("hidden_4","./hidden_4.pyc")
    compiled_names = compiled.__dir__()
    for i in range(0, len(compiled_names)):
        if compiled_names[i][0:2] != "__":
            print(compiled_names[i])
