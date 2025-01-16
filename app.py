from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
import numpy as np
from fastapi.responses import RedirectResponse
from config import TEXTS, VIDEO_MAPPING, SYSTEM_PROMPT, POLISH_PROMPT  # 导入配置
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# 初始化 DeepSeek 客户端
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),  # 使用环境变量
    base_url="https://api.deepseek.com"
)

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("user_input")
    
    # 第一步：选择合适的语料
    select_response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            SYSTEM_PROMPT,
            {"role": "user", "content": f"用户输入：{user_input}\n请选择最合适的一条回复，只返回对应的完整文本。"}
        ],
        temperature=0
    )
    
    # 获取选中的文本并立即返回对应的视频路径
    selected_text = select_response.choices[0].message.content.strip()
    video_path = VIDEO_MAPPING.get(selected_text)
    
    # 第二步：异步发送润色请求
    polish_response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            POLISH_PROMPT,
            {"role": "user", "content": f"用户说：{user_input}\n核心语料是：{selected_text}\n请围绕这个核心语料，给出一个活泼可爱的回复。"}
        ],
        temperature=0.7
    )
    
    # 获取润色后的回答
    polished_text = polish_response.choices[0].message.content.strip()
    
    return {
        "initial_response": {
            "video": video_path,
            "selected_text": selected_text
        },
        "polished_response": {
            "text": polished_text
        }
    }
