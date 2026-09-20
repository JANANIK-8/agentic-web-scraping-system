
from agents.planner_agent import create_scraping_plan
from agents.scraper_agent import scrape_website


def main():
    print("=== Agentic Web Scraping System ===")

    user_query = input(
        "\nWhat do you want to scrape? "
    )

    url = input(
        "Enter website URL: "
    )

    # Step 1: Create a scraping plan
    plan = create_scraping_plan(user_query)

    print("\n--- Scraping Plan ---")
    print(plan)

    # Step 2: Scrape the website
    print("\nScraping website...")

    try:
        result = scrape_website(url)

        print("\n--- Scraping Results ---")
        print("Website Title:", result["title"])
        print("Links Found:", len(result["links"]))

        for link in result["links"][:10]:
            print(link)

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
