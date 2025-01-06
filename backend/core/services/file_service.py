import datetime
import os
from uuid import uuid1


def upload_advert_photo(instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join(str(instance.categories.value),
                        str(datetime.datetime.strftime(instance.created_at, '%d_%m_%Y')),
                        f'{uuid1()}.{ext}')
