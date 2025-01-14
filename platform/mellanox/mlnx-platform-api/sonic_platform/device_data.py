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
DEVICE_DATA = {
    'x86_64-mlnx_msn2700-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:30":13, "31:40":14 , "41:120":15},
                "unk_untrust": {"-127:25":13, "26:30":14 , "31:35":15, "36:120":16}
            }
        },
        'fans': {
            'drawer_num': 4,
            'drawer_type': 'real',
            'fan_num_per_drawer': 2,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn2740-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:120":13},
                "unk_untrust": {"-127:15":13, "16:25":14 , "26:30":15, "31:120":17},
            }
        },
        'fans': {
            'drawer_num': 4,
            'drawer_type': 'real',
            'fan_num_per_drawer': 1,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn2100-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:40":12, "41:120":13},
                "unk_untrust": {"-127:15":12, "16:25":13, "26:30":14, "31:35":15, "36:120":16}
            }
        },
        'fans': {
            'drawer_num': 1,
            'drawer_type': 'virtual',
            'fan_num_per_drawer': 4,
            'support_fan_direction': True,
            'hot_swappable': False
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': False,
            'led_num': 2
        }
    },
    'x86_64-mlnx_msn2410-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:30":13, "31:40":14 , "41:120":15},
                "unk_untrust": {"-127:25":13, "26:30":14 , "31:35":15, "36:120":16}
            }
        },
        'fans': {
            'drawer_num': 4,
            'drawer_type': 'real',
            'fan_num_per_drawer': 2,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn2010-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:120":12},
                "unk_untrust": {"-127:15":12, "16:20":13 , "21:30":14, "31:35":15, "36:120":16}
            }
        },
        'fans': {
            'drawer_num': 1,
            'drawer_type': 'virtual',
            'fan_num_per_drawer': 4,
            'support_fan_direction': True,
            'hot_swappable': False
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': False,
            'led_num': 2
        }
    },
    'x86_64-mlnx_msn3700-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:25":12, "26:40":13 , "41:120":14},
                "unk_untrust": {"-127:15":12, "16:30":13 , "31:35":14, "36:40":15, "41:120":16},
            }
        },
        'fans': {
            'drawer_num': 6,
            'drawer_type': 'real',
            'fan_num_per_drawer': 2,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn3700c-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:40":12, "41:120":13},
                "unk_untrust": {"-127:10":12, "11:20":13 , "21:30":14, "31:35":15, "36:120":16},
            }
        },
        'fans': {
            'drawer_num': 4,
            'drawer_type': 'real',
            'fan_num_per_drawer': 2,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn3800-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:30":12, "31:40":13 , "41:120":14},
                "unk_untrust": {"-127:0":12, "1:10":13 , "11:15":14, "16:20":15, "21:35":16, "36:120":17},
            }
        },
        'fans': {
            'drawer_num': 3,
            'drawer_type': 'real',
            'fan_num_per_drawer': 1,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn4700-r0': {
       'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:35":14, "36:120":15},
                "unk_untrust": {"-127:35":14, "36:120":15},
            }
        },
        'fans': {
            'drawer_num': 6,
            'drawer_type': 'real',
            'fan_num_per_drawer': 2,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn4410-r0': {
       'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:120":16},
                "unk_untrust": {"-127:120":16},
            }
        },
        'fans': {
            'drawer_num': 6,
            'drawer_type': 'real',
            'fan_num_per_drawer': 2,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn3420-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:120":12},
                "unk_untrust": {"-127:25":12, "26:35":13, "36:40":14, "41:120":16},
            }
        },
        'fans': {
            'drawer_num': 5,
            'drawer_type': 'real',
            'fan_num_per_drawer': 2,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn4600c-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust":   {"-127:40":12, "41:120":13},
                "unk_untrust": {"-127:5":12, "6:20":13, "21:30":14, "31:35":15, "36:40":16, "41:120":17},
            }
        },
        'fans': {
            'drawer_num': 3,
            'drawer_type': 'real',
            'fan_num_per_drawer': 1,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    },
    'x86_64-mlnx_msn4600-r0': {
        'thermal': {
            'minimum_table': {
                "unk_trust": {"-127:40": 12, "41:120": 13},
                "unk_untrust": {"-127:5": 12, "6:20": 13, "21:30": 14, "31:35": 15, "36:40": 16, "41:120": 17},
            }
        },
        'fans': {
            'drawer_num': 3,
            'drawer_type': 'real',
            'fan_num_per_drawer': 1,
            'support_fan_direction': True,
            'hot_swappable': True
        },
        'psus': {
            'psu_num': 2,
            'fan_num_per_psu': 1,
            'hot_swappable': True,
            'led_num': 1
        }
    }
}
