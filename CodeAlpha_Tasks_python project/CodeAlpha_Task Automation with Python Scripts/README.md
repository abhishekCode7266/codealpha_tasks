# Task Automation — Email Extractor

A small Python script that extracts email addresses from a text file, removes duplicates, sorts them, and writes the results to an output file.

This README documents the included script `Task Automation.py`.

## What it does
- Reads a plain-text input file (default `input_emails.txt`), creating a small sample input file automatically if the file does not exist.
- Uses a regular expression to find email addresses anywhere in the file.
- Deduplicates and sorts the found addresses.
- Writes the unique addresses to `extracted_emails.txt` and prints a summary to the console.

## Files
- Task Automation.py — the script that performs extraction (located in the same folder as this README).
- input_emails.txt — default input file (the script will create a sample if missing).
- extracted_emails.txt — default output file created by the script.

## Requirements
- Python 3.6+ (no external packages required)
- Works on Windows, macOS, and Linux (ensure correct file permissions/encodings)

## Usage
1. Open a terminal and change into the directory that contains `Task Automation.py`:
   ```bash
   cd "CodeAlpha_Tasks_python project/CodeAlpha_Task Automation with Python Scripts"
   ```
2. Run the script:
   ```bash
   python "Task Automation.py"
   ```
   or, if your system uses `python3`:
   ```bash
   python3 "Task Automation.py"
   ```

The script prints the emails it found and the total count, and writes the results to `extracted_emails.txt`.

## Input format
- The script expects plain text. Email addresses can be on their own lines or embedded in other text.
- Example lines in `input_emails.txt`:
  ```
  john@gmail.com
  support@example.com
  contact: admin@test.org
  ```

## Output
- `extracted_emails.txt` — one email address per line, sorted, no duplicates.

## Regex used and limitations
- Pattern in the script:
  ```
  [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
  ```
- This is a practical regex that captures the vast majority of common email addresses, but it is not a full RFC 5322-compliant parser. It may:
  - Miss some valid but rare addresses (internationalized addresses, quoted local-parts).
  - Match some unusual/invalid addresses in edge cases.
- If you need stricter validation, consider using a dedicated email validation library or additional checks.

## Customization
- Change the input/output filenames by editing the top of `Task Automation.py`:
  ```python
  input_file = "my_input.txt"
  output_file = "my_output.txt"
  ```
- To accept filenames as command-line arguments, replace the fixed names with `argparse` usage (example snippet):
  ```python
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', default='input_emails.txt')
  parser.add_argument('--output', default='extracted_emails.txt')
  args = parser.parse_args()
  input_file = args.input
  output_file = args.output
  ```
- To use a different regex, update the `pattern` variable.

## Troubleshooting
- Permission errors: ensure you have write permission in the folder.
- Encoding issues: script opens files with UTF-8; ensure your input is UTF-8 or adjust the `encoding` parameter.
- No emails found: confirm the file path and contents; try adding a few test addresses to `input_emails.txt`.

## Potential Improvements
- Add command-line arguments (`argparse`) for filenames and regex.
- Support recursive scan of files under a directory.
- Add logging and unit tests.
- Export to CSV or other formats.
- Use an email validation library for stricter validation.

## License / Attribution
- This script is a small utility example. Add any license or project-specific attribution required for your repository.
