# Capstone - Anime series recommender

# ![banner](./assets/Banner.jpg)

## Problem Statement

There are plenty of people on this earth who, for one reason or another, have never properly given anime a chance.  

What is anime?  According to [Wikipedia](https://en.wikipedia.org/wiki/Anime):


> Anime (Japanese: アニメ) is hand-drawn and computer-generated animation originating from Japan. Outside of Japan and in English, anime refers specifically to animation produced in Japan.[1] However, in Japan and in Japanese, anime (a term derived from a shortening of the English word animation) describes all animated works, regardless of style or origin. Animation produced outside of Japan with similar style to Japanese animation is commonly referred to as anime-influenced animation. 

If someone WERE open-minded enough to give anime a try, how would we go about ensuring they have a good experience?  Maybe by recommending a few anime shows similar to live-action shows they already know and like.  Most existing recommendation engines do not often recommend anime as being similar to live-action shows, and are also not built to Advanced Search to return only anime or 'Animation'-genre results.  Let's try to change that.

---
## Executive Summary

Using TV show data from [IMDb](https://www.imdb.com/), [Wikipedia](https://en.wikipedia.org/), and [TheMovieDatabase](https://www.themoviedb.org/), I have built a recommender model that can be powered by a couple different modeling techniques in the background.  (A few of these techniques I used for this project include: LDA (Latent Dirichlet Allocation), LSI (Latent Semantic Indexing), and cosine similarity).

Given an input of a TV show name or the IMDb show page URL, we can generate a list of most-similar shows (as determined by computer).  Furthermore, the model is set up to return (for query results) all other relevant data parameters collected.  

---
## Data Dictionary

|Data Label|Source|dtype|Example|
|---|---|---|---|
|name|IMDb|object(str)|'My Hero Academia'|
|href|IMDb|object(str)|'/title/tt5626028/'|
|years|IMDb|object(str)|'(2016– )'|
|imdb_description|IMDb|object(str)|'A superhero-loving boy without any powers is d...'|
|pg_rating|IMDb|object(str)|'TV-14'|
|imdb_genre_tags|IMDb|object(pandas series)|Animation, Action, Adventure|
|imdb_rating|IMDb|float|8.3|
|num_votes|IMDb|int|68278|
|img_thumbnail|IMDb|object(str)|'https://m.media-amazon.com/images/M/MV5BOGZmYj...'|
|wiki_search_term|Wikipedia|object(str)|'My Hero Academia'|
|wiki_search_url|Wikipedia|object(str)|'https://en.wikipedia.org/wiki/My_Hero_Academia'|
|wiki_text|Wikipedia|object(str)|'My Hero Academia (Japanese: 僕のヒーローアカデミア, Hepbu...'|
|tmdb_id|TheMovieDB|float|65930.0|
|tmdb_name|TheMovieDB|object(str)|'My Hero Academia'|
|original_name|TheMovieDB|object(str)|'僕のヒーローアカデミア'|
|original_language|TheMovieDB|object(str)|'ja'|
|origin_country|TheMovieDB|object(str)|'['JP']	'|
|tmdb_popularity|TheMovieDB|float|93.045|
|tmdb_vote_average|TheMovieDB|float|8.701|
|tmdb_vote_count|TheMovieDB|float|4277.0|
|first_air_date|Wikipedia|object(str)|'2016-04-03'|
|tmdb_adult_content|TheMovieDB|object(str)|'False'|
|tmdb_poster_path|TheMovieDB|object(str)|'/ivOLM47yJt90P19RH1NvJrAJz9F.jpg'|
|tmdb_overview|TheMovieDB|object(str)|'In a world where eighty percent of the populat...'|
|tmdb_tagline|TheMovieDB|object(str)|NaN|
|tmdb_genres|TheMovieDB|object(pandas series)|Action & Adventure, Animation|
|tv_networks|TheMovieDB|object(pandas series)|Nippon TV, MBS, TBS, YTV|
|is_anime|self-generated|int|1|

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
## Sources & References

1. General Assembly DSI Lesson 705-lesson-recommender-systems
2. https://www.geeksforgeeks.org/nlp-gensim-tutorial-complete-guide-for-beginners/
3. (Jiamei Wang) https://medium.com/swlh/sentiment-analysis-topic-modeling-for-hotel-reviews-6b83653f5b08
4. (Mimi Dutta) https://www.analyticsvidhya.com/blog/2021/07/topic-modelling-with-lda-a-hands-on-introduction/
5. (Avinash Navlani) https://machinelearninggeek.com/latent-semantic-indexing-using-scikit-learn/
6. https://stackoverflow.com/questions/21285380/find-column-whose-name-contains-a-specific-string
7. https://www.statology.org/pandas-check-if-column-contains-string/
8. (Raiyan Quaium) https://medium.com/@raiyanquaium/how-to-web-scrape-using-beautiful-soup-in-python-without-running-into-http-error-403-554875e5abed
