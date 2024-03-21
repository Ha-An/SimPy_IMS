import matplotlib.pyplot as plt
from config import *

def visualization(export_Daily_Report):
    Visual_Dict = {
        'Material': [],
        'WIP': [],
        'Product': [],
        'Keys': {'Material': [], 'WIP': [], 'Product': []}
    }
    Key = ['Material', 'WIP', 'Product']
    
    for id in I.keys():
        temp = []
        for x in range(SIM_TIME):
            temp.append(export_Daily_Report[id * SIM_TIME + x][6])
        Visual_Dict[export_Daily_Report[id * SIM_TIME + x][2]].append(temp)
        Visual_Dict['Keys'][export_Daily_Report[id * SIM_TIME + x][2]].append(export_Daily_Report[id * SIM_TIME + x][1])

    visual = VISUALIAZTION.count(1)
    print(visual)
    count_type = 0
    cont_len = 1
    for x in VISUALIAZTION:
        cont = 0
        if x == 1:
            plt.subplot(int(f"{visual}1{cont_len}"))
            cont_len += 1
            for lst in Visual_Dict[Key[count_type]]:
                plt.plot(lst, label=Visual_Dict['Keys'][Key[count_type]][cont])
                plt.legend()
                cont += 1
        count_type += 1
    
    plt.show()
