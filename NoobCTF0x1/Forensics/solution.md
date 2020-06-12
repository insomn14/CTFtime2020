# [Forensics] Solution

## Can You Hear Me !!! 50pts

```
While performing Man in the Middle attack, I got a secret message from a scientist which can save the world from COVID-19. But unfortunatly I am not able to hear that. I believe that someone with good knowledge of some tools can get the secret message.

Note: Online tools also works.

Link: https://mega.nz/file/xdxHiQbb#vK91LAP9JjVKxQnMp6e_J1x7-IOIiqbST-htEAmdQWo

Replace spaces with _
```

At this challenge we were given the audio file Challenge.mp3, the sound on this audio is very small. So you have to increase the volume to hear the sound clearly, and you will get the link. https://www.shortto.com/noobarmy

After that you will be directed to download the audio.wav file. The file contains the Morse code sound. now we can decode the message [link](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)

FLAG : `noob{I_H4V3_M4D3_C0R0NA_VACC1N3}`

***

## It's easy 50pts

```
It's just an image

Link: https://github.com/AdityaSec/NoobCTF-0x1/tree/master/Forensics/It's easy

Author: Cryptonic007
```

on these challenge we were given image file iameasy.jpg but the file was corrupted. after doing analyze the signatures a.k.a Magic Bytes is different according to [List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

Before :
```
$ xxd iameasy.jpg | head -n2
00000000: 0510 1902 0010 4a46 4946 0001 0100 0048  ......JFIF.....H
00000010: 0048 0000 fffe 003b 4352 4541 544f 523a  .H.....;CREATOR:
```

After :
```
$ xxd mod_iameasy.jpg | head -n2
00000000: ffd8 ffe0 0010 4a46 4946 0001 0100 0048  ......JFIF.....H
00000010: 0048 0000 fffe 003b 4352 4541 544f 523a  .H.....;CREATOR:
```

FLAG : `noob{1_t0ld_y0u_1ts_34sy}`

***

## Fine the tone 250pts

```
James bond tried to find the tone. But, he tired now. Can you help me?

NOTE: Flag format noob{ALLCAPITAL}

Author: Cryptonic007
```

In this challenge, it is almost similar to the 'Frequency' crypto challenge. but this time we have to analyze the frequency, to do that we can use Audacity, change it to spectrogram. [link](https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling)

![image](https://github.com/insomn14/CTFtime2020/NoobCTF0x1/Forensics/Fine%20the%20tone/Screenshot.png "Screenshot.png")

From there we can start analyzing each frequency. after you get a number, replace it with the letter at each T9 keyboard emphasis. 

FLAG : `noob{YOUGOTTHETONE}`