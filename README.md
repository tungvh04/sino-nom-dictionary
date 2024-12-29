# sino-nom-dictionary

## Import
```python
import sino_nom_dictionary
```

## Function
```python
sino_nom_dictionary.retrieve(chinese_character:str, field:str, reading:str = None)
```
    Retrieve information of a Chinese character from the database.
    :param chinese_character: The Chinese character to retrieve information.
    :param field: The field to retrieve information. It can be one of the following:
        - 'stroke': The number of strokes of the Chinese character.
        - 'radical': The radical of the Chinese character.
        - 'images': The images of the Chinese character.
        - 'unicode': The Unicode of the Chinese character.
        - 'variants': The variants of the Chinese character.
        - 'nearly_similar': The nearly similar Chinese characters.
        - 'meanings': The meanings of the Chinese character.
        - 'variations': The variations of the Chinese character.
        - 'readings': The readings of the Chinese character.

    :param reading: The reading of the Chinese character. It is required when field is 'meanings'.

    :return: The information of the Chinese character or None if the field is not found.
    If field is 'stroke', the return value is an integer.
    If field is 'radical', the return value is the radical of the Chinese character.
    If field is 'unicode', the return value is the Unicode of the Chinese character. (U+xxxx)
    If field is 'nearly_similar', the return value is a list of nearly similar Chinese characters.
    If field is 'variants', the return value is a list of variants.
    If field is 'variations', the return value is a list of variations.
    If field is 'images', the return value is a list of numpy arrays.
    If field is 'readings', the return value is a list of readings.
    If field is 'meanings', the return value is the dict of source and array of meanings in that source.
    If the field is not found, the return value is None.

## Example
```python
import sino_nom_dictionary

chinese_character = '一'

print(sino_nom_dictionary.retrieve(chinese_character, 'stroke'))
print(sino_nom_dictionary.retrieve(chinese_character, 'radical'))
print(sino_nom_dictionary.retrieve(chinese_character, 'unicode'))
print(sino_nom_dictionary.retrieve(chinese_character, 'variants'))
print(sino_nom_dictionary.retrieve(chinese_character, 'variations'))
print(sino_nom_dictionary.retrieve(chinese_character, 'nearly_similar'))
print(sino_nom_dictionary.retrieve(chinese_character, 'readings'))
for reading in sino_nom_dictionary.retrieve(chinese_character, 'readings'):
    print(reading, sino_nom_dictionary.retrieve(chinese_character, 'meanings', reading))
```

Output
```
1
nhất 一 (+0 nét)
U+4E00
['𠤪']
['壹', '弌', '𠤪']
[]
['nhất', 'nhắt', 'nhứt']
nhất {'Từ điển phổ thông': ['1. một, 1', '2. bộ nhất'], 'Từ điển trích dẫn': ['1. (Danh) Một, là số đứng đầu các số đếm.', '2. (Danh) Họ “Nhất”.']}
nhắt {'btcn': ['lắt nhắt']}
nhứt {'gdhn': ['nhứt định (nhất định)']}
```

## Retrieve image
```python
import sino_nom_dictionary
from PIL import Image

chinese_character = '一'

images = sino_nom_dictionary.retrieve(chinese_character, 'images')

for image in images:
    img = Image.fromarray(image)
    img.show()
```

![Image 1](0.png)
![Image 2](1.png)
![Image 3](2.png)
![Image 4](3.png)
