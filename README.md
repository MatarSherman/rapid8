# Rapid
An API for generating and managing cyber security reports

## Prerequisits:
- Python
- Poetry - for dependency and project management `pip install poetry`

### Installation
1. Clone this repository `git clone`
2. install project dependencies from root folder using poetry `poetry install`
3. add a '.env' file
    - in the root folder create a new file called .env (should be on the same level as .gitignore and README.md).
    - in the .env file add a 'CONNECTION_STRING' variable, in which is a MongoDB connection string to a database containing a phishtank data dump.
    - notice, no double/single quotes is needed.
    - example:

      `.env`

      ```CONNECTION_STRING=mongodb+srv://a-mongo-connection-string-example```

### Usage
- Start development server `poetry run poe dev`
- Start production server `poetry run poe prod`

### Docker (Optional)
1. build the image (from root folder) `docker build -t rapid-api .`
2. run the container `docker run -p 8000:8000 rapid-api`

### API Request Examples
#### When Running On Local:
    http://localhost:8000/phish/details?domain_name=tinyurl.com
    http://localhost:8000/phish/report?start=2024-05-14
    http://localhost:8000/phish/report?start=2024-05-14&end=2024-05-16
