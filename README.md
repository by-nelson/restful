# Ansible Collection - by_nelson.restful

Documentation for the collection named `restful`.

## Build
If you want to use this repository to start your collection development then store it to a path with the following format

```sh
|_ $HOME/
  |_ collections/
    |_ ansible_collections/
      |_ ${your_namespace}
        |_ ${your_collection}(this repo)
```
Remember to store your collection following the namespace.collection convention.

If using a debian-based distro then you can install Ansible by running the script added to the repo

```sh
./setup.sh
```
> Note: Ansible commands are stored in `$HOME/.local/bin`

To run the template module execute:

```sh
python3 plugins/modules/template.py plugins/modules/template.json 
```

## Authors
Nelson Alvarez (@by_nelson)
