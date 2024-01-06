import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "write a resignation letter"
    },
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)


'''
{
  "id": "chatcmpl-7xBOxaCixkIAWT2oEbyBsRmairpFV",
  "object": "chat.completion",
  "created": 1694339535,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "[Your Name]\n[Your Address]\n[City, State, ZIP Code]\n[Email Address]\n[Phone Number]\n[Date]\n\n[Recipient's Name]\n[Recipient's Position]\n[Company/Organization Name]\n[Company/Organization Address]\n[City, State, ZIP Code]\n\nDear [Recipient's Name],\n\nI am writing to formally resign from my position at [Company/Organization Name], effective [last working day, typically two weeks from the date of the letter].\n\nWorking with [Company/Organization Name] has been a valuable experience for me, and I am grateful for the opportunities and growth I have achieved during my time here. However, after careful consideration and evaluation, I have decided to pursue a new opportunity that aligns better with my long-term career goals and personal development.\n\nI want to express my sincere gratitude to you and the entire team for your support and guidance throughout my tenure. I have learned a great deal from working alongside talented colleagues like you, and I will miss being a part of this dynamic team.\n\nIn order to ensure a smooth transition, I am willing to assist in any way I can during the interim period. Please let me know how I can be of help and if there are specific tasks or projects that require completion before my departure.\n\nMoreover,"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 256,
    "total_tokens": 271
  }
}
'''