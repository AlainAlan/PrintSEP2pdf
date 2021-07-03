# PrintSEP2pdf
Print entries in Stanford Encyclopedia of Philosophy to pdf in batch with user css style


## How

1. [Stylus :: add0n.com](https://add0n.com/stylus.html)
2. Chrome
3. Where?
    - `chrome://version/`
    - `chrome://extensions/`
    - copy Stylus's ID, find it in explorer, copy the path
7. customize those paths in `PrintSEP2pdf.py`
8. the `sum2021urls.txt` comes from the ipynb, and it can be customized too
    - check the ipynb for details (when only a certain number of entries are needed, for instance)
10. `python PrintSEP2pdf.py`
11. click to load the user css
12. wait

## notice

1. for Windows(10?) only
2. try adding Chinese Simplified in settings if font missed
3. comments mainly in Chinese, README mainly in broken English, Issue for help


btw, here's the terribly maintained user-css for SEP: [SEP-style/index.user.css at main · AlainAlan/SEP-style](https://github.com/AlainAlan/SEP-style/blob/main/index.user.css)
