
![gnuradio-logo](https://github.com/alvarezguido/gr-fsk-simple-modem/assets/47746423/9796f668-a2ac-4795-84e3-088ffe4362a8)

This is a simple and straightforward modulator and demodulator (MODEM) for simplest binary FSK (BFSK) implemented for GNURADIO. 
It reads from a text file (.txt) and transmit binary data around a certain frequency, through an SDR (software defined radio) board capable of transmiting signals (as PlutoSDR, HackRF, LimeSDR, etc).
On the other side, another SDR (rtl-sdr family is sufficient) receives electromagnetic waves with the data and recovers back to the original text in a text file.

The scope for the proyect is for understending, even for teaching purposes, some principes of digital signal communications, in a real scenario handling electromagnetic waves.

Is a very simple way to see how signals are produced and received in SDRs, by using GNURADIO graphics (QT GUI Waterfall Sink, QT GUI Time Sink, etc.)

Next is a brief explanation of each of the files available in this repo, and is significance.


## Transmiter (fskMod)
<img width="926" alt="fskMod" src="https://github.com/alvarezguido/gr-fsk-simple-modem/assets/47746423/a86a9f7a-074c-4fdd-9bd8-4a62e8d102e4">

For the transmiter, the fskMod.grc flowchart is used as shown in the image above.

- fskMod.grc and fskMod.py: These are the flowchart (.grc) and script (.py) for reading the content in ./inputMessage.txt, which is then transmited at 2 MSamples/seg over an SDR (hackrf fot his case). Some notes of this flowchart are the following:
  * The block fskMod was developed as an edited Python block, which takes the binary data and produces a complex signal at +/- 20Khz according to the bit. It can be seen by double clicking on it.
  * The Rb (data bit rate), in GNURADIO, comes as the SDR sample rate (2M Hertz) devided to Rational Resampler Interpolation (20 in this case) devided to Repeat Interpolation (100 for the case), yielding a Rb of 1Kbps.
  * The inputMessage.txt contains some message text (the alphabet) coded is ASCII. Each text character is build of 8 bits (or 1 byte lenght). Then, each bit has to be split so, after the Unpack K bits, each outcoming sample (violet) represent either a 0 (full byte of 00000000) or a 1 (the byte is 00000001). The minimun data type for GNURADIO are bytes, not bits.

### fskMod
The fskMod block was developed as an edited Python block, which takes the binary data and produces a complex signal at default +/- 20Khz according to the input bit. It can be seen by double clicking on it.

![fskMod](https://github.com/alvarezguido/gr-fsk-simple-modem/assets/47746423/b92a020b-8360-4b96-8e7d-4708f4840204)

Within the block, samp_rate, freq0 and freq1 are input variables to define the frequencies and sample rate for the block. The input signal is Float and the output is Complex, the FSK signal. The key of the block in on the formula used to produce a complex exponential whenever comes a 0 or a 1, as seen in lines 25 and 27 of the python code. The samp_rate results as the Rb*100, so samp_rate=100K for this block.

### Executing the script
As can be seen in the image, in the Options block, it has been selected "No GUI" and "Run to Completition", just because the program will be executed once every second, avoiding been transmiting all the time. The run_tx.sh does it, by simple calling the python script fskMod.py every second, which performs only one transmission before closing the program.

- run_tx.sh: this is a simple bash script for invoking the fskMod.py every 1 second, so the alphabet is transmitted once per second (this prevent of been transmitting all time).

## Receiver (fskDem)
- fskDem.grc and fskDem.py: This are the flowchart (.grc) and script (.py) for receiving the BFSK signal over the air. It is build upon generic GNURADIO blocks.
  * The flowchart should be run from GNURADIO Companion on hold for transmittions.
  * The outputBits.txt file holds the binary data demodulated.

- fskDecoder.ipynb is a jupyter notebook which receives the outputBits.txt file and produces outputMessage.txt file

- pack_bits.grc and pack_bits.py receives the outMessage.txt and pack again the bits into byte, saving the data, in ASCII text if succesfull decoded was made, in outputPackedMessage.txt
