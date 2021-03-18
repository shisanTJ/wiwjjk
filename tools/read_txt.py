import os

from config import BASE_URL


def read_txt(filename):
    filepath = BASE_URL+os.sep+"data"+os.sep+filename

    arr = []
    with open(filepath,"r",encoding="utf-8")as f:
        for data in f.readlines():
            arr.append(tuple(data.strip().split(",")))

        return arr[1::]

if __name__ == '__main__':

    print(read_txt("price.txt")[0])

