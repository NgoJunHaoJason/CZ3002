# CZ3002 camera

Performs face detection and gender recognition on a "surveillance camera".
Use a computer's webcam as the surveillance camera.

## requirements

- [anaconda](https://docs.anaconda.com/anaconda/install/)
  - [commands](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## how to set-up

1. create the virtual environment: `conda create --name cz3002_venv --file cz3002_venv.txt`
2. activate virtual environment: `conda activate cz3002_venv`
3. install pip dependencies: `pip install -r requirements.txt`
4. deactivate virtual environment when done: `conda deactivate`
5. get your Firebase Service Account key and save it in the directory `violation_handling` as `key.json`
6. create `config.json` in the directory `violation_handling` with `{"project_id": "<project_id>"}`

## how to run demo

1. activate virtual environment: `conda activate cz3002_venv`
2. run the demo: `python demo_webcam.py`
    - view parameters: `python demo_webcam.py --help`
    - press 'q' key (or 'ctrl-c') to stop demo
3. deactivate virtual environment when done: `conda deactivate`

## TODO

- send image to server
- fix LFFD not working on CPU
