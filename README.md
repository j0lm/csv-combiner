# csv-combiner

## How to use:

To run the program, follow this format:

```
python csv-combiner.py ./file-path-0.csv ./file-path-1.csv file-path-N.csv > output-file-path.csv
```

Example:

```
python csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv > output.csv
```

## How to use test program:

To automate the test cases, at least three csv input files must be put in a separate directory.  
To run the test program, follow this format:

```
python test.py ./directory-containing-input-files
```

Note: the directory path must end with a "/"  
Working example:

```
python test.py ./fixtures/
```

Failing example:

```
python test.py ./fixtures
```
