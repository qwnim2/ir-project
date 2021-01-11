from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-distilroberta-base-v1')

# Single list of sentences
sentences = ['我糙你媽',
             '我想跟你作愛',
             '你媽媽沒屁眼',
             '你兒子沒屁眼',
             '我想買一堆房子',
             '你腦袋破洞',
             '你腦袋進水了嗎',
             '這幾個房子我好想要']

#Compute embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

#Compute cosine-similarities for each sentence with each other sentence
cosine_scores = util.pytorch_cos_sim(embeddings, embeddings)

#Find the pairs with the highest cosine similarity scores
pairs = []
for i in range(len(cosine_scores)-1):
    for j in range(i+1, len(cosine_scores)):
        pairs.append({'index': [i, j], 'score': cosine_scores[i][j]})

#Sort scores in decreasing order
pairs = sorted(pairs, key=lambda x: x['score'], reverse=True)

for pair in pairs[0:10]:
    i, j = pair['index']
    print("{} \t\t {} \t\t Score: {:.4f}".format(sentences[i], sentences[j], pair['score']))