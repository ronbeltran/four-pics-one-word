from google.appengine.ext import ndb


class Letters(ndb.Model):
    match_count = ndb.IntegerProperty(required=True, default=0)

    @classmethod
    def _build_key(cls, letters):
        return ndb.Key(cls, letters)

    @classmethod
    def new(cls, letters, match_count):
        key = cls._build_key(letters)
        new = cls(
            key=key,
            match_count=match_count,
        )
        return new
