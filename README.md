Potrawy wigilijne
==============================

https://spa-wwsi.herokuapp.com/

---

## 🧐 About <a name = "about"></a>

This is simple page application intended to provide Easter recipes for specific categories.

```
├── main.py
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── static
│   ├── function.js
│   └── style.css
└── templates
    └── index.html
```


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

App was tested on python 3.8.5


Clone repository:
```
git clone https://github.com/Santhin/spa-wwsi.git
```

Install all dependencies needed for project with:

```
pip install -r requirements.txt
```
Start app with:

```
uvicorn main:app --host=0.0.0.0 --port=8000
```
open web browser and type:
```
http://localhost:8000
```

## 🚀 Deployment <a name = "deployment"></a>

Click the button below to set up this sample app on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


https://kaffeine.herokuapp.com/ 

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [FastAPI](https://fastapi.tiangolo.com/) - Server Framework
- [Heroku](https://www.heroku.com/) - Deploy

