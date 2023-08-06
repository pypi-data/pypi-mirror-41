Changelog
=========


1.0.0 (2019-02-07)
------------------

- changed to version 1.0.0 as this release is no more backwards compatible.
  [iham]

- fixed robot tests for Plone 5.1.x
  [iham]

- removed css hacks as the break css validation and ie6/7 are of no importants anymore.
  [iham]

- made responsive slides a pattern itself.
  [iham]

- refactored responsive slides to become resource & bundle
  [iham]

- refactored dynamic form resources and bundling.
  [iham]

- add and setup extra `[mosaic]` to pull in mosaic in one go.
  [jensens]

- Fixed dependency chain in `metadata.xml` and reinstall of mosaic and other dependency-roundtrips.
  [iham, jensens]

- On uninstall remove values from registry.
  [jensens]

- Minimal contained buildout overhaul.
  [jensens]

- Compile Resources in order to make it work with Plone 5.1.4.
  [jensens]


0.4 (2017-12-01)
----------------

- Only return link for related items, not the image (like) object itself.
  [tmassman]

- Add link (if available) to responsiveslides.js slider.
  [tmassman]

- Add styling for captions on responsiveslides.js slider.
  [tmassman]


0.3 (2017-12-01)
----------------

- Add custom widget for content selection.
  [tmassman]

- Register JS resources (pattern) and bundle.
  [tmassman]


0.2 (2017-11-27)
----------------

- Remove allow_fullscreen setting.
  [tmassman]


0.1 (2017-11-27)
----------------

- Initial release.
  [tmassman]

- Added responsiveslides.js based slider.
  [tmassman]
