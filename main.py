from fastapi import FastAPI

from embedding import BGE3MEmbedding
from embedding_api_model import EmbeddingInput, EmbeddingData, EmbeddingOutput, EmbeddingUsage
from log import Logger

app = FastAPI()
embedding = BGE3MEmbedding('/Users/trent/dev/model/bge_m3', use_fp16=False)
log = Logger(filename='embedding-server.log')
logger = log.logger


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.post("/embeddings")
async def get_embedding(embedding_input: EmbeddingInput):
  logger.info(f"text input for embedding is  {embedding_input}")
  input = embedding_input.input
  if type(input) == str:
    return await handler_str_input(input)
  else:
    return await handler_list_input(input)


async def handler_list_input(input):
  out_usage = EmbeddingUsage()
  output = EmbeddingOutput()
  res = embedding.get_embeddings(input)
  index = 0
  for single in res:
    out_data = EmbeddingData()
    out_data.index = index
    for e in single:
      out_data.embedding.append(float(e))
    output.data.append(out_data)
    index += 1
  output.usage = out_usage
  return output


async def handler_str_input(input):
  token_count = len(input)
  output_embedding = embedding.get_embedding(input)
  out_data = EmbeddingData()
  out_usage = EmbeddingUsage()
  out_usage.prompt_tokens = token_count
  out_usage.total_tokens = token_count
  for e in output_embedding:
    out_data.embedding.append(float(e))
  output = EmbeddingOutput()
  output.data.append(out_data)
  output.usage = out_usage
  return output
