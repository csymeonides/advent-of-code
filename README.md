# Advent of Code

## Setup
* Login to https://adventofcode.com/
* Use your browser DevTools to copy your session token from your cookies
* Paste it into a file called `src/.token`

## Development
To start working on the puzzle for year `Y` day `N`, make a copy of `src/template.py` and store it as `src/Y/dNp1.py`.

Fill in:
* `example_answer`
* `example_data`
* `parsing_config` to customise how the input data is parsed (see `ParsingConfig` for details)
* `solve` which is called with the parsed input data (list of records) and must return the answer 

Running the script will:
* Check that your `solve` function works as expected on the `example_data`
* Download the actual input data using your token, run `solve` on it and print the answer
* Print timings for each calculation

Once finished with part 1, make a copy of this file as `dNp2.py` and adjust as necessary.
