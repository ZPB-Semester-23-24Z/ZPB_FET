
import sys
sys.path.append('src/measurement')
sys.path.append('src/fr')


from measurement import *
from fr import *


fr=fr()
fr.read()
df=fr.get_df()

m=measurement()
m.load(df)

print(m.vgs_sweep.VGS)


