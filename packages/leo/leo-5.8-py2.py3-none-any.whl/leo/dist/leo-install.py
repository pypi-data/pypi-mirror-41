#!/usr/bin/env python
''' Postinstall housekeeping 
@url http://docs.python.org/2.7/distutils/builtdist.html#creating-windows-installers
'''
import os
import sys

def rewrite_launchers():
    '''replace `entry_points` code generated by Distribute in foo-script.py with our own '''
    path = os.path.join(sys.prefix, 'Scripts')
    
    for script in ['leoc-script.py', 'leo-script.pyw']:

        if script[-1] == 'w': pyexe = 'pythonw'
        else: pyexe = 'python'
            
        script = os.path.join(path, script)
        with open(script, 'w') as f:    
            f.write('''#!%s

""" Leo launcher script
A minimal script to launch leo.
"""

import leo.core.runLeo
leo.core.runLeo.run()
                ''' % (pyexe)
                )
                
            #register file in installed-files manifest
            file_created(script)
if sys.argv[1] == '-install':
    rewrite_launchers()
