from openai import OpenAI


def get_ai_summary(client: OpenAI, text: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that provides a summary of text provided to you.",
            },
            {"role": "user", "content": text},
        ],
    )

    return response.choices[0].message.content or "No summary generated"
