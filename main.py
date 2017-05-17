import codecs
from sets import Set
from hazm import Normalizer


nmz = Normalizer()
stops = "\n".join(
    sorted(
        list(
            Set(
                [
                    nmz.normalize(w) for w in codecs.open('persian', encoding='utf-8').read().split('\n') if w
                ]
            )
        )
    )
)
print stops

codecs.open('out', 'w', encoding='utf-8').write(stops)
