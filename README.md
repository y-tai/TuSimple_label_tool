# TuSimple Label Tool
A tool helps create TuSimple format dataset.



### Get started
First of all, please modify the folder path in `add_lines.py` and `create_anno.py` .

1.Run add_lines.py to generate the pictures with auxiliary lines. Then you will get the folder `XXXX_anno`.
```Shell
python add_lines.py
```

2.Use [labelme](https://github.com/wkentaro/labelme) tools to create the `LineStrip` data. And then you will get the `XXXX.json` in the `XXXX_anno` folder.

3.Run `create_anno.py` to convert the labelme format to tusimple format.
```Shell
python create_anno.py
```

Finnally, you will get the tusimple format json file.

