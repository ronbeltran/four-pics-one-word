import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'Wordsapi'

from game import utils


class Word(messages.Message):
    word = messages.StringField(1)
    frequency = messages.StringField(2)


class Words(messages.Message):
    words = messages.MessageField(Word, 1, repeated=True)


WORDS_CRITERIA_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    length=messages.IntegerField(1, variant=messages.Variant.INT32, required=True),  # noqa
    choices=messages.StringField(2, required=True)
)

WEB_CLIENT_ID = '471311115005-4bd8aqpnmrnro61ntdgstb2bsbvhma90.apps.googleusercontent.com'  # noqa
ANDROID_CLIENT_ID = ''
IOS_CLIENT_ID = ''
ANDROID_AUDIENCE = WEB_CLIENT_ID


@endpoints.api(name='wordsapi', version='v1',
               allowed_client_ids=[WEB_CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID],  # noqa
               audiences=[ANDROID_AUDIENCE],)
class WordsApi(remote.Service):

    @endpoints.method(WORDS_CRITERIA_RESOURCE, Words,
                      path='words/{length}/{choices}', http_method='POST',
                      name='words.get')
    def get_words(self, request):
        words = utils.get_words(request.length, request.choices.upper())
        return Words(words=[Word(word=w, frequency=str(utils.WORDS.get(w))) for w in words])  # noqa


app = endpoints.api_server([WordsApi])
