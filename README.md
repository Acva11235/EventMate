# EventMate - Your Personalized Event Recommender 🤖

## Overview
Ever felt overwhelmed by the sheer number of events happening during college fests? Introducing EventMate, the ultimate event recommender for college students! EventMate solves the problem of sifting through hundreds of events to find the ones that interest you the most, especially during technical and cultural fests.


## ✨ Features

- Personalized recommendations unique to your interests.
- Hybrid recommender system combining Content-based, Collaborative Filtering, and Popularity-based recommendations.
- Customizable scores and values for every college based on their needs.

## 🧠 How it Works

EventMate uses a hybrid approach to recommend events:

1. **Content-based Recommender:** Finds similarities between events and student interests by text vectorization using bag of words of the column tags, then calculates cosine distances.
2. **Collaborative Filtering Recommender:** Calculates a specific score based on student's interests, year, branch, etc., by assigning different weights.
3. **Popularity-based Recommender:** Determines event growth rate based on the number of registrations in a given time period.

The final recommendations are a mix of all three types, ensuring a diverse and personalized event list for every user.

## ⚡Customizability 

All scores and values used in EventMate are customizable to suit the needs of every college. Adjust them to match your college's preferences and requirements.

## 🚀 Getting Started 

To start using EventMate, follow these simple steps:

1. Clone the repository: `git clone https://github.com/Acva11235/EventMate.git`
2. Install the necessary dependencies. `pip install -r requirements.txt`
3. Install stopwords and punkit for rake: `python -m nltk.downloader stopwords` and `python -m nltk.downloader punkt`
4. Customize the scores and values based on your college's needs. (Available in collaborative filtering and popularity methods)
5. Run the application and start discovering exciting events! `hybrid_recommender.py`

## 🤝 Support

For any issues or queries, please contact us at [achintya.varshneya@gmail.com](mailto:support@eventmate.com).

## 📄 Author 

Achintya Varshneya
