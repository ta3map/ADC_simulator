import pandas as pd
import numpy as np

def hello():
    print('ADC is imported')
    return None

def rec(v, samples, quant_levels, samplerate):
    path = '/content/ADC_simulator/data/data'+ str(v) +'_v2'

    y = pd.read_csv(path,  header=None).to_numpy().flatten()
    Fs, y = int(y[0]), y[1:]
    
    difference = int(Fs*(samples/samplerate - (len(y)/Fs)))
    
    if difference>=0:
        std_y = np.std(y)
        mean_y = np.mean(y)
        a = std_y/2
        y = np.append(y, a*np.random.rand(difference,)+mean_y-a/2)
    else:
        y = y[0:int(len(y)+difference)]
    
    # ADC :
    converted_y = np.zeros(np.size(y));
    
    i = 0;
    for level in quant_levels:
        converted_y[y > level] = level;
        i += 1
    
    rate_step = round(Fs/samplerate);
    converted_y = converted_y[0:np.size(y):rate_step]
    return converted_y
