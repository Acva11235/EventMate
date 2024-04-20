from content_based_recommend import content_based_recommender
from collaborative_filtering_recommender import collaborative_filtering_recommder
from popularity_based_recommender import  popularity_based_recommender
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost',
                        user='root',
                        password='1234',
                        database='eventmate')

curr = conn.cursor()

regno = input("Enter the registration number: ").upper().strip()

recommendations = set()

#Content based recommendations
content_based_recommendations = content_based_recommender(regno, 10)

current = 0
while len(recommendations) !=4 and current < len(content_based_recommendations):
    recommendations.add(content_based_recommendations[current])
    current += 1

#Collaborative filtering recommendations
collaborative_filtering_recommendations = collaborative_filtering_recommder(regno, 10)

current = 0
while len(recommendations) !=8 and current < len(collaborative_filtering_recommendations):
    recommendations.add(collaborative_filtering_recommendations[current])
    current += 1

#Popularity based
popularity_recommendations = popularity_based_recommender(10)

current = 0
while len(recommendations) !=10 and current < len(popularity_recommendations):
    recommendations.add(popularity_recommendations[current])
    current += 1

print("Our recommendations for you: ")
for i in recommendations:
    query = f'Select Name, Club from event where EventID = "{i}"'
    curr.execute(query)  
    results = curr.fetchall()  
    print(f"{results[0][0]} by {results[0][1]}") 