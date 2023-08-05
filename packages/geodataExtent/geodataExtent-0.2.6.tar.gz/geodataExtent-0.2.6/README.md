- [Use as CLI-Tool](#use-as-cli-tool)
  - [Install](#install)
  - [Usage](#usage)
    - [Examples](#examples)
- [Use as module](#use-as-module)

# Use as CLI-Tool

## Install

```bat
pip install geodataExtent
```
## Usage

```bat
extract-extent --help
```
gives:
```bat
Options:
  --path TEXT  Path to Folder containing Geofiles
  -c, --clear  Clear screen before showing results
  -t, --time   execute time extraction for one file
  -s, --space  execute boundingbox extraction for one file
  -h, --hull   execute convex-hull extraction for one file
  --help       Show this message and exit.
```
Those are **only** options, you do not have to use them. However, if you do not choos any of the execution flags `(-t / -s / -h)`, the folderextraction will be triggered and gives you the spatial and temporal extent of each of your Geofiles within the chosen folder in addition to the full spatial and temporal extent of the folder.

You are not limeted to choose only one option but all of them at once except for `--help`.

If you do not use `--path`, the path will be prompted. That means it is a shortcut only.

### Examples

```
$ extract-extent -t -s -h
Pleas enter path to Folder: <path>
Pleas enter filename: <filename>

Timeextent:
['1935/01/01 00:00:00 GMT+0', '2014/01/01 00:00:00 GMT+0', 365.253164556962]


Spatialextent:
[-179.5, -89.5, 179.5, 89.5]


Spatialextent as Convex Hull:
[(-179.5, -89.5), (-179.5, 89.5), (179.5, 89.5), (179.5, -89.5)]
```

The Timeextent starts with the beginning and ends with the end date as ISO8601 standard. the last number is the average intervall in which measurements have been taken.

The spatial extent is shown as a boundingbox. `[minX/minLong, minY/minLat, maxX/maxLong, maxY/maxLat]`

For more percission the `-h / --hull` flag gives you the spatial exnent as a convex hull. That means from all the points of a dataset the outer most points are beeing calculated and returned in correct order.

#### Folderextraction <!-- omit in toc -->

If you want to extract your hole folder, the `-c / --clear` flag is recommended because a long list of processing outputs is generated before the final output appears.
```
$ extract-extent -c --path "<folder path>"
```

# Use as module

