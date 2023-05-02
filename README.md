# SMS
A Microservice application that breaks down all the core modules of school management system into microservices

## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/ChidiebereIbiam/sMS/LICENSE)

## Requirements
* Python 3.7+
* Django 4.2

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ChidiebereIbiam/SMS.git
$ cd SMS
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source venv/script/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.



## Microservice Reference

#### List of Microservices


| Parameter | Port for Testing     | Description                |
| :-------- | :------- | :------------------------- |
| `courses` | 127.0.0.1:8000 | Handles Course Microservice |
notice  | 127.0.0.1:8001| Handles Notice Microservice
result | 127.0.0.1:8002 | Result compiling and generation
student | 127.0.0.1:8003 | Student Microservice
teacher | 127.0.0.1:8004  | Teacher Microservice



## Authors

- [@Chidiebere Ibiam](https://github.com/ChidiebereIbiam)




