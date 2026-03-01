# Issue #293: Label Placement and Zoom-Out Analysis

## Root cause (placement logic)

The `updateMissionLabelPositions()` logic uses `map.latLngToContainerPoint()` and `map.containerPointToLatLng()` with a fixed 8-pixel offset. This breaks when zoomed out because of off-screen anchors, pixel-to-degree scale at low zoom, and execution order. (See prior analysis.)

## Stylization angle (to investigate)

The label **CSS and divIcon options** may also contribute:

### #293 CSS changes (map_mission_filter.css)

| Pre-#293 | #293 |
|----------|------|
| font-size: 1.3em | font-size: 1em (1.5em on hover) |
| padding-left: 20px | padding: 0 4px |
| No transform | transform: scale(1.12) on .smdb-hover |
| No transform-origin | transform-origin: left/right center |
| Simple | display: inline-block, position: relative, z-index |

### #293 divIcon options (JS)

| Pre-#293 | #293 |
|----------|------|
| No iconSize (Leaflet default) | iconSize: [280, 36] |
| No iconAnchor (Leaflet default) | iconAnchor: [0, 36] |

### Why stylization could matter

1. **iconSize [280, 36]** – Fixed pixel box. Leaflet’s marker pane scales with zoom; a fixed-size div may behave differently than auto-sized content at various zoom levels.
2. **transform: scale(1.12)** – On hover, this compounds with Leaflet’s zoom transform. `transform-origin` can change how the label appears relative to its anchor at different zoom levels.
3. **padding-left: 20px → padding: 0 4px** – Shifts where the text sits inside the icon; could affect perceived position when combined with iconAnchor.

## Isolation test results

**Test A – #293 placement + pre-#293 styling:** ✓ Zoom out works. Labels stay near tracks.

**Test B – pre-#293 placement + #293 styling:** ✗ Issue appears. Zoom out breaks label placement.

**Conclusion:** The **#293 styling** (iconSize/iconAnchor and/or the #293 CSS) causes the zoom-out bug. The #293 placement logic (northernmost point, pixel offset, zoom handler) is fine when combined with pre-#293 styling.

**Working fix:** Use #293 placement + pre-#293 label CSS (1.3em, padding-left 20px, no iconSize/iconAnchor). Commit d2bae69.
