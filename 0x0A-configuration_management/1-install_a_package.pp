# install flask version 2.1.0

exec { 'flask':
  command => 'yes | /usr/bin/pip3 install flask==2.1.0',
}
