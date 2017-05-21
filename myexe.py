from distutils.core import setup
import py2exe

setup(
        console=['tcping.py'],
        name="synsping",
        options={
            'py2exe': {
            	'compressed': 1,
                'bundle_files': 3, 
                'packages': ['six','prettytable'] 
            } 
        }
    )
