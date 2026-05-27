from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
import asyncio

load_dotenv()

@function_tool
def add_numbers(a: float, b: float) -> str:
    return f"The answer to {a} + {b} is {a+b}"

@function_tool
def sub_numbers(a: float, b: float) -> str:
    return f"The answer to {a} - {b} is {a-b}"

agent = Agent(
    name = "Math Agent",
    instructions = "Your goal is to assist the ASKER in the calculations of anything",
    tools = [add_numbers, sub_numbers]
)

async def main():
    while(True):
        user_input = input("ASKER: ")

        if (user_input.lower() == "end"):
            break
        
        result = await Runner.run(agent, user_input)
        print("AGENT: ", result.final_output)

asyncio.run(main())
