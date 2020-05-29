### Module for interfacing HDHomerun tunners from http API
### https://info.hdhomerun.com/info/http_api

import requests
import json

def HdHrDevices(ip_address=''):
    devices = []

    if ip_address == '':
        response = requests.get('http://api.hdhomerun.com/discover')
        if response:
            discovered_devices = response.json()
            for discovered_device in discovered_devices:
                devices.extend(HdHrDevices(discovered_device['LocalIP']))
    
    else:
        response = requests.get('http://' + ip_address + '/discover.json')
        if response:
            devices.append(HdHrDevice(ip_address, response.json()))

    return devices

class HdHrTuner:
    
    def __init__(self, status_response):
        try:
            self._vctNumber = status_response['VctNumber']
        except KeyError:
            self._vctNumber = 'None'
        try:
            self._vctName = status_response['VctName']
        except KeyError:
            self._vctName = 'None'
        try:
            freq = status_response['Frequency']
            self._frecuency = freq / 1000000
        except KeyError:
            self._frecuency = 0
        try:
            self._signalStrength = status_response['SignalStrengthPercent']
        except KeyError:
            self._signalStrength = 0
        try:
            self._signalQuality = status_response['SignalQualityPercent']
        except KeyError:
            self._signalQuality = 0
        try:
            self._symbolQuality = status_response['SymbolQualityPercent']
        except KeyError:
            self._symbolQuality = ''

    @property
    def vctNumber(self):
        return self._vctNumber

    @property
    def vctName(self):
        return self._vctName

    @property
    def frecuency(self):
        return self._frecuency

    @property
    def signalStrength(self):
        return self._signalStrength

    @property
    def signalQuality(self):
        return self._signalQuality

    @property
    def symbolQuality(self):
        return self._symbolQuality

    
class HdHrDevice:

    def __init__(self, ip_address, discover_response):
        self._friendlyName = discover_response['FriendlyName']
        self._modelNumber = discover_response['ModelNumber']
        self._firmwareName = discover_response['FirmwareName']
        self._firmwareVersion = discover_response['FirmwareVersion']
        try:
            self._upgradeVersion = discover_response['UpgradeAvailable']
            self._upgradeAvailable = True
        except KeyError:
            self._upgradeVersion = self._firmwareVersion
            self._upgradeAvailable = False
        self._deviceID = discover_response['DeviceID']
        self._tunerCount = discover_response['TunerCount']
        self._tuner = []
        response = requests.get('http://' + ip_address + '/status.json')
        if response:
            tuners = response.json()
            for tuner in tuners:
                self._tuner.append(HdHrTuner(tuner))

    @property
    def name(self):
        return "HDHomeRun Tuner " + self._deviceID

    @property
    def friendlyName(self):
        return self._friendlyName

    @property
    def modelNumber(self):
        return self._modelNumber

    @property
    def firmwareName(self):
        return self._firmwareName

    @property
    def firmwareVersion(self):
        return self._firmwareVersion

    @property
    def upgradeAvailable(self):
        return self._upgradeAvailable

    @property
    def upgradeVersion(self):
        return self._upgradeVersion

    @property
    def device_id(self):
        return self._deviceID

    @property
    def tunerCount(self):
        return self._tunerCount

    @property
    def tuner(self):
        return self._tuner
