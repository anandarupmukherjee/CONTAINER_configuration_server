import cherrypy
import os

class FormHandler(object):
    @cherrypy.expose
    def index(self):
        return '''
            <html>
            <body>
            <form method="post" action="submit">
              
              <label for="name">Sensor:</label>
              <input type="text" name="name"><br>
              <label for="email">Threshold:</label>
              <input type="text" name="email"><br>
              
              <label for="gender">Gender:</label>
                <select name="gender">
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>

            <input type="submit" value="Submit">
            </form>
            </body>
            </html>
        '''

    @cherrypy.expose
    def submit(self, name=None, email=None, gender=None):
        if name and email and gender:
            with open(cherrypy.config.get('data_file_path', 'app/config.txt'), 'w') as f:
                f.write(f"{name},{email},{gender}\n")
            return f"Configuration set is now, {name}!"
        else:
            return "Please enter your name and email."

if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', '6080')),
        # 'DATA_FILE': os.environ.get('DATA_FILE', '/app/data.txt')
    })
    cherrypy.quickstart(FormHandler())

