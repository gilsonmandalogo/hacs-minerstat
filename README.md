# hacs-minerstat

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
![Validate](https://github.com/gilsonmandalogo/hacs-minerstat/workflows/Validate/badge.svg)
[![buy_me_a_coffee_badge](https://img.shields.io/badge/Buy%20me%20a%20coffee-donate-yellow.svg)](https://www.buymeacoffee.com/gilson)

A integration with [Minerstart](https://minerstat.com/) to create a sensor from your rig's hashrate.

## Usage
`configuration.yaml`:
```yaml
sensor:
  - platform: hacs-minerstat
    name: "My Awesome Rig"
    access_key: "00000000"
    rig_name: "RIG1"
```

## Options
|Name|Type|Necessity|Default|Description|
|----|:--:|:-------:|:-----:|-----------|
|`platform`|string|**Required**|`hacs-minerstat`|The platform name|
|`access_key`|string|**Required**||Your personal access key from https://my.minerstat.com/|
|`rig_name`|string|**Required**||The name that you defined for your rig at Minerstat|
|`name`|string|Optional|`Minerstat`|Custom name for the sensor|

## Support this project

**Buy me a ~~coffee~~ beer 🍺**: https://www.buymeacoffee.com/gilson

**BTC**: 33TwXHzMTpSNMJZ4JcwExLExsF3BshBUPE

**ETH**: 0xa772c6bab9d175256ff635843c461d3f65a7236b

**LTC**: M9adpiNQXsbEf7j5ZVnuDCGNoXT7oMW3vd
