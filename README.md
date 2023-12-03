# Advent of Code

## Setup
* Login to https://adventofcode.com/
* Use your browser DevTools to copy your session token from your cookies
* Paste it into a file called `src/utils/.token`
* `pip install requests` if you don't have it already
* Make sure the `src` directory is in your `PYTHONPATH` 

## Development
To start working on part 1 for year `{Y}` day `{D}`, make a copy of `src/utils/template.py` and store it as `src/solutions/{Y}/d{D}p1.py`.

Fill in:
* `example_answer`
* `example_data`
* `parsing_config` to customise how the input data is parsed (see `ParsingConfig` for details)
* `solve` which must return the answer when called with the parsed input data (list of records) OR the parser object (if you have specified a `ParsingConfig.parser_class`) 

Running this file will:
* Check that your `solve` function works as expected on the `example_data` (i.e. result matches `example_answer`)
* Download the actual input data (based on the year and day in the filename) using your token, run `solve` on it and print the answer
  * The data will be stored in `src/solutions/{Y}/d{D}.data`
* Print timings for each calculation

Once you have solved the puzzle, you can fill in `real_answer` and then try to improve your time - the script will check that your result still correct.

Once finished with part 1, create file `d{D}p2.py` and adjust as necessary.
