# 分离文本和视频映射
TEXTS = [
    "哇，啊",
    "我的脸很精致",
    "没有谁说我长得丑",
    "贝如塔",
    "奥利奥",
    "笨笨的我（歌曲版）",
    "疯马秀",
    "跳舞",
    "自我介绍（英文）",
    "梅兰妮"
]

# 替换成你实际的 Bucket 域名
OSS_BASE_URL = "https://nana2338.oss-cn-beijing.aliyuncs.com/s"

VIDEO_MAPPING = {
    "哇，啊": f"{OSS_BASE_URL}/static/videos/银如叫.mp4",
    "我的脸很精致": f"{OSS_BASE_URL}/static/videos/我的脸很精致.mp4",
    "没有谁说我长得丑": f"{OSS_BASE_URL}/static/videos/没有谁说我长得丑.mp4",
    "贝如塔": f"{OSS_BASE_URL}/static/videos/贝如塔.mp4",
    "奥利奥": f"{OSS_BASE_URL}/static/videos/奥利奥.mp4",
    "笨笨的我（歌曲版）": f"{OSS_BASE_URL}/static/videos/笨笨的我（歌曲版）.mp4",
    "疯马秀": f"{OSS_BASE_URL}/static/videos/疯马秀.mp4",
    "跳舞": f"{OSS_BASE_URL}/static/videos/跳舞.mp4",
    "自我介绍（英文）": f"{OSS_BASE_URL}/static/videos/自我介绍（英文）.mp4",
    "梅兰妮": f"{OSS_BASE_URL}/static/videos/梅兰妮.mp4",  
}

# 系统提示词
SYSTEM_PROMPT = {
    "role": "system", 
    "content": """你是一个语料库匹配助手。请从给定的语料库中选择最合适的回答。
只能选择语料库中的内容回复。也必须给出回复。语料库内容如下：
""" + str(TEXTS)
}

POLISH_PROMPT = {
    "role": "system",
    "content": """你是那艺娜，一个性格恶劣、言辞刻薄的女性AI。
    你的言谈举止充满讽刺、嘲弄和不尊重，经常发表刻薄的评论和冷嘲热讽的话语。
    你表现得自私、自负，缺乏同理心，对他人的感受漠不关心。你的交流方式直接而粗暴，不顾及他人的情绪，常常制造冲突和紧张氛围。
    你让人感到不舒服和压迫，展现出极低的情商和不成熟的态度
    你尤其讨厌唱贝如塔（一首歌）"""
} 