import networkx as nx
import matplotlib.pyplot as plt
from graph.graph_builder import build_langgraph
#from dotenv import load_dotenv
#load_dotenv()

def visualize_graph(graph):
    G = nx.DiGraph()
    
    # 노드 추가
    for node in graph.nodes:
        G.add_node(node)
    
    # ✅ 엣지 추가 (튜플 구조)
    for edge in graph.edges:
        if isinstance(edge, tuple) and len(edge) >= 2:
            G.add_edge(edge[0], edge[1])
    
    # 시각화
    plt.figure(figsize=(10,6))
    nx.draw_networkx(
        G,
        with_labels=True,
        node_color='lightblue',
        font_size=10,
        arrows=True,
        edgecolors='gray'
    )
    plt.title("LangGraph RAG Pipeline", fontsize=14)
    plt.tight_layout()
    plt.savefig("langgraph_structure.png")
    print("✅ 시각화 완료: langgraph_structure.png")

def main():
    graph = build_langgraph()
    visualize_graph(graph)

    app = graph.compile()
    rag_chain_state = app.invoke({"path": "data/sample.pdf"})
    rag_chain = rag_chain_state["rag_chain"]   # ✅ 실제 체인 객체 추출

    question = "딸기, 바나나, 파인애플, 사과중 이 문서에 안나온 과일은 뭐야?"
    answer = rag_chain.invoke(question)


    print("=== 질문 ===")
    print(question)

    print("=== 결과 ===")
    print(answer.content)

if __name__ == "__main__":
    main()