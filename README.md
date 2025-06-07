Reverse Shell

This is a minimal reverse shell written in Python using raw sockets and subprocess. It helps to understand how reverse connections work at a low level.

---

## What’s in this?

* `TCPListner.py`: This runs on the attacker's machine and waits for a connection.
* `reverseshell.py`: This is executed on the victim’s machine and connects back to the attacker.

---

## How it works

1. The listener starts and listens on a port (`0.0.0.0:44444`).
2. The reverse shell (victim) connects to the attacker's IP and port.
3. The attacker sends a command.
4. The victim executes it and sends back the output.

---

## Usage

### 1. Start the listener (on your machine)

```bash
python listener.py
```

You’ll see something like:

```
Listening on 0.0.0.0 ..........
```

### 2. Run the reverse shell (on the target)

```bash
python reverseshell.py
```

As soon as the connection is made, the listener will show:

```
Connection received from ('127.0.0.1', <random_port>)
```

Now you can send a command from the server (you'll need to add the `send()` part manually here for now), and the reverse shell will send back the output.

---

## Example Demo (Manual Command Injection)

Right now, the listener is just accepting the connection and closing. For a working demo:

* Modify `listener.py` to send a command like this before `conn.close()`:

```python
conn.send(b"whoami")
```

* The victim will receive the command, run it, and send the result back.

---

## Disclaimer

This project is purely educational.
Use it only in controlled lab environments or with permission.
I am not responsible for any misuse or damage caused.

---
