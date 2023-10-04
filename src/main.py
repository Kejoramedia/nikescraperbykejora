# main
import asyncio
from src.nikescraperbykejora.scrapingresult import ProductScraperHandler


# Single Product
# async def main():
#     # User input for scraping one product
#     target_url_one = "https://www.nike.com/id/t/air-force-1-07-shoe-NMmm1B/DD8959-100"
#     txt_file_name = "Nike Air Force 1 '07"
#
#     await ProductScraperHandler.one_product(target_url_one, txt_file_name)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


# Multiple Product
async def main():
    # User input for scraping multiple products
    target_url_multi = "https://www.nike.com/id/w/girls-700000-1500000-lifestyle-shoes-13jrmz5bl6vz6bnmbzy7ok"
    csv_file_name = "Girl Lifestyle Shoes.CSV"
    product_count = 26
    timeout_seconds = 10

    await ProductScraperHandler.multi_product(target_url_multi, csv_file_name, product_count, timeout_seconds)


if __name__ == "__main__":
    asyncio.run(main())
