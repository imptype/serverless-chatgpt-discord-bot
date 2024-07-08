from dotenv import load_dotenv

# Load env if running locally
load_dotenv(override = True)

from src.bot import run

app = run()