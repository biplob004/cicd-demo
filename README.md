# Flask CI/CD Demo Application

This is a Flask demo application designed for testing and practicing CI/CD pipeline implementations.

## Features

- **Hello World Endpoint** (`/`) - Simple greeting endpoint
- **Health Check** (`/health`) - Health monitoring for CI/CD systems
- **App Info** (`/info`) - Application metadata and environment details
- **Comprehensive Testing** - Unit tests with pytest
- **Code Quality** - Automated linting and formatting
- **CI/CD Pipeline** - GitHub Actions workflow for automated testing and deployment

## Project Structure

```
cicd-demo/
├── app.py                 # Main Flask application
├── test_app.py           # Unit tests
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── .flake8              # Linting configuration
├── pyproject.toml       # Black formatter and pytest config
└── .github/
    └── workflows/
        └── ci.yml       # GitHub Actions CI/CD pipeline
```

## Setup and Installation

1. **Clone the repository** https://github.com/biplob004/cicd-demo
2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode

```bash
python app.py
```

The app will run on `http://localhost:5000`

### Production Mode

```bash
export FLASK_ENV=production
python app.py
```

## API Endpoints

- **GET /** - Returns a hello world message
- **GET /health** - Health check endpoint (returns JSON status)
- **GET /info** - Application information (name, version, environment)

## Testing

### Run Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=app --cov-report=html
```

## Code Quality

### Format Code

```bash
black .
```

### Lint Code

```bash
flake8 .
```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:

1. **Tests** on multiple Python versions (3.8-3.11)
2. **Lints** code with flake8
3. **Checks** code formatting with black
4. **Runs** comprehensive tests with coverage
5. **Builds** and verifies application startup

The pipeline runs on:

- Push to `main` or `develop` branches
- Pull requests to `main` branch

## Environment Variables

- `PORT` - Server port (default: 5000)
- `FLASK_ENV` - Environment mode (development/production)

## What's Been Implemented

✅ Flask web application with multiple endpoints  
✅ Comprehensive unit test suite  
✅ Code quality tools (flake8, black)  
✅ GitHub Actions CI/CD pipeline  
✅ Health monitoring endpoints  
✅ Environment configuration  
✅ Proper project structure and documentation
