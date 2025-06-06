#!/usr/bin/env python3

import os

import grass.script as gs


def run_viewshed(scanned_elev, env, **kwargs):
    gs.run_command(
        "r.viewshed",
        input=scanned_elev,
        output="scanned_elev_viewshed",
        coordinates="638728,220609",
        observer_elevation="5.0",
        overwrite="True",
    )


def main():
    env = os.environ.copy()
    env["GRASS_OVERWRITE"] = "1"
    elevation = "elev_lid792_1m"
    elev_resampled = "elev_resampled"
    gs.run_command("g.region", raster=elevation, res=4, flags="a", env=env)
    gs.run_command("r.resamp.stats", input=elevation, output=elev_resampled, env=env)

    run_viewshed(scanned_elev=elev_resampled, env=env)


if __name__ == "__main__":
    main()
