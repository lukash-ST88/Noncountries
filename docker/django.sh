#!/bin/bash


gunicorn deployapp.wsgi:application
