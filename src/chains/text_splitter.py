from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_docs(state):
    # ✅ PDF 로더에서 넘어온 Document 리스트
    docs = state["docs"]

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    # ✅ 다음 노드로 넘길 데이터
    return {"chunks": chunks}
