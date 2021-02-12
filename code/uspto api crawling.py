# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:38:13 2020

uspto api crawling

@author: jaewoong Han
"""

# import library
import requests
import time
import pandas as pd

# parameter setting
# Ref : https://www.patentsview.org/api/query-language.html
url_post = 'http://www.patentsview.org/api/patents/query'
post_len = 10000

# Only Change Parameter : "patent_date" ex) "yyyy-mm-dd"
q1 = '?q={"_and":[ {"_gte":{"patent_date":"2012-01-01"}},{"_or":[{"_text_all":{"patent_title":'
q2 = '}},{"_text_all":{"patent_abstract":'
q3 = '}}]}]}'

# Patent Keyword Setting
# 2-1) patent keyword
searchText_T = ['smart home', 'smart factory','smart city','smart healthcare','e-government']
print(searchText_T)
print(len(searchText_T))

# Patent Request
# post total page list
total_patent = []

for t, search_t in enumerate(searchText_T):
    print("search num: ", t)
    print("search text: ", search_t)
    st = time.time()
    pt_dict_list = []
    # post first page
    try:
        q = q1 + '"' + searchText_T[t] + '"' + q2 + '"' + searchText_T[t] + '"' + q3
        # can add 'ipc_class', 'ipc_subclass', 'ipc_section'
        f = '&f=["patent_number","patent_title","patent_date",' \
            '"patent_type", "patent_abstract", "cpc_subgroup_id"]'
        o = '&o={"page":1,"per_page":10000}'
        o1 = '&o={"page":'
        o3 = ',"per_page":10000}'
        o = o1 + str(t + 1) + o3
        # print(q)
        t_data = q + f + o
        # print(t_data)
        t_post = requests.post(url_post + t_data).json()
        # print(t_post)
        print("total_patent_num :", t_post['total_patent_count'])
        pt_dict_list.extend(t_post['patents'])
        post_page = int(t_post['total_patent_count'] / post_len) + 2
        print("post page: ", post_page)

    except:
        print("=== Try error1 ===")

    # post total page
    if post_page > 2:
        for n in range(2, post_page):

            print("page number :", n, "/", post_page)
            try:
                # data = post_data(n,post_len,patent_date,search_t)
                js_data_post = requests.post(url_post + t_data).json()
                pt_dict_list.extend(js_data_post['patents'])

            except:
                print("=== Try error2 ===")

    et = time.time()
    print("exe_time :", et - st)
    time.sleep(1)
    total_patent.extend(pt_dict_list)
    
# Filter cpc List
# filter util patent (not design etc..)
util_patent = []
for pat in total_patent:

    if pat['patent_type'] == 'utility':
          util_patent.append(pat)
print(util_patent[0])

# cpcs ->list
st = time.time()
for d in util_patent:
    cpc_set = ''
    for c in d['cpcs']:
        try:
            cpc = c['cpc_subgroup_id'].split('/')[0]
            cpc_set = cpc_set + ',' + cpc
        except:
            cpc_set = cpc_set + 'None'
    d['cpc_set'] = cpc_set

et = time.time()
print("exe_time :",et-st)

print(util_patent[0])

# dict to dataframes
df = pd.DataFrame.from_dict(util_patent).drop(['cpcs'],axis=1)

print(df.iloc[0])
print('='*50)
print(df['cpc_set'][0])

# 중복 제거
df.drop_duplicates(['patent_number'], inplace=True)

print('Length of final patents', len(df)) # 특허 개수

# cpc 범위 조절
cpc_set=[]
for cpc in df['cpc_set']:
    cpc_set.append(cpc[1:])

# date
df['patent_date']=df['patent_date'].str.replace('-','')
df['patent_date']=pd.to_numeric(df['patent_date'])

# 기간 구분
data_up_1 = df['patent_date'] <= 20141231
data_up_2 = df[(df['patent_date'] >= 20150101) & (df['patent_date'] <= 20171231)]
data_up_3 = df['patent_date'] >= 20180101
data_up_1 = df[data_up_1]
data_up_3 = df[data_up_3]

# save
data_up_1.to_csv("4차 산업혁명_1.csv",encoding='utf8')
data_up_2.to_csv("4차 산업혁명_2.csv",encoding='utf8')
data_up_3.to_csv("4차 산업혁명_3.csv",encoding='utf8')














