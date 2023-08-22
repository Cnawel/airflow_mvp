Steps for installing and Airflow instance in a small spechs UNIX server/vps

Expose port 8080 after that using UFW

# Update package database
sudo apt update

# Install Python package manager (pip)
sudo apt install python3-pip

# Install SQLite database management system
sudo apt install sqlite3

# Install Python virtual environment module
sudo apt install python3.10-venv

# Install development files for PostgreSQL
sudo apt-get install libpq-dev

# Activate Python virtual environment
source venv/bin/activate

# Install Apache Airflow version 2.5.0 with PostgreSQL support
pip install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"

# Initialize Airflow metadata database
airflow db init

# Install PostgreSQL and additional contributions
sudo apt-get install postgresql postgresql-contrib

# Switch to PostgreSQL user and start PostgreSQL command-line client
sudo -i -u postgres
psql

# PostgreSQL commands to set up Airflow database
CREATE DATABASE airflow;
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

# Modify Airflow configuration to use PostgreSQL
sed -i 's#sqlite:////home/ubuntu/airflow/airflow.db#postgresql+psycopg2://airflow:airflow@localhost/airflow#g' airflow.cfg

# Change Airflow executor from SequentialExecutor to LocalExecutor
sed -i 's#SequentialExecutor#LocalExecutor#g' airflow.cfg

# Initialize Airflow metadata database again for PostgreSQL
airflow db init

# Create admin user for Airflow
airflow users create -u airflow -f airflow -l airflow -r Admin -e airflow@gmail.com

# Start Airflow web server in the background
airflow webserver &

# Start Airflow scheduler
airflow scheduler
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

sed -i 's#sqlite:////home/ubuntu/airflow/airflow.db#postgresql+psycopg2://airflow:airflow@localhost/airflow#g' airflow.cfg

sed -i 's#SequentialExecutor#LocalExecutor#g' airflow.cfg

airflow db init

airflow users create -u airflow -f airflow -l airflow -r Admin -e airflow@gmail.com

airflow webserver &

airflow scheduler
