# Use cases for the LHCb Software configuration database

## Introduction

The LHCb Software Configuration Database (SDB) is repository for metadata concerning the LHCb software, with the goal to ease the management and release of the software artefacts, as well as their long term preservation.

## Actors

  - *Project Managers*: are in charge of tagging and releasing the software projects
  - *Users*: any member of LHCb using the software
  - *Release shifters*: in charge of releasing the software artefacts to the production system
  - *Continuous Integration system*: In charge of building the software artefacts from source

## Use cases

### 1. Importing a new project into the software configuration database

Actors: *Project Manager*

When a *Project Manager* releases a new version of a software project, she/he tags the project using the version and then proceeds to import it into the SDB. The import command inserts the new version of the project into the SDB, and links it with the project/versions it depends on.

The command also sets a flags on this new project/version that marks it as ready for release.

This step requires authentication/authorization and can be run from a specific host/cluster (e.g. lxplus) if needed.

N.B. It is not sure whether sliding dependencies (i.e. on v* or vXr* is actually needed).

### 2. Grouping projects to release into consistent stacks

Actors: *Continuous Integration system*

When several projects are being released at the same time, they cannot be build independently as they may depend on each other. Furthermore, the build systems needs to know for which configuration the projects should be built; to do so, the SDB groups the project versions to release in connected subgraphs where all nodes need release, and considering the "bottom" of the stack (i.e. projects depending on already released artefacts), take the intersection of:
  - the platforms for which the already released artefacts have been released.
  - the platforms for which the *Project Managers* or *Release shifters* have explicitly requested release.

The continuous integration system does not have credentials, so reading the stack list should be doable without any specific credentials

### 3. Mark a project stack as release

Actors: *Release shifters*

Once software artefacts have been released to the production repositories, they have to be marked as released by the *Release shifter* in charge (in order to avoid rebuilding them).

This step requires authentication/authorization and can be run from a specific host/cluster (e.g. lxplus) if needed.

### 4. Manual operations on imported software projects

Actors: *Project Manager* or *Release shifters*

Set/Unset the *release request* flag
Set the list of platforms requested for release

This step requires authentication/authorization and can be run from a specific host/cluster (e.g. lxplus) if needed.

### 5. List software stacks and information about projects

Actors:ALL

List information about project, display all projects depending on a given one (or the ones it depends on), output as a dot file is useful.

No credentials should be needed for this operation.

### 6. Set metadata about where to find the source for a given project

Actors: *Release shifter*

Set metadata on a project or project/version about where to get the source code (sourceuri). The syntax is:

system-identifier:group/project

e.g. the description of the Panoramix project is

```
"PANORAMIX": {
        "project": "PANORAMIX",
        "sourceuri": "gitlab-cern:lhcb/Panoramix"
    },
```


This step requires authentication/authorization and can be run from a specific host/cluster (e.g. lxplus) if needed.

### 7. Dumping project metadata to a file on disk

Actors: *Release shifter*

For offline use, we need to have the complete list of know projects (independently of versions), and where to get the source code from a version control system.


No credentials should be needed for this operation.