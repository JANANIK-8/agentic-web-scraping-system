
def create_scraping_plan(user_query):
    """
    Create a scraping plan from the user's request.
    """

    plan = {
        "user_query": user_query,
        "task": "Web scraping",
        "required_fields": [
            "title",
            "description",
            "url"
        ],
        "status": "Plan created"
    }

    return plan


if __name__ == "__main__":

    user_query = input(
        "What do you want to scrape? "
    )

    plan = create_scraping_plan(user_query)

    print("\n--- Scraping Plan ---")

    for key, value in plan.items():
        print(f"{key}: {value}")
