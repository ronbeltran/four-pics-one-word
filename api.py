import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


class Word(messages.Message):
    word = messages.StringField(1)


class Words(messages.Message):
    words = messages.MessageField(Word, 1, repeated=True)


WORDS_CRITERIA_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    length=messages.IntegerField(1, variant=messages.Variant.INT32, required=True),  # noqa
    choices=messages.StringField(2, required=True)
)


@endpoints.api(name='wordsapi', version='1')
class WordsApi(remote.Service):

    @endpoints.method(WORDS_CRITERIA_RESOURCE, Words,
                      path='words/{length}/{choices}', http_method='POST',
                      name='words.get')
    def get_words(self, request):
        return Words(words=[
            Word(word='HELLO'),
            Word(word='WORLD'),
        ])

app = endpoints.api_server([WordsApi])
