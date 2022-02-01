FROM python
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r ./requirements.txt
CMD ["python", "./test.py"]