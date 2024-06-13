# Survey 2024

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Poetry](https://img.shields.io/badge/Poetry-1.1.12+-green.svg)

This project is a Streamlit application for conducting the 2024 digitalization survey of Italian municipalities. The survey aims to investigate specific aspects of the informatization and digitalization of municipalities.

## Table of Contents

- [Streamlit Survey 2024](#streamlit-survey-2024)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- **Interactive Survey**: A comprehensive and interactive survey for municipalities.
- **Conditional Questions**: Displays questions based on previous answers.
- **Streamlit Integration**: Utilizes Streamlit for a user-friendly web interface.
- **Poetry Dependency Management**: Simplified dependency management and virtual environment setup with Poetry.

## Installation

### Prerequisites

- Python 3.8 or higher
- Poetry 1.1.12 or higher

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/my-streamlit-survey.git
    cd my-streamlit-survey
    ```

2. **Install dependencies**:

    ```bash
    poetry install
    ```

3. **Activate the virtual environment**:

    ```bash
    poetry shell
    ```

## Usage

To run the Streamlit application, use the following command:

```bash
streamlit run survey.py
