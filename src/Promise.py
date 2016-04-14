PENDING, FULFILLED, REJECTED = 0, 1, 2
STATES = {PENDING: 'Pending', FULFILLED: 'Fulfilled', REJECTED: 'Rejected'}


class Promise(object):

    def __init__(self, resolver):
        if not hasattr(resolver, '__call__'):
            raise Exception('Promise Resolver object must be callable')

        self.__fulfillers = []
        self.__rejectors = []
        self.__state = PENDING

    def is_pending(self):
        return self._Promise__state == PENDING

    def is_fulfilled(self):
        return self._Promise__state == FULFILLED

    def is_rejected(self):
        return self._Promise__state == REJECTED

    def get_state(self):
        return STATES[self._Promise__state]

    def then(self, on_fulfilled=None, on_rejected=None):
        if on_fulfilled is not None:
            if not hasattr(on_fulfilled, '__call__'):
                raise Exception('Promise fulfiller object must be callable')
            self.__fulfillers.append(on_fulfilled)

        if on_rejected is not None:
            if not hasattr(on_rejected, '__call__'):
                raise Exception('Promise rejector object must be callable')
            self.__rejectors.append(on_rejected)

    def catch(self, on_rejected=None):
        if on_rejected is not None:
            if not hasattr(on_rejected, '__call__'):
                raise Exception('Promise rejector object must be callable')
            self.__rejectors.append(on_rejected)

    @staticmethod
    def reject(reason=None):
        promise = Promise(lambda res, rej: rej(reason))
        promise._Promise__state = REJECTED
        return promise

    @staticmethod
    def resolve(value=None):
        promise = Promise(lambda res, rej: res(value))
        promise._Promise__state = FULFILLED
        return promise
