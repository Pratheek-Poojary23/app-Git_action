# GitHub Actions CI/CD Pipeline

## Project Setup

### 1. Project Structure
- Created `src/` and `tests/` folders
- Within `src/`: 
  - `__init__.py`
  - `math_operation.py`

### 2. Source Code
- Implemented mathematical operation functions in `math_operation.py`

### 3. Testing
- Created `tests/` directory with:
  - `__init__.py`
  - `test_operation.py` (containing unit test cases)

## Deployment

- Pushed the project to GitHub

## GitHub Actions Setup

### Workflow Configuration
1. Created `.github/workflows/` directory
2. Added `python-app.yml` file with CI/CD configuration
3. Configured automated unit tests to run on every push

### Automation
- Unit tests now run automatically whenever changes are pushed to the repository
- No manual testing required after commit

## How It Works

Each time you push code to GitHub:
1. GitHub Actions automatically triggers the workflow
2. The defined Python tests execute
3. Results are logged in the Actions tab
