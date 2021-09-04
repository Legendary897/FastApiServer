from bson import ObjectId, errors
from fastapi import HTTPException


class TryReformatId(object):

    @staticmethod
    def reformat_id(_id):
        try:
            return ObjectId(_id)
        except errors.InvalidId:
            raise HTTPException(status_code=400, detail='Invalid id')