FROM python:3
RUN pip install flask
RUN pip install requests
EXPOSE 6000/tcp
COPY todolist.py .
COPY index.html
CMD python todolist.py
