# Rapid
An API for generating and managing cyber security reports

## Prerequisits:
- Python
- Poetry - for dependency and project management `pip install poetry`

### Installation
1. Clone this repository `git clone`
2. install project dependencies from root folder using poetry `poetry install`
3. add a '.env' file
    - in the root folder create a new file called .env (should be in the same directory as .gitignore, README.md and Dockerfile).
    - in the .env file add a 'CONNECTION_STRING' variable, in which is a MongoDB connection string to a database containing a phishtank data dump.
    - notice, no double/single quotes are needed.
    - example:

      `.env`

      ```
      CONNECTION_STRING=mongodb+srv://a-mongo-connection-string-example
      ```

### Usage
#### From root folder:
- Start development server `poetry run poe dev`
- Start production server `poetry run poe prod`

### Docker (Optional)
#### From root folder:
1. Build the image `docker build -t rapid-api .`
2. Run the container `docker run -p 8000:8000 rapid-api`

### API Request Examples
#### When Running Locally/Docker:
    http://localhost:8000/phish/details?domain_name=tinyurl.com
    http://localhost:8000/phish/report?start=2024-05-14
    http://localhost:8000/phish/report?start=2024-05-14&end=2024-05-16
