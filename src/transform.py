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
        # Drop the first three rows and reset the index
        dataframe = dataframe.iloc[3:].reset_index(drop=True)
        
        # Rename columns
        dataframe.columns = [
            "Ano",
            "Homens_Qtd",
            "Homens_Pct",
            "Mulheres_Qtd",
            "Mulheres_Pct",
            "Total_PF"
        ]
        
        #Transform 'Ano' column to numeric, coercing errors to NaN        
        dataframe['Ano'] = pd.to_numeric(
            dataframe['Ano'], 
            errors='coerce'
        )
        
        # Drop rows with any NaN values
        dataframe = dataframe.dropna(how='all').reset_index(drop=True)
        
        # Define columns types
        dataframe = dataframe.astype({
            "Ano": 'int64',
            "Homens_Qtd": 'int64',
            "Homens_Pct": 'float64',
            "Mulheres_Qtd": 'int64',
            "Mulheres_Pct": 'float64',
            "Total_PF": 'int64'
        })
        
        return dataframe
    
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise
    