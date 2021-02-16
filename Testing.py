import os
import time


def follow(name):
    current = open(name, "r")
    curino = os.fstat(current.fileno()).st_ino
    i = 0
    check =True
    while check:
        while check:
            line = current.read()
            if not line:
                break
            yield line

            filename = "new_file"
            i += 1
            with open(filename + str(i), "w+") as f:
                f.write(line)
                f.close()
                print("new file created")
            if i==10:
                check=False
        # try:
        #     if os.stat(name).st_ino != curino:
        #         new = open(name, "r")
        #         current.close()
        #         current = new
        #         curino = os.fstat(current.fileno()).st_ino
        #
        #         # filename = "new_file"
        #         # i += 1
        #         # with open(filename + str(i), "w+") as f:
        #         #     line1 = current.read()
        #         #     f.write(line1)
        #
        #         continue
        # except IOError:
        #     pass
        time.sleep(1)


if __name__ == '__main__':
    fname = "test.log"
    i = 0

    for l in follow(fname):
        print("New content: {}".format(l))
