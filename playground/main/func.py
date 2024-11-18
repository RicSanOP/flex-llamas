import os
from openai import OpenAI

def get_openai_completion(sys_prompt, user_prompt):
    """
    Get a completion from OpenAI's chat model.
    
    Args:
        sys_prompt (str): The system prompt to set the context
        user_prompt (str): The user's input prompt
        
    Returns:
        str: The completion response text
    
    Requires:
        OPENAI_API_KEY environment variable to be set with a valid OpenAI API key
    """
    # Initialize the client with the API key from environment variable
    client = OpenAI(api_key="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")
    
    # Create a chat completion request
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.7,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    
    # Return the completion text
    return response.choices[0].message.content
