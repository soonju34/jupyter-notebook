#!/usr/bin/env python
# coding: utf-8

# # 딕셔너리 응용

# ## 순서가 필요없는 데이터 에서 씀

# In[1]:


a = 1
a.__add__(3)


# #### 해당 키가 없으면 추가

# In[3]:


x = {'a':10, 'b':20, 'c':30}
x.setdefault('e',40)
print(x)


# In[4]:


x['f'] =50
print(x)


# In[6]:


x.update(a=90)
print(x)


# In[7]:


x.update(b=21, c=34)
print(x)


# In[8]:


x.update({1:'apple'})       #문자열이 아닐때
print(x)


# In[10]:


x[1] = 'pear'   #키값임 인덱스 아님
print(x) 


# In[11]:


a = {'a': 90, 'b': 21, 'c': 34, 'e': 40, 'f': 50, 1: 'apple'}
a.popitem()           # 파이썬 3.5 이상 버전은 뒤에서 부터 삭제


# In[12]:


a.popitem()


# In[13]:


print(a)


# In[14]:


a = {'a': 90, 'b': 21, 'c': 34, 'e': 40}
a.get('a')           # .get() ->dict


# In[15]:


a['a']


# In[16]:


a = {'a': 90, 'b': 21, 'c': 34, 'e': 40}
for i in a:           # 키만 받아옴
    print(i, end=' ')


# In[17]:


for k, v in a.items():
    print(k,v,sep=' : ')


# ### 이중 딕셔너리

# In[18]:


terrestrial_planet = {
    'mercury' : {
        'mean_radius' : 2439.7,
        'mass' : 3.3022E +23,
        'orbital_period' : 87.969,
    },
    'venus' : {
        'mean_radius' : 6051.0,
        'mass' : 4.8676E +24,
        'orbital_period' : 224.70069,
    }
}
print(terrestrial_planet['venus']['orbital_period'])


# # set()

# ### 안에 값은 중요치 않고 딕셔너리 덩어리의 관계

# # 람다(lambda)

# #### 변수생성 불가 조건식삽입 가능

# In[19]:


def plus_ten(x):
    return x+10

plus_ten(1)


# In[20]:


lambda x : x+ 10      # 인자 : 리턴값


# In[21]:


plus_ten = lambda x: x+10
plus_ten(1)              # 익명 함수 -> 1회용


# In[24]:


(lambda x: x+10)(1)


# In[25]:


list(map(lambda x: x+10, [1,2,3]))


# ### if를 쓰면 else는 무조건 잇어야 오류가 안생긴다

# In[26]:


a = list(range(1,11))          # if를 쓰면 else는 무조건 잇어야 오류가 안생긴다
list(map(lambda x: str(x) if x % 3 ==0 else x,a))   


# ### lambda 에는 elif가 없다 if else else....

# In[ ]:


a = list([random.randint(1,100) for i in range(10)])
print(a)
list(filter(lambda x x:5 and x < 50, a))


# # 리스트 컴프리헨션과 난수 함수를 이용하여 사용자가 입력한 횟수만큰 로또 번호를 출력하시오

# In[32]:


import random


# In[38]:


number =[]
while len(number) < 6:
    a = random.randint(1,46)
    if a not in number:
        number.append(a)


# In[39]:


print(number)


# In[40]:


num = int(input("로또 추첨 회수를 입력하세요").strip())
for _ in range(num):
    print(sorted(random.sample(range(1,46), 6)))


# # 로또 번호 1회 추첨하여 표본으로 삼고 이후 반복을 하면서 당첨 번호가 나올떄까지 횟수를 출력하시오

# In[2]:


from IPython.display import clear_output
import random
sample_lotto = sorted(random.sample(range(1,46), 6))
print(f"표본 {sample_lotto}")
count = 0
while True:
    count += 1
    lotto = sorted(random.sample(range(1,46), 6))
    if lotto == sample_lotto:
        print(f"{count} 회차 당첨")
        break
    else:
        clear_output(wait=True)
        print(f"{count} 당청 안됨")


# In[ ]:




