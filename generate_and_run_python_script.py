import openai
import subprocess
import os
import sys
# OpenAI APIキー
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("prompt.txt", "r") as f:
    pre_prompt = f.read()

def get_chat_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    #print(response.choices[0]["message"]["content"].strip())
    return response.choices[0]["message"]["content"].strip()

def generate_python_script(res):
    python_code = res
    with open("generated_script.py", "w") as f:
        f.write(python_code)

def run_python_script():
    result = subprocess.run(["python3", "generated_script.py"], capture_output=True)

def main(prompt):
    #print(prompt)
    res = get_chat_response(prompt)
    generate_python_script(res)
    run_python_script()

if __name__ == "__main__":
    #prompt = pre_prompt + sys.argv[1]
    prompt = pre_prompt + input("")
    #print(prompt)
    main(prompt)
