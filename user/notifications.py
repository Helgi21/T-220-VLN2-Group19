from django.contrib.auth import get_user_model
from user import models
User = get_user_model()


class Notification:
    def __init__(self, title: str, text: str, user, link: str):
        """
        Creates a notification stored in the database that is displayed in the navbar

        :param title: String that will be displayed as the notification title (max-length: 150)
        :param text:  String that will be displayed as the notification body (max-length: 255)
        :param user:  User object that will receive the notification
        :param link:  Link to where the notification should redirect to (max-length: 255)
        """
        self.title = title
        self.text = text
        self.user = user
        self.link = link
        self.create_notification()

    def create_notification(self):
        if self.validate_data():
            notif = models.Notification()
            notif.title = self.title
            notif.text = self.text
            notif.user = self.user
            notif.onclick_link = self.link
            notif.save()
        else:
            raise TypeError("invalid data")

    def validate_data(self) -> bool:
        """ True if valid, False if not """
        if len(self.title) > 150 or len(self.text) > 255 or len(self.link) > 255:
            return False
        return True

