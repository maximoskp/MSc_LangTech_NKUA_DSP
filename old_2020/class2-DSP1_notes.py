# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:39:33 2020

@author: user
"""

import numpy as np

x = 1

y1 = 'lala'
y2 = 'lolo'
y3 = y1 + y2

c = 1.4

# lists
s = [1,3,5,6]
t = [4,5,6,7]
d = [9,6,3]
p = s + t
q = s + d
m = 2*s

# numpy arrays
s_array = np.array( s )
t_array = np.array( t )
p_array = s_array + t_array
d_array = np.array( d )
# q_array = s_array + d_array # <-- will produce error
m_array = 2*s_array

# sets
s1 = {1,2,'monkey'}
s2 = {2,'monkey',1}

# lists
l1 = [1,2,'monkey']
l2 = [2,'monkey',1]

# numpy array
a1 = np.array( l1 )

x = 'lala'
