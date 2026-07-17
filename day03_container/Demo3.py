# 用列表+字典存储多轮完整对话记录
dialog_history = []
print("===带对话记忆简易AI助手===")
while True:
    user_text = input("请提问，输入exit结束对话：")
    if user_text == "exit":
        break
    # 简单关键词回复逻辑
    if "RAG" in user_text:
        ans = "RAG可以让大模型调用私有文档资料，减少幻觉。"
    elif "Embedding" in user_text:
        ans = "嵌入就是把文字转成向量数字，用来做相似度检索。"
    else:
        ans = "暂时无法解答该问题"
    # 单轮对话打包成字典存入列表
    one_round = {
        "question": user_text,
        "answer": ans
    }
    dialog_history.append(one_round)
    print("AI：", ans)
# 退出后打印全部历史对话
print("\n====全部对话记录====")
for idx, item in enumerate(dialog_history, 1):
    print(f"第{idx}轮 用户：{item['question']}")
    print(f"第{idx}轮 AI：{item['answer']}\n")