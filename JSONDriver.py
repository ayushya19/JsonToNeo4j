
from neo4j import GraphDatabase,RoutingControl,basic_auth
from configparser import ConfigParser
from getpass import getpass
#from .neo4j_uploader import *
import sys
import json



filepath=sys.argv[1]
print(filepath)
credentials = ("bolt://localhost:7687", "neo4j", "enoughenough")

localdata = {
  "nodes":
  {
    "Person": [
      {"name": "Bob", "age": 30},
      {"name": "Jane", "age": 25}
    ]
  },
  "relationships":
  {
    "KNOWS": [
      {"_from_name": "Bob", "_to_name": "Jane", "since": 2015}
    ]
  }
}


#upload(credentials, data, node_key="name")

def main():
    #print("python main function")
    with open(filepath, "r") as jsonfile:
        datatoupload=jsonfile.read()
    upload(credentials, datatoupload, node_key="name")


if __name__ == '__main__':
    main()
# Part 3 - Python Driver
