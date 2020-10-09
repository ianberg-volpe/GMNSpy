# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [link.schema.json](../../out/link.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property  | Type      | Required | Nullable       | Defined by                                                          |
| :-------- | --------- | -------- | -------------- | :------------------------------------------------------------------ |
| [0](#0)   | `any`     | Optional | cannot be null | [Untitled schema](link-properties-0.md "undefined#/properties/0")   |
| [1](#1)   | `any`     | Optional | cannot be null | [Untitled schema](link-properties-1.md "undefined#/properties/1")   |
| [2](#2)   | `string`  | Optional | cannot be null | [Untitled schema](link-properties-2.md "undefined#/properties/2")   |
| [3](#3)   | `any`     | Optional | cannot be null | [Untitled schema](link-properties-3.md "undefined#/properties/3")   |
| [4](#4)   | `any`     | Optional | cannot be null | [Untitled schema](link-properties-4.md "undefined#/properties/4")   |
| [5](#5)   | `boolean` | Optional | cannot be null | [Untitled schema](link-properties-5.md "undefined#/properties/5")   |
| [6](#6)   | `any`     | Optional | cannot be null | [Untitled schema](link-properties-6.md "undefined#/properties/6")   |
| [7](#7)   | `any`     | Optional | cannot be null | [Untitled schema](link-properties-7.md "undefined#/properties/7")   |
| [8](#8)   | `integer` | Optional | cannot be null | [Untitled schema](link-properties-8.md "undefined#/properties/8")   |
| [9](#9)   | `number`  | Optional | cannot be null | [Untitled schema](link-properties-9.md "undefined#/properties/9")   |
| [10](#10) | `number`  | Optional | cannot be null | [Untitled schema](link-properties-10.md "undefined#/properties/10") |
| [11](#11) | `string`  | Optional | cannot be null | [Untitled schema](link-properties-11.md "undefined#/properties/11") |
| [12](#12) | `integer` | Optional | cannot be null | [Untitled schema](link-properties-12.md "undefined#/properties/12") |
| [13](#13) | `integer` | Optional | cannot be null | [Untitled schema](link-properties-13.md "undefined#/properties/13") |
| [14](#14) | `integer` | Optional | cannot be null | [Untitled schema](link-properties-14.md "undefined#/properties/14") |
| [15](#15) | `string`  | Optional | cannot be null | [Untitled schema](link-properties-15.md "undefined#/properties/15") |
| [16](#16) | `string`  | Optional | cannot be null | [Untitled schema](link-properties-16.md "undefined#/properties/16") |
| [17](#17) | `string`  | Optional | cannot be null | [Untitled schema](link-properties-17.md "undefined#/properties/17") |
| [18](#18) | `string`  | Optional | cannot be null | [Untitled schema](link-properties-18.md "undefined#/properties/18") |
| [19](#19) | `integer` | Optional | cannot be null | [Untitled schema](link-properties-19.md "undefined#/properties/19") |
| [20](#20) | `string`  | Optional | cannot be null | [Untitled schema](link-properties-20.md "undefined#/properties/20") |
| [21](#21) | `number`  | Optional | cannot be null | [Untitled schema](link-properties-21.md "undefined#/properties/21") |

## 0

Primary key – could be SharedStreets Reference ID


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Optional. The parent of this link. For example,for a sidewalk, this is the adjacent road.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Optional. Street or Path Name


`2`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link-properties-2.md "undefined#/properties/2")

### 2 Type

`string`

## 3




`3`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link-properties-3.md "undefined#/properties/3")

### 3 Type

`any`

## 4




`4`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link-properties-4.md "undefined#/properties/4")

### 4 Type

`any`

## 5

Required. Whether the link is directed (travel only occurs from the from_node to the to_node) or undirected.


`5`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [Untitled schema](link-properties-5.md "undefined#/properties/5")

### 5 Type

`boolean`

## 6

Optional. Foreign key (Link_Geometry table).


`6`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link-properties-6.md "undefined#/properties/6")

### 6 Type

`any`

## 7

Optional. Link geometry, specific format could be WKT, GeoJSON, etc.


`7`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](link-properties-7.md "undefined#/properties/7")

### 7 Type

`any`

## 8

Optional. 
1  shapepoints go from from_node to to_node;
\-1 shapepoints go in the reverse direction;
0  link is undirected or no geometry information is provided.


`8`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link-properties-8.md "undefined#/properties/8")

### 8 Type

`integer`

## 9

Optional. Length of the link in miles


`9`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](link-properties-9.md "undefined#/properties/9")

### 9 Type

`number`

## 10

% grade, negative is downhill


`10`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](link-properties-10.md "undefined#/properties/10")

### 10 Type

`number`

## 11

Facility type (e.g., freeway, arterial, etc.)


`11`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link-properties-11.md "undefined#/properties/11")

### 11 Type

`string`

## 12

Optional. Capacity (veh / hr / lane)


`12`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link-properties-12.md "undefined#/properties/12")

### 12 Type

`integer`

## 13

Optional. Free flow speed mph


`13`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link-properties-13.md "undefined#/properties/13")

### 13 Type

`integer`

## 14

Optional. Number of permanent lanes (not including turn p
pockets) in the direction of travel open to motor vehicles.
It does not include bike lanes, shoulders or parking lanes.


`14`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link-properties-14.md "undefined#/properties/14")

### 14 Type

`integer`

## 15

Optional. Type of bicycle accommodation: unknown, none, wcl, sharrow, bikelane, cycletrack, offstreet path


`15`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link-properties-15.md "undefined#/properties/15")

### 15 Type

`string`

## 16

Optional. Type of pedestrian accommodation: unknown, none, shoulder, sidewalk, offstreet path


`16`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link-properties-16.md "undefined#/properties/16")

### 16 Type

`string`

## 17

Optional. Type of parking: unknown, none, parallel, angle, other


`17`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link-properties-17.md "undefined#/properties/17")

### 17 Type

`string`

## 18

Optional. Set of allowed uses: shoulder, parking, walk, all, bike, auto, hov2, hov3, truck, bus, etc. e.g. [auto,bike]


`18`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link-properties-18.md "undefined#/properties/18")

### 18 Type

`string`

## 19

Optional.  Toll on the link, in cents.


`19`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](link-properties-19.md "undefined#/properties/19")

### 19 Type

`integer`

## 20

Optional.  Owner/operator of the link.


`20`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](link-properties-20.md "undefined#/properties/20")

### 20 Type

`string`

## 21

Optional. Width (feet) of the entire right-of-way (both directions).


`21`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](link-properties-21.md "undefined#/properties/21")

### 21 Type

`number`
