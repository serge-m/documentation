## mono_ultrasonic.vi
<p align="center">
<img src="https://github.com/monoDriveIO/client/raw/master/WikiPhotos/LV_client/sensors/mono__ultrasonicc.png" 
width="400"  />
</p>

### Description 
Configures and sample the ultrasonic sensor according to the configuration setting.

### Inputs

- **monoDrive (Ctl):** The custom ctl for monoDrive.
- **error in (Error Cluster):** Can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.


### Outputs

- **Ultrasonic Ranges:** Output the distances in meters of the object detected.
- **error out (Error Cluster):** Can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.