import sys
if len(sys.argv) < 2:
    print("Please give args")
    sys.exit(0)
name = sys.argv[1]
with open('input%s.txt'%(name), 'wt') as fi:
    with open('output%s.txt'%name, 'wt') as fo:
        print("Hi, my name is %s"%name)
        fo.write("Hi, my name is %s"%name)
        in_txt = input()
        fi.write(in_txt)


