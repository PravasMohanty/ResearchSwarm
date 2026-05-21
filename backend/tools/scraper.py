import httpx
from bs4 import BeautifulSoup


class Scraper:

    async def scrape(
        self,
        url: str
    ):

        try:

            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url,
                    timeout=10,
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    }
                )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            for tag in soup([
                "script",
                "style",
                "noscript"
            ]):
                tag.decompose()

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            return {

                "url": url,
                "content": text[:15000]
            }

        except Exception as e:

            return {

                "url": url,
                "content": "",
                "error": str(e)
            }


scraper = Scraper()