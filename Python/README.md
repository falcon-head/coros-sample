# Problem Statement

The program should, given a list of HTTP and HTTPS URLs as arguments, retrieve each URL as a document and return the number of unique external URLs referenced in the document. Your program must parse HTML document responses, although you may optionally choose to also parse other document types for external URLs. For example, an invocation with a list of URLs should look something like `program http://example.com, http://www.columbia.edu/~fdc/sample.html`. For each valid URL, your program should print a line consisting of the URL and the number of external links in the retrieved document, separated by a space, like `http://example.com 1`. Each URL should be printed on its own line of the output.

## Running the python program

The program is written in python 3.10.0

## Steps to Run the program

1. Download the program
2. cd into the directory `cd coros`
3. Run the program using `python3 -r requirements.txt` to install the required libraries
4. Run the program using `python3 url_capture.py url1 url2 url3 url4 url5`
5. The program will output the result to console

## Limitations of the program

- it will not capture any urls present outside the 'a' tags, for example paragraph with manually return url
- it will not capture the urls that doesn't contain an href with https:// or http:
