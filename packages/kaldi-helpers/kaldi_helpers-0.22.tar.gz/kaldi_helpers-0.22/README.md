# CoEDL Kaldi Helpers <img src="docs/img/kh.png" align="right"/>

A set of scripts to use in preparing a corpus for speech-to-text processing with the [Kaldi](http://kaldi-asr.org/) 
Automatic Speech Recognition Library.

Read about [setting up Docker](https://github.com/CoEDL/elpis/wiki/2018-summer-workshop-preparation) to run all this.

For more information about data requirements, see the 
[data guide](https://github.com/CoEDL/elpis/wiki/2018-summer-workshop-preparation).

## Requirements
This pipeline relies on Python 3.6 and several open-source Python packages (listed [here](./requirements.txt)).
It also assumes you have Kaldi, [sox](http://sox.sourceforge.net/) and [task](https://taskfile.org/) installed. We 
highly recommend using [our docker image](https://github.com/CoEDL/elpis/wiki/2018-summer-workshop-preparation).

## Tasks
This library uses the [task](https://taskfile.org) tool to run the more complex processes automatically. Once 
you've set up Kaldi Helpers, you can run the various pipeline tasks we've developed (or out of the box in the docker 
image). You can read about these tasks [here](https://github.com/CoEDL/elpis/wiki/tasks). 

## Workflow
<p align="center">
  <img src="docs/img/elpis-pipeline.svg"/>
</p>