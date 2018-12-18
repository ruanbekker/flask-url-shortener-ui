# flask-url-shortener-ui
URL Shortener UI in Python Flask

- Blogpost about this is available: https://blog.ruanbekker.com/blog/2018/12/18/creating-a-ui-in-python-flask-and-bootstrap-for-our-serverless-url-shortener/

![](https://user-images.githubusercontent.com/567298/50162763-c5c16e80-02e7-11e9-8744-a4c3c3c51f8e.png)

## Running Standalone:

```bash
$ pip install -r requirements.txt
$ export TINY_API_URL=https://tiny-api.mydomain.com/create
$ export X_API_KEY=someRandomSecretKey09876543210
$ gunicorn -w 2 -b 0.0.0.0:8080 --access-logfile=/dev/stdout --error-log=/dev/stderr app:app
```
