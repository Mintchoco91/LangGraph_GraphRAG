from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings(state):
    chunks = state["chunks"]
    model_name = "sentence-transformers/all-MiniLM-L6-v2"  # 무료 모델
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return {"embeddings": embeddings, "chunks": chunks}



''' 
from langchain_openai import OpenAIEmbeddings

#이건 유료버전
def get_embeddings(state):
    # ✅ 이전 단계의 chunks를 받음
    chunks = state["chunks"]

    embeddings = OpenAIEmbeddings()
    # embedding 객체만 넘기면 다음 노드에서 vectorstore에 연결 가능
    return {"embeddings": embeddings, "chunks": chunks}
'''