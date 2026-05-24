from openai import OpenAI

from app.config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)


# Generate AI response

def generate_response(question, context):

    prompt = f"""
    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
