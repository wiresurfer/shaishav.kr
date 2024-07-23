FROM squidfunk/mkdocs-material

COPY ./requirements.txt . 
RUN pip install -r requirements.txt

#ENTRYPOINT ["/bin/sh"]
