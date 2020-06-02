from homeassistant.helpers import entity
from homeassistant.components.sensor import (PLATFORM_SCHEMA)
from datetime import timedelta
import voluptuous as vol
import urllib.request, json

CONF_NAME = 'name'
CONF_ACCESS_KEY = 'access_key'
CONF_RIG_NAME = 'rig_name'
DEFAULT_NAME = 'Minerstat'
DEFAULT_SCAN_INTERVAL = timedelta(minutes=15)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_ACCESS_KEY): str,
    vol.Required(CONF_RIG_NAME): str
})

class Minerstat(entity.Entity):
    def __init__(self, hass, config):
        self.hass = hass
        self._config = config
        # self._state = None
        self._hashrate = None
        self._unit = None

    # @property
    # def state(self):
    #     return self._state

    @property
    def name(self):
        return self._config[CONF_NAME]

    def update(self):
        with urllib.request.urlopen(f'https://api.minerstat.com/v2/stats/{self._config[CONF_ACCESS_KEY]}') as url:
            data = json.loads(url.read().decode())

            self._hashrate = data[self._config[CONF_RIG_NAME]]['mining']['hashrate']['hashrate']
            self._unit = data[self._config[CONF_RIG_NAME]]['mining']['hashrate']['hashrate_unit']

    @property
    def device_state_attributes(self):
        return {
            'hashrate': self._hashrate,
            'unit': self._unit
        }
