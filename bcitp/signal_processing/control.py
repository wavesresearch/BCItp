import math
import collections
from .approach import Approach
from bcitp.utils.standards import PATH_TO_SESSION
import os


class Controller():

    def __init__(self, smanager, sessionheader):

        self.sh = sessionheader
        self.ap = self.load_approach()
        self.sm = smanager

        self.clear_states()

    def clear_states(self):
        self.U = 0

    def get_probs(self):

        t, buf = self.sm.GetBuffData()

        # if buf.shape[0] == self.sh.dp.buf_len:
        p = self.ap.classify_epoch(buf.T, 'prob')[0]
        return p

    def update_cumulative(self, p):

        if p is None:
            return

        p1 = p[0]
        p2 = p[1]

        u = p1 - p2

        self.U += u

        return self.U

    def generate_cmd(self):

        p = self.get_probs()
        U = self.update_cumulative(p)

        U1 = 100 * (U + self.sh.game.game_threshold) / \
            (2. * self.sh.game.game_threshold)

        U2 = 100 - U1

        if U1 > 100:
            cmd = 1
        elif U2 > 100:
            cmd = 2
        else:
            cmd = 0

        return cmd, [U1, U2], p

    def load_approach(self):

        ap = Approach()
        ap.load_pkl(PATH_TO_SESSION + self.sh.info.name)

        return ap
