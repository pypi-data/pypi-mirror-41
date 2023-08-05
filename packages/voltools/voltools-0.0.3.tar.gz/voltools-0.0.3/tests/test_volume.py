import numpy as np
import unittest
import time

import os
os.environ['PATH'] += ';' + r'C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin'

class TestVolume(unittest.TestCase):

    # def test_performance(self):
    #     from scipy import ndimage as nd
    #     import pyrr
    #
    #     t = np.random.rand(280, 920, 920).astype(np.float32)
    #     v = Volume(t, prefilter=False, interpolation='linear')
    #
    #     transform_m = pyrr.Matrix44.from_z_rotation(np.random.sample(1), dtype=np.float32)
    #
    #     time1 = time.perf_counter()
    #     cpu_res = nd.affine_transform(t, transform_m)
    #     time2 = time.perf_counter()
    #     v.transform_m(transform_m)
    #     time3 = time.perf_counter()
    #
    #     self.assertTrue(np.allclose(v.to_cpu(), cpu_res))
    #
    #     print('Scipy took {:.4f}s, PyCuda took {:.4f}s'.format(time2-time1, time3-time2))
    #     del v, t

    @classmethod
    def setUpClass(self):
        import pycuda.autoinit

        # Try to test installed first
        try:
            from voltools import Volume
            print('Testing PIP installed voltools version.')
            TestVolume.Volume = Volume
        except ImportError:
            # installed version not found, testing on local
            print('voltools not installed, testing local version.')
            import sys
            sys.path.append('..')
            from voltools import Volume
            TestVolume.Volume = Volume

        # Setup data
        TestVolume.data = np.random.rand(50, 50, 50).astype(np.float32) * 1000

    def test_create_linear(self):
        v = TestVolume.Volume(TestVolume.data, interpolation='linear')
        self.assertTrue(np.allclose(TestVolume.data, v.initial_data))

        self.assertTrue(v.interpolation == 'linear')

        # linear interpolation => no prefiltering => the data on gpu (in texture) should be same as initial
        self.assertTrue(np.allclose(TestVolume.data, v.to_cpu()))

        del v

    def test_create_bspline(self):
        v = TestVolume.Volume(TestVolume.data, prefilter=True, interpolation='bspline')
        self.assertTrue(np.allclose(TestVolume.data, v.initial_data))

        self.assertTrue(v.prefilter)
        self.assertTrue(v.interpolation == 'bspline')

        del v

    def test_create_bsplinehq(self):
        v = TestVolume.Volume(TestVolume.data, prefilter=True, interpolation='bsplinehq')
        self.assertTrue(np.allclose(TestVolume.data, v.initial_data))

        self.assertTrue(v.prefilter)
        self.assertTrue(v.interpolation == 'bsplinehq')

        del v

    # def test_transform_m(self):
    #     v = Volume(self.data, interpolation='linear')
    #
    #     del v
    #
    # def test_equality(self):
    #     pass
    #     # TODO

    # def test_prefilter_gpu(self):
    #     v = Volume(self.data, prefilter=True)
    #     self.assertTrue(v.prefilter)
    #
    #     # TODO get groundtruth prefilter data and compare it
    #
    #     del v
    #
    # def test_transform(self):
    #     v = Volume(self.data, prefilter=False)
    #     self.assertTrue(np.allclose(self.data, v.to_cpu()))
    #
    #     after_id = v.apply_transform_m(np.identity(4, np.float32)).to_cpu()
    #     self.assertTrue(np.allclose(self.data, after_id))
    #
    #     # # TODO make ground truth with nd.affine_transform
    #     #
    #     # angles = (np.random.sample(10) * 180.0) - 90.0
    #     # for a in angles:
    #     #     after_rotation = v.transform(rotation=(a, 0, 0), rotation_units='deg', rotation_order='szyx',
    #     #                                  around_center=False).to_cpu()
    #     #     after_rotation[after_rotation < 1.0] = 0
    #     #
    #     #     rotation_m = np.identity(4, dtype=np.float32)
    #     #     rotation_m[0:3, 0:3] = euler2mat(*(np.deg2rad(-1 * a), 0, 0), axes='sxyz')
    #     #
    #     #     gt = nd.affine_transform(self.data, rotation_m)
    #     #     # gt = nd.rotate(self.data, a, (1, 2), mode='constant', reshape=False, order=0, prefilter=False)
    #     #
    #     #     # plt.imshow(after_rotation[0])
    #     #     # # plt.imshow(self.data[0])
    #     #     # plt.show()
    #     #     if not np.allclose(gt, after_rotation):
    #     #         f, axarr = plt.subplots(2)
    #     #         axarr[0].imshow(gt[0])
    #     #         axarr[1].imshow(after_rotation[0])
    #     #         plt.show()
    #     #     self.assertTrue(np.allclose(gt, after_rotation))
    #
    #     del v


if __name__ == '__main__':
    unittest.main()
