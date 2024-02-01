import methods

#function mapping

#map each case to its corresponding function
functionMapping = {
    ("initial vertical velocity", "time", "vertical displacement"): methods.vertical_Displacement_With_Time,
    ("time", "vertical displacement", "initial vertical velocity"): methods.initial_Vertical_With_Time,
    ("vertical displacement", "initial vertical velocity", "time"): methods.time_With_Vertical_Displacement,
    ("final vertical velocity", "time", "initial vertical velocity"): methods.initial_Velocity_With_Time,
    ("initial vertical velocity", "time", "final vertical velocity"): methods.final_Velocity_With_Time,
    ("final vertical velocity", "initial vertical velocity", "time"): methods.time_With_Final_Velocity,
    ("final vertical velocity", "initial vertical velocity", "vertical displacement"): methods.vertical_Displacement_With_Initial_Velocity,
    ("final vertical velocity", "vertical displacement", "initial vertical velocity"): methods.initial_Velocity_With_Final_Velocity,
    ("initial vertical velocity", "vertical displacement", "final vertical velocity"): methods.final_Velocity_With_Initial_Velocity,
    ("horizontal velocity", "time", "horizontal displacement"): methods.horizontal_Displacement_With_Time,
    ("time, horizontal displacement", "horizontal velocity"): methods.horizontal_Velocity_With_Time,
    ("horizontal displacement", "horizontal velocity", "time"): methods.time_With_Horizontal_Displacement

}