import methods

#function mapping

#map each case to its corresponding function
functionMapping = {
    ("vertical displacement", "initial vertical velocity", "time"): methods.vertical_Displacement_With_Time,
    ("initial vertical velocity", "time", "vertical displacement"): methods.initial_Vertical_With_Time,
    ("time","vertical displacement", "initial vertical velocity"): methods.time_With_Vertical_Displacement,
    ("initial vertical velocity","final vertical velocity", "time"): methods.initial_Velocity_With_Time,
    ("final vertical velocity", "initial vertical velocity", "time"): methods.final_Velocity_With_Time, 
    ("time", "final vertical velocity", "initial vertical velocity"): methods.time_With_Final_Velocity,
    ("vertical displacement", "final vertical velocity", "initial vertical velocity"): methods.vertical_Displacement_With_Initial_Velocity,
    ("initial vertical velocity", "final vertical velocity", "vertical displacement"): methods.initial_Velocity_With_Final_Velocity,
    ("final vertical velocity", "initial vertical velocity", "vertical displacement"): methods.final_Velocity_With_Initial_Velocity,
    ("horizontal displacement", "horizontal velocity", "time"): methods.horizontal_Displacement_With_Time,
    ("horizontal velocity", "time, horizontal displacement"): methods.horizontal_Velocity_With_Time,
    ("time", "horizontal displacement", "horizontal velocity"): methods.time_With_Horizontal_Displacement

}