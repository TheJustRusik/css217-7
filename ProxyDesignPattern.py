import logging

# Define a class for document management system proxy
class DocumentManagementProxy:
    def __init__(self, document_storage_system):
        self.document_storage_system = document_storage_system
        self.logged_in_users = set()
        self.logger = logging.getLogger(__name__)
        
    def login(self, username, password):
        # Authenticate user
        if self.authenticate(username, password):
            self.logged_in_users.add(username)
            self.logger.info(f"User '{username}' logged in.")
            return True
        else:
            self.logger.warning(f"Failed login attempt for user '{username}'.")
            return False
    
    def logout(self, username):
        # Logout user
        if username in self.logged_in_users:
            self.logged_in_users.remove(username)
            self.logger.info(f"User '{username}' logged out.")
            return True
        else:
            self.logger.warning(f"Attempt to logout non-logged in user '{username}'.")
            return False
    
    def authenticate(self, username, password):
        # Mock authentication function, replace with actual authentication logic
        return username == "admin" and password == "admin@123"
    
    def access_document(self, username, document_id):
        # Check user permission and session
        if username in self.logged_in_users:
            # Log document access
            self.logger.info(f"User '{username}' accessed document '{document_id}'.")
            return self.document_storage_system.get_document(document_id)
        else:
            self.logger.warning(f"Unauthorized access attempt by user '{username}' for document '{document_id}'.")
            return None
    
    def search_documents(self, query):
        # Search documents
        self.logger.info(f"User searched for '{query}'.")
        return self.document_storage_system.search_documents(query)


# Mock document storage system
class DocumentStorageSystem:
    def __init__(self):
        self.documents = {}
        
    def add_document(self, document_id, content):
        self.documents[document_id] = content
        
    def get_document(self, document_id):
        return self.documents.get(document_id)
    
    def search_documents(self, query):
        # Mock search function, replace with actual search logic
        return [doc_id for doc_id in self.documents if query in self.documents[doc_id]]


# Example usage
if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    
    # Create document storage system
    storage_system = DocumentStorageSystem()
    storage_system.add_document("doc1", "Sample document content")
    storage_system.add_document("doc2", "Another document content")
    
    # Create document management proxy
    proxy = DocumentManagementProxy(storage_system)
    
    # User login
    proxy.login("admin", "admin@123")
    
    # Access document
    doc_content = proxy.access_document("admin", "doc1")
    print(doc_content)
    
    # Search documents
    search_results = proxy.search_documents("sample")
    print(search_results)
    
    # User logout
    proxy.logout("admin")
