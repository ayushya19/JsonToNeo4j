Neo4j Uploader with Customizable JSON Model
This repository provides a customized version of the neo4j-uploader library that allows for flexible and adaptable JSON data upload to Neo4j.

Features:

Conda Environment Management: Creates a clean conda environment for isolated project dependencies.
Neo4j Integration: Starts a Neo4j instance and ensures it's running for data upload.
Library Installation: Installs essential graph and other necessary libraries for data processing within the environment.
Enhanced Neo4j Library: Includes additional libraries within Neo4j to facilitate JSON upload.
Authentication Reset: Provides a method to reset the Neo4j password for secure authentication.
apoc Extension: Enables the apoc.import.file.enabled=true setting in Neo4j's configuration for file import capabilities.
JSON Data Conversion: Utilizes the neo4j_uploader library to convert custom JSON data into a format compatible with Neo4j.
Customizable JSON Model:
Two key requirements for the JSON data: nodes and links.
Nodes can have customized property names.
Relationships (links) can have customizable from_node and to_node property names.
List-based node and relationship values are handled for flexibility.
Pydantic Model Validation: Leverages Pydantic to validate the JSON model structure, ensuring data integrity.
Modifiable Approach: Offers an alternative approach for even greater customization (details available in the code).
Installation:

Create a conda environment: Refer to the conda documentation for creating an environment (https://conda.io/activation)
Clone this repository: Use git clone https://github.com/<your-username>/<repo-name>.git
Activate the conda environment: Follow conda's activation instructions for your operating system.
Install dependencies: Run conda install -f environment.yml (replace environment.yml with the actual filename if different)
Usage:

Prepare your JSON data: Ensure it adheres to the documented structure with nodes and links keys, along with customizable properties.
Run the script: Execute the appropriate script from the scripts directory (consult the code for details).
Upload your data: The script will convert and upload your JSON data to Neo4j.
Customization:

The provided neo4j_uploader library has been customized. Refer to the code's comments for details on further modifications.
The alternative approach mentioned in the features section offers even more flexibility. Explore the code for implementation.
Important Note:

This repository is a customized version of neo4j-uploader. Please refer to the original project's documentation for additional functionalities and potential updates: https://github.com/neo4j
Contributing:

We welcome contributions to this project! Please create pull requests with clear explanations of your changes.

License:

This project is licensed under the [mention license, e.g., MIT License] (see LICENSE file for details).

Disclaimer:

While this README provides a general overview, refer to the code itself and any additional comments for specific instructions and usage details.
