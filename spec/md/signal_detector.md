# signal_detector Schema

```txt
spec/signal_detector.schema.json
```

A signal detector is associated with a phase and a group of lanes.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_detector.schema.json](../../out/signal_detector.schema.json "open original schema") |

## signal_detector Type

unknown ([signal_detector](signal_detector.md))

# signal_detector Properties

| Property                            | Type      | Required | Nullable       | Defined by                                                                                                                      |
| :---------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| [detector_id](#detector_id)         | `any`     | Required | cannot be null | [signal_detector](signal_detector-properties-detector_id.md "spec/signal_detector.schema.json#/properties/detector_id")         |
| [signal_phase_id](#signal_phase_id) | `any`     | Required | cannot be null | [signal_detector](signal_detector-properties-signal_phase_id.md "spec/signal_detector.schema.json#/properties/signal_phase_id") |
| [link_id](#link_id)                 | `any`     | Required | cannot be null | [signal_detector](signal_detector-properties-link_id.md "spec/signal_detector.schema.json#/properties/link_id")                 |
| [start_lane](#start_lane)           | `integer` | Required | cannot be null | [signal_detector](signal_detector-properties-start_lane.md "spec/signal_detector.schema.json#/properties/start_lane")           |
| [end_lane](#end_lane)               | `integer` | Optional | cannot be null | [signal_detector](signal_detector-properties-end_lane.md "spec/signal_detector.schema.json#/properties/end_lane")               |
| [ref_node_id](#ref_node_id)         | `any`     | Required | cannot be null | [signal_detector](signal_detector-properties-ref_node_id.md "spec/signal_detector.schema.json#/properties/ref_node_id")         |
| [det_zone_lr](#det_zone_lr)         | `number`  | Required | cannot be null | [signal_detector](signal_detector-properties-det_zone_lr.md "spec/signal_detector.schema.json#/properties/det_zone_lr")         |
| [det_zone_front](#det_zone_front)   | `number`  | Optional | cannot be null | [signal_detector](signal_detector-properties-det_zone_front.md "spec/signal_detector.schema.json#/properties/det_zone_front")   |
| [det_type](#det_type)               | `string`  | Optional | cannot be null | [signal_detector](signal_detector-properties-det_type.md "spec/signal_detector.schema.json#/properties/det_type")               |

## detector_id

Primary key.


`detector_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-detector_id.md "spec/signal_detector.schema.json#/properties/detector_id")

### detector_id Type

`any`

## signal_phase_id

Required. Foreign key to signal_phase table.


`signal_phase_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-signal_phase_id.md "spec/signal_detector.schema.json#/properties/signal_phase_id")

### signal_phase_id Type

`any`

## link_id

Foreign key. The link covered by the detector.


`link_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-link_id.md "spec/signal_detector.schema.json#/properties/link_id")

### link_id Type

`any`

## start_lane

Left-most lane covered by the detector.


`start_lane`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-start_lane.md "spec/signal_detector.schema.json#/properties/start_lane")

### start_lane Type

`integer`

## end_lane

Right-most lane covered by the detector (blank if only one lane).


`end_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-end_lane.md "spec/signal_detector.schema.json#/properties/end_lane")

### end_lane Type

`integer`

## ref_node_id

The detector is on the approach to this node.


`ref_node_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-ref_node_id.md "spec/signal_detector.schema.json#/properties/ref_node_id")

### ref_node_id Type

`any`

## det_zone_lr

Required. Distance from from reference node to detector.


`det_zone_lr`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-det_zone_lr.md "spec/signal_detector.schema.json#/properties/det_zone_lr")

### det_zone_lr Type

`number`

## det_zone_front

Optional. Linear reference of front of detection zone.


`det_zone_front`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-det_zone_front.md "spec/signal_detector.schema.json#/properties/det_zone_front")

### det_zone_front Type

`number`

## det_type

Optional. Type of detector.


`det_type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [signal_detector](signal_detector-properties-det_type.md "spec/signal_detector.schema.json#/properties/det_type")

### det_type Type

`string`
