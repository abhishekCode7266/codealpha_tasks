# Stack Portfolio Tracker

A simple console-based stock portfolio tracker written in Python.

## Overview

This small script lets you enter stock symbols and quantities to compute the total investment value using a predefined (hardcoded) price list. It prints a portfolio summary to the console and optionally saves a report to `portfolio_report.txt`.

## Files

- `stack portfolio Tracker.py` — The main Python script that runs the tracker.

> Note: The filename contains spaces. When running from a terminal you may need to quote the path or rename the file to `stack_portfolio_tracker.py` for convenience.

## Requirements

- Python 3.6+ (Python 3 recommended)

## How it works

- The script contains a hardcoded `stock_prices` dictionary mapping stock symbols to their prices.
- The user is prompted to enter stock symbols (case-insensitive). Enter `done` when finished.
- For each known symbol, the script asks for the number of shares and records them in a `portfolio` dictionary.
- After input is complete, the script prints a per-stock calculation and the total investment value.
- A text report is written to `portfolio_report.txt` in the same directory.

## How to run

1. Open a terminal and change to the project folder:

   cd "CodeAlpha_Tasks_python project/CodeAlpha_Stack portfolio Tracker"

2. Run the script:

   python "stack portfolio Tracker.py"

   or, if your system uses `python3` for Python 3:

   python3 "stack portfolio Tracker.py"

If you rename the script to `stack_portfolio_tracker.py`, you can run it without quotes:

   python stack_portfolio_tracker.py

## Example session

- Enter Stock Symbol (or 'done' to finish): APPLE
- Enter Quantity: 5
- Enter Stock Symbol (or 'done' to finish): TSLA
- Enter Quantity: 2
- Enter Stock Symbol (or 'done' to finish): done

Output (example):

------ Portfolio Summary ------
APPLE : 5 shares × $180 = $900
TSLA : 2 shares × $250 = $500
-----------------------------------
Total Investment Value = $1400

A file named `portfolio_report.txt` will be saved in the same directory.

## Customization

- Update the `stock_prices` dictionary in `stack portfolio Tracker.py` to add more stocks or change prices.
- Add support for fetching live prices from an API (e.g., Yahoo Finance, Alpha Vantage) to make the tool more realistic.
- Validate numeric inputs and handle invalid entries (the current script assumes integer quantities).
- Allow updating existing holdings instead of replacing them, or support fractional shares.

## Limitations

- Prices are hardcoded; the script does not fetch real-time market data.
- No persistence other than the generated `portfolio_report.txt` file.
- Minimal input validation.

## Suggested improvements

- Rename the file to remove spaces for easier use.
- Add a requirements.txt and organize the project into a module with tests.
- Add a CLI (argparse) or simple GUI for better usability.

## License

Created by abhishekCode7266 as part of the CodeAlpha tasks collection. No license file is included; add one if you want to clarify reuse terms.
