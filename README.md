KSP-addon-version-checker
=========================

A simple program that allow people to check their add-ons folder for updates.

How-to use
===
Modders
---

* Include a *.version file somewhere inside GameData (probably in your folder, but anywhere will do)
  * Use example.version and KSP-AVC.version as an example.
* Host your *.version file somewhere online so that we can compare players' local version against your up-to-date online version.

Players
---

* Install python, Run `python main.py`. (OS X and Linux come with python by default in most cases)
  * This will create a configuration file in `~/.KSP-AVC`.
  * Then it will check through your GameData folder to try to figure out which mods you have and whether they're up to date
  * Currently KSP-AVC will not check any mods that do not have a `<module_name>.version` file, please help your favorite mod maintainers with this (be a good citizen, try to help instead of nagging!)

FAQ
===

Q. What is this *.version file in my GameData directory? Where did it come from?
A. That file is used to declare which version of a mod you're using. It contains enough information for our script to check online to see if there are any new versions of the mod.

Q. This mod doesn't contain a *.version file? How can I fix that?
A. Politely ask the mod maintainer, or even better, send them a completed version file and point them at this FAQ.

Q. Why don't you include a link to KSP-AVC in the version file to help advertise?
A. We wanted to create a file that any mod or script author would feel comfortable using. We felt it was important to ensure that other scripters, and possibly better programmers than we are, could use this work to build something really, really awesome. Who knows, maybe even Squad might be able to use this info to help with Spaceport! In the end, we care more about whether our mods are up-to-date than we do about being the authors of a script that everyone uses. 
