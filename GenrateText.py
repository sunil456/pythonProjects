"""
Text generation involves generating text using machine learning techniques. The purpose of text
generation is to automatically generate text that is indistinguishable from a text written by a human.
"""

#What is GPT-2 Model?

"""
GPT-2 stands for Generative Pre-trained Transformer 2.
It is an open-source Natural Language Processing model created by OpenAI.
It can generate paragraphs of text with state of the art performance on many language benchmarks.
It is also used for machine translation, question answering, and text summarization.
"""

from transformers import pipeline
model = pipeline("text-generation", model="gpt2")

#Here’s how you can generate text using Python by using the GPT-2 model:
sentence = model("Hi, My name is Sunil Sharma, I am here",
                 do_sample=True, top_k=50,
                 temperature=0.9, max_length=100,
                 num_return_sentance=2)

# print(sentence)
for i in sentence:
    print(i["generated_text"])