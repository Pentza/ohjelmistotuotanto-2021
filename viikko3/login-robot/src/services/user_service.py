from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise AuthenticationError("Username is too short (3 or longer)")
        
        if not re.search('^[a-z]+$', username):
            raise AuthenticationError('Username must contain only letters from a to z')

        if len(password) < 8:
            raise AuthenticationError("Password is too short (8 or longer)")
        
        if re.search('^[a-zA-Z]+$', password):
            raise AuthenticationError('Password cant contain only letters')

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
