# Neo4j Uploader with Customizable JSON Model

This project provides a customized version of neo4j-uploader that enables importing data from JSON files into a Neo4j graph database. It offers improved flexibility by allowing:

Customizable Node and Relationship Names: You can define the names used for nodes and relationships within your JSON data, making it adaptable to your specific graph model.
Convertible List Values: The uploader handles cases where node or relationship properties are represented as lists within the JSON. It automatically converts these lists into dictionaries, ensuring compatibility with the expected Neo4j data format.
## Installation

Create a conda environment:

```
conda create -n neo4j_upload python=3.x  # Replace with your desired Python version
conda activate neo4j_upload
```
Use code with caution.
content_copy
Start Neo4j:

Follow the official instructions for starting your Neo4j instance (https://neo4j.com/download/).
Install required libraries:

Bash
```pip install graph-core neo4j  # Replace with specific graph and neo4j library versions if needed
pip install <other_library_for_json_upload>  # Replace with the actual library name
```
Use code with caution.
content_copy
Reset Neo4j password (if necessary):

Refer to the Neo4j documentation for resetting the password (https://neo4j.com/docs/operations-manual/current/configuration/set-initial-password/).
Enable APOC Import (optional):

In your Neo4j settings, set apoc.import.file.enabled=true.
## Usage

Prepare your JSON data:

Structure your JSON data with two keys: nodes and links.
Each node and link within these keys should be dictionary objects.
Customize the node and relationship names within the JSON to match your desired graph model.
The uploader can handle list values for node and relationship properties, converting them into dictionaries automatically.
Run the uploader:

Bash
```
python your_script.py /path/to/your/data.json  # Replace with your script name and data path
```
Use code with caution.
content_copy
## Example JSON format: (Refer to https://github.com/neo4j for more details)

JSON
```
{
  "nodes": [
    {
      "id": "1",  # Your node ID
      "name": "Person A",  # Customizable node name
      "properties": {
        "age": 30,
        "city": "New York"
      }
    },
    // ... more nodes
  ],
  "links": [
    {
      "id": "123",  # Your relationship ID
      "from": "1",  # Customizable from node ID (refer to nodes section)
      "to": "2",  # Customizable to node ID (refer to nodes section)
      "type": "KNOWS",  # Customizable relationship type
      "properties": {
        "since": "2020-01-01"
      }
    },
    // ... more relationships
  ]
}
```

##Running the Script:

Open a terminal or command prompt and navigate to the directory containing your UploadJson.py script.

Bash
python UploadJson.py

Follow the prompts in the CLI to provide the necessary details for your JSON data and Neo4j connection.

Please mention the from node key you have used: from_name  (Replace with your relationships from node identifier)
Please mention the to node key you have used: to_name  (Replace with your relationships from node identifiee)
Please mention the name you have used for nodes: nodes  (Replace with the name you have used for node)
Please mention the name you have used for relationships: relationships  (Replace with the name you have used for node)
Please paste the path to json that you want to upload to the neo4j Database: /path/to/your/data.json  (Replace with the path to json)
Please mention the url of the Neo4j Database (e.g., bolt://localhost:7687): bolt://your_neo4j_host:port  (Replace with your connection details)
Please mention the name of the Neo4j Database: neo4j  (Replace if your database name is different)
Please write the password to access the database: **********  (Your password will not be displayed)
Please write the key id used for node name (leave blank if not applicable):  (Optional, enter key ID used)
