# EchoSuite

EchoSuite is a Python-based utility designed to enhance productivity on Windows systems by providing a quick switch mechanism between background and foreground tasks. This allows users to effectively manage their workflow by automating the execution of commonly used applications in a scheduled manner.

## Features

- Switch between predefined background tasks and a primary foreground task.
- Automate the launching of applications to optimize productivity.
- Simple configuration to set up tasks as needed.
- Designed specifically for Windows operating systems.

## Prerequisites

- Python 3.x installed on your Windows system.
- Access to command-line tools (e.g., `notepad.exe`, `calc.exe`, `mspaint.exe`) or any other executable that you wish to automate.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/echosuite.git
```

Navigate to the directory:

```bash
cd echosuite
```

## Usage

Edit the `echosuite.py` file to set up your desired background and foreground tasks. Example:

```python
echo_suite.add_background_task(["notepad.exe"])
echo_suite.add_background_task(["calc.exe"])
echo_suite.set_foreground_task(["mspaint.exe"])
```

Run the script:

```bash
python echosuite.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Developed by [Your Name](https://github.com/yourusername)