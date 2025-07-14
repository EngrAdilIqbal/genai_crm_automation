# GenAI CRM Automation

A simple GenAI agent that automates **basic CRM tasks** using **OpenAI** + **LangChain**.  
This version runs **without LangGraph** for simplicity and reliability.

---

## What this project does

This agent can:
- Create a contact
- Create a deal
- Link deals to contacts
- Simulate basic CRM workflows

It uses **natural language input** → runs through an LLM → calls **mock CRM tools** → returns a result.

---

## How it works (no LangGraph)

We use:
- `ChatOpenAI` as the LLM
- `AgentExecutor` + `create_openai_functions_agent` to enable tool calling
- A **plain Python script** to orchestrate input/output

👉 There is **no LangGraph** or **StateGraph** here — this keeps things **linear**, simple, and easier to debug.  
**Why?**  
Because the workflow is one-shot:
**Prompt → LLM → Tool → Done.**  
LangGraph is more useful for **multi-step, conditional, or branching workflows** — not needed here.

---

## 🗂️ Project Structure

```

genai\_crm\_automation/

├── main.py

├── agents/

│   └── orchestrator_agent.py

│   └── hubspot_agent.py

│   └── email_agent.py

├── tools/

│   └── crm_tools.py

│   └── email_tools.py

├── mock_crm.py

├── requirements.txt

├── README.md

````

---

## 🚀 How to run it

1️⃣ Clone this repo:

```bash
git clone https://github.com/your-username/genai_crm_automation.git
cd genai_crm_automation
````

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

**Example `requirements.txt`**

```
langchain
langchain_openai
```

3️⃣ Set your **OpenAI API key**:

```bash
export OPENAI_API_KEY=your_openai_key_here
# Or on Windows:
set OPENAI_API_KEY=your_openai_key_here
```

4️⃣ Run the agent:

```bash
python main.py
```

✅ Example interaction:

```
What do you want the CRM agent to do?
> Create a contact named John Doe with email john@example.com.
```

---

## 🧩 Why I used **mock CRM tools**

This project uses **mock CRM tools** instead of integrating with a **real CRM (like HubSpot, Salesforce, Zoho)** because:

* 💰 **Cost:** Real CRMs often require **paid tiers** for full API access.
* 🔒 **Access limits:** Free accounts have **API quotas** or restricted endpoints.
* 🔑 **API keys:** Using real keys in an open project is risky for misuse.
* 🧪 **Testing:** Mock tools make it safe to experiment without affecting real customer data.
* 🧩 **Focus:** The goal is to showcase the **agent orchestration**, not the CRM backend.
* 🔗 **Pluggable:** The mock tools can easily be swapped for real API calls when ready.

👉 If you want real integration, you can:

* Replace `tools/crm_tools.py` with actual API calls
* Add auth (OAuth, API keys)
* Map the same tool interface to real endpoints

---

## Why this works well **without LangGraph**

LangGraph is great for:

* 🧵 Complex multi-turn workflows
* 🔄 Loops, branches, memory graphs
* 🤝 Multi-agent orchestration

But for:

* ✅ Simple **one-shot tasks**
* ✅ Few tools
* ✅ Straight pipelines

...**plain `AgentExecutor` is enough** — fewer moving parts, faster debugging.

---

## ✅ Next steps

* Add real CRM API integration
* Store conversation history
* Add LangGraph if you want branching logic

---

** Maintainer:** \[Your Name]
**License:** MIT

Enjoy automating your CRM! 🚀

```

---

##  Ready to use!

If you’d like, I can also write:
- ✅ A ready `requirements.txt`
- ✅ An example `crm_tools.py`
- ✅ A `.gitignore`

**Want it? Just say: _“Yes, give me the starter pack!”_ 🚀**
```
