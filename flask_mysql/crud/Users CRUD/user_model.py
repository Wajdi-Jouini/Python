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
        results = connectToMySQL("users").query_db(query,data_dict)
        print(results, "😁" *50)
        return connectToMySQL("users").query_db(query,data_dict)

    @classmethod
    def get_one(cls,data_dict):
        query = """
        SELECT * FROM users WHERE id  = %(id)s;
        """
        results = connectToMySQL("users").query_db(query,data_dict)
        print(results)
        if results:
            return cls(results[0])
        return None

    @classmethod
    def update(cls,data_dict):
        query = """
        UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;
        """
        return connectToMySQL("users").query_db(query,data_dict)

    @classmethod
    def delete(cls,data_dict):
        query = """
        DELETE FROM users WHERE id = %(id)s;
        """
        return connectToMySQL("users").query_db(query,data_dict)
