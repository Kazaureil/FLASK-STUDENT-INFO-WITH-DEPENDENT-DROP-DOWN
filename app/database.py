from app import app, mysql

class Database(object):

	def __init__(self, uid = None, first_name = None, last_name = None, idno = None, yrlvl = None, gender = None, college = None, dept = None, course = None):
		self.uid = uid
		self.first_name = first_name
		self.last_name = last_name
		self.idno = idno
		self.yrlvl = yrlvl
		self.gender = gender
		self.college = college
		self.dept = dept
		self.course = course

	@classmethod
	def all(cls):
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM students')
		data = cur.fetchall()
		cur.close()
		return data

	@classmethod
	def course_page(cls):
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM page')
		data = cur.fetchall()
		cur.close()
		return data	

	@classmethod
	def college_dropdown(cls):
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM college')
		data = cur.fetchall()
		cur.close()
		return data

	@classmethod
	def dept_dropdown(cls):
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM department')
		data = cur.fetchall()
		cur.close()
		return data

	@classmethod
	def course_dropdown(cls):
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM course')
		data = cur.fetchall()
		cur.close()
		return data

	def add(self):
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO students(first_name, last_name, idno, yrlvl, gender, college, dept, course) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(self.first_name, self.last_name, self.idno, self.yrlvl, self.gender, self.college, self.dept, self.course))
		mysql.connection.commit()


	@classmethod
	def get_data(cls,self):
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM students WHERE uid = %s', [self])
		data = cur.fetchall()
		cur.close()
		return data


	def update_info(self, uid = None):
		cur = mysql.connection.cursor()
		cur.execute("UPDATE students SET first_name = %s, last_name = %s, idno = %s, yrlvl = %s, gender = %s, college = %s, dept = %s, course = %s WHERE uid = %s",(self.first_name, self.last_name, self.idno, self.yrlvl, self.gender, self.college, self.dept, self.course, self.uid))
		mysql.connection.commit()


	def delete_info(self, uid = None):
		cur = mysql.connection.cursor()
		cur.execute("DELETE FROM students WHERE uid = %s",[self.uid])
		mysql.connection.commit()

