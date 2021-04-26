#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from yourturn_5_4 import WeaG

w = WeaG()


# In[ ]:


from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def wea():
    content = '''
    <form action='grab'>
        <input type="text" name="location"> <input type="submit" value="確定">
    </form>
    '''
    
    return content


# In[ ]:


@app.route('/grab')
def grab():
    loc = request.args.get('location')
    r = w.grab(loc)
    content = f'''
    <form action='grab'>
        <input type="text" name="location" value={loc}> <input type="submit" value="確定">
    </form>
    '''
    if r:
        a = f'{r["O"]} 溫度:{r["T"]:.1f}度, 濕度:{r["H"]:.0%}, 雨量:{r["R"]:.1f}mm'
    else:
        a = 'no such site!'
    content += a
    
    return content


# In[ ]:


app.run()

