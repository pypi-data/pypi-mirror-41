# -*- coding: utf-8 -*-
# Copyright (c) 2016-2018 Braintech Sp. z o.o. [Ltd.] <http://www.braintech.pl>
# All rights reserved.

"""Module defines single :class 'TagsFileWriter' providing proxy for OpenBCI tags file."""
import xml.dom.minidom

from .. import types_utils

TAG_STYLES = {
    'gray': {
        'fill_color': '808080',
        'outline_color': '808080',
        'outline_width': '1.0',
        'outline_dash': '',
        'key_shortcut': 'Shift b',
        'marker': '0'
    },
    'red': {
        'fill_color': 'ff0000',
        'outline_color': '808080',
        'outline_width': '1.0',
        'outline_dash': '',
        'key_shortcut': 'Shift b',
        'marker': '0'
    },
    'blue': {
        'fill_color': '0017ff',
        'outline_color': '808080',
        'outline_width': '1.0',
        'outline_dash': '',
        'key_shortcut': 'Shift b',
        'marker': '0'
    },
}

TAG_DEFS = {
    # 'default': 'gray',
    # 'word': 'red',
    # 'mask2': 'blue'
}


class TagsFileWriter:
    """
    A proxy for OpenBCI tags file, that writes every next tag to file.

    Public interface:
    - tag_received(tag_dict)
    - finish_saving()
    """

    def __init__(self, p_file_path, p_defs=None
                 # p_defs = [{'name':'default',
                 #           'description':'default description'}]
                 ):
        """Prepare data structure for storing in-memory xml file."""
        self._file_path = p_file_path
        # TODO works in windows and linux on path with spaces?
        self._xml_factory = xml.dom.minidom.Document()
        # an object useful in the future to easily create xml elements
        self._xml_root = self._xml_factory.createElement(
            'tagFile')
        self._xml_root.setAttribute('formatVersion', '1.0')
        # this is going to be an in-memory representation of xml info file
        self._xml_factory.appendChild(self._xml_root)

        self._init_default_tags()
        self._init_tags_defs(p_defs)

        # create 'tags' tag structure
        l_td = self._xml_factory.createElement('tagData')
        self._xml_root.appendChild(l_td)
        self._tags_root = self._xml_factory.createElement('tags')
        l_td.appendChild(self._tags_root)

        self._tags = []

    def _init_default_tags(self):
        l_pg = self._xml_factory.createElement('paging')
        l_pg.setAttribute('page_size', '20.0')
        l_pg.setAttribute('blocks_per_page', '5')
        self._xml_root.appendChild(l_pg)

    def _init_tags_defs(self, p_defs):
        """
        Create structure.

        <tag_definitions>
           <def_group "name"="channelTags">
              <tag_item .... />
           </def_group>
        </tag_definitions>

        tag_item paramteres are taken from TAG_DEFS.
        """
        if not p_defs:
            return
        l_td = self._xml_factory.createElement('tag_definitions')
        self._xml_root.appendChild(l_td)

        l_tgr = self._xml_factory.createElement('def_group')
        l_tgr.setAttribute('name', 'channelTags')
        l_td.appendChild(l_tgr)

        for i_def in p_defs:
            l_item = self._xml_factory.createElement('tag_item')
            # Set name and description
            for i_key, i_value in i_def.items():
                l_item.setAttribute(i_key, i_value)

            # Set styles
            l_styles = TAG_STYLES[TAG_DEFS[i_def['name']]]
            for i_key, i_value in l_styles.items():
                l_item.setAttribute(i_key, i_value)
            l_tgr.appendChild(l_item)

    def tag_received(self, p_tag_dict):
        """
        For give dictionary with pirs key -> value create an xml element.

        An exception is with key 'desc' where xml elements are created for
        every element of p_tag_dict['desc'] value which is a dictionary.
        """
        self._tags.append(p_tag_dict)

    def _serialize_tags(self, p_first_sample_ts):
        """Write all self._tags to xml file."""
        for i_tag_dict in self._tags:
            l_tag_params = {}
            l_tag_params['name'] = self._get_tag_def_for(i_tag_dict['name'])
            l_tag_params['length'] = float(i_tag_dict['end_timestamp']) - \
                float(i_tag_dict['start_timestamp'])
            l_tag_params['position'] = float(i_tag_dict['start_timestamp']) - p_first_sample_ts

            l_tag = self._xml_factory.createElement('tag')
            l_tag.setAttribute('channelNumber', str(-1))

            for i_key, i_value in l_tag_params.items():
                l_tag.setAttribute(i_key, types_utils.to_string(i_value))

            for i_key, i_value in i_tag_dict['desc'].items():
                elem = self._xml_factory.createElement(i_key)
                val = self._xml_factory.createTextNode(types_utils.to_string(i_value))
                elem.appendChild(val)
                l_tag.appendChild(elem)

            self._tags_root.appendChild(l_tag)

    def _get_tag_def_for(self, p_tag_name):
        return p_tag_name

    def finish_saving(self, p_first_sample_ts):
        """Write xml tags to the file, return the file`s path."""
        # TODO - lapac bledy
        self._serialize_tags(p_first_sample_ts)

        f = open(self._file_path, 'wb')
        f.write(self._xml_factory.toprettyxml(encoding='utf-8'))
        f.close()
        return self._file_path
