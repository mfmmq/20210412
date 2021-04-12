""" Todo Service Implementation 

    Depends on todo.proto, build it with:

    >>> python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. todo.proto
"""

from concurrent import futures

import uuid

import grpc
from google.protobuf import empty_pb2

import todo_pb2
import todo_pb2_grpc


# Todo list storage
todo_items = None


class MyTodoServicer(todo_pb2_grpc.TodoServicer):
    """ Todo service implementation """

    def __init__(self):
        super().__init__()

    def CreateItem(self, request, context):
        """ Create an item at the end of a todo list """
        print(f'Received a todo item: "{request.action}"')
        request.id = str(uuid.uuid4()).split('-')[-1]
        # Save in in-memory storage
        # UNIMPLEMENTED
        return empty_pb2.Empty()

    def UpdateItem(self, request, context):
        """ Update an item's metadata and order """
        print('UpdateItem')
        print(request)
        # UNIMPLEMENTED
        return empty_pb2.Empty()

    def GetList(self, request, context):
        """ Return all the items in the to-do list in order"""
        return todo_pb2.TodoList(
            name='My List',
            creator='Me',
            items=None # UNIMPLEMENTED
        )


def serve():
    """ Run the server. """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(MyTodoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
