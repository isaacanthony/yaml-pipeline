FROM python:3.7
WORKDIR /src

# Install depedencies
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade -r requirements.txt

# Set up package
COPY . .
RUN pip3 install -e .
