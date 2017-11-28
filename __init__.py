import sys
import dbus
import math
import subprocess
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)

class KateControlSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(KateControlSkill, self).__init__(name="KateControlSkill")
        
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))
        
        katecontrol_filenew_intent = IntentBuilder("KateFileNewKeywordIntent").\
            require("InternalKateFileNewKeyword").build()
        self.register_intent(katecontrol_filenew_intent, self.handle_katecontrol_filenew_intent)
        
        katecontrol_fileclose_intent = IntentBuilder("KateFileCloseKeywordIntent").\
            require("InternalKateFileCloseKeyword").build()
        self.register_intent(katecontrol_fileclose_intent, self.handle_katecontrol_fileclose_intent)
        
        katecontrol_filesaveall_intent = IntentBuilder("KateFileSaveAllKeywordIntent").\
            require("InternalKateFileSaveAllKeyword").build()
        self.register_intent(katecontrol_filesaveall_intent, self.handle_katecontrol_filesaveall_intent)

        katecontrol_nexttab_intent = IntentBuilder("KateNextTabKeywordIntent").\
            require("InternalKateNextTabKeyword").build()
        self.register_intent(katecontrol_nexttab_intent, self.handle_katecontrol_nexttab_intent)
        
        katecontrol_prevtab_intent = IntentBuilder("KatePrevTabKeywordIntent").\
            require("InternalKatePrevTabKeyword").build()
        self.register_intent(katecontrol_prevtab_intent, self.handle_katecontrol_prevtab_intent)

        katecontrol_splitviewvert_intent = IntentBuilder("KateSplitViewVertKeywordIntent").\
            require("InternalKateSplitViewVertKeyword").build()
        self.register_intent(katecontrol_splitviewvert_intent, self.handle_katecontrol_splitviewvert_intent)

        katecontrol_splitviewhorz_intent = IntentBuilder("KateSplitViewHorzKeywordIntent").\
            require("InternalKateSplitViewHorzKeyword").build()
        self.register_intent(katecontrol_splitviewhorz_intent, self.handle_katecontrol_splitviewhorz_intent)
        
        katecontrol_splitviewgonext_intent = IntentBuilder("KateSplitViewGoNextKeywordIntent").\
            require("InternalKateSplitViewGoNextKeyword").build()
        self.register_intent(katecontrol_splitviewgonext_intent, self.handle_katecontrol_splitviewgonext_intent)
        
        katecontrol_splitviewgoprev_intent = IntentBuilder("KateSplitViewGoPrevKeywordIntent").\
            require("InternalKateSplitViewGoPrevKeyword").build()
        self.register_intent(katecontrol_splitviewgoprev_intent, self.handle_katecontrol_splitviewgoprev_intent)

        katecontrol_optionsconfig_intent = IntentBuilder("KateOptionsConfigIntent").\
            require("InternalKateOptionsConfigKeyword").build()
        self.register_intent(katecontrol_optionsconfig_intent, self.handle_katecontrol_optionsconfig_intent)


    def handle_katecontrol_filenew_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/file_new")
        kateObj.trigger()
                 
    def handle_katecontrol_fileclose_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/file_close")
        kateObj.trigger()


    def handle_katecontrol_filesaveall_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/file_save_all")
        kateObj.trigger()


    def handle_katecontrol_nexttab_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/view_next_tab")
        kateObj.trigger()

    def handle_katecontrol_prevtab_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/view_previous_tab")
        kateObj.trigger()
        
    def handle_katecontrol_splitviewvert_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/view_split_vert")
        kateObj.trigger()

    def handle_katecontrol_splitviewhorz_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/view_split_horiz")
        kateObj.trigger()

    def handle_katecontrol_splitviewgonext_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/go_next_split_view")
        kateObj.trigger()
        
    def handle_katecontrol_splitviewgoprev_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/go_prev_split_view")
        kateObj.trigger()
        
    def handle_katecontrol_optionsconfig_intent(self, message):
        session_bus = dbus.SessionBus()
        kate_bus = ""
        for method in session_bus.list_names():
            if method.find("kate") != -1:
                print method
                kate_bus = method
                break

        kateObj = session_bus.get_object(kate_bus, "/kate/MainWindow_1/actions/options_configure")
        kateObj.trigger()

    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return KateControlSkill()
