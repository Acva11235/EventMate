import pymysql
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity


conn = pymysql.connect(host='localhost',
                        user='root',
                        password='Mysql1234',
                        database='eventmate')

user = pd.read_sql('SELECT StudentID as ID, tags FROM student where StudentID = "22BBS0129"', conn)   
events = pd.read_sql('SELECT EventID as ID, tags FROM Event', conn)   

df =  pd.concat([user, events], ignore_index=True)

cv = CountVectorizer(max_features=10, stop_words="english")

ps = PorterStemmer()

def stem(text):
    y = []
    
    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)

df['tags'] = df['tags'].apply(stem)

vectors = cv.fit_transform(df['tags']).toarray()

events = sorted(list(enumerate(cosine_similarity(vectors)[0])), reverse=True, key=lambda x:x[1])[1:6]

for i in events:
    print(df.iloc[i[0]]["ID"])
    

conn.close()

