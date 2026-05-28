import httpx
from bs4 import BeautifulSoup
from utils.logger import logger

class Scraper:

    async def scrape(
        self,
        url: str
    ):

        try:
            logger.info(f"Scraping webpage: {url}")
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
                "content": text[:30000]
            }

        except Exception as e:

            logger.error(f"Scraping failed for {url}: {e}")

            return {

                "url": url,
                "content": "",
                "error": str(e)
            }


scraper = Scraper()
