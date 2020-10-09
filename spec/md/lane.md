# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [lane.schema.json](../../out/lane.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property | Type      | Required | Nullable       | Defined by                                                        |
| :------- | --------- | -------- | -------------- | :---------------------------------------------------------------- |
| [0](#0)  | `any`     | Optional | cannot be null | [Untitled schema](lane-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`     | Optional | cannot be null | [Untitled schema](lane-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `integer` | Optional | cannot be null | [Untitled schema](lane-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `string`  | Optional | cannot be null | [Untitled schema](lane-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `any`     | Optional | cannot be null | [Untitled schema](lane-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `any`     | Optional | cannot be null | [Untitled schema](lane-properties-5.md "undefined#/properties/5") |
| [6](#6)  | `number`  | Optional | cannot be null | [Untitled schema](lane-properties-6.md "undefined#/properties/6") |

## 0

Primary key


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key to link table.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Required. e.g., -1, 1, 2 (use left-to-right numbering).


`2`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-2.md "undefined#/properties/2")

### 2 Type

`integer`

## 3

Required. Set of allowed uses from Use_set: shoulder, parking, walk, all, bike, auto, hov2, hov3, truck, bus, etc.


`3`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-3.md "undefined#/properties/3")

### 3 Type

`string`

## 4

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is none).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


`4`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-4.md "undefined#/properties/4")

### 4 Type

`any`

## 5

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is none).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


`5`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-5.md "undefined#/properties/5")

### 5 Type

`any`

## 6

Optional. Width of the lane, feet.


`6`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-6.md "undefined#/properties/6")

### 6 Type

`number`
