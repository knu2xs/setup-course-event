'''
Name:        setupClass
Purpose:     Copies all class materials from a location storing all
             materials for a specific class to C:/student/<class>.
             In this directory the script will create three
             directories.
                 ./<class>_dataStudent
                 ./<class>_dataDemo
                 ./<class>_slides

Author:      Joel McCune

Created:     21May2013
Copyright:   (c) Joel McCune 2013
Licence:
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

# import modules
import os
import shutil
import time

class Course(object):
    '''
    Represents a course, specifically the materials for a course and
    provides a method to move all the resources into a date stamped
    target directory for teaching a class.
    '''
    
    def __init__(self, name, source):
    
        # set variables
        self.name = name
        self.source = source

        # create target path with current date YYYYMMDD
        self.nameDate = name + '_' + time.strftime('%Y%m%d')
        
        # the name of the resource directories to be copied
        self.resources = []
        self.resources.append(name + '_dataDemo')
        self.resources.append(name + '_dataStudent')
        self.resources.append(name + '_slides')
        
    def copyResources(self):
        '''
        Copies everything from a source directory to a new directory
        named the class plus a timestamp in C:\Student.
        '''
        
        # output to console
        print 'Starting to copy resources for {0}'.format(name)
        
        for resource in self.resources:
            
            # create source resource path
            source = os.path.join(self.source, resource)
            
            # create destination path
            destination = os.path.join('C:', 'Student', 
                                       self.nameDate ,resource)
            
            # attempt to copy resources
            try:
                print '\nStarting to copy {0}'.format(resource)
                shutil.copytree(source, destination)
                print 'Successfully copied {0}'.format(resource)
            
            # when it does not work
            except:
                print 'Could not copy {0}'.format(resource)
                print 'Please check to ensure the target\n  directory does not already exist.'
            
if __name__ == '__main__':
    
    # get name of parent directory where script is located
    source = os.path.dirname(os.path.realpath(__file__))
    
    # the name of the parent directory is the name of the course
    name = os.path.basename(source)
    
    thisClass = Course(name, source)
    thisClass.copyResources()
    
    # pause for input before exiting
    lastline = raw_input('\nPlease press Enter to exit...')