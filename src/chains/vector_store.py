from langchain_community.vectorstores import FAISS

def create_vectorstore(state):
    # ✅ LangGraph의 state에서 데이터 꺼내기
    chunks = state["chunks"]
    embeddings = state["embeddings"]

    # ✅ 문서 + 임베딩으로 벡터 스토어 생성
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # ✅ 다음 노드로 넘길 데이터
    return {"vectorstore": vectorstore}