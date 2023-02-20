the yml and env files are already set
• once the docker is set in the target machine execute the following commands:
docker compose up -d

• if done any update to yml file then use following command
docker compose up --force-recreate

• I have prepared a basic dag file placed in dag folder this is from where airflow reads dag. Right now its just running regex.py