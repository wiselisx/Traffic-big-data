#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
save_path='公交数据.csv'
#只更改 公交数据.csv,改成你的数据命名
# 最后会出现两个csv格式的文件
# 一个是公交站点.csv，作为节点表格，数据格式选择gbk
# 一个是公交线路.csv，作为边表格，数据格式选择gbk，边的权重代表了这两个公交站之间运营的公交线路的条数，
#同一文件夹下输入数据名称，不同的化输入数据保存的绝对路径。


# In[2]:


data=pd.read_csv(save_path)
datas=pd.DataFrame(data)
a=datas.shape[0]#读取数据有多少行
b=[]
f=[]


# In[3]:


for i in range(0,a-1):
    if datas.iloc[i,1] == datas.iloc[i+1,1]:
        c=[datas.iloc[i,2],datas.iloc[i+1,2]]
        b.append(c)
#变量b储存相邻的公交站点
#f变量存储储存相邻的公交站点和其经纬度


# In[4]:


d=pd.DataFrame(b)
temp = [[name[0], name[1], len(group)] for name, group in d.groupby([0, 1])]
#对相邻的公交站点进行去重和计算重复次数，重复次数代表这一路段经过的公交线路的条数
data_re = pd.DataFrame(temp, columns=['source', 'target', 'Weight'])
#更改列名
data_re.to_csv('公交线路.csv',mode='a', header=True, index=False,encoding='ANSI')
#公交线路.csv作为gephi实验的边表格


# In[5]:


A=datas.iloc[:,2]
B=datas.iloc[:,2]
C=datas.iloc[:,4]
D=datas.iloc[:,3]
df = pd.concat([pd.DataFrame(A),pd.DataFrame(B), pd.DataFrame(C), pd.DataFrame(D)], axis=1)
data_re1 = df.drop_duplicates(subset='bus_Stop')
#对公交站点进行去重
data_re1.columns=['ID','LABEL','Lat','Lng']
#更改列名
data_re1.to_csv('公交站点.csv',mode='a', header=True, index=False,encoding='ANSI')
#公交站点.csv作为gephi实验的节点表格
#做一个小小的实验


# In[19]:


dot=datas['bus_Stop'].unique()
xianlu=pd.concat([pd.DataFrame(datas['bus_Name'].unique()),pd.DataFrame(datas['bus_Name'].unique())], axis=1)
xianlu.columns=['ID','LABEL']
datas


# In[24]:


dot
c=[]
d=[]
for i in dot:
    a=datas[datas['bus_Stop']==i]
    b=a.drop_duplicates()
    if b.shape[0]>=2:
        for i in range(0,b.shape[0]-2):
            c=[b.iloc[i,1],b.iloc[i+1,1]]
            d.append(c)
d=pd.DataFrame(d)


# In[33]:



temp = [[name[0], name[1], len(group)] for name, group in d.groupby([0, 1])]
data_re = pd.DataFrame(temp, columns=['source', 'target', 'Weight'])
d


# In[34]:


xianlu.to_csv('公交站点-对偶.csv',mode='a', header=True, index=False,encoding='ANSI')
data_re.to_csv('公交线路-对偶.csv',mode='a', header=True, index=False,encoding='ANSI')

