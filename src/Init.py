class Init:
    def __init__(self, disk_c, current_dir, product, version):
        self.wine_disk_c_dir = disk_c
        self.adobe_dir = current_dir
        self.adobe_products = product
        self.adobe_version = version

        self.ADOBE_PRODUCTS = {
            'Adobe Premiere Pro': {},
            'Adobe After Effects': {},
            'Adobe Photoshop': {},
            'Adobe Illustrator': {},
            'Adobe Audition': {},
        }

    def get_disk_c_path(self):
        return self.wine_disk_c_dir

    def get_adobe_path(self):
        return self.adobe_dir

    def get_product(self):
        return list(self.ADOBE_PRODUCTS.keys())

    def get_product_at(self, index):
        return list(self.ADOBE_PRODUCTS.keys())[index]

    def get_product_info(self, product_name, version=None):
        if product_name not in self.ADOBE_PRODUCTS:
            return None
        # Version dynamique ✅
        v = version if version else self.adobe_version[0]
        return {
            'install_dir': f'{product_name} {v}'
        }

    def get_version(self):
        return self.adobe_version