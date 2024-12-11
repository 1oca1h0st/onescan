#!/bin/sh
pybabel extract -F i18n/babel.cfg -o i18n/messages.pot .

pybabel init -i i18n/messages.pot -d i18n/lang -l en_US
pybabel init -i i18n/messages.pot -d i18n/lang -l zh_CN

pybabel compile -d i18n/langs -l en_US
pybabel compile -d i18n/langs -l zh_CN