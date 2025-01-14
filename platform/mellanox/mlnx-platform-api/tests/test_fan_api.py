#
# Copyright (c) 2020-2021 NVIDIA CORPORATION & AFFILIATES.
# Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import sys
import pytest
from mock import MagicMock
from .mock_platform import MockFan

test_path = os.path.dirname(os.path.abspath(__file__))
modules_path = os.path.dirname(test_path)
sys.path.insert(0, modules_path)

from sonic_platform.fan import Fan
from sonic_platform.led import FanLed
from sonic_platform.fan_drawer import RealDrawer
from sonic_platform.device_data import DEVICE_DATA


def test_get_absence_fan_direction():
    fan_drawer = RealDrawer(0, DEVICE_DATA['x86_64-mlnx_msn2700-r0']['fans'])
    fan = Fan(0, fan_drawer, 1)
    fan_drawer.get_presence = MagicMock(return_value=False)

    assert not fan.is_psu_fan
    assert fan.get_direction() == Fan.FAN_DIRECTION_NOT_APPLICABLE


def test_fan_drawer_set_status_led():
    fan_drawer = RealDrawer(0, DEVICE_DATA['x86_64-mlnx_msn2700-r0']['fans'])
    with pytest.raises(Exception):
        fan_drawer.set_status_led(None, 'Invalid color')

    with pytest.raises(Exception):
        fan_drawer.set_status_led(None, Fan.STATUS_LED_COLOR_RED)
    
    fan1 = Fan(0, fan_drawer, 1)
    fan2 = Fan(1, fan_drawer, 2)
    fan_list = fan_drawer.get_all_fans()
    fan_list.append(fan1)
    fan_list.append(fan2)

    FanLed.set_status = MagicMock()

    fan1.set_status_led(Fan.STATUS_LED_COLOR_RED)
    fan_drawer.set_status_led(Fan.STATUS_LED_COLOR_RED)
    FanLed.set_status.assert_called_with(Fan.STATUS_LED_COLOR_RED)

    fan2.set_status_led(Fan.STATUS_LED_COLOR_GREEN)
    fan_drawer.set_status_led(Fan.STATUS_LED_COLOR_GREEN)
    FanLed.set_status.assert_called_with(Fan.STATUS_LED_COLOR_RED)

    fan1.set_status_led(Fan.STATUS_LED_COLOR_GREEN)
    fan_drawer.set_status_led(Fan.STATUS_LED_COLOR_GREEN)
    FanLed.set_status.assert_called_with(Fan.STATUS_LED_COLOR_GREEN)

    fan1.set_status_led(Fan.STATUS_LED_COLOR_RED)
    fan_drawer.set_status_led(Fan.STATUS_LED_COLOR_RED)
    FanLed.set_status.assert_called_with(Fan.STATUS_LED_COLOR_RED)

