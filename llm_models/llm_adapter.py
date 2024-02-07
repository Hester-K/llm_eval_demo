import openai
from openai import OpenAI
import time
from func_timeout import func_set_timeout


class LLMAdaptor:
    def get_response(self, prompt_text) -> str:
        pass

class ChatGPT35Adaptor(LLMAdaptor):
    def __init__(self) -> None:
        super().__init__()
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key="",
            base_url=""
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



# myChat = ChatGPT35Adaptor()
# prompt = "Hello who are you"
# response = myChat.get_response(prompt)
# print(response)
