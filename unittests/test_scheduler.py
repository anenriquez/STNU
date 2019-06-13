import unittest
import json
import os
import numpy as np
from scheduler.temporal_networks.pstn import PSTN
from scheduler.scheduler import Scheduler
from scheduler.structs.task import Task


PSTN_DATA = "data/pstn_two_tasks.json"
MAX_SEED = 2 ** 31 - 1


class TestScheduler(unittest.TestCase):
    def setUp(self):
        tasks = list()
        my_dir = os.path.dirname(__file__)
        stnu_json = os.path.join(my_dir, PSTN_DATA)

        self.scheduler = Scheduler('srea')
        with open(stnu_json) as json_file:
            stnu_dict = json.load(json_file)
            self.scheduler.temporal_network = PSTN.from_dict(stnu_dict)

    def test_consistency(self):
        print("Initial PSTN:\n", self.scheduler.temporal_network)

        # Resample the contingent edges.
        # Super important!
        # pstn = self.scheduler.resample_pstn(self.pstn)
        # print("Resampled pstn:\n", pstn)

        print("Getting GUIDE...")
        alpha, guide_stn = self.scheduler.get_dispatch_graph()
        print("GUIDE")
        print(guide_stn)
        print("Alpha: ", alpha)

        expected_alpha = 0.081
        self.assertEqual(alpha, expected_alpha)

        for (i, j), constraint in sorted(guide_stn.constraints.items()):
            if i == 0 and j == 1:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 38)
                self.assertEqual(upper_bound, 39)
            if i == 0 and j == 2:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 42)
                self.assertEqual(upper_bound, 47)
            if i == 0 and j == 3:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 45)
                self.assertEqual(upper_bound, 52)
            if i == 0 and j == 4:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 91)
                self.assertEqual(upper_bound, 92)
            if i == 0 and j == 5:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 97)
                self.assertEqual(upper_bound, 102)
            if i == 0 and j == 6:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 100)
                self.assertEqual(upper_bound, 107)
            if i == 1 and j == 2:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 6)
                self.assertEqual(upper_bound, 47)
            if i == 2 and j == 3:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 4)
                self.assertEqual(upper_bound, 11)
            if i == 3 and j == 4:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 0)
                self.assertEqual(upper_bound, 49)
            if i == 4 and j == 5:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 8)
                self.assertEqual(upper_bound, 57)
            if i == 5 and j == 6:
                lower_bound = -guide_stn[j][i]['weight']
                upper_bound = guide_stn[i][j]['weight']
                self.assertEqual(lower_bound, 4)
                self.assertEqual(upper_bound, 11)


if __name__ == '__main__':
    unittest.main()
