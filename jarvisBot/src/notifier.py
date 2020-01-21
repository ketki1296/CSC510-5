from init import get_driver
from mattermostdriver.exceptions import ResourceNotFound


class Notifier:
    def __init__(self):
        self.client = get_driver()
        self.client.login()
        self.user_id = self.client.users.get_user_by_username("jarvisbot")["id"]

    def notify(self, message, email):
        c_id = self.get_direct_channel_id(email)
        if c_id is None:
            print("Failed to send message to " + email)
            return

        self.client.posts.create_post(options={
            'channel_id': c_id,
            'message': message});

    def get_direct_channel_id(self, email):
        c_name = self.client.users.get_user_by_email(email)["id"] + "__" + self.user_id
        try:
            channel_id = \
                self.client.channels.get_channel_by_name(self.client.teams.get_team_by_name("se501")["id"],
                                                         c_name)[ "id"]
        except ResourceNotFound:
            c_name = self.user_id + "__" + self.client.users.get_user_by_email(email)["id"]
            try:
                channel_id = \
                    self.client.channels.get_channel_by_name(self.client.teams.get_team_by_name("se501")["id"],
                                                             c_name)["id"]
            except ResourceNotFound:
                return None
        return channel_id
