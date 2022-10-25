
import io
from typing import Tuple

from PIL import Image

Size = Tuple[int, int]

WATERMARK_FILENAME = "watermark.png"

class ImagePostprocessor:

    def __init__(self) -> None:
        self.watermark = Image.open(WATERMARK_FILENAME)

    def __get_watermark_size(self, size: Size) -> Size:
        width_or_height = int(size[0] > size[1])

        factor = size[width_or_height] / self.watermark.size[width_or_height]

        return tuple(int(self.watermark.size[i] * factor) for i in range(len(self.watermark)))


    def __get_watermark_position(self, img_size: Size, wm_size: Size) -> Size:
        pos = [0, 0]
        for i in range(len(pos)):
            if wm_size[i] < img_size[i]:
                pos[i] = int((img_size[i] - wm_size[i]) // 2)
        return tuple(pos)

    def add_watermark(
        self,
        raw_image: bytes,
        keep_proportions: bool = True
    ) -> bytes:
        image = Image.open(io.BytesIO(raw_image))

        size = (image.width, image.height)
        position = (0, 0)

        if keep_proportions:
            size = self.__get_watermark_size(image.size)
            position = self.__get_watermark_position(image.size, size)

        resized_watermark = self.watermark.resize(size=size)
        image.paste(
            im=resized_watermark,
            box=position,
            mask=resized_watermark
        )

        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=image.format)

        return img_byte_arr.getvalue()
