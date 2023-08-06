# coding=utf-8
""" Module holding tools for creating composites """
import ee
import ee.data

if not ee.data._initialized:
    ee.Initialize()

from . import today, tools, algorithms, wrapper
from .collection import Landsat


def medoid(collection, bands=None, discard_zeros=False):
    """ Medoid Composite

    :param collection: the collection to composite
    :type collection: ee.ImageCollection
    :param bands: the bands to use for computation. The composite will include
        all bands
    :type bands: list
    :param discard_zeros: Masked and pixels with value zero will not be use
        for computation. Improves dark zones.
    :type discard_zeros: bool
    :return: the Medoid Composite
    :rtype: ee.Image
    """

    first_image = ee.Image(collection.first())
    if not bands:
        bands = first_image.bandNames()

    # Create a unique id property called 'enumeration'
    enumerated = tools.imagecollection.enumerateProperty(collection)
    collist = enumerated.toList(enumerated.size())

    def over_list(im):
        im = ee.Image(im)
        n = ee.Number(im.get('enumeration'))

        # Remove the current image from the collection
        filtered = tools.ee_list.removeIndex(collist, n)

        # Select bands for medoid
        to_process = im.select(bands)

        def over_collist(img):
            return ee.Image(img).select(bands)
        filtered = filtered.map(over_collist)

        # Compute the sum of the euclidean distance between the current image
        # and every image in the rest of the collection
        # multiply by -1 to get the lowest value in the qualityMosaic
        dist = algorithms.sum_distance(
            to_process, filtered, discard_zeros=discard_zeros).multiply(-1)
        return im.addBands(dist)

    imlist = ee.List(collist.map(over_list))

    medcol = ee.ImageCollection.fromImages(imlist)
    comp = medcol.qualityMosaic('sumdist')
    final = tools.image.removeBands(comp, ['sumdist', 'mask'])
    return final


def closest_date(collection, target_date, mask_band=None, property_name=None,
                 clip_to_first=False, limit=50):
    """ Get the image closest to the given date, and fill masked values in
    that image with values from the closest date. Images must be already
    masked. Use parameter `limit` for better speed

    :param collection: the collection with masked images
    :type collection: ee.ImageCollection
    :param target_date: the target date
    :type target_date: ee.Date or str or int
    :param mask_band: the name of the band that holds the band. CAUTION: all
        bands will be masked with this mask to avoid mixing pixels from
        different images. If None, it'll use the first band
    :type mask_band: str
    :param limit: number of image to use. Too many can throw an error, and few
        many can leave 'holes' (masked pixels)
    :type limit: int
    :param clip_to_first: if True, the resulting composite will be clipped to
        the first image footprint. Defaults to False
    :type clip_to_first: bool
    :param property_name: name of the property that will hold the 'closeness'
        to the central image (closest to passed date)
    :type property_name: str
    """
    # Merge images from a single day
    collection = tools.imagecollection.reduce_equal_interval(collection, 1)

    # HELPER
    def get_mask(img):
        """ Get a mask whether the passed image is already a mask or is a
        masked image """
        unmasked = img.unmask()
        return unmasked.divide(unmasked)

    if not mask_band:
        mask_band = ee.String(ee.Image(collection.first()).bandNames().get(0))

    if not property_name:
        property_name = 'diff_with_target_date'

    # target date
    date = ee.Date(target_date)

    # order collection
    new = collection.sort('system:time_start', True)

    # add date band
    def add_date(img):
        date_band = tools.date.get_date_band(img)
        return img.addBands(date_band)
    new = new.map(add_date)

    # assign difference to target date to each image and order the collection
    # according
    def set_diff_f(img):
        d = ee.Image(img).date()
        diff = d.difference(date, 'day').abs()
        return img.set(property_name, ee.Number(diff))

    set_diff = new.map(set_diff_f)
    ordered = set_diff.sort(property_name).limit(limit)
    ordered_list = ordered.toList(ordered.size())

    # the first image is the closest to the target date
    closest = ee.Image(ordered_list.get(0))
    rest = ee.ImageCollection(ordered_list.slice(1))

    footprint = closest.get('system:footprint')

    def fill(img, ini):
        ini = ee.Image(ini)
        # mask both ini and img
        mask_ini = get_mask(ini.select(mask_band))
        masked_ini = ini.updateMask(mask_ini)

        img = ee.Image(img)
        mask_img = get_mask(img.select(mask_band))
        masked_img = img.updateMask(mask_img)

        # mask match pixels (in ini and img)
        mask_ini_not = mask_ini.Not()
        img_not = masked_img.updateMask(mask_ini_not)

        # make masked values = 0
        zero_ini = masked_ini.unmask()
        zero_img = img_not.unmask()

        # add images
        added = zero_img.add(zero_ini)

        # update mask
        new_mask = mask_ini.add(img_not.mask())

        # final result
        if clip_to_first:
            return added.updateMask(new_mask).clip(footprint)
        else:
            return added.updateMask(new_mask)

    return ee.Image(rest.iterate(fill, closest))
