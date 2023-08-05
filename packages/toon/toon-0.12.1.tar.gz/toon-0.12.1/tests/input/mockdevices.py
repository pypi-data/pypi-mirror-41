from toon.input.device import BaseDevice, make_obs
from timeit import default_timer
import ctypes
import numpy as np

Num1 = make_obs('Num1', (5,), ctypes.c_float)
Num2 = make_obs('Num2', (3, 3), ctypes.c_int)


class Dummy(BaseDevice):
    counter = 0
    t0 = default_timer()

    Num1 = Num1
    Num2 = Num2

    @property
    def foo(self):
        return 3

    def read(self):
        dat = None
        self.counter += 1
        if self.counter % 10 == 0:
            dat = np.random.randint(5, size=self.Num2.shape)
        while default_timer() - self.t0 < (1.0/self.sampling_frequency):
            pass
        self.t0 = default_timer()
        t = self.clock()
        num1 = self.Num1(t, np.random.random(self.Num1.shape))
        num2 = None
        if dat is not None:
            num2 = self.Num2(t, dat)
        return self.Returns(num1=num1,
                            num2=num2)


class SingleResp(BaseDevice):
    t0 = default_timer()
    sampling_frequency = 1000
    counter = 0

    Num1 = make_obs('Num1', (1,), int)

    def read(self):
        while default_timer() - self.t0 < (1.0/self.sampling_frequency):
            pass
        val = self.counter
        self.counter += 1
        self.t0 = default_timer()
        t = self.clock()
        return self.Num1(t, val)


class Timebomb(SingleResp):
    def read(self):
        while default_timer() - self.t0 < (1.0/self.sampling_frequency):
            pass
        val = self.counter
        self.counter += 1
        if self.counter > 10:
            raise ValueError('Broke it.')
        self.t0 = default_timer()
        t = self.clock()
        return self.Num1(t, val)


class DummyList(BaseDevice):
    counter = 0
    t0 = default_timer()

    Num1 = Num1
    Num2 = Num2

    def read(self):
        dat = None
        self.counter += 1
        if self.counter % 10 == 0:
            dat = np.random.randint(5, size=self.Num2.shape)
        while default_timer() - self.t0 < (1.0/self.sampling_frequency):
            pass
        self.t0 = default_timer()
        t = self.clock()
        num1 = self.Num1(t, np.random.random(self.Num1.shape))
        num2 = None
        if dat is not None:
            num2 = self.Num2(t, dat)
        return [self.Returns(num1=num1,
                             num2=num2),
                self.Returns(num1=num1,
                             num2=num2)]


class NoObs(BaseDevice):
    def read(self):
        pass
