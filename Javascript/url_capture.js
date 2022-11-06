const puppeteer = require('puppeteer');

/*
The limitation of the programs are
- It requires a headless browser, if the installed browser is different than the one used by puppeteer, it will not work
- it will capture all the internal URL links, as it is capturing the urls from browser
*/

// check if the given url is a vaid url or not
function validURL(url) {
  if (url.includes('http://') || url.includes('https://')) {
    return true;
  } else {
    return false;
  }
}

async function run() {
  // going through all the provided arguments from the user, ignore first 2 because those are not an url
  for (let i = 2; i < process.argv.length; ++i) {
    // check if the given value is valid url or not
    current_url = process.argv[i];
    const validResult = validURL(current_url);

    //  if the given url is a vaid url capture the results
    if (validResult === true) {
      // storing the href
      var hrefArray = new Array();

      // capture the html page with other parser around, do nothing about it
      const browser = await puppeteer.launch();
      const page = await browser.newPage();
      await page.goto(current_url);

      const hrefs = await page.$$eval('a', (as) => as.map((a) => a.href));
      console.log(hrefs);

      for (let urls of hrefs) {
        if (urls.includes('http://') || urls.includes('https://')) {
          hrefArray.push(urls);
        }
      }

      // capture the html page
      await browser.close();

      // log this to console
      console.log(current_url + ' ' + hrefArray.length);
    } else {
      // else throw the invalid url to the user
      console.log('Invalid URL', current_url);
    }
  }
}

run();
