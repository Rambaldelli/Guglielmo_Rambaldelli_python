# Homology modeling by the automodel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class
log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in
# directories for input atom files
env.io.atom_files_directory = ['.', '/home/rambo/Desktop/Bioinfo/Lab1 /Casadio DROPBOX/[2]3D Modelling/MODELLER/Esercizi/Laccase']

# Read in HETATM records from template PDBs
env.io.hetatm = True


a = automodel(env,
              alnfile  = 'out.pir',     # alignment filename
              knowns   = '3kmd',    # codes of the templates
              sequence = 'tar')              # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 5                # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual homology modeling
