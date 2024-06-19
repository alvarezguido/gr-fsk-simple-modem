#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: fskMod
# Author: guido
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import fskMod_epy_block_0 as epy_block_0  # embedded python block
import osmosdr
import time




class fskMod(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "fskMod", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100e3

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + 'hackrf'
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(2e6)
        self.osmosdr_sink_0.set_center_freq(450e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.epy_block_0 = epy_block_0.blk(samp_rate=2e6/20, freq0=-20000, freq1=20000)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(8)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, 100)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, './inputMessage.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_repeat_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.epy_block_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.osmosdr_sink_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=fskMod, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
