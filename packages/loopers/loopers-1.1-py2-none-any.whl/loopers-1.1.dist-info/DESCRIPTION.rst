### Looper


**Looper is a framework used in scrapping emails out of a webpage.

***

#### **Functions**
- Scraps emails from webpage
- Allow checking first level subdirectories 


***

#### **Requirements**
- Python 3.x or 2.x
- Working internet
- Requests

**NOTE: BeautifulSoup is for listing out links in that webpage, so it's not necessary**
***

#### **Usage**

- Install looper by entering this command in your terminal 

> pip install loopers

- Import looper to your codes. 

> from loopers import loop

loop, a function in looper takes two arguments;
- The first argument is the link to the webpage you are trying to crawl emails from 
- The second argument, **iter**, used for generating links inside that webpage, iter is either set to True or False 

> **if True** it will print out the links in that webpage. **Note:** BeautifulSoup is needed if set to True. 

>**if False**, it will skip it.

***

##### Endnote
If at all there is an issue raised during execution of the command, kindly raise an issue here or better still **mail me at akeremukhtar10@gmail.com**.
Thanks for your time. 




