FROM python:3
RUN pip install bs4
RUN pip install requests

WORKDIR /usr/src/app

CMD ["python", "/usr/src/app/stock_web_scrapper.py"]