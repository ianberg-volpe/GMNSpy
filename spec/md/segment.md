# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [segment.schema.json](../../out/segment.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property  | Type      | Required | Nullable       | Defined by                                                             |
| :-------- | --------- | -------- | -------------- | :--------------------------------------------------------------------- |
| [0](#0)   | `any`     | Optional | cannot be null | [Untitled schema](segment-properties-0.md "undefined#/properties/0")   |
| [1](#1)   | `any`     | Optional | cannot be null | [Untitled schema](segment-properties-1.md "undefined#/properties/1")   |
| [2](#2)   | `any`     | Optional | cannot be null | [Untitled schema](segment-properties-2.md "undefined#/properties/2")   |
| [3](#3)   | `number`  | Optional | cannot be null | [Untitled schema](segment-properties-3.md "undefined#/properties/3")   |
| [4](#4)   | `number`  | Optional | cannot be null | [Untitled schema](segment-properties-4.md "undefined#/properties/4")   |
| [5](#5)   | `number`  | Optional | cannot be null | [Untitled schema](segment-properties-5.md "undefined#/properties/5")   |
| [6](#6)   | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-6.md "undefined#/properties/6")   |
| [7](#7)   | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-7.md "undefined#/properties/7")   |
| [8](#8)   | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-8.md "undefined#/properties/8")   |
| [9](#9)   | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-9.md "undefined#/properties/9")   |
| [10](#10) | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-10.md "undefined#/properties/10") |
| [11](#11) | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-11.md "undefined#/properties/11") |
| [12](#12) | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-12.md "undefined#/properties/12") |
| [13](#13) | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-13.md "undefined#/properties/13") |
| [14](#14) | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-14.md "undefined#/properties/14") |
| [15](#15) | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-15.md "undefined#/properties/15") |
| [16](#16) | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-16.md "undefined#/properties/16") |
| [17](#17) | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-17.md "undefined#/properties/17") |
| [18](#18) | `number`  | Optional | cannot be null | [Untitled schema](segment-properties-18.md "undefined#/properties/18") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key to road_links. The link that the segment is located on.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Required. Foreign key to node where distance is 0.


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Required. Distance from `ref_node_id`.


`3`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-3.md "undefined#/properties/3")

### 3 Type

`number`

## 4

Required. Distance from `ref_node_id`.


`4`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-4.md "undefined#/properties/4")

### 4 Type

`number`

## 5

% grade, negative is downhill


`5`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-5.md "undefined#/properties/5")

### 5 Type

`number`

## 6

Optional. Capacity (veh/hr/ln)


`6`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-6.md "undefined#/properties/6")

### 6 Type

`integer`

## 7

Optional. Free flow speed (mph)


`7`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-7.md "undefined#/properties/7")

### 7 Type

`integer`

## 8

Optional. Number of lanes in the direction of travel (must be consistent with link lanes + lanes added).


`8`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-8.md "undefined#/properties/8")

### 8 Type

`integer`

## 9

Optional. # of lanes added on the left of the road link (negative indicates a lane drop).


`9`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-9.md "undefined#/properties/9")

### 9 Type

`integer`

## 10

Optional. # of lanes added on the left of the road link (negative indicates a lane drop).


`10`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-10.md "undefined#/properties/10")

### 10 Type

`integer`

## 11

Optional. # of lanes added on the right of the road link (negative indicates a lane drop).


`11`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-11.md "undefined#/properties/11")

### 11 Type

`integer`

## 12

Optional. Type of bicycle accommodation: unknown, none,wcl, bikelane,cycletrack,wide_shoulder, offstreet_path.


`12`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-12.md "undefined#/properties/12")

### 12 Type

`string`

## 13

Optional. Type of pedestrian accommodation:unknown,none,shoulder,sidewalk,offstreet_path.


`13`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-13.md "undefined#/properties/13")

### 13 Type

`string`

## 14

Optional. Type of parking: unknown,none,shoulder,sidewalk,offstreet_path.


`14`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-14.md "undefined#/properties/14")

### 14 Type

`string`

## 15

Optional. Set of allowed uses; comma-separated. Foreign key  to use_definition or use sets.


`15`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-15.md "undefined#/properties/15")

### 15 Type

`string`

## 16

Optional.  Toll on the link, in cents.


`16`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-16.md "undefined#/properties/16")

### 16 Type

`integer`

## 17

Optional. Optional.  Owner/operator of the link.


`17`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-17.md "undefined#/properties/17")

### 17 Type

`string`

## 18

Optional. Width (feet) of the entire right-of-way (both directions).


`18`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-18.md "undefined#/properties/18")

### 18 Type

`number`
