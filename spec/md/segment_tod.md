# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [segment_tod.schema.json](../../out/segment_tod.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property  | Type      | Required | Nullable       | Defined by                                                                 |
| :-------- | --------- | -------- | -------------- | :------------------------------------------------------------------------- |
| [0](#0)   | `any`     | Optional | cannot be null | [Untitled schema](segment_tod-properties-0.md "undefined#/properties/0")   |
| [1](#1)   | `any`     | Optional | cannot be null | [Untitled schema](segment_tod-properties-1.md "undefined#/properties/1")   |
| [2](#2)   | `any`     | Optional | cannot be null | [Untitled schema](segment_tod-properties-2.md "undefined#/properties/2")   |
| [3](#3)   | `any`     | Optional | cannot be null | [Untitled schema](segment_tod-properties-3.md "undefined#/properties/3")   |
| [4](#4)   | `integer` | Optional | cannot be null | [Untitled schema](segment_tod-properties-4.md "undefined#/properties/4")   |
| [5](#5)   | `integer` | Optional | cannot be null | [Untitled schema](segment_tod-properties-5.md "undefined#/properties/5")   |
| [6](#6)   | `integer` | Optional | cannot be null | [Untitled schema](segment_tod-properties-6.md "undefined#/properties/6")   |
| [7](#7)   | `integer` | Optional | cannot be null | [Untitled schema](segment_tod-properties-7.md "undefined#/properties/7")   |
| [8](#8)   | `integer` | Optional | cannot be null | [Untitled schema](segment_tod-properties-8.md "undefined#/properties/8")   |
| [9](#9)   | `string`  | Optional | cannot be null | [Untitled schema](segment_tod-properties-9.md "undefined#/properties/9")   |
| [10](#10) | `string`  | Optional | cannot be null | [Untitled schema](segment_tod-properties-10.md "undefined#/properties/10") |
| [11](#11) | `string`  | Optional | cannot be null | [Untitled schema](segment_tod-properties-11.md "undefined#/properties/11") |
| [12](#12) | `integer` | Optional | cannot be null | [Untitled schema](segment_tod-properties-12.md "undefined#/properties/12") |
| [13](#13) | `string`  | Optional | cannot be null | [Untitled schema](segment_tod-properties-13.md "undefined#/properties/13") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Foreign key to segment table.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`3`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-3.md "undefined#/properties/3")

### 3 Type

`any`

## 4

Optional. Capacity (veh/hr/ln)


`4`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-4.md "undefined#/properties/4")

### 4 Type

`integer`

## 5

Optional. Free flow speed (mph)


`5`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-5.md "undefined#/properties/5")

### 5 Type

`integer`

## 6

Optional. Number of lanes in the direction of travel (must be consistent with link lanes + lanes added).


`6`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-6.md "undefined#/properties/6")

### 6 Type

`integer`

## 7

Optional. # of lanes added on the left of the road link (negative indicates a lane drop).


`7`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-7.md "undefined#/properties/7")

### 7 Type

`integer`

## 8

Optional. # of lanes added on the right of the road link (negative indicates a lane drop).


`8`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-8.md "undefined#/properties/8")

### 8 Type

`integer`

## 9

Optional. Type of bicycle accommodation: unknown, none,wcl, bikelane,cycletrack,wide_shoulder, offstreet_path.


`9`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-9.md "undefined#/properties/9")

### 9 Type

`string`

## 10

Optional. Type of pedestrian accommodation: unknown,none,shoulder,sidewalk,offstreet_path.


`10`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-10.md "undefined#/properties/10")

### 10 Type

`string`

## 11

Optional. Type of parking: unknown,none,shoulder,sidewalk,offstreet_path.


`11`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-11.md "undefined#/properties/11")

### 11 Type

`string`

## 12

Optional. Toll in cents


`12`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-12.md "undefined#/properties/12")

### 12 Type

`integer`

## 13

Optional. Set of allowed uses; comma-separated. Foreign key to use_definition or use sets.


`13`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment_tod-properties-13.md "undefined#/properties/13")

### 13 Type

`string`
