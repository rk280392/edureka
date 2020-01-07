FROM devopsedu/webapp
COPY website_project /var/www/html/
EXPOSE 8223
CMD ["apachectl", "-D", "FOREGROUND"]

RUN apt-get install -y x11vnc xvfb 
RUN mkdir ~/.vnc
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
