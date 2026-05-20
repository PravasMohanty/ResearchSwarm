from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import settings


class LLMManager:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(

            model="gemini-2.5-flash",

            google_api_key=settings.GEMINI_API_KEY,

            temperature=0.3
        )

    async def generate(
        self,
        prompt: str
    ) -> str:

        response = await self.llm.ainvoke(prompt)

        return response.content


llm_manager = LLMManager()