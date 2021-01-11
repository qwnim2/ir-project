import os
import pickle
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

# Two lists of sentences
# sentences1 = ['The cat sits outside',
#              'A man is playing guitar',
#              'The new movie is awesome']

# sentences2 = ['The dog plays in the garden',
#               'A woman watches TV',
#               'The new movie is so great']

lyrics_folder = './lyrics_processed'
song_dict = {}
for song in os.listdir(lyrics_folder):
     with open(os.path.join(lyrics_folder,song), 'r') as file:
          file = file.read()
          embeddings = model.encode(file, convert_to_tensor=True)
          song_dict[song] = embeddings

with open('./embedding_songs.pk', 'wb+') as f:
     pickle.dump(song_dict, f)
# #Compute embedding for both lists
# embeddings2 = model.encode(sentences2, convert_to_tensor=True)

# with open('./a.pk', 'wb+') as f:
#      pickle.dump(embeddings1, f)
# with open('./b.pk', 'wb+') as f:
#      pickle.dump(embeddings2, f)

# #Compute cosine-similarits
# cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

# #Output the pairs with their score
# for i in range(len(sentences1)):
#     print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))