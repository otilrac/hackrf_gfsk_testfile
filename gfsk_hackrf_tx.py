#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Gfsk Hackrf Tx
# Generated: Sat Dec 14 00:15:34 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class gfsk_hackrf_tx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Gfsk Hackrf Tx")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.IFgain = IFgain = 30
        self.CenterFreq = CenterFreq = 2.4e9
        self.BBgain = BBgain = 30

        ##################################################
        # Blocks
        ##################################################
        _IFgain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._IFgain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_IFgain_sizer,
        	value=self.IFgain,
        	callback=self.set_IFgain,
        	label='IFgain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._IFgain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_IFgain_sizer,
        	value=self.IFgain,
        	callback=self.set_IFgain,
        	minimum=1,
        	maximum=40,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_IFgain_sizer)
        _CenterFreq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._CenterFreq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_CenterFreq_sizer,
        	value=self.CenterFreq,
        	callback=self.set_CenterFreq,
        	label='CenterFreq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._CenterFreq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_CenterFreq_sizer,
        	value=self.CenterFreq,
        	callback=self.set_CenterFreq,
        	minimum=2.35e9,
        	maximum=2.6e9,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_CenterFreq_sizer)
        _BBgain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._BBgain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_BBgain_sizer,
        	value=self.BBgain,
        	callback=self.set_BBgain,
        	label='BBgain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._BBgain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_BBgain_sizer,
        	value=self.BBgain,
        	callback=self.set_BBgain,
        	minimum=1,
        	maximum=40,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_BBgain_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'hackrf' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(CenterFreq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(IFgain, 0)
        self.osmosdr_sink_0.set_bb_gain(BBgain, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.digital_gfsk_mod_0 = digital.gfsk_mod(
        	samples_per_symbol=2,
        	sensitivity=1.0,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/xxno/code/hackrf_GFSK_Transmit_Text/xx.txt', True)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='',
        		pad_for_usrp=False,
        	),
        	payload_length=200,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gfsk_mod_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blks2_packet_encoder_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.digital_gfsk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_IFgain(self):
        return self.IFgain

    def set_IFgain(self, IFgain):
        self.IFgain = IFgain
        self._IFgain_slider.set_value(self.IFgain)
        self._IFgain_text_box.set_value(self.IFgain)
        self.osmosdr_sink_0.set_if_gain(self.IFgain, 0)

    def get_CenterFreq(self):
        return self.CenterFreq

    def set_CenterFreq(self, CenterFreq):
        self.CenterFreq = CenterFreq
        self._CenterFreq_slider.set_value(self.CenterFreq)
        self._CenterFreq_text_box.set_value(self.CenterFreq)
        self.osmosdr_sink_0.set_center_freq(self.CenterFreq, 0)

    def get_BBgain(self):
        return self.BBgain

    def set_BBgain(self, BBgain):
        self.BBgain = BBgain
        self._BBgain_slider.set_value(self.BBgain)
        self._BBgain_text_box.set_value(self.BBgain)
        self.osmosdr_sink_0.set_bb_gain(self.BBgain, 0)


def main(top_block_cls=gfsk_hackrf_tx, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
