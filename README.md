## 💻 Pi-Squared
This project, for Advanced Computer Science Studies in Sweden HT2024, comprises a **broker/client** (Raspberry Pi code) and a **Flask-based front end** for communication.

-----

## 🛠️ Prerequisites

Ensure these are installed on your system:

  * **docker** and **docker compose**
  * **Python 3** (preferably latest version)
  * **pip** (Python package installer)

> For Docker installation instructions: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

-----

## ☁️ Broker Setup (MQTT)

This setup uses Docker for the MQTT broker.

1.  **Navigate to the broker directory:**

    ```shell
    cd PATH/TO/YOUR/REPO/LOCATION/broker
    ```

2.  **Create a password file:**

    ```shell
    touch ./mosquitto/config/passwd
    ```

3.  **Pull image and start container:**

    ```shell
    docker compose up -d
    ```

4.  **Create the broker password:**

    ```shell
    # Replace USERNAME and PASSWORD with your desired credentials.
    # Note: Running this directly logs credentials to history (less secure).
    # For a more secure way, enter the container and run mosquitto_passwd interactively.
    docker exec mosquitto sh -c "chmod 0700 /mosquitto/config/passwd\
    ```

&& chown root:root /mosquitto/config/passwd  
&& mosquitto\_passwd -b /mosquitto/config/passwd USERNAME PASSWORD"
\`\`\`

5.  **Restart the container:**
    ```shell
    docker compose restart mosquitto
    ```

-----

## 🤖 Client Setup (Raspberry Pi Code)

1.  **Copy the configuration file:**
    Copy `client.conf.template` to a new file named `client.conf` in the client directory.

2.  **Configure the client:**
    Add the **IP/hostname**, **port**, **username**, and **password** (from the broker setup) in `client.conf`.

3.  **Install requirements** (using a `venv` is recommended):

    ```shell
    pip install -r requirements.txt
    ```

4.  **Run the client:**

    ```shell
    python3 client_test.py
    ```

    $\rightarrow$ **"hello world" output** confirms the broker connection works.

-----

## 🌐 Front End Setup (Flask Web Interface)

The front end uses **Flask**, **Jinja2**, **Tailwind CSS**, and **DaisyUI**.

### ⚙️ Installation

1.  **Set Up a Virtual Environment:**

    ```shell
    python3 -m venv venv
    ```

2.  **Activate the Virtual Environment:**

    ```shell
    source venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```shell
    pip install flask 
    pip install flask_socketio
    pip install bcrypt
    ```

### 🚀 Running the Project

To start the web application:

```shell
python main.py
```

-----

## ⚙️ Additional Docker Commands

| Command | Description |
| :--- | :--- |
| `docker compose stop` | **Stop** the container(s) |
| `docker compose down` | **Delete** the container(s) |
| `docker exec -it CONTAINERNAME sh` | **Enter** a container interactively |
| `docker exec CONTAINERNAME sh -c "COMMAND"` | **Execute** a command in a container without entering |

