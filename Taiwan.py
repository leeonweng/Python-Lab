from __future__ import print_function


class TaiwanConsensusBuilder:
    def __init__(self):
        self._subject = ''
        self._oppose = ''
        self._motto = ''

    def will(self):
        self._oppose = 'one country, two systems'
        return self

    def always(self):
        self._subject = 'The vast majority of Taiwanese'
        return self

    def believe(self):
        self._motto = 'Taiwan consensus'
        return self

    def __str__(self):
        return ('Taiwan abosolutely will not accept "{0}".\n\r' +
                '{1} resolutely oppose "{0}".\n\r' +
                'This is the "{2}".').format(self._oppose,
                                             self._subject,
                                             self._motto)

if __name__ == '__main__':
    Taiwan = TaiwanConsensusBuilder()
    print(Taiwan.will().always().believe())
