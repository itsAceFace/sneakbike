# Devops Documentation for Sneakbike

- [Devops Documentation for Sneakbike](#devops-documentation-for-sneakbike)
  - [General Architecture](#general-architecture)
  - [Setting up OBS on Many Runners' Computers](#setting-up-obs-on-many-runners--computers)
  - [Server Setup on AWS](#server-setup-on-aws)
  - [Getting Data from the RTMP Server](#getting-data-from-the-rtmp-server)

---

---

## General Architecture

We broadcast from several OBS applications to an [RTMP](https://en.wikipedia.org/wiki/Real-Time_Messaging_Protocol) server hosted into an EC2 box which, in turn, broadcasts to the Sneakbike OBS (currently running on an actual physical "on-prem" machine).

- Our EC2 instance is currently an Ubuntu 18.04 t3a.micro
  - Optimized for network io, not much memory required.
- Our on-prem OBS for Sneakbike should be replaced by a cloud equivalent
  - (Currently researching, but it works for now)
  - A cloud equivalent would allow more than one individual to "run" the stream, which is a good bus-clause practice.
- The racers have to stream from their computers as no reasonable alternative exists for capturing desktop gameplay and sending it to our RTMP.

---

---

## Setting up OBS on Many Runners' Computers

The most frustrating part without a doubt is getting everyone a similar setup on OBS. We require downloading the latest OBS and have them import both a Profile (to allow us to set resolution) as well as Scene Collections (to allow us to control what things go where, and to not have them confuse it with their own scene collections).

Due to the nature of OBS's quick-switch for Profiles and Scenes, this works well.

## Server Setup on AWS

Included in the `/scripts` folder is the shell file `server_setup.sh` which can be used as the startup script on an Ubuntu 18.04 instance.

The tl;dr is that it installs nginx and an RTMP add-on for nginx. It is extremely lightweight and fairly configurable depending on what you need.

Note the nginx config at the bottom: here we have four different ports open that users can use. The addresses will look like this:

```bash
rtmp://public-ip-address-of-ec2:port/live/secret_key
```

Here, the ports go from 1935 (standard RTMP port) to 1938. The secret key doesn't matter and you can give it to your users in private for safety.

---

---

## Getting Data from the RTMP Server

To pull the streams from the RTMP server you can use VLC or the VLC plugin on OBS: point it to the `rtmp` address above and it should pick up your user correctly. For VLC, the "Network" option is the one you should use.

Again, they will look something like this:

```bash
rtmp://public-ip-address-of-ec2:port/live/secret_key
```
