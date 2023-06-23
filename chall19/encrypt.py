import numpy as np

def str_to_arr(string):
    return np.array([ ord(char) for char in string ])

with open("message.txt", "r") as file:
    flag = file.read()

f = str_to_arr(flag)
g = str_to_arr("enough to confuse them")
c = np.convolve(f, g)

for i in range(0,len(c)-1,2):
    if(abs(c[i]-c[i+1]) <= 10000):
        c[i] -= c[i+1]
        c[i+1] += c[i]
        c[i] = c[i+1]- c[i]

ciphertext=""
for i in c: ciphertext+=str(i) + " "

with open("encrypted.txt", "w") as f:
    f.write(ciphertext)
