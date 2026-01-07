from fastapi import HTTPException

from app.skins.dao import SkinsDao


class SkinsService:


    @classmethod
    async  def get_by_id_or_404(cls, model_id:int):
        result = await  SkinsDao.find_by_id(model_id)
        if not result:
            raise  HTTPException(status_code=404, detail="skin not found")
        return result


    @classmethod
    async def get_all_skins(cls):
        return  await SkinsDao.get_all()