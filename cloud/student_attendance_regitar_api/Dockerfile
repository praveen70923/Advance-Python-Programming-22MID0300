FROM public.ecr.aws/lambda/python:3.11

WORKDIR /var/task

RUN yum install -y gcc make rust cargo && \
    python3.11 -m pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["app.lambda_handler"]
