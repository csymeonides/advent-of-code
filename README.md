# Advent of Code

## Setup
* Login to https://adventofcode.com/
* Use your browser DevTools to copy your session token from your cookies
* Paste it into a file called `src/.token`
* `pip install requests` if you don't have it already
* Make sure the repo root directory is in your `PYTHONPATH` 

## Development
To start working on the puzzle for year `Y` day `N`, make a copy of `src/template.py` and store it as `src/Y/dNp1.py`.

Fill in:
* `example_answer`
* `example_data`
* `parsing_config` to customise how the input data is parsed (see `ParsingConfig` for details)
* `solve` which must return the answer when called with the parsed input data (list of records) OR the parser object (if you have specified a `ParsingConfig.parser_class`) 

Running the script will:
* Check that your `solve` function works as expected on the `example_data`
* Download the actual input data using your token, run `solve` on it and print the answer
* Print timings for each calculation

Once finished with part 1, make a copy of this file as `dNp2.py` and adjust as necessary.
