# Shell, permissions

This directory contains scripts that showcase the usage and application of Unix
shell permissions.

## Mandatory tasks

* [0-iam_betty](./0-iam_betty)- Changes the user ID to `betty`.

* [1-who_am_i](./1-who_am_i)- Prints the effective username of the current user.

* [2-groups](./2-groups)- Prints all the groups that the current user is part of.

* [3-new_owner](./3-new_owner)- Changes the owner of the file `hello` to the
 user `betty`.

* [4-empty](./4-empty)- Creates an empty file called `hello`.

* [5-execute](./5-execute)- Adds execute permission to the owner of the file
 `hello`.

* [6-multiple_permissions](./6-multiple_permissions)-  Adds execute permission to
 the owner and the group owner, and read permission to other users, to the file `hello`.

* [7-everybody](./7-everybody)-  Adds execute permission to the owner, the group
 owner, and other users, to the file `hello`.

* [8-James_Bond](./8-James_Bond)-  Sets the file permissions of `hello` to `007`.

* [9-John_Doe](./9-John_Doe)- Sets the file permissions of `hello` to `753`.

* [10-mirror_permissions](./10-mirror_permissions)- Sets the permissions of the
 file `hello` to be the same as the file `olleh`.

* [11-directories_permissions](./11-directories_permissions)- Adds execute
 permission to all subdirectories of the current directory for the owner, group owner,
 and other users.

* [12-directory_permissions](./12-directory_permissions)-  Creates a directory called
 `my_dir` with permissions `751` in the working directory.

* [13-change_group](./13-change_group)- Changes the group owner of the file
 `hello` to `school`.

## Advanced tasks

* [100-change_owner_and_group](./100-change_owner_and_group)- Changes the owner
 to `vincent` and the group owner to `staff` for all files and directories in the
 working directory.

* [101-symbolic_link_permissions](./101-symbolic_link_permissions)- Changes the
 owner and the group owner of the symbolic link `_hello` to `vincent` and `staff`
 , respectively.

* [102-if_only](./102-if_only)- Changes the owner of the file hello to `betty`
 only if it is owned by the user `guillaume`.

* [103-Star_Wars](./103-Star_Wars)- Plays the Star Wars IV episode in the terminal.

