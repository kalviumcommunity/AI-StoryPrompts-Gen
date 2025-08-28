# AI Story Prompt Generator

**Description:**
The AI Story Prompt Generator is an AI-powered tool designed to help writers, artists, and creators generate imaginative prompts to inspire stories, artwork, or other creative works. It is perfect for overcoming writer’s block and sparking creativity by providing fresh, high-quality ideas.

**Why Useful:**

* Boosts creativity and idea generation.
* Saves time brainstorming new prompts.
* Helps maintain consistent content creation.
* Supports multiple genres, themes, and styles.

---

## **Features & Concept Mapping**

**Prompt Concepts:**

* **System and User Prompt:** Clearly defines the AI role as a creative assistant and accepts user topic or theme.
* **Zero-Shot Prompting:** Generates prompts without any prior examples.
* **One-Shot Prompting:** Provides a single example prompt to guide the AI’s output.
* **Multi-Shot Prompting:** Provides multiple example prompts for more accurate and creative output.
* **Dynamic Prompting:** Prompts adapt automatically based on user input (genre, theme, or style).
* **Chain of Thought Prompting:** AI explains its reasoning before generating prompts.

**LLM Features:**

* **Temperature:** Adjusts creativity and randomness of outputs.
* **Top P / Top K:** Controls diversity of generated ideas.
* **Stop Sequence:** Defines boundaries for AI output.
* **Structured Output:** Produces prompts in a clear, organized format.

**Tokens and Tokenization:**

* Monitors the number of tokens used per AI call to track efficiency and cost.

---

## **Sample Usage / Test Inputs**

Try these example topics to generate story prompts:

* “Fantasy adventure with dragons”
* “Romantic story in a futuristic city”
* “Horror prompt for a short story”
* “Sci-fi world-building idea”
* “Children’s bedtime story inspiration”

---

## **Tech Stack**

* **Python** – Backend scripting.
* **Groq LLM API** – AI language model for generating story prompts.
* **Streamlit** – Interactive web UI.
* **Dotenv** – Manage API keys securely.

---

## **Folder Structure**

```
AI-Story-Prompt-Generator/
├── app.py
├── requirements.txt
├── README.md
├── .env
├── src/
│   ├── config.py
│   ├── groq_client.py
│   └── utils.py
```
