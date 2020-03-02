def read_credentials_file():
    credentials = []
    with open('credentials.txt', 'r') as file:
        for line in file:
            credentials.append(line.strip())
    return credentials


def get_login():
    return read_credentials_file()[0].split(' = ')[1]


def get_password():
    return read_credentials_file()[1].split(' = ')[1]
