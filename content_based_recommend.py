
def stem(text):
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()   

    y = []
    
    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)


def content_based_recommender(regno, k):

    import pymysql
    import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity


    conn = pymysql.connect(host='localhost',
                        user='root',
                        password='1234',
                        database='eventmate')
    
    user = pd.read_sql(f'SELECT StudentID as ID, tags FROM student where StudentID = "{regno}"', conn)   
    events = pd.read_sql('SELECT EventID as ID, tags, description FROM Event', conn)

    df =  pd.concat([user, events], ignore_index=True)

    from rake_nltk import Rake

    for i in range(len(df)):

        r = Rake()
        if i:
            r.extract_keywords_from_text(df.iloc[i]["description"])
            keywords_with_scores = r.get_ranked_phrases_with_scores()

            for score, keyword in keywords_with_scores:
                if(score > 3):
                    df.loc[i, 'tags'] = df.loc[i, 'tags'] + f", {keyword}"

    df['tags'] = df['tags'].apply(stem)

    cv = CountVectorizer(max_features=50, stop_words="english") 

    vectors = cv.fit_transform(df['tags']).toarray()

    events = sorted(list(enumerate(cosine_similarity(vectors)[0])), reverse=True, key=lambda x:x[1])[1:k+1]

    recommendations = []

    for i in events:
        recommendations.append(df.iloc[i[0]]["ID"])

    return recommendations