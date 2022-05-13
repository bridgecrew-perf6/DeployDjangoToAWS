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
Create a directory named .ebextensions  >>
    create file in the folder named django.config and add the followng contents to the file
        option_settings:
            aws:elasticbeanstalk:container:python:
                 WSGIPath: greatkart/wsgi.py
deactivate the env
- run this command to create application in EB
    eb init -p python-3.7 greatkart-course
    output:> Application greatkart-course has been created.
    This createdfolder hosted the yml configuration file and deployed in AWS-EB-Applications
- run "eb init" command to setup ssh access to the environment and use the preferred key or create new one 
- now create environment inside EB 
    eb create greatkart-course-env
    it will take sometime to upload the project and create environment and install requirments, and create and deploy all the necessary infra
- "eb status" will show the env\app status 
if red , go to the application and restart the env
note down the CNAME 
CNAME: greatkart-course-env.eba-2nrr4meu.us-west-2.elasticbeanstalk.com
- add the CNAME to the allowed hosts 
- redeploy to take the changes "eb deploy"
    and restart the app incase it was red 
- now we need to configure the .env at eb console 
    AWS >Elastic Beanstalk>Environments>greatkart-course-env>Configuration>software>edit
    put all the keys and values stored at the .env
- 