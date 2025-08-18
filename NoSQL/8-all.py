#!/usr/bin/env python3

"""Module to list all documents in a MongoDB collection."""

def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
    Returns:
        List of documents, or empty list if no document is found.
    """
    return list(mongo_collection.find())
