from modules_for_working.models.user_model import User, UserAddForAdmin, UserData


class UserForMongo(object):

    @staticmethod
    def create_spec_data_format_registration(user_detail: User):
        return {
            "username": user_detail.username,
            "password": user_detail.password,
            "role": 0,
            "user_data": {
                "name": user_detail.user_data.name,
                "surname": user_detail.user_data.surname,
                "old": user_detail.user_data.old
            }
        }

    @staticmethod
    def create_spec_data_format_add_admin(user_detail: UserAddForAdmin):
        return {
            "username": user_detail.username,
            "password": user_detail.password,
            "role": 0,
            "user_data": {
                "name": user_detail.user_data.name,
                "surname": user_detail.user_data.surname,
                "old": user_detail.user_data.old
            }
        }

    @staticmethod
    def create_spec_user_data(user_detail: UserData):
        return {
                "name": user_detail.name,
                "surname": user_detail.surname,
                "old": user_detail.old
            }
