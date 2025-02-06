from .database import load_database, get_image, get_field

def retrieve(chinese_character: str, field: str, reading: str = None):
    '''
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
    If field is 'images', the return value is a list of tuples (style, image). The style is the style of the image and the image is a numpy array.
    If field is 'readings', the return value is a list of readings.
    If field is 'meanings', the return value is the dict of source and array of meanings in that source.
    If the field is not found, the return value is None.
    '''
    if not chinese_character:
        raise ValueError('Chinese character must be specified')
    if field not in ['stroke', 'radical', 'unicode', 'variants', 'nearly_similar', 'images', 'meanings', 'variations', 'readings']:
        raise ValueError(f'Invalid field: {field}')
    if field == 'images':
        image_paths = get_field(chinese_character=chinese_character, field='images_path')
        results = []
        for style, path in image_paths:
            img = get_image(path)
            results.append((style, img))
        return results
    if field == 'stroke':
        stroke = get_field(chinese_character=chinese_character, field=field)
        try:
            return int(stroke)
        except:
            return None
    if field == 'readings':
        value = get_field(chinese_character=chinese_character, field='vietnamese_meaning')
        return list(value.keys())
    if field == 'meanings':
        if reading is None:
            raise ValueError('Reading must be specified')
        value = get_field(chinese_character=chinese_character, field='vietnamese_meaning')
        value = value.get(reading, None)
        return value
    return get_field(chinese_character=chinese_character, field=field)

