# The configmount project

Config is a tool to mount configuration files into your filesystem, so that you can navigate through the configuration hierarchy and access its values like files.

## Example

Create a configuration directory for testing via `mkdir ~/etc` and place the following yaml file into it:

~/etc/config.yml
```yaml
group:
  key: value
  another group:
    key: value
```

Now create a mount directory `/mnt/etc` and mount the configuration directory into it.

```
mkdir /mnt/etc
configmount mount --root ~/etc /mnt/etc
```

You should be able to navigate into the `/mnt/etc` directory and
see the file `key` and the directory `another group`. Now you can change the configuration value of `key` like:

```
cd /mnt/etc/config.yml
echo new value >key
```

The changes are written back into the file as soon as you unmount the directory `~/etc` from the mountpoint `/mnt/etc` via:

```
fusermount -u /mnt/etc
```

Finally `cat ~/etc/config.yml` should give you the modified file.
