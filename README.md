🎫 TicketFlow

TicketFlow is a web-based ticket booking platform built with Django. It allows users to browse events, select seats, and book tickets online. Admins can manage events, venues, and bookings through a secure admin panel.

📋 Features

User authentication (Sign up, login, logout)

Browse and search events

Book tickets and select seats

View booking history

Admin panel to manage:

Events

Venues

Tickets

Users

🛠️ Tech Stack

Backend: Django (Python)

Database: SQLite (default) / PostgreSQL (production recommended)

Frontend: React

Other Tools: Git & GitHub for version control

📁 Project Structure


┣ 📂backend
┃ ┣ 📂events
┃ ┃ ┣ 📂migrations
┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜admin.py
┃ ┃ ┣ 📜apps.py
┃ ┃ ┣ 📜models.py
┃ ┃ ┣ 📜serializers.py
┃ ┃ ┣ 📜tests.py
┃ ┃ ┗ 📜views.py
┃ ┣ 📂ticketflowProject
┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃ ┣ 📜settings.cpython-311.pyc
┃ ┃ ┃ ┣ 📜urls.cpython-311.pyc
┃ ┃ ┃ ┗ 📜wsgi.cpython-311.pyc
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜asgi.py
┃ ┃ ┣ 📜settings.py
┃ ┃ ┣ 📜urls.py
┃ ┃ ┗ 📜wsgi.py
┃ ┣ 📂tickets
┃ ┃ ┣ 📂migrations
┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜admin.py
┃ ┃ ┣ 📜apps.py
┃ ┃ ┣ 📜models.py
┃ ┃ ┣ 📜serializers.py
┃ ┃ ┣ 📜tests.py
┃ ┃ ┣ 📜utils.py
┃ ┃ ┗ 📜views.py
┃ ┣ 📂users
┃ ┃ ┣ 📂migrations
┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜admin.py
┃ ┃ ┣ 📜apps.py
┃ ┃ ┣ 📜models.py
┃ ┃ ┣ 📜permissions.py
┃ ┃ ┣ 📜tests.py
┃ ┃ ┗ 📜views.py
┃ ┣ 📂venv
┃ ┃ ┣ 📂Include
┃ ┃ ┣ 📂Lib
┃ ┃ ┃ ┗ 📂site-packages
┃ ┃ ┃   ┣ 📂_distutils_hack
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜override.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┗ 📜override.py
┃ ┃ ┃   ┣ 📂asgiref
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜compatibility.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜current_thread_executor.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜local.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜server.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜sync.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜testing.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜timeout.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜typing.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜wsgi.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜compatibility.py
┃ ┃ ┃   ┃ ┣ 📜current_thread_executor.py
┃ ┃ ┃   ┃ ┣ 📜local.py
┃ ┃ ┃   ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┣ 📜server.py
┃ ┃ ┃   ┃ ┣ 📜sync.py
┃ ┃ ┃   ┃ ┣ 📜testing.py
┃ ┃ ┃   ┃ ┣ 📜timeout.py
┃ ┃ ┃   ┃ ┣ 📜typing.py
┃ ┃ ┃   ┃ ┗ 📜wsgi.py
┃ ┃ ┃   ┣ 📂asgiref-3.9.1.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂colorama
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ansi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ansitowin32.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜initialise.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜win32.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜winterm.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂tests
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ansi_test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ansitowin32_test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜initialise_test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜isatty_test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜winterm_test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜ansi_test.py
┃ ┃ ┃   ┃ ┃ ┣ 📜ansitowin32_test.py
┃ ┃ ┃   ┃ ┃ ┣ 📜initialise_test.py
┃ ┃ ┃   ┃ ┃ ┣ 📜isatty_test.py
┃ ┃ ┃   ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┗ 📜winterm_test.py
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜ansi.py
┃ ┃ ┃   ┃ ┣ 📜ansitowin32.py
┃ ┃ ┃   ┃ ┣ 📜initialise.py
┃ ┃ ┃   ┃ ┣ 📜win32.py
┃ ┃ ┃   ┃ ┗ 📜winterm.py
┃ ┃ ┃   ┣ 📂colorama-0.4.6.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂corsheaders
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜conf.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜defaults.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜middleware.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜signals.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┣ 📜checks.py
┃ ┃ ┃   ┃ ┣ 📜conf.py
┃ ┃ ┃   ┃ ┣ 📜defaults.py
┃ ┃ ┃   ┃ ┣ 📜middleware.py
┃ ┃ ┃   ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┗ 📜signals.py
┃ ┃ ┃   ┣ 📂django
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜shortcuts.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂apps
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜config.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜registry.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜config.py
┃ ┃ ┃   ┃ ┃ ┗ 📜registry.py
┃ ┃ ┃   ┃ ┣ 📂conf
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜global_settings.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂app_template
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜admin.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜tests.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py-tpl
┃ ┃ ┃   ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂de_CH
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂en_CA
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂en_IE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂es_NI
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂es_PR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fr_BE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fr_CA
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fr_CH
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ig
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂kab
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂uz
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📂project_template
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂project_name
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜asgi.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜settings.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜urls.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wsgi.py-tpl
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜manage.py-tpl
┃ ┃ ┃   ┃ ┃ ┣ 📂urls
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜i18n.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜static.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜i18n.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜static.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┗ 📜global_settings.py
┃ ┃ ┃   ┃ ┣ 📂contrib
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂admin
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜actions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜options.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sites.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜tests.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜widgets.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂am
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kab
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uz
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜djangojs.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜djangojs.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_logentry_remove_auto_add.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜0003_logentry_add_action_flag_choices.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0002_logentry_remove_auto_add.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0003_logentry_add_action_flag_choices.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂static
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂admin
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📂css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📂vendor
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┃ ┗ 📂select2
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┃   ┣ 📜LICENSE-SELECT2.md
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┃   ┣ 📜select2.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┃   ┗ 📜select2.min.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜autocomplete.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜base.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜changelists.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜dark_mode.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜dashboard.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜forms.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜login.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜nav_sidebar.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜responsive_rtl.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜responsive.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜rtl.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜unusable_password_field.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┗ 📜widgets.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📂img
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📂gis
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┃ ┣ 📜move_vertex_off.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┃ ┗ 📜move_vertex_on.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜calendar-icons.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-addlink.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-alert.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-calendar.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-changelink.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-clock.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-deletelink.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-hidelink.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-no.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-unknown-alt.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-unknown.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-viewlink.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜icon-yes.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜inline-delete.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜README.txt
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜search.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜selector-icons.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜sorting-icons.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜tooltag-add.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┗ 📜tooltag-arrowright.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📂admin
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┣ 📜DateTimeShortcuts.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┗ 📜RelatedObjectLookups.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📂vendor
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┣ 📂jquery
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┣ 📜jquery.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┣ 📜jquery.min.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┗ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┣ 📂select2
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┣ 📂i18n
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜af.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ar.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜az.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜bg.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜bn.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜bs.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ca.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜cs.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜da.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜de.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜dsb.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜el.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜en.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜es.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜et.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜eu.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜fa.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜fi.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜fr.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜gl.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜he.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜hi.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜hr.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜hsb.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜hu.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜hy.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜id.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜is.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜it.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ja.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ka.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜km.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ko.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜lt.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜lv.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜mk.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ms.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜nb.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ne.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜nl.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜pl.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ps.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜pt-BR.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜pt.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ro.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜ru.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜sk.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜sl.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜sq.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜sr-Cyrl.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜sr.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜sv.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜th.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜tk.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜tr.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜uk.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜vi.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┣ 📜zh-CN.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┃ ┗ 📜zh-TW.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┣ 📜LICENSE.md
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┣ 📜select2.full.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┃ ┗ 📜select2.full.min.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃ ┗ 📂xregexp
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃   ┣ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃   ┣ 📜xregexp.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┃   ┗ 📜xregexp.min.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜actions.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜autocomplete.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜calendar.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜cancel.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜change_form.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜core.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜filters.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜inlines.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜jquery.init.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜nav_sidebar.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜popup_response.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜prepopulate_init.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜prepopulate.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜SelectBox.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜SelectFilter2.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜theme.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜unusable_password_field.js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜urlify.js
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂admin
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂auth
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📂user
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃   ┣ 📜add_form.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃   ┗ 📜change_password.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂edit_inline
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stacked.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜tabular.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂includes
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fieldset.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜object_delete_summary.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂widgets
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clearable_file_input.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜date.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜foreign_key_raw_id.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜many_to_many_raw_id.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜radio.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜related_widget_wrapper.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜split_datetime.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜time.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜url.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜404.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜500.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜actions.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜app_index.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜app_list.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base_site.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜change_form_object_tools.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜change_form.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜change_list_object_tools.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜change_list_results.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜change_list.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜color_theme_toggle.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜date_hierarchy.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜delete_confirmation.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜delete_selected_confirmation.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜filter.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜invalid_setup.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜login.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜nav_sidebar.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜object_history.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜pagination.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜popup_response.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜prepopulated_fields_js.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜search_form.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜submit_line.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂registration
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜logged_out.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜password_change_done.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜password_change_form.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜password_reset_complete.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜password_reset_confirm.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜password_reset_done.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜password_reset_email.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜password_reset_form.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templatetags
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_list.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_modify.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜admin_urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜log.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜admin_list.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜admin_modify.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜admin_urls.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜log.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂views
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜autocomplete.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜main.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜autocomplete.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜decorators.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜main.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜actions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜checks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜decorators.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filters.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜forms.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜helpers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜options.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sites.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜tests.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜widgets.py
┃ ┃ ┃   ┃ ┃ ┣ 📂admindocs
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kab
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂admin_doc
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜bookmarklets.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜index.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜missing_docutils.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜model_detail.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜model_index.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜template_detail.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜template_filter_index.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜template_tag_index.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜view_detail.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜view_index.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜middleware.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┣ 📂auth
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜backends.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base_user.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜context_processors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜decorators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜hashers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜password_validation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜tokens.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜validators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂handlers
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜modwsgi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜modwsgi.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kab
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uz
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜changepassword.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜createsuperuser.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜changepassword.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜createsuperuser.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0002_alter_permission_name_max_length.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0003_alter_user_email_max_length.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0004_alter_user_username_opts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0005_alter_user_last_login_null.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0006_require_contenttypes_0002.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0007_alter_validators_add_error_messages.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0008_alter_user_username_max_length.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0009_alter_user_last_name_max_length.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0010_alter_group_name_max_length.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0011_update_proxy_permissions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜0012_alter_user_first_name_max_length.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0002_alter_permission_name_max_length.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0003_alter_user_email_max_length.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0004_alter_user_username_opts.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0005_alter_user_last_login_null.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0006_require_contenttypes_0002.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0007_alter_validators_add_error_messages.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0008_alter_user_username_max_length.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0009_alter_user_last_name_max_length.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0010_alter_group_name_max_length.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0011_update_proxy_permissions.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0012_alter_user_first_name_max_length.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂auth
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂widgets
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜read_only_password_hash.html
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂registration
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜password_reset_subject.txt
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜backends.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base_user.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜checks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜common-passwords.txt.gz
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜context_processors.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜decorators.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜forms.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜hashers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜middleware.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜mixins.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜password_validation.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜signals.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜tokens.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜validators.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┣ 📂contenttypes
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜prefetch.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜remove_stale_contenttypes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜remove_stale_contenttypes.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜0002_remove_content_type_name.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0002_remove_content_type_name.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜checks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜fields.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜forms.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜prefetch.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┣ 📂flatpages
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜forms.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sitemaps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templatetags
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜flatpages.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜flatpages.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜forms.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜middleware.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sitemaps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┣ 📂gis
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜feeds.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜geoip2.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜geometry.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜measure.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ptr.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜shortcuts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂admin
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜options.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜options.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂db
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂backends
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂base
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂mysql
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂oracle
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂postgis
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜const.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pgraster.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜const.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pgraster.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂spatialite
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜adapter.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜client.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂models
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜aggregates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜proxy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂sql
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜conversion.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜conversion.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜aggregates.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜lookups.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜proxy.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂forms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜widgets.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜fields.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜widgets.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂gdal
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜datasource.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜driver.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜envelope.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜error.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜feature.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜field.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜geometries.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜geomtype.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜layer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜libgdal.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜srs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂prototypes
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ds.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errcheck.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜generation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geom.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜raster.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜srs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜ds.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜errcheck.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜generation.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜geom.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜raster.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜srs.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂raster
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜band.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜const.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜source.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜band.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜const.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜source.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜datasource.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜driver.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜envelope.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜error.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜feature.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜field.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜geometries.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜geomtype.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜layer.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜libgdal.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜srs.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂geos
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜collections.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜coordseq.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜error.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜factory.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜geometry.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜io.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜libgeos.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜linestring.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜mutable_list.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜point.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜polygon.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜prepared.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂prototypes
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜coordseq.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜errcheck.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜geom.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜io.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜misc.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜predicates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜prepared.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜threadsafe.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜topology.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜coordseq.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜errcheck.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜geom.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜io.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜misc.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜predicates.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜prepared.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜threadsafe.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜topology.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜collections.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜coordseq.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜error.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜factory.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜geometry.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜io.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜libgeos.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜linestring.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜mutable_list.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜point.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜polygon.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜prepared.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜inspectdb.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ogrinspect.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜inspectdb.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜ogrinspect.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂serializers
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜geojson.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜geojson.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sitemaps
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜kml.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜kml.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂static
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂gis
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📂css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┗ 📜ol3.css
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📂img
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜draw_line_off.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜draw_line_on.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜draw_point_off.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜draw_point_on.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜draw_polygon_off.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┗ 📜draw_polygon_on.svg
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂js
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜OLMapWidget.js
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂gis
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📂kml
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┣ 📜base.kml
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┃ ┗ 📜placemarks.kml
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┣ 📜openlayers-osm.html
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📜openlayers.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂utils
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜layermapping.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜ogrinfo.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜ogrinspect.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜srs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜layermapping.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ogrinfo.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ogrinspect.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜srs.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜feeds.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜geoip2.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜geometry.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜measure.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ptr.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜shortcuts.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┣ 📂humanize
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uz
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templatetags
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜humanize.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜humanize.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┣ 📂messages
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜api.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜constants.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜context_processors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂storage
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜cookie.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜fallback.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜session.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cookie.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜fallback.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜session.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜api.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜constants.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜context_processors.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜middleware.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┣ 📂postgres
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜constraints.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜expressions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜functions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜indexes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜lookups.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜search.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜serializers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜validators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂aggregates
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜general.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜statistics.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜general.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜mixins.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜statistics.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fields
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜array.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜citext.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜hstore.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonb.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜ranges.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜array.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜citext.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜hstore.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜jsonb.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ranges.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂forms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜array.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜hstore.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜ranges.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜array.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜hstore.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜ranges.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂jinja2
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂postgres
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂widgets
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜split_array.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uz
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂postgres
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂widgets
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜split_array.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜constraints.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜expressions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜functions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜indexes.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜lookups.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜search.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜serializers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜signals.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜validators.py
┃ ┃ ┃   ┃ ┃ ┣ 📂redirects
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kab
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uz
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜0002_alter_redirect_new_path_help_text.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0002_alter_redirect_new_path_help_text.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜middleware.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜models.py
┃ ┃ ┃   ┃ ┃ ┣ 📂sessions
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base_session.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜serializers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂backends
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜cached_db.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜db.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜file.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜signed_cookies.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cached_db.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜db.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜file.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜signed_cookies.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kab
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uz
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜clearsessions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜clearsessions.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base_session.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜middleware.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜serializers.py
┃ ┃ ┃   ┃ ┃ ┣ 📂sitemaps
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sitemap_index.xml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜sitemap.xml
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┣ 📂sites
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜admin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜management.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜managers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜middleware.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜requests.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜shortcuts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂af
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ar_DZ
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ast
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂br
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂bs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ckb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂cy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂dsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂en_GB
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_CO
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_MX
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂es_VE
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂eu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂fy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ga
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gd
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂he
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hsb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂io
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂is
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ka
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kab
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂km
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂kn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ko
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ml
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂mr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ms
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂my
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ne
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂os
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pa
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sq
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sr_Latn
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂sw
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂te
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂tt
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂udm
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ug
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂ur
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂uz
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜0002_alter_domain_unique.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0002_alter_domain_unique.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜checks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜management.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜managers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜middleware.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜requests.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜shortcuts.py
┃ ┃ ┃   ┃ ┃ ┣ 📂staticfiles
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜finders.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜handlers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜storage.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜collectstatic.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜findstatic.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜runserver.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜collectstatic.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜findstatic.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜runserver.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜checks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜finders.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜handlers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜storage.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜testing.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┣ 📂syndication
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📂core
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜asgi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜paginator.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜signals.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜signing.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜validators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜wsgi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂cache
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂backends
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜db.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜filebased.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜memcached.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜redis.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜db.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜dummy.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filebased.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜locmem.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜memcached.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜redis.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┣ 📂checks
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜async_checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜caches.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜commands.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜database.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜files.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜messages.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜model_checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜registry.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜templates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜translation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂compatibility
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜django_4_0.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜django_4_0.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂security
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜csrf.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜sessions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜csrf.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜sessions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜async_checks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜caches.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜commands.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜database.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜files.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜messages.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜model_checks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜registry.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜templates.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜translation.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜urls.py
┃ ┃ ┃   ┃ ┃ ┣ 📂files
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜images.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜locks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜move.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜temp.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜uploadedfile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜uploadhandler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂storage
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜filesystem.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜handler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜memory.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜mixins.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filesystem.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜handler.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜memory.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜mixins.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜images.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜locks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜move.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜temp.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜uploadedfile.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜uploadhandler.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┣ 📂handlers
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜asgi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exception.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wsgi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜asgi.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exception.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜wsgi.py
┃ ┃ ┃   ┃ ┃ ┣ 📂mail
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜message.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂backends
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜console.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜dummy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜filebased.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜locmem.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜smtp.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜console.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜dummy.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filebased.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜locmem.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜smtp.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜message.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜color.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sql.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜templates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜check.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜compilemessages.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜createcachetable.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜dbshell.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜diffsettings.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜dumpdata.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜flush.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜inspectdb.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜loaddata.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜makemessages.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜makemigrations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜migrate.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜optimizemigration.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜runserver.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜sendtestemail.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜shell.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜showmigrations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlflush.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlmigrate.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜sqlsequencereset.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜squashmigrations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜startapp.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜startproject.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜testserver.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜check.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compilemessages.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜createcachetable.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜dbshell.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜diffsettings.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜dumpdata.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜flush.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜inspectdb.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜loaddata.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜makemessages.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜makemigrations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜migrate.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜optimizemigration.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜runserver.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sendtestemail.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜shell.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜showmigrations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sqlflush.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sqlmigrate.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sqlsequencereset.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜squashmigrations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜startapp.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜startproject.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜test.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜testserver.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜color.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sql.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜templates.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┣ 📂serializers
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜json.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜jsonl.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜python.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜pyyaml.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜xml_serializer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜json.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜jsonl.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜python.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜pyyaml.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜xml_serializer.py
┃ ┃ ┃   ┃ ┃ ┣ 📂servers
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜basehttp.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜basehttp.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜asgi.py
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┣ 📜paginator.py
┃ ┃ ┃   ┃ ┃ ┣ 📜signals.py
┃ ┃ ┃   ┃ ┃ ┣ 📜signing.py
┃ ┃ ┃   ┃ ┃ ┣ 📜validators.py
┃ ┃ ┃   ┃ ┃ ┗ 📜wsgi.py
┃ ┃ ┃   ┃ ┣ 📂db
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜transaction.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂backends
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ddl_references.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂base
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜validation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜client.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜creation.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜validation.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂dummy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂mysql
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜validation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜client.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compiler.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜creation.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜validation.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂oracle
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜functions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜oracledb_any.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜validation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜client.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜creation.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜functions.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜oracledb_any.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜validation.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂postgresql
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜psycopg_any.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜client.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compiler.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜creation.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜psycopg_any.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sqlite3
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜_functions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜client.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜creation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜introspection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜operations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_functions.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜client.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜creation.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜introspection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜operations.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ddl_references.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜signals.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜autodetector.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜executor.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜graph.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜loader.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜migration.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜optimizer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜questioner.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜recorder.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜serializer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜state.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜writer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂operations
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜special.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜fields.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜special.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜autodetector.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜executor.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜graph.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜loader.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜migration.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜optimizer.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜questioner.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜recorder.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜serializer.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜state.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜writer.py
┃ ┃ ┃   ┃ ┃ ┣ 📂models
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜aggregates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜constants.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜constraints.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜deletion.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜enums.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜expressions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜indexes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜lookups.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜manager.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜options.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜query_utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜query.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜signals.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂fields
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜composite.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜files.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜generated.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜json.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜related_descriptors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜related_lookups.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜related.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜reverse_related.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜tuple_lookups.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜composite.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜files.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜generated.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜json.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜mixins.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜proxy.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜related_descriptors.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜related_lookups.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜related.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜reverse_related.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜tuple_lookups.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂functions
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜comparison.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜datetime.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜json.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜math.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜mixins.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜text.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜window.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜comparison.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜datetime.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜json.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜math.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜mixins.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜text.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜window.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂sql
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜compiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜constants.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜datastructures.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜query.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜subqueries.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜where.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compiler.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜constants.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜datastructures.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜query.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜subqueries.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜where.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜aggregates.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜constants.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜constraints.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜deletion.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜enums.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜expressions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜indexes.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜lookups.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜manager.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜options.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜query_utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜query.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜signals.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜transaction.py
┃ ┃ ┃   ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┣ 📂dispatch
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜dispatcher.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜dispatcher.py
┃ ┃ ┃   ┃ ┃ ┗ 📜license.txt
┃ ┃ ┃   ┃ ┣ 📂forms
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜boundfield.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜fields.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜forms.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜formsets.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜renderers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜widgets.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂jinja2
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂django
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📂forms
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂errors
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📂dict
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┃ ┣ 📜default.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┃ ┣ 📜text.txt
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┃ ┗ 📜ul.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📂list
┃ ┃ ┃   ┃ ┃ ┃     ┃   ┣ 📜default.html
┃ ┃ ┃   ┃ ┃ ┃     ┃   ┣ 📜text.txt
┃ ┃ ┃   ┃ ┃ ┃     ┃   ┗ 📜ul.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂formsets
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜div.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜p.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜table.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜ul.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂widgets
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜attrs.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜checkbox_option.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜checkbox_select.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜checkbox.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜clearable_file_input.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜color.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜date.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜datetime.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜email.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜file.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜hidden.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜input_option.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜input.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜multiple_hidden.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜multiple_input.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜multiwidget.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜number.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜password.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜radio_option.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜radio.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜search.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜select_date.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜select_option.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜select.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜splitdatetime.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜splithiddendatetime.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜tel.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜text.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜textarea.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜time.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜url.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜attrs.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜div.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜field.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜label.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜p.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜table.html
┃ ┃ ┃   ┃ ┃ ┃     ┗ 📜ul.html
┃ ┃ ┃   ┃ ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂django
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📂forms
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂errors
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📂dict
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┃ ┣ 📜default.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┃ ┣ 📜text.txt
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┃ ┗ 📜ul.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📂list
┃ ┃ ┃   ┃ ┃ ┃     ┃   ┣ 📜default.html
┃ ┃ ┃   ┃ ┃ ┃     ┃   ┣ 📜text.txt
┃ ┃ ┃   ┃ ┃ ┃     ┃   ┗ 📜ul.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂formsets
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜div.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜p.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜table.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜ul.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂widgets
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜attrs.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜checkbox_option.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜checkbox_select.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜checkbox.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜clearable_file_input.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜color.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜date.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜datetime.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜email.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜file.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜hidden.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜input_option.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜input.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜multiple_hidden.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜multiple_input.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜multiwidget.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜number.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜password.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜radio_option.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜radio.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜search.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜select_date.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜select_option.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜select.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜splitdatetime.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜splithiddendatetime.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜tel.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜text.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜textarea.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜time.html
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜url.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜attrs.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜div.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜field.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜label.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜p.html
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📜table.html
┃ ┃ ┃   ┃ ┃ ┃     ┗ 📜ul.html
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜boundfield.py
┃ ┃ ┃   ┃ ┃ ┣ 📜fields.py
┃ ┃ ┃   ┃ ┃ ┣ 📜forms.py
┃ ┃ ┃   ┃ ┃ ┣ 📜formsets.py
┃ ┃ ┃   ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┣ 📜renderers.py
┃ ┃ ┃   ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┗ 📜widgets.py
┃ ┃ ┃   ┃ ┣ 📂http
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cookie.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜multipartparser.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜request.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜response.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜cookie.py
┃ ┃ ┃   ┃ ┃ ┣ 📜multipartparser.py
┃ ┃ ┃   ┃ ┃ ┣ 📜request.py
┃ ┃ ┃   ┃ ┃ ┗ 📜response.py
┃ ┃ ┃   ┃ ┣ 📂middleware
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜clickjacking.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜common.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜csrf.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜gzip.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜http.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜locale.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜security.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┣ 📜clickjacking.py
┃ ┃ ┃   ┃ ┃ ┣ 📜common.py
┃ ┃ ┃   ┃ ┃ ┣ 📜csrf.py
┃ ┃ ┃   ┃ ┃ ┣ 📜gzip.py
┃ ┃ ┃   ┃ ┃ ┣ 📜http.py
┃ ┃ ┃   ┃ ┃ ┣ 📜locale.py
┃ ┃ ┃   ┃ ┃ ┗ 📜security.py
┃ ┃ ┃   ┃ ┣ 📂template
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜autoreload.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜context_processors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜context.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜defaultfilters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜defaulttags.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜engine.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜library.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜loader_tags.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜loader.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜response.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜smartif.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂backends
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜django.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜dummy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜jinja2.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜django.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dummy.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜jinja2.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┣ 📂loaders
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜app_directories.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cached.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filesystem.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜locmem.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜app_directories.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cached.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filesystem.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜locmem.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜autoreload.py
┃ ┃ ┃   ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┣ 📜context_processors.py
┃ ┃ ┃   ┃ ┃ ┣ 📜context.py
┃ ┃ ┃   ┃ ┃ ┣ 📜defaultfilters.py
┃ ┃ ┃   ┃ ┃ ┣ 📜defaulttags.py
┃ ┃ ┃   ┃ ┃ ┣ 📜engine.py
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┣ 📜library.py
┃ ┃ ┃   ┃ ┃ ┣ 📜loader_tags.py
┃ ┃ ┃   ┃ ┃ ┣ 📜loader.py
┃ ┃ ┃   ┃ ┃ ┣ 📜response.py
┃ ┃ ┃   ┃ ┃ ┣ 📜smartif.py
┃ ┃ ┃   ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┣ 📂templatetags
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜i18n.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜l10n.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜static.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜tz.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┣ 📜i18n.py
┃ ┃ ┃   ┃ ┃ ┣ 📜l10n.py
┃ ┃ ┃   ┃ ┃ ┣ 📜static.py
┃ ┃ ┃   ┃ ┃ ┗ 📜tz.py
┃ ┃ ┃   ┃ ┣ 📂test
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜client.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜html.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜runner.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜selenium.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜signals.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜testcases.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜client.py
┃ ┃ ┃   ┃ ┃ ┣ 📜html.py
┃ ┃ ┃   ┃ ┃ ┣ 📜runner.py
┃ ┃ ┃   ┃ ┃ ┣ 📜selenium.py
┃ ┃ ┃   ┃ ┃ ┣ 📜signals.py
┃ ┃ ┃   ┃ ┃ ┣ 📜testcases.py
┃ ┃ ┃   ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┣ 📂urls
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜conf.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜converters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜resolvers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┣ 📜conf.py
┃ ┃ ┃   ┃ ┃ ┣ 📜converters.py
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┣ 📜resolvers.py
┃ ┃ ┃   ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┣ 📂utils
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_os.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜archive.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜asyncio.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜autoreload.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜choices.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜connection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜crypto.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜datastructures.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dateformat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dateparse.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜deconstruct.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜decorators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜deprecation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜duration.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜encoding.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜feedgenerator.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜functional.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜hashable.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜html.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜http.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜inspect.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ipv6.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜itercompat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜log.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜lorem_ipsum.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜module_loading.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜numberformat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜regex_helper.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜safestring.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜termcolors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜text.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜timesince.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜timezone.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜tree.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜xmlutils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂translation
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜reloader.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜template.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜trans_null.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜trans_real.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜reloader.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜template.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜trans_null.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜trans_real.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜_os.py
┃ ┃ ┃   ┃ ┃ ┣ 📜archive.py
┃ ┃ ┃   ┃ ┃ ┣ 📜asyncio.py
┃ ┃ ┃   ┃ ┃ ┣ 📜autoreload.py
┃ ┃ ┃   ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┣ 📜choices.py
┃ ┃ ┃   ┃ ┃ ┣ 📜connection.py
┃ ┃ ┃   ┃ ┃ ┣ 📜crypto.py
┃ ┃ ┃   ┃ ┃ ┣ 📜datastructures.py
┃ ┃ ┃   ┃ ┃ ┣ 📜dateformat.py
┃ ┃ ┃   ┃ ┃ ┣ 📜dateparse.py
┃ ┃ ┃   ┃ ┃ ┣ 📜dates.py
┃ ┃ ┃   ┃ ┃ ┣ 📜deconstruct.py
┃ ┃ ┃   ┃ ┃ ┣ 📜decorators.py
┃ ┃ ┃   ┃ ┃ ┣ 📜deprecation.py
┃ ┃ ┃   ┃ ┃ ┣ 📜duration.py
┃ ┃ ┃   ┃ ┃ ┣ 📜encoding.py
┃ ┃ ┃   ┃ ┃ ┣ 📜feedgenerator.py
┃ ┃ ┃   ┃ ┃ ┣ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┣ 📜functional.py
┃ ┃ ┃   ┃ ┃ ┣ 📜hashable.py
┃ ┃ ┃   ┃ ┃ ┣ 📜html.py
┃ ┃ ┃   ┃ ┃ ┣ 📜http.py
┃ ┃ ┃   ┃ ┃ ┣ 📜inspect.py
┃ ┃ ┃   ┃ ┃ ┣ 📜ipv6.py
┃ ┃ ┃   ┃ ┃ ┣ 📜itercompat.py
┃ ┃ ┃   ┃ ┃ ┣ 📜log.py
┃ ┃ ┃   ┃ ┃ ┣ 📜lorem_ipsum.py
┃ ┃ ┃   ┃ ┃ ┣ 📜module_loading.py
┃ ┃ ┃   ┃ ┃ ┣ 📜numberformat.py
┃ ┃ ┃   ┃ ┃ ┣ 📜regex_helper.py
┃ ┃ ┃   ┃ ┃ ┣ 📜safestring.py
┃ ┃ ┃   ┃ ┃ ┣ 📜termcolors.py
┃ ┃ ┃   ┃ ┃ ┣ 📜text.py
┃ ┃ ┃   ┃ ┃ ┣ 📜timesince.py
┃ ┃ ┃   ┃ ┃ ┣ 📜timezone.py
┃ ┃ ┃   ┃ ┃ ┣ 📜tree.py
┃ ┃ ┃   ┃ ┃ ┣ 📜version.py
┃ ┃ ┃   ┃ ┃ ┗ 📜xmlutils.py
┃ ┃ ┃   ┃ ┣ 📂views
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜csrf.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜debug.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜defaults.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜i18n.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜static.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂decorators
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜clickjacking.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜common.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜csrf.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜debug.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜gzip.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜http.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜vary.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜clickjacking.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜common.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜csrf.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜debug.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜gzip.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜http.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜vary.py
┃ ┃ ┃   ┃ ┃ ┣ 📂generic
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜dates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜detail.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜edit.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜list.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dates.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜detail.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜edit.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜list.py
┃ ┃ ┃   ┃ ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜csrf_403.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜default_urlconf.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜directory_index.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜i18n_catalog.js
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜technical_404.html
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜technical_500.html
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜technical_500.txt
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜csrf.py
┃ ┃ ┃   ┃ ┃ ┣ 📜debug.py
┃ ┃ ┃   ┃ ┃ ┣ 📜defaults.py
┃ ┃ ┃   ┃ ┃ ┣ 📜i18n.py
┃ ┃ ┃   ┃ ┃ ┗ 📜static.py
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┗ 📜shortcuts.py
┃ ┃ ┃   ┣ 📂django_cors_headers-4.8.0.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜REQUESTED
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂django-5.2.6.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┣ 📜AUTHORS
┃ ┃ ┃   ┃ ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE.python
┃ ┃ ┃   ┃ ┣ 📜entry_points.txt
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜REQUESTED
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂djangorestframework_simplejwt-5.5.1.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜REQUESTED
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂djangorestframework-3.16.1.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE.md
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜REQUESTED
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂jwt
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜algorithms.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜api_jwk.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜api_jws.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜api_jwt.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜help.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜jwk_set_cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜jwks_client.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜types.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜warnings.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜algorithms.py
┃ ┃ ┃   ┃ ┣ 📜api_jwk.py
┃ ┃ ┃   ┃ ┣ 📜api_jws.py
┃ ┃ ┃   ┃ ┣ 📜api_jwt.py
┃ ┃ ┃   ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┣ 📜help.py
┃ ┃ ┃   ┃ ┣ 📜jwk_set_cache.py
┃ ┃ ┃   ┃ ┣ 📜jwks_client.py
┃ ┃ ┃   ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┣ 📜types.py
┃ ┃ ┃   ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┗ 📜warnings.py
┃ ┃ ┃   ┣ 📂PIL
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_binary.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_deprecate.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_tkinter_finder.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_typing.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜AvifImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜BdfFontFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜BlpImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜BmpImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜BufrStubImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ContainerIO.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜CurImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜DcxImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜DdsImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜EpsImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ExifTags.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜features.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜FitsImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜FliImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜FontFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜FpxImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜FtexImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜GbrImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜GdImageFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜GifImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜GimpGradientFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜GimpPaletteFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜GribStubImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜Hdf5StubImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜IcnsImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜IcoImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜Image.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageChops.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageCms.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageColor.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageDraw.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageDraw2.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageEnhance.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageFilter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageFont.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageGrab.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageMath.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageMode.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageMorph.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageOps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImagePalette.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImagePath.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageQt.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageSequence.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageShow.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageStat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageTk.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageTransform.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImageWin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜ImtImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜IptcImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜Jpeg2KImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜JpegImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜JpegPresets.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜McIdasImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜MicImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜MpegImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜MpoImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜MspImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PaletteFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PalmImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PcdImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PcfFontFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PcxImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PdfImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PdfParser.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PixarImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PngImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PpmImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PsdImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜PSDraw.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜QoiImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜report.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜SgiImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜SpiderImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜SunImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜TarIO.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜TgaImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜TiffImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜TiffTags.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜WalImageFile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜WebPImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜WmfImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜XbmImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜XpmImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜XVThumbImagePlugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┣ 📜_avif.cp311-win_amd64.pyd
┃ ┃ ┃   ┃ ┣ 📜_avif.pyi
┃ ┃ ┃   ┃ ┣ 📜_binary.py
┃ ┃ ┃   ┃ ┣ 📜_deprecate.py
┃ ┃ ┃   ┃ ┣ 📜_imaging.cp311-win_amd64.pyd
┃ ┃ ┃   ┃ ┣ 📜_imaging.pyi
┃ ┃ ┃   ┃ ┣ 📜_imagingcms.cp311-win_amd64.pyd
┃ ┃ ┃   ┃ ┣ 📜_imagingcms.pyi
┃ ┃ ┃   ┃ ┣ 📜_imagingft.cp311-win_amd64.pyd
┃ ┃ ┃   ┃ ┣ 📜_imagingft.pyi
┃ ┃ ┃   ┃ ┣ 📜_imagingmath.cp311-win_amd64.pyd
┃ ┃ ┃   ┃ ┣ 📜_imagingmath.pyi
┃ ┃ ┃   ┃ ┣ 📜_imagingmorph.cp311-win_amd64.pyd
┃ ┃ ┃   ┃ ┣ 📜_imagingmorph.pyi
┃ ┃ ┃   ┃ ┣ 📜_imagingtk.cp311-win_amd64.pyd
┃ ┃ ┃   ┃ ┣ 📜_imagingtk.pyi
┃ ┃ ┃   ┃ ┣ 📜_tkinter_finder.py
┃ ┃ ┃   ┃ ┣ 📜_typing.py
┃ ┃ ┃   ┃ ┣ 📜_util.py
┃ ┃ ┃   ┃ ┣ 📜_version.py
┃ ┃ ┃   ┃ ┣ 📜_webp.cp311-win_amd64.pyd
┃ ┃ ┃   ┃ ┣ 📜_webp.pyi
┃ ┃ ┃   ┃ ┣ 📜AvifImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜BdfFontFile.py
┃ ┃ ┃   ┃ ┣ 📜BlpImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜BmpImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜BufrStubImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜ContainerIO.py
┃ ┃ ┃   ┃ ┣ 📜CurImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜DcxImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜DdsImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜EpsImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜ExifTags.py
┃ ┃ ┃   ┃ ┣ 📜features.py
┃ ┃ ┃   ┃ ┣ 📜FitsImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜FliImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜FontFile.py
┃ ┃ ┃   ┃ ┣ 📜FpxImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜FtexImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜GbrImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜GdImageFile.py
┃ ┃ ┃   ┃ ┣ 📜GifImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜GimpGradientFile.py
┃ ┃ ┃   ┃ ┣ 📜GimpPaletteFile.py
┃ ┃ ┃   ┃ ┣ 📜GribStubImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜Hdf5StubImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜IcnsImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜IcoImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜Image.py
┃ ┃ ┃   ┃ ┣ 📜ImageChops.py
┃ ┃ ┃   ┃ ┣ 📜ImageCms.py
┃ ┃ ┃   ┃ ┣ 📜ImageColor.py
┃ ┃ ┃   ┃ ┣ 📜ImageDraw.py
┃ ┃ ┃   ┃ ┣ 📜ImageDraw2.py
┃ ┃ ┃   ┃ ┣ 📜ImageEnhance.py
┃ ┃ ┃   ┃ ┣ 📜ImageFile.py
┃ ┃ ┃   ┃ ┣ 📜ImageFilter.py
┃ ┃ ┃   ┃ ┣ 📜ImageFont.py
┃ ┃ ┃   ┃ ┣ 📜ImageGrab.py
┃ ┃ ┃   ┃ ┣ 📜ImageMath.py
┃ ┃ ┃   ┃ ┣ 📜ImageMode.py
┃ ┃ ┃   ┃ ┣ 📜ImageMorph.py
┃ ┃ ┃   ┃ ┣ 📜ImageOps.py
┃ ┃ ┃   ┃ ┣ 📜ImagePalette.py
┃ ┃ ┃   ┃ ┣ 📜ImagePath.py
┃ ┃ ┃   ┃ ┣ 📜ImageQt.py
┃ ┃ ┃   ┃ ┣ 📜ImageSequence.py
┃ ┃ ┃   ┃ ┣ 📜ImageShow.py
┃ ┃ ┃   ┃ ┣ 📜ImageStat.py
┃ ┃ ┃   ┃ ┣ 📜ImageTk.py
┃ ┃ ┃   ┃ ┣ 📜ImageTransform.py
┃ ┃ ┃   ┃ ┣ 📜ImageWin.py
┃ ┃ ┃   ┃ ┣ 📜ImImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜ImtImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜IptcImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜Jpeg2KImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜JpegImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜JpegPresets.py
┃ ┃ ┃   ┃ ┣ 📜McIdasImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜MicImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜MpegImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜MpoImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜MspImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PaletteFile.py
┃ ┃ ┃   ┃ ┣ 📜PalmImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PcdImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PcfFontFile.py
┃ ┃ ┃   ┃ ┣ 📜PcxImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PdfImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PdfParser.py
┃ ┃ ┃   ┃ ┣ 📜PixarImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PngImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PpmImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PsdImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜PSDraw.py
┃ ┃ ┃   ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┣ 📜QoiImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜report.py
┃ ┃ ┃   ┃ ┣ 📜SgiImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜SpiderImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜SunImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜TarIO.py
┃ ┃ ┃   ┃ ┣ 📜TgaImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜TiffImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜TiffTags.py
┃ ┃ ┃   ┃ ┣ 📜WalImageFile.py
┃ ┃ ┃   ┃ ┣ 📜WebPImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜WmfImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜XbmImagePlugin.py
┃ ┃ ┃   ┃ ┣ 📜XpmImagePlugin.py
┃ ┃ ┃   ┃ ┗ 📜XVThumbImagePlugin.py
┃ ┃ ┃   ┣ 📂pillow-11.3.0.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜REQUESTED
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┣ 📜WHEEL
┃ ┃ ┃   ┃ ┗ 📜zip-safe
┃ ┃ ┃   ┣ 📂pip
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜__pip-runner__.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂_internal
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build_env.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜configuration.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜main.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜pyproject.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜self_outdated_check.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜wheel_builder.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂cli
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜autocompletion.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base_command.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cmdoptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜command_context.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜index_command.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜main_parser.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜main.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜parser.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜progress_bars.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜req_command.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜spinners.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜status_codes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜autocompletion.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base_command.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cmdoptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜command_context.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜index_command.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜main_parser.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜main.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜parser.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜progress_bars.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜req_command.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜spinners.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜status_codes.py
┃ ┃ ┃   ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜check.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜completion.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜configuration.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜debug.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜download.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜freeze.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜hash.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜help.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜index.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜inspect.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜install.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜list.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜lock.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜search.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜show.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜uninstall.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜check.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜completion.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜configuration.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜debug.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜download.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜freeze.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜hash.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜help.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜index.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜inspect.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜list.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜lock.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜search.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜show.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜uninstall.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜wheel.py
┃ ┃ ┃   ┃ ┃ ┣ 📂distributions
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜installed.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sdist.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜installed.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sdist.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜wheel.py
┃ ┃ ┃   ┃ ┃ ┣ 📂index
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜collector.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜package_finder.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜sources.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜collector.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜package_finder.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜sources.py
┃ ┃ ┃   ┃ ┃ ┣ 📂locations
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_distutils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_sysconfig.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_distutils.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_sysconfig.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜base.py
┃ ┃ ┃   ┃ ┃ ┣ 📂metadata
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_json.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜pkg_resources.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂importlib
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜_dists.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜_envs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_dists.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_envs.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_json.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜pkg_resources.py
┃ ┃ ┃   ┃ ┃ ┣ 📂models
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜candidate.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜direct_url.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜format_control.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜index.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜installation_report.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜link.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜pylock.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜scheme.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜search_scope.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜selection_prefs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜target_python.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜candidate.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜direct_url.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜format_control.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜index.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜installation_report.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜link.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜pylock.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜scheme.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜search_scope.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜selection_prefs.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜target_python.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜wheel.py
┃ ┃ ┃   ┃ ┃ ┣ 📂network
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜auth.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜download.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜lazy_wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜session.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜xmlrpc.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜auth.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜download.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜lazy_wheel.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜session.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜xmlrpc.py
┃ ┃ ┃   ┃ ┃ ┣ 📂operations
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜check.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜freeze.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜prepare.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂build
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜build_tracker.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata_editable.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata_legacy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜metadata.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel_editable.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜wheel_legacy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜build_tracker.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜metadata_editable.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜metadata_legacy.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜metadata.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜wheel_editable.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜wheel_legacy.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wheel.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂install
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜editable_legacy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜editable_legacy.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wheel.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜check.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜freeze.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜prepare.py
┃ ┃ ┃   ┃ ┃ ┣ 📂req
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜constructors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜req_dependency_group.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜req_file.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜req_install.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜req_set.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜req_uninstall.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜constructors.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜req_dependency_group.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜req_file.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜req_install.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜req_set.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜req_uninstall.py
┃ ┃ ┃   ┃ ┃ ┣ 📂resolution
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂legacy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜resolver.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜resolver.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂resolvelib
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜candidates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜factory.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜found_candidates.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜provider.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜reporter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜resolver.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜candidates.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜factory.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜found_candidates.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜provider.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜reporter.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜requirements.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜resolver.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜base.py
┃ ┃ ┃   ┃ ┃ ┣ 📂utils
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_jaraco_text.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_log.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜appdirs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compatibility_tags.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜datetime.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜deprecation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜direct_url_helpers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜egg_link.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜entrypoints.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filesystem.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filetypes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜glibc.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜hashes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜logging.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜misc.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜packaging.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜retry.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜setuptools_build.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜subprocess.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜temp_dir.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜unpacking.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜virtualenv.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_jaraco_text.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_log.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜appdirs.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜compatibility_tags.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜datetime.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜deprecation.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜direct_url_helpers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜egg_link.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜entrypoints.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filesystem.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filetypes.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜glibc.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜hashes.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜logging.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜misc.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜packaging.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜retry.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜setuptools_build.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜subprocess.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜temp_dir.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜unpacking.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜virtualenv.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜wheel.py
┃ ┃ ┃   ┃ ┃ ┣ 📂vcs
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜bazaar.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜git.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜mercurial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜subversion.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜versioncontrol.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜bazaar.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜git.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜mercurial.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜subversion.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜versioncontrol.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜build_env.py
┃ ┃ ┃   ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┣ 📜configuration.py
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┣ 📜main.py
┃ ┃ ┃   ┃ ┃ ┣ 📜pyproject.py
┃ ┃ ┃   ┃ ┃ ┣ 📜self_outdated_check.py
┃ ┃ ┃   ┃ ┃ ┗ 📜wheel_builder.py
┃ ┃ ┃   ┃ ┣ 📂_vendor
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂cachecontrol
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_cmd.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜adapter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜controller.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filewrapper.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜heuristics.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜serialize.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wrapper.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂caches
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜file_cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜redis_cache.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜file_cache.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜redis_cache.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_cmd.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜adapter.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cache.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜controller.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filewrapper.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜heuristics.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜serialize.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜wrapper.py
┃ ┃ ┃   ┃ ┃ ┣ 📂certifi
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜core.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cacert.pem
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜core.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┣ 📂dependency_groups
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_implementation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_lint_dependency_groups.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_pip_wrapper.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_toml_compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_implementation.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_lint_dependency_groups.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_pip_wrapper.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_toml_compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┣ 📂distlib
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜resources.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜scripts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜resources.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜scripts.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜t32.exe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜t64-arm.exe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜t64.exe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜util.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜w32.exe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜w64-arm.exe
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜w64.exe
┃ ┃ ┃   ┃ ┃ ┣ 📂distro
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜distro.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜distro.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┣ 📂idna
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜codec.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜core.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜idnadata.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜intranges.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜package_data.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜uts46data.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜codec.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜core.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜idnadata.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜intranges.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜package_data.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜uts46data.py
┃ ┃ ┃   ┃ ┃ ┣ 📂msgpack
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ext.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜fallback.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ext.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜fallback.py
┃ ┃ ┃   ┃ ┃ ┣ 📂packaging
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_elffile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_manylinux.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_musllinux.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_parser.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_structures.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_tokenizer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜markers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜metadata.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜requirements.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜specifiers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜tags.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜_spdx.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_spdx.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_elffile.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_manylinux.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_musllinux.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_parser.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_structures.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_tokenizer.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜markers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜metadata.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜requirements.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜specifiers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜tags.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜version.py
┃ ┃ ┃   ┃ ┃ ┣ 📂pkg_resources
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📂platformdirs
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜android.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜api.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜macos.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜unix.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜windows.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜android.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜api.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜macos.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜unix.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜version.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜windows.py
┃ ┃ ┃   ┃ ┃ ┣ 📂pygments
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜console.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜formatter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜lexer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜modeline.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜plugin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜regexopt.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜scanner.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sphinxext.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜style.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜token.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜unistring.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂filters
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂formatters
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜_mapping.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_mapping.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂lexers
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜_mapping.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜python.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_mapping.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜python.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂styles
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜_mapping.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_mapping.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜console.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filter.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜formatter.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜lexer.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜modeline.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜plugin.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜regexopt.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜scanner.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sphinxext.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜style.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜token.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜unistring.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜util.py
┃ ┃ ┃   ┃ ┃ ┣ 📂pyproject_hooks
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_impl.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂_in_process
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜_in_process.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_in_process.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_impl.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┣ 📂requests
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__version__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_internal_utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜adapters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜api.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜auth.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜certs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cookies.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜help.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜hooks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜packages.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sessions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜status_codes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜structures.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__version__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_internal_utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜adapters.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜api.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜auth.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜certs.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cookies.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜help.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜hooks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜packages.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sessions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜status_codes.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜structures.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┣ 📂resolvelib
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜providers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜reporters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜structs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂resolvers
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜abstract.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜criterion.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜resolution.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜abstract.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜criterion.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜resolution.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜providers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜reporters.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜structs.py
┃ ┃ ┃   ┃ ┃ ┣ 📂rich
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_cell_widths.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_emoji_codes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_emoji_replace.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_export_format.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_extension.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_fileno.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_inspect.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_log_render.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_loop.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_null_file.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_palettes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_pick.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_ratio.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_spinners.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_stack.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_timer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_win32_console.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_windows_renderer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_windows.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_wrap.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜abc.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜align.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ansi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜bar.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜box.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜cells.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜color_triplet.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜color.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜columns.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜console.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜constrain.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜containers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜control.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜default_styles.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜diagnose.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜emoji.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜errors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜file_proxy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filesize.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜highlighter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜json.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜jupyter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜layout.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜live_render.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜live.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜logging.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜markup.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜measure.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜padding.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜pager.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜palette.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜panel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜pretty.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜progress_bar.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜progress.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜prompt.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜protocol.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜region.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜repr.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜rule.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜scope.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜screen.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜segment.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜spinner.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜status.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜style.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜styled.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜syntax.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜table.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜terminal_theme.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜text.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜theme.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜themes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜traceback.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜tree.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_cell_widths.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_emoji_codes.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_emoji_replace.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_export_format.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_extension.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_fileno.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_inspect.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_log_render.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_loop.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_null_file.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_palettes.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_pick.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_ratio.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_spinners.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_stack.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_timer.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_win32_console.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_windows_renderer.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_windows.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_wrap.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜abc.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜align.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ansi.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜bar.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜box.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cells.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜color_triplet.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜color.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜columns.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜console.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜constrain.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜containers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜control.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜default_styles.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜diagnose.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜emoji.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜errors.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜file_proxy.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filesize.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜highlighter.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜json.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜jupyter.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜layout.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜live_render.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜live.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜logging.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜markup.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜measure.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜padding.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜pager.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜palette.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜panel.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜pretty.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜progress_bar.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜progress.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜prompt.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜protocol.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜region.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜repr.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜rule.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜scope.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜screen.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜segment.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜spinner.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜status.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜style.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜styled.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜syntax.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜table.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜terminal_theme.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜text.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜theme.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜themes.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜traceback.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜tree.py
┃ ┃ ┃   ┃ ┃ ┣ 📂tomli
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_parser.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_re.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_types.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_parser.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_re.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_types.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┣ 📂tomli_w
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_writer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_writer.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┣ 📂truststore
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_api.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_macos.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_openssl.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_ssl_constants.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_windows.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_api.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_macos.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_openssl.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_ssl_constants.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_windows.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜py.typed
┃ ┃ ┃   ┃ ┃ ┣ 📂urllib3
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_collections.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜connection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜connectionpool.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜fields.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜filepost.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜poolmanager.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜request.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜response.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂contrib
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜_appengine_environ.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜appengine.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜ntlmpool.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜pyopenssl.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜securetransport.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜socks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂_securetransport
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bindings.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜low_level.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜bindings.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜low_level.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_appengine_environ.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜appengine.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ntlmpool.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜pyopenssl.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜securetransport.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜socks.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂packages
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜six.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂backports
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜makefile.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜weakref_finalize.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜makefile.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜weakref_finalize.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜six.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂util
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜connection.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜queue.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜request.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜response.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜retry.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜ssl_match_hostname.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜ssltransport.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜timeout.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜url.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜wait.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜connection.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜proxy.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜queue.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜request.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜response.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜retry.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ssl_.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ssl_match_hostname.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ssltransport.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜timeout.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜url.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜wait.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_collections.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_version.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜connection.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜connectionpool.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜fields.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filepost.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜poolmanager.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜request.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜response.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┗ 📜vendor.txt
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┣ 📜__pip-runner__.py
┃ ┃ ┃   ┃ ┗ 📜py.typed
┃ ┃ ┃   ┣ 📂pip-25.2.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┣ 📂src
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂pip
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📂_vendor
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂cachecontrol
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂certifi
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂dependency_groups
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂distlib
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂distro
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂idna
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE.md
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂msgpack
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜COPYING
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂packaging
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜LICENSE.APACHE
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE.BSD
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂pkg_resources
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂platformdirs
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂pygments
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂pyproject_hooks
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂requests
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂resolvelib
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂rich
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂tomli
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE-HEADER
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂tomli_w
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┣ 📂truststore
┃ ┃ ┃   ┃ ┃ ┃     ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┃ ┃     ┗ 📂urllib3
┃ ┃ ┃   ┃ ┃ ┃       ┗ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┃ ┣ 📜AUTHORS.txt
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE.txt
┃ ┃ ┃   ┃ ┣ 📜entry_points.txt
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜REQUESTED
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂pkg_resources
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂_vendor
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜appdirs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜zipp.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂importlib_resources
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_adapters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_common.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_itertools.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_legacy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜abc.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜readers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜simple.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_adapters.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_common.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_itertools.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_legacy.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜abc.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜readers.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜simple.py
┃ ┃ ┃   ┃ ┃ ┣ 📂jaraco
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜context.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜functools.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂text
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜context.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜functools.py
┃ ┃ ┃   ┃ ┃ ┣ 📂more_itertools
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜more.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜recipes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜more.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜recipes.py
┃ ┃ ┃   ┃ ┃ ┣ 📂packaging
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__about__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_manylinux.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_musllinux.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_structures.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜markers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜requirements.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜specifiers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜tags.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__about__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_manylinux.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_musllinux.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_structures.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜markers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜requirements.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜specifiers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜tags.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜version.py
┃ ┃ ┃   ┃ ┃ ┣ 📂pyparsing
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜actions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜common.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜core.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜results.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜unicode.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂diagram
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜actions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜common.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜core.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜helpers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜results.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜testing.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜unicode.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜util.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜appdirs.py
┃ ┃ ┃   ┃ ┃ ┗ 📜zipp.py
┃ ┃ ┃   ┃ ┣ 📂extern
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┣ 📂PyJWT-2.10.1.dist-info
┃ ┃ ┃   ┃ ┣ 📜AUTHORS.rst
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂qrcode
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜console_scripts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜constants.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜LUT.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜main.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜release.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜util.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂compat
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜etree.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜png.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜etree.py
┃ ┃ ┃   ┃ ┃ ┗ 📜png.py
┃ ┃ ┃   ┃ ┣ 📂image
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜pil.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜pure.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜styledpil.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜svg.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂styles
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜colormasks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂moduledrawers
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜base.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜pil.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜svg.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜pil.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜svg.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜colormasks.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┃ ┣ 📜pil.py
┃ ┃ ┃   ┃ ┃ ┣ 📜pure.py
┃ ┃ ┃   ┃ ┃ ┣ 📜styledpil.py
┃ ┃ ┃   ┃ ┃ ┗ 📜svg.py
┃ ┃ ┃   ┃ ┣ 📂tests
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜consts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test_example.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test_qrcode_pil.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test_qrcode_pypng.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test_qrcode_svg.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test_qrcode.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test_release.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test_script.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜test_util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜consts.py
┃ ┃ ┃   ┃ ┃ ┣ 📜test_example.py
┃ ┃ ┃   ┃ ┃ ┣ 📜test_qrcode_pil.py
┃ ┃ ┃   ┃ ┃ ┣ 📜test_qrcode_pypng.py
┃ ┃ ┃   ┃ ┃ ┣ 📜test_qrcode_svg.py
┃ ┃ ┃   ┃ ┃ ┣ 📜test_qrcode.py
┃ ┃ ┃   ┃ ┃ ┣ 📜test_release.py
┃ ┃ ┃   ┃ ┃ ┣ 📜test_script.py
┃ ┃ ┃   ┃ ┃ ┗ 📜test_util.py
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜base.py
┃ ┃ ┃   ┃ ┣ 📜console_scripts.py
┃ ┃ ┃   ┃ ┣ 📜constants.py
┃ ┃ ┃   ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┣ 📜LUT.py
┃ ┃ ┃   ┃ ┣ 📜main.py
┃ ┃ ┃   ┃ ┣ 📜release.py
┃ ┃ ┃   ┃ ┗ 📜util.py
┃ ┃ ┃   ┣ 📂qrcode-8.2.dist-info
┃ ┃ ┃   ┃ ┣ 📜entry_points.txt
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜REQUESTED
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂rest_framework
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜authentication.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜checks.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜decorators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜documentation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜fields.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜filters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜generics.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜metadata.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜mixins.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜negotiation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜pagination.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜parsers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜permissions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜relations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜renderers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜request.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜response.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜reverse.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜routers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜serializers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜settings.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜status.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜throttling.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜urlpatterns.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜validators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜versioning.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜viewsets.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂authtoken
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜admin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜serializers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜drf_create_token.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜drf_create_token.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0002_auto_20160226_1747.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0003_tokenproxy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0004_alter_tokenproxy_options.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0002_auto_20160226_1747.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0003_tokenproxy.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜0004_alter_tokenproxy_options.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃   ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┃ ┣ 📜serializers.py
┃ ┃ ┃   ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┣ 📂ach
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂az
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂be
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂bg
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ca
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ca_ES
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂da
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂el
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂el_GR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂en
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂en_AU
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂en_CA
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂en_US
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂et
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂fa_IR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂fi
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂fr_CA
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂gl
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂gl_ES
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂he_IL
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂hu
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂hy
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂id
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂it
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ja
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂kk
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ko_KR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂lt
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂lv
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂mk
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂nb
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ne_NP
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂nl
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂nn
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂no
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂pl
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂pt
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂pt_PT
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ru
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂ru_RU
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂sk
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂th
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂tr_TR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂uk
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂vi
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂zh_CN
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂zh_Hans
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┣ 📂zh_Hant
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┗ 📂zh_TW
┃ ┃ ┃   ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃     ┗ 📜django.mo
┃ ┃ ┃   ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜generateschema.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜generateschema.py
┃ ┃ ┃   ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📂schemas
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜coreapi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜generators.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜inspectors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜openapi.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜coreapi.py
┃ ┃ ┃   ┃ ┃ ┣ 📜generators.py
┃ ┃ ┃   ┃ ┃ ┣ 📜inspectors.py
┃ ┃ ┃   ┃ ┃ ┣ 📜openapi.py
┃ ┃ ┃   ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┗ 📜views.py
┃ ┃ ┃   ┃ ┣ 📂static
┃ ┃ ┃   ┃ ┃ ┗ 📂rest_framework
┃ ┃ ┃   ┃ ┃   ┣ 📂css
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜bootstrap-theme.min.css
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜bootstrap-theme.min.css.map
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜bootstrap-tweaks.css
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜bootstrap.min.css
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜bootstrap.min.css.map
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜default.css
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜font-awesome-4.0.3.css
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜prettify.css
┃ ┃ ┃   ┃ ┃   ┣ 📂docs
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📂css
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜base.css
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜highlight.css
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┗ 📜jquery.json-view.min.css
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📂img
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜favicon.ico
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┗ 📜grid.png
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📂js
┃ ┃ ┃   ┃ ┃   ┃   ┣ 📜api.js
┃ ┃ ┃   ┃ ┃   ┃   ┣ 📜highlight.pack.js
┃ ┃ ┃   ┃ ┃   ┃   ┗ 📜jquery.json-view.min.js
┃ ┃ ┃   ┃ ┃   ┣ 📂fonts
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜fontawesome-webfont.eot
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜fontawesome-webfont.svg
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜fontawesome-webfont.ttf
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜fontawesome-webfont.woff
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜glyphicons-halflings-regular.eot
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜glyphicons-halflings-regular.svg
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜glyphicons-halflings-regular.ttf
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜glyphicons-halflings-regular.woff
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜glyphicons-halflings-regular.woff2
┃ ┃ ┃   ┃ ┃   ┣ 📂img
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜glyphicons-halflings-white.png
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜glyphicons-halflings.png
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜grid.png
┃ ┃ ┃   ┃ ┃   ┗ 📂js
┃ ┃ ┃   ┃ ┃     ┣ 📜ajax-form.js
┃ ┃ ┃   ┃ ┃     ┣ 📜bootstrap.min.js
┃ ┃ ┃   ┃ ┃     ┣ 📜coreapi-0.1.1.js
┃ ┃ ┃   ┃ ┃     ┣ 📜csrf.js
┃ ┃ ┃   ┃ ┃     ┣ 📜default.js
┃ ┃ ┃   ┃ ┃     ┣ 📜jquery-3.7.1.min.js
┃ ┃ ┃   ┃ ┃     ┣ 📜load-ajax-form.js
┃ ┃ ┃   ┃ ┃     ┗ 📜prettify-min.js
┃ ┃ ┃   ┃ ┣ 📂templates
┃ ┃ ┃   ┃ ┃ ┗ 📂rest_framework
┃ ┃ ┃   ┃ ┃   ┣ 📂admin
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜detail.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜dict_value.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜list_value.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜list.html
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜simple_list_value.html
┃ ┃ ┃   ┃ ┃   ┣ 📂docs
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📂auth
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜basic.html
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜session.html
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┗ 📜token.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📂langs
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜javascript-intro.html
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜javascript.html
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜python-intro.html
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜python.html
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┣ 📜shell-intro.html
┃ ┃ ┃   ┃ ┃   ┃ ┃ ┗ 📜shell.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜document.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜error.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜index.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜interact.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜link.html
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜sidebar.html
┃ ┃ ┃   ┃ ┃   ┣ 📂filters
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜base.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜ordering.html
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜search.html
┃ ┃ ┃   ┃ ┃   ┣ 📂horizontal
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜checkbox_multiple.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜checkbox.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜dict_field.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜fieldset.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜form.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜input.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜list_field.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜list_fieldset.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜radio.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜select_multiple.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜select.html
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜textarea.html
┃ ┃ ┃   ┃ ┃   ┣ 📂inline
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜checkbox_multiple.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜checkbox.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜dict_field.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜fieldset.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜form.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜input.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜list_field.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜list_fieldset.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜radio.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜select_multiple.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜select.html
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜textarea.html
┃ ┃ ┃   ┃ ┃   ┣ 📂pagination
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜numbers.html
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜previous_and_next.html
┃ ┃ ┃   ┃ ┃   ┣ 📂vertical
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜checkbox_multiple.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜checkbox.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜dict_field.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜fieldset.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜form.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜input.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜list_field.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜list_fieldset.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜radio.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜select_multiple.html
┃ ┃ ┃   ┃ ┃   ┃ ┣ 📜select.html
┃ ┃ ┃   ┃ ┃   ┃ ┗ 📜textarea.html
┃ ┃ ┃   ┃ ┃   ┣ 📜admin.html
┃ ┃ ┃   ┃ ┃   ┣ 📜api.html
┃ ┃ ┃   ┃ ┃   ┣ 📜base.html
┃ ┃ ┃   ┃ ┃   ┣ 📜login_base.html
┃ ┃ ┃   ┃ ┃   ┣ 📜login.html
┃ ┃ ┃   ┃ ┃   ┣ 📜raw_data_form.html
┃ ┃ ┃   ┃ ┃   ┗ 📜schema.js
┃ ┃ ┃   ┃ ┣ 📂templatetags
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜rest_framework.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┗ 📜rest_framework.py
┃ ┃ ┃   ┃ ┣ 📂utils
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜breadcrumbs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜encoders.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜field_mapping.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜formatting.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜html.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜humanize_datetime.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜json.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜mediatypes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜model_meta.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜representation.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜serializer_helpers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜timezone.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜urls.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜breadcrumbs.py
┃ ┃ ┃   ┃ ┃ ┣ 📜encoders.py
┃ ┃ ┃   ┃ ┃ ┣ 📜field_mapping.py
┃ ┃ ┃   ┃ ┃ ┣ 📜formatting.py
┃ ┃ ┃   ┃ ┃ ┣ 📜html.py
┃ ┃ ┃   ┃ ┃ ┣ 📜humanize_datetime.py
┃ ┃ ┃   ┃ ┃ ┣ 📜json.py
┃ ┃ ┃   ┃ ┃ ┣ 📜mediatypes.py
┃ ┃ ┃   ┃ ┃ ┣ 📜model_meta.py
┃ ┃ ┃   ┃ ┃ ┣ 📜representation.py
┃ ┃ ┃   ┃ ┃ ┣ 📜serializer_helpers.py
┃ ┃ ┃   ┃ ┃ ┣ 📜timezone.py
┃ ┃ ┃   ┃ ┃ ┗ 📜urls.py
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┣ 📜authentication.py
┃ ┃ ┃   ┃ ┣ 📜checks.py
┃ ┃ ┃   ┃ ┣ 📜compat.py
┃ ┃ ┃   ┃ ┣ 📜decorators.py
┃ ┃ ┃   ┃ ┣ 📜documentation.py
┃ ┃ ┃   ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┣ 📜fields.py
┃ ┃ ┃   ┃ ┣ 📜filters.py
┃ ┃ ┃   ┃ ┣ 📜generics.py
┃ ┃ ┃   ┃ ┣ 📜metadata.py
┃ ┃ ┃   ┃ ┣ 📜mixins.py
┃ ┃ ┃   ┃ ┣ 📜negotiation.py
┃ ┃ ┃   ┃ ┣ 📜pagination.py
┃ ┃ ┃   ┃ ┣ 📜parsers.py
┃ ┃ ┃   ┃ ┣ 📜permissions.py
┃ ┃ ┃   ┃ ┣ 📜relations.py
┃ ┃ ┃   ┃ ┣ 📜renderers.py
┃ ┃ ┃   ┃ ┣ 📜request.py
┃ ┃ ┃   ┃ ┣ 📜response.py
┃ ┃ ┃   ┃ ┣ 📜reverse.py
┃ ┃ ┃   ┃ ┣ 📜routers.py
┃ ┃ ┃   ┃ ┣ 📜serializers.py
┃ ┃ ┃   ┃ ┣ 📜settings.py
┃ ┃ ┃   ┃ ┣ 📜status.py
┃ ┃ ┃   ┃ ┣ 📜test.py
┃ ┃ ┃   ┃ ┣ 📜throttling.py
┃ ┃ ┃   ┃ ┣ 📜urlpatterns.py
┃ ┃ ┃   ┃ ┣ 📜urls.py
┃ ┃ ┃   ┃ ┣ 📜validators.py
┃ ┃ ┃   ┃ ┣ 📜versioning.py
┃ ┃ ┃   ┃ ┣ 📜views.py
┃ ┃ ┃   ┃ ┗ 📜viewsets.py
┃ ┃ ┃   ┣ 📂rest_framework_simplejwt
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜authentication.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜backends.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜serializers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜settings.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜state.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜tokens.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜views.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂locale
┃ ┃ ┃   ┃ ┃ ┣ 📂ar
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂cs
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂de
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂es
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂es_AR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂es_CL
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂fa
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂fa_IR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂fr
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂he_IL
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂id_ID
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂it_IT
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂ko_KR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂nl_NL
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂pl_PL
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂pt_BR
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂ro
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂ru_RU
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂sl
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂sv
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂tr
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┣ 📂uk_UA
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃ ┃   ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃ ┃   ┗ 📜django.po
┃ ┃ ┃   ┃ ┃ ┗ 📂zh_Hans
┃ ┃ ┃   ┃ ┃   ┗ 📂LC_MESSAGES
┃ ┃ ┃   ┃ ┃     ┣ 📜django.mo
┃ ┃ ┃   ┃ ┃     ┗ 📜django.po
┃ ┃ ┃   ┃ ┣ 📂token_blacklist
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜admin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜apps.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜models.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂management
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂commands
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜flushexpiredtokens.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜flushexpiredtokens.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📂migrations
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0002_outstandingtoken_jti_hex.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0003_auto_20171017_2007.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0004_auto_20171017_2013.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0005_remove_outstandingtoken_jti.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0006_auto_20171017_2113.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0007_auto_20171017_2214.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0008_migrate_to_bigautofield.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0010_fix_migrate_to_bigautofield.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0011_linearizes_history.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜0012_alter_outstandingtoken_user.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜0013_alter_blacklistedtoken_options_and_more.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0001_initial.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0002_outstandingtoken_jti_hex.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0003_auto_20171017_2007.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0004_auto_20171017_2013.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0005_remove_outstandingtoken_jti.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0006_auto_20171017_2113.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0007_auto_20171017_2214.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0008_migrate_to_bigautofield.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0010_fix_migrate_to_bigautofield.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0011_linearizes_history.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜0012_alter_outstandingtoken_user.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜0013_alter_blacklistedtoken_options_and_more.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜admin.py
┃ ┃ ┃   ┃ ┃ ┣ 📜apps.py
┃ ┃ ┃   ┃ ┃ ┗ 📜models.py
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜authentication.py
┃ ┃ ┃   ┃ ┣ 📜backends.py
┃ ┃ ┃   ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┣ 📜models.py
┃ ┃ ┃   ┃ ┣ 📜py.typed
┃ ┃ ┃   ┃ ┣ 📜serializers.py
┃ ┃ ┃   ┃ ┣ 📜settings.py
┃ ┃ ┃   ┃ ┣ 📜state.py
┃ ┃ ┃   ┃ ┣ 📜tokens.py
┃ ┃ ┃   ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┗ 📜views.py
┃ ┃ ┃   ┣ 📂setuptools
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_deprecation_warning.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_entry_points.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_imp.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_importlib.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_itertools.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_path.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜_reqs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜archive_util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜build_meta.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜dep_util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜depends.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜discovery.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜dist.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜errors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜extension.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜glob.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜installer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜launch.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜logging.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜monkey.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜msvc.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜namespaces.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜package_index.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜py34compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜sandbox.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜unicode_utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜windows_support.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂_distutils
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_collections.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_functools.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_macos_compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_msvccompiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜archive_util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜bcppcompiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ccompiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cmd.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜config.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜core.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜cygwinccompiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜debug.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dep_util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dir_util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dist.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜errors.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜extension.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜fancy_getopt.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜file_util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filelist.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜log.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜msvc9compiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜msvccompiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py38compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py39compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜spawn.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sysconfig.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜text_file.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜unixccompiler.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜versionpredicate.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂command
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_framework_compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜bdist_dumb.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜bdist_rpm.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜bdist.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜build_clib.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜build_ext.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜build_py.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜build_scripts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜build.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜check.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜clean.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜config.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜install_data.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜install_egg_info.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜install_headers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜install_lib.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜install_scripts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜install.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜py37compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜register.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜sdist.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜upload.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_framework_compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜bdist_dumb.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜bdist_rpm.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜bdist.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build_clib.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build_ext.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build_py.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build_scripts.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜check.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜clean.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜config.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install_data.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install_egg_info.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install_headers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install_lib.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install_scripts.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py37compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜register.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sdist.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜upload.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜_collections.py
┃ ┃ ┃   ┃ ┃ ┣ 📜_functools.py
┃ ┃ ┃   ┃ ┃ ┣ 📜_macos_compat.py
┃ ┃ ┃   ┃ ┃ ┣ 📜_msvccompiler.py
┃ ┃ ┃   ┃ ┃ ┣ 📜archive_util.py
┃ ┃ ┃   ┃ ┃ ┣ 📜bcppcompiler.py
┃ ┃ ┃   ┃ ┃ ┣ 📜ccompiler.py
┃ ┃ ┃   ┃ ┃ ┣ 📜cmd.py
┃ ┃ ┃   ┃ ┃ ┣ 📜config.py
┃ ┃ ┃   ┃ ┃ ┣ 📜core.py
┃ ┃ ┃   ┃ ┃ ┣ 📜cygwinccompiler.py
┃ ┃ ┃   ┃ ┃ ┣ 📜debug.py
┃ ┃ ┃   ┃ ┃ ┣ 📜dep_util.py
┃ ┃ ┃   ┃ ┃ ┣ 📜dir_util.py
┃ ┃ ┃   ┃ ┃ ┣ 📜dist.py
┃ ┃ ┃   ┃ ┃ ┣ 📜errors.py
┃ ┃ ┃   ┃ ┃ ┣ 📜extension.py
┃ ┃ ┃   ┃ ┃ ┣ 📜fancy_getopt.py
┃ ┃ ┃   ┃ ┃ ┣ 📜file_util.py
┃ ┃ ┃   ┃ ┃ ┣ 📜filelist.py
┃ ┃ ┃   ┃ ┃ ┣ 📜log.py
┃ ┃ ┃   ┃ ┃ ┣ 📜msvc9compiler.py
┃ ┃ ┃   ┃ ┃ ┣ 📜msvccompiler.py
┃ ┃ ┃   ┃ ┃ ┣ 📜py38compat.py
┃ ┃ ┃   ┃ ┃ ┣ 📜py39compat.py
┃ ┃ ┃   ┃ ┃ ┣ 📜spawn.py
┃ ┃ ┃   ┃ ┃ ┣ 📜sysconfig.py
┃ ┃ ┃   ┃ ┃ ┣ 📜text_file.py
┃ ┃ ┃   ┃ ┃ ┣ 📜unixccompiler.py
┃ ┃ ┃   ┃ ┃ ┣ 📜util.py
┃ ┃ ┃   ┃ ┃ ┣ 📜version.py
┃ ┃ ┃   ┃ ┃ ┗ 📜versionpredicate.py
┃ ┃ ┃   ┃ ┣ 📂_vendor
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ordered_set.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜typing_extensions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜zipp.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂importlib_metadata
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_adapters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_collections.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_functools.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_itertools.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_meta.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_text.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_adapters.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_collections.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_functools.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_itertools.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_meta.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜_text.py
┃ ┃ ┃   ┃ ┃ ┣ 📂importlib_resources
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_adapters.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_common.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_itertools.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_legacy.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜abc.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜readers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜simple.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_adapters.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_common.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_compat.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_itertools.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_legacy.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜abc.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜readers.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜simple.py
┃ ┃ ┃   ┃ ┃ ┣ 📂jaraco
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜context.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜functools.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂text
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜context.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜functools.py
┃ ┃ ┃   ┃ ┃ ┣ 📂more_itertools
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜more.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜recipes.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜more.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜recipes.py
┃ ┃ ┃   ┃ ┃ ┣ 📂packaging
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__about__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_manylinux.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_musllinux.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_structures.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜markers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜requirements.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜specifiers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜tags.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜version.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__about__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_manylinux.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_musllinux.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_structures.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜markers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜requirements.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜specifiers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜tags.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜utils.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜version.py
┃ ┃ ┃   ┃ ┃ ┣ 📂pyparsing
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜actions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜common.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜core.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜helpers.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜results.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜testing.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜unicode.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜util.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂diagram
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜actions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜common.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜core.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜helpers.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜results.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜testing.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜unicode.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜util.py
┃ ┃ ┃   ┃ ┃ ┣ 📂tomli
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_parser.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜_re.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜_types.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_parser.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_re.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜_types.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜ordered_set.py
┃ ┃ ┃   ┃ ┃ ┣ 📜typing_extensions.py
┃ ┃ ┃   ┃ ┃ ┗ 📜zipp.py
┃ ┃ ┃   ┃ ┣ 📂command
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜alias.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜bdist_egg.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜bdist_rpm.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build_clib.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build_ext.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build_py.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜build.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜develop.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜dist_info.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜easy_install.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜editable_wheel.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜egg_info.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install_egg_info.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install_lib.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install_scripts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜install.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜py36compat.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜register.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜rotate.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜saveopts.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜sdist.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜setopt.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜test.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜upload_docs.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜upload.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜alias.py
┃ ┃ ┃   ┃ ┃ ┣ 📜bdist_egg.py
┃ ┃ ┃   ┃ ┃ ┣ 📜bdist_rpm.py
┃ ┃ ┃   ┃ ┃ ┣ 📜build_clib.py
┃ ┃ ┃   ┃ ┃ ┣ 📜build_ext.py
┃ ┃ ┃   ┃ ┃ ┣ 📜build_py.py
┃ ┃ ┃   ┃ ┃ ┣ 📜build.py
┃ ┃ ┃   ┃ ┃ ┣ 📜develop.py
┃ ┃ ┃   ┃ ┃ ┣ 📜dist_info.py
┃ ┃ ┃   ┃ ┃ ┣ 📜easy_install.py
┃ ┃ ┃   ┃ ┃ ┣ 📜editable_wheel.py
┃ ┃ ┃   ┃ ┃ ┣ 📜egg_info.py
┃ ┃ ┃   ┃ ┃ ┣ 📜install_egg_info.py
┃ ┃ ┃   ┃ ┃ ┣ 📜install_lib.py
┃ ┃ ┃   ┃ ┃ ┣ 📜install_scripts.py
┃ ┃ ┃   ┃ ┃ ┣ 📜install.py
┃ ┃ ┃   ┃ ┃ ┣ 📜launcher manifest.xml
┃ ┃ ┃   ┃ ┃ ┣ 📜py36compat.py
┃ ┃ ┃   ┃ ┃ ┣ 📜register.py
┃ ┃ ┃   ┃ ┃ ┣ 📜rotate.py
┃ ┃ ┃   ┃ ┃ ┣ 📜saveopts.py
┃ ┃ ┃   ┃ ┃ ┣ 📜sdist.py
┃ ┃ ┃   ┃ ┃ ┣ 📜setopt.py
┃ ┃ ┃   ┃ ┃ ┣ 📜test.py
┃ ┃ ┃   ┃ ┃ ┣ 📜upload_docs.py
┃ ┃ ┃   ┃ ┃ ┗ 📜upload.py
┃ ┃ ┃   ┃ ┣ 📂config
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜_apply_pyprojecttoml.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜expand.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜pyprojecttoml.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜setupcfg.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂_validate_pyproject
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜error_reporting.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜extra_validations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜fastjsonschema_exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜fastjsonschema_validations.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜formats.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜error_reporting.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜extra_validations.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜fastjsonschema_exceptions.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜fastjsonschema_validations.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜formats.py
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜_apply_pyprojecttoml.py
┃ ┃ ┃   ┃ ┃ ┣ 📜expand.py
┃ ┃ ┃   ┃ ┃ ┣ 📜pyprojecttoml.py
┃ ┃ ┃   ┃ ┃ ┗ 📜setupcfg.py
┃ ┃ ┃   ┃ ┣ 📂extern
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜_deprecation_warning.py
┃ ┃ ┃   ┃ ┣ 📜_entry_points.py
┃ ┃ ┃   ┃ ┣ 📜_imp.py
┃ ┃ ┃   ┃ ┣ 📜_importlib.py
┃ ┃ ┃   ┃ ┣ 📜_itertools.py
┃ ┃ ┃   ┃ ┣ 📜_path.py
┃ ┃ ┃   ┃ ┣ 📜_reqs.py
┃ ┃ ┃   ┃ ┣ 📜archive_util.py
┃ ┃ ┃   ┃ ┣ 📜build_meta.py
┃ ┃ ┃   ┃ ┣ 📜cli-32.exe
┃ ┃ ┃   ┃ ┣ 📜cli-64.exe
┃ ┃ ┃   ┃ ┣ 📜cli-arm64.exe
┃ ┃ ┃   ┃ ┣ 📜cli.exe
┃ ┃ ┃   ┃ ┣ 📜dep_util.py
┃ ┃ ┃   ┃ ┣ 📜depends.py
┃ ┃ ┃   ┃ ┣ 📜discovery.py
┃ ┃ ┃   ┃ ┣ 📜dist.py
┃ ┃ ┃   ┃ ┣ 📜errors.py
┃ ┃ ┃   ┃ ┣ 📜extension.py
┃ ┃ ┃   ┃ ┣ 📜glob.py
┃ ┃ ┃   ┃ ┣ 📜gui-32.exe
┃ ┃ ┃   ┃ ┣ 📜gui-64.exe
┃ ┃ ┃   ┃ ┣ 📜gui-arm64.exe
┃ ┃ ┃   ┃ ┣ 📜gui.exe
┃ ┃ ┃   ┃ ┣ 📜installer.py
┃ ┃ ┃   ┃ ┣ 📜launch.py
┃ ┃ ┃   ┃ ┣ 📜logging.py
┃ ┃ ┃   ┃ ┣ 📜monkey.py
┃ ┃ ┃   ┃ ┣ 📜msvc.py
┃ ┃ ┃   ┃ ┣ 📜namespaces.py
┃ ┃ ┃   ┃ ┣ 📜package_index.py
┃ ┃ ┃   ┃ ┣ 📜py34compat.py
┃ ┃ ┃   ┃ ┣ 📜sandbox.py
┃ ┃ ┃   ┃ ┣ 📜script (dev).tmpl
┃ ┃ ┃   ┃ ┣ 📜script.tmpl
┃ ┃ ┃   ┃ ┣ 📜unicode_utils.py
┃ ┃ ┃   ┃ ┣ 📜version.py
┃ ┃ ┃   ┃ ┣ 📜wheel.py
┃ ┃ ┃   ┃ ┗ 📜windows_support.py
┃ ┃ ┃   ┣ 📂setuptools-65.5.0.dist-info
┃ ┃ ┃   ┃ ┣ 📜entry_points.txt
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜LICENSE
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜REQUESTED
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂sqlparse
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__main__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜cli.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜exceptions.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜formatter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜keywords.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜lexer.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜sql.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜tokens.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┗ 📜utils.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂engine
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜filter_stack.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜grouping.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜statement_splitter.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜filter_stack.py
┃ ┃ ┃   ┃ ┃ ┣ 📜grouping.py
┃ ┃ ┃   ┃ ┃ ┗ 📜statement_splitter.py
┃ ┃ ┃   ┃ ┣ 📂filters
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜aligned_indent.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜others.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜output.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜reindent.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜right_margin.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜tokens.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜aligned_indent.py
┃ ┃ ┃   ┃ ┃ ┣ 📜others.py
┃ ┃ ┃   ┃ ┃ ┣ 📜output.py
┃ ┃ ┃   ┃ ┃ ┣ 📜reindent.py
┃ ┃ ┃   ┃ ┃ ┣ 📜right_margin.py
┃ ┃ ┃   ┃ ┃ ┗ 📜tokens.py
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┣ 📜__main__.py
┃ ┃ ┃   ┃ ┣ 📜cli.py
┃ ┃ ┃   ┃ ┣ 📜exceptions.py
┃ ┃ ┃   ┃ ┣ 📜formatter.py
┃ ┃ ┃   ┃ ┣ 📜keywords.py
┃ ┃ ┃   ┃ ┣ 📜lexer.py
┃ ┃ ┃   ┃ ┣ 📜sql.py
┃ ┃ ┃   ┃ ┣ 📜tokens.py
┃ ┃ ┃   ┃ ┗ 📜utils.py
┃ ┃ ┃   ┣ 📂sqlparse-0.5.3.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┣ 📜AUTHORS
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┣ 📜entry_points.txt
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┣ 📂tzdata
┃ ┃ ┃   ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┣ 📂zoneinfo
┃ ┃ ┃   ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┣ 📂Africa
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Abidjan
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Accra
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Addis_Ababa
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Algiers
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Asmara
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Asmera
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bamako
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bangui
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Banjul
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bissau
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Blantyre
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Brazzaville
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bujumbura
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cairo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Casablanca
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ceuta
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Conakry
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dakar
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dar_es_Salaam
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Djibouti
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Douala
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜El_Aaiun
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Freetown
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Gaborone
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Harare
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Johannesburg
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Juba
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kampala
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Khartoum
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kigali
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kinshasa
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lagos
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Libreville
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lome
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Luanda
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lubumbashi
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lusaka
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Malabo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Maputo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Maseru
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mbabane
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mogadishu
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Monrovia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nairobi
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ndjamena
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Niamey
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nouakchott
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ouagadougou
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Porto-Novo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Sao_Tome
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Timbuktu
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tripoli
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tunis
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Windhoek
┃ ┃ ┃   ┃ ┃ ┣ 📂America
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂Argentina
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Buenos_Aires
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Catamarca
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜ComodRivadavia
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Cordoba
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Jujuy
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜La_Rioja
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Mendoza
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Rio_Gallegos
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Salta
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜San_Juan
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜San_Luis
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Tucuman
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜Ushuaia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂Indiana
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Indianapolis
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Knox
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Marengo
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Petersburg
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Tell_City
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Vevay
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Vincennes
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜Winamac
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂Kentucky
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Louisville
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜Monticello
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂North_Dakota
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Beulah
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┣ 📜Center
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜New_Salem
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Adak
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Anchorage
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Anguilla
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Antigua
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Araguaina
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Aruba
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Asuncion
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Atikokan
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Atka
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bahia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bahia_Banderas
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Barbados
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Belem
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Belize
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Blanc-Sablon
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Boa_Vista
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bogota
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Boise
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Buenos_Aires
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cambridge_Bay
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Campo_Grande
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cancun
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Caracas
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Catamarca
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cayenne
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cayman
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chicago
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chihuahua
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ciudad_Juarez
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Coral_Harbour
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cordoba
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Costa_Rica
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Coyhaique
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Creston
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cuiaba
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Curacao
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Danmarkshavn
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dawson
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dawson_Creek
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Denver
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Detroit
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dominica
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Edmonton
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Eirunepe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜El_Salvador
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ensenada
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Fort_Nelson
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Fort_Wayne
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Fortaleza
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Glace_Bay
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Godthab
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Goose_Bay
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Grand_Turk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Grenada
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Guadeloupe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Guatemala
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Guayaquil
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Guyana
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Halifax
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Havana
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Hermosillo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Indianapolis
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Inuvik
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Iqaluit
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Jamaica
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Jujuy
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Juneau
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Knox_IN
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kralendijk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜La_Paz
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lima
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Los_Angeles
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Louisville
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lower_Princes
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Maceio
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Managua
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Manaus
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Marigot
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Martinique
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Matamoros
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mazatlan
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mendoza
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Menominee
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Merida
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Metlakatla
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mexico_City
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Miquelon
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Moncton
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Monterrey
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Montevideo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Montreal
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Montserrat
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nassau
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜New_York
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nipigon
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nome
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Noronha
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nuuk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ojinaga
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Panama
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Pangnirtung
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Paramaribo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Phoenix
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Port_of_Spain
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Port-au-Prince
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Porto_Acre
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Porto_Velho
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Puerto_Rico
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Punta_Arenas
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Rainy_River
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Rankin_Inlet
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Recife
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Regina
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Resolute
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Rio_Branco
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Rosario
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Santa_Isabel
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Santarem
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Santiago
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Santo_Domingo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Sao_Paulo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Scoresbysund
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Shiprock
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Sitka
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜St_Barthelemy
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜St_Johns
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜St_Kitts
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜St_Lucia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜St_Thomas
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜St_Vincent
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Swift_Current
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tegucigalpa
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Thule
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Thunder_Bay
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tijuana
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Toronto
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tortola
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Vancouver
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Virgin
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Whitehorse
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Winnipeg
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Yakutat
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Yellowknife
┃ ┃ ┃   ┃ ┃ ┣ 📂Antarctica
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Casey
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Davis
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜DumontDUrville
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Macquarie
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mawson
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜McMurdo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Palmer
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Rothera
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜South_Pole
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Syowa
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Troll
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Vostok
┃ ┃ ┃   ┃ ┃ ┣ 📂Arctic
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Longyearbyen
┃ ┃ ┃   ┃ ┃ ┣ 📂Asia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Aden
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Almaty
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Amman
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Anadyr
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Aqtau
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Aqtobe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ashgabat
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ashkhabad
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Atyrau
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Baghdad
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bahrain
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Baku
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bangkok
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Barnaul
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Beirut
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bishkek
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Brunei
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Calcutta
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chita
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Choibalsan
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chongqing
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chungking
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Colombo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dacca
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Damascus
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dhaka
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dili
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dubai
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dushanbe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Famagusta
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Gaza
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Harbin
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Hebron
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ho_Chi_Minh
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Hong_Kong
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Hovd
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Irkutsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Istanbul
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Jakarta
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Jayapura
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Jerusalem
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kabul
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kamchatka
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Karachi
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kashgar
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kathmandu
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Katmandu
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Khandyga
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kolkata
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Krasnoyarsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kuala_Lumpur
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kuching
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kuwait
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Macao
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Macau
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Magadan
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Makassar
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Manila
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Muscat
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nicosia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Novokuznetsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Novosibirsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Omsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Oral
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Phnom_Penh
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Pontianak
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Pyongyang
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Qatar
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Qostanay
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Qyzylorda
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Rangoon
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Riyadh
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Saigon
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Sakhalin
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Samarkand
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Seoul
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Shanghai
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Singapore
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Srednekolymsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Taipei
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tashkent
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tbilisi
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tehran
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tel_Aviv
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Thimbu
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Thimphu
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tokyo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tomsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ujung_Pandang
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ulaanbaatar
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ulan_Bator
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Urumqi
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ust-Nera
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Vientiane
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Vladivostok
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Yakutsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Yangon
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Yekaterinburg
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Yerevan
┃ ┃ ┃   ┃ ┃ ┣ 📂Atlantic
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Azores
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bermuda
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Canary
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cape_Verde
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Faeroe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Faroe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Jan_Mayen
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Madeira
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Reykjavik
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜South_Georgia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜St_Helena
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Stanley
┃ ┃ ┃   ┃ ┃ ┣ 📂Australia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜ACT
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Adelaide
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Brisbane
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Broken_Hill
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Canberra
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Currie
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Darwin
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Eucla
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Hobart
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜LHI
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lindeman
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lord_Howe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Melbourne
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜North
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜NSW
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Perth
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Queensland
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜South
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Sydney
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tasmania
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Victoria
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜West
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Yancowinna
┃ ┃ ┃   ┃ ┃ ┣ 📂Brazil
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Acre
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜DeNoronha
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜East
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜West
┃ ┃ ┃   ┃ ┃ ┣ 📂Canada
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Atlantic
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Central
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Eastern
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mountain
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Newfoundland
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Pacific
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Saskatchewan
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Yukon
┃ ┃ ┃   ┃ ┃ ┣ 📂Chile
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Continental
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜EasterIsland
┃ ┃ ┃   ┃ ┃ ┣ 📂Etc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-0
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-1
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-10
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-11
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-12
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-13
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-14
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-2
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-3
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-4
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-5
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-6
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-7
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-8
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT-9
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+0
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+1
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+10
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+11
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+12
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+2
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+3
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+4
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+5
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+6
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+7
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+8
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT+9
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜GMT0
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Greenwich
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜UCT
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Universal
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜UTC
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Zulu
┃ ┃ ┃   ┃ ┃ ┣ 📂Europe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Amsterdam
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Andorra
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Astrakhan
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Athens
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Belfast
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Belgrade
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Berlin
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bratislava
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Brussels
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bucharest
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Budapest
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Busingen
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chisinau
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Copenhagen
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Dublin
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Gibraltar
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Guernsey
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Helsinki
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Isle_of_Man
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Istanbul
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Jersey
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kaliningrad
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kiev
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kirov
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kyiv
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Lisbon
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ljubljana
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜London
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Luxembourg
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Madrid
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Malta
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mariehamn
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Minsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Monaco
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Moscow
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nicosia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Oslo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Paris
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Podgorica
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Prague
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Riga
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Rome
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Samara
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜San_Marino
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Sarajevo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Saratov
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Simferopol
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Skopje
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Sofia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Stockholm
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tallinn
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tirane
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tiraspol
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ulyanovsk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Uzhgorod
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Vaduz
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Vatican
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Vienna
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Vilnius
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Volgograd
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Warsaw
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Zagreb
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Zaporozhye
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Zurich
┃ ┃ ┃   ┃ ┃ ┣ 📂Indian
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Antananarivo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chagos
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Christmas
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Cocos
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Comoro
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kerguelen
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mahe
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Maldives
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mauritius
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mayotte
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Reunion
┃ ┃ ┃   ┃ ┃ ┣ 📂Mexico
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜BajaNorte
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜BajaSur
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜General
┃ ┃ ┃   ┃ ┃ ┣ 📂Pacific
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Apia
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Auckland
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Bougainville
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chatham
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Chuuk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Easter
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Efate
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Enderbury
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Fakaofo
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Fiji
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Funafuti
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Galapagos
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Gambier
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Guadalcanal
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Guam
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Honolulu
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Johnston
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kanton
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kiritimati
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kosrae
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Kwajalein
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Majuro
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Marquesas
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Midway
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Nauru
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Niue
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Norfolk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Noumea
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Pago_Pago
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Palau
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Pitcairn
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Pohnpei
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Ponape
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Port_Moresby
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Rarotonga
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Saipan
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Samoa
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tahiti
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tarawa
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Tongatapu
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Truk
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Wake
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Wallis
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Yap
┃ ┃ ┃   ┃ ┃ ┣ 📂US
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📂__pycache__
┃ ┃ ┃   ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-311.pyc
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Alaska
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Aleutian
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Arizona
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Central
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜East-Indiana
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Eastern
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Hawaii
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Indiana-Starke
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Michigan
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Mountain
┃ ┃ ┃   ┃ ┃ ┃ ┣ 📜Pacific
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜Samoa
┃ ┃ ┃   ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┃ ┣ 📜CET
┃ ┃ ┃   ┃ ┃ ┣ 📜CST6CDT
┃ ┃ ┃   ┃ ┃ ┣ 📜Cuba
┃ ┃ ┃   ┃ ┃ ┣ 📜EET
┃ ┃ ┃   ┃ ┃ ┣ 📜Egypt
┃ ┃ ┃   ┃ ┃ ┣ 📜Eire
┃ ┃ ┃   ┃ ┃ ┣ 📜EST
┃ ┃ ┃   ┃ ┃ ┣ 📜EST5EDT
┃ ┃ ┃   ┃ ┃ ┣ 📜Factory
┃ ┃ ┃   ┃ ┃ ┣ 📜GB
┃ ┃ ┃   ┃ ┃ ┣ 📜GB-Eire
┃ ┃ ┃   ┃ ┃ ┣ 📜GMT
┃ ┃ ┃   ┃ ┃ ┣ 📜GMT-0
┃ ┃ ┃   ┃ ┃ ┣ 📜GMT+0
┃ ┃ ┃   ┃ ┃ ┣ 📜GMT0
┃ ┃ ┃   ┃ ┃ ┣ 📜Greenwich
┃ ┃ ┃   ┃ ┃ ┣ 📜Hongkong
┃ ┃ ┃   ┃ ┃ ┣ 📜HST
┃ ┃ ┃   ┃ ┃ ┣ 📜Iceland
┃ ┃ ┃   ┃ ┃ ┣ 📜Iran
┃ ┃ ┃   ┃ ┃ ┣ 📜iso3166.tab
┃ ┃ ┃   ┃ ┃ ┣ 📜Israel
┃ ┃ ┃   ┃ ┃ ┣ 📜Jamaica
┃ ┃ ┃   ┃ ┃ ┣ 📜Japan
┃ ┃ ┃   ┃ ┃ ┣ 📜Kwajalein
┃ ┃ ┃   ┃ ┃ ┣ 📜leapseconds
┃ ┃ ┃   ┃ ┃ ┣ 📜Libya
┃ ┃ ┃   ┃ ┃ ┣ 📜MET
┃ ┃ ┃   ┃ ┃ ┣ 📜MST
┃ ┃ ┃   ┃ ┃ ┣ 📜MST7MDT
┃ ┃ ┃   ┃ ┃ ┣ 📜Navajo
┃ ┃ ┃   ┃ ┃ ┣ 📜NZ
┃ ┃ ┃   ┃ ┃ ┣ 📜NZ-CHAT
┃ ┃ ┃   ┃ ┃ ┣ 📜Poland
┃ ┃ ┃   ┃ ┃ ┣ 📜Portugal
┃ ┃ ┃   ┃ ┃ ┣ 📜PRC
┃ ┃ ┃   ┃ ┃ ┣ 📜PST8PDT
┃ ┃ ┃   ┃ ┃ ┣ 📜ROC
┃ ┃ ┃   ┃ ┃ ┣ 📜ROK
┃ ┃ ┃   ┃ ┃ ┣ 📜Singapore
┃ ┃ ┃   ┃ ┃ ┣ 📜Turkey
┃ ┃ ┃   ┃ ┃ ┣ 📜tzdata.zi
┃ ┃ ┃   ┃ ┃ ┣ 📜UCT
┃ ┃ ┃   ┃ ┃ ┣ 📜Universal
┃ ┃ ┃   ┃ ┃ ┣ 📜UTC
┃ ┃ ┃   ┃ ┃ ┣ 📜W-SU
┃ ┃ ┃   ┃ ┃ ┣ 📜WET
┃ ┃ ┃   ┃ ┃ ┣ 📜zone.tab
┃ ┃ ┃   ┃ ┃ ┣ 📜zone1970.tab
┃ ┃ ┃   ┃ ┃ ┣ 📜zonenow.tab
┃ ┃ ┃   ┃ ┃ ┗ 📜Zulu
┃ ┃ ┃   ┃ ┣ 📜__init__.py
┃ ┃ ┃   ┃ ┗ 📜zones
┃ ┃ ┃   ┣ 📂tzdata-2025.2.dist-info
┃ ┃ ┃   ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┣ 📂licenses
┃ ┃ ┃   ┃ ┃ ┃ ┗ 📜LICENSE_APACHE
┃ ┃ ┃   ┃ ┃ ┗ 📜LICENSE
┃ ┃ ┃   ┃ ┣ 📜INSTALLER
┃ ┃ ┃   ┃ ┣ 📜METADATA
┃ ┃ ┃   ┃ ┣ 📜RECORD
┃ ┃ ┃   ┃ ┣ 📜top_level.txt
┃ ┃ ┃   ┃ ┗ 📜WHEEL
┃ ┃ ┃   ┗ 📜distutils-precedence.pth
┃ ┃ ┣ 📂Scripts
┃ ┃ ┃ ┣ 📜activate
┃ ┃ ┃ ┣ 📜activate.bat
┃ ┃ ┃ ┣ 📜Activate.ps1
┃ ┃ ┃ ┣ 📜deactivate.bat
┃ ┃ ┃ ┣ 📜django-admin.exe
┃ ┃ ┃ ┣ 📜pip.exe
┃ ┃ ┃ ┣ 📜pip3.11.exe
┃ ┃ ┃ ┣ 📜pip3.exe
┃ ┃ ┃ ┣ 📜python.exe
┃ ┃ ┃ ┣ 📜pythonw.exe
┃ ┃ ┃ ┣ 📜qr.exe
┃ ┃ ┃ ┗ 📜sqlformat.exe
┃ ┃ ┗ 📜pyvenv.cfg
┃ ┣ 📜db.sqlite3
┃ ┗ 📜manage.py
┣ 📂frontend
┃ ┣ 📂public
┃ ┃ ┗ 📜vite.svg
┃ ┣ 📂src
┃ ┃ ┣ 📂assets
┃ ┃ ┃ ┗ 📜react.svg
┃ ┃ ┣ 📂components
┃ ┃ ┃ ┗ 📜SeatMap.jsx
┃ ┃ ┣ 📂pages
┃ ┃ ┃ ┣ 📜EventDetail.jsx
┃ ┃ ┃ ┣ 📜Home.jsx
┃ ┃ ┃ ┗ 📜TicketView.jsx
┃ ┃ ┣ 📂services
┃ ┃ ┃ ┗ 📜api.js
┃ ┃ ┣ 📜App.css
┃ ┃ ┣ 📜App.jsx
┃ ┃ ┣ 📜index.css
┃ ┃ ┗ 📜main.jsx
┃ ┣ 📜.env
┃ ┣ 📜.gitignore
┃ ┣ 📜eslint.config.js
┃ ┣ 📜index.html
┃ ┣ 📜package.json
┃ ┣ 📜README.md
┃ ┗ 📜vite.config.js
┗ 📜manage.py



⚙️ Installation
Follow these steps to run the project locally:

1. Clone the repository
git clone [https://github.com/your-username/TicketFlow.git](https://github.com/your-username/TicketFlow.git)
cd TicketFlow

2. Create a virtual environment
python -m venv venv

3. Activate the environment
Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Run migrations
python manage.py migrate

6. Create a superuser (admin)
python manage.py createsuperuser

7. Run the development server
python manage.py runserver

🚀 Usage
Open your browser and go to http://127.0.0.1:8000/.

Log in using your admin credentials at /admin.

Create events, venues, and tickets in the admin panel.

Users can register, browse events, and book tickets.

📦 Deployment
For production deployment, use:

Gunicorn / uWSGI as WSGI server

Nginx or Apache HTTP Server as reverse proxy

PostgreSQL as database

Docker (optional) for containerization

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

