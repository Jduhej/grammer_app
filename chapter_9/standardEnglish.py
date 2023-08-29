import openai

openai.api_key = str(open("token.txt").read())


# Creating a class
class StandardEnglish():
    def __init__(self, text_to_convert):
        self.text_to_convert = text_to_convert

    def convertStandardEnglish(self):

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":"user",
                "content":f"{self.text_to_convert}"
            }],
            temperature=0,
            max_tokens=256
        )

        result = {
            "id":response.id,
            "created":response.created,
            "model":response.model,
            "completion_tokens":response.usage.completion_tokens,
            "prompt_tokens":response.usage.prompt_tokens,
            "total_tokens":response.usage.total_tokens,
            "output":response.messages,
            "status":response.choices[0].finish_reason,
        }

        return result.messages