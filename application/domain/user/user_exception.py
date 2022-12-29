class UserNotFoundError(Exception):
    message = "El usuario especificado no existe."

    def __str__(self):
        return UserNotFoundError.message


class UsersNotFoundError(Exception):
    message = "No se han encontrado usuarios."

    def __str__(self):
        return UsersNotFoundError.message

