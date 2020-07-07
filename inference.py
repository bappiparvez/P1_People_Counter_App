#!/usr/bin/env python3
"""
 Copyright (c) 2018 Intel Corporation.
 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit persons to whom the Software is furnished to do so, subject to
 the following conditions:
 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import sys
import logging as log
from openvino.inference_engine import IENetwork, IECore

class Network:
    """
    Load and configure inference plugins for the specified target devices 
    and performs synchronous and asynchronous modes for the specified infer requests.
    """

    def __init__(self):
        ### TODO: Initialize any class variables desired ###
        self.network = None
        self.plugin = None
        self.output_blob = None
        self.input_blob = None
        self.infer_request = None
        self.exec_network = None
        

    def load_model(self, model,device="CPU", cpu_extension=None): 
        
        # Initialize the plugin //Creating Inference Engine
        self.plugin = IECore()
        
        ### TODO: Load the model ###
        model_xml = model
        model_bin = os.path.splitext(model_xml)[0] + ".bin"
        
        # Read the IR as a IENetwork
        log.info("Loading network files:\n\t{}\n\t{}".format(model_xml, model_bin))
        self.network = IENetwork(model=model_xml, weights=model_bin)
        
        ### TODO: Add any necessary extensions ###
        if cpu_extension and "CPU" in device:
            self.plugin.add_extension(cpu_extension, device)
        
        ### TODO: Check for supported layers ###
        # Get the supported layers of the network
        supported_layers = self.plugin.query_network(network=self.network, device_name=device)

        # Check for any unsupported layers, and let the user know if anything is missing. Exit           the program, if so.
        unsupported_layers = [l for l in self.network.layers.keys() if l not in supported_layers]
        if len(unsupported_layers) != 0:
            log.error("Following layers are not supported by the plugin for specified device {}:\n {}".format(device, ', '.join(unsupported_layers)))
            log.error("Please try to specify cpu extensions library path in sample's command line parameters using -l or --cpu_extension command line argument")
            sys.exit(1)
        
        ### TODO: Return the loaded inference plugin ###
        self.exec_network = self.plugin.load_network(self.network, device)
        
        # Get the input layer
        self.input_blob = next(iter(self.network.inputs))
        self.output_blob = next(iter(self.network.outputs))

        ### Note: You may need to update the function parameters. ###
        return 

    def get_input_shape(self):
        ### TODO: Return the shape of the input layer ###
        return self.network.inputs[self.input_blob].shape

    def exec_net(self,image):
        ### TODO: Start an asynchronous request ###
        self.exec_network.start_async(request_id=0, inputs={self.input_blob: image})
    
        ### TODO: Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        return

    def wait(self):
        ### TODO: Wait for the request to be complete. ###
        
        ### TODO: Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        return self.exec_network.requests[0].wait(-1)

    def get_output(self):
        ### TODO: Extract and return the output results
        
        ### Note: You may need to update the function parameters. ###
        return self.exec_network.requests[0].outputs[self.output_blob]