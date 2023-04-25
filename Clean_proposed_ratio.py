#!/usr/bin/env python
# coding: utf-8

# In[1]:

  
import numpy as np

E1 = [0.02095595, 0.10207997, 0.34386311, 0.10347681, 0.32355996]

E1 = [round(e1, 2) for e1 in E1]
E1 = [E1] + [round(1-sum(E1), 2)]
E1 = str(E1)
E1 = E1.replace('[', '')
E1 = E1.replace(']', '')


E2 = [0.30066782, 0.07008543, 0.29193824, 0.01688483, 0.09917794]

E2 = [round(e2, 2) for e2 in E2]
E2 = [E2] + [round(1-sum(E2), 2)]
E2 = str(E2)
E2 = E2.replace('[', '')
E2 = E2.replace(']', '')
"""
E3 = [0.16836643, 0.26945089, 0.11308402, 0.17356542, 0.09180488]
E3 = [round(e1, 2) for e1 in E3]
E3 = [E3] + [round(1-sum(E3), 2)]
E3 = str(E3)
E3 = E3.replace('[', '')
E3 = E3.replace(']', '')
E4 = [0.53469204, 0.19364906, 0.04954231, 0.03100594, 0.18916575]
E4 = [round(e1, 2) for e1 in E4]
E4 = [E4] + [round(1-sum(E4), 2)]
E4 = str(E4)
E4 = E4.replace('[', '')
E4 = E4.replace(']', '')

print ('', E1, '\n', E2, '\n', E3, '\n', E4)
"""
print ('', E1, '\n', E2)

