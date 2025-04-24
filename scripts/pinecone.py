from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


model_name = "deepvk/USER-bge-m3"  # 1024 dimensional
model_kwargs = {"device": "cpu"}
encode_kwargs = {'normalize_embeddings': False}


embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)


file_path = r"C:\Users\andre\dio-1c-agent\parser\books\Архитектура и работа с данными.txt"

with open(file_path, encoding="utf-8") as file:
    text = file.read()


print(len(text))


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    length_function=len,
)

chunks = text_splitter.create_documents([text])

print(len(chunks))
print(chunks[400])
