#!/usr/bin/env python
# coding: utf-8

# # الوظيفة الأولى 
# رمق عزالدين سعود
# 1261

# In[3]:


#السؤال الأول الطلب الأول

grad_students=['ramaq','saeed','ahmad','samar','rana']
sname=input('Enter Name:')
if sname in grad_students:
    print(sname,'is graduated')
else:
    print(sname,"is'nt graduated")


# In[11]:


#السؤال الأول الطلب الثاني

odd=[x for x in range(1,1001) if x%2!=0]
print(odd)


# In[12]:


#السؤال الأول الطلب الثالث
L=['Network','Math','Programming','Physics','Music']
for i in L:
    if i.startswith('P'):
        print(i)


# In[15]:


#السؤال الأول الطلب الرابع
d={x:x**2 for x in range(1,11)}
print(d)


# In[20]:


#السؤال الثاني
def func(par1):
    binary=[]
    while par1>0:
        binary.append(par1%2)
        par1//=2
    binary.reverse()
    return binary
while True:
    n=int(input('enter decimal and -1 to stop: '))    
    if n==-1:
        break
    m=func(n)
    for i in m:
        print(i,end='')
    print()


# In[28]:


#السؤال الثالث
username=input('enter your name: ')
infile='t.txt'
outfile='outfile.txt'
infile1=open(infile,'r')
infile2=open(infile,'r')
outfile=open(outfile,'w')
a=0
l1=[line.rstrip().split(',')[0] for line in infile1]
l2=[line.rstrip().split(',')[-1] for line in infile2]
infile1.close()
infile1.close()
for i in range(len(l1)):
    print(l1[i])
    answer=input()
    if answer ==l2[i]:
        a+=1
l=[username+'\n',str(a)]
print(l)
outfile.writelines(l)
outfile.close()


# In[ ]:




