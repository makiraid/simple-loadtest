# HTTP Load Testing Tool

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Using a Virtual Environment](#using-a-virtual-environment)
  - [Usage](#usage)
  - [Example](#example)
- [Contributing](#contributing)
- [License](#license)
- [Notes on the README](#notes-on-the-readme  )

## Overview

This project is a simple HTTP load testing tool written in Python. It allows users to perform concurrent HTTP requests to a specified URL, providing insights into the performance of an API. The tool supports custom configurations for request method, headers and body, making it flexible for various testing scenarios.

## Features

- Perform concurrent HTTP POST requests.
- Configurable request headers and body through a JSON file.
- Command-line interface for user-friendly interaction.
- Input validation for request counts.

## Requirements

- Python 3.1 or higher
- `aiohttp` library for asynchronous HTTP requests

## Installation

### Using a Virtual Environment

1. **Clone the Repository**

   ```bash
    git clone https://github.com/makiraid/simple-loadtest.git
    cd simple-loadtest
   ```

2. **Create a Virtual Environment**

    ```bash
      python3 -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On macOS and Linux:

      ```bash
        source venv/bin/activate
      ```

    - On Windows:

      ```bash
        venv\Scripts\activate
      ```

4. **Install Dependencies Install the required packages using `pip`.**

    ```bash
      pip install -r requirements.txt
    ```

5. **Create a Configuration File Create a `config.json` file in the root directory of the project with the following structure:**

    ```json
      {
        "url": "https://api.example.com/v1/users",
        "method": "GET",
        "headers": {
          "Content-Type": "application/json",
          "Authorization": "Bearer [your_token]"
        },
        "body": null
      }
    ```

### Usage

1. **Run the Load Test To run the load test, use the following command:**

    ```bash
    python main.py
    ```

2. **Input Request Count The tool will prompt you to enter the number of requests you want to send:**

    ```bash
    How many requests?
    ```

3. **Input Validation**

    - If you leave the input blank or enter an invalid number, you will receive an error message prompting you to enter a valid request count.

### Example

  ```bash
    python main.py

    How many requests? 10

    Total Requests: 10
    Successful Requests: 10
    Failed Requests: 0
    Total Duration: 0.35 seconds
    Requests per second: 28.57
  ```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you find any bugs or have suggestions for improvements.

### License

This project is licensed under the [MIT](LICENSE) License.
