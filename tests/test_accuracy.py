#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2022 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# External modules
import numpy as np
import unittest
# Internal modules
from miseval import *

#-----------------------------------------------------#
#                 Unittest: Accuracy                  #
#-----------------------------------------------------#
class TEST_IntersectionOverUnion(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # Create ground truth
        np.random.seed(1)
        self.gt_bi = np.random.randint(2, size=(32,32))
        self.gt_mc = np.random.randint(5, size=(32,32))
        # Create prediction
        np.random.seed(2)
        self.pd_bi = np.random.randint(2, size=(32,32))
        self.pd_mc = np.random.randint(5, size=(32,32))

    #-------------------------------------------------#
    #            Calculate : ACC Variant #1           #
    #-------------------------------------------------#
    def test_calc_Accuracy_Sets(self):
        # Check binary score
        score_bi = calc_Accuracy_Sets(self.gt_bi, self.pd_bi, c=1)
        self.assertTrue(isinstance(score_bi, np.float64))
        # Check multi-class score
        for i in range(5):
            score_mc = calc_Accuracy_Sets(self.gt_mc, self.pd_mc, c=i)
            self.assertTrue(isinstance(score_mc, np.float64))
        # Check existance in metric_dict
        self.assertTrue("ACC" in metric_dict)
        self.assertTrue(callable(metric_dict["ACC"]))
        self.assertTrue("Accuracy" in metric_dict)
        self.assertTrue(callable(metric_dict["Accuracy"]))
        self.assertTrue("RandIndex" in metric_dict)
        self.assertTrue(callable(metric_dict["RandIndex"]))
        self.assertTrue("RI" in metric_dict)
        self.assertTrue(callable(metric_dict["RI"]))

    #-------------------------------------------------#
    #            Calculate : ACC Variant #2           #
    #-------------------------------------------------#
    def test_calc_Accuracy_CM(self):
        # Check binary score
        score_bi = calc_Accuracy_CM(self.gt_bi, self.pd_bi, c=1)
        self.assertTrue(isinstance(score_bi, np.float64))
        self.assertTrue(score_bi == calc_Accuracy(self.gt_bi, self.pd_bi, c=1))
        # Check multi-class score
        for i in range(5):
            score_mc = calc_Accuracy_CM(self.gt_mc, self.pd_mc, c=i)
            self.assertTrue(isinstance(score_mc, np.float64))
            self.assertTrue(score_mc == calc_Accuracy(self.gt_mc, self.pd_mc, c=i))

    #-------------------------------------------------#
    #          Calculate : Balanced Accuracy          #
    #-------------------------------------------------#
    def test_calc_BalancedAccuracy(self):
        # Check binary score
        score_bi = calc_BalancedAccuracy(self.gt_bi, self.pd_bi, c=1)
        self.assertTrue(isinstance(score_bi, np.float64))
        # Check multi-class score
        for i in range(5):
            score_mc = calc_BalancedAccuracy(self.gt_mc, self.pd_mc, c=i)
            self.assertTrue(isinstance(score_mc, np.float64))
        # Check existance in metric_dict
        self.assertTrue("BACC" in metric_dict)
        self.assertTrue(callable(metric_dict["BACC"]))
        self.assertTrue("BalancedAccuracy" in metric_dict)
        self.assertTrue(callable(metric_dict["BalancedAccuracy"]))

    #-------------------------------------------------#
    #         Calculate : Adjusted Rand Index         #
    #-------------------------------------------------#
    def test_calc_AdjustedRandIndex(self):
        # Check binary score
        score_bi = calc_AdjustedRandIndex(self.gt_bi, self.pd_bi, c=1)
        self.assertTrue(isinstance(score_bi, np.float64))
        # Check multi-class score
        for i in range(5):
            score_mc = calc_AdjustedRandIndex(self.gt_mc, self.pd_mc, c=i)
            self.assertTrue(isinstance(score_mc, np.float64))
        # Check existance in metric_dict
        self.assertTrue("ARI" in metric_dict)
        self.assertTrue(callable(metric_dict["ARI"]))
        self.assertTrue("AdjustedRandIndex" in metric_dict)
        self.assertTrue(callable(metric_dict["AdjustedRandIndex"]))
