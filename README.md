# Tsinghua University News Downloader

## Usage

`gt.py` gets news url and stores them to `urls.json`;

`dl.py` reads news url from `urls.json` and download them to `news.json`.

News are stored in the format of `{'url': url, 'title': title, 'content': content}`, while content splits lines with `\n` and paragraphs with `\n \n`.

Default multithreads number is set to 32.

Existing data can be found in `urls.json` and `news.json` (up to 2019-7-4).

## To-dos

 - Seperate configs like catagories to `settings.config`;

 - Support breakpoints;

 - ...