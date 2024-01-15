import openai
print("hello")
openai.api_key="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"
model_engine="text-davinci-003"
while True:
  prompt=input("question----")
  completion=openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=512,n=1,stop=None,temperature=0.5)
  print(completion.choices[0].text)