#!/usr/bin/env python
# coding: utf-8

# ## Building Multipliers on Overall Optimism and Confidence

# In[1]:


x = 0
y = 0


# In[2]:


print('Pick a number on the scale:')
t = 0
while t == 0:
  x1 = input("How I organise myself...\n I complete the tasks as they come|1-----o2-----o3-----o4-----5|I have a to do list and complete the tasks:     ")
  if x1 == '1':
    x1 = -2
    x += x1
    t += 1
  elif x1 == '2':
    x1 = -1
    x += x1
    t += 1
  elif x1 == '3':
    x1 = 0
    x += x1
    t += 1
  elif x1 == '4':
    x1 = 1
    x += x1
    t += 1
  elif x1 == '5':
    x1 = 2
    x += x1
    t += 1
  else:
    print('Please try again, input a number from the scale...')


# In[3]:


print('Pick a number on the scale:')
t = 0
while t == 0:
  x2 = input("In what style do I complete my tasks?\n Pomodoro (25min blocks with 5min breaks)|1-----o2-----o3-----o4-----5|Large blocks (3-5hr blocks non-stop):     ")
  if x2 == '1':
    x2 = 2
    x += x2
    t += 1
  elif x2 == '2':
    x2 = 1
    x += x2
    t += 1
  elif x2 == '3':
    x2 = 0
    x += x2
    t += 1
  elif x2 == '4':
    x2 = -1
    x += x2
    t += 1
  elif x2 == '5':
    x2 = -2
    x += x2
    t += 1
  else:
    print('Please try again, input a number from the scale...')


# In[4]:


print('Pick a number on the scale:')
t = 0
while t == 0:
  y1 = input("Schedules make me...\n Stressed|1-----o2-----o3-----o4-----5|Relieved:     ")
  if y1 == '1':
    y1 = -2
    y += y1
    t += 1
  elif y1 == '2':
    y1 = -1
    y += y1
    t += 1
  elif y1 == '3':
    y1 = 0
    y += y1
    t += 1
  elif y1 == '4':
    y1 = 1
    y += y1
    t += 1
  elif y1 == '5':
    y1 = 2
    y += y1
    t += 1
  else:
    print('Please try again, input a number from the scale...')


# In[5]:


print('Pick a number on the scale:')
t = 0
while t == 0:
  x3 = input("How long do you usually spend trying to plan or organise yourself for the week?\n 10mins|-----o30mins-----o1hr-----o1hr 30mins-----2hrs|:     ")
  if x3 == '10mins':
    x3 = 2
    x += x3
    t += 1
  elif x3 == '30mins':
    x3 = 1
    x += x3
    t += 1
  elif x3 == '1hr':
    x3 = 0
    x += x3
    t += 1
  elif x3 == '1hr 30mins':
    x3 = -1
    x += x3
    t += 1
  elif x3 == '2hrs':
    x3 = -2
    x += x3
    t += 1
  else:
    print('Please try again, input a number from the scale...')


# In[6]:


print('Pick a number on the scale:')
t = 0
while t == 0:
  y2 = input("When I try to organise myself...\n I know some tasks might prevent me from completing all tasks|1-----o2-----o3-----o4-----5|I hope to get everything done:     ")
  if y2 == '1':
    y2 = -2
    y += y2
    t += 1
  elif y2 == '2':
    y2 = -1
    y += y2
    t += 1
  elif y2 == '3':
    y2 = 0
    y += y2
    t += 1
  elif y2 == '4':
    y2 = 1
    y += y2
    t += 1
  elif y2 == '5':
    y2 = 2
    y += y2
    t += 1
  else:
    print('Please try again, input a number from the scale...')


# In[7]:


print('Pick a number on the scale:')
t = 0
while t == 0:
  y3 = input("My ways of scheduling usually provide me:\n Opportunities to succeed|1-----o2-----o3-----o4-----5|Opportunities to do more:     ")
  if y3 == '1':
    y3 = 2
    y += y3
    t += 1
  elif y3 == '2':
    y3 = 1
    y += y3
    t += 1
  elif y3 == '3':
    y3 = -1
    y += y3
    t += 1
  elif y3 == '4':
    y3 = 1
    y += y3
    t += 1
  elif y3 == '5':
    y3 = 2
    y += y3
    t += 1
  else:
    print('Please try again, input a number from the scale...')


# In[8]:


print(x)
print(y)


# In[64]:


print('-----------Overall Confidence and Optimism-----------')
print('Confidence:', x/3)
print('Optimism:', y/3)


# In[10]:


x = x/3
y = y/3


# In[73]:


from math import exp, ceil


# In[33]:


#g = float(exp(1))


# In[61]:


def time_multi(a, b):
  if a >= 0 and b >= 0:
    num_1 = -3*(exp(-((a)**2+(b)**2)**2))+4
    return num_1
  elif a >= 0 and b <= 0:
    new_val = a + b
    if new_val >= 0:
      b = new_val
      num_2 = -3*(exp(-((a)**2+(b)**2)**2))+4
      return num_2
    elif new_val <= 0:
      a = new_val
      num_3 = exp(-((a)**2+(b)**2)**2)
      return num_3
  elif a <= 0 and b >= 0:
    new_val = b + a
    if new_val >= 0:
      a = new_val
      num_4 = -3*(exp(-((a)**2+(b)**2)**2))+4
      return num_4
    elif new_val <= 0:
      b = new_val
      num_5 = exp(-((a)**2+(b)**2)**2)
      return num_5
  elif a <= 0 and b <= 0:
    num_6 = exp(-((a)**2+(b)**2)**2)
    return num_6


# In[62]:


multi_1 = time_multi(x, y)
print(multi_1)


# In[ ]:


if multi_1 < 0.25:
    multi_1 = 0.25
    print('New multi_1 adjustment:', multi_1)


# ## Building Confidence Multipliers based on individual tasks

# In[18]:


print('Three point estimation - Provide the following estimations for the total time in hours you wish to spend for the task:')
print('NOTE: Use decimal notation for mins.')
t = 0
while t == 0:
  x_1 = input('Best-case scenario estimate: ')
  try:
    x_1 = float(x_1)
  except:
    print('Please input a number...')
  else:
    t += 1

t1 = 0
while t1 == 0:
  y_1 = input('Worst-case scenario estimate: ')
  try:
    y_1 = float(y_1)
  except:
    print('Please input a number...')
  else:
    if x_1 > y_1:
        t1 += 1
    else:
        print('Please input a number less than', x_1)

t2 = 0
while t2 == 0:
  z_1 = input('Most-likely-case scenario estimate: ')
  try:
    z_1 = float(z_1)
  except:
    print('Please input a number...')
  else:
    if z_1 > y_1 and z_1 < x_1:
        t2 += 1
    else:
        print('Please input a number in between', y_1 ,'and', x_1)


# In[36]:


j = -((x_1 - y_1)/x_1 * 4 + (-2))
k = -((x_1 - z_1)/x_1 * 4 + (-2))
print('-----------Confidence and optimism for the individual task-----------')
print('Confidence:', j)
print('Optimism:', k)


# In[55]:


'''
def time_multi2(a, b):
  if a > 0 and b > 0:
    v_1 = -3*(math.exp(-((a)**2+(b)**2)**2))+4
    return v_1
  elif a > 0 and b < 0:
    new_val = a + b
    if new_val >= 0:
      b = new_val
      v_2 = -3*(math.exp(-(a**2+b**2)**2))+4
      return v_2
    elif new_val <= 0:
      a = new_val
      v_3 = math.exp(-(a**2+b**2)**2)
      return v_3
  elif a < 0 and b > 0:
    new_val = b + a
    if new_val >= 0:
      a = new_val
      v_4 = -3*(math.exp(-(a**2+b**2)**2))+4
      return v_4
    elif new_val <= 0:
      b = new_val
      v_5 = math.exp(-(a**2+b**2)**2)
      return v_5
  elif a < 0 and b < 0:
    v_6 = math.exp(-(a**2+b**2)**2)
    return v_6
'''
    


# In[1]:


# error keeps coming saying that "'int' object is not callable", hence proceed
# to next block where instead of using a function the same block of code is repeated
multi_2 = time_multi(j, k)
multi_2 = multi_2/2.6666666666667
if multi_2 < 0.25:
    multi_2 = 0.25
print('Specific task multiplier:', multi_2)


# In[78]:


new_multi = multi_2 * multi_1
print('-----------Recommendation-----------')
print('Combined multiplier:', new_multi)
print('Therefore you should spend', new_multi*z_1, 'hrs on this task each week.')
p1 = 0

while p1 == 0:
    days = input('How many days would you like to commit to this task each week?:    ')
    try:
        days = int(days)
    except:
        print('Please input a whole number of days...')
    else:
        if days > 7:
            print('There are only 7 days in a week...')
        else:
            p1 += 1

import datetime
time = round((new_multi*z_1)/(days), 2)
hour = int(time)
minute = int((time - int(time))*60.0)
print('You should spend', (datetime.time(hour, minute)).strftime('%H:%M'), '(hrs:mins) each day on this task.')

