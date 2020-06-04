# hacs-minerstat

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
