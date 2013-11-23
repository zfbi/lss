import os,sys,jarray,time
from jarray import zeros

from java.awt import *
from java.io import *
from java.lang import *
from java.util import *
from javax.swing import *

from edu.mines.jtk.awt import *
from edu.mines.jtk.dsp import *
from edu.mines.jtk.interp import *
from edu.mines.jtk.io import *
from edu.mines.jtk.mosaic import *
from edu.mines.jtk.ogl.Gl import *
from edu.mines.jtk.opt import *
from edu.mines.jtk.sgl import *
from edu.mines.jtk.util import *
from edu.mines.jtk.util.ArrayMath import *

#from lss.dev import *
from lss.eni import *
#from lss.fault import *
#from lss.flat import *
from lss.util import *
from lss.vel import *
from lss.vel.Util import *

# Do everything on Swing thread.
def run(main):
  class RunMain(Runnable):
    def run(self):
      main(sys.argv)
  SwingUtilities.invokeLater(RunMain())
