# README

## Top-level Schemas

-   [geometry](./geometry.md "The geometry is an optional file that contains geometry information (shapepoints) for a line object") – `spec/geometry.schema.json`
-   [lane](./lane.md "The lane file allocates portions of the physical right-of-way that might be used for travel") – `spec/lane.schema.json`
-   [lane_tod](./lane_tod.md "An optional file that handles day-of-week and time-of-day restrictions on lanes that traverse entire links") – `spec/lane_tod.schema.json`
-   [link](./link.md "A link is an edge in a network, defined by the nodes it travels from and to") – `spec/link.schema.json`
-   [link_tod](./link_tod.md "Handles day-of-week and time-of-day restrictions on links") – `spec/link_tod.schema.json`
-   [location](./location.md "A location is a vertex that is associated with a specific location along a link") – `spec/location.schema.json`
-   [movement](./movement.md "Describes how inbound and outbound links connect at an intersection") – `spec/movement.schema.json`
-   [movement_tod](./movement_tod.md "Handles day-of-week and time-of-day restrictions on movements") – `spec/movement_tod.schema.json`
-   [node](./node.md "A list of vertices that locate points on a map") – `spec/node.schema.json`
-   [segment](./segment.md "A portion of a link defined by link_id,ref_node_id, start_lr, and end_lr") – `spec/segment.schema.json`
-   [segment_lane](./segment_lane.md "Defines added and dropped lanes, and changes to lane parameters") – `spec/segment_lane.schema.json`
-   [segment_lane_tod](./segment_lane_tod.md "An optional file that handles day-of-week and time-of-day restrictions on lanes within segments of links") – `spec/segment_lane_tod.schema.json`
-   [segment_tod](./segment_tod.md "An optional file that handles day-of-week and time-of-day restrictions on segments") – `spec/segment_tod.schema.json`
-   [signal_controller](./signal_controller.md "The signal controller is associated with an intersection or a cluster of intersections") – `spec/signal_controller.schema.json`
-   [signal_coordination](./signal_coordination.md "Establishes coordination for several signal controllers, associated with a timing_plan") – `spec/signal_coordination.schema.json`
-   [signal_detector](./signal_detector.md "A signal detector is associated with a controller, a phase and a group of lanes") – `spec/signal_detector.schema.json`
-   [signal_phase_mvmt](./signal_phase_mvmt.md "Associates Movements and pedestrian Links (e") – `spec/signal_phase_mvmt.schema.json`
-   [signal_timing_phase](./signal_timing_phase.md "For signalized nodes, provides signal timing and establishes phases that may run concurrently") – `spec/signal_timing_phase.schema.json`
-   [signal_timing_plan](./signal_timing_plan.md "For signalized nodes, establishes timing plans") – `spec/signal_timing_plan.schema.json`
-   [time_set_definitions](./time_set_definitions.md "The time_set_definitions file is an optional representation of time-of-day and day-of-week sets to enable time restrictions through \_tod files") – `spec/time_set_definitions.schema.json`
-   [use_definition](./use_definition.md "The Use_Definition file defines the characteristics of each vehicle type or non-travel purpose (e") – `spec/use_definition.schema.json`
-   [use_group](./use_group.md "Defines groupings of uses, to reduce the size of the Allowed_Uses lists in the other tables") – `spec/use_group.schema.json`
-   [zone](./zone.md "Locates zones (travel analysis zones, parcels) on a map") – `spec/zone.schema.json`

## Other Schemas

### Objects



### Arrays

