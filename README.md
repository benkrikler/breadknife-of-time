# The breadknife of time
Takes a video and converts it into a [slit-scan style image](https://en.wikipedia.org/wiki/Slit-scan_photography).
If every frame in your video is stacked on top of the last, the image becomes a 3D block of what was seen.
It's like building a loaf of bread by stacking the individual slices together.
Now we take this tool, and slice the loaf along the direction we were stacking things:
we get a slice of what was seen in the same location, but at different moments.
This tool is basically a breadknife for time.

## Endorsements
"Hopefully I'm not overselling this project with that name" -- Ben Krikler

"[It's] the best thing since sliced time" -- Sioni Summers


## Installing
```
git clone https://github.com/benkrikler/breadknife-of-time.git
cd breadknife-of-time
pip install -r requirements.txt
```

## Usage
Use the `--help` option to get up to date built-in help.

An example command for you:
```bash
 ./breadknife.py -s centre -o my_slit_scan.jpg input_film.mp4 -p 1
```
