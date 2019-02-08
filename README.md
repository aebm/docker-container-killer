# docker-container-killer [![Build Status](https://travis-ci.org/aebm/docker-container-killer.svg)](https://travis-ci.org/aebm/docker-container-killer)
Kill rogue containers that match a given regex and are older than the minutes given

## Examples

* Build image as ${IMAGE_NAME}

  ```bash
  docker build -t ${IMAGE_NAME} .
  ```

* View help

  ```bash
  docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -it ${IMAGE_NAME} --help
  ```

* Run and show what containers matching REGEX and older than MINUTES it is going to delete without deleting them

  ```bash
  docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -it ${IMAGE_NAME} --noop --verbose --minutes MINUTES REGEX
  ```
  
* Delete all containers older than 72 hours
  
  ```bash
  docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -it ${IMAGE_NAME} --minutes $((72 * 60)) ''
  ```
