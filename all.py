from flask import Flask, render_template, request, redirect, url_for, session, flash, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import secrets
from config import DATABASE_CONFIG
from secret import SECRET_KEY
import mysql.connector
import datetime
import pandas as pd
import csv
from recommend.doctor import RecommendationModel
import sys