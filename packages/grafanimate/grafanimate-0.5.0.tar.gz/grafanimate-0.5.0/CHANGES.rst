#####################
grafanimate changelog
#####################


in progress
===========


2019-02-04 0.5.0
================
- Add "5 minute" and "30 minute" intervals
- Decrease frame rate to 2 fps when rendering using ffmpeg
- Add luftdaten.info to attribution area on leaflet map widget
- Add LDI NYE shot scenario
- Fix missing dependency to the "Munch" package
- Fix "ptrace" Makefile target for uploading renderings
- Add "grafana-start" Makefile target
- Prevent stalling of Grafana Studio Javascript when waiting for data arrival
  of all panels when actually rendering a single panel only.
- Deactivate default attribution of luftdaten.info for map panels
- Improve documentation


2018-12-28 0.4.1
================
- Update documentation


2018-12-28 0.4.0
================
- Add parameters ``--panel-id``, ``--header-layout`` and ``--datetime-format``
- Refactor some parts of the machinery
- Increase time to wait for Browser starting up
- Improve interval handling
- Pick reasonable timeframe for "cdc_maps" example scenario
- Improve timing for heavy dashboards
- Add Makefile target for uploading to web space
- Refactor the machinery
- Get dashboard title from Grafana runtime scope for deriving the output filename from
- Properly produce .mp4 and .gif artifacts
- Fix window size wrt. ffmpeg animated gif rendering
- Add quick hack to remove specific panel from specific dashboard
- Add option --header-layout=no-folder to omit folder name from dashboard title
- Reduce gap for scenario "ldi_with_gaps"


2018-12-27 0.3.0
================
- Fix missing ``grafana-sidecar.js`` file in Python sdist package
- Add intervals "secondly", "minutely" and "yearly". Thanks, weef!
- Improve date formatting and separation of concerns
- Add sanity checks, improve logging
- Fix croaking when initially opening dashboard with "from=0&to=0" parameters
- Optimize user interface for wide dashboad names
- Fix stalling on row-type panel objects
- Don't initially run "onPanelRefresh"?
- Update documentation


2018-12-26 0.2.0
================
- Pretend to be a real program. Happy testing!


2018-12-25 0.1.0
================
- Add proof of concept for wrapping Grafana and adjusting its
  time range control, i.e. navigating the time dimension
