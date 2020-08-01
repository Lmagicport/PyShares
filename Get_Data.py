'''
in this moudle you can get shares’s data from internet
'''

# get shares list from money.163

import numpy as np
import pandas as pd


class SpySharesData:

    def __init__(self, f=0):
        'f means which market you need to get data'
        self.flag = f
    
    # 数据来自上海交易所和深圳交易所官方网站，如果没有找到需要的股票代码，可以自行对代码进行补充，补充后的文件欢迎上传至项目中
    def spydatalist(self,shares_code):
        # flag=1 表示股票数据来自上海股票交易所中的A股列表
        if self.flag == 1:
            data_xlsx = pd.read_excel(r'shares_data\sh_a.xlsx')
            shares_data = pd.DataFrame(data_xlsx)

            
            
            

            
            
