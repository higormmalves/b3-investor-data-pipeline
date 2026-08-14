from extract import extract_data
import pandas as pd
import logging

# Define logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Function to transform data
def transform_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    try:
        dataframe = dataframe.iloc[3:].reset_index(drop=True)
        
        dataframe.columns = [
            "Ano",
            "Homens_Qtd",
            "Homens_Pct",
            "Mulheres_Qtd",
            "Mulheres_Pct",
            "Total_PF"
        ]
        
        return dataframe
    
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise
    
if __name__ == "__main__":
    df = extract_data("../data/raw/b3_investors_data.csv")
    df_transformed = transform_data(df)

    print(df_transformed.head())