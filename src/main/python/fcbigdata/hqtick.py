'''
Created on 18 Sep 2017

@author: aadebuger
'''

import tushare as ts
import talib as ta
import numpy as np
period_ma=200
period_ave=1
def  func1():
        data = ts.get_hist_data('600818')
        print("data",data)
        data=data.sort_index().loc[:,['open','high','low','close']]
        print("data1",data)
        data['ma']=ta.MA(np.array(data['close']),20)
        print("data2",data)        
if __name__ == '__main__':
    func1()