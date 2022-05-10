# DeployDjangoToAWS

create AWS account 
install AWS CLI "out of env"
configure credentials 
install aws ebs cli "out of env"
    brew update
    brew install awsebcli
copy the project files to the repo root directory
create python3.8 env, activate and install the requirements
    python3.8 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    pip install --upgrade pip
.env
    https://djecrety.ir/   >> generate key
    DEBUG=True
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=youremailaddress@gmail.com
    EMAIL_HOST_PASSWORD=yourStrongPassword
    EMAIL_USE_TLS=True
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver