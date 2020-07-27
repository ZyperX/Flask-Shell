from flask import *
import subprocess
app=Flask(__name__)
@app.route("/",methods=['post','get'])
def start():
 cmds=""
 op=""
 if request.method=='POST':
  cmds=request.form.get('cmd')
  pss=cmds.split()
  try:
   op=subprocess.check_output(pss)
   op=op.split()
   if len(op) >1 :
    op=['\n']+op
  except:
   op=['Unknown Command']
 return render_template('temp.html',message=cmds,output=op)

app.run()
