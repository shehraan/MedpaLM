import google.generativeai as palm
palm.configure(api_key='Your-API-Key')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
question = input("Please enter a question you would like to ask MedPalm: ")

prompt = """
You are an expert at answering questions.

Answer the following question: """+question

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print("\nAnswer: "+completion.result)