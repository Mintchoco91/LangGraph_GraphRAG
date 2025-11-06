1. conda create -n graphrag python=3.10
2. conda activate langgraph_graphrag
3. pip install -r requirements.txt
4. ollama pull mistral
5. ollama serve > /dev/null 2>&1 &
6. ps aux | grep ollama # 서비스 확인
7. nohup ollama run mistral > /dev/null 2>&1 &