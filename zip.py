# Zip the output folder

import os

output_folder = 'output'

if os.name == 'nt':  # Windows
    os.system(f'powershell "Compress-Archive -Path {output_folder} -DestinationPath {output_folder}.zip -Force"')
else:  # Linux/MacOS
    os.system(f'zip -r {output_folder}.zip {output_folder}')

print("Zip file created successfully")