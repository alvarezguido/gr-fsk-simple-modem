This is a simple and straightforward modulator and demodulator (MODEM) for binary FSK implemented for GNURADIO. 
It reads from a text file (txt) and transmit binary data around a certain frequency, through and SDR (software defined radio) capable of transmiting signals (PlutoSDR, HackRF, LimeSDR, etc).
On the other side, another SDR (rtl-sdr family is sufficient) receives the data and recovers back to the original text.

The scope for the proyect is for understending, even for teaching purposes, some principes of digital signal communications, in a real scenario with electromagnetic waves.

Is a very simple way to see how signals are produced and received in SDRs, by using GNURADIO graphics (QT GUI Waterfall Sink, QT GUI Time Sink, etc.)

Next is a brief explanation of each of the files available in this repo, and is significance.

- fskMod.grc and fskMod.py: This are the flowchart (.grc) and script (.py) for reading the content in ./inputMessage.txt, which is then transmited at 2 MSamples/seg over an SDR (hackrf fot his case). Some notes of this flowchart are the following:
  * The block fskMod was developed as an edited Python block, which takes the binary data and produces a complex signal at +/- 20Khz according to the bit. It can be seen by double clicking on it.
  * The Rb (data bit rate), in GNURADIO, results as SDR sample rate (2M Hertz) devided to Rational Resampler Interpolation (20 in this case) devided to Repeat Interpolation (100 for the case).
  * The inputMessage.txt contains some message text (the alphabet) coded is ASCII. Each text character is build of 8 bits (or 1 byte lenght). Then, each bit has to be split so, after the Unpack K bits, each outcoming sample (violet) represent either a 0 (full byte of 00000000) or a 1 (the byte is 00000001). The minimun data type for GNURADIO are bytes, not bits.
  * 
