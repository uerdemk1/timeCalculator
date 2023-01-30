FROM ubuntu

RUN apt-get update && \
 apt install -y python3 && \
 apt install -y python3-pip && \
 pip install requests

COPY timeCalculator.py /home/timeCalculator.py

RUN chmod +x /home/timeCalculator.py
