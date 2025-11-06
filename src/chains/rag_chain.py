from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama  # ⚙️ 최신 패키지 (langchain-ollama 설치 필요)

def build_rag_chain(state):
    # ✅ LangGraph state에서 vectorstore 객체 추출
    vectorstore = state["vectorstore"]

    # ✅ 로컬 LLM 사용 (무료)
    llm = ChatOllama(model="mistral")

    # ✅ 프롬프트를 완전 한글로 변환
    prompt = ChatPromptTemplate.from_template("""
    당신은 아래 문서를 기반으로 사용자의 질문에 대답하는 한국어 어시스턴트입니다.

    문서 내용:
    {context}

    질문:
    {question}

    위 문서를 참고하여, 질문에 대한 답변을 **한국어로만** 자연스럽게 작성하세요.
    """)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # ✅ LCEL 방식 체인 구성 (문자열 입력 전용)
    rag_chain = (
        {"context": lambda x: retriever.invoke(x), "question": lambda x: x}
        | prompt
        | llm
    )

    return {"rag_chain": rag_chain}
