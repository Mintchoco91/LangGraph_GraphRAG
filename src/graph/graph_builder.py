from typing import TypedDict
from langgraph.graph import StateGraph
from chains.pdf_loader import load_pdf
from chains.text_splitter import split_docs
from chains.embedding import get_embeddings
from chains.vector_store import create_vectorstore
from chains.rag_chain import build_rag_chain

# ✅ 1️⃣ 그래프 상태 정의
class GraphState(TypedDict):
    path: str
    docs: list
    chunks: list
    embeddings: object
    vectorstore: object
    rag_chain: object

# ✅ 2️⃣ 그래프 구성
def build_langgraph():
    graph = StateGraph(GraphState)  # state_schema 필수 인자 추가

    # 노드 등록
    graph.add_node("load_pdf", load_pdf)
    graph.add_node("split_docs", split_docs)
    graph.add_node("embed", get_embeddings)
    graph.add_node("vectorstore", create_vectorstore)
    graph.add_node("rag", build_rag_chain)

    # 엣지 연결
    graph.add_edge("load_pdf", "split_docs")
    graph.add_edge("split_docs", "embed")
    graph.add_edge("embed", "vectorstore")
    graph.add_edge("vectorstore", "rag")

    graph.set_entry_point("load_pdf")
    graph.set_finish_point("rag")

    return graph
