#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangfangyong'

import os
import sys
cur_path = os.path.abspath(os.path.join(os.path.dirname('__file__'), os.path.pardir))
sys.path.append(cur_path)

from example import format_data
from example import ttypes
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

__HOST = 'localhost'
__PORT = 9000


class FormatDataHandler(object):
    def do_format(self, data):
        print(data.text, data.id)
        # can do something
        return ttypes.Data(data.text.upper(), data.id)


if __name__ == '__main__':
    handler = FormatDataHandler()

    processor = format_data.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    rpcServer = TServer.TSimpleServer(processor,transport, tfactory, pfactory)

    print('Starting the rpc server at', __HOST,':', __PORT)
    rpcServer.serve()
    print('done')
