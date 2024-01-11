def update_url(dictionary: dict) -> dict:
    for key, value in dictionary.items():
        if key == "img_src" or key == "source":
            dictionary.update({key: value.unicode_string()})
    return dictionary
