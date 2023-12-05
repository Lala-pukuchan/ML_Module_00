FROM python:3.7

RUN pip install --upgrade pip && \
    pip install --upgrade pandas && \
    pip install --upgrade numpy && \
    pip install --upgrade matplotlib && \
    pip install --upgrade jupyter && \
    pip install --upgrade pycodestyle