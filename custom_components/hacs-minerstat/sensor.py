from homeassistant.helpers import entity
from homeassistant.components.sensor import (PLATFORM_SCHEMA)
from datetime import timedelta
import voluptuous as vol
import urllib.request, json
import homeassistant.helpers.config_validation as cv

__version__ = '1.0.0'

CONF_NAME = 'name'
CONF_ACCESS_KEY = 'access_key'
CONF_RIG_NAME = 'rig_name'
DEFAULT_NAME = 'Minerstat'
DEFAULT_SCAN_INTERVAL = timedelta(minutes=15)
SCAN_INTERVAL = timedelta(minutes=15)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_ACCESS_KEY): str,
    vol.Required(CONF_RIG_NAME): str
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([Minerstat(hass, config)])

class Minerstat(entity.Entity):
    def __init__(self, hass, config):
        self.hass = hass
        self._config = config
        self._state = None
        self._unit = None
        self.update()

    @property
    def name(self):
        return self._config[CONF_NAME]

    @property
    def icon(self):
        return 'mdi:bitcoin'

    @property
    def state(self):
        return self._state

    def update(self):
        req = urllib.request.Request(f'https://api.minerstat.com/v2/stats/{self._config[CONF_ACCESS_KEY]}/{self._config[CONF_RIG_NAME]}', headers={'User-Agent' : "Home-assistant.io"})
        with urllib.request.urlopen(req) as url:
            data = json.loads(url.read().decode())

            self._state = data[self._config[CONF_RIG_NAME]]['mining']['hashrate']['hashrate']
            self._unit = data[self._config[CONF_RIG_NAME]]['mining']['hashrate']['hashrate_unit']

    @property
    def device_state_attributes(self):
        return {
            'unit_of_measurement': self._unit
        }
