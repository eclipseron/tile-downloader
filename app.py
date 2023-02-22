import urllib.request

from os import path, makedirs

IMG_PATH = path.abspath('./tmp')

def img_download(url: str, path: str):
    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        print(e)
    finally:
        print('finish')

def tile_downloader(tiles):
    
    if not path.exists(IMG_PATH):
        makedirs(IMG_PATH)
        print('creating directory')
    for tile in tiles:
        imgUrl = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'.format(x=tile[0], y=tile[1], z=tile[2])
        filename = '{x}_{y}_{z}.png'.format(x=tile[0], y=tile[1], z=tile[2])
        file_path = path.join(IMG_PATH, filename)
        
        if not path.exists(file_path):
            img_download(imgUrl, path.join(IMG_PATH, filename))
        else:
            print('file is already exists')

tiles = [[211341,136744,18], [211341,136745,18], [211340,136744,18], [211341,136743,18], [211339,136744,18]] #specify tiles [x, y, z]
tile_downloader(tiles)