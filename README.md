#### **Backend**


**python env on unix:**
python3 -m venv `<environment name>`

source `<rootProject>`/`<environment name>`/bin/activate

**python dependences after activate venv:**

```
pip install -r requirements.txt
```

**run backend:**

```
flask run
```

or

```
flask run --debug
```

python tests:

```
python -m unittest -v
```


#### **Frontend**

`cd` to `clinet` folder 

**install npm packages:**

```
npm install
```

**start frontend:**

```
npm run dev
```

**start tests:**

```
npm test
```
