#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av_len = len(sys.argv)
    result = 0
    if av_len == 1:
        print("0")
        exit()
    for i in range(1, av_len):
        result += int(sys.argv[i])
    print("{:d}".format(result))
