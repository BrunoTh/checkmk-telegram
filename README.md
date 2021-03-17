# checkmk-telegram
Receive checkmk notifications via Telegram.

## How to use
1. Install the mkp.

2. Create a Telegram Bot using @BotFather (https://core.telegram.org/bots#6-botfather)

3. Create a new notification rule and select `Telegram` as Notification Method and paste the Bot Token you got from @BotFather.

4. Add the Telegram Username to the users that are going to receive notification via Telegram. Just go to __Setup__ > __Users__ and edit the users. Enter the Telegram usernames into the Field _Telegram Username_.

## Development

### Requirements

For the best development experience I recommend VSCode.

- Docker
- Docker image of Checkmk 2.0.0 Free Edition: https://checkmk.com/download
- VSCode Extension: Dev Container

### Preparation

1. Download and import the Docker image:
    ```
    $ docker load -i <path_to>/check-mk-enterprise-docker-2.0.0.demo.tar.gz
    ```

2. Open the folder in the Dev Container: 
    Ctrl+Shift+P: `> Remote-Container: Open Folder in Container...`

3. Install pylint after the container is configured. A notification should pop up where you can do so. This will be fixed in the future.

### Access the local checkmk instance

The Docker container exposes the port 5000 to access the checkmk instance: http://localhost:5000/cmk

To log into the instance use the credentials:
```
Username: cmkadmin
Password: cmkadmin
```

### Build and Test your changes

Use the task _Build and install mkp_ to pack and install the mkp. This is also the default build task (_Tasks: Run Build Task_ or Ctrl+Shift+B).
