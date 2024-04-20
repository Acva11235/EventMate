def stem(text):
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()   

    y = []
    
    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)

def collaborative_filtering_recommder(regno, k):

    import pymysql
    import pandas as pd
    import numpy as np
    from rake_nltk import Rake
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    conn = pymysql.connect(host='localhost',
                            user='root',
                            password='1234',
                            database='eventmate')
    

    ratings = pd.read_sql('SELECT * FROM studentrating', conn)   

    minimum_rating = 3

    x = ratings.groupby("StudentID").count()["Rating"] >= minimum_rating
    frequent_users = x[x].index
    
    filtered_ratings = ratings[ratings['StudentID'].isin(frequent_users)]

    minimum_event_appearance = 3

    y = filtered_ratings.groupby("EventID").count()["Rating"] >= minimum_event_appearance
    famous_events = y[y].index

    final_ratings = filtered_ratings[filtered_ratings["EventID"].isin(famous_events)]

    students = pd.read_sql(f'SELECT StudentID as ID, tags, Branch, Year, Program FROM student', conn) 

    students['tags'] = students['tags'].apply(stem)

    cv = CountVectorizer(max_features=50, stop_words="english") 

    vectors = cv.fit_transform(students['tags']).toarray()
    vectors

    distance_matrix = cosine_similarity(vectors)

    branch_score = 0.25
    year_score = 0.1
    program_score = 0.1

    for i in  range(len(distance_matrix)):
        for j in range(i+1):

            if (students.iloc[i]["Branch"] == students.iloc[j]["Branch"]):
                distance_matrix[i][j] += branch_score
                distance_matrix[j][i] = distance_matrix[i][j]
            
            if (students.iloc[i]["Program"] == students.iloc[j]["Program"]):
                distance_matrix[i][j] += program_score
                distance_matrix[j][i] = distance_matrix[i][j]

            if (students.iloc[i]["Year"] == students.iloc[j]["Year"]):
                distance_matrix[i][j] += year_score
                distance_matrix[j][i] = distance_matrix[i][j]

    similar_students = sorted(list(enumerate(distance_matrix[np.where(students == f"{regno}")[0][0]])), reverse=True, key=lambda x:x[1])[1:11]

    top_similar_students = []

    for i in similar_students:
        top_similar_students.append(students.iloc[i[0]]["ID"])

    final_ratings = final_ratings[ratings["StudentID"].isin(top_similar_students)].reset_index()

    rating_sum = final_ratings.groupby("EventID").sum("Rating")["Rating"]
    rating_count = (final_ratings.groupby("EventID").count()["Rating"])

    avg_rating = pd.concat([rating_sum,  rating_count], axis=1)

    avg_rating["Average"] = avg_rating.iloc[:, :1] / avg_rating.iloc[:, 1:2]
    avg_rating = avg_rating.sort_values(by="Average", ascending=False).reset_index()
    avg_rating = avg_rating.iloc[:k+1, :]
    avg_rating = avg_rating[avg_rating["Average"] > 5]
    avg_rating
    
    recommended_events = list(avg_rating["EventID"])

    return recommended_events