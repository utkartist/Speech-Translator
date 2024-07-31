# Help regarding Virtual Environment and requirement.txt file :

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Creating a Virtual Environment](#creating-a-virtual-environment)
    - [Installing Dependencies](#installing-dependencies)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)


## Setup

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- pip (Python package installer)

### Creating a Virtual Environment
To create a virtual environment, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to your project directory.
3. Run the following command to create a virtual environment:
   python -m venv myenv
   myenv can be replaced by environment name of your choice.
4. Activate the virtual environment:
   #### On Windows:
   
   myenv\Scripts\activate
   #### On macOS and Linux:
   
   myenv/bin/activate

### Installing Dependencies:

Once the virtual environment is activated, install the required packages using requirements.txt

Ensure you are in the project directory.

### Run the following command to install the dependencies:
pip install -r requirements.txt
This will install all the necessary packages listed in requirements.txt.
Installing Dependencies
Once the virtual environment is activated, install the required packages using requirements.txt:


## Usage:

### Example command to run the project:
python main.py

