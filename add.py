""" Add an item to the list """
import grpc

import todo_pb2
import todo_pb2_grpc


def add_item(action):
    channel = grpc.insecure_channel('localhost:50051')
    stub = todo_pb2_grpc.TodoStub(channel)
    stub.CreateItem(todo_pb2.TodoItem(
        action=action,
        is_complete=False
    ))


if __name__ == '__main__':
    add_item('Create a todo item')
