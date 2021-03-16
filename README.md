# checkmk-telegram
Receive checkmk notifications via Telegram.


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
