from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE 
from flask_app.models.ninja import Ninja
class Dojo:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.dojo_name = data_dict['dojo_name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.ninjas_list = []

# READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(f"Result from Database = {results}")
        all_dojos = []
        for row in results:
            all_dojos.append(cls(row))
        return all_dojos

            # CREATE ONE DOJO
    @classmethod
    def create_dojo(cls, data_dict):
        query = """
        INSERT INTO dojos (dojo_name) VALUES (%(dojo_name)s);
        """
        # ! THIS METHOD RETURN THE ID OF NEW CREATED DOJO
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        print(f"this is the result after insert one Dojo:{result}")
        return result

    # READ ONE DOJO
    @classmethod
    def get_one(cls, data_dict):
        query = """
        SELECT * FROM dojos WHERE id  = %(id)s;
        """
        query_2 = """
        SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query_2, data_dict)
        print(results)
        ninjas = []
        if results:
            this_dojo = cls(results[0])
            for row in results:
                x = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at']
                }
                ninja=Ninja(x)
                #dojo = dojo.Dojo(x)
                ninjas.append(ninja)
            this_dojo.ninjas_list = ninjas
            return ninjas
        return []
        

        

    