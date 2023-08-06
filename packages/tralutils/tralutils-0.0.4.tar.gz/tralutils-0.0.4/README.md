tralutils
=========

python package for working with [Tral](https://www.tral.ru/production/tral_7/) videodata archive

Project Page: https://github.com/sv99/tralutils

Install
-------

Install from pip::

    pip install setuptools -U
    pip install tralutils

Install development version::

    git clone
    pip install -e .[dev]

make tar.gz for PyPi::
    
    pip install twine
    python setup.py sdist
    twine upload dist/tralutils-x.x.x.tar.gz

videodata dir
-------------

В каталоге videodata/ хранится архив видеонакопителя.

Файлы с одним именем хранят информацию об одном и том же фрагменте архива.

xx.30m xx.1h xx.6h xx.12h xx.24h xx.7d - файлы активности (иерархические индексные файлы)

xx.evt - события

xx.id3 - индексные файлы

xx.msn3 - содержат потоки данных. Размер *.msn3-файлов не превышает 600 мегабайт.

MSN3 формат позволяет передавать видео, звук и текст по сети Internet от архиватора для воспроизведения на компьютере пользователя.
Формат спроектирован для эффективной передачи данных, но не для их изменения.

Архив проиндексирован. Основные индексные файлы имеют ID3 формат.

В ID3 файле размещены записи одинакового размера/типа MSN_ID3_REC, которые относятся к одноименному файлу архива.

Записи MSN_ID3_REC хранят информацию о потоке, сформировавшем событие, о числе каналов для которых есть информация
по активности, время формирования события, позиция в одноименном MSN3 файле и информация по активности внутри каналов.

Файлы форматов 30M, 1H, 6H, 12H, 24H, 7D
являются прореженными ID3 файлами, с разной степенью прореживания

Информация о событиях заносится как в файлы данных архива в формате MSN3, так и в EVT файлы, которые являются
вспомогательными файлами и их содержимое используется для быстрого перехода на событие,
т. е. выполнения операций позиционирования по имени события. В EVT файле размещены записи типа EVENT_FILE_DATA_T.

Usage
-----

    videodir.py [-h] -i INPUT [-v] [--version]

    Show tral archive videodir information

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT   videodata dir
      -v, --verbose
      --version             show program's version number and exit

    tralinfo.py [-h] -i INPUT [-v] [--version]

    Show single tral videodata file info

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT   videdata file
      -v, --verbose
      --version             show program's version number and exit

