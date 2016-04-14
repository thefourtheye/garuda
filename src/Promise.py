PENDING, FULFILLED, REJECTED = 0, 1, 2
STATES = {PENDING: 'Pending', FULFILLED: 'Fulfilled', REJECTED: 'Rejected'}


class Promise(object):

    def __init__(self, resolver):
        if not hasattr(resolver, '__call__'):
            raise Exception('Promise Resolver object must be callable')

        self.__fulfillers = []
        self.__rejectors = []
        self.__state = PENDING

    def isPending(self):
        return self._Promise__state == PENDING

    def isFulfilled(self):
        return self._Promise__state == FULFILLED

    def isRejected(self):
        return self._Promise__state == REJECTED

    def getState(self):
        return STATES[self._Promise__state]

    def then(self, onFulfilled=None, onRejected=None):
        if onFulfilled is not None:
            if not hasattr(onFulfilled, '__call__'):
                raise Exception('Promise fulfiller object must be callable')
            self.__fulfillers.append(onFulfilled)

        if onRejected is not None:
            if not hasattr(onRejected, '__call__'):
                raise Exception('Promise rejector object must be callable')
            self.__rejectors.append(onRejected)

    def catch(self, onRejected=None):
        if onRejected is not None:
            if not hasattr(onRejected, '__call__'):
                raise Exception('Promise rejector object must be callable')
            self.__rejectors.append(onRejected)

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
