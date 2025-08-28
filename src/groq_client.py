# src/groq_client.py
from groq import Groq
from src.config import GROQ_API_KEY

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


def build_zero_shot_prompt(topic):
    """Zero-Shot: AI generates prompts without examples"""
    return f"""
You are a creative AI assistant. Generate 5 imaginative story prompts based on this topic: "{topic}".
Explain your reasoning step by step before listing the prompts.
"""


def build_one_shot_prompt(topic):
    """One-Shot: AI guided with a single example"""
    return f"""
You are a creative AI assistant. Generate 5 imaginative story prompts based on this topic: "{topic}".
Example:

Topic: Fantasy with dragons
Prompts:

1. A young dragon discovers its hidden powers while exploring ancient ruins.
2. A village must unite to stop a rogue dragon from destroying their home.


Now generate prompts for "{topic}".
"""





def build_multi_shot_prompt(topic):
    """Multi-Shot: AI guided with multiple examples"""
    return f"""
You are a creative AI assistant. Generate 5 imaginative story prompts based on this topic: "{topic}".
Examples:
1) Topic: Time travel adventure
   Prompts:
   1. A teenager accidentally travels to the past and must prevent a disaster.
   2. Two friends discover a time machine and explore historicals events.


2) Topic: Alien invasion
   Prompts:
   1. Humanity's first contact with aliens leads to an unexpected alliance.
   2. A city survives an alien attack by decoding their mysterious messages.

Now generate prompts for "{topic}".
"""


def get_ai_response(prompt, stream=False):
    """
    Call Groq LLM with prompt. Supports streaming if stream=True.
    Logs token usage for efficiency.
    """
    if stream:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None
        )
        response_text = ""
        for chunk in completion:
            # Use getattr safely
            delta = getattr(chunk.choices[0], "delta", None)
            if delta:
                content = getattr(delta, "content", "")
                if content:  # Only append if not None or empty
                    print(content, end="", flush=True)
                    response_text += content
        print()
        return response_text or ""
    else:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_completion_tokens=1024,
            top_p=1

        )
        tokens_used = getattr(response.usage, "total_tokens", None)
        if tokens_used is not None:
            print(f"Tokens used: {tokens_used}")
        # Return safe string


        message_content = getattr(response.choices[0].message, "content", "")
        return message_content or ""
