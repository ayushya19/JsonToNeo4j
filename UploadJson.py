
from configparser import ConfigParser
from getpass import getpass
from neo4j_uploaderV2 import upload
import questionary


def main():
  
  # Interactive QA to get all the relevant information.

  josnFilePath=questionary.text("Please paste the path to json tht you want to upload to the neo4j Database").ask()

  #filepath=sys.argv[1]
  
  print(josnFilePath)
  
  neo4jURI=questionary.text("Please mention the url of the Neo4j Database").ask()
  
  print(neo4jURI)
  
  databaseName=questionary.text("Please mention the name of the Neo4j Database").ask()
  
  print(databaseName)
  
  databasePassword=questionary.password("Please write the password to access the database").ask()
  
  #credentials = ("bolt://localhost:7687", "neo4j", "enoughenough")

  #credentials tuple to upload
  credentials=(neo4jURI,databaseName,databasePassword)

  #Datastream through which you can upload
  with open(josnFilePath, "r") as jsonfile:
    jsonContent=jsonfile.read()
  
  #The upload function has been taken from Json_upload library which is using its own local version
  upload(credentials, jsonContent, node_key="id")


if __name__ == '__main__':
    main()
