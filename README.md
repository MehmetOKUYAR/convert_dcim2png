# Convert_Dcim2Png
 You can use dcim images to convert them to png format
 
 dcim image also contains all the patient's information. You can also access them with code
 
 ~~~
 (0002, 0000) File Meta Information Group Length  UL: 216
(0002, 0001) File Meta Information Version       OB: b'\x00\x01'
(0002, 0002) Media Storage SOP Class UID         UI: CT Image Storage
(0002, 0003) Media Storage SOP Instance UID      UI: 1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.10.0
(0002, 0010) Transfer Syntax UID                 UI: Explicit VR Little Endian
(0002, 0012) Implementation Class UID            UI: 1.3.6.1.4.1.5962.99.2
(0002, 0013) Implementation Version Name         SH: 'PIXELMEDJAVA001'
(0002, 0016) Source Application Entity Title     AE: 'CLEANER'
-------------------------------------------------
(0008, 0008) Image Type                          CS: ['ORIGINAL', 'PRIMARY', 'AXIAL']
(0008, 0012) Instance Creation Date              DA: '20060101'
(0008, 0013) Instance Creation Time              TM: '000148.000'
(0008, 0016) SOP Class UID                       UI: CT Image Storage
(0008, 0018) SOP Instance UID                    UI: 1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.10.0
(0008, 0020) Study Date                          DA: '20060101'
(0008, 0021) Series Date                         DA: '20060101'
(0008, 0022) Acquisition Date                    DA: '20060101'
(0008, 0023) Content Date                        DA: '20060101'
(0008, 0030) Study Time                          TM: '000000.000'
(0008, 0031) Series Time                         TM: '000119.000'
(0008, 0032) Acquisition Time                    TM: '000139.000'
(0008, 0033) Content Time                        TM: '000148.000'
(0008, 0050) Accession Number                    SH: '54879843'
(0008, 0060) Modality                            CS: 'CT'
(0008, 0070) Manufacturer                        LO: 'GE MEDICAL SYSTEMS'
(0008, 0090) Referring Physician's Name          PN: ''
(0008, 1030) Study Description                   LO: 'CRANE+POLYGONE'
(0008, 103e) Series Description                  LO: 'Crane SPC'
(0008, 1090) Manufacturer's Model Name           LO: 'LightSpeed Pro 32'
(0008, 1140)  Referenced Image Sequence  1 item(s) ---- 
   (0008, 1150) Referenced SOP Class UID            UI: CT Image Storage
   (0008, 1155) Referenced SOP Instance UID         UI: 1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.2.0
   ---------
(0009, 0010) Private Creator                     LO: 'GEMS_IDEN_01'
(0009, 1001) [Full fidelity]                     LO: 'CT_LIGHTSPEED'
(0009, 1002) [Suite id]                          SH: 'CT01'
(0009, 1004) [Product id]                        SH: 'LightSpeed Pro'
(0009, 1027) [Image actual date]                 SL: 1375266389
(0010, 0010) Patient's Name                      PN: 'Doe^Pierre'
(0010, 0020) Patient ID                          LO: '54879843'
(0010, 0030) Patient's Birth Date                DA: ''
(0010, 0040) Patient's Sex                       CS: 'M'
(0010, 1010) Patient's Age                       AS: '025Y'
(0012, 0062) Patient Identity Removed            CS: 'YES'
(0012, 0063) De-identification Method            LO: ['Deidentified', 'Descriptors retained', 'Patient Characteristics retained', 'Device identity removed', 'Institution identity removed', 'Dates modified', 'All private retained', 'UIDs remapped']
(0012, 0064)  De-identification Method Code Sequence  6 item(s) ---- 
   (0008, 0100) Code Value                          SH: '113100'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Basic Application Confidentiality Profile'
   ---------
   (0008, 0100) Code Value                          SH: '210005'
   (0008, 0102) Coding Scheme Designator            SH: '99PMP'
   (0008, 0104) Code Meaning                        LO: 'Retain all descriptors unchanged'
   ---------
   (0008, 0100) Code Value                          SH: '113108'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Retain Patient Characteristics Option'
   ---------
   (0008, 0100) Code Value                          SH: '113107'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Retain Longitudinal Temporal Information Modified Dates Option'
   ---------
   (0008, 0100) Code Value                          SH: '210002'
   (0008, 0102) Coding Scheme Designator            SH: '99PMP'
   (0008, 0104) Code Meaning                        LO: 'Retain all private elements'
   ---------
   (0008, 0100) Code Value                          SH: '210001'
   (0008, 0102) Coding Scheme Designator            SH: '99PMP'
   (0008, 0104) Code Meaning                        LO: 'Remap UIDs'
   ---------
(0018, 0022) Scan Options                        CS: 'HELICAL MODE'
(0018, 0050) Slice Thickness                     DS: '1.25'
(0018, 0060) KVP                                 DS: '120.0'
(0018, 0090) Data Collection Diameter            DS: '320.0'
(0018, 1020) Software Versions                   LO: '07MW18.4'
(0018, 1030) Protocol Name                       LO: '1.1 Crane Helice Sans Inj et avec Injectin-----Sans DMPR'
(0018, 1100) Reconstruction Diameter             DS: '250.0'
(0018, 1110) Distance Source to Detector         DS: '949.075012'
(0018, 1111) Distance Source to Patient          DS: '541.0'
(0018, 1120) Gantry/Detector Tilt                DS: '0.0'
(0018, 1130) Table Height                        DS: '202.5'
(0018, 1140) Rotation Direction                  CS: 'CW'
(0018, 1150) Exposure Time                       IS: '1460'
(0018, 1151) X-Ray Tube Current                  IS: '146'
(0018, 1152) Exposure                            IS: '13'
(0018, 1160) Filter Type                         SH: 'HEAD FILTER'
(0018, 1170) Generator Power                     IS: '36000'
(0018, 1190) Focal Spot(s)                       DS: '0.7'
(0018, 1210) Convolution Kernel                  SH: 'SOFT'
(0018, 5100) Patient Position                    CS: 'HFS'
(0018, 9305) Revolution Time                     FD: 0.800000011920929
(0018, 9306) Single Collimation Width            FD: 0.625
(0018, 9307) Total Collimation Width             FD: 20.0
(0018, 9309) Table Speed                         FD: 13.281249802093956
(0018, 9310) Table Feed per Rotation             FD: 10.625
(0018, 9311) Spiral Pitch Factor                 FD: 0.53125
(0019, 0010) Private Creator                     LO: 'GEMS_ACQU_01'
(0019, 1002) [Detector Channel]                  SL: 912
(0019, 1003) [Cell number at Theta]              DS: '389.75'
(0019, 1004) [Cell spacing]                      DS: '1.0239'
(0019, 100f) [Horiz. Frame of ref.]              DS: '695.5'
(0019, 1011) [Series contrast]                   SS: 0
(0019, 1018) [First scan ras]                    LO: 'I'
(0019, 101a) [Last scan ras]                     LO: 'S'
(0019, 1023) [Table Speed [mm/rotation]]         DS: '10.625'
(0019, 1024) [Mid Scan Time [sec]]               DS: '1.019512'
(0019, 1025) [Mid scan flag]                     SS: 1
(0019, 1026) [Tube Azimuth [degree]]             SL: 355
(0019, 1027) [Rotation Speed [msec]]             DS: '0.8'
(0019, 102c) [Number of triggers]                SL: 15023
(0019, 102e) [Angle of first view]               DS: '0.0'
(0019, 102f) [Trigger frequency]                 DS: '1230.0'
(0019, 1039) [SFOV Type]                         SS: 2049
(0019, 1042) [Segment Number]                    SS: 0
(0019, 1043) [Total Segments Required]           SS: 0
(0019, 1047) [View compression factor]           SS: 1
(0019, 1052) [Recon post proc. Flag]             SS: 1
(0019, 106a) [Dependent on #views processed]     SS: 4
(0020, 000d) Study Instance UID                  UI: 1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.3.0
(0020, 000e) Series Instance UID                 UI: 1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.7.0
(0020, 0010) Study ID                            SH: ''
(0020, 0011) Series Number                       IS: '2'
(0020, 0012) Acquisition Number                  IS: '1'
(0020, 0013) Instance Number                     IS: '4'
(0020, 0032) Image Position (Patient)            DS: [-125.000, -134.800, -5.750]
(0020, 0037) Image Orientation (Patient)         DS: [1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000]
(0020, 0052) Frame of Reference UID              UI: 1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.5.0
(0020, 1040) Position Reference Indicator        LO: 'OM'
(0020, 1041) Slice Location                      DS: '-5.75'
(0021, 0010) Private Creator                     LO: 'GEMS_RELA_01'
(0021, 1003) [Series from which Prescribed]      SS: 2
(0021, 1035) [Series from which prescribed]      SS: 1
(0021, 1036) [Image from which prescribed]       SS: 1
(0021, 1091) [Biopsy position]                   SS: 0
(0021, 1092) [Biopsy T location]                 FL: 0.0
(0021, 1093) [Biopsy ref location]               FL: 0.0
(0023, 0010) Private Creator                     LO: 'GEMS_STDY_01'
(0023, 1070) [Start time(secs) in first axial]   FD: 1375266409.036882
(0027, 0010) Private Creator                     LO: 'GEMS_IMAG_01'
(0027, 1010) [Scout Type]                        SS: 0
(0027, 101c) [Vma mamp]                          SL: 0
(0027, 101e) [Vma mod]                           SL: 0
(0027, 101f) [Vma clip]                          SL: 65
(0027, 1020) [Smart scan ON/OFF flag]            SS: 2
(0027, 1035) [Plane Type]                        SS: 2
(0027, 1042) [Center R coord of plane image]     FL: 0.0
(0027, 1043) [Center A coord of plane image]     FL: 9.800000190734863
(0027, 1044) [Center S coord of plane image]     FL: -5.75
(0027, 1045) [Normal R coord]                    FL: 0.0
(0027, 1046) [Normal A coord]                    FL: -0.0
(0027, 1047) [Normal S coord]                    FL: 1.0
(0027, 1050) [Scan Start Location]               FL: 0.0
(0027, 1051) [Scan End Location]                 FL: 0.0
(0028, 0002) Samples per Pixel                   US: 1
(0028, 0004) Photometric Interpretation          CS: 'MONOCHROME2'
(0028, 0010) Rows                                US: 512
(0028, 0011) Columns                             US: 512
(0028, 0030) Pixel Spacing                       DS: [0.488281, 0.488281]
(0028, 0100) Bits Allocated                      US: 16
(0028, 0101) Bits Stored                         US: 16
(0028, 0102) High Bit                            US: 15
(0028, 0103) Pixel Representation                US: 1
(0028, 0120) Pixel Padding Value                 SS: -2000
(0028, 1050) Window Center                       DS: '40.0'
(0028, 1051) Window Width                        DS: '100.0'
(0028, 1052) Rescale Intercept                   DS: '-1024.0'
(0028, 1053) Rescale Slope                       DS: '1.0'
(0028, 1054) Rescale Type                        LO: 'HU'
(0040, 0244) Performed Procedure Step Start Date DA: '20060101'
(0040, 0245) Performed Procedure Step Start Time TM: '000000.000'
(0040, 0254) Performed Procedure Step Descriptio LO: 'CRANE+POLYGONE'
(0043, 0010) Private Creator                     LO: 'GEMS_PARM_01'
(0043, 1010) [Window value]                      US: 100
(0043, 1012) [X-ray chain]                       SS: [99, 99, 99]
(0043, 1016) [Number of overranges]              SS: 0
(0043, 101e) [Delta Start Time [msec]]           DS: '0.289431'
(0043, 101f) [Max overranges in a view]          SL: 0
(0043, 1021) [Corrected after glow terms]        SS: 0
(0043, 1025) [Reference channels]                SS: [0, 0, 0, 0, 0, 0]
(0043, 1026) [No views ref chans blocked]        US: [0, 0, 0, 0]
(0043, 1027) [Scan Pitch Ratio]                  SH: '0.531:1'
(0043, 1028) [Unique image iden]                 OB: b'00'
(0043, 102b) [Private Scan Options]              SS: [4, 0, 1, 0]
(0043, 1031) [Recon Center Coordinates]          DS: [0.000000, 9.800000]
(0043, 1040) [Trigger on position]               FL: 100.26629638671875
(0043, 1041) [Degree of rotation]                FL: 5495.76513671875
(0043, 1042) [DAS trigger source]                SL: 0
(0043, 1043) [DAS fpa gain]                      SL: 0
(0043, 1044) [DAS output source]                 SL: 0
(0043, 1045) [DAS ad input]                      SL: 0
(0043, 1046) [DAS cal mode]                      SL: 0
(0043, 104d) [Start scan to X-ray on delay]      FL: 0.0
(0043, 104e) [Duration of X-ray on]              FL: 12.213821411132812
(0043, 1064) [Image Filter]                      CS: ''
(0045, 0010) Private Creator                     LO: 'GEMS_HELIOS_01'
(0045, 1001) [Number of Macro Rows in Detector]  SS: 32
(0045, 1002) [Macro width at ISO Center]         FL: 0.625
(0045, 1003) [DAS type]                          SS: 14
(0045, 1004) [DAS gain]                          SS: 4
(0045, 1006) [Table Direction]                   CS: 'OUT OF GANTRY'
(0045, 1007) [Z smoothing Factor]                FL: 0.0
(0045, 1008) [View Weighting Mode]               SS: 0
(0045, 1009) [Sigma Row number]                  SS: 0
(0045, 100a) [Minimum DAS value]                 FL: 0.0
(0045, 100b) [Maximum Offset Value]              FL: 0.0
(0045, 100c) [Number of Views shifted]           SS: 0
(0045, 100d) [Z tracking Flag]                   SS: 0
(0045, 100e) [Mean Z error]                      FL: 0.0
(0045, 100f) [Z tracking Error]                  FL: 0.0
(0045, 1010) [Start View 2A]                     SS: 0
(0045, 1011) [Number of Views 2A]                SS: 0
(0045, 1012) [Start View 1A]                     SS: 0
(0045, 1013) [Sigma Mode]                        SS: 0
(0045, 1014) [Number of Views 1A]                SS: 0
(0045, 1015) [Start View 2B]                     SS: 0
(0045, 1016) [Number Views 2B]                   SS: 0
(0045, 1017) [Start View 1B]                     SS: 0
(0045, 1018) [Number of Views 1B]                SS: 0
(0045, 1021) [Iterbone Flag]                     SS: 1
(0045, 1022) [Perisstaltic Flag]                 SS: 0
(0045, 1032) [TemporalResolution]                FL: 1.46016263961792
(0045, 103b) [NoiseReductionImageFilterDesc]     LO: ''
(7fe0, 0010) Pixel Data                          OW: Array of 524288 elements
~~~~~~~~~~
 

### Run the application

The input parameters can be changed using the command line :
~~~
multi_dcm_to_png.py -i <input_dir> -o <output_dir>
~~~~~~~~~
For running example :
~~~~
python3 multi_dcm_to_png.py -i images_dcm/ -o images_png/
~~~~~~~~~

### Example Output

<img src="https://github.com/MehmetOKUYAR/convert_dcim2png/blob/main/images_png/1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.10.0.png" alt="1" width = 480 height = 360px >
