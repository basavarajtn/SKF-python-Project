Feature: Verify all the options are present in the Bearing type dropdown

    @smoke
    Scenario Outline:
        Then All the below listed option should be visable "<BearingList>"
        Examples:
            | BearingList |
            |Insert bearing (Y-bearing)        |
            |Angular contact ball bearing     |
            |Self-aligning ball bearing       |
            |Cylindrical roller bearings       |
            |Needle roller bearings            |
            |Tapered roller bearings           |
            |Spherical roller bearings         |
            |CARB toroidal roller bearings     |
            |Thrust ball bearings              |
            |Cylindrical roller thrust bearings|
            |Needle roller thrust bearings     |
            |Spherical roller thrust bearings  |
            |Track roller                      |
            |Deep groove ball bearings         |

    @smoke
    Scenario:
        Then All the below listed option should be visable
        | BearingList                     |
        |Insert bearing (Y-bearing)        |
        |Angular contact ball bearing     |
        |Self-aligning ball bearing       |
        |Cylindrical roller bearings       |
        |Needle roller bearings            |
        |Tapered roller bearings           |
        |Spherical roller bearings         |
        |CARB toroidal roller bearings     |
        |Thrust ball bearings              |
        |Cylindrical roller thrust bearings|
        |Needle roller thrust bearings     |
        |Spherical roller thrust bearings  |
        |Track roller                      |
        |Deep groove ball bearings         |
