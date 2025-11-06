# LangGraph 프레임워크를 활용한 GraphRAG 파이프라인 구성 Sample 

### 🧩 소개 : LangGraph를 활용하여 RAG 파이프라인을 실행 그래프 형태로 구성하고 추론을 수행함. (Knowledge Graph 기반 GraphRAG은 아님)

### 🧩 RAG Pipeline Configuration


- **Serving**: Ollama  
- **Model**: Mistral (via Ollama runtime)  
- **Embedding Model**: all-MiniLM-L6-v2 (SentenceTransformers)
- **Vector Store**: FAISS  
- **Framework**: LangGraph + LangChain  
- **Pipeline Type**: Execution Graph-based RAG

### 🧩 Install
1. conda create -n graphrag python=3.10
2. conda activate langgraph_graphrag
3. pip install -r requirements.txt
4. ollama pull mistral
5. ollama serve > /dev/null 2>&1 &
6. ps aux | grep ollama # 서비스 확인
7. nohup ollama run mistral > /dev/null 2>&1 &


<img width="3248" height="1048" alt="image" src="https://github.com/user-attachments/assets/1f404b76-aeb3-4478-8479-24ecae5d0c74" />
