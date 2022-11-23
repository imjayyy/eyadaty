from typing import List
from typing import Any
from dataclasses import dataclass
import json
from bson import ObjectId

@dataclass
class Coordinates:
    lat: float
    lng: float

    @staticmethod
    def from_dict(obj: Any) -> 'Coordinates':
        _lat = float(obj.get("lat"))
        _lng = float(obj.get("lng"))
        return Coordinates(_lat, _lng)

@dataclass
class Id:
    oid: str

    @staticmethod
    def from_dict(obj: Any) -> 'Id':
        _oid = ObjectId(obj.get("$oid"))
        return Id(_oid)


@dataclass
class UserRecomend:
    oid: str

    @staticmethod
    def from_dict(obj: Any) -> 'UserRecomend':
        _oid = ObjectId(obj.get("$oid"))
        return UserRecomend(_oid)

@dataclass
class Service:
    ar: str
    fr: str

    @staticmethod
    def from_dict(obj: Any) -> 'Service':
        _ar = str(obj.get("ar"))
        _fr = str(obj.get("fr"))
        return Service(_ar, _fr)




@dataclass
class Repeat:
    valueEn: str
    valueFr: str
    valueAr: str
    value: str
    id: int
    checked: bool
    full: bool
    half: bool
    time_from: List[int]
    time_to: List[int]
    time_from_1: List[int]
    time_to_1: List[int]
    time_from_2: List[int]
    time_to_2: List[int]

    @staticmethod
    def from_dict(obj: Any) -> 'Repeat':
        _valueEn = str(obj.get("valueEn"))
        _valueFr = str(obj.get("valueFr"))
        _valueAr = str(obj.get("valueAr"))
        _value = str(obj.get("value"))
        _id = int(obj.get("id"))
        _checked = ''
        _full = ''
        _half = ''
        _time_from = [y for y in obj.get("time_from")]
        _time_to = [y for y in obj.get("time_to")]
        _time_from_1 = [y for y in obj.get("time_from_1")]
        _time_to_1 = [y for y in obj.get("time_to_1")]
        _time_from_2 = [y for y in obj.get("time_from_2")]
        _time_to_2 = [y for y in obj.get("time_to_2")]
        return Repeat(_valueEn, _valueFr, _valueAr, _value, _id, _checked, _full, _half, _time_from, _time_to, _time_from_1, _time_to_1, _time_from_2, _time_to_2)

@dataclass
class DoctorProfile:
    _id: Id
    note: List[object]
    speciality: List[str]
    speciality_old: List[str]
    coord: List[float]
    services: List[Service]
    repeat: List[Repeat]
    new_coord: List[float]
    isVerified: bool
    nbrView: int
    nbrLike: int
    nbrLove: int
    canbeshown: bool
    isinStorage: bool
    rating: int
    yes_recomend: int
    no_recomend: int
    total_recomend: int
    user_recomend: List[UserRecomend]
    isfirstyes: bool
    isdoneyes: bool
    departments: List[object]
    list_docs: List[object]
    mobili_range: List[object]
    pharm_type: List[object]
    pharm_size: List[object]
    pharm_relation: List[object]
    pharm_interest: List[object]
    firstname_ar: str
    lastname_ar: str
    firstname_fr: str
    lastname_fr: str
    fullname_ar: str
    fullname_fr: str
    gender: str
    birthday: str
    mobile: str
    tele: str
    secret_phone: str
    exprience: str
    clinic_name: str
    wilaya_ar: str
    baladiya_ar: str
    wilaya_fr: str
    baladiya_fr: str
    address: str
    coordinates: Coordinates
    user_image: str
    added_by: str
    type_profile: str
    type_user: str
    dateCreated: str
    __v: int
    id_wilaya: int
    id_baladiya: int
    lastUpdated: str
    address_fr: str
    bio: str
    fb_id: str
    fb_page: str
    instegrame: str
    isalways: bool
    linkedin: str
    mobile_2: str
    site: str
    wife_ar: str
    wife_fr: str

    @staticmethod
    def from_dict(obj: Any) -> 'DoctorProfile':
        __id = Id.from_dict(obj.get("_id"))
        _note = [y for y in obj.get("note")]
        _speciality = [y for y in obj.get("speciality")]
        _speciality_old = [y for y in obj.get("speciality_old")]
        _coord = [y for y in obj.get("coord")]
        _services = [y for y in obj.get("services")]
        _repeat = [y for y in obj.get("repeat")]
        _new_coord = [y for y in obj.get("new_coord")]
        _isVerified = obj.get("_isVerified")
        _nbrView = int(obj.get("nbrView"))
        _nbrLike = int(obj.get("nbrLike"))
        _nbrLove = int(obj.get("nbrLove"))
        _canbeshown = obj.get("_canbeshown")
        _isinStorage = obj.get("_isinStorage")
        _rating = int(obj.get("rating"))
        _yes_recomend = int(obj.get("yes_recomend"))
        _no_recomend = int(obj.get("no_recomend"))
        _total_recomend = int(obj.get("total_recomend"))
        _user_recomend = [y for y in obj.get("user_recomend")]
        _isfirstyes =  obj.get("_isfirstyes")
        _isdoneyes =  obj.get("_isdoneyes")
        _departments = [y for y in obj.get("departments")]
        _list_docs = [y for y in obj.get("list_docs")]
        _mobili_range = [y for y in obj.get("mobili_range")]
        _pharm_type = [y for y in obj.get("pharm_type")]
        _pharm_size = [y for y in obj.get("pharm_size")]
        _pharm_relation = [y for y in obj.get("pharm_relation")]
        _pharm_interest = [y for y in obj.get("pharm_interest")]
        _firstname_ar = str(obj.get("firstname_ar"))
        _lastname_ar = str(obj.get("lastname_ar"))
        _firstname_fr = str(obj.get("firstname_fr"))
        _lastname_fr = str(obj.get("lastname_fr"))
        _fullname_ar = str(obj.get("fullname_ar"))
        _fullname_fr = str(obj.get("fullname_fr"))
        _gender = str(obj.get("gender"))
        _birthday = str(obj.get("birthday"))
        _mobile = str(obj.get("mobile"))
        _tele = str(obj.get("tele"))
        _secret_phone = str(obj.get("secret_phone"))
        _exprience = str(obj.get("exprience"))
        _clinic_name = str(obj.get("clinic_name"))
        _wilaya_ar = str(obj.get("wilaya_ar"))
        _baladiya_ar = str(obj.get("baladiya_ar"))
        _wilaya_fr = str(obj.get("wilaya_fr"))
        _baladiya_fr = str(obj.get("baladiya_fr"))
        _address = str(obj.get("address"))
        _coordinates = Coordinates.from_dict(obj.get("coordinates"))
        _user_image = str(obj.get("user_image"))
        _added_by = str(obj.get("added_by"))
        _type_profile = str(obj.get("type_profile"))
        _type_user = str(obj.get("type_user"))
        _dateCreated = str(obj.get("dateCreated"))
        ___v = int(obj.get("__v"))
        _id_wilaya = int(obj.get("id_wilaya"))
        _id_baladiya = int(obj.get("id_baladiya"))
        _lastUpdated = str(obj.get("lastUpdated"))
        _address_fr = str(obj.get("address_fr"))
        _bio = str(obj.get("bio"))
        _fb_id = str(obj.get("fb_id"))
        _fb_page = str(obj.get("fb_page"))
        _instegrame = str(obj.get("instegrame"))
        _isalways = str(obj.get("_isalways"))
        _linkedin = str(obj.get("linkedin"))
        _mobile_2 = str(obj.get("mobile_2"))
        _site = str(obj.get("site"))
        _wife_ar = str(obj.get("wife_ar"))
        _wife_fr = str(obj.get("wife_fr"))
        return DoctorProfile(__id, _note, _speciality, _speciality_old, _coord, _services, _repeat, _new_coord, _isVerified, _nbrView, _nbrLike, _nbrLove, _canbeshown, _isinStorage, _rating, _yes_recomend, _no_recomend, _total_recomend, _user_recomend, _isfirstyes, _isdoneyes, _departments, _list_docs, _mobili_range, _pharm_type, _pharm_size, _pharm_relation, _pharm_interest, _firstname_ar, _lastname_ar, _firstname_fr, _lastname_fr, _fullname_ar, _fullname_fr, _gender, _birthday, _mobile, _tele, _secret_phone, _exprience, _clinic_name, _wilaya_ar, _baladiya_ar, _wilaya_fr, _baladiya_fr, _address, _coordinates, _user_image, _added_by, _type_profile, _type_user, _dateCreated, ___v, _id_wilaya, _id_baladiya, _lastUpdated, _address_fr, _bio, _fb_id, _fb_page, _instegrame, _isalways, _linkedin, _mobile_2, _site, _wife_ar, _wife_fr)


# jsonstring = json.loads(myjsonstring)
# DoctorProfile = DoctorProfile.from_dict(jsonstring)
