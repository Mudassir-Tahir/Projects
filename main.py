from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

# openai.api_key = "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"

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
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

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://mudassirtahirmt:f47B26UNL_gJ%3An_@chatgpt.ta9jbmf.mongodb.net/ChatGPTClone"
mongo = PyMongo(app)

@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats = myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:    
            data = {"question": question, "anwser": f"{chat['answer']}" }
            return jsonify(data)
        else:
           response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                prompt=question,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
        print(response)
        data = {"question": question, "answer": response["choices"][0]["text"]}
        mongo.db.chats.insert_one({"question": question, "answer": response["choices"][0]["text"]})
        return jsonify(data)
    data = {"result": "It seems like you entered a random or incomplete string of characters. How can I assist you today? If you have any questions or need information, please feel free to ask, and I'll do my best to help." }

    return jsonify(data)



app.run(debug=True)