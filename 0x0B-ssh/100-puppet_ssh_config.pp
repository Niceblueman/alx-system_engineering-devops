include stdlib
# blabla

file_line { 'disable PasswordAuthentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Public key config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  replace => true,
}
