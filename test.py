from openai import OpenAI # 用于进行 OpenAI API 请求
import config

# 设置 OpenAI API 凭据
openai_client = OpenAI(
    api_key=config.OPENAI_API_KEY
)

num_stories = 10
prompts = ["I was walking down the street and"] * num_stories

# 批处理完成请求，每次请求生成 10 个故事
response = openai_client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompts,
    max_tokens=20,
)

# 通过索引将完成结果匹配到提示
stories = [""] * len(prompts)
for choice in response.choices:
    stories[choice.index] = prompts[choice.index] + choice.text.strip()

# 打印生成的故事
for story in stories:
    print(story)
