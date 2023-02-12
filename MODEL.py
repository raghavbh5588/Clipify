import cohere
co = cohere.Client('CP3qAhd01F0x9Y01BElLse0AgQ9yY3ISj2nW4CH0') # This is your trial API key
from cohere.classify import Example




examples = [
    
]

inputs = [
    
]

response = co.classify(
    model = 'large',
    input = inputs,
    examples = examples
  )

print(response.classifications)