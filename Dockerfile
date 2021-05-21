FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/ilham77mansiz/PETERCORD- /root/PETERCORD-
WORKDIR /root/PETERCORD-/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
