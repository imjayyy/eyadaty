import pymongo, os, json, bson, bson.json_util
# from bson.json_util import loads, dumps

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["Eyadaty"]
profiledoctortabibook_news = mydb['profiledoctortabibook_news']



path = 'Eyadaty_data\profiledoc_db\profiledoctortabibook_news'


to_convert = [path, path]

for i in to_convert:

    INPUTF = i + ".bson"
    OUTPUTF = i + ".json"

    input_file = open(INPUTF, 'rb')
    output_file = open(OUTPUTF, 'w')

    raw = (input_file.read())
    datas = bson.decode_all(raw)
    # json.dump(datas, output_file)
    a = json.loads(bson.json_util.dumps(datas))
    json.dump(a, output_file)

    # profiledoctortabibook_news.insert_many(a)
    print('finished')
# for folder in listt:
#     path_ = "Eyadaty_data/" + folder
#     if folder.endswith('.json'):
#         f = open(path_)
#         data = json.load(f, encoding="UTF-8")
#         collection = mydb[folder]
#         collection.insert_many(data)
#     else:
#         print( os.listdir(path_) )
