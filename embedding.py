from FlagEmbedding import BGEM3FlagModel


class BGE3MEmbedding:
    def __init__(self, model_path: str, use_fp16: bool = False):
        self.model = BGEM3FlagModel(model_path, use_fp16=use_fp16)

    def get_embeddings(self, sentences: []):
        return self.model.encode(sentences)['dense_vecs']

    def get_embedding(self, sentence: str):
        return self.model.encode([sentence])['dense_vecs'][0]






