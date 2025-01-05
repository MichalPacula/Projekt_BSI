FROM ubuntu:25.04

WORKDIR /demonstracja

RUN apt update && apt install -y build-essential python3-dev libssl-dev libffi-dev python3-cryptography

COPY ransomware.py .

RUN mkdir wazne_pliki
RUN echo "wazna informacja\nto jest bardzo wazna informacja" >> wazne_pliki/plik1.txt &\
    echo "kolejna wazna informacja" >> wazne_pliki/plik2.txt &\
    echo "to juz trzecia wazna informacja\nczyli ostatnia" >> wazne_pliki/plik3.txt \