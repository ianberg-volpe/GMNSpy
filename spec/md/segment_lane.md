# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [segment_lane.schema.json](../../out/segment_lane.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property | Type      | Required | Nullable       | Defined by                                                                |
| :------- | --------- | -------- | -------------- | :------------------------------------------------------------------------ |
| [0](#0)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `integer` | Optional | cannot be null | [Untitled schema](segment_lane-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `string`  | Optional | cannot be null | [Untitled schema](segment_lane-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-5.md "undefined#/properties/5") |
| [6](#6)  | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-6.md "undefined#/properties/6") |
| [7](#7)  | `number`  | Optional | cannot be null | [Untitled schema](segment_lane-properties-7.md "undefined#/properties/7") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key to the associated segment.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Required. -1, 1, 2 (use left-to-right numbering). 0 signifies a lane that is dropped on the segment.


`2`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-2.md "undefined#/properties/2")

### 2 Type

`integer`

## 3

Optional. If a lane drops or changes characteristics on the segment, the lane_id for that lane.


`3`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-3.md "undefined#/properties/3")

### 3 Type

`any`

## 4

Optional. Set of allowed uses; comma-separated. Foreign key for use group.


`4`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-4.md "undefined#/properties/4")

### 4 Type

`string`

## 5

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is none)


`5`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-5.md "undefined#/properties/5")

### 5 Type

`any`

## 6

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the left (default is none)


`6`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-6.md "undefined#/properties/6")

### 6 Type

`any`

## 7

Optional. Width of the lane (feet)


`7`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-7.md "undefined#/properties/7")

### 7 Type

`number`
