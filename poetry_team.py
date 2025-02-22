from groq import Groq
from dotenv import load_dotenv
import pronouncing
import gradio as gr
import os

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---- Core Poetry Functions ---- #
def brainstorm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{
            "role": "user",
            "content": f"Generate 3-5 poem themes about: {prompt}\nFormat: - Themes: [...]"
        }],
        temperature=0.7
    )
    return response.choices[0].message.content

def write_poem(themes: str) -> str:
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{
            "role": "user",
            "content": f"Write a poem using:\n{themes}\n- 3 stanzas with rhyme scheme\n- Include metaphors"
        }],
        temperature=0.8
    )
    return response.choices[0].message.content

def edit_poem(poem: str) -> str:
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{
            "role": "user",
            "content": f"Improve this poem:\n{poem}\n- Fix rhymes\n- Enhance imagery"
        }]
    )
    return response.choices[0].message.content

def analyze_rhymes(poem: str) -> str:
    lines = [line.strip() for line in poem.split('\n') if line.strip()]
    last_words = [line.split()[-1].lower() for line in lines if line.split()]
    
    rhyme_report = []
    for i, word in enumerate(last_words):
        rhymes = pronouncing.rhymes(word)
        rhyme_list = ", ".join(rhymes[:3]) + "..." if rhymes else "None"
        rhyme_report.append(f"Line {i+1} ('{word}'): {rhyme_list}")
    
    return "\n".join(rhyme_report)

# ---- Full Workflow ---- #
def generate_poem(prompt: str) -> str:
    # Generate content
    themes = brainstorm(prompt)
    draft = write_poem(themes)
    final_poem = edit_poem(draft)
    
    # Analyze rhymes
    rhyme_analysis = analyze_rhymes(final_poem)
    
    # Format output
    return f"""🌟 FINAL POEM 🌟
{final_poem}

🔍 RHYME ANALYSIS 🔍
{rhyme_analysis}"""

# ---- Web Interface ---- #
interface = gr.Interface(
    fn=generate_poem,
    inputs=gr.Textbox(label="Enter your theme", placeholder="A robot learning to love..."),
    outputs=gr.Textbox(label="Result", lines=20),
    title="🤖 AI Poetry Team",
    description="Generate poems with rhyme analysis powered by Groq"
)

if __name__ == "__main__":
    interface.launch()