<div align="center">
  <img src="logo.png" width="75" height="75" />
  <h3 align="center">Emotional Wellbeing API</h3>
    <p>Final Masters Project to design and implement an application to detect stress, depression, loneliness and suicide risk, giving custom advices to users.</p>
</div>

## Table of Contents

- [🤔 What is this project?](#-what-is-this-project)
- [🎯 Key Features](#-key-features)
- [🚀 Getting Started](#-getting-started)
- [💙 Contributing](#-contributing)
- [🙏 Credits](#-credits)

## 🤔 What is this project?

This repository contains the API component of *Emotional Wellbeing*, a Final Masters Project to design and implement an application to detect stress, depression, loneliness and suicide risk, giving custom advices to users.​ For more information about the project, please check [this](https://github.com/VicDominguez/Emotional-Wellbeing-Docs).

## 🎯 Key Features

- **Anonymized statistics**: this endpoint provides, for each measure (stress, depression, loneliness), an average daily questionaries score of all members who uploaded their data of three temporal ranges: yesterday, current week and last seven days.

- **Data upload**: there are endpoints to upload user daily questionaries, one off questionaries and biometric data. One off questionaries and user biometric data are uploaded to enable further research on that topic, current API doesn't provide more actions on them.

- **Database integration**: Seamless integration with a MongoDB database to read and write data. 

- **Logging and Testing**: Includes dedicated [testing](tests/), wide log usage and a github-actions based [pipeline](.github/workflows/master.yml).

## 🚀 Getting Started

As this project is fully-writted on Python, dependencies can be found [here](requirements.txt) and installed via pip.  Also, this Flask-based API can be launched from two different points, [api-prod](src/api-prod.py) and [app-test](src/api-test.py), being for production and testing respectively. IP and port can be changed at the end of these two files.

Nevertheless, this API works alongisde with MongoDB, so an instance needs to be available. Host, port and database/collection name can be configured dynamically on [Database](src/database.py) object and from callers [Endpoints](src/endpoints.py), [api-prod](src/api-prod.py) and [app-test](src/api-test.py).

Finally, examples can be found [here](examples/) and Client-side application to interact with can be found [here](https://github.com/Emotional-Wellbeing/App).

## 💙 Contributing

Any contributions you make are **greatly appreciated**, so if you have any idea of how to make this project better, please [create a pull request](https://github.com/VicDominguez/Emotional-Wellbeing-Docs/pulls). Also if you find any bug, please [create an issue](https://github.com/VicDominguez/Emotional-Wellbeing-Docs/issues/new).

## 🙏 Credits

This project was originally created by [@VicDominguez](https://github.com/VicDominguez) on 2023, with the support of ETSISI-UPM (School of Computer Systems Engineering, Polytechnic University of Madrid) and [@maria-marco](https://github.com/maria-marco). 
