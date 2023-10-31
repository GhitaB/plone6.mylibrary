# My library

A simple books manager
Plone 6 with Volto website (theme: [kitconcept/volto-light-theme](https://github.com/kitconcept/volto-light-theme))

## Quick Start

```shell
$ git clone https://github.com/GhitaB/plone6.mylibrary
$ cd plone6.mylibrary
$ nvm use v18
$ make install
$ make start-backend
$ make start-frontend
```

## Fixes
[Error when uploading large files](https://community.plone.org/t/plone-6-0-8-soft-released/18086#error-when-uploading-large-files-3)

```
In mylibrary/backend/instance/etc/zope.conf
update
form-memory-limit 20MB
Restart backend, retry upload.
```

[How to create a project like this](https://github.com/GhitaB/plone6.mylibrary/blob/main/notes.txt)
