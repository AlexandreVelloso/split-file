# File splitter

## How to run the code
This project requires ffmpeg

### Activate the virtual env
```
$ source bin/activate
```

### Run the code
```
python3 main.py
```

## Youtube-dl commands

### Download playlist as mp3 files

If you don't want to set the start download index you can remove the --playlist-start options
'''
youtube-dl --playlist-start 0 --extract-audio --audio-format mp3 <playlist_url>
'''