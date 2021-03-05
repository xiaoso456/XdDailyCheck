import random


class Location(object):
    random_1 = random.randrange(1, 1000) * 0.000000000001
    random_2 = random.randrange(1, 100) * 0.000001
    Q = 34.127750108507 + random_1
    R = 108.836475965712 + random_1
    Ing = 108.836476 + random_2
    lat = 34.12775 + random_2
    location_dict = {
        "sfzx": 1,
        "tw": 2,
        "area": "陕西省 西安市 长安区",
        "city": "西安市",
        "province": "陕西省",
        "address": "陕西省西安市长安区兴隆街道海棠路西安电子科技大学南校区",
        "geo_api_info":{"type":"complete","position":{"Q":Q,"R":R,"lng":Ing,"lat":lat},"location_type":"html5","message":"Get geolocation success.Convert Success.Get address success.","accuracy":30,"isConverted":True,"status":1,"addressComponent":{"citycode":"029","adcode":"610116","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"雷甘路","streetNumber":"266号","country":"中国","province":"陕西省","city":"西安市","district":"长安区","township":"兴隆街道"},"formattedAddress":"陕西省西安市长安区兴隆街道海棠路西安电子科技大学南校区","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"},
        "sfcyglq": 0,  # 是否处于隔离期
        "sfyzz": 0,  # 是否有症状
        "qtqk": None,   # 其他情况
        "ymtys": 0  # 一码通颜色
    }
