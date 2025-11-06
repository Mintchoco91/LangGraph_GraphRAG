import os
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(state):
    rel_path = state["path"]

    # 프로젝트 루트 경로 계산
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    abs_path = os.path.join(project_root, rel_path)

    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"❌ PDF 파일을 찾을 수 없습니다: {abs_path}")
    else:
        print(f"✅ PDF 파일을 찾았습니다: {abs_path}")

    # ✅ PyPDFLoader는 List[Document]를 반환함
    loader = PyPDFLoader(abs_path)
    docs = loader.load()

    # ✅ LangGraph의 다음 노드로 그대로 넘기기
    return {"docs": docs}
