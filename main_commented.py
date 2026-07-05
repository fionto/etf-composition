from pathlib import Path
import pandas as pd

# ============================================================================
# STEP 1: SETTING UP THE FILE PATH
# ============================================================================
# Path(__file__) gets the location of this script file
# .parent navigates to the folder containing this script
# / 'data' appends a subfolder called 'data' to the path
raw_datasets_dir = Path(__file__).parent / 'data'
filename = 'Constituent_IE000YKHGYN2.xlsx'

# Combine the directory path and filename to get the full file path
filepath = raw_datasets_dir / filename

# ============================================================================
# STEP 2: READING THE EXCEL FILE
# ============================================================================
# index_col=0 means: use the first column (column 0) as the row index
# This means the first column won't be treated as regular data but as row labels
df = pd.read_excel(filepath, index_col=0)

# ============================================================================
# STEP 3: UNDERSTANDING iterrows()
# ============================================================================
# WHAT DOES iterrows() RETURN?
# ----------------------------
# iterrows() returns an iterator that yields pairs of (index, row) for each row
# 
# - 'index' is the index label of the current row (could be number, date, etc.)
# - 'row' is a Series object containing ALL the data for that row
# 
# The 'row' Series has:
#   - Keys = column names (like "Currency", "Weighting")
#   - Values = the actual data in that cell
# 
# HOW TO ACCESS DATA FROM 'row':
# ------------------------------
# 1. row["Currency"]     # Dictionary-style access (recommended)
# 2. row.Currency        # Attribute-style access (works but can conflict)
# 3. row.iloc[0]         # Position-based access (not recommended here)
# 
# IMPORTANT WARNING:
# ------------------
# iterrows() returns a COPY of each row, NOT a view!
# Modifying 'row' will NOT affect the original DataFrame.

# Initialize an empty dictionary to store currency totals
# Format: { "USD": 45.5, "EUR": 30.2, ... }
currencies = {}

# Loop through the first 20 rows of the DataFrame
# df.head(20).iterrows() creates an iterator for exactly 20 rows
# 
# for _, row in ... 
#   - '_' (underscore) is used for the index because we DON'T need it
#   - 'row' is the Series containing all column data for this row
for _, row in df.head(20).iterrows():
    
    currency = row["Currency"]
    weight = row["Weighting"]
    
    # ========================================================================
    # UNDERSTANDING THE DICTIONARY UPDATE
    # ========================================================================
    # currencies.get(currency, 0) works like this:
    #   - If 'currency' exists in the dictionary → return its current value
    #   - If 'currency' does NOT exist → return the default value (0)
    currencies[currency] = currencies.get(currency, 0) + weight

print(currencies)