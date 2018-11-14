from mycroft import MycroftSkill, intent_file_handler


class KathyMskTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.msk.kathy.intent')
    def handle_test_msk_kathy(self, message):
        self.speak_dialog('test.msk.kathy')


def create_skill():
    return KathyMskTest()

