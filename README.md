# Capstone

# ![banner](https://git.generalassemb.ly/wangdj3/project-3/blob/master/assets/Banner.jpg)
## Anime series recommender

---
## Problem Statement

There are plenty of people on this earth who, for one reason or another, have never properly given anime a chance.  

What is anime?  According to [Wikipedia](https://en.wikipedia.org/wiki/Anime):


> Anime (Japanese: アニメ) is hand-drawn and computer-generated animation originating from Japan. Outside of Japan and in English, anime refers specifically to animation produced in Japan.[1] However, in Japan and in Japanese, anime (a term derived from a shortening of the English word animation) describes all animated works, regardless of style or origin. Animation produced outside of Japan with similar style to Japanese animation is commonly referred to as anime-influenced animation. 

If someone WERE open-minded enough to give anime a try, how would we go about ensuring they have a good experience?  Maybe by recommending a few anime shows similar to live-action shows they already know and like.  Most existing recommendation engines are not built to Advanced Search to return only anime or 'Animation'-genre results.  Let's try to change that.

---
## Executive Summary

Given TV show data from [IMDb](https://www.imdb.com/), [Wikipedia](https://en.wikipedia.org/), and [TheMovieDatabase](https://www.themoviedb.org/), We have built a recommender model that can be powered by a couple different modeling techniques in the background.  Given an input of a TV show name or the IMDb show page URL, we can generate a list of most-similar shows (as determined by computer).  Furthermore, the model is set up to return all other relevant data parameters collected.  These parameters are given below:

['name', 'href', 'years', 'imdb_description', 'pg_rating',
       'imdb_genre_tags', 'imdb_rating', 'num_votes', 'img_thumbnail',
       'wiki_search_term', 'wiki_search_url', 'wiki_text', 'tmdb_id',
       'tmdb_name', 'original_name', 'original_language', 'origin_country',
       'tmdb_popularity', 'tmdb_vote_average', 'tmdb_vote_count',
       'first_air_date', 'tmdb_adult_content', 'tmdb_poster_path',
       'tmdb_overview', 'tmdb_tagline', 'tmdb_genres', 'tv_networks',
       'tmdb_keywords']


---
## Data Background

|Data Label|Source|
|---|---|
|name|IMDb|
|href|IMDb|
|years|IMDb|
|imdb_description|IMDb|
|pg_rating|IMDb|
|imdb_genre_tags|IMDb|
|imdb_rating|IMDb|
|num_votes|IMDb|
|img_thumbnail|IMDb|
|wiki_search_term|Wikipedia|
|wiki_search_url|Wikipedia|
|wiki_text|Wikipedia|
|tmdb_id|TheMovieDB|
|tmdb_name|TheMovieDB|
|original_name|TheMovieDB|
|original_language|TheMovieDB|
|origin_country|TheMovieDB|
|tmdb_popularity|TheMovieDB|
|tmdb_vote_average|TheMovieDB|
|tmdb_vote_count|TheMovieDB|
|first_air_date|Wikipedia|
|tmdb_adult_content|TheMovieDB|
|tmdb_poster_path|TheMovieDB|
|tmdb_overview|TheMovieDB|
|tmdb_tagline|TheMovieDB|
|tmdb_genres|TheMovieDB|
|tv_networks|TheMovieDB|
|is_anime|self-generated|

---
## Methodology

After data preprocessing, like lemmatizing, stopword removal, and tokenizing; several different models were constructed based on the collected data.


### Model Descriptions

##### Model 1: 
Latent Dirichlet Allocation (LDA)

##### Model 2:
Latent Semantic Indexing (LSI)

##### Model 3:
Weighted LDA

##### Model 4:
Keywords only One-Hot-Encoding, Cosine Similarity

##### Model 5:
Semi-Ensembled

The way the recommendations are generated, it's capable of generating anime-only results as well as all-shows results.

---
## Results/Primary Findings

I, as the resident anime expert, am not particularly impressed by the recommendations generated.  Further tuning is probably required.

Based on the internal algorithms used in the LDA/LSI processes, there was a good amount of randomness in the results generated, resulting in quite different results each time.  Sometimes (with the LDA models), it would spit out topic groups where two of the topics appear to be identical words & weights, which was weird.  Sometimes, catching it on a "good" model felt like catching lightning in a bottle. 

What was to be the highlight of the show, a Streamlit app, did not come to fruition, as it gave "low memory" errors when trying to run predictor.  This error persisted, even when running from local machine instead of as a Streamlet.io hosted webapp.  Therefore, in lieu, the recommender engine can be tried inside the '05_recommender...' series notebooks located inside the './code/' folder.

(The low memory issue is understandable, I suppose, because the computer must keep the entire matrices of topic similarities/weights in memory, because it doesn't know which show will be queried.)


---
## Conclusions/Next Steps

Though I am THOROUGHLY disappointed at how the results and end-product did not come to fruition as planned, much was learned about the topics of unsupervised learning and 


---
## Sources & References

1. General Assembly DSI Lesson 705-lesson-recommender-systems
2. https://www.geeksforgeeks.org/nlp-gensim-tutorial-complete-guide-for-beginners/
3. (Jiamei Wang) https://medium.com/swlh/sentiment-analysis-topic-modeling-for-hotel-reviews-6b83653f5b08
4. (Mimi Dutta) https://www.analyticsvidhya.com/blog/2021/07/topic-modelling-with-lda-a-hands-on-introduction/
5. (Avinash Navlani) https://machinelearninggeek.com/latent-semantic-indexing-using-scikit-learn/
6. https://stackoverflow.com/questions/21285380/find-column-whose-name-contains-a-specific-string
7. https://www.statology.org/pandas-check-if-column-contains-string/