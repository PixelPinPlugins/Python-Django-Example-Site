# Python Social Auth Example Site

This example site is used to demonstrate how to implement Python Social Auth with PixelPin. Guide found [on PixelPin's developer website](https://developer.pixelpin.io/pythondjango.php)

#Vagrant

Run 

```shell
$ vagrant up
```

To run a virtual environment with Pyhton 3.6.5, Django 2.0.4, OpenSSL 1.1.0 installed.

# Running the site
Make sure you update the ALLOWED_HOSTS variable in settings.py

```shell
$ sudo python3.6 -m pip install social-auth-app-django social-auth-core[openidconnect] -r requirements.txt
$ sudo python3.6 manage.py runserver 192.168.33.14

```