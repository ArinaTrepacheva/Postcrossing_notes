import io
import sqlite3
import sys
from datetime import date
from random import randrange

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

template_reg = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1096</width>
    <height>844</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>MS Shell Dlg 2</family>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>170</y>
      <width>411</width>
      <height>461</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:rgb(228, 255, 255);
border-radius:35px;</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLineEdit" name="nameEdit">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>110</y>
       <width>301</width>
       <height>51</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: white;
border-radius: 20px;
color:rgb(199, 199, 199);
font-size: 20px;
</string>
     </property>
     <property name="text">
      <string>Имя...</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="passwordEdit">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>190</y>
       <width>301</width>
       <height>51</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: white;
border-radius: 20px;
color:rgb(199, 199, 199);
font-size: 20px;
</string>
     </property>
     <property name="text">
      <string>Пароль...</string>
     </property>
    </widget>
    <widget class="QPushButton" name="login_button">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>280</y>
       <width>251</width>
       <height>51</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgb(157, 157, 157);
color:white;
font-size:18px;
border-radius:13px;</string>
     </property>
     <property name="text">
      <string>Войти</string>
     </property>
    </widget>
    <widget class="QPushButton" name="signup_button">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>350</y>
       <width>251</width>
       <height>51</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgb(157, 157, 157);
color:white;
font-size:18px;
border-radius:13px;</string>
     </property>
     <property name="text">
      <string>Регистрация</string>
     </property>
    </widget>
    <widget class="QLabel" name="operationlb">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>0</y>
       <width>311</width>
       <height>101</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Cascadia Code SemiBold</family>
       <pointsize>22</pointsize>
       <weight>7</weight>
       <italic>false</italic>
       <bold>false</bold>
      </font>
     </property>
     <property name="toolTip">
      <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;вв&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
     </property>
     <property name="styleSheet">
      <string notr="true">font: 63 22pt &quot;Cascadia Code SemiBold&quot;;
</string>
     </property>
     <property name="text">
      <string>Вход</string>
     </property>
    </widget>
    <widget class="QLabel" name="errorlabel">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>420</y>
       <width>331</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Yu Gothic UI Semibold</family>
       <pointsize>12</pointsize>
       <weight>7</weight>
       <italic>false</italic>
       <bold>false</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:red;
font: 63 12pt &quot;Yu Gothic UI Semibold&quot;;</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>-30</x>
      <y>-110</y>
      <width>1341</width>
      <height>1001</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>регистрация.jpg</pixmap>
    </property>
   </widget>
   <zorder>label</zorder>
   <zorder>frame</zorder>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1096</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
template_main = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1057</width>
    <height>827</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="hellolabel">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>10</y>
      <width>311</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Monotype Corsiva</family>
      <pointsize>20</pointsize>
      <weight>50</weight>
      <italic>true</italic>
      <bold>false</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">
font: italic 20pt &quot;Monotype Corsiva&quot;;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="sendbutton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>320</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:rgb(194, 255, 250);
color:rgb(52, 52, 52);
font: 11pt &quot;Yu Gothic UI Semilight&quot;;
border-radius: 13px;

</string>
    </property>
    <property name="text">
     <string>Отправленные</string>
    </property>
   </widget>
   <widget class="QPushButton" name="getbutton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>480</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:rgb(194, 255, 250);
color:rgb(52, 52, 52);
font: 11pt &quot;Yu Gothic UI Semilight&quot;;
border-radius: 13px;

</string>
    </property>
    <property name="text">
     <string>Полученные</string>
    </property>
   </widget>
   <widget class="QPushButton" name="calendar">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>560</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:rgb(194, 255, 250);
color:rgb(52, 52, 52);
font: 11pt &quot;Yu Gothic UI Semilight&quot;;
border-radius: 13px;

</string>
    </property>
    <property name="text">
     <string>календарь </string>
    </property>
   </widget>
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>261</width>
      <height>831</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(43, 0, 130)</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QPushButton" name="add_button">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>640</y>
       <width>201</width>
       <height>51</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgb(194, 255, 250);
color:rgb(52, 52, 52);
font: 11pt &quot;Yu Gothic UI Semilight&quot;;
border-radius: 13px;

</string>
     </property>
     <property name="text">
      <string>Добавить</string>
     </property>
    </widget>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>-10</y>
       <width>241</width>
       <height>161</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">font: 63 18pt &quot;Yu Gothic UI Semibold&quot;;
color: white</string>
     </property>
     <property name="text">
      <string>Всего открыток:</string>
     </property>
    </widget>
    <widget class="QLabel" name="countlabel">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>90</y>
       <width>221</width>
       <height>101</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">font: 80 40pt &quot;Yu Gothic UI Semibold&quot;;
color: rgb(255, 0, 0)</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="delete_button">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>720</y>
       <width>201</width>
       <height>51</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgb(194, 255, 250);
color:rgb(52, 52, 52);
font: 11pt &quot;Yu Gothic UI Semilight&quot;;
border-radius: 13px;

</string>
     </property>
     <property name="text">
      <string>Удалить</string>
     </property>
    </widget>
   </widget>
   <widget class="QLineEdit" name="searchEdit">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>70</y>
      <width>561</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-radius:13px;
color:rgb(115, 115, 115);
font-size:14px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="search">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>80</y>
      <width>71</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Поиск</string>
    </property>
   </widget>
   <widget class="QPushButton" name="allbutton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>400</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:rgb(194, 255, 250);
color:rgb(52, 52, 52);
font: 11pt &quot;Yu Gothic UI Semilight&quot;;
border-radius: 13px;

</string>
    </property>
    <property name="text">
     <string>Все</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>140</y>
      <width>581</width>
      <height>621</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(232, 229, 255);
border-radius: 20px;
color: rgb(0, 0, 127);</string>
    </property>
   </widget>
   <widget class="QCalendarWidget" name="calendarWidget">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>140</y>
      <width>401</width>
      <height>281</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(232, 229, 255);
border-radius: 20px;
color: rgb(0, 0, 127);</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="depend_table">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>490</y>
      <width>511</width>
      <height>271</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(232, 229, 255);
border-radius: 20px;
color: rgb(0, 0, 127);</string>
    </property>
   </widget>
   <widget class="QPushButton" name="find_button">
    <property name="geometry">
     <rect>
      <x>510</x>
      <y>430</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:rgb(81, 99, 177);
color:white;
font: 11pt &quot;Yu Gothic UI Semilight&quot;;
border-radius: 13px;
</string>
    </property>
    <property name="text">
     <string>Найти</string>
    </property>
   </widget>
   <zorder>frame</zorder>
   <zorder>hellolabel</zorder>
   <zorder>sendbutton</zorder>
   <zorder>getbutton</zorder>
   <zorder>calendar</zorder>
   <zorder>searchEdit</zorder>
   <zorder>search</zorder>
   <zorder>allbutton</zorder>
   <zorder>tableWidget</zorder>
   <zorder>calendarWidget</zorder>
   <zorder>depend_table</zorder>
   <zorder>find_button</zorder>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1057</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
template_add = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>640</width>
    <height>480</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>10</y>
      <width>331</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 63 18pt &quot;Yu Gothic UI Semibold&quot;;</string>
    </property>
    <property name="text">
     <string>Добавление открытки</string>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>90</y>
      <width>111</width>
      <height>271</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label_2">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>Название</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>Страна</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_4">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>Статус</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_5">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>От/кому</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_6">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>Дата</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>90</y>
      <width>251</width>
      <height>271</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QLineEdit" name="title">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="country">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QComboBox" name="status">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="name_users">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QDateEdit" name="dateEdit">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="add_btn">
    <property name="geometry">
     <rect>
      <x>442</x>
      <y>307</y>
      <width>141</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(0, 0, 127);
color: white;
font-size: 14px;
border-radius: 20px;</string>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QLabel" name="error_lb">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>400</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 63 9pt &quot;Yu Gothic UI Semibold&quot;;
color:red;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>640</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
template_delete = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>640</width>
    <height>480</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>10</y>
      <width>331</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 63 18pt &quot;Yu Gothic UI Semibold&quot;;</string>
    </property>
    <property name="text">
     <string>Удаление открытки</string>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>90</y>
      <width>111</width>
      <height>271</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label_2">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>Название</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>Страна</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_4">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>Статус</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_5">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>От/кому</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_6">
       <property name="styleSheet">
        <string notr="true">font: 14pt &quot;Yu Gothic UI Semilight&quot;;</string>
       </property>
       <property name="text">
        <string>Дата</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>90</y>
      <width>251</width>
      <height>271</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QLineEdit" name="title">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="country">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QComboBox" name="status">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="name_users">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QDateEdit" name="dateEdit">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="delete_btn">
    <property name="geometry">
     <rect>
      <x>442</x>
      <y>307</y>
      <width>141</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(0, 0, 127);
color: white;
font-size: 14px;
border-radius: 20px;</string>
    </property>
    <property name="text">
     <string>Удалить</string>
    </property>
   </widget>
   <widget class="QLabel" name="error_lb">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>400</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 63 9pt &quot;Yu Gothic UI Semibold&quot;;
color:red;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>640</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Regestration(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = io.StringIO(template_reg)
        uic.loadUi(ui_file, self)
        self.setWindowTitle('Вход')
        self.setFixedSize(1096, 844)
        self.con = sqlite3.connect('postcrossing.sqlite')
        cur = self.con.cursor()
        self.data = cur.execute('select * from Users').fetchall()
        self.login_button.clicked.connect(self.log_func)
        self.signup_button.clicked.connect(self.signup_func)

    def log_func(self):
        self.errorlabel.setText('')
        name = self.nameEdit.text()
        password = self.passwordEdit.text()
        cur = self.con.cursor()
        inf = cur.execute(f'select * from Users where name = ? and password = ?', (name, password)).fetchall()
        if not name or not password or not name or name == 'Имя...' or password == 'Пароль...' or not inf:
            self.errorlabel.setText('Некорректные данные')
        else:
            self.close()
            self.window = MainScreen(self, inf[0][0])
            self.window.show()

    def signup_func(self):
        self.errorlabel.setText('')
        name = self.nameEdit.text()
        password = self.passwordEdit.text()
        cur = self.con.cursor()
        inf = cur.execute(f'select * from Users where name = ? and password = ?', (name, password)).fetchall()
        if not name or not password or not name or name == 'Имя...' or password == 'Пароль...' or inf:
            self.errorlabel.setText('Некорректные данные')
        else:
            idd = cur.execute("SELECT max(id) FROM Users").fetchone()[0] + 1
            cur.execute("INSERT INTO  Users VALUES (?,?,?)", (int(idd), name, password))
            self.con.commit()
            self.close()
            self.window = MainScreen(self, idd)
            self.window.show()


class AddScreen(QMainWindow):
    def __init__(self, parent, ide):
        super().__init__(parent)
        self.ide = ide
        ui_file = io.StringIO(template_add)
        uic.loadUi(ui_file, self)
        self.setFixedSize(640, 480)
        now_d = date.today()
        self.dateEdit.setDate(now_d)
        self.setWindowTitle('Добавление открытки')
        self.status.addItems(['Отправлена', 'Получена'])
        self.add_btn.clicked.connect(self.add_func)

    def add_func(self):
        self.error_lb.setText('')
        title = self.title.text()
        country = self.country.text()
        status = '1' if self.status.currentText() == 'Отправлена' else '0'
        user = self.name_users.text()
        data = (str(self.dateEdit.date().toString('dd-MM-yyyy'))).replace('-', '.')
        if not title or not country or not user:
            self.error_lb.setText('Некорректные данные')
        else:
            self.con = sqlite3.connect('postcrossing.sqlite')
            cur = self.con.cursor()
            result = cur.execute("SELECT max(id) FROM Posts").fetchone()[0] + 1
            new_data = (result, title, self.ide, country, status, user, data)
            cur.execute("INSERT INTO Posts VALUES (?,?,?,?,?,?,?)", new_data)
            self.con.commit()
            self.parent().update_result()
            self.close()


class DeleteScreen(QMainWindow):
    def __init__(self, parent, ide):
        super().__init__(parent)
        self.ide = ide
        ui_file = io.StringIO(template_delete)
        uic.loadUi(ui_file, self)
        self.setFixedSize(640, 480)
        now_d = date.today()
        self.dateEdit.setDate(now_d)
        self.setWindowTitle('Удаление открытки')
        self.status.addItems(['Отправлена', 'Получена'])
        self.delete_btn.clicked.connect(self.delete_func)

    def delete_func(self):
        self.error_lb.setText('')
        title = self.title.text()
        country = self.country.text()
        status = '1' if self.status.currentText() == 'Отправлена' else '0'
        data = (str(self.dateEdit.date().toString('dd-MM-yyyy'))).replace('-', '.')
        if not title or not country:
            self.error_lb.setText('Некорректные данные')
        else:
            self.con = sqlite3.connect('postcrossing.sqlite')
            cur = self.con.cursor()
            new_data = (title, self.ide, country, status, data)
            cur.execute("DELETE from Posts where name=? and id_users = ? and country = ? and status = ? and data = ?",
                        new_data)
            self.con.commit()
            self.parent().update_result()
            self.close()


class MainScreen(QMainWindow):
    def __init__(self, parent, ide):
        super().__init__(parent)
        self.ide = ide
        self.status = 2
        self.setFixedSize(1057, 827)
        ui_file = io.StringIO(template_main)
        uic.loadUi(ui_file, self)
        self.setWindowTitle('Главная')
        self.calendarWidget.hide()
        self.depend_table.hide()
        self.find_button.hide()
        self.tableWidget.show()
        self.con = sqlite3.connect('postcrossing.sqlite')
        cur = self.con.cursor()
        name_user = cur.execute('select name from Users where id = ?', (self.ide,)).fetchone()[0]
        lang_list = ['Привет', 'Hello', 'Përshëndetje.', 'Հի', 'Прывітанне', '안녕', 'Selam', 'হাই', 'Hej', 'こんにちは',
                     'ሰላም']
        self.hellolabel.setText(f'{lang_list[randrange(0, 11)]}! {name_user}')

        self.posts = cur.execute('select * from Posts where id_users = ?', (ide,)).fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Страна', 'Статус', 'Дата'])
        self.tableWidget.setRowCount(0)
        for i in range(len(self.posts)):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.posts[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.posts[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.posts[i][3])))
            if self.posts[i][4] == '1':
                self.tableWidget.setItem(i, 3, QTableWidgetItem("отправлена"))
            else:
                self.tableWidget.setItem(i, 3, QTableWidgetItem("получена"))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.posts[i][6])))
        self.searchEdit.textChanged.connect(self.search_func)
        self.sendbutton.clicked.connect(self.send_func)
        self.allbutton.clicked.connect(self.update_result)
        self.getbutton.clicked.connect(self.get_func)
        self.countlabel.setText(str(len(self.posts)))
        self.add_button.clicked.connect(self.add_func)
        self.delete_button.clicked.connect(self.delete_func)
        self.calendar.clicked.connect(self.calendar_func)

    def calendar_func(self):
        self.calendarWidget.show()
        self.depend_table.show()
        self.status = 2
        self.find_button.show()
        self.tableWidget.hide()
        self.find_button.clicked.connect(self.find_func)

    def find_func(self):
        data = self.calendarWidget.selectedDate().toString('dd-MM-yyyy').replace('-', '.')
        cur = self.con.cursor()
        self.posts = cur.execute('select * from Posts where id_users = ? and data = ?', (self.ide, data)).fetchall()
        self.depend_table.setColumnCount(5)
        self.depend_table.setHorizontalHeaderLabels(['ID', 'Название', 'Страна', 'Статус', 'Дата'])
        self.depend_table.setRowCount(0)
        for i in range(len(self.posts)):
            self.depend_table.setRowCount(
                self.depend_table.rowCount() + 1)
            self.depend_table.setItem(i, 0, QTableWidgetItem(str(self.posts[i][0])))
            self.depend_table.setItem(i, 1, QTableWidgetItem(str(self.posts[i][1])))
            self.depend_table.setItem(i, 2, QTableWidgetItem(str(self.posts[i][3])))
            if self.posts[i][4] == '1':
                self.depend_table.setItem(i, 3, QTableWidgetItem("отправлена"))
            else:
                self.depend_table.setItem(i, 3, QTableWidgetItem("получена"))
            self.depend_table.setItem(i, 4, QTableWidgetItem(str(self.posts[i][6])))

    def delete_func(self):
        self.calendarWidget.hide()
        self.depend_table.hide()
        self.find_button.hide()
        self.tableWidget.show()
        self.delete_form = DeleteScreen(self, self.ide)
        self.delete_form.show()

    def add_func(self):
        self.calendarWidget.hide()
        self.depend_table.hide()
        self.find_button.hide()
        self.tableWidget.show()
        self.add_form = AddScreen(self, self.ide)
        self.add_form.show()

    def update_result(self):
        self.calendarWidget.hide()
        self.depend_table.hide()
        self.find_button.hide()
        self.tableWidget.show()
        self.status = 2
        cur = self.con.cursor()
        self.posts = cur.execute('select * from Posts where id_users = ?', (self.ide,)).fetchall()
        self.countlabel.setText(str(len(self.posts)))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Страна', 'Статус', 'Дата'])
        self.tableWidget.setRowCount(0)
        for i in range(len(self.posts)):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.posts[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.posts[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.posts[i][3])))
            if self.posts[i][4] == '1':
                self.tableWidget.setItem(i, 3, QTableWidgetItem("отправлена"))
            else:
                self.tableWidget.setItem(i, 3, QTableWidgetItem("получена"))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.posts[i][6])))

    def send_func(self):
        self.calendarWidget.hide()
        self.depend_table.hide()
        self.find_button.hide()
        self.tableWidget.show()
        self.status = 1
        cur = self.con.cursor()
        self.posts = cur.execute('select * from Posts where id_users = ? and status = 1', (self.ide,)).fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Страна', 'Статус', 'Дата'])
        self.tableWidget.setRowCount(0)
        for i in range(len(self.posts)):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.posts[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.posts[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.posts[i][3])))
            if self.posts[i][4] == '1':
                self.tableWidget.setItem(i, 3, QTableWidgetItem("отправлена"))
            else:
                self.tableWidget.setItem(i, 3, QTableWidgetItem("получена"))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.posts[i][6])))

    def get_func(self):
        self.calendarWidget.hide()
        self.depend_table.hide()
        self.find_button.hide()
        self.tableWidget.show()
        self.status = 0
        cur = self.con.cursor()
        self.posts = cur.execute('select * from Posts where id_users = ? and status = 0', (self.ide,)).fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Страна', 'Статус', 'Дата'])
        self.tableWidget.setRowCount(0)
        for i in range(len(self.posts)):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.posts[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.posts[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.posts[i][3])))
            if self.posts[i][4] == '1':
                self.tableWidget.setItem(i, 3, QTableWidgetItem("отправлена"))
            else:
                self.tableWidget.setItem(i, 3, QTableWidgetItem("получена"))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.posts[i][6])))

    def search_func(self):
        self.calendarWidget.hide()
        self.depend_table.hide()
        self.find_button.hide()
        self.tableWidget.show()
        text = self.searchEdit.text()
        cur = self.con.cursor()
        if self.status == 2:
            data = cur.execute(f"select * from posts where name like '{text}%' and id_users = {self.ide}").fetchall()
        else:
            data = cur.execute(
                f"select * from posts where name like '{text}%' and id_users = {self.ide} and status = {str(self.status)}").fetchall()
        if data:
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Страна', 'Статус', 'Дата'])
            self.tableWidget.setRowCount(0)
            for i in range(len(data)):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(data[i][0])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(data[i][1])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(data[i][3])))
                if data[i][4] == '1':
                    self.tableWidget.setItem(i, 3, QTableWidgetItem("отправлена"))
                else:
                    self.tableWidget.setItem(i, 3, QTableWidgetItem("получена"))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(data[i][6])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Regestration()
    ex.show()
    sys.exit(app.exec())
