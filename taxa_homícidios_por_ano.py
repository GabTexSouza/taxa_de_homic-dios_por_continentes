#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[35]:


df = pd.read_csv(r'C:\Users\gabri\Desktop\projeto.csv', sep = ';')
df = df.rename(columns={'Número_de_Suícidios': 'Número de Homicídios'})


# In[36]:


df


# In[37]:


df.shape


# In[38]:


df.info()


# In[39]:


df.isnull().sum()


# In[40]:


df.describe()


# In[42]:


lista = ['Rate', 'Número de Homicídios', 'Ano']
for a in lista:
    print(a)
    df[a] = df[a].astype(int)


# In[43]:


df


# In[44]:


df1 = df.sort_values('Número de Homicídios', ascending=False).head(5)
df1


# In[45]:


df1 = df[['País','Número de Homicídios']].sort_values(by  = 'Número de Homicídios', ascending = False).head(5)
df1['Porcentagem'] = (df1['Número de Homicídios'] * 100 / df1['Número de Homicídios'].sum()).round(2)
df1


# In[46]:


df1.plot(x = 'País', y = 'Número de Homicídios', kind = 'pie', labels = df1.País, autopct = '%1.2f%%' )
plt.legend().set_visible(False)


# In[47]:


df2 = df.groupby('Região')['Número de Homicídios'].sum().sort_values(ascending=False)
df2


# In[48]:


df2.plot(kind = 'bar')
plt.show()


# In[49]:


df3 = df.groupby('Sub_Região')['Número de Homicídios'].sum().sort_values(ascending = False)
df3


# In[50]:


df3.index


# In[28]:


df3.values


# In[29]:


sns.barplot(x= df3.index, y = df3.values)
plt.xticks(rotation = 90)
xlabel = None


# In[51]:


df


# In[52]:


df[df['Região'].isin(['Ásia', 'Europa'])]


# In[54]:


df4 = df[(df['Região'] == 'Ásia') | (df['Região'] == 'Europa')]
df4 = df4[df4['Ano'] > 2016][['Região', 'Ano', 'Número de Homicídios']]
df4


# In[55]:


df4 = df4.groupby(['Região','Ano']).sum()['Número de Homicídios']
df4


# In[57]:


df_visual = df4.unstack(level = 0)
df_visual


# In[69]:


df_visual.index = df_visual.index.astype(int).astype(str)


# In[ ]:





# In[71]:


df_visual.plot(kind = 'line', figsize = (10,6))
plt.xlabel = 'Ano'
plt.ylabel = 'Número de Homicídios'
plt.title('Número de Homicidios na Europa e Ásia (2017 - 2019)')


# In[72]:


df


# In[75]:


df5 = df.groupby(['Ano'])['Rate'].sum().sort_values(ascending = False)
df5


# In[78]:


df5.plot(kind = 'bar', figsize = (7,3), color = 'red', edgecolor = 'black')
plt.title('Taxa de Homicidio através dos anos')


# In[104]:


df6 = df[['Ano','Região', 'Número de Homicídios']]
df6 = df6.groupby(['Ano', 'Região']).sum().sort_values(by= 'Ano', ascending = False)
df6


# In[113]:


df6.plot(kind = 'bar', figsize= (12,6), colormap = 'plasma')
plt.xlabel = 'Ano'
plt.ylabel = 'Número de Homicídios'
plt.title('Número de Homicidios por Ano e Região')
plt.show()


# In[ ]:





# In[118]:


df7 = df.groupby('Sub_Região')['Número de Homicídios'].mean().sort_values(ascending = False).round(2)
df7


# In[ ]:





# In[119]:


df7.index


# In[120]:


df7.values


# In[123]:


data = {
    
    'Categoria': df7.index,
    'Valores': df7.values,
    'Info': df7.values
}
df = pd.DataFrame(data)
df


# In[126]:


import plotly.express as px


# In[131]:


fig = px.treemap(df, path = ['Categoria'], values = 'Valores', title = 'Treemap')
fig.update_traces(hovertemplate = 'Category: %{label}<br>Value:%{value}')
fig.show()


# In[ ]:





# In[ ]:


df.to


# In[ ]:





# In[ ]:




