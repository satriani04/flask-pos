# Flask-pos
this is simple point of sale application build with python and flask micro framework.
this project created from workshop python by pythonID 8-9 Juni
[visit this master repo](https://github.com/faisalburhanudin/py89)

## How to setup
1. clone this repo
	`
	git clone repo-url
	`
2. open directory and create virtualenv
	`
	cd flask-pos
	`
	`
	virtualenv -p python3 env
	`
3. install all package
	`
	pip install -r requirements.txt
	`
4. dump sql to your local machine
5. make configuration file
	`
	cp pos/config.example.py pos/config.py
	`
6. run project
	`
	python run.py
	`
	and visit localhost:5000