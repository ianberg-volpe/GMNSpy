# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [link_tod.schema.json](../../out/link_tod.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property  | Type      | Required | Nullable       | Defined by                                                              |
| :-------- | --------- | -------- | -------------- | :---------------------------------------------------------------------- |
| [0](#0)   | `any`     | Optional | cannot be null | [Untitled schema](link_tod-properties-0.md "undefined#/properties/0")   |
| [1](#1)   | `any`     | Optional | cannot be null | [Untitled schema](link_tod-properties-1.md "undefined#/properties/1")   |
| [2](#2)   | `any`     | Optional | cannot be null | [Untitled schema](link_tod-properties-2.md "undefined#/properties/2")   |
| [3](#3)   | `any`     | Optional | cannot be null | [Untitled schema](link_tod-properties-3.md "undefined#/properties/3")   |
| [4](#4)   | `integer` | Optional | cannot be null | [Untitled schema](link_tod-properties-4.md "undefined#/properties/4")   |
| [5](#5)   | `integer` | Optional | cannot be null | [Untitled schema](link_tod-properties-5.md "undefined#/properties/5")   |
| [6](#6)   | `integer` | Optional | cannot be null | [Untitled schema](link_tod-properties-6.md "undefined#/properties/6")   |
| [7](#7)   | `string`  | Optional | cannot be null | [Untitled schema](link_tod-properties-7.md "undefined#/properties/7")   |
| [8](#8)   | `string`  | Optional | cannot be null | [Untitled schema](link_tod-properties-8.md "undefined#/properties/8")   |
| [9](#9)   | `string`  | Optional | cannot be null | [Untitled schema](link_tod-properties-9.md "undefined#/properties/9")   |
| [10](#10) | `Any`     | Optional | cannot be null | [Untitled schema](link_tod-properties-10.md "undefined#/properties/10") |
| [11](#11) | `integer` | Optional | cannot be null | [Untitled schema](link_tod-properties-11.md "undefined#/properties/11") |

## 0

Primary key


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key, link table


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`3`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-3.md "undefined#/properties/3")

### 3 Type

`any`

## 4

Optional. Capacity (veh / hr / lane)


`4`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-4.md "undefined#/properties/4")

### 4 Type

`integer`

## 5

Optional. Free flow speed mph


`5`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-5.md "undefined#/properties/5")

### 5 Type

`integer`

## 6

Optional. Number of permanent lanes (not including turn p
pockets) in the direction of travel open to motor vehicles.
It does not include bike lanes, shoulders or parking lanes.


`6`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-6.md "undefined#/properties/6")

### 6 Type

`integer`

## 7

Optional. Type of bicycle accommodation: unknown, none, WCL, sharrow, bikelane, cycletrack, offstreet path


`7`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-7.md "undefined#/properties/7")

### 7 Type

`string`

## 8

Optional. Type of pedestrian accommodation: unknown, none, shoulder, sidewalk, offstreet path


`8`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-8.md "undefined#/properties/8")

### 8 Type

`string`

## 9

Optional. Type of parking: unknown, none, parallel, angle, other


`9`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-9.md "undefined#/properties/9")

### 9 Type

`string`

## 10

Use_Set. Optional.


`10`

-   is optional
-   Type: `Any`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-10.md "undefined#/properties/10")

### 10 Type

`Any`

## 11

toll in cents.


`11`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link_tod-properties-11.md "undefined#/properties/11")

### 11 Type

`integer`
