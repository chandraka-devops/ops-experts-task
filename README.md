## EqualExperts API Assignment 

### Prerequisites( Installation )
* You should have docker installed check:- `docker --version`
* Optional:- Good to run with Python virtual env for code coverage.
* Python3 version should have >=python3.9
* pip3 should have installed.

### Build,  test, and package it into a container
* Step 1:- Clone this repository to your local machine.
```
 ## Optional :- Create github token if required for clone 
 git clone https://github.com/EqualExperts-Assignments/equal-experts-shrewd-quiet-enchanting-offering-58db94a9f9f2.git
```
* Step 2:- It should have folder structure like below
```
chandra_project
├── app.py
├── Dockerfile
├── README.md
├── requirements.txt
└── test_app.py
```

* Step 3:- Now go to chandra_project directory and do docker image build.
```
  docker build -t equal-experts-gist-api:1.0.0 .

  docker images | grep experts-gist
  equal-experts-gist-api                                                  1.0.0                  4b4152dae52c   About a minute ago   142MB

```
* Step 4:- Start app container for application. 
```
  docker run -d -p 8080:8080 --name=gist-api equal-experts-gist-api:1.0.0

  docker ps -a | grep gist-api
  55daa691573e   equal-experts-gist-api:1.0.0              "python3 app.py"         3 minutes ago    Up 3 minutes                  0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp   gist-api                                            1.0.0                  4b4152dae52c   About a minute ago   142MB
   
```

* Step 5:- (Optional) :- Better to run venv for coverage 
```
python3 -m venv appvenv
source appvenv/bin/activate
pip install -r requirements.txt
```

* Step 6:- Run Unit test case and coverage (On another terminal)
```
python3 test_app.py

## Run for coverage

coverage run --source=app -m unittest discover

 ⇒  coverage report -m
Name     Stmts   Miss  Cover   Missing
--------------------------------------
app.py      20      4    80%   16, 21-22, 30
--------------------------------------
TOTAL       20      4    80%

```

## Troubleshoot
### Docker logs after app start 
```
⇒  docker logs gist-api
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
Press CTRL+C to quit
```

### Issues and Solution If any
* Optional(Recommendation :- If you face issue NotOpenSSLWarning: urllib3 v2 )
  If you're just testing or developing locally, downgrade urllib3:
  `pip install 'urllib3<2'`
