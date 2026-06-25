import pandas as pd 

api_key_file = "tool_info/API_KEYS.xlsx"

# def get_api_key (tool_name) :

#     df = pd.read_excel(api_key_file)

#     row = df[df["TOOL"].str.upper() == tool_name.upper()]

#     if row.empty:
#         raise ValueError (f"No API key found for '{tool_name}'")
    
#     return row.iloc[0]["API_KEYS"]

_df = pd.read_excel(api_key_file)

_API_KEYS = dict(
    zip(
        _df["TOOL"].str.upper(),
        _df["API_KEY"]
    )
)

def get_api_key(tool_name):
    return _API_KEYS.get(tool_name.upper())