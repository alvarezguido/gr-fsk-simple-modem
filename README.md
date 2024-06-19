This is a simple and straightforward modulator and demodulator (MODEM) for binary FSK implemented for GNURADIO. 
It reads from a text file (txt) and transmit binary data around a certain frequency, through and SDR capable of transmiting signals (PlutoSDR, HackRF, LimeSDR, etc).
On the other side, another SDR (rtl-sdr family is sufficient) receives the data and recovers back to the original text.
The scope for the proyect is for understending, even for teaching purposes, of principes of digital signal communications.

Is a very simple way to see the produced and incoming signals in SDRs, by using GNURADIO instruments (QT GUI Waterfall Sink, QT GUI Time Sink, etc.)
Next is a brief explanation of each of the files published in this repo, and is significance.
