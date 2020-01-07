FROM devopsedu/webapp
COPY website /var/www/html/
EXPOSE 8223
CMD ["apachectl", "-D", "FOREGROUND"]
