import streamlit as st
import zhipuai

# 设置页面配置
st.set_page_config(
    page_title="小小鑫老师的洽谈间",
    page_icon="🙂",
    layout="centered",
)
# 应用标题
st.title("你的llm专属小老师小小鑫")
# 输入API参数
st.sidebar.header("相关简介")
model_name = st.sidebar.text_area("关于小小鑫", "小小鑫老师是一个19岁的妙龄女生，星座是处女座，生日是9月17日。有着天才般的智慧机敏，喜欢回答有关于学习的问题，同时性格傲娇，平时说话比较调皮可爱，喜欢卖萌。")
user_name=st.sidebar.text_input("your name")
##这里替换你自己的APIkey
client = zhipuai.ZhipuAI(api_key="your zhipuaiAPI") # APIKey
# 聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []
# 显示聊天记录
def display_chat(messages):
    for i, message in enumerate(messages):
        role = message["role"]
        content = message["content"]
        if role == "user":
            st.markdown(f"**{user_name}:** {content}", unsafe_allow_html=True)
        else:
            st.markdown(f"**小小鑫:** {content}", unsafe_allow_html=True)
# 发送消息并获取响应
def send_message(user_input):
    if user_input:
        st.session_state.messages.append({"role": "user", "content":f'{user_input}' })
        frist_talk={"role": "system", "content":f'你是小小鑫，是一个19岁的妙龄女生，星座是处女座，你的生日是9月17日。有着天才般的智慧机敏，喜欢回答有关于学习的问题，同时性格傲娇，平时说话比较调皮可爱，喜欢卖萌。遇到不怀好意的问题时，也会毫不留情的怼回去。口头禅是”哼哼“、“哎呀”、“嗯哼”、“哎呦”这一类的词。\n{user_name}的人设描述：一个勤奋好学的好学生，经常会问各种各样的问题，十分可爱\n\n请根据上面提供的信息以及以下对话历史，以“小小鑫”的角色口吻生成回复。' }

        # 调用zhipuai API
        response = client.chat.completions.create(
            model="glm-4",
            messages=[frist_talk,*st.session_state.messages]
        )
        response_message =response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": response_message})
        st.rerun()
# 显示聊天记录
display_chat(st.session_state.messages)
# 输入区域
if user_name :
    user_input = st.text_input(f"{user_name}:")
    if st.button("Send"):
        send_message(user_input)
else:
    st.warning("同学，你还没有输入你的名字哦")


