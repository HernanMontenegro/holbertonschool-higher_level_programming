#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    compiled_names = dir(hidden_4)
    for i in range(0, len(compiled_names)):
        if compiled_names[i][0:2] != "__":
            print(compiled_names[i])
