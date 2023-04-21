import numpy as np
import re
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
with open(r'E:\\4\\Text-2.txt', 'r') as f:
    content=f.read()
    a=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    b=np.array(["the","eye","of","existence","hair","and","nature","month","head","darwin","size","touch","second","conclusion","revolution","muscles","necessity","public","body","within","to","in","distribution","words"])
    x1 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("the"), content))
    a[0]=x1
    x2 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("eye"), content))
    a[1]=x2
    x3 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("of"), content))
    a[2]=x3
    x4 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("existence"), content))
    a[3]=x4
    x5 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("hair"), content))
    a[4]=x5
    x6 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("and"), content))
    a[5]=x6
    x7 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("nature"), content))
    a[6]=x7
    x8 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("month"), content))
    a[7]=x8
    x9 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("head"), content))
    a[8]=x9
    x10 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("darwin"), content))
    a[9]=x10
    x11 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("size"), content))
    a[10]=x11
    x12 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("touch"), content))
    a[11]=x12
    x13 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("second"), content))
    a[12]=x13
    x14 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("conclusion"), content))
    a[13]=x14
    x15 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("revolution"), content))
    a[14]=x15
    x16 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("muscles"), content))
    a[15]=x16
    x17 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("necessity"), content))
    a[16]=x17
    x18 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("public"), content))
    a[17]=x18
    x19 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("body"), content))
    a[18]=x19
    x20 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("within"), content))
    a[19]=x20
    x21 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("to"), content))
    a[20]=x21
    x22 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("in"), content))
    a[21]=x22
    x23 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("distribution"), content))
    a[22]=x23
    x24 = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("words"), content))
    a[23]=x24
    c=a.copy()
    a=np.sort(a)[::-1]
    print("word : rank : frequency")
    for x in range(24):
        print(b[x],":",np.where(a == c[x])[0][0]+1,":",c[x])
xaxis = np.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])
for x in range(24):    
        xaxis[x] = np.log(x+1)  
yaxis = np.log(a.copy())
yaxis[23]=0
figure, axis = plt.subplots(2, 2)

axis[0, 0].plot(xaxis, yaxis)
axis[0, 0].set_title('loglog_DD.png')
sum=0
for y in range(24):
    sum = sum + a[y]
p=0.5/sum
erdos = nx.erdos_renyi_graph(sum,p)
watts = nx.watts_strogatz_graph(sum,5,p)
barabasi = nx.barabasi_albert_graph(sum,3,1)
#erdos
degrees = dict(erdos.degree()) # dictionary node:degree
# filtering nodes outdegree values with outdegree > 0
pos_degree_vals = list(filter(lambda val: val > 0,  degrees.values()))
# getting unique and sorted outdegree values
uq_pos_degree_vals = sorted(set(pos_degree_vals))
# counting frequency of each outdegree values
hist = [pos_degree_vals.count(x) for x in uq_pos_degree_vals]
x = np.asarray(uq_pos_degree_vals, dtype = float)
y = np.asarray( hist, dtype = float)
logx = np.log10(x)
logy = np.log10(y)
axis[0, 1].plot(logx, logy)
axis[0, 1].set_title("Erdos")
#watts
degrees = dict(watts. degree()) # dictionary node:degree
# filtering nodes outdegree values with outdegree > 0
pos_degree_vals = list(filter(lambda val: val > 0,  degrees.values()))
# getting unique and sorted outdegree values
uq_pos_degree_vals = sorted(set(pos_degree_vals))
# counting frequency of each outdegree values
hist = [pos_degree_vals.count(x) for x in uq_pos_degree_vals]
x = np.asarray(uq_pos_degree_vals, dtype = float)
y = np.asarray( hist, dtype = float)
logx = np.log10(x)
logy = np.log10(y)
axis[1, 0].plot(logx, logy)
axis[1, 0].set_title("watts")
#barabasi
degrees = dict(barabasi. degree()) # dictionary node:degree
# filtering nodes outdegree values with outdegree > 0
pos_degree_vals = list(filter(lambda val: val > 0,  degrees.values()))
# getting unique and sorted outdegree values
uq_pos_degree_vals = sorted(set(pos_degree_vals))
# counting frequency of each outdegree values
hist = [pos_degree_vals.count(x) for x in uq_pos_degree_vals]
x = np.asarray(uq_pos_degree_vals, dtype = float)
y = np.asarray( hist, dtype = float)
logx = np.log10(x)
logy = np.log10(y)
axis[1, 1].plot(logx, logy)
axis[1, 1].set_title("barabasi")

plt.savefig('loglog_DD.png')