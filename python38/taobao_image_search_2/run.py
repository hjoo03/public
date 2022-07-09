import time
import json
from lib.logger import logger
from lib.func_txy import get_dataset
from lib.func_txy import get_signature
from lib.func_txy import upload_1688_image_by_url
from lib.func_txy import upload_1688_image_by_filename


def get_1688_url_by_image_url(image_url):
    """
    :param image_url
    :return
    """

    status, data, callback = get_dataset()
    print(f"status:{status}///data:{data}///callback:{callback}")
    json_str = data.replace("{}(".format(callback), "").replace(");", '')
    data_set = json.loads(json_str).get('cbu.searchweb.config.system.currenttime', {}).get('dataSet', '')
    status, signature, policy, OSSAccessKeyId = get_signature(data_set)

    # upload image file
    status, key = upload_1688_image_by_url(image_url, signature, policy, OSSAccessKeyId)

    if status == "succ":
        url_res = 'https://s.1688.com/youyuan/index.htm?' \
                  'tab=imageSearch&imageType=oss&imageAddress={}&spm=a260k.635.3262836.d1088'.format(key)
        return url_res
    else:
        return ""


def get_1688_url_by_filename(filename):
    """
    :param filename
    :return
    """
    status, data, callback = get_dataset()
    json_str = data.replace("{}(".format(callback), "").replace(");", '')
    data_set = json.loads(json_str).get('cbu.searchweb.config.system.currenttime', {}).get('dataSet', '')
    status, signature, policy, OSSAccessKeyId = get_signature(data_set)

    # upload image file
    status, key = upload_1688_image_by_filename(filename, signature, policy, OSSAccessKeyId)

    if status == "succ":
        url_res = 'https://s.1688.com/youyuan/index.htm?' \
                  'tab=imageSearch&imageType=oss&imageAddress={}&spm=a260k.635.3262836.d1088'.format(key)
        return url_res
    else:
        return ""


def test_by_image_url(image_url=""):
    image_url = image_url or 'https://img.alicdn.com/imgextra/i4/1926017125/O1CN01ahHXLx22VITkqbuim_!!1926017125.jpg'
    t0 = time.time()
    url_res = get_1688_url_by_image_url(image_url)
    print(url_res)
    logger.info(url_res)
    t1 = time.time()
    print(t1 - t0)


def test_by_filename(filename=''):
    filename = filename or "image.jpg"
    t0 = time.time()
    url_res = get_1688_url_by_filename(filename)
    print(url_res)
    logger.info(url_res)
    t1 = time.time()
    print(t1 - t0)


if __name__ == '__main__':
    logger.info("run")
    test_by_image_url()
    test_by_filename()
    logger.info("end")
