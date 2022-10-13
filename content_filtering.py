from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df=pd.read_csv('articles.csv',encoding="utf-8")
df=df[df['title'].notna()]
count=CountVectorizer(stop_words='english')
count_metrics=count.fit_transform(df['title'])
cosin_sim=cosine_similarity(count_metrics,count_metrics)
df=df.reset_index()
indices=pd.Series(df.index,index=df['contentId'])
def get_recommendations(contentId):
    idx=indices[int(contentId)]
    sim_scores=list(enumerate(cosin_sim[idx]))
    sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
    sim_scores=sim_scores[1:11]
    article_indices=[i[0]for i in sim_scores]
    return df[['url','title','text','lang','total_events']].iloc[article_indices].values.tolist()