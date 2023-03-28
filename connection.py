# encoding: utf-8
# Revisión 2019 (a Python 3 y base64): Pablo Ventura
# Copyright 2014 Carlos Bederián
# $Id: connection.py 455 2011-05-01 00:32:09Z carlos $

import socket
from constants import *
from base64 import b64encode

class Connection(object):
    """
    Conexión punto a punto entre el servidor y un cliente.
    Se encarga de satisfacer los pedidos del cliente hasta
    que termina la conexión.
    """

    def __init__(self, socket: socket.socket, directory: str):
        # FALTA: Inicializar atributos de Connection
        self.socket = socket
        self.directory = directory
        pass

    def handle(self):
        while True:
            comando: bytes = b"";
            while True:
                # TODO: leer hasta que llegue la secuencia de terminacion del comando
                # recibir un byte
                char = self.socket.recv(1)
                comando += char
            # TODO: parsear comando y ejecutar la funcion pertinente
            # (la idea es tener una funcion por comando)
            # Si el comando es quit salimos del loop

        self.socket.close()

    # TODO: handlers de cada comando
    def get_file_listing(self):
        pass
    def get_metadata(self, filename: bytes):
        pass
    def get_slice(self, filename: bytes, offset: int, size: int):
        pass
    def quit(self):
        pass
