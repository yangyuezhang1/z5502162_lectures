""" yf_example3.py

The purpose of this module is to download stock price data for Qantas for a given year and
save the information into CSV file
"""

# Import statement
import os
import toolkit_config as cfg
import yf_example2

# Define function
def qan_prc_to_csv(year):
    """
    Parameters for qan_prc_to_csv
    ----------
    year : integer
        Specify the year for the function to download stock price data for the given period

    Parameters for yf_prc_to_csv
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """

    # Construct the variable for yf_prc_to_csv function
    pth = os.path.join(cfg.DATADIR, f"qan_prc_{year}.csv")  # Using information from toolkit_config module
    tic = 'QAN.AX'
    start = f"{year}-01-01"                                  # specify start date using year parameter as year
    end = f"{year}-12-31"                                     # specify end date using year parameter as year

    # Call the yf_prc_to_csv function from yf_example2 module
    yf_example2.yf_prc_to_csv(tic, pth, start=start, end=end)

if __name__ == "__main__":
    year = 2000                                             # specify the year parameter to 2000
    qan_prc_to_csv(year)