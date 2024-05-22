# Rapid
An API for generating and managing cyber security reports

## Prerequisits:
- Python
- Poetry - for dependency and project management `pip install poetry`

### Installation
1. Clone this repository `git clone`
2. install project dependencies from root folder using poetry `poetry install`

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
