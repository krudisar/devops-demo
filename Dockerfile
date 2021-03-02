FROM centos/python-36-centos7
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY src/app.py /app
CMD [ "python3", "./app.py" ]
