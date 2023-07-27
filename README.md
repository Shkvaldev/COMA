# COMA
**Open source system that tries to implement useful voice UI**
> This software is under development! (By the way, it is just a demo concept of a real system, that is beeing developed by me in rust)

> All start modules are shipped in russian by default!

## Targets
### [*] Main target
- **Making it possible for blind or visually impaired people to use computers without any obstacles**

## Important note: this software could not exist without the following components
- **Vosk by Alphacephei (is used to recognize user speech in server-side software)**
- **RHVoice by Olga Yakovleva (is used to generate answers for user in server-side software)**

## Installation
> There is only Arch Linux support for now!
1. Clone the repository:
```shell
git clone (repo url here)
cd COMA
```
2. Install all _system_ dependences:
```shell
sudo pacman -Sy $(cat packages.txt)
```
3. Install all _python_ dependences:
```shell
pip install -r requirements.txt --break-system-packages
```
4. Run the server:
```shell
python main.py
```

## Platforms
- **Linux (server)**
- **All OSs that have Telegram support (client)**

## TODO
- **Popular initialization systems support (SystemD, OpenRC, RunIt)**
- **Simple installator**
- **Simple CLI or WEB manager**
- **Docker support**
- **Independent clients for Linux and Android**
- **Anvanced system for creating conversations**
- **Extend API**
