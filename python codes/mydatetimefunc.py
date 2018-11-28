# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:01:35 2018

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:50:39 2018

@author: hp
"""
import numpy as np
from datetime import datetime
def mydatetimefunc(timestamp):
    B=len(timestamp)
    dt=np.zeros((B,3))
    day1=0
    month1=0
    year1=0
    print(B)
    for i in range(10):
        print(timestamp[i])
        dt1=datetime.fromtimestamp(timestamp[i])
        day1=dt1.day
        month1=dt1.month
        year1=dt1.year
        print(day1)
        dt[i,:]=[day1,month1,year1]
    return(dt)