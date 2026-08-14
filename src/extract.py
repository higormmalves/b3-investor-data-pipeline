import logging
import os
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def extract_data(file_path: str) -> pd.DataFrame:
    try:
        dataframe = pd.read_csv(
            file_path,
            header=None,
            sep="|"
        )

        if dataframe.empty:
            logger.warning("No data found in %s", file_path)

        logger.info(
            "Extracted %d rows from %s",
            len(dataframe),
            file_path
        )

        return dataframe

    except FileNotFoundError:
        logger.error("File not found: %s", file_path)
        raise

    except pd.errors.ParserError:
        logger.exception("Failed to parse %s", file_path)
        raise


file_path = os.getenv("FILE_PATH")

if not file_path:
    raise ValueError("FILE_PATH environment variable is not set")
