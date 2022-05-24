from ..repositories.productRepository import ProductRepository

class ProductService:
    def __init__(self):
        self.productRepository = ProductRepository()

    def listProducts(self):
        return self.productRepository.listProduct()

    def addProduct(self, product):
        return self.productRepository.addProduct(product)

    def updateService(self, id, product):
        return self.productRepository.updateProduct(id, product)

    def getById(self, id):
        return self.productRepository.getById(id)

    def deleteService(self, id):
        return self.productRepository.deleteProduct(id)