import logging
import os
import pandas as pd
from dotenv import load_dotenv

#Define logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

#Function to extract data from a CSV file
def extract_data(file_path: str) -> pd.DataFrame:
    #
    try:
        dataframe = pd.read_csv(
            file_path,
            header=None,
            sep="|"
        )
        #Verify if the dataframe is empty and log a warning
        if dataframe.empty:
            logger.warning("No data found in %s", file_path)
            return dataframe
        
        logger.info(
            "Extracted %d rows from %s",
            len(dataframe),
            file_path
        )
        return dataframe

    #Treat file not found error
    except FileNotFoundError:
        logger.error("File not found: %s", file_path)
        raise
    
    #Treat parse error
    except pd.errors.ParserError:
        logger.exception("Failed to parse %s", file_path)
        raise

def main():
    load_dotenv()
    
    file_path = os.getenv("FILE_PATH")

    if not file_path:
        raise ValueError("FILE_PATH environment variable is not set")

    df = extract_data(file_path)


if __name__ == "__main__":
    main()