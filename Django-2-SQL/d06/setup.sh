sudo apt-get install libpq-dev
sudo apt update
sudo apt install postgresql


# write them after; sudo -i -u postgres
# postgres=# CREATE USER djangouser WITH PASSWORD 'secret';
# postgres=# CREATE DATABASE djangotraining OWNER djangouser;
# postgres=# GRANT ALL PRIVILEGES ON DATABASE djangotraining TO djangouser;