import asyncio

from tools.llm import llm_manager


async def main():

    response = await llm_manager.generate(
        "Explain what AGI is in 3 lines"
    )

    print(response)


asyncio.run(main())
print(dir(llm_manager))