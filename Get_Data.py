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
    def spydatalist(self, shares_code) -> dict:
        # flag=1 表示股票数据来自上海股票交易所中的A股列表，本方法只返回股票的代码和名称
        # 返回字典格式:code:{'简称': '现代制药'}
        if self.flag == 1:

            try:
                # 读取需要的列的信息
                data_xls = pd.read_excel(r'shares_data\sh_a.xlsx',header=0, index_col=0,usecols=['简称','代码'])
                CompanyInfo = pd.DataFrame(data_xls)
                if type(CompanyInfo) == pd.DataFrame:
                    CompanyCodeResult = CompanyInfo.to_dict(orient= 'index')
                    return CompanyCodeResult
            except Exception as e:
                print(e)
        elif self.flag == 2:
            # flag =2 表示股票数据来自上海股票交易所中的B股列表

                

            
            
            

            
            
