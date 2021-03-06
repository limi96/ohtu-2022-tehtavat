from entities.user import User
import re
from repositories.user_repository import UserRepository

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

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        if re.search("^[a-z]+$", username) is None:
            raise UserInputError("Username can only contain letters a-z")

        if len(username) < 3: 
            raise UserInputError("Username is too short")

        if len(password) < 8:
            raise UserInputError("Password is too short")

        if UserRepository.find_by_username(self._user_repository, username) is not None: 
            raise UserInputError("Username is already taken")
        
        if re.search("[^a-z]$", password) is None:
            raise UserInputError("Password must not contain only letters")
