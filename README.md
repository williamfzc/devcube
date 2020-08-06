# devcube

last step to use docker in local development

## what is it

Quickly create a virtual env and check in.

![Untitled.gif](https://i.loli.net/2020/08/05/jsD23rcybRxgIXP.gif)

All you need is a very simple config file:

```json
{
    "env": {
        "name": "hello",
        "image": "maven:slim"
    }
}
```

and enjoy same env everywhere. You can replace `maven` with custom image.

## goal

I got tired of env issues in co-development. At the most of time we dev from different kinds of platforms (linux/mac/windows ...), which may bring some potential env risks. For example, some building scripts may have different behaves on different platforms (caused by path or something else).

Thanks to docker, now we have a stable/standard/safe env for building artifacts in CI systems.

Although docker has been usage very widely in cloud, in local development it is still not convenient enough. For example, users at least need to know:

- what is docker
- what is volume
- what is container
- what is image
- ...

after that, they still need to type some long command (easily forget) to build an image and start a container ...

This repo aims at providing virtual env, which is same as the remote one in CI system, for your local desktop with docker, with less cost. Based on it, developers can use the same env as their CI system used, and pay much less patient on env issues.

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

## contribution

`devcube` now is very light-weight (easy to read and understand). You can directly read the code. PR and issues are welcome.

## license

[MIT](LICENSE)
