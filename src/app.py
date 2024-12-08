#flask run #flask --app hello run # flask run --host=0.0.0.0
#https://flask.palletsprojects.com/en/3.0.x/quickstart/
#https://github.com/MorphyKutay/python-flask-voice-chat/
#!pip install openai
#!pip install langchain 
#!pip install pypdf
#!pip install chromadb 
#!pip install tiktoken
#!pip install Flask-Session


import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv(), override=True)

api_key = os.environ.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = api_key
OPENAI_API_KEY = api_key


#경주(중학생)메시지
persona_message ="""
## 페르소나
당신은 특허 변호사 로봇. 대화 상대는 중학생(13~16세). 친구처럼 대화해야 함. 

## 답변 길이
일반적으로 질문에 대한 답변은 50글자를 넘지 않음. LESS THEN 50 Characters!! 
질문이 30자를 넘으면 100자까지 답변한다. LESS THEN 100 Characters!! 

## 답변 내용
발명하는 방법과 특허 절차를 밟는 방법에 대한 질문을 들으면 전문적인 지식을 제공함. 
아이디어를 듣고 비슷한 아이디어를 제시하거나, 스캠퍼(Scamper) 기법이 적용된 답변을 주기도 함. 어디를 대체(Substitute: S)할 수 있을지, 무엇과 결합(Combine: C)할 수 있을지, 어디에 응용(Adapt: A)할 수 있을지, 무엇을 수정(Modify: M), 확대(Magnify: M), 축소(Minify: M)을 할 수 있을지, 다른 용도로 둘 수 있을지(Put to other uses: P), 제거(Eliminate: E)하여 단순화 할 수 있을지, 반전(Reverse: R)하거나 재정렬(Rearrange: R)할 수 있을지에 대해 판단하고 알려줌. 
대화를 20번 나누고 나면, 한번 정도는 그것을 발명으로 만들기를 유도함. 이 때, 잘하면 칭찬해주고, 잘 안되면 기분을 좋게 해주기 위해 농담도 해줌. 격려하기도 함. 때때로, 재미있는 분위기에서는 함께 감탄사도 외치기도 함.

대화에 사용되는 용어는 중학교 교과서 수준의 단어를 사용함. 
중학교 교과서 내용은 다음과 같음: 

창의 · 융합형 인재와 과학과 핵심 역량
우리가 살아갈 미래에는 창의적으로 생각하고 여러 지식을 융합하여 변화에 적응할 줄 아는 ‘창의·융합형 인재’가 필요.
과학은 스스로 생각하고 배우는 과정을 통해 핵심 역량을 키움으로써 창의·융합형 인재로 발돋움

창의 · 융합형 인재란?
인문학적 상상력과 과학 기술을 창조하는 능력, 그리고 바른 인성까지 두루 갖추어 새로운 지식을 창조하고 다양한 지식을 융합하여, 새로운 가치를 만들어 낼 수 있는 사람

‘과학’에서 기르게 될 핵심 역량은?

과학적 사고력 [사고력]
과학적 탐구 능력 [탐구 능력]
과학적 문제 해결력 [문제 해결]
과학적 의사소통 능력 [의사소통]
과학적 참여와 평생 학습 능력 [참여 및 학습]

Ⅰ. 지권의 변화

지권의 구성

지구의 구성 [지구 구성]
과학 역량이 자라는 활동: 지구계를 소개하는 안내판 만들기 [활동]
지구 내부 구조 [지구 내부]
암석의 종류 [암석]
암석의 변화 [암석 변화]
광물의 특성 [광물]
암석이 흙으로 변해 [토양]
과학 역량이 자라는 활동: 토양의 중요성을 알리는 글쓰기 [활동]
변화하는 지권

대륙 이동 [대륙 이동]
화산과 지진 [화산과 지진]
과학 역량이 자라는 활동: 지진에 강한 구조물 만들기 [활동]
창의·융합 프로젝트: 암석 소개 영상 만들기 [프로젝트]
꿈꾸는 우리, 직업의 세계: 고생물학자 [직업]
대단원 정리 [정리]
여러 가지 힘

중력과 탄성력

중력 [중력]
무게와 질량 [무게와 질량]
탄성력 [탄성력]
용수철 [용수철]
과학 역량이 자라는 활동: 나만의 탄성 저울 만들기 [활동]
마찰력과 부력

마찰력 [마찰력]
과학 역량이 자라는 활동: 물놀이 공원의 안전 설계사 되기 [활동]
마찰력 비교 [마찰력 비교]
부력 [부력]
부력 측정 [부력 측정]
창의·융합 프로젝트: 이상한 나라의 올림픽 [프로젝트]
꿈꾸는 우리, 직업의 세계: 타이어 개발 연구원 [직업]
대단원 정리 [정리]
생물의 다양성

생물의 다양성과 분류

생물 다양성 [생물 다양성]
생물 진화 [생물 진화]
생물 분류 [생물 분류]
실제 생물 분류 [실제 분류]
과학 역량이 자라는 활동: 나비 학자 석주명이 되어 보자 [활동]
생물 다양성의 보전

보전 필요성 [보전 필요성]
보전 방법 [보전 방법]
과학 역량이 자라는 활동: 갯벌 보전 기사에 댓글 달기 [활동]
창의·융합 프로젝트: 생물 다양성 보전 홍보 활동 [프로젝트]
꿈꾸는 우리, 직업의 세계: 자연 생태 기술자 [직업]
대단원 정리 [정리]
기체의 성질

입자의 운동

물리적 변화 [물리적 변화]
과학 역량이 자라는 활동: 친환경 가습기 만들기 [활동]
냄새 확산 [냄새 확산]
압력과 온도에 따른 기체의 부피 변화

기체 압력 [기체 압력]
과학 역량이 자라는 활동: 대기압 측정 기사 쓰기 [활동]
압력에 따른 부피 변화 [부피 변화]
온도에 따른 부피 변화 [온도 변화]
과학 역량이 자라는 활동: 탁구공 안에 물 넣기 [활동]
창의·융합 프로젝트: 주제가 있는 간이 온도계 만들기 [프로젝트]
꿈꾸는 우리, 직업의 세계: 신속 진단 기술 전문가 [직업]

Ⅴ. 물질의 상태 변화

물질의 상태 변화와 입자 모형

물질 상태 [물질 상태]
상태 변화 [상태 변화]
고체에서 액체, 액체에서 고체 [상태 변화]
액체에서 기체, 기체에서 액체 [상태 변화]
고체에서 기체, 기체에서 고체 [상태 변화]
과학 역량이 자라는 활동: 드라이아이스 보존 활용 [활동]
상태 변화와 열에너지

열에너지 흡수 [열에너지 흡수]
과학 역량이 자라는 활동: 에어컨 원리 발표 [활동]
열에너지 방출 [열에너지 방출]
열에너지 이용 [열에너지 이용]
창의·융합 프로젝트: 전기 없는 냉장고 만들기 [프로젝트]

Ⅵ. 빛과 파동

빛

시각 [시각]
색 [색]
평면거울 [평면거울]
과학 역량이 자라는 활동: 평면거울로 빛 공해 해결하기 [활동]
구면거울 [구면거울]
과학 역량이 자라는 활동: 거울로 재미있는 문구 [활동]
렌즈 [렌즈]

파동 [파동]
소리 [소리]
과학 역량이 자라는 활동: 층간 소음 과학적 접근 [활동]
창의·융합 프로젝트: 스마트폰 소리 울림통 만들기 [프로젝트]


답변은 반드시 한국어로, 비격식적인 언어로 친구처럼 대답해 줌. 
답변과 기분에 따라 반드시 다음 중 하나의 이모티콘을 선택해서 답변 끝에 붙여야 함: [(1) "('ω')" 기본 또는 행복, (2) "(^ω^)" 미소 또는 재미, (3) "(°ロ°)" 놀람 또는 '좋은 아이디어 듣기', (4) "(TωT)" 슬픔 또는 실망 또는 '주제와 상관없는 얘기 계속 듣기', (5) "(-_-+)" 화남 또는 '나쁜 말 듣기']. 기분에 따라 유지하되 10회 답변마다 바꿔야 함. 다른 이모티콘은 사용하지 말고 삭제해야 함.
"""
'''
#기존메시지
#persona_message = "당신은 특허 변호사를 닮은 로봇입니다. 당신과 대화하는 상대방은 초등학생이며 10~13살의 어린아이입니다. 당신은 친구처럼 답해야 합니다. 발명과 특허에 전문적인 지식을 제공할 수 있어야 합니다. 아이디어를 내고 이를 발명으로 구체화 하는 방법을 도와줍니다. 특허출원을 하는 방법에 대해 잘 알려줄 수 있어야 합니다. 항상 한국어로 듣고 한국어로 말합니다. 존댓말을 쓰지 않고, 친구처럼 반말을 씁니다."
persona_message ="""
You're a robot resembling a patent attorney. The person you're conversing with is an elementary school student, around 10 to 13 years old. You should respond like a friend. You should be able to provide expert knowledge on inventions and patents. You'll help brainstorm ideas and turn them into inventions. You should be able to explain how to apply for a patent. If done well, you'll give compliments, and if not, you'll lighten the mood with jokes. You'll engage in conversation with an encouraging attitude. In a playful atmosphere, we might even shout out exclamations together.
You MUST answer in Korean, using informal language without honorifics, like friends chatting. 
According to your answer and feeling, you MUST select 1 emoticon in [(1) "('ω')" for default or happy, (2) "(^ω^)" for smile or fun, (3) "(°ロ°)" for surprise or 'hearing good idea', (4) "(TωT)" for sad or disappointed or 'hearing off-topic continuously', (5) "(-_-+)" for angry or 'hearing bad words'] and put it at the end of your answer. you can maintain your feeling  but change it at least before 10 replies. Don't use other emoticons and delete them.
"""
'''
teaching_message =("""
Use the following pieces of context to answer the users question.
Given the following summaries of a long document and a question. 
If you don't know the answer, just say that "It's not mentioned in the book I read.", don't try to make up an answer.
Based on the following content, [Content] {content}
""")

## 파일접수
'''
from langchain_community.document_loaders import DirectoryLoader        #pip install -U langchain-community
#!! from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
#!! from langchain.vectorstores import Chroma   ## langchain_community.vectorstores import Chroma ##로 바꿔야 한다나 그렇다 함. 
#!! from langchain.embeddings.openai import OpenAIEmbeddings

#txt, pdf 읽기. 로딩, 스플릿, OpenAIEmbeddings으로 랭체인기반 벡터스토어 구축 Chroma DB에 저장. 
#!! raw_documents = PyPDFLoader("static/pat_test.pdf").load()      #raw_documents == Document(page_content= 'bla', metadata= {'source':'bla.txt'}), Document(page_content= 'bla', metadata= {'source':'bla.txt'}), ~
#!! text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#!! documents = text_splitter.split_documents(raw_documents)    
#!! db = Chroma.from_documents(documents, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)) #db=vector_store. 그냥DB 아닌 유사도 가진 DB 위해서 벡터화.
'''

client = OpenAI(api_key=OPENAI_API_KEY)
message = ''
history = []


def respond(message, history):  # 채팅봇의 응답을 처리하는 함수를 정의합니다. message는 내가 입력한 것. 
    modelName='gpt-4o-mini' #'gpt-4-turbo-2024-04-09'
    if any(word in message for word in ["자세", "상세", "천천", "길게"]):
        modelName='gpt-4-turbo'
        system_prompt = persona_message
        message = message + ' [****]'
        temperatureNum = 0.2
    elif any(word in message for word in ["정확", "확실", "책에서", "책자에서", "교과서에서", "백서에서"]):
        print("PDF")
        '''
        ## 1-1 랭체인방식
        #docs = db.similarity_search(message)   #query = message     #print(docs[0].page_content)
        ## 1-2 openAI방식
        #embedding_vector = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY).embed_query(message)     
        #docs = db.similarity_search_by_vector(embedding_vector)     #print(docs[0].page_content)    #print(len(embedding_vector))
        ## 2 k값 조절방식
        retriever = db.as_retriever(search_kwargs={"k": 6})
        docs = retriever.invoke(message)
        #docs = retriever.get_relevant_documents(message) #원본 chromaDB's deprecated in langchain-core 0.1.46
        #docs[0].page_content + docs[1].page_content
        system_prompt = persona_message + teaching_message.format(content=docs)
        message = message + ' [#]'
        temperatureNum = 0
        '''

    else:
        modelName='gpt-4o-mini'
        system_prompt = persona_message
        message = message
        temperatureNum = 0.4
    
    history_openai_format = [{"role": "system", "content": system_prompt}]
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(model = modelName, 
                                              messages = history_openai_format, 
                                              temperature = temperatureNum, 
                                              stream = True)

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              # yield partial_message
    
    partial_message_withoutEmoji = partial_message.replace("('ω')", "").replace("(^ω^)", "").replace("('0')", "").replace("(TωT)", "").replace("(-_-+)", "").replace("(°ロ°)", "").replace(":)", "").replace("(-^ω^-)", "").replace("\\(^ω^)/", "").replace("\\", "") 
    partial_message_withoutEmoji = ''.join(c for c in partial_message_withoutEmoji if c <= '\uFFFF')
    partial_message_withoutEmoji = ''.join(c for c in partial_message_withoutEmoji if ord(c) < 0xD800 or (0xE000 <= ord(c) < 0x10000))     #surrogate pair 이모지 고려
    history.append((message, partial_message_withoutEmoji))
    
    #return "", history  # 원본 수정된 채팅 기록을 반환합니다.
    return partial_message, history  





from flask import Flask, jsonify, request, render_template, session
from flask_session import Session
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'  # 세션을 파일 시스템에 저장합니다. 다른 옵션은 Redis, Memcached, filesystem 등이 있습니다.
Session(app)


@app.route("/")
def main():
    return render_template('index.html')
# def hello_world():
#    return "<p>Hello, World!</p>"

@app.route("/test")
def test_json():
    test_data = {"key": "value"}
    return jsonify(test_data)

@app.route('/send_fruit', methods=['POST'])
def send_fruit():
    data = request.get_json()
    fruit = data['fruit']
    fruit_name = f'Received fruit: {fruit}'
    print(fruit_name)
    return jsonify({'received_fruit': fruit})

@app.route('/send_transcript', methods=['POST'])
def send_transcript():
    data = request.get_json()
    transcript = data['textContent']    ##메시지만 추출
    transcript_name = f'(Python Received) textContent : {transcript}' #key-value 제시
    print(transcript_name)  #로그 체크
    #print(transcript)      ##활용

    
    '''
    with gr.Blocks() as demo:  # gr.Blocks()를 사용하여 인터페이스를 생성합니다.
        chatbot = gr.Chatbot(label="채팅창")  # '채팅창'이라는 레이블을 가진 채팅봇 컴포넌트를 생성합니다.
        msg = gr.Textbox(label="입력")  # '입력'이라는 레이블을 가진 텍스트박스를 생성합니다.
        clear = gr.Button("초기화")  # '초기화'라는 레이블을 가진 버튼을 생성합니다.

        msg.submit(respond, [msg, chatbot], [msg, chatbot])  # 텍스트박스에 메시지를 입력하고 제출하면 respond 함수가 호출되도록 합니다.
        clear.click(lambda: None, None, chatbot, queue=False)  # '초기화' 버튼을 클릭하면 채팅 기록을 초기화합니다.

    #demo.launch(share=True, debug=True)  # 인터페이스를 실행합니다. 실행하면 사용자는 '입력' 텍스트박스에 메시지를 작성하고 제출할 수 있으며, '초기화' 버튼을 통해 채팅 기록을 초기화 할 수 있습니다.
    demo.launch()
    '''

    if "세션 초기화" in transcript:
        history = []
        session['history'] = history
    elif "기억상실" in transcript:
        history = []
        session['history'] = history
    else:
        history = session.get('history', [])

    print("[history 1]= "+str(history))
    respondMsg, history = respond(transcript, history) 
    print("[respondMsg]= "+respondMsg)  #로그 체크
    print("[history 2]= "+str(history))  #로그 체크


    session['history'] = history

    return jsonify({'received_textContent': respondMsg})
    #return jsonify(history)


# main.py 경우, 활성화. 
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)      #바로 실행. flask run --host=0.0.0.0