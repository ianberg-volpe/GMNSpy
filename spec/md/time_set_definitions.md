# time_set_definitions Schema

```txt
spec/time_set_definitions.schema.json
```

The optional time_set_definitions file encodes a set of times-of-day and days-of-week into a timeday_id.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [time_set_definitions.schema.json](../../out/time_set_definitions.schema.json "open original schema") |

## time_set_definitions Type

unknown ([time_set_definitions](time_set_definitions.md))

# time_set_definitions Properties

| Property                  | Type      | Required | Nullable       | Defined by                                                                                                                           |
| :------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| [timeday_id](#timeday_id) | `any`     | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-timeday_id.md "spec/time_set_definitions.schema.json#/properties/timeday_id") |
| [monday](#monday)         | `boolean` | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-monday.md "spec/time_set_definitions.schema.json#/properties/monday")         |
| [tuesday](#tuesday)       | `boolean` | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-tuesday.md "spec/time_set_definitions.schema.json#/properties/tuesday")       |
| [wednesday](#wednesday)   | `boolean` | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-wednesday.md "spec/time_set_definitions.schema.json#/properties/wednesday")   |
| [thursday](#thursday)     | `boolean` | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-thursday.md "spec/time_set_definitions.schema.json#/properties/thursday")     |
| [Friday](#Friday)         | `boolean` | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-friday.md "spec/time_set_definitions.schema.json#/properties/Friday")         |
| [saturday](#saturday)     | `boolean` | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-saturday.md "spec/time_set_definitions.schema.json#/properties/saturday")     |
| [sunday](#sunday)         | `boolean` | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-sunday.md "spec/time_set_definitions.schema.json#/properties/sunday")         |
| [holiday](#holiday)       | `boolean` | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-holiday.md "spec/time_set_definitions.schema.json#/properties/holiday")       |
| [start_time](#start_time) | `time`    | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-start_time.md "spec/time_set_definitions.schema.json#/properties/start_time") |
| [end_time](#end_time)     | `time`    | Optional | cannot be null | [time_set_definitions](time_set_definitions-properties-end_time.md "spec/time_set_definitions.schema.json#/properties/end_time")     |

## timeday_id

Primary key.Primary key, similar to `service_id` in GTFS. Unique name of the time of day. Preferable legible rather than a number.


`timeday_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-timeday_id.md "spec/time_set_definitions.schema.json#/properties/timeday_id")

### timeday_id Type

`any`

## monday

Required. Whether Mondays are included.


`monday`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-monday.md "spec/time_set_definitions.schema.json#/properties/monday")

### monday Type

`boolean`

## tuesday

Required. Whether Tuesdays are included.


`tuesday`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-tuesday.md "spec/time_set_definitions.schema.json#/properties/tuesday")

### tuesday Type

`boolean`

## wednesday

Required. Whether Wednesdays are included.


`wednesday`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-wednesday.md "spec/time_set_definitions.schema.json#/properties/wednesday")

### wednesday Type

`boolean`

## thursday

Required. Whether Thursdays are included.


`thursday`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-thursday.md "spec/time_set_definitions.schema.json#/properties/thursday")

### thursday Type

`boolean`

## Friday

Required. Whether Fridays are included.


`Friday`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-friday.md "spec/time_set_definitions.schema.json#/properties/Friday")

### Friday Type

`boolean`

## saturday

Required. Whether Saturdays are included.


`saturday`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-saturday.md "spec/time_set_definitions.schema.json#/properties/saturday")

### saturday Type

`boolean`

## sunday

Required. Whether Sundays are included.


`sunday`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-sunday.md "spec/time_set_definitions.schema.json#/properties/sunday")

### sunday Type

`boolean`

## holiday

Required. Whether holidays are included.


`holiday`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-holiday.md "spec/time_set_definitions.schema.json#/properties/holiday")

### holiday Type

`boolean`

## start_time

Required. Start time in HH:MM format.


`start_time`

-   is optional
-   Type: `time`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-start_time.md "spec/time_set_definitions.schema.json#/properties/start_time")

### start_time Type

`time`

## end_time

Required. End  time in HH:MM format.


`end_time`

-   is optional
-   Type: `time`
-   cannot be null
-   defined in: [time_set_definitions](time_set_definitions-properties-end_time.md "spec/time_set_definitions.schema.json#/properties/end_time")

### end_time Type

`time`
