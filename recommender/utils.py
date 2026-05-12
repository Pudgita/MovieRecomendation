import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from .models import Movie
from sklearn.preprocessing import MinMaxScaler

def get_recommendations(features_list, k=5):
    movies_queryset = Movie.objects.all()
    if not movies_queryset.exists():
        return []

    data = list(movies_queryset.values('id', 'year', 'rating', 'happy', 'action', 'weird'))
    df = pd.DataFrame(data)

    scaler = MinMaxScaler()
    feature_cols = ['year', 'rating', 'happy', 'action', 'weird']
    
    scaled_features = scaler.fit_transform(df[feature_cols])

    model = NearestNeighbors(n_neighbors=3, metric='euclidean')
    model.fit(scaled_features)


    user_query = np.array([features_list]).reshape(1, -1)
    user_query_scaled = scaler.transform(user_query)

    distances, indices = model.kneighbors(user_query_scaled)

    recommended_ids = df.iloc[indices[0]]['id'].tolist()
    
    return Movie.objects.filter(id__in=recommended_ids)