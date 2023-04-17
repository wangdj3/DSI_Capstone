import streamlit as st

st.write("""
TEST 123
""")

#!/usr/bin/env python
# coding: utf-8

# # Recommender output

# #### Set input & output parameters

# In[183]:


raw_data_directory = "../data/"
output_directory = "../outputs/"


# In[184]:


input_model_name = "lda_lsi_weighted_1_run1" #manually input the filename (no extension) of csv to be used as input


# In[185]:


anime_output_only = True


# #### Imports

# In[186]:


import numpy as np
import pandas as pd

from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_distances

# for progress bar on loops
from tqdm import tqdm


# #### Read in Dataframe of raw data with info columns

# In[187]:


lookup_df = pd.read_csv(f"{raw_data_directory}merged_nowiki_df.csv")


# In[188]:


lookup_df.head(2)


# In[189]:


lookup_df.columns


# #### Read in Dataframe of modeling results

# In[190]:


df = pd.read_csv(f"{output_directory}{input_model_name}.csv")
df.head()


# In[191]:


df.shape


# In[192]:


df.isna().sum()


# In[193]:


df.fillna("",inplace=True)


# #### Make lookup tables for href to name, href to years

# > Because there are instances of 'name' not being unique, we use 'href' as the unique index instead.

# In[194]:


href_to_name_dict = {}

for i in range(len(df)):
    href_to_name_dict[ df.loc[i,'href'] ] = df.loc[i,'name']


# In[195]:


href_to_years_dict = {}

for i in range(len(lookup_df)):
    href_to_years_dict[ lookup_df.loc[i,'href'] ] = lookup_df.loc[i,'years']


# In[196]:


len(href_to_name_dict)


# #### Select only the columns we want

# In[197]:


df.columns


# In[198]:


# Technique Reference: https://stackoverflow.com/questions/21285380/find-column-whose-name-contains-a-specific-string

columnns_to_drop =[]

dropcol_prefix = "lsa_topic"
columnns_to_drop = [col for col in df if dropcol_prefix in col]

dropcol_prefix2 = "forced_alt_lda_"
columnns_to_drop += [col for col in df if dropcol_prefix2 in col]

df.drop(columns=['name']+columnns_to_drop, inplace=True)
df.head(3)


# In[199]:


df.columns


# In[200]:


df.set_index('href', inplace=True)


# #### Generate cosine similarity matrix

# In[201]:


# Generate a matrix of cosine similarities that can be used for lookup
dists = cosine_distances(df)
cos_similarities_df = pd.DataFrame(dists, index=df.index, columns=df.index)
cos_similarities_df.head()

# Reference: General Assembly DSI Lesson 705-lesson-recommender-systems


# ## Define functions for generating results from requests

# #### Function to generate a dataframe of the looked up show info, given a dataframe/list of similarity results 

# In[203]:


def display_results_info(raw_results, num_results_to_show=5, anime_output_only=anime_output_only, lookup_df=lookup_df):

    display_results_df = pd.DataFrame(columns = lookup_df.columns)
    # display_results_df['match_score'] = ''
    
    if num_results_to_show > len(raw_results):
        num_results_to_show = len(raw_results)
        print(f"Warning: requested number of results exceeds number of possible outputs.")

    if isinstance(raw_results, list): 
        raw_results_indices = raw_results
    elif isinstance(raw_results, pd.DataFrame):
        raw_results_indices = raw_results.index
    else:
        print("Error- unsupported type passed to display_results function. Only takes: list or dataframe")
        return

    if anime_output_only:
        i = 0
        j = 0
        while i < len(raw_results_indices) and j < num_results_to_show:
            lookup_item = raw_results_indices[i]
            temp_row = lookup_df[lookup_df['href']== lookup_item]

            i += 1

            if anime_output_only:
                if (temp_row['is_anime']==1).bool():
                    display_results_df = pd.concat([display_results_df, temp_row])
                    j += 1
                else: 
                    # print(f"{str(temp_row[['name']])} is not anime")
                    pass
            else:
                display_results_df = pd.concat([display_results_df, temp_row])
                j += 1
    else:
        for i in range(num_results_to_show):
            lookup_item = raw_results_indices[i]
            temp_row = lookup_df[lookup_df['href']== lookup_item]

            display_results_df = pd.concat([display_results_df, temp_row])   

    if len(display_results_df) < num_results_to_show:
        print(f"Sorry- there are not {num_results_to_show} results to be shown.")

    return display_results_df


# #### Function to generate a list of recommendations (most similar entries), based on cosine similarity

# In[204]:


def results_from_href(href, num_results=5, anime_output_only=anime_output_only, lookup_df=lookup_df):

    if (lookup_df['href'].eq(href)).any():

        # Create & populate a df with cos_similarities and 'name' cols ('href' is index), ranked by similarity
        raw_rec_results = cos_similarities_df[href].sort_values()
        
        raw_rec_results_df = pd.DataFrame(raw_rec_results)
        raw_rec_results_df['name'] = np.nan  #need to create the blank column first, otherwise it will Error

        for i in range(len(raw_rec_results_df)):
            lookup_item = raw_rec_results_df.index[i]
            item_name = href_to_name_dict[lookup_item]

            temp_row = raw_rec_results_df.iloc[i,:].copy()
            temp_row['name'] = item_name
            raw_rec_results_df.iloc[i,:] = temp_row
        
        return display_results_info(raw_rec_results_df, num_results, anime_output_only, lookup_df) 

    else:
        print(f"(Error in results_from_href function.) No exact match found for the following href input. Please try again:\n{href}")
        return   


# Technique reference for boolean checking on search string: https://www.statology.org/pandas-check-if-column-contains-string/


# #### (Helper function for getting 'href' info in proper string form)

# In[205]:


def get_href_as_str(href_entry):
    '''
    A helper function, since desired output is usually a dataframe.  Casting to string adds unwanted info into it.
    
    '''

    split_list = href_entry.split("/")
    return f"/{split_list[1]}/{split_list[2]}/"


# #### The "main" function, that generates full output based on user entry. (Accepts show titles or href strings as input.)

# In[ ]:





# In[206]:


def get_recommendations(input_name, num_results=5, anime_output_only=anime_output_only):
    
    if (anime_output_only):
        print("Generating Anime Output Only... \n")
    else:
        print("All results types being displayed... \n")
    
    if not isinstance(input_name, str):
        print("Error: Input a string, plz")
        return
    elif "/title/" in input_name:
        try:
            temp_results = results_from_href(input_name, num_results, anime_output_only=anime_output_only)
            print(f"Displaying results for: {href_to_name_dict[input_name]} {href_to_years_dict[input_name]}. href: {input_name}\n")

            if len(temp_results) < num_results:
                print(f"Only {len(temp_results)} results found, compared to the requested {num_results}.")

            return temp_results
        except:
            return
    
    else:
        name = input_name.lower().strip()
        found_names_df = lookup_df[lookup_df['name'].str.lower().str.contains(name)]
        num_results_found = len(found_names_df)

        if num_results_found == 0:
            found_names_df = lookup_df[lookup_df['name'].str.lower().str.contains(name[:int(np.floor(len(name)/2))])]
            num_results_found = len(found_names_df)
            
            if num_results_found > 0:
                print(f"No exact matches.  {num_results_found} results starting the same found. Please copy/paste in href of desired entry from list or try again. \n")
                print(found_names_df[['name', 'years', 'href']])
            else:
                found_names_df = lookup_df[lookup_df['name'].str.lower().str.contains(name[:int(np.floor(len(name)/4))])]
                num_results_found = len(found_names_df)
                
                if num_results_found > 0:
                    print(f"No exact matches.  {num_results_found} results starting the same found. Please copy/paste in href of desired entry from list or try again. \n")
                    print(found_names_df[['name', 'years', 'href']])
                else:
                    print("No matches found starting with those characters.  Try again, focusing on the first few chars.")
            return
        elif num_results_found > 1:
            print(f"{num_results_found} results found starting with your entry. Please copy/paste in href of desired entry from list or try again. \n")
            print(found_names_df[['name', 'years', 'href']])
            return
        else:
            # print(found_names_df['href'])
            if (lookup_df['name'].eq(name)).any():
                print(f'Exact match found for "{input_name}". Generating recommendations... \n')
            else:
                print(f'1 "match" found starting with "{input_name}". Generating recommendations...')
                        
            search_href = get_href_as_str(str(found_names_df['href']))
            
            temp_results = results_from_href(search_href, num_results, anime_output_only=anime_output_only)
            print(f"Displaying results for: {href_to_name_dict[search_href]} {href_to_years_dict[search_href]}. href: {search_href}\n")

            if len(temp_results) < num_results:
                print(f"Only {len(temp_results)} results found, compared to the requested {num_results}.")

            return temp_results



# Calling our function by prompting user for query string

user_input = input ("Enter a show title to search: ")

get_recommendations(user_input)

