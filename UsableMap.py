import methods

#map of each usable case depending on what the user is looking for

usableMapping = {
    ("vertical displacement"): [["initial vertical velocity", "time"], ["final vertical velocity", "initial vertical velocity"]],
    ("initial vertical velocity"): [["time", "vertical displacement"],["final vertical velocity", "time"],["final vertical velocity", "vertical displacement"]],
    ("time"): [["vertical displacement", "initial vertical velocity"],["final vertical velocity", "initial vertical velocity"],["horizontal displacement", "horizontal velocity"]],
    ("final vertical velocity"): [["initial vertical velocity", "time"],["initial vertical velocity", "vertical displacement"]], 
    ("horizontal displacement"): ["horizontal velocity", "time"],
    ("horizontal velocity"): ["time, horizontal displacement"],
    

}