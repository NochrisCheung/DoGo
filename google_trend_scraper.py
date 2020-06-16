from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd
import json
import os.path
import fnmatch

pytrends = TrendReq(hl='en-UK', tz=360,  timeout=(10,25))
kw_list = []
json_dir = './google_trend_search/'

def define_search(search_term_list):
    global kw_list
    kw_list = search_term_list
    pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='GB-ENG')

def get_related_search_terms(parent_search_term, layer_num):
    define_search([parent_search_term])
    pytrends.related_queries()
    related_queries = pytrends.related_queries()[parent_search_term]['top']
    query, value = related_queries['query'], related_queries['value']
    related_queries_dict = {'layer': layer_num}
    related_queries_dict[parent_search_term] = dict(zip(query, value))
    with open(json_dir+str(layer_num)+'_'+parent_search_term+'_related_queries.json', 'w') as f:
        json.dump(related_queries_dict,f)
        f.close

def scraper_related_search_terms(top_parent_search_term = 'delivery', start_layer_num = 0, end_layer_num = 2):
    for layer_num in range(start_layer_num, end_layer_num):
        if layer_num == 0:
            get_related_search_terms(top_parent_search_term, layer_num)
        else:
            for file in os.listdir('./google_trend_search/'):
                if fnmatch.fnmatch(file, '*'+str(layer_num - 1)+'*'):
                    with open(json_dir+file, 'r') as f:
                        related_keyword_dict = json.load(f)
                        related_search_term_list = list(related_keyword_dict[list(related_keyword_dict)[1]])
                        f.close
                    for related_search_term in related_search_term_list:
                        get_related_search_terms(related_search_term, layer_num)

def find_json(keyword, layer_num):
    for file in os.listdir('./google_trend_search/'):
        if fnmatch.fnmatch(file, str(layer_num)+'_'+keyword+'_related_queries.json'):
            return file

def read_json(file):
    with open(json_dir+file, 'r') as json_file:
        keyword_dict = json.load(json_file)
        json_file.close
    return keyword_dict

def append_keyword_list(keyword_dict):
    keyword_and_value = pd.DataFrame.from_dict(list(keyword_dict[list(keyword_dict)[1]].items()))
    keyword_list = keyword_and_value[0]
    with open(json_dir+'keyword_list.csv', 'a') as file:
        for keyword in keyword_list:
            file.write(keyword + '\n')
        file.close

def collect_all_keywords():
    for file in os.listdir('./google_trend_search/'):
        append_keyword_list(read_json(file))

def read_and_process_keyword_list_csv():
    full_keyword_list = pd.read_csv(json_dir+'keyword_list.csv',names = ['keywords'])
    full_keyword_list = full_keyword_list.drop_duplicates(subset=None, keep='first', inplace=False)
    full_keyword_list['string_length'] = [len(kw) for kw in full_keyword_list['keywords'].values]
    full_keyword_list = full_keyword_list.sort_values(by=['string_length'], ascending=True)
    full_keyword_list = full_keyword_list.reset_index(drop = True)
    return full_keyword_list

first_word = [full_keyword_list['keywords'][0]]
aggregated_data = pd.DataFrame()
for i in range(0,200):
    print(i)
    compare_list = first_word + full_keyword_list['keywords'][i*4+1:(i+1)*4+1].values.tolist()
    define_search(compare_list)
    data = pytrends.interest_over_time()
    tranposed_data = data[data.columns[0:-1]].transpose()
    aggregated_data = aggregated_data.append(tranposed_data)

aggregated_data

trial_process = aggregated_data

trial_process['mean'] = trial_process.mean(axis = 1)
sorted_trial_process = trial_process.sort_values(by=['mean'], ascending = False)
reindexed_sorted_trial_process =sorted_trial_process.reset_index()

remove_dupliated_trial_process = reindexed_sorted_trial_process.groupby('index').mean().reset_index()
remove_dupliated_trial_process = remove_dupliated_trial_process.sort_values(by=['mean'], ascending = False)
remove_dupliated_trial_process[remove_dupliated_trial_process['mean'] <= 10]

plt.plot(remove_dupliated_trial_process['mean'].values)


define_search(full_keyword_list['keywords'].head(5).values.tolist())
data = pytrends.interest_over_time()
tranposed_data = data[data.columns[0:-1]].transpose()
new_data = new_data.append(new_data)
new_data
data[data.columns[0:-1]].to_csv('first_interaction.csv',index = False)
plt.plot(data)

# for layer_num in range(0,1):
#     if layer_num == 0:
#         top_layer_search_term_df = pd.DataFrame.from_dict(list(data[list(data)[1]].items()))
#     else:
#         parent_term = list(data)[1]
#         search_term_df = pd.DataFrame.from_dict(list(data[list(data)[1]].items()))
#         search_term_df[search_term_df[0] == 'free delivery']
#         parent_term
#
#         related_search_term_df.columns = ['search_terms','index']
