# 
FROM python:3.9

# 
WORKDIR /MyFastBack

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /MyFastBack
#COPY . .
# 
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["uvicorn", "main:app", "--host", "api0602", "--port", "8000", "--reload"]

