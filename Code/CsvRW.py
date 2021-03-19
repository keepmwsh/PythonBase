import os
import shutil
import pandas as pd

# 读取CSV数据
def readc():
    Path = 'C:\\Users\\snowg\\Desktop\\Python\\PythonBase\\File\\TestOne.csv'
    sets = []
    with open(Path) as csvFile:
        csvReader = csvFile.readlines()
        for each in csvReader:
            signal = each[:-1].split(',')
            sets.append(signal)
    print(sets)

# 写入字符串
def writec(result):
    AllPath = 'C:\\Users\\snowg\\Desktop\\Python\\PythonBase\\'
    Path = 'File\\TestOne.csv'

    with open(AllPath + Path, 'a', newline='') as csvFile:
        for each in result:
            for signal in each:
                csvFile.write(signal)

# 写入列表
def writel(lists, index):
    FileName = 'Result.csv'
    result = pd.DataFrame(lists)
    result.to_csv(FileName, header=index, index=False, encoding='gbk', mode='w')

    Path = 'C:\\Users\\snowg\\Desktop\\Python\\PythonBase\\File\\TestOne.csv'

    if os.path.exists(os.getcwd() + '\\' + FileName):
        # 删除目标文件夹下面的文件
        os.remove(Path)
        shutil.move(FileName, Path)
        print("Success")
    else:
        print(os.getcwd() + FileName)
        print("Filed")

if __name__ == "__main__":
    data = ['one', 'tow', 'three']
    index = ['line01']
    writel(data, index)
    # readc()