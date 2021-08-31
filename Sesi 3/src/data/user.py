def get_user_transaction():
    query = """
        select username, age from user_db
    """
    
    print(query)
    return [{
        "username": "abraham",
        "age": 20
    }]

if __name__ == "__main__":
    print(get_user_transaction())