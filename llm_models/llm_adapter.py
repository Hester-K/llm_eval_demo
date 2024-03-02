import openai
from openai import OpenAI
import time
from func_timeout import func_set_timeout
import google.generativeai as genai
import dashscope
import configparser

class LLMAdaptor:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read('model_config.ini')

    def get_response(self, prompt_text) -> str:
        pass

class ChatGPT35Adaptor(LLMAdaptor):
    def __init__(self) -> None:
        super().__init__()
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            # api_key="sk-4JNSmRrN990CJuayLzWp4AlJQmGhGhk9rBE6Pv1It8Ivde8f",
            # base_url="https://api.chatanywhere.tech/v1"
            api_key=self.config.get('GPT', 'API_KEY'),
            base_url=self.config.get('GPT', 'BASE_URL')
        )

    @func_set_timeout(10)
    def response(self, prompt):
        time.sleep(0.2)
        messages = [
            {"role": "user", "content": prompt},
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=1,
        )

        # print(response)
        return response.choices[0].message.content

    def get_response(self, prompt) -> str:
        max_retries = 5
        response = None
        for retry_count in range(0, max_retries):
            try:
                response = self.response(prompt)
                if response != None:
                    break
            except:
                retry_count += 1
                print(f"time out, retry_count = {retry_count}")
                if retry_count == max_retries:
                    response = "unknown"
        return response

class GeminiAdaptor(LLMAdaptor):
    def __init__(self) -> None:
        super().__init__()
        # genai.configure(api_key='AIzaSyA4ARSS4eyB38lsv2YEfgpKlR_uEJj-PNw')
        genai.configure(api_key=self.config.get('Gemini', 'API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro')

    def get_response(self, prompt_text) -> str:
        response = self.model.generate_content(prompt_text)
        return response.text

class QWenAdaptor(LLMAdaptor):
    def __init__(self) -> None:
        super().__init__()        
        # self.api_key = 'sk-20b6919235e54f529212769394e98ca4'
        self.api_key=self.config.get('Qwen', 'API_KEY')
        print(self.api_key)
        dashscope.api_key = self.api_key
        self.model = dashscope.Generation.Models.qwen_max

    def get_response(self, prompt_text) -> str:
        response = dashscope.Generation.call(
            model = self.model,
            prompt = prompt_text
        )
        return response.output.text

# myChat = ChatGPT35Adaptor()
# prompt = "你是谁"
# response = myChat.get_response(prompt)
# print(response)
