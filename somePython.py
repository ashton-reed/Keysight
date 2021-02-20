"""
    Run like so : python3 /path/to/scripy.py Example
"""

import os
# let's try out pathlib
from pathlib import Path
# required to use command-line arguments
import sys
 
def createFile():
 
    # but make sure the user gives us the project name!
    if len(sys.argv) != 2:
        print('Usage - python3 /path/to/script.py PROJECT_NAME')
        exit(1)
 
    # let's get the project name from CLI arguments so we can re-use this script
    proj_name = sys.argv[1]
 
    # This wasn't the path of the directory we are creating before
    proj_path = Path(f'./{proj_name}')
 
    try:
        os.mkdir(proj_name)
    except OSError:
        print(f'Creation of the directory {proj_path} failed')
    else:
        print(f'Successfully created the directory {proj_path}')
 
    # a list of the files to create
    proj_files = [ f'{proj_path}/{proj_name}.py',
                   f'{proj_path}/{proj_name}.csproj',
                   f'{proj_path}/{proj_name}.TapPlan',
                   f'{proj_path}/package.xml',
            ]


    # Don't Repeat yourself - D.R.Y.
    #for proj_file in proj_files:
    # Using "with" will close the file handle when it's done
    with open(proj_files[0], 'w') as f:
        forPy(f)
    #   pass
    with open(proj_files[1], "w") as f:
        csProj(f)
    #    pass
    with open(proj_files[2], "w") as f:
        tapPlan(f)
    #    pass
    with open(proj_files[3], "w") as f:
        packageXml(f)
    #    pass
def forPy(f):
    text = """ import OpenTap\n
    print("HelloWorld")
    class HelloWorld:
        # ToDo: Add property here for each parameter the end user should be able to change
    
    def HelloWorld():
        # ToDo: Set default values for properties / settings.
   
    def PrePlanRun():
        base.PrePlanRun()
        # ToDo: Optionally add any setup code this step needs to run before the testplan starts
 
    def Run():
        # ToDo: Add test case code here
        RunChildSteps() # If step has child steps.
        UpgradeVerdict(Verdict.Pass)
    
    def PostPlanRun():
        # ToDo: Optionally add any cleanup code this step need to run after the entire testplan has finished
        base.PostPlanRun()
    """
    f.write(text)
   
def csProj(f):
    
    text = """"
    <Project Sdk="Microsoft.NET.Sdk" ToolsVersion="Current">
    <PropertyGroup>
        <TargetFrameworkIdentifier></TargetFrameworkIdentifier>
        <TargetFrameworkVersion></TargetFrameworkVersion>
        <TargetFramework>netstandard2.0</TargetFramework>
    </PropertyGroup>
   
  <PropertyGroup>
    <OpenTapPackageDefinitionPath>package.xml</OpenTapPackageDefinitionPath>
    <CreateOpenTapPackage>false</CreateOpenTapPackage>
  </PropertyGroup>
 
  <PropertyGroup Condition="'$(Configuration)' == 'Release'">
    <CreateOpenTapPackage>true</CreateOpenTapPackage>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="OpenTAP" Version="$(OpenTapVersion)" />
  </ItemGroup>
</Project> 
"""
    f.write(text)


def tapPlan(f):
   
    text = "HELLO TAP PLAN"
        
    f.write(text)


def packageXml(f):
    text = """
<?xml version="1.0" encoding="UTF-8"?>

<!-- InfoLink: Specifies a location where additional information about the package can be found. Version: The version of the package. Must be in a semver 2.0 compatible format. This can be automatically updated from GIT. For Version the following macro is available (Only works if the project directory is under Git source control): $(GitVersion) - Gets the version from Git in the recommended format Major.Minor.Build-PreRelease+CommitHash.BranchName. -->

-<Package OS="Windows,Linux" Version="0.1.0-alpha" InfoLink="" xmlns="http://opentap.io/schemas/package" Name="HelloWorld">

<Description>This is my OpenTAP plugin package.</Description>

-<Files>

-<File SourcePath="HelloWorld.dll" Path="Packages/HelloWorld/HelloWorld.dll">

<SetAssemblyInfo Attributes="Version"/>

<!--ObfuscateWithDotfuscator/-->


</File>

</Files>

</Package>
 """
    
    f.write(text)


if __name__=='__main__':
    createFile()
 
