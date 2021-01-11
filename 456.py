import pickle
import operator
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

with open('./embedding_songs.pk', 'rb') as f:
    song_dict = pickle.load(f)

query = input("Enter the query: ")
query = model.encode(query, convert_to_tensor=True)
#Compute cosine-similarits
cosine_scores = {}
for song in song_dict.keys():
    cosine_scores[song] = util.pytorch_cos_sim(song_dict[song],\
                                                 query)
print(max(cosine_scores.items(), key=operator.itemgetter(1))[0])
#Output the pairs with their score
# for i in range(len(sentences1)):
#     print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))