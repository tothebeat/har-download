har-download
============

Download the HTTP Archive for a given page using selenium, Firefox, firebug, and netexport.

Motivation
----------
Some sites load images through JavaScript, and it can be troublesome to scrape their sources when looking only at the DOM. By capturing a log of all net traffic that occurs when loading the page, the image resources (and a lot of other stuff!) can be picked out very easily. This could be done using a local web proxy but I don't know of a good and simple one, and it doesn't seem very fast to spin up or tear down.

HAR Format
----------
* http://www.softwareishard.com/blog/har-viewer/

Interesting Sites
-----------------
* http://bav.bodleian.ox.ac.uk/ - Uses OpenSeadragon for Deep Zoom images, based on Microsoft's Seadragon platform.
* http://zoom.it/
