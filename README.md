# File splitter

## How to run the code
This project requires ffmpeg

After installing the dependencies you can run the script
```
python3 split_file.py
```

## parameters.txt file structure

The parameters file structure is very simple <br>
The header of the file has the following fields

```
file name
first part number
part prefix
separator
file total time
part duration
```

The rest of the file have each start of a section followed by the name of the section

```
00:00 chapter1
10:00 chapter2
```