setup-course-event
==================

When teaching technical classes, resources need to be moved to a temporary location on a regular basis. The resources in this repository make this job easier.

The script depends on a predefined directory structure. The parent directory for the script should be the name of the class. In this directory there should be three directories, one for each resource type. These resources include demonstration data, student data and slides, with the directories respectively named <classname>_dataDemo, <classname>_dataStudent, and <classname>_slides.

The script will create a directory in C:\Student following the convention of <classname>_<timestamp>. The timestamp will be in the form of YYYYMMDD. In this way, each event will have a unique directory. Also, if teaching multiple events consecutively of the same class, the directories will organize consecutively. This organization makes it easier to identify which resources to use and also which to clean up following an event.
