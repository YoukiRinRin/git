import tqdm
import numpy as np
import keyboard 


print('タイミングよくEnterキーを押してバットを振ろう')

while 1:
    for i in tqdm.tqdm(range(int(1e7))):
        np.pi*np.pi
        if i % 1e6 == 0:
            print(i)
    
        if keyboard.read_key() == "p":
            break
        elif keyboard.read_key() == :
           continue
    if keyboard.read_key() == "p":
        break
    elif keyboard.read_key() == None:
        continue

            