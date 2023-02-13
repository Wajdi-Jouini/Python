from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']


    # ! ALL queries are class methods
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users").query_db(query)
        print(f"Result from Database = [results]")
        all_users = []

        for row in results:
            all_users.append(cls(row))
        return all_users

        # ================ CREATE USER ================
    @classmethod
    def create_user(cls,data_dict):
        query = """
        INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), Now());

        """
        return connectToMySQL("users").query_db(query,data_dict)
