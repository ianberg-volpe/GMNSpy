# signal_timing_plan Schema

```txt
spec/signal_timing_plan.schema.json
```

For signalized nodes, establishes timing plans.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_timing_plan.schema.json](../../out/signal_timing_plan.schema.json "open original schema") |

## signal_timing_plan Type

unknown ([signal_timing_plan](signal_timing_plan.md))

# signal_timing_plan Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                             |
| :-------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| [timing_plan_id](#timing_plan_id) | `any`     | Required | cannot be null | [signal_timing_plan](signal_timing_plan-properties-timing_plan_id.md "spec/signal_timing_plan.schema.json#/properties/timing_plan_id") |
| [controller_id](#controller_id)   | `any`     | Required | cannot be null | [signal_timing_plan](signal_timing_plan-properties-controller_id.md "spec/signal_timing_plan.schema.json#/properties/controller_id")   |
| [timeday_id](#timeday_id)         | `any`     | Optional | cannot be null | [signal_timing_plan](signal_timing_plan-properties-timeday_id.md "spec/signal_timing_plan.schema.json#/properties/timeday_id")         |
| [time_day](#time_day)             | `any`     | Optional | cannot be null | [signal_timing_plan](signal_timing_plan-properties-time_day.md "spec/signal_timing_plan.schema.json#/properties/time_day")             |
| [cycle_length](#cycle_length)     | `integer` | Optional | cannot be null | [signal_timing_plan](signal_timing_plan-properties-cycle_length.md "spec/signal_timing_plan.schema.json#/properties/cycle_length")     |

## timing_plan_id

Primary key.


`timing_plan_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_plan](signal_timing_plan-properties-timing_plan_id.md "spec/signal_timing_plan.schema.json#/properties/timing_plan_id")

### timing_plan_id Type

`any`

## controller_id

Required. Foreign key (signal_controller table).


`controller_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_plan](signal_timing_plan-properties-controller_id.md "spec/signal_timing_plan.schema.json#/properties/controller_id")

### controller_id Type

`any`

## timeday_id

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`timeday_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_plan](signal_timing_plan-properties-timeday_id.md "spec/signal_timing_plan.schema.json#/properties/timeday_id")

### timeday_id Type

`any`

## time_day

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`time_day`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_plan](signal_timing_plan-properties-time_day.md "spec/signal_timing_plan.schema.json#/properties/time_day")

### time_day Type

`any`

## cycle_length

Cycle length in seconds.


`cycle_length`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_plan](signal_timing_plan-properties-cycle_length.md "spec/signal_timing_plan.schema.json#/properties/cycle_length")

### cycle_length Type

`integer`

### cycle_length Constraints

**maximum**: the value of this number must smaller than or equal to: `600`

**minimum**: the value of this number must greater than or equal to: `0`
