# -*- coding: utf-8 -*-
# Copyright (c) 2016-2018 Braintech Sp. z o.o. [Ltd.] <http://www.braintech.pl>
# All rights reserved.

"""
Module defines single :class 'DataReadProxy'.

Author:
    Mateusz Kruszyński <mateusz.kruszynski@gmail.com>
"""
import os.path
import struct

import numpy as np

from . import signal_constants
from . import signal_exceptions
from . import signal_logging as logger

LOGGER = logger.get_logger('data_read_proxy', 'info')
SAMPLE_SIZES = signal_constants.SAMPLE_SIZES
SAMPLE_STRUCT_TYPES = signal_constants.SAMPLE_STRUCT_TYPES


class DataReadProxy:
    """Class 'DataReadProxy' reads data from file."""

    def __init__(self, p_file_path, sample_type='FLOAT'):
        """
        Initialize class and start reading from file.

        :param p_file_path: name of file containing data samples
        :param sample_type: type of data
        """
        self._file_path = p_file_path
        self._sample_size = SAMPLE_SIZES[sample_type]
        self._sample_struct_type = '<' + SAMPLE_STRUCT_TYPES[sample_type]
        self.start_reading()

    def start_reading(self):
        """Start reading from file."""
        try:
            self._data_file = open(self._file_path, 'rb')
        except IOError as e:
            LOGGER.error("An error occurred while opening the data file!")
            raise e

    def finish_reading(self):
        """Finish reading from file."""
        self._data_file.close()

    def get_all_values(self, p_channels_num=1):
        """Get all values from channel (:param. p_channel)."""
        assert (p_channels_num > 0)

        self.finish_reading()
        self.start_reading()

        f_len = float(os.path.getsize(self._file_path))
        ch_len = int((f_len / self._sample_size) / p_channels_num)

        if ch_len * self._sample_size * p_channels_num != f_len:
            LOGGER.info("Remained samples {} .Should be 0."
                        .format(f_len - ch_len * self._sample_size * p_channels_num))

        vals = np.zeros((p_channels_num, ch_len))
        k = 0
        while True:
            try:
                r = np.fromfile(self._data_file, self._sample_struct_type, p_channels_num)
            except MemoryError:
                break
            if len(r) < p_channels_num:
                break
            for i in range(p_channels_num):
                vals[i, k] = r[i]
            k += 1
        return vals

    def get_next_value(self):
        """
        Return next value from data file (as python float).

        Close data file and raise NoNextValue exception if eof.
        """
        l_raw_data = self._data_file.read(self._sample_size)
        try:
            # TODO - by now it is assumed that error means eof..
            # What if it is not eof but eg. 4-chars
            # string from the end of a broken file?
            return struct.unpack(self._sample_struct_type, l_raw_data)[0]
        except struct.error:
            raise signal_exceptions.NoNextValue()

    def get_next_values(self, p_num):
        """
        Return next p_num values from data file (as numpy array).

        Close data file and raise NoNextValue exception if eof.
        """
        # Read data from file
        # LOGGER.debug("Before reading "+str(self._sample_size*p_num)+" samples.
        # CURRENT POSITION/8 = "+str(self._data_file.tell()/8))
        l_raw_data = self._data_file.read(self._sample_size * p_num)
        # LOGGER.debug("After read. CURRENT POSITION/8 = "+str(self._data_file.tell()/8))

        # Initialize return array
        if len(l_raw_data) == self._sample_size * p_num:
            # If all data required for return array is present
            return np.frombuffer(l_raw_data, dtype=self._sample_struct_type).astype('float64')
        else:
            # Either len(l_raw_data) is 0 and its ok -> EOF
            # or len(l_raw_data) > 0 and its last len(l_raw_data) data from the file.

            LOGGER.info("Remained sample of %s length (should be zero) as required length was %s. No next value.",
                        len(l_raw_data), self._sample_size * p_num)
            raise signal_exceptions.NoNextValue()

    def goto_value(self, p_value_no):
        """
        Set the engine, so that nex 'get_next_value' call will return value number p_value_no+1.

        Eg. if p_value_no == 0, calling get_next_value will return first value.
        if p_value_no == 11, calling get_next_value will return 12-th value.
        """
        # LOGGER.debug("DOING SEEK TO: "+str(p_value_no))
        self._data_file.seek(p_value_no * self._sample_size)
        # LOGGER.debug("DATA FILE SEEK DONE. CURRENT POSITION/8 = "+str(self._data_file.tell()/8))
