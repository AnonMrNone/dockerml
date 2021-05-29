#!/usr/bin/env python
# coding: utf-8

# In[2]:


import subprocess
import sys


# In[3]:


#taking the arguments
arg = sys.argv


# In[11]:


#splitting the arguments
img = arg[1]
contname = arg[2]
code = arg[3]
data = arg[4]
modelname = arg[5]


# In[7]:


docker = "docker -H tcp://65.0.21.186:6969"


# In[9]:


startcont = subprocess.getstatusoutput("{0} run -dit --name {1} {2}".format(docker,contname,img))
if startcont[0] == 0:
    print("[*]container created: {0}".format(startcont[1]))
else:
    print(startcont[1])


# In[ ]:


copycode = subprocess.getstatusoutput("{0} cp ./{1} {2}:/".format(docker,code,contname))
if copycode[0] == 0:
    print("[*]copied {0} to /".format(code))
else:
    print(copycode[1])
copyds = subprocess.getstatusoutput("{0} cp ./{1} {2}:/".format(docker,data,contname))
if copyds[0] == 0:
    print("[*]copied {0} to /".format(data))
else:
    print(copyds[1])


# In[ ]:


runcode = subprocess.getstatusoutput("{0} exec -it {1} python3 {2}".format(docker,contname,code))
if runcode[0] == 0:
    print("[*]code exec done")
else:
    print(runcode[1])


# In[ ]:


getmodel = subprocess.getstatusoutput("{0} cp {1}:/{2} ./".format(docker,contname,modelname))
if getmodel[0] == 0:
    print("[*]model copied to ./")
else:
    print(getmodel[1])


# In[ ]:


delcont = subprocess.getstatusoutput("{0} rm -f {1}".format(docker,contname))
if delcont[0] == 0:
    print("[*]container {0} deleted".format(contname))

