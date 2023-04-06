import pandas as pd
import numpy as np

import scipy.stats as st


chat_id = 1311912267 # Ваш chat ID, не меняйте название переменной

#ускорение a = 2*S/t^2

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = st.t.interval(alpha=(1 - p), df=len(x)-1, loc=x.mean(),scale=st.sem(x))
    alpha = 1 - p
    #loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    return 2*res[0]/4225, \
            2*res[1]/4225
