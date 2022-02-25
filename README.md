### Exchange Rates

This python script has the following functionalities:

- Web scraping (https://x-rates.com/table/?from=EUR&amount=1).
- Retrieving the latest exchange rates.
- Saving the fetched data to a CSV file.

The steps that must be taken to set up this script are as follows:

- Clone the GitHub repository (preferably into */home/"user"/projects/*)
	```
	[mkdir ~/projects/]
	git clone git@github.com:mohelhelb/xrate.git [~/projects/xrate/]
	```	
- Isolate the project by creating a virtual environment.
	```
	pip install virtualenv
	virtualenv ~/projects/xrate/venv/
	source ~/projects/xrate/venv/bin/activate
	```
- Install the project's dependencies (See the *requirements.txt* file).
	```
	pip install -r ~/projects/xrate/requirements.txt
	```
- Modify the *xrate_file* variable (`xrate_file=f"xrates_{tday}.csv"`) in the *websraper.py* script accordingly.
- Execute the python script.
	```
	[sudo chmod a+x ~/projects/xrate/webscraper.py]
	python ~/projects/xrate/webscraper.py
	```
