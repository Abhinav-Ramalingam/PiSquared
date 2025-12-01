# Pi-Squared
Project for Advanced Computer Science Studies in Sweden HT2024

**prerequisites:**
- docker 
- docker compose
- python3

*how to install docker and docker compose:*
https://docs.docker.com/compose/install/

---
# broker setup

**navigate to the broker directory**
```shell
cd PATH/TO/YOUR/REPO/LOCATION/broker
```
**create a password file for the broker**

```shell
touch ./mosquitto/config/passwd
```

**pull the docker image and start the container:**

```shell
docker compose up -d
```

**create the broker password**
```shell
# exchange USERNAME AND PASSWORD for the username and password you want to use
# this way the the password gets logged to to the history which is less secure
# for a more secure way: enter the container and run the passwd command interactively
docker exec mosquitto sh -c "chmod 0700 /mosquitto/config/passwd\
 && chown root:root /mosquitto/config/passwd\
  && mosquitto_passwd -b /mosquitto/config/passwd USERNAME PASSWORD"
```
**restart the container**
```shell
docker compose restart mosquitto
```

---

# client setup
1. copy the `client.conf.template` to `client.conf` in the client directory
2. add ip/hostname, port, username and password in the config file
3. install requirements (might want to use a venv for that)
```shell
pip install -r requirements.txt
```
4. run client.py
```shell
python3 client_test.py
```
$\rightarrow$ if you see a hello world output, the connection to the broker works

---

## additional docker (compose) commands

**stop the container**
```shell
docker compose stop
```
**delete the container:**
```shell
docker compose down
```

**enter a container**
```shell
docker exec -it CONTAINERNAME sh 
```

**execute a command in a container without entering**
```shell
docker exec CONTAINERNAME sh -c "COMMAND"
```

