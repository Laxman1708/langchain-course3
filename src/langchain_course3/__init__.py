from os import getenv

from dotenv import load_dotenv


def main() -> None:
    print("Hello from langchain-course3!")
    print("Loading environment variables from .env file...")
    load_dotenv()

    openai_api_key = getenv("OPENAI_API_KEY")
    print(f"OPENAI_API_KEY: {openai_api_key}")


if __name__ == "__main__":
    main()
