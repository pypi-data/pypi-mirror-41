# Map Dictionary Keys

## Installation

```pip install map-dictionary-keys```

## Usage 

```python
from map_dictionary_keys import map_dictionary_keys

d = {
    'some_key_to_map': 'value'
}


def some_mapping_function(key_name):
    return key_name.upper()

mapped_dictionary = map_dictionary_keys(d, some_mapping_function)
```

In the above example, `mapped_dictionary` will be mapped according to the function `some_mapping_function` as follows:

```python
mapped_dictionary = {
    'SOME_KEY_TO_MAP': 'value'
}
``` 


This function _will_ work for all levels of nested dictionaries. In the following example, both `'sub_dictionary'` and `'key_name'` will be converted as per the mapping function passed to `map_dictionary_keys`. 

```python
dictionary = {
    'sub_dictionary': {
        'key_name': 'value'
    }
}
```

It _will_ also work for nested lists of dictionaries. For example, in the following example, `'key_name'` will be mapped according to the mapping function provided to `map_dictionary_keys`.  

```python
dictionary = {
    'list_of_dictionaries': [
        {
            'key_name': 'value'
        }
    ]
}
```

This function does not currently work for lists nested beyond the first level. For example, in the following example, `'key_name'` will _not_ be mapped according to the mapping function provided to `map_dictionary_keys`. 

```python
dictionary = {
    'my_list': [
        [
            {
                'key_name': 'value'
            }
        ]
    ]
}
```