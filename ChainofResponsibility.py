from abc import ABC, abstractmethod

# Support request class
class SupportRequest:
    def __init__(self, request_id, description, priority):
        self.request_id = request_id
        self.description = description
        self.priority = priority

# Handler interface
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

# Concrete handler for hardware issues
class HardwareHandler(Handler):
    def handle_request(self, request):
        if request.priority <= 3:
            print("Hardware team is handling request:", request.request_id)
        else:
            print("Hardware team cannot handle request:", request.request_id)
            # Pass the request to the next handler
            self.next.handle_request(request)

# Concrete handler for software issues
class SoftwareHandler(Handler):
    def handle_request(self, request):
        if request.priority <= 2:
            print("Software team is handling request:", request.request_id)
        else:
            print("Software team cannot handle request:", request.request_id)
            # Pass the request to the next handler
            self.next.handle_request(request)

# Concrete handler for network issues
class NetworkHandler(Handler):
    def handle_request(self, request):
        if request.priority <= 1:
            print("Network team is handling request:", request.request_id)
        else:
            print("Network team cannot handle request:", request.request_id)
            # Pass the request to the next handler
            self.next.handle_request(request)

# Client class that sets up the chain of responsibility
class SupportSystem:
    def __init__(self):
        self.hardware_handler = HardwareHandler()
        self.software_handler = SoftwareHandler()
        self.network_handler = NetworkHandler()

        # Set up the chain of responsibility
        self.hardware_handler.next = self.software_handler
        self.software_handler.next = self.network_handler

    def raise_request(self, request):
        # Start handling the request from the first handler in the chain
        self.hardware_handler.handle_request(request)

# Test cases
def test_support_system():
    system = SupportSystem()
    # Test hardware issue
    hardware_request = SupportRequest(1, "Hardware malfunction", 2)
    system.raise_request(hardware_request)
    
    # Test software issue
    software_request = SupportRequest(2, "Software crash", 3)
    system.raise_request(software_request)
    
    # Test network issue
    network_request = SupportRequest(3, "Network outage", 1)
    system.raise_request(network_request)

test_support_system()
