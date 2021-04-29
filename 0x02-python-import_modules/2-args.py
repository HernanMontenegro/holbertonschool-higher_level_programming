#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av_len = len(sys.argv)
    if av_len == 1:
        print("0 arguments.")
        exit()
    elif av_len == 2:
        print("1 argument:")
        print("{:d}: {}".format(1, sys.argv[1]))
        exit()
    print("{:d} arguments:".format(av_len - 1))
    for i in range(1, av_len):
        print("{:d}: {}".format(i, sys.argv[i]))
