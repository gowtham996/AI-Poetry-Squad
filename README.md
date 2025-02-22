# 🤖 AI Poetry Team

An AI agent team that collaboratively writes poems using Groq's LLMs (Llama 3/Mixtral). Features brainstorming, writing, editing agents, and rhyme analysis.

![Demo](https://i.imgur.com/5XJQZ6L.png) <!-- Add your screenshot later -->

## Features
- **Multi-Agent Workflow**: Brainstorm → Write → Edit → Analyze
- **Rhyme Analysis**: Checks rhyming words using `pronouncing`
- **Web Interface**: Gradio UI for easy interaction
- **Groq Integration**: Ultra-fast LLM inference

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- [Groq API Key](https://console.groq.com/)

### Installation
```bash
git clone https://github.com/your-username/AI-Poetry-Team.git
cd AI-Poetry-Team
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# OR
.\.venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### Configuration
1. Create `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Add your [Groq API key](https://console.groq.com/) to `.env`

### Usage
```bash
python poetry_team.py
# Access UI at http://localhost:7860
```

## Example Output
**Input**: "A robot learning to love"  
**Themes**:
- Mechanical longing
- Binary emotions  
**Poem**:
```
Silicon Heartbeats
The robot's pulse, a timed delay...
```

## 📚 Resources
- [Groq Documentation](https://groq.com/)
- [Gradio UI Guide](https://www.gradio.app/)
