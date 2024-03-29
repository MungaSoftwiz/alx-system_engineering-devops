# Use Puppet to make changes to a configuration file
include stdlib

file_line { 'Disable passwd authn':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication no',
  replace  => true,
}
file_line { 'Identity file for private key':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'IdentityFile ~/.ssh/school',
  replace  => true,
}
