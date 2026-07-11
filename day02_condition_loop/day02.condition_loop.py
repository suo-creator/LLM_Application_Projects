# Day2综合Demo：带判断逻辑的简易问答机器人
question = input("请输入你的问题：")
# 关键词判断
if "天气" in question:
    reply = "今日晴天，气温适宜。"
elif "时间" in question:
    reply = "当前系统时间可自行查看电脑右下角。"
elif "大模型" in question or "RAG" in question:
    reply = "RAG是检索增强生成，可以让AI读取私有文档回答问题。"
else:
    reply = "暂时无法理解你的问题，请更换提问方式。"

print("AI回复：", reply)

# 循环多次问答，输入quit结束
while True:
    user_in = input("\n继续提问，输入quit退出：")
    if user_in == "quit":
        print("对话结束")
        break