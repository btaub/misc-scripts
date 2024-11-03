# con-CAT-enate

### category: steg

## clue

```
I recently got a new cat named Pearl.

This is a picture of her.
```
## flag

```
binwalk -ve keht.jpg

../steg/_keht.jpg.extracted/0:          JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=2, software=Picasa], baseline, precision 8, 3024x4032, components 3
../steg/_keht.jpg.extracted/1E:         TIFF image data, little-endian, direntries=2, software=Picasa
../steg/_keht.jpg.extracted/E9FDF:      ColorSync color profile 4.3, type lcms, RGB/XYZ-mntr device by lcms, 672 bytes, 2-11-2024 23:36:05 'GIMP built-in sRGBlc'
../steg/_keht.jpg.extracted/E9FDF.zlib: zlib compressed data
../steg/_keht.jpg.extracted/E9304:      PNG image data, 908 x 738, 8-bit/color RGBA, non-interlaced
../steg/_keht.jpg.extracted/E9344:      ASCII text
../steg/_keht.jpg.extracted/E9344.zlib: zlib compressed data

E9304 = png w/ flag
```
![E9304.png](https://raw.githubusercontent.com/btaub/misc-scripts/refs/heads/master/ctf/carolinaCon-2024/images/E9304.png)
