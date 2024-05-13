#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    nginx = client.logs.nginx
    print(nginx.count_documents({}), "logs")
    print("Methods:")
    print("\tmethod GET:", nginx.count_documents({"method": "GET"}))
    print("\tmethod POST:", nginx.count_documents({"method": "POST"}))
    print("\tmethod PUT:", nginx.count_documents({"method": "PUT"}))
    print("\tmethod PATCH:", nginx.count_documents({"method": "PATCH"}))
    print("\tmethod DELETE:", nginx.count_documents({"method": "DELETE"}))
    print(nginx.count_documents({"method": "GET", "path": "/status"}),
          "status check")
    