
import unittest

from sas.dataloader.loader import  Loader
from sas.dataloader.manipulations import Ring, CircularAverage, SectorPhi, get_q,reader2D_converter
 
import os.path
import numpy, math
import sas.dataloader.data_info as data_info

class Averaging(unittest.TestCase):
    """
        Test averaging manipulations on a flat distribution
    """
    def setUp(self):
        """
            Create a flat 2D distribution. All averaging results
            should return the predefined height of the distribution (1.0).
        """
        x_0  = numpy.ones([100,100])
        dx_0 = numpy.ones([100,100])
        
        self.data = data_info.Data2D(data=x_0, err_data=dx_0)
        detector = data_info.Detector()
        detector.distance = 1000.0  #mm
        detector.pixel_size.x = 1.0 #mm
        detector.pixel_size.y = 1.0 #mm
        
        # center in pixel position = (len(x_0)-1)/2
        detector.beam_center.x = (len(x_0)-1)/2 #pixel number
        detector.beam_center.y = (len(x_0)-1)/2 #pixel number
        self.data.detector.append(detector)
        
        source = data_info.Source()
        source.wavelength = 10.0 #A
        self.data.source = source
        
        # get_q(dx, dy, det_dist, wavelength) where units are mm,mm,mm,and A respectively.
        self.qmin = get_q(1.0, 1.0, detector.distance, source.wavelength)

        self.qmax = get_q(49.5, 49.5, detector.distance, source.wavelength)
        
        self.qstep = len(x_0)
        x=  numpy.linspace(start= -1*self.qmax,
                               stop= self.qmax,
                               num= self.qstep,
                               endpoint=True )  
        y = numpy.linspace(start= -1*self.qmax,
                               stop= self.qmax,
                               num= self.qstep,
                               endpoint=True )
        self.data.x_bins=x
        self.data.y_bins=y
        self.data = reader2D_converter(self.data)
            
    def test_ring_flat_distribution(self):
        """
            Test ring averaging
        """
        r = Ring(r_min=2*self.qmin, r_max=5*self.qmin, 
                 center_x=self.data.detector[0].beam_center.x, 
                 center_y=self.data.detector[0].beam_center.y)
        r.nbins_phi = 20
        
        o = r(self.data)
        for i in range(20):
            self.assertEqual(o.y[i], 1.0)
            
    def test_sectorphi_full(self):
        """
            Test sector averaging
        """
        r = SectorPhi(r_min=self.qmin, r_max=3*self.qmin, 
                      phi_min=0, phi_max=math.pi*2.0)
        r.nbins_phi = 20
        o = r(self.data)
        for i in range(7):
            self.assertEqual(o.y[i], 1.0)
            
            
    def test_sectorphi_partial(self):
        """
        """
        phi_max = math.pi * 1.5
        r = SectorPhi(r_min=self.qmin, r_max=3*self.qmin, 
                      phi_min=0, phi_max=phi_max)
        self.assertEqual(r.phi_max, phi_max)
        r.nbins_phi = 20
        o = r(self.data)
        self.assertEqual(r.phi_max, phi_max)
        for i in range(17):
            self.assertEqual(o.y[i], 1.0)
            
            

class data_info_tests(unittest.TestCase):
    
    def setUp(self):
        self.data = Loader().load('MAR07232_rest.ASC')
        
    def test_ring(self):
        """
            Test ring averaging
        """
        r = Ring(r_min=.005, r_max=.01, 
                 center_x=self.data.detector[0].beam_center.x, 
                 center_y=self.data.detector[0].beam_center.y,
                 nbins = 20)
        ##r.nbins_phi = 20
        
        o = r(self.data)
        answer = Loader().load('ring_testdata.txt')
        
        for i in range(r.nbins_phi - 1):
            self.assertAlmostEqual(o.x[i + 1], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i + 1], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i + 1], answer.dy[i], 4)
            
    def test_circularavg(self):
        """
            Test circular averaging
            The test data was not generated by IGOR.
        """
        r = CircularAverage(r_min=.00, r_max=.025, 
                 bin_width=0.0003)
        r.nbins_phi = 20
        
        o = r(self.data)

        answer = Loader().load('avg_testdata.txt')
        for i in range(r.nbins_phi):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)
            
    def test_box(self):
        """
            Test circular averaging
            The test data was not generated by IGOR.
        """
        from sas.dataloader.manipulations import Boxsum, Boxavg
        
        r = Boxsum(x_min=.01, x_max=.015, y_min=0.01, y_max=0.015)
        s, ds, npoints = r(self.data)
        self.assertAlmostEqual(s, 34.278990899999997, 4)
        self.assertAlmostEqual(ds, 7.8007981835194293, 4)
        self.assertAlmostEqual(npoints, 324.0000, 4)        
    
        r = Boxavg(x_min=.01, x_max=.015, y_min=0.01, y_max=0.015)
        s, ds = r(self.data)
        self.assertAlmostEqual(s, 0.10579935462962962, 4)
        self.assertAlmostEqual(ds, 0.024076537603455028, 4)
            
    def test_slabX(self):
        """
            Test slab in X
            The test data was not generated by IGOR.
        """
        from sas.dataloader.manipulations import SlabX
        
        r = SlabX(x_min=-.01, x_max=.01, y_min=-0.0002, y_max=0.0002, bin_width=0.0004)
        r.fold = False
        o = r(self.data)

        answer = Loader().load('slabx_testdata.txt')
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)
            
    def test_slabY(self):
        """
            Test slab in Y
            The test data was not generated by IGOR.
        """
        from sas.dataloader.manipulations import SlabY
        
        r = SlabY(x_min=.005, x_max=.01, y_min=-0.01, y_max=0.01, bin_width=0.0004)
        r.fold = False
        o = r(self.data)

        answer = Loader().load('slaby_testdata.txt')
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)
            
    def test_sectorphi_full(self):
        """
            Test sector averaging I(phi)
            When considering the whole azimuthal range (2pi), 
            the answer should be the same as ring averaging.
            The test data was not generated by IGOR.
        """
        from sas.dataloader.manipulations import SectorPhi
        import math
        
        nbins = 19
        phi_min = math.pi / (nbins + 1)
        phi_max = math.pi * 2 - phi_min
        
        r = SectorPhi(r_min=.005,
                      r_max=.01,
                      phi_min=phi_min,
                      phi_max=phi_max,
                      nbins=nbins)
        o = r(self.data)

        answer = Loader().load('ring_testdata.txt')
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)
            
    def test_sectorphi_quarter(self):
        """
            Test sector averaging I(phi)
            The test data was not generated by IGOR.
        """
        from sas.dataloader.manipulations import SectorPhi
        import math
        
        r = SectorPhi(r_min=.005, r_max=.01, phi_min=0, phi_max=math.pi/2.0)
        r.nbins_phi = 20
        o = r(self.data)

        answer = Loader().load('sectorphi_testdata.txt')
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)
            
    def test_sectorq_full(self):
        """
            Test sector averaging I(q)
            The test data was not generated by IGOR.
        """
        from sas.dataloader.manipulations import SectorQ
        import math
        
        r = SectorQ(r_min=.005, r_max=.01, phi_min=0, phi_max=math.pi/2.0)
        r.nbins_phi = 20
        o = r(self.data)

        answer = Loader().load('sectorq_testdata.txt')
        for i in range(len(o.x)):
            self.assertAlmostEqual(o.x[i], answer.x[i], 4)
            self.assertAlmostEqual(o.y[i], answer.y[i], 4)
            self.assertAlmostEqual(o.dy[i], answer.dy[i], 4)
            

if __name__ == '__main__':
    unittest.main()
