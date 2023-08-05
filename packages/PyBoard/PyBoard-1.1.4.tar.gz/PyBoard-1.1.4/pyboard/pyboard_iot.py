"""
 Copyright (c) 2018-2019 Kaiyu Liu, All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""


import asyncio
import datetime
import json
import sys
import signal
import argparse
import websockets
from pymata_aio.constants import Constants
from pyboard_core import PyBoardCore


class PyboardIOT:
    def __init__(self, my_core):
        self.core = my_core

        self.command_map = {
            "analogRead": self.analogRead,
            "analogWrite": self.analogWrite,
            "digitalRead": self.digitalRead,
            "digitalWrite": self.digitalWrite,
            "disableAnalogReporting": self.disableAnalogReporting,
            "disableDigitalReporting": self.disableDigitalReporting,
            "enableAnalogReporting": self.disableAnalogReporting,
            "enableDigitalReporting": self.disableDigitalReporting,
            "configEncoder": self.configEncoder,
            "encoderRead": self.encoderRead,
            "getAnalogLatchData": self.getAnalogLatchData,
            "getAnalogMap": self.getAnalogMap,
            "getCapabilityReport": self.getCapabilityReport,
            "getDigitalLatchData": self.getDigitalLatchData,
            "getFirmwareVersion": self.getFirmwareVersion,
            "getPinState": self.getPinState,
            "getProtocolVersion": self.getProtocolVersion,
            "get_pymata_version": self.get_pymata_version,
            "configI2C": self.configI2C,
            "readI2CData": self.readI2CData,
            "readI2CRequest": self.readI2CRequest,
            "writeI2CRequest": self.writeI2CRequest,
            "keepAlive": self.keepAlive,
            "configNeopixel": self.configNeopixel,
            "setNeopixelColor": self.setNeopixelColor,
            "playTone": self.playTone,
            "setAnalogLatch": self.setAnalogLatch,
            "setDigitalLatch": self.setDigitalLatch,
            "pinMode": self.pinMode,
            "setSamplingInterval": self.setSamplingInterval,
            "configSonar": self.configSonar,
            "sonar_read": self.sonar_read,
            "configServo": self.configServo,
            "configStepper": self.configStepper,
            "stepStepper": self.stepStepper
        }
        self.websocket = None

    # noinspection PyUnusedLocal
    async def get_message(self, websocket, path):
        """
        :param websocket: websocket
        :param path: path
        :return:
        """

        self.websocket = websocket
        try:
            while True:
                payload = await self.websocket.recv()

                # cmd_dict = json.loads(payload.decode('utf8'))
                cmd_dict = json.loads(payload)
                client_cmd = cmd_dict.get("method")

                if client_cmd in self.command_map:
                    cmd = self.command_map.get(client_cmd)
                    params = cmd_dict.get("params")
                    if params[0] != "null":
                        await cmd(params)
                    else:
                        await cmd()
        except websockets.exceptions.ConnectionClosed:
            sys.exit()

    async def analogRead(self, command):
        """
        This method reads and returns the last reported value for an analog pin.
        Normally not used since analog pin updates will be provided automatically
        as they occur with the analog_message_reply being sent to the client after pinMode is called.
        (see enableAnalogReporting for message format).

        :param command: {"method": "analogRead", "params": [ANALOG_PIN]}
        :returns: {"method": "analogRead_reply", "params": [PIN, ANALOG_DATA_VALUE]}
        """
        pin = int(command[0])
        data_val = await self.core.analog_read(pin)
        reply = json.dumps({"method": "analogRead_reply", "params": [pin, data_val]})
        await self.websocket.send(reply)

    async def analogWrite(self, command):
        """
        This method writes a value to an analog pin.

        It is used to set the output of a PWM pin or the angle of a Servo.

        :param command: {"method": "analogWrite", "params": [PIN, WRITE_VALUE]}
        :returns: No return message.
        """
        pin = int(command[0])
        value = int(command[1])
        await self.core.analog_write(pin, value)

    async def digitalRead(self, command):
        """
        This method reads and returns the last reported value for a digital pin.
        Normally not used since digital pin updates will be provided automatically
        as they occur with the digital_message_reply being sent to the client after pinMode is called..
        (see enableDigitalReporting for message format)

        :param command: {"method": "digitalRead", "params": [PIN]}
        :returns: {"method": "digitalRead_reply", "params": [PIN, DIGITAL_DATA_VALUE]}
        """
        pin = int(command[0])
        data_val = await self.core.digital_read(pin)
        reply = json.dumps({"method": "digitalRead_reply", "params": [pin, data_val]})
        await self.websocket.send(reply)

    async def digitalWrite(self, command):
        """
        This method writes a zero or one to a digital pin.

        :param command: {"method": "digitalWrite", "params": [PIN, DIGITAL_DATA_VALUE]}
        :returns: No return message..
        """
        pin = int(command[0])
        value = int(command[1])
        await self.core.digital_write(pin, value)

    async def disableAnalogReporting(self, command):
        """
        Disable Firmata reporting for an analog pin.

        :param command: {"method": "disableAnalogReporting", "params": [PIN]}
        :returns: No return message..
        """
        pin = int(command[0])
        await self.core.disable_analog_reporting(pin)

    async def disableDigitalReporting(self, command):
        """
        Disable Firmata reporting for a digital pin.

        :param command: {"method": "disableDigitalReporting", "params": [PIN]}
        :returns: No return message.
        """
        pin = int(command[0])
        await self.core.disable_digital_reporting(pin)

    async def enableAnalogReporting(self, command):
        """
        Enable Firmata reporting for an analog pin.

        :param command: {"method": "enableAnalogReporting", "params": [PIN]}
        :returns: {"method": "analog_message_reply", "params": [PIN, ANALOG_DATA_VALUE]}
        """
        pin = int(command[0])
        await self.core.enable_analog_reporting(pin)

    async def enableDigitalReporting(self, command):
        """
        Enable Firmata reporting for a digital pin.

        :param command: {"method": "enableDigitalReporting", "params": [PIN]}
        :returns: {"method": "digital_message_reply", "params": [PIN, DIGITAL_DATA_VALUE]}
        """
        pin = int(command[0])
        await self.core.enable_digital_reporting(pin)

    async def configEncoder(self, command):
        """
        Configure 2 pins for FirmataPlus encoder operation.

        :param command: {"method": "configEncoder", "params": [PIN_A, PIN_B]}
        :returns: {"method": "encoder_data_reply", "params": [ENCODER_DATA]}
        """
        pin_a = int(command[0])
        pin_b = int(command[1])
        await self.core.encoder_config(pin_a, pin_b, self.encoder_callback)

    async def encoderRead(self, command):
        """
        This is a polling method to read the last cached FirmataPlus encoder value.
        Normally not used. See encoder config for the asynchronous report message format.

        :param command: {"method": "encoderRead", "params": [PIN_A]}
        :returns: {"method": "encoderRead_reply", "params": [PIN_A, ENCODER_VALUE]}
        """
        pin = int(command[0])
        val = await self.core.encoder_read(pin)
        reply = json.dumps({"method": "encoderRead_reply", "params": [pin, val]})
        await self.websocket.send(reply)

    async def getAnalogLatchData(self, command):
        """
        This method retrieves a latch table entry for an analog pin.

        See constants.py for definition of reply message parameters.

        :param command:  {"method": "getAnalogLatchData", "params": [ANALOG_PIN]}
        :returns: {"method": "getAnalogLatchData_reply", "params": [ANALOG_PIN, LATCHED_STATE, THRESHOLD_TYPE,\
         THRESHOLD_TARGET, DATA_VALUE, TIME_STAMP ]}
        """
        pin = int(command[0])
        data_val = await self.core.get_analog_latch_data(pin)
        if data_val:
            data_val = data_val[0:-1]
        reply = json.dumps({"method": "getAnalogLatchData_reply", "params": [pin, data_val]})
        await self.websocket.send(reply)

    async def getAnalogMap(self):
        """
        This method retrieves the Firmata analog map.

        Refer to: http://firmata.org/wiki/Protocol#Analog_Mapping_Query to interpret the reply

        The command JSON format is: {"method":"getAnalogMap","params":["null"]}
        :returns: {"method": "analog_map_reply", "params": [ANALOG_MAP]}
        """
        value = await self.core.get_analog_map()
        if value:
            reply = json.dumps({"method": "analog_map_reply", "params": value})
        else:
            reply = json.dumps({"method": "analog_map_reply", "params": "None"})
        await self.websocket.send(reply)

    async def getCapabilityReport(self):
        """
        This method retrieves the Firmata capability report.

        Refer to http://firmata.org/wiki/Protocol#Capability_Query

        The command format is: {"method":"getCapabilityReport","params":["null"]}

        :returns: {"method": "capability_report_reply", "params": [RAW_CAPABILITY_REPORT]}
        """
        value = await self.core.get_capability_report()
        await asyncio.sleep(.1)
        if value:
            reply = json.dumps({"method": "capability_report_reply", "params": value})
        else:
            reply = json.dumps({"method": "capability_report_reply", "params": "None"})
        await self.websocket.send(reply)

    async def getDigitalLatchData(self, command):
        """
        This method retrieves a latch table entry for a digital pin.

        See constants.py for definition of reply message parameters.

        :param command:  {"method": "getDigitalLatchData", "params": [DPIN]}
        :returns: {"method": "getDigitalLatchData_reply", "params": [DIGITAL_PIN, LATCHED_STATE, THRESHOLD_TYPE,\
         THRESHOLD_TARGET, DATA_VALUE, TIME_STAMP ]}
        """
        pin = int(command[0])
        data_val = await self.core.get_digital_latch_data(pin)
        if data_val:
            data_val = data_val[0:-1]
        reply = json.dumps({"method": "getDigitalLatchData_reply", "params": [pin, data_val]})
        await self.websocket.send(reply)

    async def getFirmwareVersion(self):
        """
        This method retrieves the Firmata firmware version.

        See: http://firmata.org/wiki/Protocol#Query_Firmware_Name_and_Version


        JSON command: {"method": "getFirmwareVersion", "params": ["null"]}

        :returns: {"method": "firmware_version_reply", "params": [FIRMWARE_VERSION]}
        """
        value = await self.core.get_firmware_version()
        if value:
            reply = json.dumps({"method": "firmware_version_reply", "params": value})
        else:
            reply = json.dumps({"method": "firmware_version_reply", "params": "Unknown"})
        await self.websocket.send(reply)

    async def getPinState(self, command):
        """
        This method retrieves a Firmata pin_state report for a pin..

        See: http://firmata.org/wiki/Protocol#Pin_State_Query

        :param command: {"method": "getPinState", "params": [PIN]}
        :returns: {"method": "getPinState_reply", "params": [PIN_NUMBER, PIN_MODE, PIN_STATE]}
        """
        pin = int(command[0])
        value = await self.core.get_pin_state(pin)
        if value:
            reply = json.dumps({"method": "pin_state_reply", "params": value})
        else:
            reply = json.dumps({"method": "pin_state_reply", "params": "Unknown"})
        await self.websocket.send(reply)

    async def getProtocolVersion(self):
        """
        This method retrieves the Firmata protocol version.

        JSON command: {"method": "getProtocolVersion", "params": ["null"]}

        :returns: {"method": "protocol_version_reply", "params": [PROTOCOL_VERSION]}
        """
        value = await self.core.get_protocol_version()
        if value:
            reply = json.dumps({"method": "protocol_version_reply", "params": value})
        else:
            reply = json.dumps({"method": "protocol_version_reply", "params": "Unknown"})
        await self.websocket.send(reply)

    async def get_pymata_version(self):
        """
         This method retrieves the PyMata release version number.

         JSON command: {"method": "get_pymata_version", "params": ["null"]}

         :returns:  {"method": "pymata_version_reply", "params":[PYMATA_VERSION]}
        """
        value = await self.core.get_pymata_version()
        if value:
            reply = json.dumps({"method": "pymata_version_reply", "params": value})
        else:
            reply = json.dumps({"method": "pymata_version_reply", "params": "Unknown"})
        await self.websocket.send(reply)

    async def configI2C(self, command):
        """
        This method initializes the I2c and sets the optional read delay (in microseconds).

        It must be called before doing any other i2c operations for a given device.
        :param command: {"method": "configI2C", "params": [DELAY]}
        :returns: No Return message.
        """
        delay = int(command[0])
        await self.core.i2c_config(delay)

    async def readI2CData(self, command):
        """
        This method retrieves the last value read for an i2c device identified by address.
        This is a polling implementation and readI2CRequest and readI2CRequest_reply may be
        a better alternative.
        :param command: {"method": "readI2CData", "params": [I2C_ADDRESS ]}
        :returns:{"method": "readI2CData_reply", "params": i2c_data}
        """
        address = int(command[0])
        i2c_data = await self.core.i2c_read_data(address)
        reply = json.dumps({"method": "readI2CData_reply", "params": i2c_data})
        await self.websocket.send(reply)

    async def readI2CRequest(self, command):
        """
        This method sends an I2C read request to Firmata. It is qualified by a single shot, continuous
        read, or stop reading command.
        Special Note: for the read type supply one of the following string values:

         "0" = I2C_READ

         "1" = I2C_READ | I2C_END_TX_MASK"

         "2" = I2C_READ_CONTINUOUSLY

         "3" = I2C_READ_CONTINUOUSLY | I2C_END_TX_MASK

         "4" = I2C_STOP_READING

        :param command: {"method": "readI2CRequest", "params": [I2C_ADDRESS, I2C_REGISTER,
                NUMBER_OF_BYTES, I2C_READ_TYPE ]}
        :returns: {"method": "readI2CRequest_reply", "params": [DATA]}
        """
        device_address = int(command[0])
        register = int(command[1])
        number_of_bytes = int(command[2])

        if command[3] == "0":
            read_type = Constants.I2C_READ_CONTINUOUSLY
        elif command[3] == "1":
            read_type = Constants.I2C_READ
        elif command[3] == "2":
            read_type = Constants.I2C_READ | Constants.I2C_END_TX_MASK
        elif command[3] == "3":
            read_type = Constants.I2C_READ_CONTINUOUSLY | Constants.I2C_END_TX_MASK
        else:  # the default case stop reading valid request or invalid request
            read_type = Constants.I2C_STOP_READING

        await self.core.i2c_read_request(device_address, register, number_of_bytes, read_type,
                                         self.readI2CRequest_callback)
        await asyncio.sleep(.1)

    async def writeI2CRequest(self, command):
        """
        This method performs an I2C write at a given I2C address,
        :param command: {"method": "writeI2CRequest", "params": [I2C_DEVICE_ADDRESS, [DATA_TO_WRITE]]}
        :returns:No return message.
        """
        device_address = int(command[0])
        params = command[1]
        params = [int(i) for i in params]
        await self.core.i2c_write_request(device_address, params)

    async def keepAlive(self, command):
        """
        Periodically send a keep alive message to the Arduino.
        Frequency of keep alive transmission is calculated as follows:
        keepAlive_sent = period - (period * margin)

        :param command:  {"method": "keepAlive", "params": [PERIOD, MARGIN]}
        Period is time period between keepalives. Range is 0-10 seconds. 0 disables the keepalive mechanism.
        Margin is a  safety margin to assure keepalives are sent before period expires. Range is 0.1 to 0.9
        :returns: No return value
        """
        period = int(command[0])
        margin = int(command[1])
        await self.core.keep_alive(period, margin)

    async def playTone(self, command):
        """
        This method controls a piezo device to play a tone. It is a FirmataPlus feature.
        Tone command is TONE_TONE to play, TONE_NO_TONE to stop playing.
        :param command: {"method": "playTone", "params": [PIN, TONE_COMMAND, FREQUENCY(Hz), DURATION(MS)]}
        :returns:No return message.
        """
        pin = int(command[0])
        if command[1] == "TONE_TONE":
            tone_command = Constants.TONE_TONE
        else:
            tone_command = Constants.TONE_NO_TONE
        frequency = int(command[2])
        duration = int(command[3])
        await self.core.play_tone(pin, tone_command, frequency, duration)

    async def setAnalogLatch(self, command):
        """
        This method sets the an analog latch for a given analog pin, providing the threshold type, and
        latching threshold.
        :param command: {"method": "setAnalogLatch", "params": [PIN, THRESHOLD_TYPE, THRESHOLD_VALUE]}
        :returns:{"method": "analog_latch_data_reply", "params": [PIN, DATA_VALUE_LATCHED, TIMESTAMP_STRING]}
        """
        pin = int(command[0])
        threshold_type = int(command[1])
        threshold_value = int(command[2])
        await self.core.set_analog_latch(pin, threshold_type, threshold_value, self.analog_latch_callback)

    async def setDigitalLatch(self, command):
        """
        This method sets the a digital latch for a given digital pin, the threshold type, and latching threshold.
        :param command:{"method": "setDigitalLatch", "params": [PIN, THRESHOLD (0 or 1)]}
        :returns:{"method": digital_latch_data_reply", "params": [PIN, DATA_VALUE_LATCHED, TIMESTAMP_STRING]}
        """
        pin = int(command[0])
        threshold_value = int(command[1])
        await self.core.set_digital_latch(pin, threshold_value, self.digital_latch_callback)

    async def pinMode(self, command):
        """
        This method sets the pin mode for the selected pin. It handles: Input, Analog(Input) PWM, and OUTPUT. Servo
        is handled by configServo().
        :param command: {"method": "pinMode", "params": [PIN, MODE]}
        :returns:No return message.
        """
        pin = int(command[0])
        mode = int(command[1])
        if mode == Constants.INPUT:
            cb = self.digital_callback
        elif mode == Constants.ANALOG:
            cb = self.analog_callback
        else:
            cb = None

        await self.core.set_pin_mode(pin, mode, cb)

    async def setSamplingInterval(self, command):
        """
        This method sets the Firmata sampling interval in ms.
        :param command:{"method": "setSamplingInterval", "params": [INTERVAL]}
        :returns:No return message.
        """
        sample_interval = int(command[0])
        await self.core.set_sampling_interval(sample_interval)

    async def configSonar(self, command):
        """
        This method configures 2 pins to support HC-SR04 Ping devices.
        This is a FirmataPlus feature.
        :param command: {"method": "configSonar", "params": [TRIGGER_PIN, ECHO_PIN, PING_INTERVAL(default=50),
         MAX_DISTANCE(default= 200 cm]}
        :returns:{"method": "sonar_data_reply", "params": [DISTANCE_IN_CM]}
        """
        trigger = int(command[0])
        echo = int(command[1])
        interval = int(command[2])
        max_dist = int(command[3])
        await self.core.sonar_config(trigger, echo, self.sonar_callback, interval, max_dist)

    async def sonar_read(self, command):
        """
        This method retrieves the last sonar data value that was cached.
        This is a polling method. After sonar config, sonar_data_reply messages will be sent automatically.
        :param command: {"method": "sonar_read", "params": [TRIGGER_PIN]}
        :returns:{"method": "sonar_read_reply", "params": [TRIGGER_PIN, DATA_VALUE]}
        """
        pin = int(command[0])
        val = await self.core.sonar_data_retrieve(pin)

        reply = json.dumps({"method": "sonar_read_reply", "params": [pin, val]})
        await self.websocket.send(reply)

    async def configNeopixel(self, command):
        """
        This method configures a digital pin to support configNeopixel devices.
        This is a FirmataPlus feature.
        :param command: {"method": "configNeopixel", "params": [datapin,, count, brightness]}
        :returns:No message returned.
        """
        pin = int(command[0])
        ledcount = int(command[1])
        brightness = int(command[2])
        await self.core.neopixel_config(pin, ledcount, brightness)

    async def setNeopixelColor(self, command):
        """
        This method retrieves the last sonar data value that was cached.
        This is a polling method. After sonar config, sonar_data_reply messages will be sent automatically.
        :param command: {"method": "sonar_read", "params": [TRIGGER_PIN]}
        :returns:{"method": "sonar_read_reply", "params": [TRIGGER_PIN, DATA_VALUE]}
        """
        index = int(command[0])
        red = int(command[1])
        green = int(command[2])
        blue = int(command[3])
        await self.core.neopixel(index, red, green, blue)


    async def configServo(self, command):
        """
        This method configures a pin for servo operation. The servo angle is set by using analogWrite().
        :param command: {"method": "configServo", "params": [PIN, MINIMUM_PULSE(ms), MAXIMUM_PULSE(ms)]}
        :returns:No message returned.
        """
        pin = int(command[0])
        min_pulse = int(command[1])
        max_pulse = int(command[2])
        await self.core.servo_config(pin, min_pulse, max_pulse)

    async def configStepper(self, command):
        """
        This method configures 4 pins for stepper motor operation.
        This is a FirmataPlus feature.
        :param command: {"method": "configStepper", "params": [STEPS_PER_REVOLUTION, [PIN1, PIN2, PIN3, PIN4]]}
        :returns:No message returned.
        """
        steps_per_revs = int(command[0])
        pins = command[1]
        pin1 = int(pins[0])
        pin2 = int(pins[1])
        pin3 = int(pins[2])
        pin4 = int(pins[3])
        await self.core.stepper_config(steps_per_revs, [pin1, pin2, pin3, pin4])

    async def stepStepper(self, command):
        """
        This method activates a stepper motor motion.
        This is a FirmataPlus feature.
        :param command: {"method": "stepper_step", "params": [SPEED, NUMBER_OF_STEPS]}
        :returns:No message returned.
        """
        speed = int(command[0])
        num_steps = int(command[1])
        await self.core.stepper_step(speed, num_steps)

    def analog_callback(self, data):
        """
        This method handles the analog message received from pymata_core
        :param data: analog callback message
        :returns:{"method": "analog_message_reply", "params": [PIN, DATA_VALUE}
        """
        reply = json.dumps({"method": "analog_message_reply", "params": [data[0], data[1]]})
        asyncio.ensure_future(self.websocket.send(reply))

    def analog_latch_callback(self, data):
        """
        This method handles analog_latch data received from pymata_core
        :param data: analog latch callback message
        :returns:{"method": "analog_latch_data_reply", "params": [ANALOG_PIN, VALUE_AT_TRIGGER, TIME_STAMP_STRING]}
        """
        ts = data[2]
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        reply = json.dumps({"method": "analog_latch_data_reply", "params": [data[0], data[1], st]})
        asyncio.ensure_future(self.websocket.send(reply))

    def digital_callback(self, data):
        """
        This method handles the digital message received from pymata_core
        :param data: digital callback message
        :returns:{"method": "digital_message_reply", "params": [PIN, DATA_VALUE]}
        """
        reply = json.dumps({"method": "digital_message_reply", "params": [data[0], data[1]]})
        asyncio.ensure_future(self.websocket.send(reply))

    def digital_latch_callback(self, data):
        """
        This method handles the digital latch data message received from pymata_core
        :param data: digital latch callback message
        :returns:s{"method": "digital_latch_data_reply", "params": [PIN, DATA_VALUE_AT_TRIGGER, TIME_STAMP_STRING]}
        """
        ts = data[2]
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        reply = json.dumps({"method": "digital_latch_data_reply", "params": [data[0], data[1], st]})
        asyncio.ensure_future(self.websocket.send(reply))

    def encoder_callback(self, data):
        """
        This method handles the encoder data message received from pymata_core
        :param data: encoder data callback message
        :returns:{"method": "encoder_data_reply", "params": [ENCODER VALUE]}
        """
        reply = json.dumps({"method": "encoder_data_reply", "params": data})
        asyncio.ensure_future(self.websocket.send(reply))

    def readI2CRequest_callback(self, data):
        """
        This method handles the i2c read data message received from pymata_core.
        :param data: i2c read data callback message
        :returns:{"method": "readI2CRequest_reply", "params": [DATA_VALUE]}
        """
        reply = json.dumps({"method": "readI2CRequest_reply", "params": data})
        asyncio.ensure_future(self.websocket.send(reply))

    def readI2CData_callback(self, data):
        """
        This method handles the i2c cached read data received from pymata_core.
        :param data: i2c read cached data callback message
        :returns:{"method": "readI2CData_reply", "params": [DATA_VALUE]}
        """
        reply = json.dumps({"method": "readI2CData_reply", "params": data})
        asyncio.ensure_future(self.websocket.send(reply))

    def sonar_callback(self, data):
        """
        This method handles sonar data received from pymata_core.
        :param data: sonar data callback message
        :returns:{"method": "sonar_data_reply", "params": [DATA_VALUE]}
        """
        reply = json.dumps({"method": "sonar_data_reply", "params": data})
        asyncio.ensure_future(self.websocket.send(reply))


"""

 usage: pymata_iot.py [-h] [-host HOSTNAME] [-port PORT] [-wait WAIT]
                 [-comport COM] [-sleep SLEEP] [-log LOG]

    optional arguments:
      -h, --help      show this help message and exit
      -host HOSTNAME  Server name or IP address
      -port PORT      Server port number
      -wait WAIT      Arduino wait time
      -comport COM    Arduino COM port
      -sleep SLEEP    sleep tune in ms.
      -log LOG        True = send output to file, False = send output to console
      -ardIPAddr ADDR Wireless module ip address (WiFly)
      -ardPort PORT   Wireless module ip port (Wifly)
      -handshake STR  Wireless device handshake string (WiFly)
"""
parser = argparse.ArgumentParser()
parser.add_argument("-host", dest="hostname", default="localhost", help="Server name or IP address")
parser.add_argument("-port", dest="port", default="9000", help="Server port number")
parser.add_argument("-wait", dest="wait", default="2", help="Arduino wait time")
parser.add_argument("-comport", dest="com", default="None", help="Arduino COM port")
parser.add_argument("-sleep", dest="sleep", default=".001", help="sleep tune in ms.")
parser.add_argument("-log", dest="log", default="False", help="redirect console output to log file")
parser.add_argument("-ardIPAddr", dest="aIPaddr", default="None", help="Arduino IP Address (WiFly")
parser.add_argument("-ardPort", dest="aIPport", default="2000", help="Arduino IP port (WiFly")
parser.add_argument("-handshake", dest="handshake", default="*HELLO*", help="IP Device Handshake String")

args = parser.parse_args()

ip_addr = args.hostname
ip_port = args.port

if args.com == 'None':
    comport = None
else:
    comport = args.com

if args.log == 'True':
    log = True
else:
    log = False

ard_ip_addr = args.aIPaddr
ard_ip_port = args.aIPport
ard_handshake = args.handshake

core = PyBoardCore(int(args.wait), float(args.sleep), log, comport, 
                  ard_ip_addr, ard_ip_port, ard_handshake)

# core = PymataCore()
core.start()


# Signal handler to trap control C
# noinspection PyUnusedLocal,PyUnusedLocal
def _signal_handler(sig, frame):
    if core is not None:
        print('\nYou pressed Ctrl+C')
        task = asyncio.ensure_future(core.shutdown())
        asyncio.get_event_loop().run_until_complete(task)
        sys.exit(1)


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)
server = PyboardIOT(core)

try:
    start_server = websockets.serve(server.get_message, '127.0.0.1', 9000)

    asyncio.get_event_loop().run_until_complete(start_server)

    asyncio.get_event_loop().run_forever()
except websockets.exceptions.ConnectionClosed:
    sys.exit()
except RuntimeError:
    sys.exit()
