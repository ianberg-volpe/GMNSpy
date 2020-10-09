# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [segment_lane_tod.schema.json](../../out/segment_lane_tod.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property | Type      | Required | Nullable       | Defined by                                                                    |
| :------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------- |
| [0](#0)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `integer` | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `string`  | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-5.md "undefined#/properties/5") |
| [6](#6)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-6.md "undefined#/properties/6") |
| [7](#7)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-7.md "undefined#/properties/7") |
| [8](#8)  | `number`  | Optional | cannot be null | [Untitled schema](segment_lane_tod-properties-8.md "undefined#/properties/8") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key, segment_lane table


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`3`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-3.md "undefined#/properties/3")

### 3 Type

`any`

## 4

Required. Lane number identified as offset to the right from the centerline. i.e. -1, 1, 2 (use left-to-rightnumbering).


`4`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-4.md "undefined#/properties/4")

### 4 Type

`integer`

## 5

Optional. Set of allowed uses; comma-separated. Foreign key to use_definition or use sets.


`5`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-5.md "undefined#/properties/5")

### 5 Type

`string`

## 6

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is None).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `Regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `Physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


`6`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-6.md "undefined#/properties/6")

### 6 Type

`any`

## 7

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is None).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `Regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `Physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


`7`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-7.md "undefined#/properties/7")

### 7 Type

`any`

## 8

Optional. Width of the lane, feet.


`8`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment_lane_tod-properties-8.md "undefined#/properties/8")

### 8 Type

`number`
