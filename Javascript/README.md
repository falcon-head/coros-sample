# Problem Statement

The program should, given a list of HTTP and HTTPS URLs as arguments, retrieve each URL as a document and return the number of unique external URLs referenced in the document. Your program must parse HTML document responses, although you may optionally choose to also parse other document types for external URLs. For example, an invocation with a list of URLs should look something like `program http://example.com, http://www.columbia.edu/~fdc/sample.html`. For each valid URL, your program should print a line consisting of the URL and the number of external links in the retrieved document, separated by a space, like `http://example.com 1`. Each URL should be printed on its own line of the output.

## Running the Javascript program

The program is written in node v16.18.0

## Steps to Run the program

1. Download the program
2. cd into the directory `cd Javascript`
3. Run the program using `npm install` to install the required libraries
4. Run the program using `node url_capture.js url1 url2 url3 url4 url5`
5. The program will output the result to console

## Limitations of the program

The limitation of the programs are

- It requires a headless browser, if the installed browser is different than the one used by puppeteer, it will not work
- it will capture all the internal URL links along with external URL link, as it is capturing the urls from browser

# Problem Statement

The program should, given a list of HTTP and HTTPS URLs as arguments, retrieve each URL as a document and return the number of unique external URLs referenced in the document. Your program must parse HTML document responses, although you may optionally choose to also parse other document types for external URLs. For example, an invocation with a list of URLs should look something like `program http://example.com, http://www.columbia.edu/~fdc/sample.html`. For each valid URL, your program should print a line consisting of the URL and the number of external links in the retrieved document, separated by a space, like `http://example.com 1`. Each URL should be printed on its own line of the output.

## Running the Javascript program

The program is written in node v16.18.0

## Steps to Run the program

1. Download the program
2. cd into the directory `cd Javascript`
3. Run the program using `npm install` to install the required libraries
4. Run the program using `node url_capture.js url1 url2 url3 url4 url5`
5. The program will output the result to console

## Limitations of the program

The limitation of the programs are

- It requires a headless browser, if the installed browser is different than the one used by puppeteer, it will not work
- it will capture all the internal URL links along with external URL link, as it is capturing the urls from browser
