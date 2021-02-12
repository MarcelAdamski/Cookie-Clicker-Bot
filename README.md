# Cookie-Clicker-Bot
[Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) Bot made using Python 3 with Selenium Framework. Made for educational purposes only.

## Installation

Download files and run with your favourite IDE. Enjoy.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium Framework if you don't have yet.

```bash
pip install selenium
```
In PATH variable put path to your ChromeDriver.exe. If you don't have ChromeDriver you can download it here: [ChromeDriver](https://chromedriver.chromium.org/downloads)

## Functionalities

* Clicking at BigCookie
* First buying the most expensive upgrade from store and then goes to least expensive upgrade 
* Loading saves
* Saving game
* Clicking golden cookie whenever it appears on screen

## Starting parameters

Please adjust parameters in code for your needs. 

* SMALL_CLICK_LOOP - determines how many clicks in one "small loop" - default is 100 and I recommend leaving this option at 100
* SHOP - determines how many "small clicks" multiplied by this variable to perform, before trying to buy anything from shop or try to upgrade. For example 25 means shopping every ~40sec and 50 means shopping every ~1:15
* SAVE - determines how many "small clicks" multiplied by this variable to perform, before trying to save a game. For exmaple 50 means saving about every 1:20min and 100 means saving about every 2:30
* LOOPS - one loop is "SMALL_CLICK_LOOP" clicks on bigCookie, checks for shop and save.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
