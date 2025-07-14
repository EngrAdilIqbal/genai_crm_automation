# main.py

from agents.orchestrator_agent import orchestrate

def main():
    user_prompt = input("What do you want the CRM agent to do?\n> ")
    result = orchestrate.invoke({"input": user_prompt})
    print(result)

if __name__ == "__main__":
    main()
