# Loducode web3

Basic components for the development of loducode s.a.s.

### install

`pip install loducode_web3==0.0.3`

## functionalities

- **Admin**
    - AttributeLAndAdmin
    - AttributeNftAdmin
    - LandAdmin
    - NftAdmin
- **Models**
    - AttributeLand
    - AttributeNft  
    - Land  
    - Nft
- **Urls Api**
    - /api/nfts/
    - /api/attributes_nft/
    - /api/lands/
    - /api/attributes_lands/
- **Views api**
    - AttributeLandViewSet
    - AttributeNftViewSet
    - LandViewSet
    - NftViewSet

## Commands

- python setup.py sdist bdist_wheel
- twine upload --repository pypi dist/loducode_web3-0.0.3*

entrar a la carpeta loducode_web3 y correr
- django-admin makemessages
- django-admin compilemessages

####Version 0.0.2
- bug imports

####Version 0.0.1
- first version
