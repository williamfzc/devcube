# devcube

last step to use docker in local development

## goal

This repo aims at providing virtual env, which is same as the remote one, for your local desktop with docker. 

Based on it, developers can use the same env as their CI system used, and pay much less patient on env issues.

Yes, of course developers can use docker directly to sync/build their env, but it is still not a convenient enough way to achieve this.

## usage

This repo will make everything simple and stable enough.

Assume that you have a repo called `YOUR_PROJECT` now:

```bash
cd YOUR_PROJECT
vim .devcube.json
```

add a json file:

```json
{
    "env": {
        "name": "hello",
        "image": "maven:slim"
    }
}
```

start simply:

```bash
devcube start
```

as you can see, now you can use `maven` inside the container directly, without installation on your real machine. Thanks docker:

```bash
root@df726801e785:/devcube# mvn --version
Apache Maven 3.6.3 (cecedd343002696d0abb50b32b541b8a6ba2883f)
Maven home: /usr/share/maven
Java version: 14.0.2, vendor: Oracle Corporation, runtime: /usr/local/openjdk-14
Default locale: en, platform encoding: UTF-8
OS name: "linux", version: "4.19.76-linuxkit", arch: "amd64", family: "unix"
```

and your workspace will be mapping:

```bash
root@df726801e785:/devcube# ls
LICENSE  README.md  devcube  devcube.egg-info  dist  example  requirements.txt  setup.py
```

Quite easy, ah? As a team manager, all you need to do is:

- upload your image to public/private repository
- upload your json file

and then all your teammates can use the same env to build apps without knowing what docker is. Say goodbye to env issues.

## installation

python >= 3.6

```bash
pip install devcube
```

## license

[MIT](LICENSE)
