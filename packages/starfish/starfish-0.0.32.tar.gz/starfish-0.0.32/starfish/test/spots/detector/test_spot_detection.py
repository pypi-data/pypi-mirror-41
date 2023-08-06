import numpy as np
import pytest
from scipy.ndimage.filters import gaussian_filter

from starfish.imagestack.imagestack import ImageStack
from starfish.spots._detector._base import SpotFinderAlgorithmBase
from starfish.spots._detector.blob import BlobDetector
from starfish.spots._detector.detect import detect_spots
from starfish.spots._detector.local_max_peak_finder import LocalMaxPeakFinder
from starfish.spots._detector.trackpy_local_max_peak_finder import TrackpyLocalMaxPeakFinder
from starfish.types import Axes


def simple_gaussian_spot_detector() -> BlobDetector:
    """create a basic gaussian spot detector"""
    return BlobDetector(min_sigma=1, max_sigma=4, num_sigma=5, threshold=0, measurement_type='max')


def simple_trackpy_local_max_spot_detector() -> TrackpyLocalMaxPeakFinder:
    """create a basic local max peak finder"""
    return TrackpyLocalMaxPeakFinder(
        spot_diameter=3,
        min_mass=0.01,
        max_size=10,
        separation=2,
    )


def simple_local_max_spot_detector() -> LocalMaxPeakFinder:
    return LocalMaxPeakFinder(
        min_distance=6,
        stringency=0,
        min_obj_area=0,
        max_obj_area=np.inf,
        threshold=0
    )


# initialize spot detectors
gaussian_spot_detector = simple_gaussian_spot_detector()
trackpy_local_max_spot_detector = simple_trackpy_local_max_spot_detector()
local_max_spot_detector = simple_local_max_spot_detector()


def synthetic_two_spot_3d_2round_2ch() -> ImageStack:
    """produce a 2-channel 2-round ImageStack

    Notes
    -----
    - After Gaussian filtering, all max intensities are 7
    - Two spots are located at (4, 10, 90) and (6, 90, 10)
    - Both spots are 1-hot, and decode to:
        - spot 1: (round 0, ch 0), (round 1, ch 1)
        - spot 2: (round 0, ch 1), (round 1, ch 0)

    Returns
    -------
    ImageStack :
        noiseless ImageStack containing two spots

    """

    # blank data_image
    data = np.zeros((2, 2, 10, 100, 100), dtype=np.float32)

    # round 0 channel 0
    data[0, 0, 4, 10, 90] = 1.0
    data[0, 0, 5, 90, 10] = 0

    # round 0 channel 1
    data[0, 1, 4, 10, 90] = 0
    data[0, 1, 5, 90, 10] = 1.0

    # round 1 channel 0
    data[1, 0, 4, 10, 90] = 0
    data[1, 0, 5, 90, 10] = 1.0

    # round 1 channel 1
    data[1, 1, 4, 10, 90] = 1.0
    data[1, 1, 5, 90, 10] = 0

    data = gaussian_filter(data, sigma=(0, 0, 2, 2, 2))
    return ImageStack.from_numpy_array(data)


# create the data_stack
data_stack = synthetic_two_spot_3d_2round_2ch()


@pytest.mark.parametrize('data_stack, spot_detector, radius_is_gyration', [
    (data_stack, gaussian_spot_detector, False),
    (data_stack, trackpy_local_max_spot_detector, True),
    (data_stack, local_max_spot_detector, False)
])
def test_spot_detection_with_reference_image(
        data_stack: ImageStack,
        spot_detector: SpotFinderAlgorithmBase,
        radius_is_gyration: bool,
):
    """
    This testing method uses a reference image to identify spot locations. Thus, it should detect
    two spots, each with max intensity 7. Because the channels and rounds are aggregated, this
    method should recognize the 1-hot code used in the testing data, and see one channel "on" per
    round. Thus, the total intensity across all channels and round for each spot should be 14.

    """
    reference_image_mp = data_stack.max_proj(Axes.CH, Axes.ROUND)
    reference_image_mp_numpy = reference_image_mp._squeezed_numpy(Axes.CH, Axes.ROUND)

    intensity_table = detect_spots(data_stack=data_stack,
                                   spot_finding_method=spot_detector.image_to_spots,
                                   reference_image=reference_image_mp_numpy,
                                   measurement_function=np.max,
                                   radius_is_gyration=radius_is_gyration)
    assert intensity_table.shape == (2, 2, 2), "wrong number of spots detected"
    expected = [0.01587425, 0.01587425]
    assert np.allclose(intensity_table.sum((Axes.ROUND, Axes.CH)).values, expected), \
        "wrong spot intensities detected"


@pytest.mark.parametrize('data_stack, spot_detector, radius_is_gyration', [
    (data_stack, gaussian_spot_detector, False),
    (data_stack, trackpy_local_max_spot_detector, True),
    (data_stack, local_max_spot_detector, False)
])
def test_spot_detection_with_reference_image_from_max_projection(
        data_stack: ImageStack,
        spot_detector: SpotFinderAlgorithmBase,
        radius_is_gyration: bool,
):
    """
    This testing method builds a reference image to identify spot locations. Thus, it should detect
    two spots, each with max intensity 7. Because the channels and rounds are aggregated, this
    method should recognize the 1-hot code used in the testing data, and see one channel "on" per
    round. Thus, the total intensity across all channels and round for each spot should be 14.
    """
    intensity_table = detect_spots(data_stack=data_stack,
                                   spot_finding_method=spot_detector.image_to_spots,
                                   reference_image_from_max_projection=True,
                                   measurement_function=np.max,
                                   radius_is_gyration=radius_is_gyration)
    assert intensity_table.shape == (2, 2, 2), "wrong number of spots detected"
    expected = [0.01587425, 0.01587425]
    assert np.allclose(intensity_table.sum((Axes.ROUND, Axes.CH)).values, expected), \
        "wrong spot intensities detected"


@pytest.mark.parametrize('data_stack, spot_detector, radius_is_gyration', [
    (data_stack, gaussian_spot_detector, False),
    (data_stack, trackpy_local_max_spot_detector, True),
    (data_stack, local_max_spot_detector, False)
])
def test_spot_finding_no_reference_image(
        data_stack: ImageStack,
        spot_detector: SpotFinderAlgorithmBase,
        radius_is_gyration: bool,
):
    """
    This testing method does not provide a reference image, and should therefore check for spots
    in each (round, ch) combination in sequence. With the given input, it should detect 4 spots,
    each with a max value of 7. Because each (round, ch) are measured sequentially, each spot only
    measures a single channel. Thus the total intensity across all rounds and channels for each
    spot should be 7.
    """
    intensity_table = detect_spots(data_stack=data_stack,
                                   spot_finding_method=spot_detector.image_to_spots,
                                   measurement_function=np.max,
                                   radius_is_gyration=radius_is_gyration,
                                   n_processes=1)
    assert intensity_table.shape == (4, 2, 2), "wrong number of spots detected"
    expected = [0.00793712] * 4
    assert np.allclose(intensity_table.sum((Axes.ROUND, Axes.CH)).values, expected), \
        "wrong spot intensities detected"
