## Credits: Dawnthedemon (Primary Developer), VGMoose
## Version: V1.1 (Snake)
## Changelog:
## 1. Migrated to python
## 2. Using Gpt4o mini

## todo:
## 1. install openai (pip install openai)
## 2. Link bot account
## 3. Administators
## 4. Logical Instruction Language Support



## code below:
# importing openai module into your openai environment
import openai

# assigning API KEY to initialize openai environment
openai.api_key = ''

prompt = "hello! how are you?"
model = "gpt-3.5-turbo"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
if input() == "test": print(generated_text) else print(":(")